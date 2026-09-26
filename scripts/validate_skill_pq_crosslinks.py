#!/usr/bin/env python3
"""Validate and regenerate the live skill→PQ reverse index.

This validator intentionally treats docs/data/skills.json as the canonical source.
It does not infer that a PQ has no skill rewards merely because no current skill record
points to it; it only validates explicit source_parallel_quests relationships.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "docs/data/skills.json"
OUT = ROOT / "docs/data/skill-pq-reverse-index-2026-09-26.json"

EXPECTED_SKILLS = 474
EXPECTED_EDGES = 246
EXPECTED_REPRESENTED_PQS = 170

data = json.loads(SKILLS.read_text(encoding="utf-8"))
records = data["records"]
ids = [r["id"] for r in records]
assert len(records) == EXPECTED_SKILLS, f"skill count {len(records)} != {EXPECTED_SKILLS}"
assert len(set(ids)) == EXPECTED_SKILLS, "duplicate canonical skill IDs"

# Keep the checked-in reverse artifact synchronized with the deterministic source projection.
# A count-only check can pass while individual PQ edges drift.
existing_reverse = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else None

by_pq = {str(i): [] for i in range(1, 187)}
for record in records:
    for pq_id in record.get("source_parallel_quests", []):
        assert isinstance(pq_id, int) and 1 <= pq_id <= 186, (record["id"], pq_id)
        by_pq[str(pq_id)].append({"skill_id": record["id"], "name": record["name"]})

edge_count = sum(len(v) for v in by_pq.values())
represented = sum(bool(v) for v in by_pq.values())
assert edge_count == EXPECTED_EDGES, f"edge count {edge_count} != {EXPECTED_EDGES}"
assert represented == EXPECTED_REPRESENTED_PQS, f"represented PQ count {represented} != {EXPECTED_REPRESENTED_PQS}"
expected_pq_ids = {pq: {"skill_count": len(items), "skill_ids": [x["skill_id"] for x in items], "skills": [x["name"] for x in items], "relationship_status": ("canonical_skill_endpoint_present" if items else "no_canonical_skill_endpoint_in_current_skill_corpus")} for pq, items in by_pq.items()}
if existing_reverse is not None:
    actual_projection = existing_reverse.get("pq_ids")
    assert actual_projection == expected_pq_ids, "checked-in reverse index differs from deterministic source_parallel_quests projection"

payload = {
    "schema_version": "1.0",
    "generated_on": "2026-09-26",
    "scope": "Canonical skill dataset → Parallel Quest reverse navigation",
    "source": "docs/data/skills.json",
    "canonical_skill_count": len(records),
    "represented_pq_count": represented,
    "total_skill_pq_edges": edge_count,
    "pq_ids": {
        pq: {
            "skill_count": len(items),
            "skill_ids": [x["skill_id"] for x in items],
            "skills": [x["name"] for x in items],
            "relationship_status": (
                "canonical_skill_endpoint_present" if items
                else "no_canonical_skill_endpoint_in_current_skill_corpus"
            ),
        }
        for pq, items in by_pq.items()
    },
}
OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"PASS: {len(records)} skills, {edge_count} skill→PQ edges, {represented} represented PQ IDs")
