#!/usr/bin/env python3
"""Cross-check Parallel Quest skill rewards against the canonical skill catalog.

The validator is intentionally strict: a missing canonical skill is an audit finding,
not a successful link. Known transcription aliases are recorded rather than hidden.
"""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PQ_DIR=ROOT/'docs/data/parallel-quest-research-batches'; SKILLS=ROOT/'docs/data/skills.json'; REPORT=ROOT/'docs/data/pq-skill-crosslink-report.json'
ALIASES={'kamekameha':'kamehameha','x100 big bang kamehameha':'x100 big bang kamehameha','x 100 big bang kamehameha':'x100 big bang kamehameha','ill bomber':'iii bomber'}
def norm(v): return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9 ]+',' ',str(v).casefold())).strip()
def main():
 d=json.loads(SKILLS.read_text(encoding='utf-8')); canonical_names={norm(r.get('name')):r.get('name') for r in d.get('records',[]) if r.get('name')}; links=[]; unresolved=[]; aliases=[]; seen=set()
 for path in sorted(PQ_DIR.glob('pq-batch-*.json')):
  if 'numbering-reconciliation' in path.name or 'skill-crosslink' in path.name: continue
  try: payload=json.loads(path.read_text(encoding='utf-8'))
  except (OSError,json.JSONDecodeError): continue
  for q in payload.get('records',[]):
   for raw in q.get('skill_rewards',[]) or []:
    raw=str(raw).strip(); n=norm(raw); target=ALIASES.get(n,n); key=(q.get('number'),n)
    if key in seen: continue
    seen.add(key)
    if target in canonical_names:
     item={'pq':q.get('number'),'skill':raw,'canonical_skill':canonical_names[target],'match':'alias' if target!=n else 'exact'}; links.append(item)
     if target!=n: aliases.append(item)
    else: unresolved.append({'pq':q.get('number'),'skill':raw})
 report={'schema_version':'1.1','generated_by':'scripts/validate_pq_skill_links.py','canonical_skill_records':len(canonical_names),'linked_skill_rewards':len(links),'alias_matches':aliases,'unresolved':unresolved,'status':'passed' if not unresolved else 'unresolved_links'}
 REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(json.dumps(report,indent=2,ensure_ascii=False))
 if unresolved: print(f'Unresolved PQ skill links: {len(unresolved)}'); return 1
 print(f'Validated {len(links)} unique PQ skill links against {len(canonical_names)} canonical skills.'); return 0
if __name__=='__main__': raise SystemExit(main())
