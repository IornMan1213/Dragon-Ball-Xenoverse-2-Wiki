#!/usr/bin/env python3
"""Audit Super Soul cross-domain endpoint coverage without deleting source-backed edges."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]/"docs/data"
rel=json.loads((R/"pq-reward-relationships.json").read_text(encoding="utf-8"))
ss=json.loads((R/"super-souls-record-layer.json").read_text(encoding="utf-8"))
ai=json.loads((R/"super-souls/pq-acquisition-index-041-186.json").read_text(encoding="utf-8"))
projection=json.loads((R/"pq-super-soul-crosslink-report.json").read_text(encoding="utf-8"))
targets={x["target"] for x in rel["verified_relationships"] if x["relationship"]=="pq_rewards_super_soul"}
detailed={x.get("name") for x in ss["records"]}
indexed={n for x in ai["records"] for n in x.get("super_souls",[])}
if not isinstance(projection, dict):\n    raise SystemExit("PQ Super Soul crosslink report root must be an object")\nexpected_linked = sum(x["relationship"] == "pq_rewards_super_soul" for x in rel.get("verified_relationships", []) if isinstance(x, dict))\nif projection.get("linked_super_soul_rewards") != expected_linked:\n    raise SystemExit("PQ Super Soul crosslink report linked reward count drift")\nreport={"schema_version":"1.0","audit_date":"2026-09-27","domain":"super_souls","canonical_forward_rows":sum(x["relationship"]=="pq_rewards_super_soul" for x in rel["verified_relationships"]),"canonical_forward_targets":len(targets),"detailed_record_layer_records":len(ss["records"]),"detailed_records_matching_forward_targets":len(targets&detailed),"forward_targets_without_detailed_record":sorted(targets-detailed),"pq_acquisition_index_records":len(ai["records"]),"pq_acquisition_index_targets":len(indexed),"forward_targets_present_in_pq_acquisition_index":len(targets&indexed),"forward_targets_absent_from_pq_acquisition_index":sorted(targets-indexed),"status":"gap_identified","interpretation":"Partial endpoint coverage is an enrichment gap, not negative evidence against canonical forward relationships."}
(Path(__file__).resolve().parents[1]/"docs/data/super-soul-consumer-endpoint-coverage-audit-2026-09-27.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2,ensure_ascii=False))
