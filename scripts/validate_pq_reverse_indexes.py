#!/usr/bin/env python3
"""Validate PQ reverse-index projections against normalized reward maps and unified index.

Canonical rule: normalized reward maps are the source layer for this check. Reverse
indexes are projections only; this validator never infers missing rewards.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DOMAINS = ("skills", "super_souls", "clothing", "accessories")
ARTWORKS = "artworks"
CANONICAL_RELATIONSHIP_TYPES = {"pq_rewards_skill": "skills", "pq_rewards_super_soul": "super_souls", "pq_rewards_equipment": "equipment", "pq_features_character": "characters", "pq_requires_dlc": "dlc", "pq_farming_route": "farming"}

RANGES = (
    ("081-120", 81, 120, "pq-081-120-reward-map.json", "pq-reverse-index-081-120.json"),
    ("121-142", 121, 142, "pq-121-142-reward-map.json", "pq-reverse-index-121-142.json"),
    ("143-162", 143, 162, "pq-143-162-reward-map.json", "pq-reverse-index-143-162.json"),
    ("163-186", 163, 186, "pq-163-186-reward-map.json", "pq-reverse-index-163-186.json"),
)


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def source_index(data):
    out = {domain: {} for domain in DOMAINS}
    records = data["records"]
    if isinstance(records, dict):
        normalized = [
            (int(pq), {
                "skills": [name for name, kind in rewards if kind == "skill"],
                "super_souls": [name for name, kind in rewards if kind == "super_soul"],
                "clothing": [name for name, kind in rewards if kind == "clothing"],
                "accessories": [name for name, kind in rewards if kind == "accessory"],
            })
            for pq, rewards in records.items()
        ]
    elif records and isinstance(records[0], (list, tuple)) and len(records[0]) == 2:
        normalized = [
            (int(pq), {
                "skills": [name for name, kind in rewards if kind == "skill"],
                "super_souls": [name for name, kind in rewards if kind == "super_soul"],
                "clothing": [name for name, kind in rewards if kind == "clothing"],
                "accessories": [name for name, kind in rewards if kind == "accessory"],
            })
            for pq, rewards in records
        ]
    else:
        normalized = []
        for record in records:
            if "rewards" in record:
                normalized.append((int(record["pq"]), record.get("rewards", {})))
            else:
                normalized.append((int(record["pq"]), {
                    domain: list(record.get(domain, [])) for domain in DOMAINS
                }))
    for pq, reward_map in normalized:
        for domain in DOMAINS:
            for name in reward_map.get(domain, []):
                out[domain].setdefault(str(name), []).append(pq)
    return out


def projection_index(data):
    raw = data.get("indexes", data)
    return {domain: {str(k): [int(x) for x in v] for k, v in raw.get(domain, {}).items()}
            for domain in DOMAINS}


def pair_set(index):
    return {
        (domain, name, pq)
        for domain, items in index.items()
        for name, pqs in items.items()
        for pq in pqs
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args()
    root = Path(args.root)
    data_dir = root / "docs" / "data" / "pq-reward-normalization"

    unified = load(data_dir / "pq-unified-reverse-index-1-186.json")
    unified_index = projection_index(unified)

    canonical = load(root / "docs" / "data" / "pq-reward-relationships.json")
    canonical_pairs = {domain: set() for domain in CANONICAL_RELATIONSHIP_TYPES.values()}
    for relationship in canonical.get("verified_relationships", []):
        domain = CANONICAL_RELATIONSHIP_TYPES.get(relationship.get("relationship"))
        if domain:
            pq = int(str(relationship["pq"]).replace("pq-", ""))
            canonical_pairs[domain].add((domain, str(relationship["target"]), pq))

    failures = []
    report = []

    for label, lo, hi, source_name, reverse_name in RANGES:
        source = source_index(load(data_dir / source_name))
        reverse = projection_index(load(data_dir / reverse_name))

        source_pairs = pair_set(source)
        reverse_pairs = pair_set(reverse)
        missing = sorted(source_pairs - reverse_pairs)
        extra = sorted(reverse_pairs - source_pairs)

        unified_pairs = {
            (domain, name, pq)
            for domain, items in unified_index.items()
            for name, pqs in items.items()
            for pq in pqs
            if lo <= pq <= hi
        }
        canonical_range_pairs = {
            pair
            for domain_pairs in canonical_pairs.values()
            for pair in domain_pairs
            if lo <= pair[2] <= hi
        }
        unified_equipment_pairs = {
            ("equipment", name, pq)
            for subtype in ("clothing", "accessories")
            for name, pqs in unified_index.get(subtype, {}).items()
            for pq in pqs
            if lo <= pq <= hi
        }
        unified_canonical_pairs = {
            pair for pair in unified_pairs
            if pair[0] in {"skills", "super_souls", "characters", "dlc", "farming"}
        } | unified_equipment_pairs
        unified_missing = sorted(canonical_range_pairs - unified_canonical_pairs)
        unified_extra = sorted(unified_canonical_pairs - canonical_range_pairs)

        row = {
            "range": label,
            "source_pairs": len(source_pairs),
            "reverse_pairs": len(reverse_pairs),
            "missing_from_reverse": len(missing),
            "extra_in_reverse": len(extra),
            "missing_from_unified_canonical": len(unified_missing),
            "extra_in_unified_canonical": len(unified_extra),
        }
        report.append(row)

        # Standalone reverse indexes are projections of normalized source maps.
        # Differences from the unified canonical layer are informational because
        # normalized source maps are explicitly allowed to be partial or variant.
        if missing or extra:
            failures.append((label, missing, extra, unified_missing, unified_extra))

    print(json.dumps({
        "status": "pass" if not failures else "fail",
        "ranges": report,
        "canonical_comparison": {
            "semantics": "informational",
            "rule": "Standalone reverse indexes must match normalized source maps exactly; differences from the unified canonical relationship projection are retained as source-layer drift and must not override canonical relationships.",
            "ranges_with_canonical_projection_drift": sum(1 for row in report if row["missing_from_unified_canonical"] or row["extra_in_unified_canonical"]),
            "total_missing_from_unified_canonical": sum(row["missing_from_unified_canonical"] for row in report),
            "total_extra_in_unified_canonical": sum(row["extra_in_unified_canonical"] for row in report)
        }
    }, indent=2))

    if failures:
        for label, missing, extra, unified_missing, unified_extra in failures:
            print(f"\n[{label}]")
            if missing:
                print("missing from standalone:", missing)
            if extra:
                print("extra in standalone:", extra)
            if unified_missing:
                print("missing from unified canonical projection:", unified_missing)
            if unified_extra:
                print("extra in unified canonical projection:", unified_extra)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
