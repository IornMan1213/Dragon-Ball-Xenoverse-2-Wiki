#!/usr/bin/env python3
"""Validate current Expert Mission skill acquisition endpoint parity.

This validator treats docs/data/skill-acquisition-index.json and
docs/data/expert-mission-endpoints.json as the current machine-readable
Expert Mission acquisition layers. Historical audit snapshots are not used
as current baselines.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
ACQ = ROOT / "docs/data/skill-acquisition-index.json"
ENDPOINTS = ROOT / "docs/data/expert-mission-endpoints.json"

EXPECTED_SKILLS = 470
EXPECTED_EMS = 18
EXPECTED_EM_RANGE = set(range(3, 21))


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    skills = load(SKILLS)
    acq = load(ACQ)
    endpoints = load(ENDPOINTS)

    skill_rows = skills.get("skills", skills if isinstance(skills, list) else [])
    acq_rows = acq["records"]
    endpoint_rows = endpoints["endpoints"]

    skill_ids = {row.get("id") for row in skill_rows if row.get("id")}
    acq_ids = {row.get("skill_id") for row in acq_rows if row.get("skill_id")}
    endpoint_ids = {
        skill_id
        for row in endpoint_rows
        for skill_id in row.get("skills", [])
        if skill_id
    }
    em_numbers = {row["expert_mission"] for row in endpoint_rows}

    duplicate_acq_skill_ids = len(acq_ids) != len([r["skill_id"] for r in acq_rows])
    duplicate_endpoint_ids = len(endpoint_rows) != len({r["id"] for r in endpoint_rows})
    unresolved_acq_ids = sorted(acq_ids - skill_ids)
    endpoint_skill_ids_missing = sorted(endpoint_ids - skill_ids)
    acq_endpoint_mismatch = sorted(acq_ids ^ endpoint_ids)

    checks = {
        "canonical_skill_count": len(skill_rows) == EXPECTED_SKILLS,
        "acquisition_record_count": len(acq_rows) == EXPECTED_EMS,
        "endpoint_record_count": len(endpoint_rows) == EXPECTED_EMS,
        "expert_mission_range": em_numbers == EXPECTED_EM_RANGE,
        "no_duplicate_acquisition_skill_ids": not duplicate_acq_skill_ids,
        "no_duplicate_endpoint_ids": not duplicate_endpoint_ids,
        "all_acquisition_skill_ids_canonical": not unresolved_acq_ids,
        "all_endpoint_skill_ids_canonical": not endpoint_skill_ids_missing,
        "acquisition_endpoint_skill_set_parity": not acq_endpoint_mismatch,
    }

    print(json.dumps({
        "canonical_skill_count": len(skill_rows),
        "expert_mission_acquisition_records": len(acq_rows),
        "expert_mission_endpoint_records": len(endpoint_rows),
        "expert_mission_numbers": sorted(em_numbers),
        "unique_acquisition_skill_ids": len(acq_ids),
        "unique_endpoint_skill_ids": len(endpoint_ids),
        "unresolved_acquisition_skill_ids": unresolved_acq_ids,
        "unresolved_endpoint_skill_ids": endpoint_skill_ids_missing,
        "acquisition_endpoint_skill_set_mismatch": acq_endpoint_mismatch,
        "checks": checks,
        "status": "pass" if all(checks.values()) else "fail",
    }, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
