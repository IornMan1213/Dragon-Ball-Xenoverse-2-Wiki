#!/usr/bin/env python3
"""Validate presentation character IDs against the canonical character name layer."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"docs"/"data"
CANON=DATA/"characters-record-layer.json"
BRIDGE=DATA/"characters"/"character-id-identity-bridge.json"
PRESETS=DATA/"character-presets-record-layer.json"
KEYS=DATA/"partner-customization-key-record-layer.json"
def load(p):
    with p.open(encoding="utf-8") as f:return json.load(f)
def main():
    canonical=set(load(CANON).get("character_names",[]))
    bridge=load(BRIDGE).get("records",[])
    ids={r["character_id"] for r in bridge}
    duplicate_ids=len(ids)!=len(bridge)
    invalid=[r for r in bridge if r.get("canonical_character_name") not in canonical]
    sources={"character_presets":sorted({r.get("character_id") for r in load(PRESETS).get("records",[]) if r.get("character_id")}),
             "partner_customization":sorted({r.get("character_id") for r in load(KEYS).get("records",[]) if r.get("character_id")})}
    unresolved={domain:sorted(set(vals)-ids) for domain,vals in sources.items()}
    report={"schema_version":"1.0.0","scope":"presentation character_id → canonical character-name navigation",
            "canonical_source":str(CANON.relative_to(ROOT)),"bridge":str(BRIDGE.relative_to(ROOT)),
            "results":{"canonical_character_names":len(canonical),"bridge_records":len(bridge),
                       "invalid_canonical_targets":invalid,"duplicate_bridge_ids":duplicate_ids,
                       "source_id_counts":{k:len(v) for k,v in sources.items()},
                       "unresolved_source_ids":unresolved,
                       "status":"clean" if not invalid and not duplicate_ids and not any(unresolved.values()) else "unresolved"},
            "rules":["Canonical character names remain authoritative.","Presentation character_id values are not canonical IDs.","Only explicit bridge records may resolve presentation IDs.","No bridge mapping creates a PQ or other canonical relationship."]}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 1 if report["results"]["status"]!="clean" else 0
if __name__=="__main__":raise SystemExit(main())
