# PQ cross-domain completion criteria

The PQ layer is not considered exhaustive merely because PQ 1-186 have records. Exhaustiveness requires the relationships between quests and the rest of the database to resolve cleanly.

A complete PQ graph must provide:

1. Every PQ 1-186 has a stable canonical record.
2. Every explicit skill reward is linked to a canonical skill record.
3. Every explicit Super Soul reward is linked to a canonical Super Soul record.
4. Every explicit clothing/accessory reward is linked to canonical equipment records.
5. Character/enemy references resolve to canonical character records where available.
6. DLC requirements resolve to canonical DLC records.
7. Farming routes are separated from guaranteed reward claims.
8. Ultimate Finish conditions and reward attribution conflicts remain explicitly tracked.
9. Reverse lookup works from each reward back to every PQ that awards it.
10. Audit tooling rejects duplicate canonical edges and unresolved required targets.

The current branch establishes the aggregation and relationship framework; subsequent passes will fill the remaining edges rather than treating sparse source data as complete.
