import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const dataDir = path.join(root, 'docs', 'data');
const failures = [];
const warnings = [];

const files = [
  'equipment-accessories-record-layer.json',
  'accessory-pq-research.json',
  'accessory-pq-reconciliation-157-168.json',
  'accessory-pq-audit-169-186.json',
  'accessory-shop-research.json',
  'accessory-raid-gift-reconciliation.json',
  'accessory-wish-special-reconciliation.json',
  'accessory-canonicalization-audit.json',
];

const statusValues = new Set(['indexed', 'partially_verified', 'verified']);
const excludedStatuses = new Set(['excluded_non_accessory', 'checked_no_accessory_in_basic_reward_extract', 'checked_no_accessory_in_current_basic_reward_extract', 'not_safely_promoted_from_current_checked_extract']);

function readJson(filename) {
  const file = path.join(dataDir, filename);
  if (!fs.existsSync(file)) {
    failures.push(`${filename}: missing file`);
    return null;
  }
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    failures.push(`${filename}: invalid JSON (${error.message})`);
    return null;
  }
}

function records(payload) {
  return Array.isArray(payload?.records) ? payload.records.filter(Boolean) : [];
}

const loaded = new Map();
for (const filename of files) loaded.set(filename, readJson(filename));

const crossLayer = new Map();
for (const [filename, payload] of loaded) {
  for (const record of records(payload)) {
    const name = String(record.name ?? record.canonical_name ?? record.accessory ?? '').trim();
    if (!name) continue;
    const key = name.toLocaleLowerCase();
    if (!crossLayer.has(key)) crossLayer.set(key, { name, files: [] });
    const entry = crossLayer.get(key);
    if (!entry.files.includes(filename)) entry.files.push(filename);

    const status = record.verification_status ?? record.status;
    if (status && !statusValues.has(status) && !excludedStatuses.has(status)) {
      failures.push(`${filename}: ${name}: invalid verification status '${status}'`);
    }

    if (record.sources !== undefined && (!Array.isArray(record.sources) || record.sources.length === 0)) {
      warnings.push(`${filename}: ${name}: empty sources`);
    }
  }
}

for (const [key, entry] of crossLayer) {
  if (entry.files.length > 1) {
    warnings.push(`cross-layer match candidate: ${entry.name} -> ${entry.files.join(', ')}`);
  }
}

for (const [filename, payload] of loaded) {
  const rows = records(payload);
  const ids = new Map();
  const names = new Map();
  for (const [index, record] of rows.entries()) {
    if (record.id) {
      const id = String(record.id);
      if (ids.has(id)) failures.push(`${filename}: duplicate id '${id}' at records ${ids.get(id)} and ${index}`);
      else ids.set(id, index);
    }
    const name = String(record.name ?? record.canonical_name ?? record.accessory ?? '').trim().toLocaleLowerCase();
    if (name) {
      if (names.has(name)) warnings.push(`${filename}: duplicate name '${name}' at records ${names.get(name)} and ${index}; verify whether these are alternate routes or duplicate identities`);
      else names.set(name, index);
    }
  }
}

const pqAudit = loaded.get('accessory-pq-audit-169-186.json');
for (const record of records(pqAudit)) {
  const pq = record.pq;
  if (!Number.isInteger(pq) || pq < 169 || pq > 186) failures.push(`accessory-pq-audit-169-186.json: invalid PQ '${pq}'`);
  for (const item of record.accessories ?? []) {
    if (/\b(clothes?|costume|suit|gi|uniform)\b/i.test(item)) {
      failures.push(`accessory-pq-audit-169-186.json: clothing-like item incorrectly classified as accessory: '${item}'`);
    }
  }
}

const pqReconciliation = loaded.get('accessory-pq-reconciliation-157-168.json');
for (const record of records(pqReconciliation)) {
  const status = record.status;
  if (status === 'excluded_non_accessory' && record.accessory && !/\b(clothes?|costume|suit|gi|uniform)\b/i.test(record.accessory)) {
    warnings.push(`accessory-pq-reconciliation-157-168.json: '${record.accessory}' is excluded as non-accessory without an obvious clothing marker; review manually`);
  }
}

const canonical = loaded.get('accessory-canonicalization-audit.json');
const intentional = new Set();
for (const row of canonical?.intentional_non_merges ?? []) {
  for (const item of row.items ?? []) intentional.add(String(item).toLocaleLowerCase());
}
for (const item of intentional) {
  if (!crossLayer.has(item)) warnings.push(`intentional non-merge is not currently present in a loaded layer: '${item}'`);
}

console.log(`Accessory audit: ${failures.length} failure(s), ${warnings.length} warning(s), ${crossLayer.size} distinct normalized names observed across loaded layers.`);
for (const message of failures) console.error(`FAIL: ${message}`);
for (const message of warnings.slice(0, 200)) console.warn(`WARN: ${message}`);
if (warnings.length > 200) console.warn(`WARN: ${warnings.length - 200} additional warnings omitted`);
process.exitCode = failures.length ? 1 : 0;
