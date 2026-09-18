# Exhaustive TODO — Live Status Snapshot

**Last updated:** 2026-09-18

This is the live progress companion to TODO-EXHAUSTIVE.md. It records the current repository state without treating indexed names as fully verified game data.

## Current campaign

### Skills

- **Canonical source index:** docs/data/skills.json remains a seeded/indexed catalog generated on 2026-09-14; it has not yet been proven synchronized with the later research batches now present in docs/data/skill-research-batches/.
- **Research batch frontier:** the repository currently contains skill research through **Batch 316**.
- **Immediate P0 issue:** canonical verification-status enum drift and the cleanup script's bare-marker gap have been corrected, but Repository Quality and Clean Internal Artifacts still fail on commit 2c20abe5. The connector exposes failed jobs but no usable step logs. Skills Sync has not yet been rerun against the corrected research frontier.
- **Batch 314 correction:** removed duplicate records for Heat Dome Attack, Perfect Kamehameha, Angry Explosion, Gigantic Meteor, and Sphere of Destruction. Earlier evidence remains in Batches 17/35, 312, 13, 306, and 307 respectively.
- **Research standard:** unresolved values remain null; Ultimate Finish requirements are not inferred from silence; canonical identity remains (name.casefold(), class, subcategory).

## Latest research batch

**Batch 315:** added five Ki Blast Ultimate records — Final Flash (SS3 DAIMA), Super Kamehameha (SS4 DAIMA), Thunder Flash, Prominence Flash, and Mystic Flash. Variable/uncertain fields remain null; these are research-layer records and are not claimed as canonical until Skills Sync/validators succeed.

## Current priorities

### P0 — Critical

1. Determine the cause of the remaining four GitHub Actions failures when usable runner logs/annotations become available.
2. Rerun the four failing workflows after the cause is identified and fixed; do not call them successful based on a rerun request alone.
3. Do not claim canonical synchronization until skills.json and skills-index.json are fetched after a successful generation/validation path.

### P1 — Highest value

1. Synchronize the accumulated non-duplicate skill research into the canonical catalog.
2. Reconcile final-DLC Batch 36, including The Power to Overcome and PQ185/PQ186 reward relationships, before adding more batches.
3. Re-verify completed batches and reconcile unresolved costs, acquisition, CaC, mechanics, and UF fields.
4. Begin a structured coverage audit of thin/underdeveloped systems and pages so missing records and missing fields become explicit research work.
5. Resume new Ki Blast Ultimate batches only when they do not displace higher-value verification or coverage work.

### Exhaustive coverage track

This is an active research track, not a future polish task. The presence of a page or index does not mean the system is exhaustively documented. For each system, audit record count, field completeness, acquisition/reward relationships, restrictions, mechanics, provenance, uncertainty, and cross-links.

- Parallel Quests: individual records, objectives, Ultimate Finish conditions, reward slots, skill/equipment drops, unlocks, DLC/version provenance.
- Awoken/Transformations: every CaC form plus character-only forms, race restrictions, resource model, stages, prerequisites, effects, exceptions, and version history.
- Expert Missions: all missions, phases, bosses, mechanics, rewards, unlocks, and mission-count definitions.
- Super Souls / Equipment / QQ Bangs: individual records and structured acquisition/effect/stat/recipe provenance.
- Characters / Story / Time Rifts / Shops / Raids: record-level coverage, relationships, prerequisites, rewards, and version/DLC provenance.

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

- Commit b42c5759: the four canonical skill verification-status values were normalized from invalid `corrected`/`researched` states to schema-valid `partially_verified` states in both canonical files.
- Commit 2c20abe5: cleanup was strengthened to remove bare `filecite`/`memcite` markers in addition to PUA spans and turn references.
- Commit 2c20abe5: Repository Quality and Clean Internal Artifacts still fail; Pages is still building. Skills Sync was not triggered by the status/cleanup-only changes.
- The available connector exposes check-run failure counts but not the underlying annotation payloads, so the root cause remains unresolved.

## Known blockers

- GitHub currently exposes failed workflow runs but the connector cannot retrieve usable step logs for the latest failures.
- Canonical skill generation depends on the external Madreag skill corpus inside GitHub Actions; local container execution cannot reach GitHub from this environment.
- The canonical catalog therefore remains unclaimed as synchronized until Actions or another verified generation path produces and validates the generated files.

## Definition of done

A skill is not done merely because its name exists or a research batch exists. It requires enough evidence for identity, type, restrictions, costs, mechanics, acquisition, conditions, provenance, version history where relevant, related content, and explicit uncertainty.


### Billing blocker detail — 2026-09-18

The repository owner reports that GitHub displays a **billing error when these workflows are attempted**. This is consistent with the observed runner-level symptom (`steps: []`, `runner_id: 0`, no usable step logs) and should now be treated as the leading documented explanation for the Actions blocker. This is user-reported account/billing evidence, not connector-observed billing telemetry. Do not modify validators or workflow logic merely to bypass the billing restriction. Canonical synchronization remains blocked until Actions can actually execute and produce observable validation output, or an independently verifiable generation path is established.
