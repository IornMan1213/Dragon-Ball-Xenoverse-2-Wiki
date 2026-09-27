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

    failures: list[str] = []
    if not isinstance(rel, dict):
        failures.append("relationship source must be an object")
        rel = {}
    if not isinstance(skills, dict):
        failures.append("skills source must be an object")
        skills = {}
    if not isinstance(bridge, dict):
        failures.append("character bridge source must be an object")
        bridge = {}
    skill_records = skills.get("records")
    bridge_records = bridge.get("records")
    if not isinstance(skill_records, list):
        failures.append("skills.records must be a list")
        skill_records = []
    if not isinstance(bridge_records, list):
        failures.append("character bridge records must be a list")
        bridge_records = []
    if any(not isinstance(row, dict) for row in skill_records):
        failures.append("every canonical skill record must be an object")
    if any(not isinstance(row, dict) for row in bridge_records):
        failures.append("every character bridge record must be an object")
    skill_id_values = [row.get("id") for row in skill_records if isinstance(row, dict)]
    bridge_name_values = [row.get("canonical_character_name") for row in bridge_records if isinstance(row, dict)]
    from collections import Counter
    valid_skill_id_values = [value for value in skill_id_values if isinstance(value, str) and value.strip()]
    valid_bridge_name_values = [value for value in bridge_name_values if isinstance(value, str) and value.strip()]
    duplicate_skill_ids = sorted(k for k,v in Counter(valid_skill_id_values).items() if v > 1)
    duplicate_bridge_names = sorted(k for k,v in Counter(valid_bridge_name_values).items() if v > 1)
    skill_ids = set(valid_skill_id_values)
    canonical_names = set(valid_bridge_name_values)
    if len(valid_skill_id_values) != len(skill_id_values):
        failures.append("canonical skill IDs must be non-empty strings")
    if duplicate_skill_ids:
        failures.append(f"duplicate canonical skill IDs: {duplicate_skill_ids}")
    if len(valid_bridge_name_values) != len(bridge_name_values):
        failures.append("canonical partner names must be non-empty strings")
    if duplicate_bridge_names:
        failures.append(f"duplicate canonical partner names: {duplicate_bridge_names}")
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
