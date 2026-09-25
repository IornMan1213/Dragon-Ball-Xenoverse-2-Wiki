#!/usr/bin/env python3
"""Validate PQ-facing summary/reference consumer contracts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = ROOT / "docs/data/pq-reward-relationships.json"
PQ_LAYER = ROOT / "docs/data/parallel-quests-record-layer.json"

CONSUMERS = {
    "guides": ROOT / "docs/Guides.md",
    "skills_database": ROOT / "docs/Skills-Database.md",
    "skills_complete_database": ROOT / "docs/Skills-Complete-Database.md",
    "skill_unlock_database": ROOT / "docs/Skills-Unlock-Database.md",
    "qq_bangs": ROOT / "docs/QQ-Bangs.md",
    "farming_hub": ROOT / "docs/Farming-Hub.md",
    "farming_routes": ROOT / "docs/Farming-Routes.md",
    "equipment_database": ROOT / "docs/Equipment-Database.md",
    "accessory_pq_database": ROOT / "docs/Accessory-PQ-Database.md",
}

EXPECTED_RELATIONSHIP_COUNTS = {
    "pq_rewards_skill": 244,
    "pq_rewards_super_soul": 145,
    "pq_rewards_equipment": 124,
    "pq_features_character": 247,
    "pq_requires_dlc": 86,
    "pq_farming_route": 7,
}

EXPECTED_FARMING_PQS = {15, 22, 44, 45, 68, 83, 88}

def main() -> int:
    relationships = json.loads(REL.read_text(encoding="utf-8")).get("verified_relationships", [])
    pq_records = json.loads(PQ_LAYER.read_text(encoding="utf-8")).get("records", [])
    pq_ids = {int(r["number"]) for r in pq_records if str(r.get("number", "")).isdigit()}

    relationship_counts = {
        key: sum(1 for row in relationships if row.get("relationship") == key)
        for key in EXPECTED_RELATIONSHIP_COUNTS
    }
    farming_pqs = {
        int(str(row["pq"]).split("-")[-1])
        for row in relationships
        if row.get("relationship") == "pq_farming_route" and str(row.get("pq", "")).isdigit()
    }

    checks = {
        "pq_record_layer_is_186_records": len(pq_records) == 186,
        "pq_record_numbers_are_1_to_186": pq_ids == set(range(1, 187)),
        "canonical_relationship_counts": relationship_counts == EXPECTED_RELATIONSHIP_COUNTS,
        "canonical_farming_set": farming_pqs == EXPECTED_FARMING_PQS,
    }

    texts = {name: path.read_text(encoding="utf-8") for name, path in CONSUMERS.items()}

    checks.update({
        "guides_uses_database_first_workflow": "Database-First Workflow" in texts["guides"] and "Skills Database" in texts["guides"],
        "skills_database_preserves_pq_boundary": "does not, by itself, establish that the skill is guaranteed" in texts["skills_database"],
        "skills_complete_preserves_pq_boundary": "must not be read as a guaranteed drop" in texts["skills_complete_database"],
        "skill_unlock_preserves_pq_boundary": "Canonical PQ→skill association; independently verified Ultimate Finish/trigger/drop fields" in texts["skill_unlock_database"],
        "qq_bangs_pq83_is_noncanonical_farming_claim": "community/research acquisition lead" in texts["qq_bangs"] and "not a canonical `pq_features_farming` relationship" in texts["qq_bangs"],
        "farming_hub_uses_canonical_dragon_ball_set": all(f"PQ{pq}" in texts["farming_hub"] for pq in sorted(EXPECTED_FARMING_PQS)),
        "farming_hub_preserves_acquisition_uncertainty": "do not treat the existence of a PQ→skill relationship as proof of a guaranteed or Ultimate-Finish-only skill reward" in texts["farming_hub"],
        "farming_routes_does_not_rank_canonical_farming_set": "does not rank them by clear speed or drop probability" in texts["farming_routes"] and "does not treat it as a universal best route" in texts["farming_routes"],
        "equipment_database_separates_acquisition_layers": "DLC ownership must never replace the actual unlock condition" in texts["equipment_database"],
        "accessory_pq_database_preserves_reward_condition_boundary": "does **not** establish whether an accessory is" in texts["accessory_pq_database"],
    })

    # Current-facing summary consumers must not resurrect superseded canonical baselines.
    forbidden_current_scalars = ("860", "862", "854", "151 Super Soul", "125 equipment")
    stale_hits = {}
    for name, body in texts.items():
        hits = [token for token in forbidden_current_scalars if token in body]
        if hits:
            stale_hits[name] = hits
    checks["summary_consumers_have_no_superseded_current_scalars"] = not stale_hits

    bad = [name for name, value in checks.items() if not value]
    result = {
        "schema_version": "1.0.0",
        "status": "pass" if not bad else "fail",
        "pq_records": len(pq_records),
        "canonical_relationship_counts": relationship_counts,
        "canonical_farming_pqs": sorted(farming_pqs),
        "consumers_checked": list(CONSUMERS),
        "failed_checks": bad,
        "stale_current_scalar_hits": stale_hits,
        "checks": checks,
        "evidence_boundary": "This validator checks current summary/reference presentation contracts and canonical scalar/set consistency. It does not infer reward guarantees, Ultimate Finish requirements, drop rates, or new relationships from prose.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not bad else 1

if __name__ == "__main__":
    raise SystemExit(main())
