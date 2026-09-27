#!/usr/bin/env python3
"""Validate the recovered canonical Super Soul PQ acquisition contract.

This validator checks only deterministic identity and cross-layer parity. It
never infers missing rewards, mechanics, probabilities, or alternate routes.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = ROOT / "docs/data/pq-reward-relationships.json"
SOULS = ROOT / "docs/data/super-souls-record-layer.json"
INDEX = ROOT / "docs/data/super-souls/pq-acquisition-index-001-186.json"

EXPECTED_RELATIONSHIPS = 137
EXPECTED_UNIQUE_TARGETS = 134
EXPECTED_INDEX_TARGETS = 134


def load_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERROR: cannot parse {path}: {exc}")
    if not isinstance(value, dict):
        raise SystemExit(f"ERROR: {path} must contain a JSON object")
    return value


rel = load_object(REL)
souls = load_object(SOULS)
index = load_object(INDEX)

rows = rel.get("verified_relationships")
records = souls.get("records")
index_rows = index.get("records")

if not isinstance(rows, list):
    raise SystemExit("ERROR: pq-reward-relationships.verified_relationships must be a list")
if not isinstance(records, list):
    raise SystemExit("ERROR: super-souls-record-layer.records must be a list")
if not isinstance(index_rows, list):
    raise SystemExit("ERROR: pq-acquisition-index.records must be a list")

soul_rows = []
for row in rows:
    if not isinstance(row, dict):
        raise SystemExit("ERROR: relationship row must be an object")
    if row.get("relationship") != "pq_rewards_super_soul":
        continue
    target = row.get("target")
    pq = row.get("pq")
    if not isinstance(target, str) or not target.strip():
        raise SystemExit("ERROR: Super Soul relationship target must be a non-empty string")
    if type(pq) is not int or not 1 <= pq <= 186:
        raise SystemExit(f"ERROR: invalid Super Soul PQ id: {pq!r}")
    soul_rows.append((pq, target))

if len(soul_rows) != EXPECTED_RELATIONSHIPS:
    raise SystemExit(
        f"ERROR: expected {EXPECTED_RELATIONSHIPS} Super Soul relationships; found {len(soul_rows)}"
    )

canonical_names = []
canonical_ids = set()
for row in records:
    if not isinstance(row, dict):
        raise SystemExit("ERROR: Super Soul record must be an object")
    ident = row.get("id")
    name = row.get("name")
    if not isinstance(ident, str) or not ident.strip():
        raise SystemExit("ERROR: Super Soul record id must be a non-empty string")
    if not isinstance(name, str) or not name.strip():
        raise SystemExit("ERROR: Super Soul record name must be a non-empty string")
    if ident in canonical_ids:
        raise SystemExit(f"ERROR: duplicate Super Soul id: {ident}")
    canonical_ids.add(ident)
    canonical_names.append(name)

canonical_name_set = set(canonical_names)
if len(canonical_name_set) != len(canonical_names):
    raise SystemExit("ERROR: duplicate Super Soul canonical names detected")

relationship_targets = {target for _, target in soul_rows}
if len(relationship_targets) != EXPECTED_UNIQUE_TARGETS:
    raise SystemExit(
        f"ERROR: expected {EXPECTED_UNIQUE_TARGETS} unique Super Soul relationship targets; found {len(relationship_targets)}"
    )
missing_records = sorted(relationship_targets - canonical_name_set)
if missing_records:
    raise SystemExit(f"ERROR: relationship targets missing from canonical records: {missing_records}")

index_targets = set()
for row in index_rows:
    if not isinstance(row, dict):
        raise SystemExit("ERROR: acquisition-index row must be an object")
    pq = row.get("pq")
    targets = row.get("super_souls")
    if type(pq) is not int or not 1 <= pq <= 186:
        raise SystemExit(f"ERROR: invalid acquisition-index PQ id: {pq!r}")
    if not isinstance(targets, list):
        raise SystemExit(f"ERROR: acquisition-index super_souls must be a list for PQ {pq}")
    for target in targets:
        if not isinstance(target, str) or not target.strip():
            raise SystemExit(f"ERROR: invalid acquisition-index Super Soul target at PQ {pq}")
        index_targets.add(target)

if len(index_targets) != EXPECTED_INDEX_TARGETS:
    raise SystemExit(
        f"ERROR: expected {EXPECTED_INDEX_TARGETS} unique acquisition-index targets; found {len(index_targets)}"
    )

missing_index = sorted(relationship_targets - index_targets)
extra_index = sorted(index_targets - relationship_targets)
if missing_index:
    raise SystemExit(f"ERROR: relationship targets missing from acquisition index: {missing_index}")
if extra_index:
    raise SystemExit(f"ERROR: acquisition index contains unsupported extra targets: {extra_index}")

print(
    "PASS: recovered Super Soul PQ acquisition contract is consistent "
    f"({len(soul_rows)} relationships / {len(relationship_targets)} unique targets / "
    f"{len(index_targets)} indexed targets / {len(canonical_ids)} canonical records)."
)
