# Dragon Ball Xenoverse 2 Wiki — Persistent AI Continuation Prompt

> Canonical handoff for autonomous AI continuation of this repository.
>
> **Last updated:** 2026-09-19
> **Repository:** `IornMan1213/Dragon-Ball-Xenoverse-2-Wiki`
> **Branch:** `main`

## Mission

Continue the repository's development, research, data-quality, documentation, and validation work **directly on GitHub**. Do not merely provide suggestions or a plan.

The goal is a polished, comprehensive, evidence-backed Xenoverse 2 wiki whose structured data is genuinely exhaustive rather than merely populated.

At the start of every cycle:
1. Read this file.
2. Inspect the live repository and relevant files.
3. Follow the priority order below.
4. Research claims when evidence is needed.
5. Modify the repository directly.
6. Preserve verified information and uncertainty.
7. Commit useful completed work.
8. Inspect applicable validation and GitHub Actions status.
9. Check for accidental AI/internal citation artifacts.
10. Update this file before finishing.

## Non-negotiable research rules

- Never invent an unlock condition, reward rate, mechanic, restriction, cost, or acquisition route.
- A missing field is research work; a populated field is not automatically verified.
- Distinguish directly verified facts, incomplete source-supported facts, general/inferred progression, and unresolved information.
- Preserve conflicting evidence instead of silently choosing a convenient answer.
- Keep source/provenance information in repository data where the schema supports it.
- Never put ChatGPT UI citations such as `cite...`, `filecite...`, `memcite...`, or `turn...search...` into repository files.
- Never weaken, disable, bypass, or rewrite validators merely to make CI pass.
- If CI fails before workflow steps execute, treat that as an infrastructure/runner/account issue until evidence shows otherwise.
- Preserve canonical numbering anomalies such as the known missing/cut PQ36.

## Priority order

### P0 — Validation/infrastructure
GitHub Actions has repeatedly shown failures where jobs terminate with zero recorded steps. The repository audit also records a reported billing problem when jobs are attempted.

Do not weaken validation.

### P1 — Skills
Continue the canonical skill second-pass audit:
- exact Ki/Stamina costs
- acquisition routes
- CaC availability
- race/gender restrictions
- character-only variants
- Ultimate Finish requirements
- DLC/version provenance
- mechanics
- historical/version-sensitive differences

Do not trust stale milestone counts; inspect the live canonical files.

### P1 — Parallel Quests
Continue:
- unlock routes
- reward-slot semantics
- exact drop percentages where evidence exists
- acquisition details
- DLC/version provenance
- skill cross-links
- equipment/accessory provenance
- unresolved reward semantics
- record-level sources

Known completed frontier:
- PQ1–10: tutorial unlock wording verified.
- PQ12–20: unlock metadata refined; specific PQ dependencies preserved.
- PQ21–50: bounded availability metadata added where exact individual prerequisites were not established.
- PQ51: Great Saiyaman 1 + 2 near the beach.
- PQ52: complete PQ53.
- PQ56: speak with Kid Trunks near the waterfall.
- PQ57–60: bounded Buu-era progression metadata; exact triggers remain unresolved.
- PQ61–70: bounded evidence metadata added because consulted sources establish quest placement/objectives but not reliable individual unlock triggers.
- PQ71–80: unlock research reviewed; exact-looking prerequisites were removed where consulted evidence did not directly establish them, preserving bounded uncertainty.
- PQ161–186: later-batch reward/unlock semantics enriched; exact unknown percentages remain unresolved rather than fabricated.
- PQ184 Chaotic Time Impact: documented as a 50% Ultimate Finish bonus-slot drop.

**Next exact PQ task: PQ131–140.**
First recompute the live unlock census instead of trusting historical counts.

### P1 — Awoken / Transformations
Build exhaustive structured coverage:
- CaC vs character-only
- race/gender restrictions
- stages/forms
- resource requirements
- prerequisites
- effects
- exceptions
- DLC/version provenance

### P1/P2 — Expert Missions
Complete EM01–20 mechanics, phases, rewards, skill drops, first-clear/repeat distinctions, and version differences.

### P2 — Super Souls
Expand inventory and verify triggers, magnitudes, durations, stacking, Limit Burst, acquisition/rotation, and DLC/version history.

### P2 — Equipment
Expand clothing/accessory inventory with exact stats, slots/set relationships, costs, PQ/EM/raid/shop provenance, and version history.

### P2 — QQ Bangs
Document reproducible recipe families, materials, observed six-stat outputs, RNG behavior, and version differences.

### P2 — Characters
Build structured playable/NPC coverage, forms, restrictions, skills, mentors, PQ/EM/story appearances, and DLC/version provenance.

### P2 — Story / Time Rifts / Conton City
Build structured mission, unlock, NPC, reward, progression-gate, location, and DLC/version coverage.

### P2 — Shops / Rewards / Raids / Events
Build exhaustive inventories, costs, rotations, progression requirements, dates/recurrence, historical availability, and reward provenance.

### P3 — UI / Pages / Navigation
Only after data-completeness work, expose the improved structured research surface through pages/navigation.

## Current cycle state

### Active workstream
**Parallel Quest unlock-route research.**

### Next exact action
1. Recompute the live PQ unlock census.
2. Research **PQ121–130** individually.
3. Prioritize DLC ownership, PQ-board availability, NPC/story/progression gates, and prerequisite-PQ evidence.
4. Do not manufacture sequential prerequisites.
5. Update the relevant batch with record-level sources.
6. Update `docs/COVERAGE-AUDIT.md`.
7. Inspect GitHub Actions without weakening validators.
8. Update this file with the new state and commit the complete cycle.

