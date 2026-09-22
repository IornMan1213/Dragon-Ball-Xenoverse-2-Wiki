#!/usr/bin/env python3
"""Validate published Character/DLC navigation and its canonical identity contracts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = {
    "docs/Characters.md": [
        ("character_explorer", "Characters-All.html", ROOT / "docs" / "Characters-All.html"),
        ("character_profiles", "Character-Core-Profiles.md", ROOT / "docs" / "Character-Core-Profiles.md"),
        ("dlc_character_audit", "data/characters/dlc-character-identity-audit.json", ROOT / "docs" / "data" / "characters" / "dlc-character-identity-audit.json"),
        ("dlc_character_bridge", "data/characters/dlc-character-identity-bridge.json", ROOT / "docs" / "data" / "characters" / "dlc-character-identity-bridge.json"),
    ],
    "docs/DLC-Overview.md": [
        ("canonical_dlc_identity", "./data/dlc/canonical-dlc-identity.json", ROOT / "docs" / "data" / "dlc" / "canonical-dlc-identity.json"),
        ("pq_reverse_index", "./data/dlc/pq-reverse-index.json", ROOT / "docs" / "data" / "dlc" / "pq-reverse-index.json"),
        ("pq_reverse_audit", "./data/dlc/pq-reverse-navigation-audit.json", ROOT / "docs" / "data" / "dlc" / "pq-reverse-navigation-audit.json"),
        ("future_saga_map", "./data/future-saga-content-map.json", ROOT / "docs" / "data" / "future-saga-content-map.json"),
        ("dlc_presentation_audit", "./data/dlc/dlc-presentation-consumer-audit.json", ROOT / "docs" / "data" / "dlc" / "dlc-presentation-consumer-audit.json"),
    ],
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    results = {}
    failures = []

    # Published-page local-link contract.
    for page, links in CHECKS.items():
        page_path = ROOT / page
        text = page_path.read_text(encoding="utf-8")
        page_results = []
        for label, href, target in links:
            present = href in text
            exists = target.exists()
            ok = present and exists
            page_results.append({
                "label": label,
                "href": href,
                "link_present": present,
                "target_exists": exists,
                "status": "clean" if ok else "unresolved",
            })
            if not ok:
                failures.append(f"{page}:{label}")
        results[page] = page_results

    # Character provenance bridge must resolve only to canonical character identities.
    character_layer = load(ROOT / "docs" / "data" / "characters-record-layer.json")
    canonical_characters = character_layer.get("character_names", [])
    canonical_character_set = set(canonical_characters)
    bridge = load(ROOT / "docs" / "data" / "characters" / "dlc-character-identity-bridge.json")
    bridge_records = bridge.get("records", [])
    bridge_missing_targets = sorted({
        record.get("canonical_character_name")
        for record in bridge_records
        if record.get("canonical_character_name") is not None
        and record.get("canonical_character_name") not in canonical_character_set
    })
    unresolved_with_target = [
        record.get("source_name")
        for record in bridge_records
        if record.get("status") == "unresolved_source_label"
        and record.get("canonical_character_name") is not None
    ]
    bridge_duplicate_sources = len(bridge_records) - len({
        record.get("source_name") for record in bridge_records
    })
    bridge_ok = (
        len(canonical_characters) == 149
        and len(canonical_character_set) == 149
        and len(bridge_records) == 15
        and not bridge_missing_targets
        and not unresolved_with_target
        and bridge_duplicate_sources == 0
    )
    results["character_identity_bridge"] = {
        "canonical_character_count": len(canonical_characters),
        "canonical_character_unique_count": len(canonical_character_set),
        "bridge_records": len(bridge_records),
        "bridge_duplicate_sources": bridge_duplicate_sources,
        "resolved_targets_missing_from_canonical": bridge_missing_targets,
        "unresolved_records_with_canonical_target": unresolved_with_target,
        "status": "clean" if bridge_ok else "unresolved",
    }
    if not bridge_ok:
        failures.append("character_identity_bridge")

    # Canonical DLC identity must resolve every existing PQ→DLC endpoint exactly once.
    relationship_data = load(ROOT / "docs" / "data" / "pq-reward-relationships.json")
    canonical_dlc_targets = {
        str(row.get("target"))
        for row in relationship_data.get("verified_relationships", [])
        if row.get("relationship") == "pq_requires_dlc"
    }
    dlc_identity = load(ROOT / "docs" / "data" / "dlc" / "canonical-dlc-identity.json")
    dlc_records = dlc_identity.get("records", [])
    dlc_ids = [record.get("id") for record in dlc_records]
    dlc_names = [record.get("name") for record in dlc_records]
    identity_name_map = {
        str(record.get("name")): record.get("id")
        for record in dlc_records
    }
    missing_dlc_targets = sorted(canonical_dlc_targets - set(identity_name_map))
    orphan_dlc_names = sorted(set(identity_name_map) - canonical_dlc_targets)
    duplicate_dlc_ids = len(dlc_ids) - len(set(dlc_ids))
    duplicate_dlc_names = len(dlc_names) - len(set(dlc_names))
    bad_sources = [
        record.get("name")
        for record in dlc_records
        if record.get("pq_relationships_source") != "docs/data/pq-reward-relationships.json"
    ]
    dlc_ok = (
        len(dlc_records) == 20
        and duplicate_dlc_ids == 0
        and duplicate_dlc_names == 0
        and not missing_dlc_targets
        and not orphan_dlc_names
        and not bad_sources
    )
    results["canonical_dlc_identity"] = {
        "canonical_pq_dlc_targets": len(canonical_dlc_targets),
        "identity_records": len(dlc_records),
        "unique_ids": len(set(dlc_ids)),
        "unique_names": len(set(dlc_names)),
        "missing_canonical_targets": missing_dlc_targets,
        "orphan_identity_names": orphan_dlc_names,
        "duplicate_ids": duplicate_dlc_ids,
        "duplicate_names": duplicate_dlc_names,
        "records_with_wrong_relationship_source": bad_sources,
        "status": "clean" if dlc_ok else "unresolved",
    }
    if not dlc_ok:
        failures.append("canonical_dlc_identity")

    report = {
        "schema_version": "1.1.0",
        "scope": "published Character/DLC page local navigation plus canonical identity resolution",
        "rules": [
            "Published page links must resolve to repository-local artifacts.",
            "Resolved DLC-character provenance labels must target existing canonical character identities; unresolved variants remain explicit.",
            "The canonical DLC identity layer must resolve every existing pq_requires_dlc target exactly once and must not introduce orphan identities.",
            "Canonical identity layers remain authoritative.",
            "This audit checks navigation and identity resolution only; it does not infer missing content relationships.",
        ],
        "results": results,
        "status": "clean" if not failures else "unresolved",
        "failures": failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
