# Exhaustive TODO — Live Status Snapshot

**Last updated:** 2026-09-18

This is the live progress companion to TODO-EXHAUSTIVE.md. It records the current repository state without treating indexed names as fully verified game data.

## Current campaign

### Skills

- **Canonical source index:** docs/data/skills.json remains a seeded/indexed catalog generated on 2026-09-14; it has not yet been proven synchronized with the later research batches now present in docs/data/skill-research-batches/.
- **Research batch frontier:** the repository currently contains skill research through **Batch 314**.
- **Immediate P0 issue:** the corrected commit 05b3bbd now triggers all normal repository workflows, but Skills Sync, Wiki Data Audit, Repository Quality, and Clean Internal Artifacts still fail; each was rerun once with the same result. The connector exposes failed jobs/check runs but no usable step logs or failure annotations. Pages deployment succeeds.
- **Batch 314 correction:** removed duplicate records for Heat Dome Attack, Perfect Kamehameha, Angry Explosion, Gigantic Meteor, and Sphere of Destruction. Earlier evidence remains in Batches 17/35, 312, 13, 306, and 307 respectively.
- **Research standard:** unresolved values remain null; Ultimate Finish requirements are not inferred from silence; canonical identity remains (name.casefold(), class, subcategory).

## Current priorities

### P0 — Critical

1. Determine the cause of the remaining four GitHub Actions failures when usable runner logs/annotations become available.
2. Rerun the four failing workflows after the cause is identified and fixed; do not call them successful based on a rerun request alone.
3. Do not claim canonical synchronization until skills.json and skills-index.json are fetched after a successful generation/validation path.

### P1 — Highest value

1. Synchronize the accumulated non-duplicate skill research into the canonical catalog.
2. Continue Ki Blast Ultimate coverage with a duplicate check before every batch.
3. Re-verify completed batches and reconcile unresolved costs, acquisition, CaC, mechanics, and UF fields.
4. Reconcile final-DLC Batch 36, including The Power to Overcome and PQ185/PQ186 reward relationships.

### P2 — Important

- Expand and verify Parallel Quest reward/acquisition crosslinks.
- Reconcile Awoken/Transformation records, including Power to Overcome.
- Expand Expert Mission records and reconcile mission-count definitions.
- Expand Super Souls, Equipment, and QQ Bang structured research.
- Strengthen duplicate/enum/source/acquisition data audits.

### P3 — Polish

- Continue GitHub Pages search/explorer, navigation, responsive UI, accessibility, and data-card improvements.
- Continue internal-artifact cleanup and documentation synchronization.
- Recheck native GitHub Pages deployment only from an observable successful run.

## Latest validation result

- Commit 05b3bbd: Pages deployment succeeded.
- Commit 05b3bbd: Skills Sync, Wiki Data Audit, Repository Quality, and Clean Internal Artifacts failed; rerun attempt 2 also failed for each.
- The available connector exposes check-run failure counts but not the underlying annotation payloads, so the root cause remains unresolved.

## Known blockers

- GitHub currently exposes failed workflow runs but the connector cannot retrieve usable step logs for the latest failures.
- Canonical skill generation depends on the external Madreag skill corpus inside GitHub Actions; local container execution cannot reach GitHub from this environment.
- The canonical catalog therefore remains unclaimed as synchronized until Actions or another verified generation path produces and validates the generated files.

## Definition of done

A skill is not done merely because its name exists or a research batch exists. It requires enough evidence for identity, type, restrictions, costs, mechanics, acquisition, conditions, provenance, version history where relevant, related content, and explicit uncertainty.
