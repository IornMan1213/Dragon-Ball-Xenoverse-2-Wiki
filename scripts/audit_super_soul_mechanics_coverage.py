#!/usr/bin/env python3
"""Audit Super Soul mechanics-field coverage against the canonical record layer.

This is a deterministic coverage audit only. It does not infer mechanics,
convert secondary evidence into canonical facts, or modify records.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "docs/data/super-souls-record-layer.json"

FIELDS = (
    "trigger_condition",
    "effect_text",
    "effect_magnitude",
    "duration",
    "stacking_behavior",
    "limit_burst",
    "limit_burst_trigger",
    "limit_burst_effect",
    "usable_by_cac",
    "race_restriction",
    "dlc_requirement",
)

def populated(value) -> bool:
    return value is not None and value != ""

def main() -> int:
    try:
        layer = json.loads(LAYER.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"{LAYER}: invalid JSON: {exc}")
    if not isinstance(layer, dict):
        raise SystemExit("Super Soul record layer root must be an object")
    records = layer.get("records")
    if not isinstance(records, list):
        raise SystemExit("records must be a list")
    coverage = {}
    if any(not isinstance(record, dict) for record in records):
        raise SystemExit("every Super Soul record must be an object")
    for field in FIELDS:
        count = sum(populated(record.get(field)) for record in records)
        coverage[field] = {"populated": count, "missing": len(records) - count}
    print(json.dumps({
        "record_count": len(records),
        "fields": coverage,
        "status": "passed_with_partial_mechanics_coverage",
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
