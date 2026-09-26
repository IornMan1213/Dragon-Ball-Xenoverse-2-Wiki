#!/usr/bin/env python3
"""Validate canonical Partner Customization skill relationships."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REL=ROOT/"docs/data/partner-skill-relationships.json"
SKILLS=ROOT/"docs/data/skills.json"
def main()->int:
    rel=json.loads(REL.read_text(encoding="utf-8"))
    skills=json.loads(SKILLS.read_text(encoding="utf-8"))
    ids={row["skill_id"] for row in skills}
    failures=[]; seen=set()
    assert rel["schema_version"]=="1.0"
    assert rel["relationship_type"]=="partner_customization"
    for row in rel["relationships"]:
        key=(row["skill_id"],row["partner_name"])
        if row["skill_id"] not in ids: failures.append(f"unknown canonical skill_id: {row['skill_id']}")
        if key in seen: failures.append(f"duplicate relationship: {key}")
        seen.add(key)
        if row.get("relationship")!="custom_partner_availability": failures.append(f"unexpected relationship: {row.get('relationship')}")
        if not row.get("evidence"): failures.append(f"missing evidence: {key}")
    if failures:
        for x in failures: print("FAIL:",x)
        return 1
    print(f"PASS: {len(rel['relationships'])} partner/custom skill relationships; all targets canonical and unique.")
    return 0
if __name__=="__main__": raise SystemExit(main())
