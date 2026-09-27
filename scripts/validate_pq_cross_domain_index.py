#!/usr/bin/env python3
"""Validate the canonical PQ cross-domain index contract without inventing relationship data."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs/data/pq-cross-domain-index.json"
EXPECTED_PQS = 186
EXPECTED_ENTITIES = {"skills", "super_souls", "equipment", "accessories", "characters", "dlc", "farming"}

def main() -> int:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    failures: list[str] = []

    if not isinstance(data, dict):
        failures.append("index root must be an object")
        data = {}

    if data.get("schema_version") != "1.0":
        failures.append("schema_version must be 1.0")
    if data.get("scope") != "PQ 1-186":
        failures.append("scope must be exactly 'PQ 1-186'")

    forward = data.get("forward_index")
    if not isinstance(forward, str) or not forward.strip():
        failures.append("forward_index must be a non-empty string")
    elif not (ROOT / forward).is_file():
        failures.append(f"forward_index file missing: {forward}")

    entries = data.get("reverse_indexes_to_generate")
    if not isinstance(entries, list):
        failures.append("reverse_indexes_to_generate must be a list")
        entries = []

    if len(entries) != len(EXPECTED_ENTITIES):
        failures.append(f"reverse_indexes_to_generate must contain exactly {len(EXPECTED_ENTITIES)} entries")

    seen_entities: set[str] = set()
    seen_reports: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            failures.append(f"reverse-index entry must be an object: {entry!r}")
            continue
        entity = entry.get("entity")
        if not isinstance(entity, str) or not entity.strip():
            failures.append(f"reverse-index entity must be a non-empty string: {entry!r}")
            continue
        if entity in seen_entities:
            failures.append(f"duplicate reverse-index entity: {entity}")
        seen_entities.add(entity)

        report = entry.get("report")
        if not isinstance(report, str) or not report.strip():
            failures.append(f"reverse-index report must be a non-empty string: {entity}")
        elif report in seen_reports:
            failures.append(f"duplicate reverse-index report: {report}")
        else:
            seen_reports.add(report)
        if entity != "farming":
            for field in ("key", "value"):
                if not isinstance(entry.get(field), str) or not entry[field].strip():
                    failures.append(f"{entity} reverse-index {field} must be a non-empty string")
        if entity == "farming":
            source = entry.get("source")
            if not isinstance(source, str) or not source.strip():
                failures.append("farming reverse-index source must be a non-empty string")
            elif source != forward:
                failures.append("farming reverse-index source must equal forward_index")

    if len(seen_reports) != len(entries):
        failures.append("reverse-index reports must be unique for every entry")

    if seen_entities != EXPECTED_ENTITIES:
        failures.append(f"reverse-index entities differ from expected set: {sorted(seen_entities)}")

    rule = data.get("completion_rule")
    if not isinstance(rule, str) or not rule.strip():
        failures.append("completion_rule must be a non-empty string")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        return 1

    print(f"PASS: PQ cross-domain index schema valid; {EXPECTED_PQS} PQ scope; {len(entries)} reverse-index entries; unique reports; entities={sorted(seen_entities)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
