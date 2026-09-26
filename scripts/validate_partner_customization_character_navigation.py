#!/usr/bin/env python3
"""Validate Partner Customization key -> canonical character navigation.

This validator checks only deterministic identity/navigation contracts. It does not
promote DLC ownership, raid history, or other partially verified metadata into
canonical character relationships.
"""
from __future__ import annotations
import json
import re
from collections import Counter
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
    bridge_records = bridge.get("records", [])
    bridge_ids = [x.get("character_id") for x in bridge_records]
    bridge_by_id = {x.get("character_id"): x.get("canonical_character_name") for x in bridge_records if x.get("character_id") is not None}
    duplicate_bridge_ids = sorted(k for k,v in Counter(bridge_ids).items() if k is not None and v > 1)
    malformed_bridge_ids = [{"character_id": x.get("character_id"), "type": type(x.get("character_id")).__name__} for x in bridge_records if x.get("character_id") is not None and not isinstance(x.get("character_id"), str)]
    canonical = set(chars.get("character_names", []))

    expected = list(range(1, 21))
    key_numbers = [x.get("key_number") for x in key_records]
    recon_numbers = [x.get("key") for x in recon_records]
    duplicate_key_numbers = sorted(k for k,v in Counter(key_numbers).items() if k is not None and v > 1)
    duplicate_recon_numbers = sorted(k for k,v in Counter(recon_numbers).items() if k is not None and v > 1)
    malformed_key_numbers = [{"key_number": x.get("key_number"), "type": type(x.get("key_number")).__name__} for x in key_records if x.get("key_number") is not None and not isinstance(x.get("key_number"), int)]
    malformed_recon_numbers = [{"key": x.get("key"), "type": type(x.get("key")).__name__} for x in recon_records if x.get("key") is not None and not isinstance(x.get("key"), int)]

    failures = []
    checks = {
        "exact_key_count": len(key_records) == 20,
        "exact_key_numbers": sorted(key_numbers) == expected,
        "exact_reconciliation_count": len(recon_records) == 20,
        "reconciliation_key_numbers": sorted(recon_numbers) == expected,
        "key_numbers_unique": not duplicate_key_numbers,
        "reconciliation_key_numbers_unique": not duplicate_recon_numbers,
        "all_key_character_ids_bridged": all(x.get("character_id") in bridge_by_id for x in key_records),
        "all_bridge_targets_canonical": all(name in canonical for name in bridge_by_id.values()),
        "bridge_ids_unique": not duplicate_bridge_ids,
        "bridge_id_fields_are_strings": not malformed_bridge_ids,
        "key_reconciliation_identity_parity": False,
        "key_reconciliation_join_keys_exact": False,
    }
    key_by_number = {x.get("key_number"): x for x in key_records}
    recon_by_number = {x.get("key"): x for x in recon_records}
    common_numbers = set(key_by_number) & set(recon_by_number)
    checks["key_reconciliation_join_keys_exact"] = (
        len(common_numbers) == 20
        and set(key_by_number) == set(recon_by_number) == set(expected)
    )
    checks["key_reconciliation_identity_parity"] = checks["key_reconciliation_join_keys_exact"] and all(
        key_by_number[n].get("character_id") == recon_by_number[n].get("character_id")
        and key_by_number[n].get("partner") == recon_by_number[n].get("partner")
        for n in expected
    )
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
    checks["page_search_link_targets_match_partner_names"] = all(name in expected_names for name, _ in search_links)
    checks["all_key_partners_have_search_links"] = not missing_links
    checks["no_unmapped_extra_partner_search_links"] = not extra_links

    checks["key_number_fields_are_integers"] = not malformed_key_numbers
    checks["reconciliation_key_fields_are_integers"] = not malformed_recon_numbers
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
        "duplicate_key_numbers": duplicate_key_numbers,
        "duplicate_reconciliation_key_numbers": duplicate_recon_numbers,
        "duplicate_bridge_character_ids": duplicate_bridge_ids,
        "malformed_bridge_character_ids": malformed_bridge_ids,
        "malformed_key_numbers": malformed_key_numbers,
        "malformed_reconciliation_key_numbers": malformed_recon_numbers,
        "identity_mismatches": [x for x in failures if isinstance(x, dict)],
        "status": "clean" if not failures else "unresolved",
        "evidence_boundary": "This audit validates identity/navigation only. It does not verify DLC ownership, raid rotation, TP Medal costs, or other partially verified Partner Customization facts.",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not failures else 1

if __name__ == "__main__":
    raise SystemExit(main())