### Latest known PQ unlock census
**176 canonical PQ records across 18 research batches; 24 currently lack an explicit `unlock_condition` field.** The remaining missing records are PQ36, PQ53–55, PQ131–140, and PQ151–160. Field presence is not equivalent to exact-route verification.

## Recent commits

- `d4e9fc6e747fb1faf5851d7cd9209779568701cf` — PQ51–60 unlock refinement
- `50f6ccfeb1933501b09478c366def4be7f11d675` — coverage audit refresh
- `18c1835ab886b6e43d154992befc4caa539af5f7` — PQ41–50 coverage refresh
- `684e382e6c7b101ff747a16ca3107c7b87a64e3f` — PQ31–40 coverage refresh
- `e1cce5bdf2db5e8eda9cdff9724aad62ed2fb11a` — PQ12–20 coverage refresh

## Important repository files

- `docs/COVERAGE-AUDIT.md`
- `docs/data/parallel-quest-research-batches/`
- `docs/data/skills.json`
- `docs/data/verified-skills.json`
- `docs/data/mentors-record-layer.json`
- `docs/data/parallel-quests-record-layer.json`
- `docs/data/equipment-accessories-record-layer.json`
- `.github/workflows/`
- `scripts/`


### 2026-09-19 cycle update — PQ111–120
- Workstream: Parallel Quest unlock-route research.
- Recomputed all 18 canonical PQ research batches after the prior cycle: **176 records total; 34 records remain without an explicit unlock_condition field**.
- Remaining missing unlock records are PQ36, PQ53–55, PQ121–140, and PQ151–160. This live census supersedes stale historical counts.
- Researched PQ111–120 individually. Current evidence maps PQ111–112 to Super Pack 4, PQ113–117 to Extra Pack 1, and PQ118–120 to Extra Pack 2.
- Recorded the conservative DLC-era unlock route for all ten as owning the relevant DLC pack and having the Parallel Quest board open. No sequential prerequisite was invented.
- Added record-level sources to all ten records: Madreag individual quest pages, the maintained Steam all-PQ guide, the Steam DLC-to-PQ mapping discussion, and the DLC reference.
- Updated `docs/data/parallel-quest-research-batches/pq-batch-12.json` and `docs/COVERAGE-AUDIT.md`.
- Commits: `05ec68d4b802c512f0140b46bbc09aa9cd165f89` (PQ111–120 research), `8042276049a7d9751e9e6433f1332b463dcc8b5c` (audit refresh), `4537caba8a2fd4304f366c5ca3a7eeb823f7f34` (live census correction).
- Validation: all 18 batch files were fetched and parsed successfully; total record count remains 176 and the live missing-unlock count is 34.
- CI status: the connector returned no pull-request workflow runs for the latest audit commit; prior push-triggered audit/quality/cleanup failures exposed zero steps/logs. Validators were not weakened. Continue treating opaque pre-step failures as infrastructure/account signals until actionable logs exist.
- Next exact task: **PQ121–130**; repeat the live census first and continue treating DLC ownership/version provenance as first-class evidence.

### 2026-09-19 cycle update — PQ101–110
- Workstream: Parallel Quest unlock-route research.
- Recomputed all 18 canonical PQ research batches: 176 records total; 54 records remain without an explicit unlock_condition.
- Researched PQ101–110 individually using current Madreag datamined quest records plus the maintained Steam PQ guide, GameFAQs UF discussion, and DLC mapping.
- PQ101–103 now record Super Pack 1 ownership + PQ-board availability; PQ104–106 use Super Pack 2; PQ107–109 use Super Pack 3; PQ110 uses Super Pack 4.
- Added record-level source URLs to all PQ101–110 records and preserved unresolved reward-slot semantics where evidence was insufficient.
- Updated `docs/data/parallel-quest-research-batches/pq-batch-11.json` and `docs/COVERAGE-AUDIT.md`.
- Commits: `7e74ea206ff4672d0501e96e2a083d23ee38f540` (PQ101–110 research), `2ec23fb1c2db0048094413c78b90a25c08dcde97` (coverage census).
- Validation/CI: push-triggered Wiki data audit, Repository quality, and cleanup runs failed with jobs exposing no steps/logs; this remains an infrastructure/runner/account signal and validators were not weakened. A Pages deployment run for the latest commit was queued at inspection time.
- Current unresolved unlock records: PQ36, PQ53–55, PQ111–140, PQ151–160 (54 total). Exact reward-slot semantics remain unresolved in many earlier records and are a separate research dimension.
- Next exact task: **PQ111–120**; repeat the live census first and treat DLC ownership/version provenance as first-class evidence.

### 2026-09-19 cycle update — PQ71–100
- Workstream: Parallel Quest unlock-route research.
- PQ91–97 were verified as a sequential PQ chain against an independent Japanese PQ reference and corroborating community evidence.
- PQ98 was verified as a special progression gate involving the base-game story, five Time Eggs, and the Unknown History story.
- PQ99–100 were verified as the continuation after PQ98.
- Updated `pq-batch-10.json`, `docs/COVERAGE-AUDIT.md`, and this handoff.
- Evidence discipline: exact-looking prerequisites are retained only where the consulted sources support them.
- Next exact task: PQ101–110 (DLC-era PQs); treat DLC ownership/version provenance as a first-class field when researching them.


