#!/usr/bin/env python3
"""Apply researched Awoken overrides and regenerate the deterministic skill index."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
INDEX = ROOT / "docs/data/skills-index.json"
OVERRIDES = ROOT / "docs/data/awoken-canonical-overrides.json"
INDEX_FIELDS = ("name", "class", "subcategory", "verification_status", "research_status", "sources")


def key(record: dict) -> tuple[str, str, str]:
    values = (record.get("name"), record.get("class"), record.get("subcategory"))
    if any(not isinstance(value, str) or not value.strip() for value in values):
        raise ValueError("Awoken identity fields must be non-empty strings")
    return (values[0].casefold(), values[1], values[2])


def rebuild_index(data: dict) -> None:
    records = sorted(
        data.get("records", []),
        key=lambda r: (str(r.get("name", "")).casefold(), str(r.get("class", "")), str(r.get("subcategory", ""))),
    )
    data["records"] = records
    INDEX.write_text(
        json.dumps(
            {
                "schema_version": data.get("schema_version", "1.2"),
                "source_index": data.get("source_index"),
                "generated": data.get("generated"),
                "category_counts": data.get("category_counts", {}),
                "target_category_counts": data.get("target_category_counts", {}),
                "record_count": len(records),
                "records": [{field: r[field] for field in INDEX_FIELDS if field in r} for r in records],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    try:
        data = json.loads(SKILLS.read_text(encoding="utf-8"))
        overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Awoken override application failed: invalid JSON: {exc}")
        return 1
    if not isinstance(data, dict) or not isinstance(overrides, dict):
        print("Awoken override application failed: source roots must be objects")
        return 1
    records = data.get("records", [])
    override_records = overrides.get("records", [])
    if not isinstance(records, list) or not isinstance(override_records, list):
        print("Awoken override application failed: records containers must be lists")
        return 1
    try:
        by_key = {key(r): r for r in records}
    except ValueError as exc:
        print(f"Awoken override application failed: {exc}")
        return 1

    applied = 0
    missing = []
    for override in override_records:
        target = by_key.get(key(override))
        if target is None:
            missing.append(override.get("name", "<unnamed>"))
            continue
        for field, value in override.items():
            if field not in {"name", "class", "subcategory"}:
                target[field] = value
        target.setdefault("sources", [])
        target["sources"] = list(dict.fromkeys(target["sources"] + ["docs/data/awoken-canonical-overrides.json"]))
        applied += 1

    data["awoken_promotion"] = {
        "status": "applied_with_missing_stage_targets" if missing else "applied",
        "source": "docs/data/awoken-canonical-overrides.json",
        "applied_records": applied,
        "missing_records": missing,
        "note": "Missing targets are reported for audit; staged forms may be represented only through parent transformation records in the generated catalog."
    }
    data["generated"] = "2026-09-17"
    data["status"] = "research-enriched"
    rebuild_index(data)
    SKILLS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Applied {applied} Awoken overrides; missing={len(missing)}; regenerated deterministic skill index.")
    if missing:
        print("Missing canonical targets:")
        for name in missing:
            print(f"- {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
