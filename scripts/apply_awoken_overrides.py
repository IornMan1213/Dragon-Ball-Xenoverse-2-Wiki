#!/usr/bin/env python3
"""Apply researched Awoken overrides after the exhaustive skills catalog build."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
OVERRIDES = ROOT / "docs/data/awoken-canonical-overrides.json"


def key(record: dict) -> tuple[str, str, str]:
    return (str(record.get("name", "")).casefold(), str(record.get("class", "")), str(record.get("subcategory", "")))


def main() -> int:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    records = data.get("records", [])
    by_key = {key(r): r for r in records}

    applied = 0
    missing = []
    for override in overrides.get("records", []):
        target = by_key.get(key(override))
        if target is None:
            missing.append(override.get("name", "<unnamed>"))
            continue
        for field, value in override.items():
            if field not in {"name", "class", "subcategory"}:
                target[field] = value
        target.setdefault("sources", [])
        target["sources"] = list(dict.fromkeys(target["sources"] + [
            "docs/data/awoken-canonical-overrides.json"
        ]))
        applied += 1

    data["awoken_promotion"] = {
        "status": "applied",
        "source": "docs/data/awoken-canonical-overrides.json",
        "applied_records": applied,
        "missing_records": missing,
    }
    data["generated"] = "2026-09-17"
    data["status"] = "research-enriched"
    SKILLS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Applied {applied} Awoken overrides; missing={len(missing)}")
    if missing:
        print("Missing canonical targets:")
        for name in missing:
            print(f"- {name}")
    return 0 if not missing else 2


if __name__ == "__main__":
    raise SystemExit(main())