### 2026-09-19 cycle update — PQ121–130
- Workstream: Parallel Quest unlock-route research.
- Recomputed the live census before editing: **176 canonical PQ records; 24 records remain without an explicit `unlock_condition` field**.
- Researched PQ121–130 individually. Current evidence maps PQ121–122 to Extra Pack 2, PQ123–127 to Extra Pack 3, and PQ128–130 to Extra Pack 4.
- Added the conservative DLC-era unlock route to all ten: owning the relevant DLC pack and having the Parallel Quest board available. No sequential prerequisite was invented.
- Added record-level provenance to all ten records using the maintained Steam all-PQ guide, the Steam DLC-to-PQ mapping discussion, and Bandai Namco's official DLC reference.
- Updated `docs/data/parallel-quest-research-batches/pq-batch-13.json` and `docs/COVERAGE-AUDIT.md`.
- Commits: `44c2ce4622cc41dd921edb94faaf741569f798a8` (PQ121–130 research), `29c04917673d82f433172dca6be5e5683817ddeb` (coverage audit).
- Validation: batch JSON was parsed and rewritten through the repository connector; all ten records received explicit unlock metadata, verification state, source URLs, and a 2026-09-19 verification date. A follow-up repository-wide census is still required before treating the count as final.
- CI status: no new actionable workflow result was available during this cycle; prior opaque pre-step failures remain infrastructure/account signals. Validators were not weakened.
- Current unresolved unlock records: PQ36, PQ53–55, PQ131–140, PQ151–160 (**24 total**).
- Exact next task: **PQ131–140**; recompute the live census first, then research the Ultra Pack-era DLC mapping and exact unlock routes without inventing sequential prerequisites.

## End-of-cycle update protocol

Every cycle MUST append/update a concise state section containing:
- date
- workstream
- files/records changed
- research performed
- evidence limitations
- commits
- validation results
- CI status
- current unresolved counts
- exact next task

A new AI chat must be able to continue from this file without depending on the previous chat transcript.

## New-chat starter

> Read `docs/AI-CONTINUATION-PROMPT.md` from `IornMan1213/Dragon-Ball-Xenoverse-2-Wiki`, inspect the live repository, follow its priorities and rules, and **continue the work directly on the repository**. Do not just give suggestions. At the end, update the persistent handoff file so the next chat can continue from it.


### 2026-09-19 cycle update — PQ131–140
- Workstream: Parallel Quest unlock-route research.
- Live census after this cycle: 176 canonical records across 18 batches; 14 records remain without an explicit `unlock_condition` field.
- Remaining missing records: PQ36, PQ53–55, and PQ151–160.
- Researched PQ131–140 individually. Evidence maps PQ131–132 to Extra Pack 4, PQ133–137 to Ultra Pack 1, and PQ138–140 to Ultra Pack 2.
- Added the conservative unlock route to all ten: own the relevant DLC pack and have the Parallel Quest board available. No sequential prerequisite, story gate, or NPC trigger was added without direct evidence.
- Added record-level sources, `unlock_verification`, and 2026-09-19 verification dates to `docs/data/parallel-quest-research-batches/pq-batch-14.json`.
- Sources consulted: maintained Steam all-PQ guide, Steam DLC-to-PQ mapping discussion, and Bandai Namco's official Xenoverse 2 DLC reference. These establish DLC-era availability but do not independently establish additional individual prerequisite gates; those remain unresolved.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-14.json`, `docs/COVERAGE-AUDIT.md`, and this handoff.
- Commits: `b4dfcfb303e403825dbd9b099715ab56ed53d860` (PQ131–140), `7d3e5cc1255df74bd182a50e778fe37909c9bd1c` (coverage audit), plus this handoff commit.
- Validation: all 18 batch files fetched and parsed successfully; 176 total records and 14 missing unlock fields. All PQ131–140 records now have explicit unlock metadata and provenance.
- CI: new push-triggered Repository quality and cleanup runs for `7d3e5cc1255df74bd182a50e778fe37909c9bd1c` were queued at inspection. Combined status reported no checks. The preceding Repository quality run failed before actionable steps/logs were exposed. Validators were not weakened.
- Current unresolved unlock count: 14 — PQ36, PQ53–55, PQ151–160.
- Exact next task: PQ151–160; recompute the live census first, research the DLC-era unlock routes and provenance, then handle PQ36 and PQ53–55 as special missing/numbering cases.


### 2026-09-19 cycle update — PQ151–160
- Workstream: Parallel Quest unlock-route research.
- Recomputed the live census: **176 canonical PQ records; 4 records remain without an explicit `unlock_condition` field**.
- Remaining missing records are **PQ36 and PQ53–55**.
- Researched PQ151–160 individually. Current DLC mapping is PQ151–154 → Conton City Vote Pack; PQ155–158 → Hero of Justice Pack 1; PQ159–160 → Hero of Justice Pack 2. The maintained Steam all-PQ guide independently lists these groupings; the DLC reference confirms the four Conton City Vote Pack quests.
- Added the conservative unlock route to all ten: own the relevant DLC pack and have the Parallel Quest board available. No unsupported sequential, story, NPC, or prerequisite-PQ gate was inferred.
- Added record-level sources, `unlock_verification`, and 2026-09-19 verification dates to `docs/data/parallel-quest-research-batches/pq-batch-15.json`.
- Updated `docs/COVERAGE-AUDIT.md` with the new four-record gap.
- Commits: `99a9d5617366bcc8ed73bae52b444c4db5241236` (PQ151–160 research), `51b95ef7ab6f4bdbfced04d7bfb18e0e45bcccdf` (coverage audit cleanup/update), plus this handoff commit.
- Validation: batch 15 was fetched and parsed successfully; all ten PQ151–160 records now have explicit unlock metadata and provenance. Repository-wide census remains 176 records with 4 missing unlock fields.
- CI: inspect the push-triggered runs for the latest commit before making any validator changes. Previous opaque pre-step failures remain infrastructure/account signals; validators must not be weakened.
- Current unresolved unlock count: **4** — PQ36, PQ53–55.
- Exact next task: **PQ36 and PQ53–55**. Treat these as special base-game/early-PQ cases rather than applying the DLC ownership template. Research their exact unlock routes from independent evidence, then recompute the full census and update the audit/handoff.


