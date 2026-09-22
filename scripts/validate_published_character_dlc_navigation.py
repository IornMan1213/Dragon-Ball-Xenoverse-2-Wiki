#!/usr/bin/env python3
"""Validate published Character/DLC page navigation against local canonical artifacts."""
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

def main() -> int:
    results = {}
    failures = []
    for page, links in CHECKS.items():
        text = (ROOT / page).read_text(encoding="utf-8")
        page_results = []
        for label, href, target in links:
            present = href in text
            exists = target.exists()
            ok = present and exists
            page_results.append({"label": label, "href": href, "link_present": present, "target_exists": exists, "status": "clean" if ok else "unresolved"})
            if not ok:
                failures.append(f"{page}:{label}")
        results[page] = page_results
    report = {
        "schema_version": "1.0.0",
        "scope": "published Character/DLC page local navigation",
        "rules": [
            "Published page links must resolve to repository-local artifacts.",
            "Canonical identity layers remain authoritative.",
            "This audit checks navigation only; it does not infer missing content relationships.",
        ],
        "results": results,
        "status": "clean" if not failures else "unresolved",
        "failures": failures,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not failures else 1

if __name__ == "__main__":
    raise SystemExit(main())
