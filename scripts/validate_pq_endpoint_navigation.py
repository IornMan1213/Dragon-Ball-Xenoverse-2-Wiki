#!/usr/bin/env python3
"""Validate canonical PQ endpoint navigation without promoting evidence layers.

Canonical relationship data is authoritative. This validator checks exact endpoint
resolution, canonical PQ identity resolution, and duplicate structured (PQ,target)
pairs for every registered relationship domain, plus the explicit alias/granularity bridge.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"

REL = DATA / "pq-reward-relationships.json"
SKILLS = DATA / "skills.json"
SOULS = DATA / "super-souls-record-layer.json"
EQUIPMENT = DATA / "equipment-accessories-record-layer.json"
CHARACTERS = DATA / "characters-record-layer.json"
BRIDGE = DATA / "pq-endpoint-alias-granularity-map.json"
DLC = DATA / "dlc" / "canonical-dlc-identity.json"

DOMAIN_TO_REL = {
    "skills": "pq_rewards_skill",
    "super_souls": "pq_rewards_super_soul",
    "equipment": "pq_rewards_equipment",
    "characters": "pq_features_character",
    "dlc": "pq_requires_dlc",
}


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def canonical_names(data, domain):
    if domain == "characters":
        return set(data.get("character_names", []))
    return {record["name"] for record in data.get("records", []) if record.get("name")}


def main() -> int:
    relationships = load(REL).get("verified_relationships", [])
    pq_records = load(DATA / "parallel-quests-record-layer.json").get("records", [])
    canonical_pq_ids = {record.get("id") for record in pq_records if record.get("id")}
    canonical_pq_numbers = {record.get("number") for record in pq_records}
    bridge = load(BRIDGE)

    dlc_names = {record["name"] for record in load(DLC).get("records", []) if record.get("name")}

    canonical = {
        "skills": canonical_names(load(SKILLS), "skills"),
        "super_souls": canonical_names(load(SOULS), "super_souls"),
        "equipment": canonical_names(load(EQUIPMENT), "equipment"),
        "characters": canonical_names(load(CHARACTERS), "characters"),
    }

    results = {}
    failures = []
    for domain, relationship in DOMAIN_TO_REL.items():
        edges = [e for e in relationships if e.get("relationship") == relationship and e.get("pq") and e.get("target")]
        pairs = [(e.get("pq"), e.get("target")) for e in edges]
        duplicate_pair_count = len(pairs) - len(set(pairs))
        invalid_pq_ids = sorted({e.get("pq") for e in edges if e.get("pq") not in canonical_pq_ids})
        targets = sorted({e.get("target") for e in edges if e.get("target")})
        if domain == "dlc":
            missing = [name for name in targets if name not in dlc_names]
            status = "clean" if not missing else "unresolved"
            note = "Every DLC endpoint resolves by exact canonical DLC identity." if not missing else "Unresolved DLC targets require an explicit canonical DLC identity record; do not infer."
        else:
            missing = [name for name in targets if name not in canonical[domain]]
            status = "clean" if not missing else "unresolved"
            note = "Every endpoint resolves by exact canonical name." if not missing else "Unresolved targets require an explicit identity conflict/alias or canonical record; do not infer."
        results[domain] = {
            "relationship_type": relationship,
            "edge_count": len(edges),
            "unique_target_count": len(targets),
            "missing_target_count": len(missing),
            "missing_targets": missing,
            "duplicate_pair_count": duplicate_pair_count,
            "invalid_pq_id_count": len(invalid_pq_ids),
            "invalid_pq_ids": invalid_pq_ids,
            "status": status if not duplicate_pair_count and not invalid_pq_ids else "unresolved",
            "note": note,
        }
        if missing:
            failures.extend(f"{domain}: {name}" for name in missing)
        if duplicate_pair_count:
            failures.append(f"{domain}: duplicate (PQ,target) pairs={duplicate_pair_count}")
        if invalid_pq_ids:
            failures.extend(f"{domain}: invalid PQ id {pq}" for pq in invalid_pq_ids)

    bridge_checks = []
    for item in bridge.get("equipment", []):
        targets = item.get("canonical_targets", [])
        unresolved = [t for t in targets if t not in canonical["equipment"]]
        bridge_checks.append({
            "pq": item.get("pq"),
            "domain": "equipment",
            "status": "clean" if not unresolved else "unresolved",
            "unresolved_targets": unresolved,
        })
    for item in bridge.get("dlc", []):
        bridge_checks.append({
            "pq_range": item.get("pq_range"),
            "domain": "dlc",
            "status": "explicit_granularity",
            "canonical_targets": item.get("canonical_targets", []),
        })

    report = {
        "schema_version": "1.1.0",
        "scope": "PQ 1-186 canonical endpoint navigation",
        "source_of_truth": str(REL.relative_to(ROOT)),
        "canonical_identity_layers": {
            "skills": str(SKILLS.relative_to(ROOT)),
            "super_souls": str(SOULS.relative_to(ROOT)),
            "equipment": str(EQUIPMENT.relative_to(ROOT)),
            "characters": str(CHARACTERS.relative_to(ROOT)),
            "dlc": str(DLC.relative_to(ROOT)),
        },
        "canonical_pq_identity": {
            "record_count": len(pq_records),
            "unique_id_count": len(canonical_pq_ids),
            "unique_number_count": len(canonical_pq_numbers),
            "expected_number_range": "1-186",
        },
        "results": results,
        "bridge_checks": bridge_checks,
        "rules": [
            "Canonical relationship data is authoritative.",
            "Verification status and research/projection layers never override canonical identity.",
            "Exact canonical name matches are required for direct navigation.",
            "Explicit aliases/conflicts/granularity may explain source/display differences but do not create canonical edges.",
            "DLC endpoints resolve against the standalone canonical DLC identity layer; bundle/chapter granularity remains explicit.",
        ],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