### 2026-09-19 cycle update — PQ36 and PQ53–55
- Workstream: Parallel Quest unlock-route research.
- Live census after the final missing-unlock pass: **176 canonical PQ records across 18 research batches; 0 records remain without an explicit `unlock_condition` field**.
- **PQ36 — The Cell Games Begin:** added the reported prerequisite `Complete PQ 35`; preserved the separate numbering/existence conflict because the maintained player-facing quest corpus and independent guides document PQ36 while another datamined corpus claims it was cut.
- **PQ53 — The Fist of Justice!:** added the NPC trigger to talk to Great Saiyaman 1 and Great Saiyaman 2 on the floating Resort Island south of Conton City's Recreation Plaza.
- **PQ54 — Majin Revival:** added `Complete PQ 52` as the direct completion-state report, but marked the route `partially_verified_conflicting_community_evidence` because another community reply attributes the unlock to the earlier Great Saiyaman blue-exclamation quest.
- **PQ55 — Tag with Gotenks:** added `Complete PQ 54` as the prerequisite.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-04.json`, `docs/data/parallel-quest-research-batches/pq-batch-06.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Evidence limitations: PQ53 has a direct trigger reference; PQ36 has prerequisite evidence plus a separate numbering conflict; PQ54 has conflicting community reports; PQ55 has a direct prerequisite report. No unsupported drop percentages were added.
- Validation: both edited batch JSON files were fetched, parsed, modified, and rewritten successfully. The repository-wide unlock census is now 176/176 records with explicit unlock fields.
- CI: no validator was weakened. Continue treating opaque pre-step GitHub Actions failures as infrastructure/account signals unless actionable logs appear; inspect the latest push-triggered runs before changing validation.
- Current unresolved unlock count: **0 missing fields**, with **PQ54 route conflict** and bounded/uncertain routes elsewhere still requiring verification.
- Exact next task: **reconcile record-level PQ provenance and reward/acquisition/version semantics**, starting with unresolved reward-slot semantics and older records lacking record-level `sources`; then continue the next P1 coverage track according to the live TODO and validation state.

- Commits for this cycle: `cadb477aa7442bc338521e9929162c429242a5c6` (PQ36), `110e02c1f42242c3c8ae8d24a6dff3924df0b951` (PQ53–55), `ae50088213a92b7ad34e6ce413bf8a3f5e962f17` (coverage audit), `ca89b37745f925ad13f9f4ef9bfaacd3fdd67f7d` (changelog), and `6359d8ee9622c029b9bcef669178e00812c07178` (handoff).


### 2026-09-19 cycle update — PQ1–10 record-level provenance
- Workstream: Parallel Quest provenance and reward/acquisition evidence cleanup.
- Live PQ census remains **176 canonical records across 18 research batches; 0 records lack an explicit `unlock_condition` field**.
- Recomputed the batch-level provenance gap before editing: **122 of 176 records lacked an individual `sources` array**. This is distinct from unlock-field completeness and is now treated as a separate evidence-quality gap.
- Completed the first bounded provenance pass on **PQ1–PQ10**. All ten records now have explicit record-level source URLs and a 2026-09-19 verification date.
- Sources used: maintained 186-PQ Steam transcription, Steam PQ reward transcription, and an independent quest-objective reference. These support the documented quest identity/objectives/rewards; exact reward-slot/drop percentages remain unresolved where the sources do not establish them.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-01.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `9106443db5f7469806c87b32d8dca7a17b7e5384` (PQ1–10 provenance), `060abb3d86283dd26338ab0cae89901dd3558d64` (coverage audit), `d26d8e99ec1f482a787559473d3de83260d13888` (changelog).
- Validation: all 18 PQ batches were fetched and parsed before the pass; total remains 176. PQ1–PQ10 now have record-level sources. Repository text search found no ChatGPT/UI citation artifacts or tool-result identifiers.
- CI: the latest changelog commit has no associated workflow runs and no reported status checks through the available GitHub connector. No validator was weakened. Continue treating missing/opaque Actions execution as an infrastructure/account signal until actionable logs appear.
- Remaining provenance gap after this pass: **112 PQ records still lack individual `sources` arrays**. Reward-slot semantics remain a separate unresolved field across many records.
- Exact next task: **continue the record-level provenance pass with PQ11–PQ20**, while checking their existing reward/acquisition claims against the maintained PQ transcription and an independent source. Preserve unresolved reward-slot/drop semantics rather than inferring them; then update the coverage audit, changelog, and this handoff and inspect Actions again.


