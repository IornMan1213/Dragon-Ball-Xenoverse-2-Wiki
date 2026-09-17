#!/usr/bin/env python3
"""Offline integrity checks for checked-in research batches."""
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


def validate_correction_metadata(path: Path, record: dict, errors: list[str]) -> None:
    """Ensure corrections carry enough identity/provenance to be deterministic."""
    correction = record.get("correction_of")
    fields = record.get("correction_fields")
    if correction is None:
        if fields is not None:
            errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: correction_fields requires correction_of")
        return
    if not isinstance(correction, dict):
        errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: correction_of must be an object")
        return
    if not correction.get("name"):
        errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: correction_of.name is required")
    if not isinstance(fields, list) or not fields or not all(isinstance(field, str) and field for field in fields):
        errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: correction_fields must be a non-empty list of field names")
    if "class" not in correction and "previous_class" not in correction:
        errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: correction_of must preserve the previous class")
    if "subcategory" not in correction and "previous_subcategory" not in correction:
        errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: correction_of must preserve the previous subcategory")


def validate_skill_semantics(path: Path, record: dict, errors: list[str], skip_uf: bool = False) -> None:
    """Reject certainty that the research model cannot substantiate."""
    validate_correction_metadata(path, record, errors)
    uf = record.get("ultimate_finish_required")
    if not skip_uf:
        if uf not in (None, True, False):
            errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: ultimate_finish_required must be true, false, or null")
        if uf is False and not has_explicit_negative_uf_evidence(record):
            errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: ultimate_finish_required=false lacks explicit non-Ultimate-Finish evidence; use null when unresolved")
    if record.get("usable_by_cac") is True:
        has_cac_basis = any(record.get(field) not in (None, "", []) for field in ("race_restriction", "character_source", "unlock_method"))
        if not has_cac_basis:
            errors.append(f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: usable_by_cac=true lacks a player-character evidence field")


def has_explicit_negative_uf_evidence(record: dict) -> bool:
    if record.get("ultimate_finish_evidence"):
        return True
    if record.get("verification_status") == "verified":
        return True
    text = " ".join(str(record.get(k, "")) for k in ("unlock_method", "source_quest_or_shop")).casefold()
    pq_route = "parallel quest" in text or "pq " in text
    if pq_route:
        return any(token in text for token in ("any clear", "first-clear", "normal clear", "basic reward", "standard reward", "not an ultimate finish", "not ultimate finish"))
    return any(token in text for token in ("skill shop", "tp medal shop", "mentor", "instructor quest", "extra story", "built into", "character-locked", "not obtainable", "shenron wish", "wish"))


def collect_uf_corrections() -> set[tuple[str, str, str]]:
    """Find canonical keys whose historical UF value is explicitly superseded."""
    corrected: set[tuple[str, str, str]] = set()
    if not SKILL_DIR.exists():
        return corrected
    for path in sorted(SKILL_DIR.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for r in records(payload):
            if not isinstance(r, dict):
                continue
            c = r.get("correction_of")
            if c and "ultimate_finish_required" in r.get("correction_fields", []):
                corrected.add((str(c.get("name", r.get("name", ""))).casefold(), str(c.get("previous_class", c.get("class", r.get("class", "")))), str(c.get("previous_subcategory", c.get("subcategory", "")))))
    return corrected


def main() -> int:
    errors: list[str] = []
    files_checked = 0
    skill_records = pq_records = awoken_records = 0
    skill_keys: dict[tuple[str, str, str], list[str]] = {}
    pq_numbers: dict[int, list[str]] = {}
    superseded_uf_keys = collect_uf_corrections()

    for directory, pattern in ((SKILL_DIR, "*.json"), (PQ_DIR, "pq-batch-*.json"), (AWOKEN_DIR, "*.json")):
        if not directory.exists():
            errors.append(f"Missing research directory: {directory.relative_to(ROOT)}")
            continue
        for path in sorted(directory.glob(pattern)):
            if "crosslink" in path.name or "numbering-reconciliation" in path.name:
                continue
            payload = load_json(path, errors)
            files_checked += 1
            if payload is None:
                continue
            rs = records(payload)
            if not rs:
                continue
            historical_duplicate = bool(payload.get("historical_duplicate_of"))
            if directory == SKILL_DIR:
                for r in rs:
                    if not isinstance(r, dict) or not r.get("name"):
                        errors.append(f"{path.relative_to(ROOT)}: record missing name")
                        continue
                    skill_records += 1
                    key = (str(r["name"]).casefold(), str(r.get("class", "")), str(r.get("subcategory", "")))
                    skip_uf = historical_duplicate or (not r.get("correction_of") and key in superseded_uf_keys)
                    if not historical_duplicate:
                        validate_skill_semantics(path, r, errors, skip_uf=skip_uf)
                    if historical_duplicate or r.get("correction_of"):
                        continue
                    skill_keys.setdefault(key, []).append(path.name)
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
                    pq_numbers.setdefault(number, []).append(path.name)
            else:
                awoken_records += len(rs)

    for key, files in skill_keys.items():
        unique = list(dict.fromkeys(files))
        if len(unique) > 1:
            errors.append(f"Duplicate non-correction skill key {key} across batches: {', '.join(unique)}")
    for number, files in pq_numbers.items():
        unique = list(dict.fromkeys(files))
        if len(unique) > 1:
            errors.append(f"PQ{number} appears in multiple batches: {', '.join(unique)}")

    if errors:
        print("Research-batch validation failed:")
        print("\n".join(dict.fromkeys(errors)))
        return 1
    print(f"Research batches validated offline: files={files_checked}, skill records={skill_records}, PQ records={pq_records}, Awoken records={awoken_records}.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
