#!/usr/bin/env python3
"""Normalize the canonical Transformation category to the current CaC Awoken roster."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
ROSTER = ROOT / "docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json"

RACE_BY_NAME = {
    "Super Saiyan": "Saiyan", "Super Saiyan 2": "Saiyan", "Super Saiyan 3": "Saiyan",
    "Super Vegeta": "Saiyan", "Super Vegeta 2": "Saiyan", "Future Super Saiyan": "Saiyan",
    "Super Saiyan God": "Saiyan", "Super Saiyan God Super Saiyan": "Saiyan",
    "Super Saiyan God Super Saiyan (Evolved)": "Saiyan", "Kaioken": None,
    "Kaioken x3": None, "Kaioken x20": None, "Potential Unleashed": None,
    "Beast": None, "Ultra Instinct": None, "Turn Golden": "Frieza Race",
    "Purification": "Majin", "Become Giant": "Namekian", "Power Pole Pro": "Earthling",
    "The Power to Overcome": None,
}


def key(r: dict) -> tuple[str, str, str]:
    return (str(r.get("name", "")).casefold(), str(r.get("class", "")), str(r.get("subcategory", "")))


def main() -> int:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    roster = json.loads(ROSTER.read_text(encoding="utf-8"))["canonical_transformation_roster"]
    wanted = {name.casefold(): name for name in roster}
    records = data.get("records", [])
    # Remove stale Transformation-category entries only; Race research records are separate.
    records = [r for r in records if not (r.get("class") == "Awoken" and r.get("subcategory") == "Transformation")]
    source = "docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json"
    for name in roster:
        record = {
            "name": name,
            "class": "Awoken",
            "subcategory": "Transformation",
            "verification_status": "partially_verified",
            "research_status": "curated_batch",
            "usable_by_cac": True,
            "sources": [source],
        }
        race = RACE_BY_NAME.get(name)
        if race:
            record["race_restriction"] = race
        records.append(record)
    data["records"] = sorted(records, key=lambda r: (r.get("name", "").casefold(), r.get("class", ""), r.get("subcategory", "")))
    data.setdefault("category_counts", {})["Transformations"] = len(roster)
    data.setdefault("target_category_counts", {})["Transformations"] = len(roster)
    data["awoken_transformation_category"] = {
        "status": "normalized",
        "record_count": len(roster),
        "source": source,
        "note": "Transformation-category records are membership/index records. Detailed mechanics and acquisition are carried by the audited Awoken research records and promotion layer."
    }
    SKILLS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Normalized Transformation category to {len(roster)} CaC Awoken records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
