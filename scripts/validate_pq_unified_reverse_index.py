#!/usr/bin/env python3
"""Validate the PQ 1-186 unified reverse index against canonical relationships.

Canonical relationship data is authoritative. This validator checks exact target/PQ
parity for skills, Super Souls, equipment (clothing/accessory union), characters,
DLC, and farming. It reports drift and never mutates repository data.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REL_TO_DOMAIN = {
    "pq_rewards_skill": "skills",
    "pq_rewards_super_soul": "super_souls",
    "pq_rewards_equipment": "equipment",
    "pq_features_character": "characters",
    "pq_requires_dlc": "dlc",
    "pq_farming_route": "farming",
}
EQUIPMENT_DOMAINS = ("clothing", "accessories")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def pq_number(value):
    return int(str(value).replace("pq-", ""))


def canonical_pairs(data):
    result = {domain: set() for domain in REL_TO_DOMAIN.values()}
    for row in data.get("verified_relationships", []):
        domain = REL_TO_DOMAIN.get(row.get("relationship"))
        if domain:
            result[domain].add((str(row["target"]), pq_number(row["pq"])))
    return result


def projection_pairs(data, domain):
    values = set()
    duplicate_pairs = 0
    invalid_list_fields = []
    for name, pqs in data.get(domain, {}).items():
        if not isinstance(pqs, list):
            invalid_list_fields.append(str(name))
            continue
        flattened = [(str(name), pq_number(pq)) for pq in pqs]
        duplicate_pairs += len(flattened) - len(set(flattened))
        values.update(flattened)
    return values, duplicate_pairs, invalid_list_fields


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args()
    root = Path(args.root)
    data_dir = root / "docs" / "data" / "pq-reward-normalization"

    unified = load(data_dir / "pq-unified-reverse-index-1-186.json")
    canonical = canonical_pairs(load(root / "docs" / "data" / "pq-reward-relationships.json"))

    report = {}
    failures = []
    for domain in ("skills", "super_souls", "characters", "dlc", "farming"):
        expected = canonical[domain]
        actual, duplicate_pairs, invalid_list_fields = projection_pairs(unified, domain)
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        report[domain] = {
            "canonical_pairs": len(expected),
            "projection_pairs": len(actual),
            "missing": len(missing),
            "extra": len(extra),
            "duplicate_pairs": duplicate_pairs,
            "invalid_list_fields": len(invalid_list_fields),
        }
        if missing or extra or duplicate_pairs or invalid_list_fields:
            failures.append(domain)

    expected = canonical["equipment"]
    actual = set()
    for domain in EQUIPMENT_DOMAINS:
        domain_pairs, duplicate_pairs, invalid_list_fields = projection_pairs(unified, domain)
        actual |= domain_pairs
        equipment_duplicate_pairs = locals().get("equipment_duplicate_pairs", 0) + duplicate_pairs
        equipment_invalid_list_fields = locals().get("equipment_invalid_list_fields", 0) + len(invalid_list_fields)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    report["equipment"] = {
        "canonical_pairs": len(expected),
        "projection_pairs": len(actual),
        "missing": len(missing),
        "extra": len(extra),
        "duplicate_pairs": equipment_duplicate_pairs,
        "invalid_list_fields": equipment_invalid_list_fields,
    }
    if missing or extra or equipment_duplicate_pairs or equipment_invalid_list_fields:
        failures.append("equipment")

    print(json.dumps({
        "status": "pass" if not failures else "fail",
        "scope": "PQ 1-186",
        "semantics": "canonical relationship parity; validator is read-only",
        "domains": report,
        "failed_domains": failures,
    }, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
