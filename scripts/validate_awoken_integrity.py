#!/usr/bin/env python3
"""Validate that promoted Awoken research remains present in the canonical catalog."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
OVERRIDES = ROOT / "docs/data/awoken-canonical-overrides.json"

KEY = lambda r: (str(r.get("name", "")).casefold(), str(r.get("class", "")), str(r.get("subcategory", "")))


def main() -> int:
    skills = json.loads(SKILLS.read_text(encoding="utf-8"))
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    records = {KEY(r): r for r in skills.get("records", [])}
    promoted = 0
    missing = []
    mismatches = []
    for expected in overrides.get("records", []):
        target = records.get(KEY(expected))
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
