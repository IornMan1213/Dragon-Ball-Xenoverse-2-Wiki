#!/usr/bin/env python3
"""Cross-check Parallel Quest skill rewards against the canonical skill catalog."""
from __future__ import annotations
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PQ_DIR=ROOT/'docs/data/parallel-quest-research-batches'
SKILLS=ROOT/'docs/data/skills.json'
ALIASES={'kamekameha':'kamehameha','x 100 big bang kamehameha':'x100 big bang kamehameha'}

def norm(v):
    v=str(v).casefold().replace('’',"'")
    v=re.sub(r'\s+',' ',v).strip()
    return v

def main():
    data=json.loads(SKILLS.read_text(encoding='utf-8'))
    canonical={norm(r.get('name')) for r in data.get('records',[]) if r.get('name')}
    canonical_names={norm(r.get('name')):r.get('name') for r in data.get('records',[]) if r.get('name')}
    links=[]; unresolved=[]; aliases=[]; duplicate_links=set()
    for path in sorted(PQ_DIR.glob('pq-batch-*.json')):
        if 'numbering-reconciliation' in path.name or 'skill-crosslink' in path.name: continue
        try: payload=json.loads(path.read_text(encoding='utf-8'))
        except (OSError,json.JSONDecodeError): continue
        for q in payload.get('records',[]):
            num=q.get('number')
            for skill in q.get('skill_rewards',[]) or []:
                raw=str(skill).strip(); n=norm(raw); target=ALIASES.get(n,n)
                link=(num,n)
                if link in duplicate_links: continue
                duplicate_links.add(link)
                if target in canonical:
                    links.append({'pq':num,'skill':raw,'canonical_skill':canonical_names[target],'match':'exact' if target==n else 'alias'})
                    if target!=n: aliases.append({'pq':num,'source_name':raw,'canonical_name':canonical_names[target]})
                else:
                    unresolved.append({'pq':num,'skill':raw})
    report={'schema_version':'1.0','generated_by':'scripts/validate_pq_skill_links.py','canonical_skill_records':len(canonical),'linked_skill_rewards':len(links),'alias_matches':aliases,'unresolved':unresolved,'status':'passed' if not unresolved else 'unresolved_links'}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    if unresolved:
        print(f"Unresolved PQ skill links: {len(unresolved)}", flush=True)
        return 1
    print(f"Validated {len(links)} unique PQ skill links against {len(canonical)} canonical skills.")
    return 0
if __name__=='__main__': raise SystemExit(main())
