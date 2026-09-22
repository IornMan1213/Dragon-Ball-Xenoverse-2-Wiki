# Continuation checkpoint — PQ current-baseline reconciliation — 2026-09-22

## Completed
- Re-read the current continuation/efficiency protocol and inspected the live PQ relationship consumer layer.
- Verified the authoritative current baseline as **859 total relationships**: 244 skills, 151 Super Souls, 124 equipment, 247 character references, 86 DLC, 7 farming.
- Confirmed multiple current consumer audits independently expose 859/124.
- Found three remaining current-looking fields that still expose the obsolete 860/862-era totals:
  - `docs/data/pq-reward-relationships.json` — `current_reconciliation_2026_09_22.total_unique_relationships` is 860.
  - `docs/data/pq-cross-domain-status.json` — current projection `total_edges` is 860.
  - `docs/COVERAGE-AUDIT.md` — latest current-cycle wording contains 862-era totals.
- Added `docs/data/pq-current-baseline-single-source-reconciliation-2026-09-22.json` documenting the deterministic correction targets and the historical-preservation rule.

## Safety boundary
The three target files are large/append-only artifacts. The available connector returns truncated content for them, so replacing a whole file from the truncated response would risk destructive loss. No unsafe replacement was attempted.

## Exact next task
1. Obtain a complete-file-safe write path for the three current-looking fields.
2. Change only current/live/baseline totals to 859/124.
3. Preserve all dated 860/862/840 historical snapshots unchanged.
4. Re-run exact relationship-pair parity across the registered reverse indexes.
5. Update the canonical continuation handoff using append-only semantics if the complete file can be safely preserved; otherwise create the next dated cycle checkpoint as the repository's established fallback.

## Evidence
- `docs/data/pq-current-consumer-baseline-correction-2026-09-22.json` establishes the current 859/124 baseline.
- `docs/data/pq-reference-page-audit.json` and `docs/data/skill-pq-acquisition-presentation-audit.json` independently expose 859 current relationships.
- `docs/data/pq-endpoint-alias-granularity-map.json` records canonical edge count 859 before/after presentation metadata.

## Commit
- `b924c99a3d8fcc666148a1652ffc3fbb2286f17f` — current-baseline single-source reconciliation audit.

## Do not do
- Do not rewrite historical 860/862/840 records merely because they are old.
- Do not infer a replacement relationship for PQ99 Mr. Shape Up L.
- Do not reconstruct large JSON/Markdown files from truncated connector output.
