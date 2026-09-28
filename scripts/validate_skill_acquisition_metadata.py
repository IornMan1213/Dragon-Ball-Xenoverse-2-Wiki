#!/usr/bin/env python3
"""Validate internal acquisition metadata consistency for the canonical skill corpus."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/data/skills.json"

def fail(message):
    raise SystemExit(f"ERROR: {message}")

try:
    data = json.loads(DATA.read_text(encoding="utf-8"))
except Exception as exc:
    fail(f"skills.json: invalid JSON: {exc}")

if not isinstance(data, dict):
    fail("skills root must be an object")
records = data.get("records")
if not isinstance(records, list):
    fail("records must be a list")
expected_count = len(records)  # derive the recovered canonical corpus size at validation time; do not freeze a pre-recovery count
if any(not isinstance(r, dict) for r in records):
    fail("every skill record must be an object")

required_fields = ("id", "name", "unlock_method", "source_quest_or_shop", "acquisition_type")
for i, record in enumerate(records):
    missing = [field for field in required_fields if field not in record]
    if missing:
        fail(f"record {i} missing required acquisition fields: {missing}")
    for field in ("id", "name", "unlock_method", "source_quest_or_shop", "acquisition_type"):
        value = record[field]
        if not isinstance(value, str) or not value.strip():
            fail(f"record {i} {field} must be a non-empty string")

ids = [record["id"] for record in records]
if len(set(ids)) != expected_count:
    fail(f"canonical skill IDs must be unique ({expected_count} canonical records expected)")

anomalies = []
invalid_pq_endpoints = []
for record in records:
    skill_id = record["id"]
    pq = record.get("source_parallel_quests", [])
    if not isinstance(pq, list):
        fail(f"source_parallel_quests must be a list for {skill_id}")
    invalid = [
        {"skill_id": skill_id, "pq_id": pq_id}
        for pq_id in pq
        if not isinstance(pq_id, int) or isinstance(pq_id, bool) or not 1 <= pq_id <= 186
    ]
    invalid_pq_endpoints.extend(invalid)
    if not invalid and len(pq) != len(set(pq)):
        fail(f"source_parallel_quests must not contain duplicate PQ IDs for {skill_id}")
    acquisition_type = record["acquisition_type"]
    unlock_method = record["unlock_method"].lower()
    if acquisition_type == "tp_medal_shop" and "tp medal shop" not in unlock_method:
        anomalies.append(skill_id)
    if acquisition_type == "skill_shop" and "skill shop" not in unlock_method:
        anomalies.append(skill_id)
    if acquisition_type == "parallel_quest" and not pq:
        anomalies.append(skill_id)
    if acquisition_type != "parallel_quest" and pq and "parallel quest" not in unlock_method:
        anomalies.append(skill_id)

if invalid_pq_endpoints:
    fail(f"invalid PQ endpoints: {invalid_pq_endpoints}")
if anomalies:
    fail(f"acquisition metadata anomalies: {anomalies}")

print(f"PASS: {expected_count} canonical records; acquisition schema, acquisition_type/unlock_method/PQ endpoint consistency, unique PQ endpoints, and PQ endpoint ranges hold.")
