#!/usr/bin/env python3
"""Validate internal acquisition metadata consistency for the canonical skill corpus."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"docs/data/skills.json").read_text(encoding="utf-8"))
records=data["records"]
assert len(records)==474
assert all(r.get("unlock_method") for r in records)
assert all(r.get("source_quest_or_shop") for r in records)
assert all(r.get("acquisition_type") for r in records)
anomalies=[]
for r in records:
    a=r["acquisition_type"]; u=str(r["unlock_method"]).lower(); pq=r.get("source_parallel_quests") or []
    if a=="tp_medal_shop" and not ("tp medal shop" in u or "stp medal shop" in u): anomalies.append(r["id"])
    if a=="skill_shop" and "skill shop" not in u: anomalies.append(r["id"])
    if a=="parallel_quest" and not pq: anomalies.append(r["id"])
    if a!="parallel_quest" and pq and "parallel quest" not in u: anomalies.append(r["id"])
assert not anomalies, anomalies
print("PASS: 474 records; required acquisition fields present; acquisition_type/unlock_method/PQ endpoint consistency holds.")
