#!/usr/bin/env python3
"""Audit character-facing presentation consumers for canonical identity and parity."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"docs"/"data"
def load(p):
    with p.open(encoding="utf-8") as f:return json.load(f)
def main():
    canon=set(load(DATA/"characters-record-layer.json").get("character_names",[]))
    bridge=load(DATA/"characters"/"character-id-identity-bridge.json").get("records",[])
    presets=load(DATA/"character-presets-record-layer.json").get("records",[])
    partners=load(DATA/"partner-customization-key-record-layer.json").get("records",[])
    recon=load(DATA/"partner-customization-key-reconciliation.json").get("records",[])\n    explorer=(ROOT/"docs"/"Characters-All.html").read_text(encoding="utf-8")
    bridge_map={r["character_id"]:r.get("canonical_character_name") for r in bridge}
    preset_ids=sorted({r["character_id"] for r in presets if r.get("character_id")})
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
    preset_navigation_links=sum(1 for _ in presets) if "Search/" in explorer else 0\n    checks={
      "bridge_ids_unique":len(bridge_map)==len(bridge),
      "bridge_targets_canonical":not invalid_targets,
      "all_preset_character_ids_bridged":not unresolved_preset,
      "all_partner_character_ids_bridged":not unresolved_partner,
      "partner_reconciliation_id_parity":not partner_parity,
      "partner_display_names_match_canonical_bridge":not partner_name_mismatches,\n      "preset_explorer_has_character_search_navigation": "searchUrl(name)" in explorer and preset_navigation_links==len(presets)
    }
    report={"schema_version":"1.0.0","scope":"character-facing presentation consumers",
      "canonical_source":"docs/data/characters-record-layer.json",
      "bridge":"docs/data/characters/character-id-identity-bridge.json",
      "consumers":["docs/data/character-presets-record-layer.json","docs/data/partner-customization-key-record-layer.json","docs/data/partner-customization-key-reconciliation.json"],
      "results":{"canonical_character_names":len(canon),"bridge_records":len(bridge),
        "preset_records":len(presets),"preset_distinct_character_ids":len(preset_ids),
        "partner_key_records":len(partners),"partner_distinct_character_ids":len(partner_ids),
        "partner_reconciliation_distinct_character_ids":len(recon_ids),
        "unresolved_preset_character_ids":unresolved_preset,
        "unresolved_partner_character_ids":unresolved_partner,
        "invalid_bridge_targets":invalid_targets,
        "partner_reconciliation_id_parity_differences":partner_parity,
        "partner_display_name_mismatches":partner_name_mismatches,\n        "preset_explorer_navigation_records":preset_navigation_links,
        "checks":checks,
        "status":"clean" if all(checks.values()) else "unresolved"},
      "evidence_boundary":"This audit proves identity/navigation parity only. It does not verify preset numbering, loadouts, raid rotation, DLC ownership, TP Medal costs, or historical update chronology.",
      "rules":["Canonical character names remain authoritative.","Presentation IDs are resolved only through the explicit bridge.","Unresolved identity variants remain unresolved.","No character identity is inferred from a slug or display-name similarity."]}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 0 if report["results"]["status"]=="clean" else 1
if __name__=="__main__":raise SystemExit(main())
