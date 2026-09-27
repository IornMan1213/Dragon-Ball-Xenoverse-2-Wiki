#!/usr/bin/env python3
"""Validate the canonical Super Soul endpoint record layer.

This validator checks deterministic identity/schema invariants only. It never
infers mechanics or acquisition data and never removes canonical PQ edges.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "docs/data/super-souls-record-layer.json"
REL = ROOT / "docs/data/pq-reward-relationships.json"

def main() -> int:
    layer = json.loads(LAYER.read_text(encoding="utf-8"))
    rel = json.loads(REL.read_text(encoding="utf-8"))
    records = layer.get("records")
    if not isinstance(records, list):
        raise SystemExit("records must be a list")
    ids = [r.get("id") for r in records if isinstance(r, dict)]
    names = [r.get("name") for r in records if isinstance(r, dict)]
    if len(records) != len(ids) or any(not isinstance(x, str) or not x for x in ids):
        raise SystemExit("every record must have a non-empty string id")
    if len(set(ids)) != len(ids):
        raise SystemExit("duplicate Super Soul ids")
    if any(not isinstance(x, str) or not x for x in names):
        raise SystemExit("every record must have a non-empty string name")
    if len(set(names)) != len(names):
        raise SystemExit("duplicate Super Soul names")
    required = {"id","name","verification_status","sources"}
    for i, record in enumerate(records):
        missing = required - record.keys()
        if missing:
            raise SystemExit(f"record {i} missing required fields: {sorted(missing)}")
        if record["verification_status"] not in {"indexed","partially_verified","verified"}:
            raise SystemExit(f"record {record['id']} has invalid verification_status")
        if not isinstance(record["sources"], list) or not record["sources"]:
            raise SystemExit(f"record {record['id']} must have at least one source")
    targets = {
        row["target"] for row in rel.get("verified_relationships", [])
        if isinstance(row, dict) and row.get("relationship") == "pq_rewards_super_soul"
    }
    missing_targets = sorted(targets - set(names))
    print(json.dumps({
        "record_count": len(records),
        "unique_ids": len(set(ids)),
        "unique_names": len(set(names)),
        "canonical_pq_super_soul_targets": len(targets),
        "canonical_targets_without_endpoint": missing_targets,
        "status": "passed" if not missing_targets else "passed_with_enrichment_gaps",
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
