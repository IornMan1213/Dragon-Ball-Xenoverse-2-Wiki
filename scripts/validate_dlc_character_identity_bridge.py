#!/usr/bin/env python3
"""Validate DLC headline-character provenance labels against canonical character identities."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"docs"/"data"
CANON=DATA/"characters-record-layer.json"
BASELINE=DATA/"records"/"character-dlc-baseline.json"
BRIDGE=DATA/"characters"/"dlc-character-identity-bridge.json"
def load(p):
    with p.open(encoding="utf-8") as f:return json.load(f)
def main():
    canonical=set(load(CANON).get("character_names",[]))
    baseline=load(BASELINE).get("records",[])
    bridge=load(BRIDGE).get("records",[])
    by_source={r.get("source_name"):r for r in bridge}
    missing=[r.get("name") for r in baseline if r.get("name") not in by_source]
    invalid=[r for r in bridge if r.get("canonical_character_name") and r.get("canonical_character_name") not in canonical]
    duplicate_sources=len(by_source)!=len(bridge)
    baseline_names={r.get("name") for r in baseline}
    extra=[r.get("source_name") for r in bridge if r.get("source_name") not in baseline_names]
    unresolved=[r for r in bridge if r.get("status")=="unresolved_source_label"]
    report={"schema_version":"1.0.0","scope":"DLC headline-character provenance to canonical character identity",
            "canonical_source":str(CANON.relative_to(ROOT)),"baseline":str(BASELINE.relative_to(ROOT)),"bridge":str(BRIDGE.relative_to(ROOT)),
            "results":{"baseline_records":len(baseline),"bridge_records":len(bridge),"missing_bridge_records":missing,
                       "invalid_canonical_targets":invalid,"duplicate_source_labels":duplicate_sources,"extra_bridge_records":extra,
                       "unresolved_source_labels":unresolved,"status":"clean_with_explicit_unresolved" if not missing and not invalid and not duplicate_sources and not extra else "unresolved"},
            "rules":["Canonical character names remain authoritative.","Explicit aliases may resolve only unambiguous identities.","Unresolved variants must remain explicit rather than being collapsed into a base character.","This bridge does not create DLC or gameplay relationships."]}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 1 if report["results"]["status"]!="clean_with_explicit_unresolved" else 0
if __name__=="__main__":raise SystemExit(main())
