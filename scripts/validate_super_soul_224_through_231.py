#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/data/super-souls-record-layer.json"
EXPECTED = {
    "super-soul-224", "super-soul-225", "super-soul-226", "super-soul-227",
    "super-soul-228", "super-soul-229", "super-soul-230", "super-soul-231",
}

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    records = {r["id"]: r for r in payload["records"]}
    missing = sorted(EXPECTED - records.keys())
    stale = sorted(i for i in EXPECTED if i in records and records[i].get("last_verified") != "2026-09-22")
    unresolved_effects = sorted(i for i in EXPECTED if i in records and not records[i].get("effect_text"))
    unresolved_sources = sorted(i for i in EXPECTED if i in records and not records[i].get("sources"))
    out = {
        "schema_version": "1.0.0",
        "scope": "bounded Super Soul provenance/mechanics batch validation",
        "records": sorted(EXPECTED),
        "missing_ids": missing,
        "stale_last_verified": stale,
        "missing_effect_text": unresolved_effects,
        "missing_sources": unresolved_sources,
        "status": "clean" if not (missing or stale or unresolved_effects or unresolved_sources) else "unresolved",
    }
    print(json.dumps(out, indent=2))
    return 0 if out["status"] == "clean" else 1

if __name__ == "__main__":
    raise SystemExit(main())
