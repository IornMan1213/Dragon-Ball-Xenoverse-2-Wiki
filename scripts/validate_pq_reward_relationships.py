#!/usr/bin/env python3
"""Validate the canonical PQ cross-domain relationship store.

No reward inference is performed. This only validates the stored relationship
rows against the repository's cross-domain schema and canonical PQ range.
"""
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/data/pq-reward-relationships.json"
SCHEMA = ROOT / "docs/data/pq-cross-domain-schema.json"
AUDIT = ROOT / "docs/data/pq-reward-relationship-integrity-audit-2026-09-27.json"

REL_TYPES = {
    "pq_rewards_skill", "pq_rewards_super_soul", "pq_rewards_equipment",
    "pq_features_character", "pq_requires_dlc", "pq_farming_route",
}
STATUSES = {"indexed", "source_backed", "partially_verified", "verified", "conflict"}
PQ_RE = re.compile(r"^pq-(\d{3})$")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    data = load(SOURCE)
    schema = load(SCHEMA)
    if not isinstance(data, dict):
        raise SystemExit("PQ reward relationship root must be an object")
    if not isinstance(schema, dict):
        raise SystemExit("cross-domain schema root must be an object")
    if not isinstance(data, dict):
        raise SystemExit("PQ reward relationship root must be an object")
    if not isinstance(schema, dict):
        raise SystemExit("cross-domain schema root must be an object")
    rows = data.get("verified_relationships")
    if not isinstance(rows, list):
        raise SystemExit("verified_relationships must be a list")
    if schema.get("additionalProperties") is not False:
        raise SystemExit("cross-domain schema must forbid additional properties")

    seen = set()
    counts = {}
    malformed = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            malformed.append((i, "row is not an object"))
            continue
        required = {"pq", "relationship", "target", "status", "source"}
        missing = required - row.keys()
        extra = set(row) - required - {"notes"}
        if missing or extra:
            malformed.append((i, f"missing={sorted(missing)} extra={sorted(extra)}"))
            continue
        pq = row["pq"]
        m = PQ_RE.fullmatch(pq) if isinstance(pq, str) else None
        number = int(m.group(1)) if m else None
        if number is None or not 1 <= number <= 186:
            malformed.append((i, "pq must be pq-001 through pq-186"))
            continue
        rel = row["relationship"]
        status = row["status"]
        target = row["target"]
        source = row["source"]
        if rel not in REL_TYPES:
            malformed.append((i, "invalid relationship type"))
            continue
        if status not in STATUSES:
            malformed.append((i, "invalid status"))
            continue
        if not isinstance(target, str) or not target.strip():
            malformed.append((i, "target must be non-empty string"))
            continue
        if not isinstance(source, str) or not source.strip() or not urlparse(source).scheme:
            malformed.append((i, "source must be URI-like string"))
            continue
        if "notes" in row and not isinstance(row["notes"], str):
            malformed.append((i, "notes must be string"))
            continue
        key = (pq, rel, target)
        if key in seen:
            malformed.append((i, "duplicate relationship key"))
            continue
        seen.add(key)
        counts[rel] = counts.get(rel, 0) + 1

    expected = data.get("current_counts")
    expected_map = {
        "pq_rewards_skill": "skill",
        "pq_rewards_super_soul": "super_soul",
        "pq_rewards_equipment": "equipment",
        "pq_features_character": "character",
        "pq_requires_dlc": "dlc",
        "pq_farming_route": "farming",
    }
    if not isinstance(expected, dict) or set(expected) != set(expected_map.values()):
        malformed.append((-1, "current_counts must contain exactly skill, super_soul, equipment, character, dlc, farming"))
    elif any(not isinstance(expected[key], int) or isinstance(expected[key], bool) or expected[key] < 0 for key in expected_map.values()):
        malformed.append((-1, "current_counts values must be non-negative integers"))

    if not isinstance(expected, dict) or set(expected) != set(expected_map.values()):
        malformed.append((-1, "current_counts must contain exactly skill, super_soul, equipment, character, dlc, farming"))
    elif any(not isinstance(expected[key], int) or isinstance(expected[key], bool) or expected[key] < 0 for key in expected_map.values()):
        malformed.append((-1, "current_counts values must be non-negative integers"))

    count_mismatches = {
        rel: {"stored": expected.get(key), "actual": counts.get(rel, 0)}
        for rel, key in expected_map.items()
        if not isinstance(expected, dict) or expected.get(key) != counts.get(rel, 0)
    }

    report = {
        "schema_version": "1.0",
        "audited_at": "2026-09-27",
        "relationship_rows": len(rows),
        "unique_relationship_keys": len(seen),
        "malformed_rows": len(malformed),
        "count_mismatches": count_mismatches,
        "counts_by_relationship": counts,
        "pq_range": [1, 186],
        "status": "passed" if not malformed and not count_mismatches else "failed",
        "evidence_boundary": "Structural validation only; absence of a relationship is not treated as evidence that a reward is unavailable.",
    }
    AUDIT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
