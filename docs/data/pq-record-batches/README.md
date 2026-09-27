# PQ record population batches

This directory contains source-backed population batches that complement the canonical Parallel Quest index/layer.

## Canonical current range

The current player-facing numbered range is **PQ 1-186**. Use `docs/data/parallel-quests-canonical-index.json` as the aggregation manifest.

Canonical batch sources:

- PQ 1-14: `../parallel-quests-index.json` (seed/index layer)
- PQ 15-20: `pq-015-020.json`
- PQ 21-40: `pq-021-040.json`
- PQ 41-60: `pq-041-060.json`
- PQ 61-80: `pq-061-080.json`
- PQ 81-100: `pq-081-100.json`
- PQ 101-120: `pq-101-120-final.json`
- PQ 121-142: `pq-121-142.json`
- PQ 143-162: `pq-143-162.json`
- PQ 163-186: `pq-163-186-final.json`

## Verification policy

Each batch intentionally uses `partially_verified` until reward provenance, opponent-specific drop attribution, unlock chains, and cross-domain references have been reconciled. Empty arrays are not claims of no rewards; they mean the batch did not yet establish the relevant relationship with sufficient confidence.

## Historical staging files

Older `restored`, `audit-v2`, `audit-v3`, `summary`, and reconciliation artifacts may remain for provenance. They are not additional canonical records. Downstream loaders should follow the aggregation manifest and must not load duplicate staging files as separate records.
