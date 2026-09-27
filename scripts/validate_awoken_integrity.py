#!/usr/bin/env python3
"""Validate that promoted Awoken research remains present in the canonical catalog."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
OVERRIDES = ROOT / "docs/data/awoken-canonical-overrides.json"

def canonical_key(record: object, label: str) -> tuple[str, str, str]:
    if not isinstance(record, dict):
        raise SystemExit(f"{label} must be an object")
    values = tuple(record.get(field) for field in ("name", "class", "subcategory"))
    if any(not isinstance(value, str) or not value.strip() for value in values):
        raise SystemExit(f"{label} name/class/subcategory must be non-empty strings")
    return (values[0].casefold(), values[1], values[2])


def main() -> int:
    try:
        skills = json.loads(SKILLS.read_text(encoding="utf-8"))
        overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Awoken source JSON invalid: {exc}")
    if not isinstance(skills, dict) or not isinstance(overrides, dict):
        raise SystemExit("Awoken source roots must be objects")
    skill_records = skills.get("records")
    override_records = overrides.get("records")
    if not isinstance(skill_records, list) or not isinstance(override_records, list):
        raise SystemExit("skills.records and awoken overrides.records must be lists")
    records = {}
    for i, record in enumerate(skill_records):
        key = canonical_key(record, f"skills.records[{i}]")
        if key in records:
            raise SystemExit(f"duplicate canonical Awoken identity: {key}")
        records[key] = record
    promoted = 0
    missing = []
    mismatches = []
    for i, expected in enumerate(override_records):
        target = records.get(canonical_key(expected, f"awoken overrides.records[{i}]"))
        if target is None:
            missing.append(expected.get("name", "<unnamed>"))
            continue
        promoted += 1
        for field, value in expected.items():
            if field in {"name", "class", "subcategory", "sources"}:
                continue
            if target.get(field) != value:
                mismatches.append({"name": expected.get("name"), "field": field, "expected": value, "actual": target.get(field)})
    if missing or mismatches:
        print(f"Awoken integrity failure: promoted={promoted}, missing={len(missing)}, mismatches={len(mismatches)}")
        if missing:
            print("Missing: " + ", ".join(missing))
        for item in mismatches[:20]:
            print(f"Mismatch: {item['name']} / {item['field']}: expected={item['expected']!r} actual={item['actual']!r}")
        return 1
    print(f"Awoken integrity validated: {promoted} promoted records match canonical overrides.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
