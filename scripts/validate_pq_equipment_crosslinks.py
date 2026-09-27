#!/usr/bin/env python3
"""Validate the canonical PQ -> equipment consumer projection without changing data."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = ROOT / "docs/data/pq-reward-relationships.json"
ENDPOINTS = [
    ROOT / "docs/data/equipment-accessories-record-layer.json",
    ROOT / "docs/data/equipment-record-layer.json",
]

def fail(msg):
    raise SystemExit(f"ERROR: {msg}")

def load_object(path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path}: invalid JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{path}: root must be an object")
    return value

rel = load_object(REL)
rows = rel.get("verified_relationships")
if not isinstance(rows, list):
    fail("pq-reward-relationships.json: verified_relationships must be a list")

equipment_rows = []
for row in rows:
    if not isinstance(row, dict):
        continue
    if row.get("relationship") == "pq_rewards_equipment":
        equipment_rows.append(row)

if not equipment_rows:
    fail("No canonical pq_rewards_equipment relationships found")

bad = []
keys = []
targets = []
for i, row in enumerate(equipment_rows):
    pq, target, status, source = row.get("pq"), row.get("target"), row.get("status"), row.get("source")
    if not isinstance(pq, str) or not pq:
        bad.append(f"row {i}: pq must be non-empty string")
    if not isinstance(target, str) or not target:
        bad.append(f"row {i}: target must be non-empty string")
    if not isinstance(status, str) or not status:
        bad.append(f"row {i}: status must be non-empty string")
    if not isinstance(source, str) or not source.strip():
        bad.append(f"row {i}: source must be non-empty string")
    if isinstance(pq, str):
        if not (pq.startswith("pq-") and pq[3:].isdigit() and 1 <= int(pq[3:]) <= 186):
            bad.append(f"row {i}: pq must match pq-001 through pq-186")
    if isinstance(status, str) and status not in {"verified", "inferred", "uncertain"}:
        bad.append(f"row {i}: unsupported relationship status: {status!r}")
    if isinstance(pq, str) and isinstance(target, str):
        keys.append((pq, target))
        targets.append(target)

if len(keys) != len(set(keys)):
    bad.append("duplicate canonical pq/target relationship keys detected")

endpoint_names = []
for path in ENDPOINTS:
    obj = load_object(path)
    records = obj.get("records")
    if not isinstance(records, list):
        bad.append(f"{path}: records must be a list")
        continue
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            bad.append(f"{path}: record {i} must be an object")
            continue
        name = record.get("name")
        if not isinstance(name, str) or not name:
            bad.append(f"{path}: record {i} name must be a non-empty string")
            continue
        endpoint_names.append(name)

if len(endpoint_names) != len(set(endpoint_names)):
    bad.append("duplicate endpoint equipment names detected")

unique_targets = sorted(set(targets))
endpoint_set = set(endpoint_names)
matched = sorted(set(unique_targets) & endpoint_set)
gaps = sorted(set(unique_targets) - endpoint_set)

if bad:
    for msg in bad:
        print(f"FAIL: {msg}")
    raise SystemExit(1)

print(json.dumps({
    "canonical_edges": len(equipment_rows),
    "unique_targets": len(unique_targets),
    "endpoint_records": len(endpoint_names),
    "endpoint_identity_matches": len(matched),
    "endpoint_identity_gaps": len(gaps),
    "status": "passed",
}, indent=2))
