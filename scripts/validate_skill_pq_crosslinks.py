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

try:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    raise SystemExit(f"{SKILLS}: invalid JSON: {exc}")
if not isinstance(data, dict):
    raise SystemExit("skills root must be an object")
records = data.get("records") if isinstance(data, dict) else None
if not isinstance(records, list): raise SystemExit("canonical skill records must be a list")
if len(records) != EXPECTED_SKILLS: raise SystemExit(f"skill count {len(records)} != {EXPECTED_SKILLS}")
if any(not isinstance(r, dict) for r in records): raise SystemExit("every canonical skill record must be an object")
if any(not isinstance(r.get("id"), str) or not r.get("id").strip() for r in records): raise SystemExit("every canonical skill must have a non-empty string id")
if any(not isinstance(r.get("name"), str) or not r.get("name").strip() for r in records): raise SystemExit("every canonical skill must have a non-empty string name")
assert all("source_parallel_quests" not in r or isinstance(r["source_parallel_quests"], list) for r in records), "source_parallel_quests must be a list when present"
for record in records:
    endpoints = record.get("source_parallel_quests", [])
    for pq_id in endpoints:
        assert isinstance(pq_id, int) and not isinstance(pq_id, bool) and 1 <= pq_id <= 186, (record["id"], pq_id)
    assert len(endpoints) == len(set(endpoints)), f"duplicate source_parallel_quests IDs: {record['id']}"
ids = [r["id"] for r in records]
if len(set(ids)) != EXPECTED_SKILLS: raise SystemExit("duplicate canonical skill IDs")

# Keep the checked-in reverse artifact synchronized with the deterministic source projection.
# A count-only check can pass while individual PQ edges drift.
existing_reverse = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else None
if existing_reverse is not None:
    assert isinstance(existing_reverse, dict), "checked-in reverse index root must be an object"
    assert existing_reverse.get("schema_version") == "1.0", "checked-in reverse index schema_version must be 1.0"
    assert existing_reverse.get("scope") == "Canonical skill dataset → Parallel Quest reverse navigation", "checked-in reverse index scope drift"
    assert existing_reverse.get("source") == "docs/data/skills.json", "checked-in reverse index source drift"
    assert existing_reverse.get("generated_on") == "2026-09-26", "checked-in reverse index generated_on drift"
    assert existing_reverse.get("canonical_skill_count") == EXPECTED_SKILLS, "checked-in reverse index canonical skill count drift"
    assert existing_reverse.get("represented_pq_count") == EXPECTED_REPRESENTED_PQS, "checked-in reverse index represented PQ count drift"
    assert existing_reverse.get("total_skill_pq_edges") == EXPECTED_EDGES, "checked-in reverse index edge count drift"

by_pq = {str(i): [] for i in range(1, 187)}
for record in records:
    for pq_id in record.get("source_parallel_quests", []):
        assert isinstance(pq_id, int) and not isinstance(pq_id, bool) and 1 <= pq_id <= 186, (record["id"], pq_id)
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
