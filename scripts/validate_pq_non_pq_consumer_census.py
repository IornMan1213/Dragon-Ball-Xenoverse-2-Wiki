#!/usr/bin/env python3
"""Validate the registered non-PQ consumer current-baseline census.

This validator checks the machine-readable census against the canonical relationship
layer. Historical audit snapshots are intentionally excluded from current-state
assertions.
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
    census = load(DATA / "pq-non-pq-consumer-census-2026-09-22.json")

    edges = rel.get("verified_relationships", [])
    counts = {}
    for edge in edges:
        key = edge.get("relationship")
        counts[key] = counts.get(key, 0) + 1

    expected = census["canonical_baseline"]
    failures = []
    if len(rel.get("records", [])) not in (0, expected["pq_records"]):
        failures.append("unexpected PQ record container shape/count")
    if len(edges) != expected["total_edges"]:
        failures.append(f"canonical total: expected {expected['total_edges']}, got {len(edges)}")

    mapping = {
        "skill":"pq_rewards_skill",
        "super_soul":"pq_rewards_super_soul",
        "equipment":"pq_rewards_equipment",
        "character":"pq_features_character",
        "dlc":"pq_requires_dlc",
        "farming":"pq_farming_route",
    }
    for domain, relationship in mapping.items():
        got = counts.get(relationship, 0)
        if got != expected[domain]:
            failures.append(f"canonical {domain}: expected {expected[domain]}, got {got}")

    producer = load(DATA / "pq-relationship-producer-census.json")
    p = producer["producers"]
    if p["equipment"]["forward"] != 124 or p["equipment"]["reverse"] != 122:
        failures.append("producer equipment projection is not 124/122")
    if producer["master"]["total_relationships"] != 854:
        failures.append("producer master total is not 854")

    report = {
        "schema_version":"1.0.0",
        "canonical_total":len(edges),
        "canonical_counts":counts,
        "producer_equipment":p["equipment"],
        "census_consumer_count":len(census["consumers"]),
        "status":"clean" if not failures else "unresolved",
        "failures":failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
