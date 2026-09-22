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
    for record in data["records"]:
        pq = int(record["pq"])
        for domain in DOMAINS:
            for name in record.get(domain, []):
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
        unified_missing = sorted(source_pairs - unified_pairs)
        unified_extra = sorted(unified_pairs - source_pairs)

        row = {
            "range": label,
            "source_pairs": len(source_pairs),
            "reverse_pairs": len(reverse_pairs),
            "missing_from_reverse": len(missing),
            "extra_in_reverse": len(extra),
            "missing_from_unified": len(unified_missing),
            "extra_in_unified": len(unified_extra),
        }
        report.append(row)

        if missing or extra or unified_missing or unified_extra:
            failures.append((label, missing, extra, unified_missing, unified_extra))

    print(json.dumps({"status": "pass" if not failures else "fail", "ranges": report}, indent=2))

    if failures:
        for label, missing, extra, unified_missing, unified_extra in failures:
            print(f"\n[{label}]")
            if missing:
                print("missing from standalone:", missing)
            if extra:
                print("extra in standalone:", extra)
            if unified_missing:
                print("missing from unified:", unified_missing)
            if unified_extra:
                print("extra in unified:", unified_extra)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
