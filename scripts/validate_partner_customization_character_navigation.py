#!/usr/bin/env python3
"""Validate Partner Customization key -> canonical character navigation.

This validator checks only deterministic identity/navigation contracts. It does not
promote DLC ownership, raid history, or other partially verified metadata into
canonical character relationships.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"

def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def main() -> int:
    keys = load("partner-customization-key-record-layer.json")
    recon = load("partner-customization-key-reconciliation.json")
    bridge = load("characters/character-id-identity-bridge.json")
    chars = load("characters-record-layer.json")
    page = (ROOT / "docs" / "Partner-Customization.md").read_text(encoding="utf-8")

    key_records = keys.get("records", [])
    recon_records = recon.get("records", [])
    bridge_by_id = {x.get("character_id"): x.get("canonical_character_name") for x in bridge.get("records", [])}
    canonical = set(chars.get("character_names", []))

    expected = list(range(1, 21))
    key_numbers = [x.get("key_number") for x in key_records]
    recon_numbers = [x.get("key") for x in recon_records]

    failures = []
    checks = {
        "exact_key_count": len(key_records) == 20,
        "exact_key_numbers": sorted(key_numbers) == expected,
        "exact_reconciliation_count": len(recon_records) == 20,
        "reconciliation_key_numbers": sorted(recon_numbers) == expected,
        "all_key_character_ids_bridged": all(x.get("character_id") in bridge_by_id for x in key_records),
        "all_bridge_targets_canonical": all(name in canonical for name in bridge_by_id.values()),
        "key_reconciliation_identity_parity": all(
            (a.get("key_number") == b.get("key"))
            and (a.get("character_id") == b.get("character_id"))
            and (a.get("partner") == b.get("partner"))
            for a, b in zip(sorted(key_records, key=lambda x: x.get("key_number", 0)),
                             sorted(recon_records, key=lambda x: x.get("key", 0)))
        ),
    }
    for i, row in enumerate(key_records, 1):
        cid = row.get("character_id")
        partner = row.get("partner")
        if bridge_by_id.get(cid) != partner:
            failures.append({"key": row.get("key_number"), "character_id": cid,
                             "record_partner": partner, "bridge_name": bridge_by_id.get(cid)})
    search_links = re.findall(r'\[([^\]]+)\]\(Search/\?q=([^\)]+)\)', page)
    linked_names = {name for name, _ in search_links}
    expected_names = {x.get("partner") for x in key_records}
    missing_links = sorted(expected_names - linked_names)
    extra_links = sorted(linked_names - expected_names)
    checks["page_has_exactly_20_key_search_links"] = len(search_links) == 20
    checks["all_key_partners_have_search_links"] = not missing_links
    checks["no_unmapped_extra_partner_search_links"] = not extra_links

    for label, ok in checks.items():
        if not ok:
            failures.append(label)

    report = {
        "schema_version": "1.0.0",
        "scope": "Partner Customization key -> canonical character navigation",
        "canonical_sources": {
            "characters": "docs/data/characters-record-layer.json",
            "identity_bridge": "docs/data/characters/character-id-identity-bridge.json",
            "key_records": "docs/data/partner-customization-key-record-layer.json",
            "reconciliation": "docs/data/partner-customization-key-reconciliation.json",
            "page": "docs/Partner-Customization.md",
        },
        "counts": {
            "key_records": len(key_records),
            "reconciliation_records": len(recon_records),
            "bridge_records": len(bridge.get("records", [])),
            "canonical_character_names": len(canonical),
            "page_search_links": len(search_links),
        },
        "checks": checks,
        "missing_page_search_links": missing_links,
        "extra_page_search_links": extra_links,
        "identity_mismatches": [x for x in failures if isinstance(x, dict)],
        "status": "clean" if not failures else "unresolved",
        "evidence_boundary": "This audit validates identity/navigation only. It does not verify DLC ownership, raid rotation, TP Medal costs, or other partially verified Partner Customization facts.",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not failures else 1

if __name__ == "__main__":
    raise SystemExit(main())
