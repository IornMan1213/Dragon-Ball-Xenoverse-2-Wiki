#!/usr/bin/env python3
"""Validate canonical Partner Customization skill relationships and character endpoints."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = ROOT / "docs/data/partner-skill-relationships.json"
SKILLS = ROOT / "docs/data/skills.json"
BRIDGE = ROOT / "docs/data/characters/character-id-identity-bridge.json"

def main() -> int:
    rel = json.loads(REL.read_text(encoding="utf-8"))
    skills = json.loads(SKILLS.read_text(encoding="utf-8"))
    bridge = json.loads(BRIDGE.read_text(encoding="utf-8"))

    skill_ids = {row["id"] for row in skills["records"]}
    canonical_names = {row["canonical_character_name"] for row in bridge["records"]}
    failures: list[str] = []
    relationships = rel.get("relationships", [])
    if not isinstance(relationships, list):
        failures.append("relationships must be a list")
        relationships = []
    elif len(relationships) != 3:
        failures.append(f"unexpected relationship count: {len(relationships)} (expected 3)")
    seen: set[tuple[str, str]] = set()

    if rel.get("schema_version") != "1.0":
        failures.append("unexpected relationship schema_version")
    if rel.get("relationship_type") != "partner_customization":
        failures.append("unexpected relationship_type")
    if bridge.get("schema_version") != "1.0.0":
        failures.append("unexpected character bridge schema_version")

    for row in relationships:
        if not isinstance(row, dict):
            failures.append(f"relationship record must be an object: {row!r}")
            continue
        key = (row.get("skill_id", ""), row.get("partner_name", ""))
        if row.get("skill_id") not in skill_ids:
            failures.append(f"unknown canonical skill_id: {row.get('skill_id')}")
        if row.get("partner_name") not in canonical_names:
            failures.append(f"unknown canonical partner_name: {row.get('partner_name')}")
        if key in seen:
            failures.append(f"duplicate relationship: {key}")
        seen.add(key)
        if row.get("relationship") != "custom_partner_availability":
            failures.append(f"unexpected relationship: {row.get('relationship')}")
        evidence = row.get("evidence", [])
        if not isinstance(evidence, list):
            failures.append(f"evidence must be a list: {key}")
            evidence = []
        if not evidence:
            failures.append(f"missing evidence: {key}")
        for evidence_path in evidence:
            if not isinstance(evidence_path, str) or not evidence_path.strip():
                failures.append(f"invalid evidence path value: {key}: {evidence_path!r}")
                continue
            if not (ROOT / evidence_path).is_file():
                failures.append(f"missing evidence file: {key}: {evidence_path}")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        return 1

    print(
        f"PASS: {len(relationships)} partner/custom relationships; "
        f"canonical skill IDs, canonical partner names, uniqueness, relationship types, "
        f"and evidence paths all resolve."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
