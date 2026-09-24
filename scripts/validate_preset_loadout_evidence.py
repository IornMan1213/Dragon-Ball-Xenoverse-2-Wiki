#!/usr/bin/env python3
"""Validate preset/loadout evidence boundaries without inferring numeric mappings."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"

EXPECTED_NUMERIC_UNRESOLVED = {
    "goku-preset-2", "goku-preset-3", "goku-preset-4", "goku-preset-5",
    "goku-preset-6", "goku-preset-7", "goku-preset-8", "goku-preset-9",
    "goku-preset-10", "goku-preset-11", "goku-preset-12",
    "goku-preset-14", "goku-preset-15", "goku-preset-16", "goku-preset-17",
    "goku-preset-18", "vegeta-preset-10", "vegeta-preset-11",
    "captain-ginyu-preset-5", "captain-ginyu-preset-6",
}

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    data = load(DATA / "character-presets-record-layer.json")
    records = data.get("records", [])
    verified = [r for r in records if r.get("loadout_status") == "verified"]
    numeric_unresolved = {
        r.get("id") for r in records
        if r.get("id") in EXPECTED_NUMERIC_UNRESOLVED
        and r.get("loadout_status") != "verified"
    }
    invalid_verified = []
    for r in verified:
        if not isinstance(r.get("loadout"), dict):
            invalid_verified.append(r.get("id"))
            continue
        if not r.get("loadout_source"):
            invalid_verified.append(r.get("id"))
            continue
        if not isinstance(r.get("sources"), list) or not r.get("sources"):
            invalid_verified.append(r.get("id"))
    checks = {
        "record_ids_unique": len({r.get("id") for r in records}) == len(records),
        "verified_loadouts_have_required_evidence": not invalid_verified,
        "numeric_unresolved_boundary_preserved": numeric_unresolved == EXPECTED_NUMERIC_UNRESOLVED,
    }
    out = {
        "schema_version": "1.0.0",
        "scope": "preset/loadout evidence boundary",
        "canonical_records": len(records),
        "verified_loadouts": len(verified),
        "numeric_unresolved_expected": len(EXPECTED_NUMERIC_UNRESOLVED),
        "numeric_unresolved_present": len(numeric_unresolved),
        "invalid_verified_records": invalid_verified,
        "checks": checks,
        "status": "clean" if all(checks.values()) else "unresolved",
        "evidence_boundary": (
            "A numeric preset is not promoted to a complete loadout unless the canonical "
            "record contains a loadout object, explicit loadout_source, and non-empty sources. "
            "No row order, costume order, chapter order, or visual proximity may establish "
            "numeric-to-named loadout identity."
        ),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out["status"] == "clean" else 1

if __name__ == "__main__":
    raise SystemExit(main())
