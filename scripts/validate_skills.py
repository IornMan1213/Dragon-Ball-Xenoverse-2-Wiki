#!/usr/bin/env python3
"""Validate the canonical XV2 skills JSON against repository schema rules."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data" / "skills.json"
SCHEMA = ROOT / "docs" / "data" / "skills.schema.json"
ALLOWED_CLASS = {"Super", "Ultimate", "Evasive", "Awoken", "Mixed", "Counter"}
ALLOWED_SUB = {"Ki Blast", "Strike", "Power Up", "Other", "Race", "Special", "Counter"}
ALLOWED_STATUS = {"indexed", "partially_verified", "verified"}
ALLOWED_RESEARCH = {"indexed", "partially_enriched", "enriched", "page_unavailable"}


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert schema["title"] == "Dragon Ball Xenoverse 2 Skill Record"
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise SystemExit("skills.json must contain a non-empty records array")

    seen = set()
    for i, r in enumerate(records):
        for key in ("name", "class", "subcategory", "verification_status", "sources"):
            if key not in r:
                raise SystemExit(f"record {i} missing required field: {key}")
        if not isinstance(r["name"], str) or not r["name"].strip():
            raise SystemExit(f"record {i} has invalid name")
        if r["class"] not in ALLOWED_CLASS or r["subcategory"] not in ALLOWED_SUB:
            raise SystemExit(f"record {i} has invalid class/subcategory")
        if r["verification_status"] not in ALLOWED_STATUS:
            raise SystemExit(f"record {i} has invalid verification_status")
        if r.get("research_status") and r["research_status"] not in ALLOWED_RESEARCH:
            raise SystemExit(f"record {i} has invalid research_status")
        if not isinstance(r["sources"], list) or not r["sources"]:
            raise SystemExit(f"record {i} must contain at least one source")
        key = (r["name"].casefold(), r["class"], r["subcategory"])
        if key in seen:
            raise SystemExit(f"duplicate record: {key}")
        seen.add(key)

    counts = data.get("category_counts", {})
    if not isinstance(counts, dict) or not counts:
        raise SystemExit("category_counts is missing or empty")
    if any(not isinstance(v, int) or v < 0 for v in counts.values()):
        raise SystemExit("category_counts contains an invalid value")

    expected = data.get("record_count")
    if expected is not None and expected != len(records):
        raise SystemExit(f"record_count={expected} does not match records={len(records)}")

    print(f"Validated {len(records)} skill records across {len(counts)} categories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
