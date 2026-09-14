import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const dataDir = path.join(root, 'docs', 'data');
const batchDir = path.join(dataDir, 'skill-catalog-batches');
const failures = [];
const warnings = [];

function readJson(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    failures.push(`${path.relative(root, file)}: invalid JSON (${error.message})`);
    return null;
  }
}

const canonicalFile = path.join(dataDir, 'skills.json');
const verifiedFile = path.join(dataDir, 'verified-skills.json');
const canonical = readJson(canonicalFile);
const verified = readJson(verifiedFile);

if (!canonical) failures.push('Canonical skills database is unavailable.');
if (!verified) failures.push('Verified skills database is unavailable.');

const records = [];
for (const record of canonical?.records ?? []) records.push({ ...record, origin: 'canonical' });
for (const record of verified?.records ?? []) records.push({ ...record, origin: 'verified' });

if (fs.existsSync(batchDir)) {
  for (const filename of fs.readdirSync(batchDir).filter(name => name.endsWith('.json')).sort()) {
    const file = path.join(batchDir, filename);
    const batch = readJson(file);
    if (!batch) continue;
    if (!batch.category || !batch.source || !Array.isArray(batch.records)) {
      failures.push(`${path.relative(root, file)}: batch requires category, source and records[]`);
      continue;
    }
    if (Number.isInteger(batch.count) && batch.count !== batch.records.length) {
      failures.push(`${path.relative(root, file)}: count=${batch.count} but records=${batch.records.length}`);
    }
    if (!batch.source.startsWith('http')) warnings.push(`${path.relative(root, file)}: source is not an HTTP URL`);
    for (const name of batch.records) records.push({ name, class: batch.category, origin: filename });
  }
}

const seen = new Map();
for (const record of records) {
  const key = `${record.name}|${record.class ?? ''}|${record.subcategory ?? ''}`.toLowerCase();
  if (seen.has(key)) {
    const previous = seen.get(key);
    warnings.push(`duplicate candidate: ${record.name} [${record.origin}] also appears in ${previous}`);
  } else {
    seen.set(key, record.origin);
  }
  if (!record.name) failures.push(`${record.origin}: record has no name`);
}

if (canonical?.category_counts) {
  for (const [category, expected] of Object.entries(canonical.category_counts)) {
    const matching = records.filter(record => record.origin === `${category}.json` || record.class === category || record.subcategory === category);
    if (expected < 0) failures.push(`${category}: negative expected count`);
    if (!matching.length) warnings.push(`${category}: no directly attributable loaded batch records; category may rely on canonical seed data`);
  }
}

console.log(`Skill/data audit: ${failures.length} failure(s), ${warnings.length} warning(s)`);
for (const message of failures) console.error(`FAIL: ${message}`);
for (const message of warnings.slice(0, 100)) console.warn(`WARN: ${message}`);
if (warnings.length > 100) console.warn(`WARN: ${warnings.length - 100} additional warnings omitted`);
process.exitCode = failures.length ? 1 : 0;
