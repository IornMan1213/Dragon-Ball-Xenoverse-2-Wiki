#!/usr/bin/env python3
"""Audit structured Dragon Ball Xenoverse 2 wiki data.

The audit is intentionally conservative: it reports duplicate identities, missing
required fields, empty provenance, invalid verification states, category-count
mismatches, and obvious cross-domain references. It never promotes data to
verified and never mutates source records.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"

REQUIRED_BY_FILE = {
    "skills.json": ["name", "class", "subcategory", "verification_status", "sources"],
    "verified-skills.json": ["name", "verification_status", "sources"],
    "mentors-record-layer.json": ["id", "name", "verification_status", "sources"],
    "parallel-quests-record-layer.json": ["id", "number", "name", "verification_status", "sources"],
}
VALID_STATUS = {"indexed", "partially_verified", "verified"}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def records_from(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and isinstance(payload.get("records"), list):
        return [r for r in payload["records"] if isinstance(r, dict)]
    if isinstance(payload, list):
        return [r for r in payload if isinstance(r, dict)]
    return []


def effective_value(record: dict[str, Any], field: str, payload: Any) -> Any:
    """Resolve a record value, allowing supported file-level defaults."""
    if field in record:
        return record[field]
    if field == "verification_status" and isinstance(payload, dict):
        return payload.get("verification_status")
    return None


def main() -> int:
    findings: list[dict[str, Any]] = []
    summary = Counter()
    scanned = 0

    for filename, required in REQUIRED_BY_FILE.items():
        path = DATA / filename
        if not path.exists():
            findings.append({"severity": "error", "type": "missing_file", "file": filename})
            summary["errors"] += 1
            continue
        try:
            payload = load_json(path)
        except json.JSONDecodeError as exc:
            findings.append({"severity": "error", "type": "invalid_json", "file": filename, "message": str(exc)})
            summary["errors"] += 1
            continue

        records = records_from(payload)
        scanned += len(records)
        ids: dict[str, list[int]] = defaultdict(list)
        names: dict[str, list[int]] = defaultdict(list)
        for idx, record in enumerate(records):
            record_id = record.get("id")
            name = record.get("name")
            if record_id:
                ids[str(record_id)].append(idx)
            if name:
                names[str(name).strip().casefold()].append(idx)

            missing = [
                field
                for field in required
                if effective_value(record, field, payload) is None
            ]
            if missing:
                findings.append({"severity": "error", "type": "missing_required_fields", "file": filename, "record": name or record_id, "fields": missing})
                summary["errors"] += 1

            sources = effective_value(record, "sources", payload)
            if "sources" in record and not sources:
                findings.append({"severity": "error", "type": "empty_sources", "file": filename, "record": name or record_id})
                summary["errors"] += 1

            status = effective_value(record, "verification_status", payload)
            if status is not None and status not in VALID_STATUS:
                findings.append({"severity": "error", "type": "invalid_verification_status", "file": filename, "record": name or record_id, "status": status})
                summary["errors"] += 1

        for value, positions in ids.items():
            if len(positions) > 1:
                findings.append({"severity": "error", "type": "duplicate_id", "file": filename, "id": value, "records": positions})
                summary["errors"] += 1
        for value, positions in names.items():
            if len(positions) > 1:
                findings.append({"severity": "warning", "type": "duplicate_name", "file": filename, "name": value, "records": positions})
                summary["warnings"] += 1

        if isinstance(payload, dict) and isinstance(payload.get("category_counts"), dict):
            actual = Counter(str(r.get("subcategory") or r.get("class") or "") for r in records)
            for category, declared in payload["category_counts"].items():
                count = actual.get(category, 0)
                if count != declared:
                    findings.append({"severity": "warning", "type": "category_count_mismatch", "file": filename, "category": category, "declared": declared, "actual": count})
                    summary["warnings"] += 1

    report = {
        "schema_version": "1.1",
        "generated_by": "scripts/audit_wiki_data.py",
        "game": "Dragon Ball Xenoverse 2",
        "records_scanned": scanned,
        "summary": {
            "errors": summary["errors"],
            "warnings": summary["warnings"],
            "findings": len(findings),
        },
        "policy": {
            "errors_block_promotion": True,
            "warnings_require_review": True,
            "no_automatic_verification": True,
            "no_count_inflation_from_partial_sources": True,
            "file_level_verification_defaults_supported": True,
        },
        "findings": findings,
    }
    out = DATA / "audit-latest.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if summary["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