### 2026-09-19 cycle update — PQ11–20 record-level provenance
- Workstream: Parallel Quest provenance and reward/acquisition evidence cleanup.
- Completed the second bounded provenance pass on **PQ11–PQ20**. All ten records now have explicit record-level source URLs and a 2026-09-19 verification date.
- Rechecked objective and Ultimate Finish claims against the maintained Steam 186-PQ transcription, Critical Hit, Twinfinite, and the maintained PQ11 repository record where applicable. These sources corroborate the documented objective sequences; the pass did not invent unsupported reward probabilities or unlock gates.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-02.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `0e270cacd215af12f7f2e2f0283c768642141be6` (PQ11–20 provenance), `3bd7862cd32d271004304f3305db5a6feacb699e` (coverage audit), `1efbb24e1a0399ddff296f214835ea541bcbf7c3` (changelog).
- Validation: PQ11–PQ20 now have record-level sources. The repository-wide PQ census remains **176 records** with **0 missing explicit `unlock_condition` fields**. Reward-slot semantics remain a separate unresolved evidence-quality track.
- CI: inspect the latest push-triggered runs before changing validators; no validator was weakened during this cycle.
- Remaining provenance gap: **102 PQ records** still lack individual `sources` arrays after completing PQ1–PQ20.
- Exact next task: **continue with PQ21–PQ30**, recheck objective/Ultimate Finish claims against independent sources, add record-level provenance, then update the coverage audit, changelog, and this handoff and inspect Actions/status.


### 2026-09-19 cycle update — PQ21–30 provenance and reward reconciliation
- Workstream: Parallel Quest provenance and reward/acquisition evidence cleanup.
- Completed the third bounded provenance pass on **PQ21–PQ30**. All ten records now have explicit record-level source URLs and 2026-09-19 verification dates.
- Reconciled basic reward lists against the maintained 186-PQ Steam transcription and independent PQ tables. Several incomplete repository reward lists were corrected, including PQ22, PQ26, PQ28, PQ29, and PQ30.
- Strengthened PQ27 and PQ28 unlock metadata with explicit NPC triggers: Metal Cooler near Master Cell in northern Conton City for PQ27, and Appule in the Bamboo Forest for PQ28. Other quests retain conservative unlock wording where exact quest-specific triggers were not independently established.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-03.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `581cc2067b38370ef2a970f459ba567d9a40367a` (PQ21–30 provenance/rewards), `7d9b0501c9352e96ff8427685c1321c5cb987b67` (coverage audit), `f5d67985bf25616768eaf387abd72bdfd75c7f3c` (changelog).
- Validation: all 18 PQ batches were fetched and parsed after the edit; **176 total records**, **0 missing explicit `unlock_condition` fields**, and **92 records still lacking individual `sources` arrays**.
- CI: inspect the latest push-triggered runs/status before changing validators. No validator was weakened during this cycle.
- Exact next task: **continue with PQ31–PQ40**, with the same record-level provenance pass plus reward reconciliation. Pay special attention to PQ36's already-documented numbering/existence conflict and preserve that conflict rather than silently resolving it. Then update the coverage audit, changelog, handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ31–40 provenance pass
- Workstream: Parallel Quest provenance and objective/reward evidence cleanup.
- Completed record-level provenance for **PQ31–PQ40**. All ten records now have explicit source URLs and 2026-09-19 verification dates.
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription plus independent Ultimate Finish/objective tables. Existing reward lists in this batch matched the primary transcription, so no speculative reward-slot percentages were added.
- PQ36's existing numbering/existence conflict remains explicitly documented and independently cross-checked; it was not silently deleted or normalized.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-04.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `e1c68ad1706c210663ee68003e16cd74adaae961` (PQ31–40 provenance), `676c403463c6918c47a3ff1ad675782d9c6c8c15` (coverage audit), `209da396b119668bc997c9d4bba434e0b656909c` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **82 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **continue with PQ41–PQ50** using the same provenance/reward reconciliation workflow. Verify the future-era objectives and reward lists independently, preserve unresolved acquisition/drop semantics, then update the coverage audit, changelog, handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ41–50 provenance pass
- Workstream: Parallel Quest provenance and objective/reward evidence cleanup.
- Completed record-level provenance for **PQ41–PQ50**. All ten records now have explicit source URLs and 2026-09-19 verification dates.
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription plus independent Ultimate Finish/objective references. Exact reward-slot/drop percentages remain unresolved by design.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-05.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `7053b7f5c1cd5373ec8ee7654c9e4217a18b0b8d` (PQ41–50 provenance), `4d7c71d52a04d1ec267de11d041a295c8294e47e` (coverage audit), `98cc58e6919c8743ade08754267a8628ebc9dc73` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **72 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **continue with PQ51–PQ60**, using the same provenance/reward reconciliation workflow. Verify the transition into the 6-star PQs carefully, cross-check objectives and rewards independently, preserve unresolved acquisition/drop semantics, then update the coverage audit, changelog, handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ51–60 provenance pass
- Workstream: Parallel Quest provenance and objective/reward evidence cleanup.
- Completed record-level provenance for **PQ51–PQ60**. All ten records now have explicit source URLs and 2026-09-19 verification dates.
- Independently cross-checked the transition from 5-star PQs into the 6-star block, including objectives and basic rewards. PQ52's unusual completion-of-PQ53 unlock behavior is preserved because multiple long-running guides report it; it was not silently normalized. PQ54/PQ55 unlock evidence remains attributed to the underlying community report.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-06.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `a2f3ab52b99181e89eed18537d2ea4de79fdd927` (PQ51–60 provenance), `f50f39a50ad2fa08882164c596e72ed6d0f30133` (coverage audit), `2a2a4df9448863a7f100f181ab6788fb7a63b249` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **66 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **continue with PQ61–PQ70**, covering the remaining early/base-game quests with the same record-level provenance and reward reconciliation. Pay special attention to the transition from the Buu-era quests into Beerus/Dragon Ball Super material, verify unlock metadata conservatively, and preserve documented historical conflicts rather than inventing certainty. Then update the coverage audit, changelog, handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ61–70 unlock reconciliation and provenance
- Workstream: Parallel Quest provenance plus unlock-route accuracy.
- Completed record-level provenance for **PQ61–PQ70**, with 2026-09-19 verification dates.
- Reconciled the previously conservative unlock metadata against an independent Japanese progression table: PQ61/PQ63 are tied to the Beerus/Wrath of the God of Destruction story arc; PQ62 and PQ64–PQ68 follow the documented PQ chain; PQ69 requires the Beerus-arc progression plus the documented Trunks interaction near the Time Nest; PQ70 is tied to the Resurrection of the Emperor/Golden Frieza story arc.
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references. Exact reward-slot/drop percentages remain unresolved.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-07.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `76ba4364aa319df83d324f82af3b675cf05ff877` (PQ61–70 research), `f6aa653826042880f7b9ca86fb0cd7436f21ff7f` (coverage audit cleanup), `9f00eabc756369ef84f1b620370994661bcbf1fa` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **56 records still lacking individual `sources` arrays**.
- An accidental chat citation marker was introduced into the audit during this cycle and immediately removed in commit `f6aa653826042880f7b9ca86fb0cd7436f21ff7f`; the repository audit text was rechecked before continuing.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **continue with PQ71–PQ80**, the 7-star block. Verify the story/NPC unlock routes carefully, especially PQ70→71 and any NPC-triggered quests, and reconcile objectives/rewards against independent sources. Keep provenance at record level, avoid unsupported drop percentages, update the coverage audit/changelog/handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ71–80 provenance pass
- Workstream: Parallel Quest provenance and 7-star objective/reward verification.
- Completed record-level provenance for **PQ71–PQ80**, all with explicit source URLs and 2026-09-19 verification dates.
- Cross-checked the 7-star objective sequences and documented basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references. Exact reward-slot/drop percentages remain unresolved.
- Reviewed unlock metadata conservatively. Existing documented routes were retained; broader evidence indicates PQ availability can also depend on story progression, so no unsupported single-prerequisite claim was added.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-08.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `a1330abb009dc4dd1498d42385660dd3c5f0157e` (PQ71–80 research), `111f9f17f37a5e193bf59241ec7e6cf3f6b2d724` (coverage audit), `3e2758cfa023c0ae671c48baa92610601ae29c6b` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **46 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **continue with PQ81–PQ90**. Research the next 7-star block, including PQ81/PQ82 chain behavior, Dragon Ball/time-patroller mechanics, unlock routes, objective sequences, basic rewards, and individual provenance. Preserve conflicts and uncertainty instead of inventing prerequisites or drop rates. Then update coverage audit, changelog, handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ81–90 provenance and difficulty pass
- Workstream: Parallel Quest provenance, difficulty metadata, and objective/reward verification.
- Completed record-level provenance for **PQ81–PQ90**, with explicit sources and 2026-09-19 verification dates.
- Corrected missing difficulty metadata: all ten quests are documented as **7-star** base-game PQs.
- Cross-checked objective sequences and basic rewards against the maintained 186-PQ transcription and independent Ultimate Finish references. PQ83 has community evidence for an 81→82→83 progression, but broader sources show base-game PQ availability can also involve story progression/NPC triggers; unresolved individual unlock fields were not overclaimed.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-09.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `53208c49a7e3d710dab1710e6c77dfd2062ea0d5` (PQ81–90 research), `c5cb05c6d33ab2372c0ed91fb463a0611b2518ee` (coverage audit), `302fecc0724c5dbfccff7df90ea1b63b538141b6` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **36 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **continue with PQ91–PQ100**, the final ten base-game PQs. Verify difficulty metadata, unlock routes, objective sequences, Dragon Ball/Ultimate Finish mechanics, rewards, and record-level provenance. Pay particular attention to the final PQ100 and any conflicts in old guides. Then update coverage audit, changelog, handoff, and inspect Actions/status.


