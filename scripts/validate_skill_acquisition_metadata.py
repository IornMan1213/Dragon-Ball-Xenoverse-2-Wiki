#!/usr/bin/env python3
"""Validate internal acquisition metadata consistency for the canonical skill corpus."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"docs/data/skills.json").read_text(encoding="utf-8"))
assert isinstance(data, dict), "skills root must be an object"
records=data.get("records")
assert isinstance(records, list), "records must be a list"
assert len(records)==474, f"skill record count {len(records)} != 474"
assert all(isinstance(r, dict) for r in records), "every skill record must be an object"
required_fields=("id", "name", "unlock_method", "source_quest_or_shop", "acquisition_type")
assert all(all(field in r for field in required_fields) for r in records), "every skill record must expose required acquisition fields"
assert len({r["id"] for r in records})==474, "canonical skill IDs must be unique"
assert all(isinstance(r["id"], str) and r["id"].strip() for r in records), "canonical skill IDs must be non-empty strings"
assert all(isinstance(r["name"], str) and r["name"].strip() for r in records), "skill names must be non-empty strings"
assert all(isinstance(r["unlock_method"], str) and r["unlock_method"].strip() for r in records)
assert all(isinstance(r["source_quest_or_shop"], str) and r["source_quest_or_shop"].strip() for r in records)
assert all(isinstance(r["acquisition_type"], str) and r["acquisition_type"].strip() for r in records)
anomalies=[]
invalid_pq_endpoints=[]
for r in records:
    pq=r.get("source_parallel_quests") or []
    assert isinstance(pq, list), f"source_parallel_quests must be a list for {r["id"]}"
    assert len(pq) == len(set(pq)), f"source_parallel_quests must not contain duplicate PQ IDs for {r["id"]}"
    invalid_pq_endpoints.extend({"skill_id": r["id"], "pq_id": pq_id} for pq_id in pq if not isinstance(pq_id, int) or isinstance(pq_id, bool) or not 1 <= pq_id <= 186)
    a=r["acquisition_type"]; u=str(r["unlock_method"]).lower()
    if a=="tp_medal_shop" and "tp medal shop" not in u: anomalies.append(r["id"])
    if a=="skill_shop" and "skill shop" not in u: anomalies.append(r["id"])
    if a=="parallel_quest" and not pq: anomalies.append(r["id"])
    if a!="parallel_quest" and pq and "parallel quest" not in u: anomalies.append(r["id"])
assert not invalid_pq_endpoints, invalid_pq_endpoints
assert not anomalies, anomalies
print("PASS: 474 records; acquisition schema, acquisition_type/unlock_method/PQ endpoint consistency, unique PQ endpoints, and PQ endpoint ranges hold.")
