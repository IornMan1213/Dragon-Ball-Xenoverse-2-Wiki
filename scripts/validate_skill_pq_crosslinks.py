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

try:
    data = json.loads(SKILLS.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    raise SystemExit(f"{SKILLS}: invalid JSON: {exc}")
if not isinstance(data, dict):
    raise SystemExit("skills root must be an object")
records = data.get("records") if isinstance(data, dict) else None
if not isinstance(records, list): raise SystemExit("canonical skill records must be a list")
if any(not isinstance(r, dict) for r in records): raise SystemExit("every canonical skill record must be an object")
if any(not isinstance(r.get("id"), str) or not r.get("id").strip() for r in records): raise SystemExit("every canonical skill must have a non-empty string id")
if any(not isinstance(r.get("name"), str) or not r.get("name").strip() for r in records): raise SystemExit("every canonical skill must have a non-empty string name")
if any("source_parallel_quests" in r and not isinstance(r["source_parallel_quests"], list) for r in records): raise SystemExit("source_parallel_quests must be a list when present")
for record in records:
    endpoints = record.get("source_parallel_quests", [])
    for pq_id in endpoints:
        if not isinstance(pq_id, int) or isinstance(pq_id, bool) or not 1 <= pq_id <= 186: raise SystemExit(f"invalid source_parallel_quests value for {record['id']}: {pq_id!r}")
    if len(endpoints) != len(set(endpoints)): raise SystemExit(f"duplicate source_parallel_quests IDs: {record['id']}")
ids = [r["id"] for r in records]
if len(set(ids)) != len(records): raise SystemExit("duplicate canonical skill IDs")

# Keep the checked-in reverse artifact synchronized with the deterministic source projection.
# A count-only check can pass while individual PQ edges drift.
if OUT.exists():
    try:
        existing_reverse = json.loads(OUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"{OUT}: invalid JSON: {exc}")
else:
    existing_reverse = None
if existing_reverse is not None:
    if not isinstance(existing_reverse, dict): raise SystemExit("checked-in reverse index root must be an object")
    if existing_reverse.get("schema_version") != "1.0": raise SystemExit("checked-in reverse index schema_version must be 1.0")
    if existing_reverse.get("scope") != "Canonical skill dataset → Parallel Quest reverse navigation": raise SystemExit("checked-in reverse index scope drift")
    if existing_reverse.get("source") != "docs/data/skills.json": raise SystemExit("checked-in reverse index source drift")
    if existing_reverse.get("generated_on") != "2026-09-28": raise SystemExit("checked-in reverse index generated_on drift")
    if existing_reverse.get("canonical_skill_count") != len(records): raise SystemExit("checked-in reverse index canonical skill count drift")

by_pq = {str(i): [] for i in range(1, 187)}
for record in records:
    for pq_id in record.get("source_parallel_quests", []):
        if not isinstance(pq_id, int) or isinstance(pq_id, bool) or not 1 <= pq_id <= 186: raise SystemExit(f"invalid source_parallel_quests value for {record["id"]}: {pq_id!r}")
        by_pq[str(pq_id)].append({"skill_id": record["id"], "name": record["name"]})

edge_count = sum(len(v) for v in by_pq.values())
represented = sum(bool(v) for v in by_pq.values())
if edge_count != EXPECTED_EDGES: raise SystemExit(f"edge count {edge_count} != {EXPECTED_EDGES}")
if represented != EXPECTED_REPRESENTED_PQS: raise SystemExit(f"represented PQ count {represented} != {EXPECTED_REPRESENTED_PQS}")
if existing_reverse is not None:
    if existing_reverse.get("represented_pq_count") != represented: raise SystemExit("checked-in reverse index represented PQ count drift")
    if existing_reverse.get("total_skill_pq_edges") != edge_count: raise SystemExit("checked-in reverse index edge count drift")
expected_pq_ids = {pq: {"skill_count": len(items), "skill_ids": [x["skill_id"] for x in items], "skills": [x["name"] for x in items], "relationship_status": ("canonical_skill_endpoint_present" if items else "no_canonical_skill_endpoint_in_current_skill_corpus")} for pq, items in by_pq.items()}
if existing_reverse is not None:
    actual_projection = existing_reverse.get("pq_ids")
    if actual_projection != expected_pq_ids: raise SystemExit("checked-in reverse index differs from deterministic source_parallel_quests projection")

payload = {
    "schema_version": "1.0",
    "generated_on": "2026-09-28",
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
