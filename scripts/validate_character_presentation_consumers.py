#!/usr/bin/env python3
"""Audit character-facing presentation consumers for canonical identity and parity."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"docs"/"data"

def load(p):
    with p.open(encoding="utf-8") as f:
        return json.load(f)

def main():
    canon=set(load(DATA/"characters-record-layer.json").get("character_names",[]))
    bridge=load(DATA/"characters"/"character-id-identity-bridge.json").get("records",[])
    presets=load(DATA/"character-presets-record-layer.json").get("records",[])
    partners=load(DATA/"partner-customization-key-record-layer.json").get("records",[])
    recon=load(DATA/"partner-customization-key-reconciliation.json").get("records",[])
    explorer=(ROOT/"docs"/"Characters-All.html").read_text(encoding="utf-8")
    characters_page=(ROOT/"docs"/"Characters.md").read_text(encoding="utf-8")
    core_profiles=(ROOT/"docs"/"Character-Core-Profiles.md").read_text(encoding="utf-8")
    import re
    preset_label_pattern=re.compile(r"(?i)\b(?:[A-Za-z][A-Za-z0-9()'’ -]+\s+)?Preset\s+\d+")
    markdown_preset_labels=sorted(set(preset_label_pattern.findall(characters_page+"\\n"+core_profiles)))
    characters_explorer_link="Characters-All.html" in characters_page or "Characters-All.md" in characters_page
    core_profile_search_design=("Search/" in core_profiles or "searchUrl(" in core_profiles or not markdown_preset_labels)

    bridge_ids=[r.get("character_id") for r in bridge]
    bridge_source_names=[r.get("source_name") for r in bridge]
    bridge_map={r["character_id"]:r.get("canonical_character_name") for r in bridge if r.get("character_id") is not None}
    duplicate_bridge_ids=sorted(k for k,v in Counter(bridge_ids).items() if k is not None and v>1)
    duplicate_bridge_source_names=sorted(k for k,v in Counter(bridge_source_names).items() if k is not None and v>1)
    malformed_bridge_ids=[{"source_name":r.get("source_name"),"type":type(r.get("character_id")).__name__} for r in bridge if r.get("character_id") is not None and not isinstance(r.get("character_id"),str)]
    preset_ids=sorted({r["character_id"] for r in presets if r.get("character_id")})
    preset_record_ids=[r.get("id") for r in presets]
    duplicate_preset_ids=sorted(k for k,v in Counter(preset_record_ids).items() if k is not None and v>1)
    malformed_preset_ids=[{"id":r.get("id"),"type":type(r.get("id")).__name__} for r in presets if r.get("id") is not None and not isinstance(r.get("id"),str)]
    numbered_pairs=[(r.get("character_id"),r.get("preset_number")) for r in presets if r.get("preset_number") is not None]
    duplicate_character_preset_pairs=sorted([list(k) for k,v in Counter(numbered_pairs).items() if v>1])
    allowed_record_types={"preset","separate_character"}
    special_records=[{"id":r.get("id"),"record_type":r.get("record_type"),"character_id":r.get("character_id"),"preset_number":r.get("preset_number")} for r in presets if r.get("record_type") and r.get("record_type")!="preset"]
    invalid_record_types=sorted({"<missing>" if not r.get("record_type") else r.get("record_type") for r in presets}-allowed_record_types)
    special_numbering_conflicts=sorted(r.get("id") for r in presets if r.get("record_type")=="separate_character" and r.get("preset_number") is not None)
    partner_ids=sorted({r["character_id"] for r in partners if r.get("character_id")})
    recon_ids=sorted({r["character_id"] for r in recon if r.get("character_id")})
    unresolved_preset=sorted(set(preset_ids)-set(bridge_map))
    unresolved_partner=sorted(set(partner_ids)-set(bridge_map))
    invalid_targets=sorted((cid,name) for cid,name in bridge_map.items() if name not in canon)
    partner_parity=sorted(set(partner_ids)^set(recon_ids))
    partner_name_mismatches=[]
    for r in partners:
        target=bridge_map.get(r.get("character_id"))
        if target and r.get("partner")!=target:
            partner_name_mismatches.append({"key":r.get("key_number"),"character_id":r.get("character_id"),"partner":r.get("partner"),"canonical":target})

    preset_navigation_links=len(presets) if "searchUrl(name)" in explorer else 0
    checks={
        "bridge_ids_unique":not duplicate_bridge_ids and len(bridge_map)==len(bridge),
        "bridge_source_names_unique":not duplicate_bridge_source_names,
        "bridge_id_fields_are_strings":not malformed_bridge_ids,
        "bridge_targets_canonical":not invalid_targets,
        "all_preset_character_ids_bridged":not unresolved_preset,
        "all_partner_character_ids_bridged":not unresolved_partner,
        "partner_reconciliation_id_parity":not partner_parity,
        "partner_display_names_match_canonical_bridge":not partner_name_mismatches,
        "preset_explorer_has_character_search_navigation":preset_navigation_links==len(presets),
        "preset_record_ids_unique":not duplicate_preset_ids and len(preset_record_ids)==len(set(preset_record_ids)),
        "preset_id_fields_are_strings":not malformed_preset_ids,
        "numbered_character_preset_pairs_unique":not duplicate_character_preset_pairs,
        "record_types_allowed":not invalid_record_types,
        "separate_character_records_unumbered":not special_numbering_conflicts,
        "characters_page_links_canonical_explorer":characters_explorer_link,
        "core_profiles_do_not_hardcode_preset_labels":not markdown_preset_labels,
        "core_profiles_expose_search_design":core_profile_search_design,
    }
    report={"schema_version":"1.0.0","scope":"character-facing presentation consumers",
      "canonical_source":"docs/data/characters-record-layer.json",
      "bridge":"docs/data/characters/character-id-identity-bridge.json",
      "consumers":["docs/data/character-presets-record-layer.json","docs/data/partner-customization-key-record-layer.json","docs/data/partner-customization-key-reconciliation.json","docs/Characters-All.html","docs/Characters.md","docs/Character-Core-Profiles.md"],
      "results":{"canonical_character_names":len(canon),"bridge_records":len(bridge),
        "preset_records":len(presets),"preset_distinct_character_ids":len(preset_ids),
        "partner_key_records":len(partners),"partner_distinct_character_ids":len(partner_ids),
        "partner_reconciliation_distinct_character_ids":len(recon_ids),
        "unresolved_preset_character_ids":unresolved_preset,
        "unresolved_partner_character_ids":unresolved_partner,
        "invalid_bridge_targets":invalid_targets,
        "duplicate_bridge_character_ids":duplicate_bridge_ids,
        "duplicate_bridge_source_names":duplicate_bridge_source_names,
        "malformed_bridge_character_ids":malformed_bridge_ids,
        "partner_reconciliation_id_parity_differences":partner_parity,
        "partner_display_name_mismatches":partner_name_mismatches,
        "preset_explorer_navigation_records":preset_navigation_links,
        "duplicate_preset_record_ids":duplicate_preset_ids,
        "malformed_preset_record_ids":malformed_preset_ids,
        "duplicate_numbered_character_preset_pairs":duplicate_character_preset_pairs,
        "special_record_types":special_records,
        "invalid_record_types":invalid_record_types,
        "special_record_numbering_conflicts":special_numbering_conflicts,
        "markdown_consumers":{
          "characters_page_links_canonical_explorer":characters_explorer_link,
          "core_profiles_expose_search_design":core_profile_search_design,
          "hard_coded_preset_label_matches":markdown_preset_labels
        },
        "checks":checks,
        "status":"clean" if all(checks.values()) else "unresolved"},
      "evidence_boundary":"This audit proves identity/navigation parity and producer-record integrity only. It does not verify complete preset numbering, loadouts, unlock routes, DLC ownership, raid rotation, TP Medal costs, or historical update chronology.",
      "rules":["Canonical character names remain authoritative.","Presentation IDs are resolved only through the explicit bridge.","Unresolved identity variants remain unresolved.","No character identity is inferred from a slug or display-name similarity."]}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 0 if report["results"]["status"]=="clean" else 1

if __name__=="__main__":
    raise SystemExit(main())
