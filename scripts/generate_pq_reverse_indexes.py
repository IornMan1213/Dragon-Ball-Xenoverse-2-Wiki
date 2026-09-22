#!/usr/bin/env python3
"""Deterministically generate PQ standalone reverse indexes from normalized reward maps.

Canonical rule: normalized reward maps are the source layer. This generator only
projects explicitly typed rewards; it never infers missing rewards or edits canonical
relationship data.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DOMAINS = ("skills", "super_souls", "clothing", "accessories")
RANGES = (
    ("081-120", 81, 120, "pq-081-120-reward-map.json", "pq-reverse-index-081-120.json"),
    ("121-142", 121, 142, "pq-121-142-reward-map.json", "pq-reverse-index-121-142.json"),
    ("143-162", 143, 162, "pq-143-162-reward-map.json", "pq-reverse-index-143-162.json"),
    ("163-186", 163, 186, "pq-163-186-reward-map.json", "pq-reverse-index-163-186.json"),
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def source_records(data):
    records = data["records"]
    if isinstance(records, dict):
        return [
            (int(pq), {
                "skills": [name for name, kind in rewards if kind == "skill"],
                "super_souls": [name for name, kind in rewards if kind == "super_soul"],
                "clothing": [name for name, kind in rewards if kind == "clothing"],
                "accessories": [name for name, kind in rewards if kind == "accessory"],
                "artworks": [name for name, kind in rewards if kind == "artwork"],
            })
            for pq, rewards in records.items()
        ]
    if isinstance(records, list):
        if records and "rewards" in records[0]:
            return [(int(row["pq"]), row.get("rewards", {})) for row in records]
        return [
            (int(row["pq"]), {
                "skills": [name for name, kind in row.get("rewards", []) if kind == "skill"],
                "super_souls": [name for name, kind in row.get("rewards", []) if kind == "super_soul"],
                "clothing": [name for name, kind in row.get("rewards", []) if kind == "clothing"],
                "accessories": [name for name, kind in row.get("rewards", []) if kind == "accessory"],
            })
            for row in records
        ]
    return [
        (int(pq), {
            "skills": [name for name, kind in rewards if kind == "skill"],
            "super_souls": [name for name, kind in rewards if kind == "super_soul"],
            "clothing": [name for name, kind in rewards if kind == "clothing"],
            "accessories": [name for name, kind in rewards if kind == "accessory"],
        })
        for pq, rewards in records.items()
    ]


def build_index(data):
    index = {domain: {} for domain in DOMAINS}
    for pq, rewards in source_records(data):
        for domain in DOMAINS:
            for value in rewards.get(domain, []):
                key = str(value)
                index[domain].setdefault(key, []).append(pq)
    for domain in DOMAINS:
        for values in index[domain].values():
            values.sort()
    return index


def build_artworks(data):
    artworks = {}
    for pq, rewards in source_records(data):
        for value in rewards.get("artworks", []):
            artworks.setdefault(str(value), []).append(pq)
    for values in artworks.values():
        values.sort()
    return artworks


def expected_payload(data, scope, source_name):
    index = build_index(data)
    artworks = build_artworks(data)
    if artworks:
        index["artworks"] = artworks
    return {
        "schema_version": "1.0",
        "scope": f"PQ {scope}",
        "status": data.get("status", "source_normalized_partial"),
        "source_map": source_name,
        "indexes": index,
        "notes": [
            "Reverse indexes are generated only from the typed reward relationships established in the source reward map.",
            "Absence from an index does not prove absence from alternate drops or acquisition routes.",
            "Zeni and consumables are excluded because they are not cross-domain collectible relationships.",
        ],
    }


def canonical_json(value):
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--write", action="store_true",
                        help="write deterministic standalone indexes")
    args = parser.parse_args()
    data_dir = Path(args.root) / "docs" / "data" / "pq-reward-normalization"

    failures = []
    results = []
    for scope, lo, hi, source_name, output_name in RANGES:
        source = load(data_dir / source_name)
        expected = expected_payload(source, scope, source_name)
        output_path = data_dir / output_name
        actual = load(output_path) if output_path.exists() else None
        actual_index = ((actual or {}).get("indexes")
                        if isinstance(actual, dict) and "indexes" in actual
                        else {domain: (actual or {}).get(domain, {}) for domain in DOMAINS})
        same = actual is not None and actual_index == expected["indexes"]
        results.append({
            "range": scope,
            "pq_count": hi - lo + 1,
            "source_pairs": sum(len(pqs) for items in expected["indexes"].values() for pqs in items.values()),
            "matches_expected": same,
        })
        if args.write:
            if actual is None:
                output_path.write_text(canonical_json(expected), encoding="utf-8")
            else:
                updated = dict(actual)
                if "indexes" in updated:
                    updated["indexes"] = expected["indexes"]
                else:
                    for domain in DOMAINS:
                        updated[domain] = expected["indexes"][domain]
                output_path.write_text(canonical_json(updated), encoding="utf-8")
        elif not same:
            failures.append(scope)

    print(json.dumps({
        "status": "pass" if not failures else "fail",
        "mode": "write" if args.write else "check",
        "ranges": results,
        "mismatched_ranges": failures,
    }, indent=2))
    return 1 if failures and not args.write else 0


if __name__ == "__main__":
    raise SystemExit(main())
