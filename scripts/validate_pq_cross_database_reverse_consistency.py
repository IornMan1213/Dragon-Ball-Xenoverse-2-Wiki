#!/usr/bin/env python3
"""Validate canonical PQ reward relationships against the unified reverse projection.

Canonical relationship data is authoritative. The unified reverse index is a
derived projection and may use numeric PQ numbers plus split equipment domains.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"
REL = DATA / "pq-reward-relationships.json"
UNIFIED = DATA / "pq-reward-normalization" / "pq-unified-reverse-index-1-186.json"

REL_TYPES = {
    "skills": "pq_rewards_skill",
    "super_souls": "pq_rewards_super_soul",
    "equipment": "pq_rewards_equipment",
    "characters": "pq_features_character",
    "dlc": "pq_requires_dlc",
    "farming": "pq_farming_route",
}

def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)

def canonical_pairs(relationships, relationship_type):
    return {
        (int(str(edge["pq"]).split("-")[-1]), str(edge["target"]))
        for edge in relationships
        if edge.get("relationship") == relationship_type
    }

def reverse_pairs(mapping):
    return {
        (int(pq), str(target))
        for target, pqs in mapping.items()
        for pq in pqs
    }

def main() -> int:
    relationships = load(REL).get("verified_relationships", [])
    unified = load(UNIFIED)

    mappings = {
        "skills": unified.get("skills", {}),
        "super_souls": unified.get("super_souls", {}),
        "equipment": {
            **unified.get("clothing", {}),
            **unified.get("accessories", {}),
        },
        "characters": unified.get("characters", {}),
        "dlc": unified.get("dlc", {}),
        "farming": unified.get("farming", {}),
    }

    domains = {}
    for domain, relationship_type in REL_TYPES.items():
        forward = canonical_pairs(relationships, relationship_type)
        reverse = reverse_pairs(mappings[domain])
        domains[domain] = {
            "canonical_pairs": len(forward),
            "reverse_pairs": len(reverse),
            "missing_reverse_pairs": sorted(forward - reverse),
            "extra_reverse_pairs": sorted(reverse - forward),
            "duplicate_canonical_rows": len([
                e for e in relationships if e.get("relationship") == relationship_type
            ]) - len(forward),
            "status": "clean" if forward == reverse else "drift",
        }

    bad = [d for d, result in domains.items() if result["status"] != "clean"]
    result = {
        "schema_version": "1.0.0",
        "scope": "PQ 1-186 canonical reward/reverse-index consistency",
        "source_of_truth": str(REL.relative_to(ROOT)),
        "projection": str(UNIFIED.relative_to(ROOT)),
        "normalization_rules": [
            "Canonical pq-NNN identifiers are normalized to integer PQ numbers.",
            "Equipment canonical edges are compared against the unified clothing + accessories projections.",
            "Reverse projections are derived navigation data and do not create canonical relationships.",
            "Absence from a partial source-normalized projection is not treated as evidence of no acquisition."
        ],
        "domains": domains,
        "status": "clean" if not bad else "drift",
        "failed_domains": bad,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not bad else 1

if __name__ == "__main__":
    raise SystemExit(main())
