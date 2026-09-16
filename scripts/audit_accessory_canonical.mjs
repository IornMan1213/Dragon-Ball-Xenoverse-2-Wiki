#!/usr/bin/env node
import fs from 'node:fs';

const file = 'docs/data/accessory-canonical-reconciliation.json';
const data = JSON.parse(fs.readFileSync(file, 'utf8'));
const errors = [];
const warnings = [];
const ids = new Set();
const names = new Map();
const allowed = new Set(['indexed', 'partially_verified', 'verified']);

for (const record of data.records ?? []) {
  if (!record.id || ids.has(record.id)) errors.push(`duplicate/missing id: ${record.id ?? '<missing>'}`);
  ids.add(record.id);
  if (!record.canonical_name) errors.push(`${record.id}: missing canonical_name`);
  if (record.canonical_name) {
    if (names.has(record.canonical_name)) warnings.push(`duplicate canonical name: ${record.canonical_name}`);
    names.set(record.canonical_name, record.id);
  }
  if (!allowed.has(record.status)) errors.push(`${record.id}: invalid status ${record.status}`);
  if (!Array.isArray(record.routes) || record.routes.length === 0) errors.push(`${record.id}: no acquisition routes`);
  if (!Array.isArray(record.aliases)) errors.push(`${record.id}: aliases must be an array`);
}

const aliasOwner = new Map();
for (const record of data.records ?? []) {
  for (const alias of record.aliases ?? []) {
    if (aliasOwner.has(alias)) errors.push(`alias belongs to multiple records: ${alias}`);
    aliasOwner.set(alias, record.id);
  }
}

for (const group of data.unresolved_alias_groups ?? []) {
  if (!group.group || !Array.isArray(group.terms) || !group.reason) errors.push('malformed unresolved alias group');
}

if (errors.length) {
  console.error('Accessory canonical audit failed:');
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}
console.log(`Accessory canonical audit passed: ${data.records.length} canonical records, ${aliasOwner.size} unique aliases.`);
if (warnings.length) {
  console.log('Warnings:');
  for (const warning of warnings) console.log(`- ${warning}`);
}
