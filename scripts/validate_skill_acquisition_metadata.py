#!/usr/bin/env python3
"""Validate skill acquisition metadata against canonical PQ→skill associations.

The canonical source_parallel_quests field is the complete relationship set.
source_quest/source_quest_or_shop are primary presentation/source fields and may
name only one member of that set. This validator therefore rejects explicit PQ
numbers outside the canonical set, but does not require primary-source fields
to enumerate every associated PQ.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
REL = ROOT / "docs/data/pq-reward-relationships.json"
PATTERN = re.compile(r"\b(?:PQ|Parallel Quest)\s*#?\s*(\d{1,3})\b", re.I)

def nums(value):
    return {int(m.group(1)) for m in PATTERN.finditer(str(value or ""))}

def main():
    skills = json.loads(SKILLS.read_text(encoding="utf-8"))["records"]
    rels = json.loads(REL.read_text(encoding="utf-8"))["verified_relationships"]
    graph = {}
    for e in rels:
        if e.get("relationship") == "pq_rewards_skill":
            graph.setdefault(e["target"], set()).add(int(e["pq"].replace("pq-", "")))

    missing_graph = []
    metadata_outside_graph = []
    for record in skills:
        name = record["name"]
        canonical = set(map(int, record.get("source_parallel_quests", [])))
        expected = graph.get(name, set())
        if canonical != expected:
            missing_graph.append({
                "name": name,
                "source_parallel_quests": sorted(canonical),
                "canonical_graph": sorted(expected),
            })
        explicit = nums(record.get("source_quest")) | nums(record.get("source_quest_or_shop"))
        outside = sorted(explicit - canonical)
        if outside:
            metadata_outside_graph.append({
                "name": name,
                "explicit_pqs": sorted(explicit),
                "canonical_pqs": sorted(canonical),
                "outside_canonical": outside,
            })

    result = {
        "schema_version": "1.0.0",
        "skill_count": len(skills),
        "canonical_pq_skill_edges": sum(1 for e in rels if e.get("relationship") == "pq_rewards_skill"),
        "canonical_crosslink_mismatches": missing_graph,
        "primary_source_outside_canonical": metadata_outside_graph,
        "primary_source_subset_rule": "source_quest/source_quest_or_shop may name a single primary PQ; they must not name a PQ outside source_parallel_quests.",
        "status": "clean" if not missing_graph and not metadata_outside_graph else "unresolved",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "clean" else 1

if __name__ == "__main__":
    raise SystemExit(main())
