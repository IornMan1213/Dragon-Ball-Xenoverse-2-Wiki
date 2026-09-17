#!/usr/bin/env python3
"""Offline integrity checks for checked-in research batches.

This intentionally does not judge factual correctness; it catches malformed JSON,
missing batch records, duplicate canonical keys within a batch, and duplicate PQ
numbers before an external corpus build is attempted.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "docs/data/skill-research-batches"
PQ_DIR = ROOT / "docs/data/parallel-quest-research-batches"
AWOKEN_DIR = ROOT / "docs/data/awoken-research-batches"


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def records(payload):
    if not isinstance(payload, dict):
        return []
    value = payload.get("corrections") or payload.get("records") or []
    return value if isinstance(value, list) else []


def main() -> int:
    errors: list[str] = []
    files_checked = 0
    skill_records = 0
    pq_records = 0
    awoken_records = 0

    skill_keys: dict[tuple[str, str, str], str] = {}
    pq_numbers: dict[int, str] = {}

    for directory, pattern in ((SKILL_DIR, "*.json"), (PQ_DIR, "pq-batch-*.json"), (AWOKEN_DIR, "*.json")):
        for path in sorted(directory.glob(pattern)):
            if "crosslink" in path.name or "numbering-reconciliation" in path.name:
                continue
            payload = load_json(path, errors)
            files_checked += 1
            if payload is None:
                continue
            rs = records(payload)
            if not rs:
                # Audit/index batches can legitimately contain metadata only.
                continue
            if directory == SKILL_DIR:
                for r in rs:
                    if not isinstance(r, dict) or not r.get("name"):
                        errors.append(f"{path.relative_to(ROOT)}: record missing name")
                        continue
                    skill_records += 1
                    key = (str(r["name"]).casefold(), str(r.get("class", "")), str(r.get("subcategory", "")))
                    previous = skill_keys.get(key)
                    if previous and previous == path.name:
                        errors.append(f"{path.relative_to(ROOT)}: duplicate skill key {key}")
                    skill_keys.setdefault(key, path.name)
            elif directory == PQ_DIR:
                local_numbers: set[int] = set()
                for r in rs:
                    if not isinstance(r, dict) or r.get("number") is None:
                        errors.append(f"{path.relative_to(ROOT)}: record missing PQ number")
                        continue
                    pq_records += 1
                    number = r["number"]
                    if not isinstance(number, int):
                        errors.append(f"{path.relative_to(ROOT)}: non-integer PQ number {number!r}")
                        continue
                    if number in local_numbers:
                        errors.append(f"{path.relative_to(ROOT)}: duplicate PQ number {number} inside batch")
                    local_numbers.add(number)
                    previous = pq_numbers.get(number)
                    if previous and previous != path.name:
                        errors.append(f"PQ{number} appears in both {previous} and {path.name}")
                    pq_numbers.setdefault(number, path.name)
            else:
                awoken_records += len(rs)

    if errors:
        print("Research-batch validation failed:")
        print("\n".join(dict.fromkeys(errors)))
        return 1

    print(f"Research batches validated offline: files={files_checked}, skill records={skill_records}, PQ records={pq_records}, Awoken records={awoken_records}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