### 2026-09-19 cycle update — PQ91–100 final base-game provenance pass
- Workstream: Complete the base-game PQ1–PQ100 provenance/objective/reward audit.
- Completed record-level provenance for **PQ91–PQ100**, with explicit sources and 2026-09-19 verification dates.
- Corrected missing difficulty metadata: PQ91–PQ100 are **7-star** quests.
- Reconciled reward discrepancies against the maintained 186-PQ transcription and independent guides. PQ95 now records Flash Bomber and Drain Field; PQ96 records GT Vegeta's Jacket and Absolute Zero; PQ97 records its full documented reward set including Charged Ki Wave and Phantom Fist; PQ98 records Lord Slug's Clothes and Dimension Ray; PQ100 records x100 Big Bang Kamehameha, SSGSS Vegeta Wig, and Whis Symbol Battle Suit.
- Cross-checked Ultimate Finish objectives, including PQ100's 8-minute condition followed by SSGSS Goku/Vegeta. Unlock metadata was kept conservative where no unique prerequisite is consistently established.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-10.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `a4ba623945d9ec3903c6440d5cd865e46bdce78e` (PQ91–100 research), `6a8ff70456aec7002287aeeb2ff44905c5128aa6` (coverage audit), `c284f67ee57dd66a28cc8a7622c21ed60fbf3458` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **26 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Base-game PQ1–PQ100 provenance pass is now complete at the current record-level-source standard. **Exact next task: continue with the remaining 26 records lacking individual sources, starting with the next highest-priority batch and preserving the same evidence standard.** Do not assume the remaining records are lower quality merely because they lack sources; inspect each batch, reconcile objectives/rewards/unlocks independently, and update coverage audit, changelog, handoff, and Actions/status after each pass.


