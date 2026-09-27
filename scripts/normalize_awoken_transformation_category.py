#!/usr/bin/env python3
"""Normalize the canonical Awoken transformation index without violating the skill schema.

Stage forms (SS2/SS3, Super Vegeta 2, Kaioken x3/x20) are documented as stages of
parent Awoken records and are not separate canonical records in this index.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
ROSTER = ROOT / "docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json"

PARENT_ROSTER = [
    "Super Saiyan", "Super Vegeta", "Future Super Saiyan", "Super Saiyan God",
    "Super Saiyan God Super Saiyan", "Super Saiyan God Super Saiyan (Evolved)",
    "Kaioken", "Potential Unleashed", "Beast", "Ultra Instinct", "Turn Golden",
    "Purification", "Become Giant", "Power Pole Pro", "The Power to Overcome",
]
RACE_BY_NAME = {
    "Super Saiyan": "Saiyan", "Super Vegeta": "Saiyan", "Future Super Saiyan": "Saiyan",
    "Super Saiyan God": "Saiyan", "Super Saiyan God Super Saiyan": "Saiyan",
    "Super Saiyan God Super Saiyan (Evolved)": "Saiyan", "Kaioken": "Universal",
    "Potential Unleashed": "Universal", "Beast": "Universal", "Ultra Instinct": "Universal",
    "Turn Golden": "Frieza Race", "Purification": "Majin", "Become Giant": "Namekian",
    "Power Pole Pro": "Earthling", "The Power to Overcome": "Universal",
}


def main() -> int:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
    roster = json.loads(ROSTER.read_text(encoding="utf-8"))["canonical_transformation_roster"]
    if set(PARENT_ROSTER) - set(roster):
        raise SystemExit("Awoken roster correction is missing a parent transformation.")
    records = [r for r in data.get("records", []) if not (r.get("class") == "Awoken" and r.get("subcategory") == "Race")]
    source = "docs/data/awoken-research-batches/awoken-batch-07-canonical-roster-correction.json"
    for name in PARENT_ROSTER:
        records.append({
            "name": name,
            "class": "Awoken",
            "subcategory": "Race",
            "verification_status": "partially_verified",
            "research_status": "partially_enriched",
            "usable_by_cac": True,
            "race_restriction": RACE_BY_NAME[name],
            "sources": [source],
        })
    data["records"] = sorted(records, key=lambda r: (r.get("name", "").casefold(), r.get("class", ""), r.get("subcategory", "")))
    data.setdefault("category_counts", {})["Transformations"] = len(PARENT_ROSTER)
    data.setdefault("target_category_counts", {})["Transformations"] = len(PARENT_ROSTER)
    data["awoken_transformation_category"] = {
        "status": "normalized",
        "record_count": len(PARENT_ROSTER),
        "individual_forms_documented": len(roster),
        "source": source,
        "note": "Schema-valid canonical records use Awoken/Race. Stage forms are documented as parent-chain stages and are not duplicate canonical records."
    }
    SKILLS.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Normalized Transformation index to {len(PARENT_ROSTER)} parent Awoken records ({len(roster)} individual forms documented).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
