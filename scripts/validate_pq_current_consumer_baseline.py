#!/usr/bin/env python3
"""Validate registered current PQ consumer baseline invariants.

Historical audit snapshots are deliberately excluded from current-state checks.
Canonical relationship data remains authoritative.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    rel = load(DATA / "pq-reward-relationships.json")
    producer = load(DATA / "pq-relationship-producer-census.json")
    authoritative = load(DATA / "pq-current-baseline-single-source-reconciliation-2026-09-22.json")

    edges = rel.get("verified_relationships", [])
    counts = {}
    for edge in edges:
        relationship = edge.get("relationship")
        counts[relationship] = counts.get(relationship, 0) + 1

    expected = {
        "pq_rewards_skill": 244,
        "pq_rewards_super_soul": 145,
        "pq_rewards_equipment": 124,
        "pq_features_character": 247,
        "pq_requires_dlc": 86,
        "pq_farming_route": 7,
    }
    failures = []
    for key, value in expected.items():
        if counts.get(key, 0) != value:
            failures.append(f"canonical {key}: expected {value}, got {counts.get(key, 0)}")

    if len(edges) != authoritative["authoritative_current_baseline"]["total_edges"]:
        failures.append("canonical total does not match correction audit baseline")

    equipment = producer["producers"]["equipment"]
    if equipment["forward"] != 124 or equipment["reverse"] != 122:
        failures.append(f"producer equipment projection stale: {equipment}")
    if producer["target_normalization"]["total_relationships"] != 853:
        failures.append("producer target-normalization total is stale")

    report = {
        "schema_version": "1.0.0",
        "canonical_total": len(edges),
        "canonical_counts": counts,
        "producer_current_equipment": equipment,
        "expected_current_baseline": authoritative["authoritative_current_baseline"],
        "historical_snapshot_policy": "Historical audit snapshots are not current-state inputs.",
        "status": "clean" if not failures else "unresolved",
        "failures": failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
