#!/usr/bin/env python3
"""Validate the critical canonical database recovery contract.

This is intentionally deterministic and does not infer missing research data.
It checks that the restored canonical skill corpus and its navigation artifacts
remain present, parseable, and identity-consistent.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
SKILL_INDEX = ROOT / "docs/data/skills-index.json"
SKILL_PQ = ROOT / "docs/data/skill-pq-reverse-index-2026-09-26.json"
PQ_REWARDS = ROOT / "docs/data/pq-reward-relationships.json"


def load(path: Path) -> dict:
    if not path.is_file():
        raise SystemExit(f"missing required database artifact: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"database artifact root must be an object: {path}")
    return value


def unique_ids(records: object, label: str) -> set[str]:
    if not isinstance(records, list):
        raise SystemExit(f"{label}.records must be a list")
    ids: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise SystemExit(f"{label}.records[{index}] must be an object")
        skill_id = record.get("id")
        if not isinstance(skill_id, str) or not skill_id:
            raise SystemExit(f"{label}.records[{index}].id must be a non-empty string")
        ids.append(skill_id)
    result = set(ids)
    if len(result) != len(ids):
        raise SystemExit(f"{label} contains duplicate skill IDs")
    return result


def main() -> None:
    skills = load(SKILLS)
    skill_index = load(SKILL_INDEX)
    skill_pq = load(SKILL_PQ)
    pq_rewards = load(PQ_REWARDS)

    skill_ids = unique_ids(skills, "skills")
    index_ids = unique_ids(skill_index, "skills-index")

    if index_ids != skill_ids:
        raise SystemExit("skills-index identity set does not exactly match skills.json")

    if skill_pq.get("canonical_skill_count") != len(skill_ids):
        raise SystemExit("skill-PQ reverse artifact canonical_skill_count does not match skills.json")
    pq_ids = skill_pq.get("pq_ids")
    if not isinstance(pq_ids, dict):
        raise SystemExit("skill-PQ reverse artifact pq_ids must be an object")
    derived_edges = 0
    derived_represented = 0
    seen_reverse_edges: set[tuple[str, str]] = set()
    for pq_id, entry in pq_ids.items():
        if not isinstance(pq_id, str) or not pq_id.startswith("pq-") or not pq_id[3:].isdigit():
            raise SystemExit(f"skill-PQ reverse artifact has invalid PQ identity: {pq_id!r}")
        if not isinstance(entry, dict):
            raise SystemExit(f"skill-PQ reverse artifact entry {pq_id!r} must be an object")
        skill_refs = entry.get("skill_ids")
        if not isinstance(skill_refs, list):
            raise SystemExit(f"skill-PQ reverse artifact {pq_id!r}.skill_ids must be a list")
        if skill_refs and any(not isinstance(ref, str) or not ref for ref in skill_refs):
            raise SystemExit(f"skill-PQ reverse artifact {pq_id!r} contains a malformed skill ID")
        if len(set(skill_refs)) != len(skill_refs):
            raise SystemExit(f"skill-PQ reverse artifact {pq_id!r} contains duplicate skill IDs")
        unknown = sorted(set(skill_refs) - skill_ids)
        if unknown:
            raise SystemExit(f"skill-PQ reverse artifact {pq_id!r} references unknown canonical skills: {unknown[:5]!r}")
        for skill_ref in skill_refs:
            edge = (pq_id, skill_ref)
            if edge in seen_reverse_edges:
                raise SystemExit(f"duplicate skill-PQ reverse edge: {edge!r}")
            seen_reverse_edges.add(edge)
        derived_edges += len(skill_refs)
        derived_represented += bool(skill_refs)
    if skill_pq.get("total_skill_pq_edges") != derived_edges:
        raise SystemExit("skill-PQ reverse artifact edge count does not match its projection")
    if skill_pq.get("represented_pq_count") != derived_represented:
        raise SystemExit("skill-PQ reverse artifact represented PQ count does not match its projection")

    reward_rows = pq_rewards.get("verified_relationships")
    if not isinstance(reward_rows, list):
        raise SystemExit("PQ reward verified_relationships must be a list")
    current_counts = pq_rewards.get("current_counts")
    required_counts = {"skill", "super_soul", "equipment", "character", "dlc", "farming"}
    if not isinstance(current_counts, dict) or set(current_counts) != required_counts:
        raise SystemExit("PQ reward current_counts contract is malformed")
    relation_map = {
        "skill": "pq_rewards_skill",
        "super_soul": "pq_rewards_super_soul",
        "equipment": "pq_rewards_equipment",
        "character": "pq_features_character",
        "dlc": "pq_requires_dlc",
        "farming": "pq_farming_route",
    }
    actual_counts = {key: 0 for key in required_counts}
    seen_reward_keys: set[tuple[str, str, str]] = set()
    for index, row in enumerate(reward_rows):
        if not isinstance(row, dict):
            raise SystemExit(f"PQ reward relationship row {index} must be an object")
        pq_id = row.get("pq")
        target = row.get("target")
        relationship = row.get("relationship")
        if not isinstance(pq_id, str) or not pq_id.startswith("pq-") or not pq_id[3:].isdigit():
            raise SystemExit(f"PQ reward relationship row {index} has invalid PQ identity: {pq_id!r}")
        if not isinstance(target, str) or not target.strip():
            raise SystemExit(f"PQ reward relationship row {index} has an empty/non-string target")
        matched = [key for key, rel in relation_map.items() if relationship == rel]
        if not matched:
            raise SystemExit(f"PQ reward relationship row {index} has unknown relationship type: {relationship!r}")
        source = row.get("source")
        if not isinstance(source, str) or not source.strip():
            raise SystemExit(f"PQ reward relationship row {index} has an empty/non-string source")
        identity = (pq_id, relationship, target)
        if identity in seen_reward_keys:
            raise SystemExit(f"duplicate canonical PQ reward relationship key: {identity!r}")
        seen_reward_keys.add(identity)
        actual_counts[matched[0]] += 1
    for key, count in current_counts.items():
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise SystemExit(f"PQ reward current_counts[{key!r}] must be a non-negative integer")
    if actual_counts != current_counts:
        raise SystemExit(f"PQ reward current_counts mismatch: stored={current_counts!r}, actual={actual_counts!r}")
    if sum(actual_counts.values()) != sum(current_counts.values()):
        raise SystemExit("PQ reward relationship total does not equal the stored current_counts total")

    print("PASS: canonical database recovery contract is structurally intact.")
    print(f"canonical skills: {len(skill_ids)}")
    print("skills-index identities: exact match")
    print(f"skill→PQ reverse: {len(skill_ids)} skills / {derived_edges} edges / {derived_represented} represented PQs")
    print("PQ reward relationship count keys: skill, super_soul, equipment, character, dlc, farming")


if __name__ == "__main__":
    main()