### 2026-09-19 cycle update — PQ161–170 provenance pass
- Workstream: Remaining DLC Parallel Quest record-level provenance.
- Completed source coverage for **PQ161–PQ170**, with explicit source URLs and 2026-09-19 verification dates.
- Independent references confirm PQ161–162 as Hero of Justice Pack 2 and PQ163–170 as Future Saga Chapter 1, along with their listed Ultimate Finish conditions and basic rewards.
- Existing explicit reward/drop-rate evidence was preserved; no probabilities were inferred beyond the maintained corpus.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-16.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `5c0eaf8f926dc5495b20f21fb8932412abcb27ac` (PQ161–170 research), `4ea086886b425dd0db2a10adc38a34e29a57348e` (coverage audit), `e86fa4086cc14760b30c0ca7781d45c550aa2ec6` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **16 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **PQ171–PQ180**, then PQ181–PQ186. Continue reducing the remaining 16 unsourced records with the same record-level provenance standard. Pay attention to Future Saga Chapter 1/2/3 and later DLC associations, objective/reward changes, and exact skill-drop semantics; preserve explicit percentages but never infer them. Update coverage audit, changelog, handoff, and Actions/status after each pass.


### 2026-09-19 cycle update — PQ171–180 provenance pass
- Workstream: Remaining DLC Parallel Quest record-level provenance.
- Completed source coverage for **PQ171–PQ180**, with explicit source URLs and 2026-09-19 verification dates.
- Independent references cross-check the Future Saga Chapter 1/2 and Dragon Ball DAIMA DLC associations, Ultimate Finish conditions, and documented rewards.
- Existing explicit reward/drop-rate evidence was preserved; no probabilities were inferred beyond the maintained corpus.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-17.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `acb3b5a10fbf7b47efbb698069a802d47ffbf1e1` (PQ171–180 research), `b2e4a7a14736864f50ce1270b27f987e928b2145` (coverage audit), `4de13829c0efcd4c19674bcea9c87ea79e110d14` (changelog).
- Validation census: **176 total records**, **0 missing `unlock_condition` fields**, **6 records still lacking individual `sources` arrays**.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: **PQ181–PQ186**. These are the final six unsourced records. Continue with the same record-level provenance standard, carefully distinguishing Dragon Ball DAIMA Pack versus Future Saga Chapter 3/4 content and preserving documented Ultimate Finish/reward evidence without inventing probabilities. Update coverage audit, changelog, handoff, and Actions/status after the final pass.


### 2026-09-19 cycle update — PQ181–186 final provenance pass
- Workstream milestone: **complete record-level provenance coverage for PQ1–PQ186**.
- Completed source coverage for **PQ181–PQ186**, with explicit source URLs and 2026-09-19 verification dates.
- Independent references cross-check the final DLC associations, Ultimate Finish conditions, and documented rewards. PQ181 is Dragon Ball DAIMA Pack; PQ182–184 are Future Saga Chapter 3; PQ185–186 are Future Saga Chapter 4.
- PQ184's explicitly documented 50% Ultimate Finish bonus-slot rate for Chaotic Time Impact was preserved. No unsupported probabilities were added to the other five final records.
- Files changed: `docs/data/parallel-quest-research-batches/pq-batch-18.json`, `docs/COVERAGE-AUDIT.md`, `CHANGELOG.md`, and this handoff.
- Commits: `66e6e9a3b04523dabac4bc2aaf684f4806415b9a` (PQ181–186 research), `fbeee7523b6e557562b470e749d2a4ac3734b0de` (coverage audit), `a81fe43704ba7b661ee4c72a053c6ac50c691db0` (changelog).
- Validation census: **176 total records, 0 missing `unlock_condition` fields, 0 records lacking individual `sources` arrays**. This completes the current PQ provenance coverage objective.
- CI: inspect Actions/status for the final handoff commit before changing validators. No validator was weakened.
- Exact next task: do not stop at provenance completion. Re-open the repository TODO/priority list and identify the highest-priority remaining **data-quality/functionality gap**. Continue exhaustive page/function/detail coverage rather than starting another redundant source pass. Preserve conflicts, cite evidence, and update this handoff after the next substantive work unit.


### 2026-09-19 cycle update — Super Soul batch 03 promotion and priority refresh
- Workstream: post-PQ-provenance data-quality expansion.
- Inspected the authoritative `TODO.md` after completing PQ1–PQ186 provenance. The previous handoff's stale PQ-to-skill unresolved count was no longer accurate: the live `docs/data/pq-skill-crosslink-report.json` is currently `resolved` with **0 unresolved references** against the 298-record canonical skill catalog.
- Promoted **Super Soul research batch 03 (IDs 024–031)** into `docs/data/super-souls-record-layer.json` after duplicate, schema, acquisition, trigger/effect, Limit Burst, and independent-source reconciliation. Canonical Super Soul population is now **26 records**, up from 18.
- Preserved unresolved current shop-rotation timing and drop-rate semantics; no unsupported values were filled.
- Updated `docs/Super-Souls-Database.md`, `docs/data/coverage-gaps.json`, `TODO.md`, and `CHANGELOG.md` to reflect the new baseline and priorities.
- Commits: `ca75f7b653ea8622d576ecd27b794b29dd727909` (canonical Super Souls), `f6842a2c5e2b41d879640d4b3962d76ff5de799d` (batch finalization), `5485adf46c15c6dae5d96de2caf81352fbdb679f` (database page), `7cf0a059f1cbadfe12358a0ea9434f5ab705128` (coverage gaps), `8d5472238261bcf35bce7703026969762cc240f7` (TODO), `e57927e52634f456d6f7a9244ebf33963194b5eb` (changelog).
- Validation: live cross-link report is resolved with 0 unresolved references; repository artifact audit remains clean in the inspected coverage audit. GitHub Actions still exposes no usable runner-step evidence for the known pre-run failures, so validators were not weakened and CI was not claimed as passing.
- Exact next task: continue **Super Soul expansion** beyond the 26-record baseline, prioritizing acquisition families that are still absent/underrepresented (Expert Missions, raids/events, shops/rotations, DLC-specific souls), while independently reconciling triggers/effects/Limit Burst behavior. In parallel, continue the P0 Actions diagnosis only from observable GitHub evidence and maintain the exhaustive coverage gap map.


