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


def validate_skill_semantics(path: Path, record: dict, errors: list[str]) -> None:
    """Reject certainty that the research model cannot substantiate.

    In particular, ``ultimate_finish_required: false`` is not a safe default:
    an audit that merely fails to establish an Ultimate Finish requirement must
    use null. A negative assertion is accepted only when the record carries an
    explicit evidence field explaining how that negative was established.
    """
    uf = record.get("ultimate_finish_required")
    if uf not in (None, True, False):
        errors.append(
            f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: "
            f"ultimate_finish_required must be true, false, or null"
        )
    if uf is False and not record.get("ultimate_finish_evidence"):
        errors.append(
            f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: "
            "ultimate_finish_required=false requires explicit ultimate_finish_evidence; "
            "use null when the requirement is unresolved"
        )

    # A CaC claim is allowed only when the research record identifies some
    # player-character basis. This catches accidental blanket true values while
    # avoiding an overly narrow requirement for a particular race restriction.
    if record.get("usable_by_cac") is True:
        has_cac_basis = any(
            record.get(field) not in (None, "", [])
            for field in ("race_restriction", "character_source", "unlock_method")
        )
        if not has_cac_basis:
            errors.append(
                f"{path.relative_to(ROOT)}: {record.get('name', '<unnamed>')}: "
                "usable_by_cac=true lacks a player-character evidence field"
            )


def main() -> int:
    errors: list[str] = []
    files_checked = 0
    skill_records = pq_records = awoken_records = 0
    skill_keys: dict[tuple[str, str, str], list[str]] = {}
    pq_numbers: dict[int, list[str]] = {}

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
            if directory == SKILL_DIR:
                for r in rs:
                    if not isinstance(r, dict) or not r.get("name"):
                        errors.append(f"{path.relative_to(ROOT)}: record missing name")
                        continue
                    skill_records += 1
                    validate_skill_semantics(path, r, errors)
                    key = (str(r["name"]).casefold(), str(r.get("class", "")), str(r.get("subcategory", "")))
                    # A correction intentionally references the same canonical key
                    # as its historical record. It is not duplicate coverage: the
                    # builder applies the correction over the earlier record.
                    if r.get("correction_of"):
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


if __name__=='__main__':
    raise SystemExit(main())