### 2026-09-19 cycle update — FUTURE SAGA Chapter 4 Super Soul expansion
- Workstream: Super Soul catalogue expansion after PQ provenance completion.
- Added four FUTURE SAGA Chapter 4 Super Souls to the canonical research layer: records **032–035**.
- Official DLC evidence establishes four new Chapter 4 Super Souls; repository PQ185/PQ186 reward inventories provide acquisition leads. Community testing supplies secondary effect evidence for three records. These are explicitly marked **partially verified**; item-level mechanics, exact Normal-vs-Ultimate-Finish mapping, and drop rates were not inferred.
- Canonical Super Soul population is now **30 records**.
- Files changed: `docs/data/super-souls-record-layer.json`, `docs/Super-Souls-Database.md`, `docs/data/coverage-gaps.json`, `CHANGELOG.md`, and this handoff.
- Commits: `704820758f555d13ddcf06350be1258f8c6b24fa` (canonical records), `fe7e53073daaeae8dd1826980d2157a0e77d6c4d` (database), `e348bda6a107c873dcf984c97d0a1b93bc403e4c` (coverage gaps), `87a9f9f7078f108a55771010e910fe15ea2e10dc` (changelog).
- Validation: PQ-to-skill cross-link report remains resolved with 0 unresolved references; coverage audit artifact check remains clean. Do not infer CI success where GitHub exposes no workflow-run evidence.
- Exact next task: continue Super Soul expansion beyond 30, prioritizing acquisition families absent from the canonical layer (Expert Missions, raids/events, TP Medal Shop rotations, DLC-specific rewards) and upgrading partially verified Chapter 4 mechanics only when stronger item-level evidence is found.


### 2026-09-19 cycle update — Raid/Event Super Soul batch 04
- Continued the Super Soul expansion after Chapter 4, targeting an underrepresented acquisition family: **Online Raid Quest** rewards.
- Added research batch 04 and promoted canonical records **036–039**: “Buu's reached full power!”, “I'm over 1,000 years old.”, “My Ki is building... Overflowing...”, and “I am going to bathe in your blood!”.
- Reconciled acquisition and secondary effect evidence from the raid inventory/catalog and historical GameFAQs raid reports. Record 036 retains the documented 10%-vs-20% discrepancy; record 039 retains the categorical XXL label without inventing a percentage.
- Canonical Super Soul population is now **34 records**.
- Commits: `94edc1e35bc08f5c77d1ab3c30f9b879bf857c32` (research batch), `83c7d0831599230cecbb2cd89a75d57e8bf3cc86` (canonical layer), `52006691fd5ca1760153c0f8dee23de36f5ab776` (database), `96ad639272a60d11142d1308d8c801cfa4987991` (coverage), `9ebedde3a9d885334629617c15bcca32b3a2f9e4` (changelog).
- Next task: continue Super Soul expansion beyond 34, prioritizing **Expert Mission-specific souls**, then additional raid/event families, TP Medal Shop/STP rotations, and DLC-specific rewards. Upgrade secondary evidence only when stronger item-level evidence is found.
- Do not infer drop rates or historical recurrence schedules, and do not claim CI success without exposed workflow-run evidence.


### 2026-09-19 cycle update — Raid/Event Super Soul batch 05
- The planned Expert Mission investigation was checked against current repository/source evidence. Available Expert Mission references primarily enumerate mission rewards as skills, Zeni, and TP Medals and do not establish a new Expert-Mission-specific Super Soul family. Do not invent one merely to satisfy the priority label.
- Continued the broader Super Soul acquisition-family expansion with records 040–043: “You fool! Why are you laughing?”, “Not on my watch!”, “Over here, you idiot...”, and “Bye-bye, universe!”.
- Added docs/data/super-souls-research-batch-05.json and promoted the four records into the canonical layer. Official anniversary material independently confirms the Fused Zamasu/“Bye-bye, universe!” reward and historical Masked Saiyan/Hercule raid rewards; secondary item records provide effect details.
- Canonical Super Soul population is now 38 records.
- Commits: 868ce79a2f30f76f405ab2330a1e905a81489f0e (research batch), 355a4276df4cd65b9bf1d943920db1ab4b811ce9 (canonical layer), a62eef930190807741b9729c89a67b83d882cd3e (database), 709419be50351186f125a4d7c03a18db254595c1 (coverage), ec234d52ca0b8c6e41b55fab2d2eb2f7b3f9b1a4 (changelog).
- Next task: continue Super Soul expansion beyond 38, prioritizing additional raid/event families and DLC-specific rewards; simultaneously audit the existing PQ cross-link layer for Super Souls that are named but not yet promoted into canonical records.
- Preserve conflicts, do not infer drop rates/recurrence schedules, and do not claim CI success without exposed workflow-run evidence.
