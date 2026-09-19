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

**PQ unlock-field frontier is complete.** The live 18-batch census now shows explicit `unlock_condition` fields on all 176 canonical records; do not reopen the completed PQ unlock-field pass unless new evidence or a contradiction appears.

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
**P1 skill race-restriction census, following completion of the PQ unlock-field pass.**

### Next exact action
1. Recompute the live skill census.
2. Identify every CaC-usable skill with `race_restriction: null`.
3. Research explicit race/gender/form restrictions from accessible evidence; do not infer a restriction from character ownership alone.
4. Preserve unresolved fields when evidence is insufficient.
5. Update the relevant skill data and `docs/COVERAGE-AUDIT.md` in evidence-backed batches.
6. Inspect GitHub Actions without weakening validators.
7. Check for accidental AI/internal citation artifacts.
8. Update this file and commit the complete cycle.

### Latest known PQ unlock census
**176 canonical PQ records across 18 research batches; 0 records lack an explicit `unlock_condition` field.** Field presence is not equivalent to exact-route verification; PQ54 retains a documented route conflict, and PQ36 retains the known numbering/existence anomaly.

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


### 2026-09-19 cycle update — Raid Super Soul candidate batch 06
- Continued the Super Soul expansion by auditing the broader raid-exclusive catalogue rather than forcing an Expert Mission family that current evidence does not establish.
- Indexed records **044–047**: “Let's see you handle THIS kind of power!”, “Your time in this fight ends now!”, “Kind of human-like, don't you think?”, and “Kicking a Shadow Dragon in the head is not a wise thing to do!”.
- Added research batch `docs/data/super-souls-research-batch-06.json`. All four are explicitly **partially verified** because acquisition-family evidence is stronger than the currently reconciled item-level mechanic evidence.
- Canonical indexed Super Soul population is now **42 records**.
- Commits: `cbee59a0e5efd86dc07a95e654a1a0274a426b87` (research), `9ee20d52e9483b2986d94c38ca254bb807fdcd9d` (canonical), `4a5f0bb609a53428189449a0b5258f1c6690d77e` (database), `df87d99e5d806a0bc05d61aefeb69066faec66f9` (coverage), `bdfb0d97768e113f2bf58271465e2852b1aea738` (changelog).
- Next task: reconcile 044–047 against item-level effect evidence, then continue the raid/DLC Super Soul census. Do not infer drop rates, recurrence schedules, or numeric values from categorical labels.


### 2026-09-19 cycle update — Raid Super Soul reconciliation 044–047
- Reconciled the four previously indexed raid candidates against item-level/community evidence.
- **044** “Let's see you handle THIS kind of power!”: verified core effect — Giant Form boosts all attacks (+15% reported) and provides stamina auto-recovery; Great Ape Baby raid provenance established.
- **045** “Your time in this fight ends now!”: verified — Instant Transmission restores Ki; catalogue data lists +100 Ki, while community testing reports one bar normally and two bars for close use. Saibaman raid provenance established.
- **046** “Kind of human-like, don't you think?”: verified — Energy Field temporarily reduces damage taken for wearer and allies by 20% for 10 seconds; Super 17 raid provenance confirmed by official Bandai Namco event documentation.
- **047** “Kicking a Shadow Dragon in the head is not a wise thing to do!”: remains partially verified — defense effects are documented, but the stamina-damage reduction magnitude and exact historical raid mapping remain unresolved.
- Canonical population remains **42 records**.
- Commits: `50447e2f6275734c3996879a2c937eb1c0e9d77b` (canonical), `f6c89aefe23ab22f6f785a9c9d473a035d04e4c3` (research), `a3f717b799b6196cfd644b341a6113fdcb8e5ec3` (database), `b811a8a34eff61916ea21a79628cbb2b9d525663` (coverage), `f1a6b8a879465c0b11c35c049316402e5c1f9919` (changelog).
- Next task: continue the raid/DLC Super Soul census beyond 047, prioritizing unreconciled raid-exclusive names and exact item-level acquisition/effect provenance. Do not infer recurrence schedules or drop probabilities.


### 2026-09-19 cycle update — Awoken/CaC classification correction
- Workstream: **Awoken / Transformation coverage audit**, following the tracker’s P1 cross-system coverage priority. The prior handoff’s Super Soul work remains complete at 42 indexed records; this cycle corrected a higher-priority data-quality issue in the canonical skill layer.
- Audited current Awoken classification against Xenoverse 2-specific references. Three seeded records incorrectly presented character-only forms as CaC transformations: **Pure Progress**, **Super Saiyan Blue Kaioken**, and **Supersonic Mode**.
- Corrected those three records in `docs/data/skills.json` to `usable_by_cac: false`, added correction/research provenance, and created/updated `docs/data/skill-research-batches/skill-batch-37.json`.
- Evidence: the maintained research corpus explicitly lists Pure Progress as Hit-only and SSGSS Kaioken/Supersonic Mode among cast-exclusive Awoken states; the current Awoken reference likewise separates CaC forms from race-exclusive/cast-only forms. cite references are kept out of repository files; web evidence was reviewed externally during this cycle.
- Updated `TODO.md`, `docs/data/coverage-gaps.json`, and `CHANGELOG.md` so the stale Super Soul count is now **42** and the Awoken correction is tracked.
- Commits: `e8550a05f97f421948edb4ff74a9b2b29e223391` (canonical skill correction), `3fec3b5d0382aec59598d5660de47c5164a367cf` (correction batch), `2fb1ad700ba2f2507d69e9c6d69ea982b0e5ffdf` (TODO), `7b8d9656a0ab66cbd4e842ab11e4ab5ac4d539bd` (changelog), `b72cf0efc817f47ddb74f515a37fc08f3ca4b7e5` (coverage).
- Evidence limitation: this cycle corrected availability/classification only. Exact stage modifiers, resource costs, unlock routes, and version-sensitive mechanics for the remaining Awoken records still require individual reconciliation.
- Next exact task: continue the Awoken/Transformation audit record-by-record, prioritizing remaining indexed forms with only `indexed` status and resolving CaC availability before adding new skill batches. Preserve character-only forms as such and do not infer CaC eligibility from category membership alone.


### 2026-09-19 cycle update — canonical skill deduplication + Awoken audit continuation
- Continued the Awoken/Transformation data-quality track and inspected the live canonical `docs/data/skills.json` rather than assuming its 298 records were unique.
- Found **15 duplicate skill-name identities** in the canonical layer. Several were thin `indexed` placeholders duplicated by richer researched records; `Big Bang Knuckle` also existed twice with conflicting category metadata.
- Reconciled duplicates by exact skill name: retained the richest record, merged distinct source URLs/non-empty fields, and preserved all historical research batch files. Canonical skill population is now **283 unique records** instead of 298 duplicate-containing records.
- Added `docs/data/skill-research-batches/skill-batch-39.json` documenting the correction and the 15 affected names.
- Synchronized `docs/data/pq-skill-crosslink-report.json` from 298 to **283** canonical records; its unique canonical name count was already 283 and unresolved count remains 0.
- Updated `TODO.md` to reflect the deduplicated canonical count.
- Important: do not recreate the removed generic duplicate entries merely to reach 298; the canonical uniqueness rule is one record per exact skill identity, while historical research remains preserved.
- Next task remains the Awoken/Transformation audit: resolve remaining `indexed` forms' CaC availability, unlock routes, costs, stages, and version-sensitive mechanics record-by-record. The current deduplication correction should be treated as a prerequisite for reliable coverage counts.


### 2026-09-19 cycle update — Saiyan Awoken verification batch 40
- Continued the Awoken/Transformation audit after canonical skill deduplication.
- Verified **Future Super Saiyan**, **Super Saiyan God Super Saiyan**, and **Super Saiyan God Super Saiyan (Evolved)** as Saiyan CaC Awoken Skills.
- Recorded SSGSS unlock as level 90 + max Whis friendship; recorded Evolved as level 95 + max Vegeta friendship + prior SSGSS acquisition. Future Super Saiyan remains on the Vegeta/Capsule Corporation progression route.
- Preserved the distinction between a mentor awarding a skill to any race and the actual race restriction: SSGSS and Evolved remain Saiyan-only despite Whis being able to award them to a non-Saiyan character meeting the mentor requirement. This distinction is supported by the Awoken reference and GameFAQs unlock documentation. cite references are external only; repository provenance is stored in skill-batch-40.json.
- Added `docs/data/skill-research-batches/skill-batch-40.json`; updated `docs/data/skills.json`, `TODO.md`, `docs/data/coverage-gaps.json`, and `CHANGELOG.md`.
- Next task: continue the Awoken audit across remaining partially verified race-exclusive and universal forms, resolving unlock routes and exact mechanics before adding new forms.


### 2026-09-19 cycle update — Core Awoken reconciliation batch 41
- Reconciled the remaining primary Awoken records in the canonical layer: **Kaioken, Potential Unleashed, Ultra Instinct, Beast, Super Saiyan, Super Vegeta, Super Saiyan God, Turn Golden, Purification, Become Giant, and Power Pole Pro**.
- Promoted all 11 from `partially_verified` to `verified` for core unlock/CaC availability facts.
- Recorded the documented race boundaries: universal CaC forms versus Saiyan, Earthling, Namekian, Majin, and Frieza Race exclusive forms. Do not infer race eligibility from mentor-award behavior.
- Recorded supported resource thresholds: Kaioken 100/300/500 Ki, Super Saiyan 300/400/500 Ki, Super Vegeta 300/400 Ki, Super Saiyan God 300 Ki, race-exclusive 300 Ki forms where supported, Power Pole Pro 0 Ki, and 500 Ki activation for Potential Unleashed/Beast/Ultra Instinct.
- Added `docs/data/skill-research-batches/skill-batch-41.json` and updated canonical skills, TODO, coverage gaps, and changelog.
- External evidence reviewed includes the current Awoken reference, individual transformation records, GameFAQs unlock tables, and the current research corpus. cite references are external only; repository provenance is stored in batch 41.
- Next exact task: audit the remaining transformation records for version-sensitive mechanics and cast-only/DLC boundaries, then reconcile any still-partial records without inventing unsupported values.


### 2026-09-19 cycle update — Transformation stage reconciliation batch 42
- Reconciled **Super Saiyan 2** as a stage of the Super Saiyan Awoken Skill: Saiyan-only, 400 Ki, not separately equipped.
- Audited **The Power to Overcome** from Future Saga Chapter 4. Core facts are now documented: universal CaC availability, 500 Ki activation, Chapter 4 DLC requirement, unlock after Quest 31 / Ultimate All-Out Showdown, and two-stage behavior.
- Exact Power to Overcome numeric stage modifiers remain deliberately unresolved because current 2026 sources conflict on defense, speed, damage, duration, and cooldown values. Do not replace the conflict with a guessed value.
- Added `docs/data/skill-research-batches/skill-batch-42.json` and updated canonical skills, coverage gaps, TODO, and changelog.
- Next exact task: continue version-sensitive transformation mechanics and remaining partial Awoken records, prioritizing independent corroboration of exact stage values.


### 2026-09-19 cycle update — Power to Overcome mechanics batch 43
- Enriched the canonical **The Power to Overcome** record using current 2026 testing references.
- Stage 1 now records reported +20% defense, +5% movement speed, below-50%-HP recovery, and the unblockable sword-strike grab replacement.
- Stage 2 now records reported ~12-second duration, +15% basic attack damage, +30% Strike/Ki Super damage, effectively/infinite Ki regeneration, and HP drain.
- Conflicting Stage 2 movement-speed and cooldown reports remain unresolved; exact HP regeneration rate also remains unresolved.
- Added `docs/data/skill-research-batches/skill-batch-43.json`; updated skills, coverage gaps, and changelog.
- Next task: continue the remaining version-sensitive transformation audit and do not promote disputed numeric mechanics without independent corroboration.


### 2026-09-19 cycle update — Awoken mechanics batch 44
- Synchronized current descriptive mechanics across the canonical Awoken layer: Kaioken, Potential Unleashed, Beast, Super Saiyan stages, Super Vegeta, Future Super Saiyan, Super Saiyan God, SSGSS, SSGSS Evolved, Turn Golden, Purification, Become Giant, Power Pole Pro, Ultra Instinct, and Super Saiyan 2.
- Added stage-specific resource thresholds, attack/defense modifiers, Stamina/Ki drain, movement effects, moveset changes, and Ultra Instinct's post-1.22.00 non-consuming transformation behavior.
- Added `docs/data/skill-research-batches/skill-batch-44.json` and updated canonical skills, coverage gaps, and changelog.
- Source baseline: consolidated Awoken research table plus individual Awoken references. Meta/build rankings were intentionally excluded.
- Next exact task: finish the remaining Awoken/version-sensitive audit by reconciling disputed values and documenting version provenance, then proceed to QQ Bang expansion.


### 2026-09-19 cycle update — Indexed Evasive skill audit batch 45
- Workstream: P1 canonical skill audit.
- Live skill census: 283 unique records; 18 indexed, 247 partially_verified, 18 verified.
- Audited eight indexed Evasives: Absolute Zero, Dragon Burn, Explosive Wave, Punisher Guard, Final Pose, Mach Dash, Angry Shout, Energy Barrier.
- Updated docs/data/skills.json, docs/data/skill-research-batches/skill-batch-45.json, and docs/COVERAGE-AUDIT.md.
- Verified CaC availability, acquisition route, stamina cost, naming, and descriptive mechanics. Exact reward-slot/drop gating remains unresolved and no probabilities were invented.
- Commits: e2e163920ce684a286515c6b06556c5ecea57554; b6bc84f95b8f540d1075c8290d5b4e59fc00a532; a654c7bad4faa66b3b81378b03eb11b79ac3e371.
- Validation: modified JSON parsed; no accidental ChatGPT/UI citation artifacts found.
- CI: no pull-request workflow runs returned for the latest coverage commit; validators were not weakened.
- PQ state: 176 records, 0 missing unlock_condition fields, 0 missing individual source arrays.
- Exact next task: audit the remaining 18 indexed skill records, prioritizing CaC/race restrictions, acquisition routes, resource costs, and DLC/version provenance.


### 2026-09-19 cycle update — Indexed skill completion pass
- Workstream: P1 canonical skill audit.
- Audited all 18 records that remained indexed after the canonical deduplication and Evasive audit: Destructo-Disc, Emperor's Blast, Final Flash (Super), Galick Gun, Kamehameha, Masenko, Afterimage Strike, Dancing Parapara, Energy Charge, Energy Release, Instant Charge, Rise to Action, Rising Rage, Solar Flare, Spirit Boost, Time Bullet, Wall of Defense, and Final Kamehameha.
- Updated docs/data/skills.json with CaC availability, acquisition route, source location, Ki cost, and core descriptive mechanics where current evidence supported them. Character-only records were explicitly kept non-CaC.
- The live skill census is now 283 unique records with no records left at `indexed` status; the reconciled records remain `partially_verified` where exact reward-slot probabilities or version-sensitive details remain unresolved.
- Updated docs/COVERAGE-AUDIT.md. Commit: 8f82dd22a7e0d43f4186da95295807b1fd8feedd (skills), e17130e2f663ee18b59bc755d6e2f6a046cab3cf (coverage).
- Tooling limitation: creation of a new skill-batch-48.json failed twice because the GitHub create-file wrapper returned HTTP 422 requiring a SHA for a new file. No historical batch was overwritten to bypass this.
- CI: no new actionable workflow evidence was exposed; validators were not weakened.
- Exact next task: recompute the live skill census, identify the highest-impact partially_verified gaps, then continue P1 skill research into exact race/gender restrictions, DLC/version provenance, and unresolved reward/acquisition semantics before moving to QQ Bang expansion.


### 2026-09-19 cycle update — Skill acquisition/CaC reconciliation follow-up
- Continued P1 canonical skill research after clearing all `indexed` records.
- Reconciled another high-impact partial cohort: Burst Reflection, Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, God Breaker, Heroic Counter, Punisher Shield, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz, Celestial Wave, Force Shield, Instant Rise, Ki Explosion, and Maiden Burst.
- Added concrete acquisition/source locations and CaC eligibility; filled supported zero-Ki Evasive costs. Late-PQ DLC pack provenance remains explicitly unresolved where quest-number evidence alone is insufficient.
- Skills commit: `4ec88f3820e2a38d49f3cfa10e6256b244e679c7`. Coverage commit: `756f51f2e9c54d4e5f5e6bc026dc8b027bbd0ab7`.
- Exact next task: recompute the live partial-field gaps and prioritize records with missing race restrictions, DLC/version provenance, or exact reward-slot semantics. Do not downgrade the evidence standard merely to increase the verified count.


### 2026-09-19 cycle update — Skill CaC/provenance reconciliation batch
- Recomputed the live canonical skill census: **283 unique records; 265 partially_verified; 18 verified; 0 indexed**.
- Identified remaining partial-field gaps, with race restrictions and DLC/version provenance now the dominant broad gaps rather than missing indexed records.
- Reconciled **Burst Reflection, Divine Kamehameha, Perfect Shot, Spirit Bomb, Instant Transmission, Super Guard, Afterimage, and Celestial Wave** using current Xenoverse 2 references.
- Added/confirmed CaC eligibility, acquisition routes, supported resource values, and provenance. Divine Kamehameha remains explicitly version/update-sensitive; Celestial Wave retains Vote Pack/PQ151 provenance.
- Skills commit: `28a6fb4b85a7a6eabf4b60052a8a92f7a5c6bee1`. Coverage commit: `4c4576a2c0c9571f4dd3e8b5e275fccd5c4e8cc5`.
- Exact next task: continue the missing `usable_by_cac` and race/DLC field audit, prioritizing skills with character-only users or recent DLC/DAIMA-era names. Do not mark a skill verified merely because a source lists a user; establish Future Warrior/CaC availability explicitly.


### 2026-09-19 cycle update — Charge/support CaC and race restriction batch
- Continued the P1 missing-`usable_by_cac` audit using current Future Warrior technique references and individual skill pages.
- Reconciled **Bending Kamehameha, Full Power Charge, Maximum Charge, Charged Ki Wave, Ultimate Charge, Burst Charge, Data Input, Pressure Sign, Meditation, Deadly Dance, and Quick Sleep**.
- Confirmed CaC availability for the charge/support/mentor skills; recorded Quick Sleep as **Majin-only** rather than treating it as universally available. Data Input is Extra Pack 1 / Expert Mission 20; Ultimate Charge and Burst Charge are PQ134/Extra Pack-era skills.
- Skills commit: `00ef8d9e609274297915e365f21f0924e598d968`; coverage commit: `b8be718e528cbb5c03e356448d8639ee160cab9e`.
- Note: the public Fandom endpoint was robots-blocked in one web lookup, so corroboration used accessible Dragon Ball Wiki/current repository source URLs rather than pretending the blocked page was independently verified.
- Exact next task: continue the remaining missing `usable_by_cac` cohort, prioritizing recent DLC/DAIMA skills and explicit character-only boundaries, then reconcile race restrictions before promoting any records to `verified`.


### 2026-09-19 cycle update — Future Warrior ultimate-skill reconciliation
- Continued the missing-`usable_by_cac` audit with Future Warrior-specific evidence rather than inferring CaC eligibility from a character's use of a skill.
- Reconciled **Big Bang Kamehameha, Super Spirit Bomb, Emperor's Death Beam, and Final Explosion**. Big Bang Kamehameha is obtainable through the TP Medal Shop; Super Spirit Bomb through Expert Mission 16; Emperor's Death Beam is obtainable by the Future Warrior; Final Explosion through the TP Medal Shop. 
- Skills commit: `ed425d388377902aed738ba03ae49b85342d3c41`; coverage commit: `71c9479de17e21b3a0eac16f5b18ddd6b8614e32`.
- The external Fandom search endpoint remains intermittently robots-blocked; accessible search results and repository source URLs were used where available. No unsupported claims were promoted to `verified`.
- Exact next task: continue the remaining missing-CaC cohort, focusing on DAIMA/Future Saga skills and explicit racial/character boundaries, then perform a census of remaining null core fields before moving beyond the skills workstream.


### 2026-09-19 cycle update — DAIMA/Future Saga boundary investigation
- Read the live handoff and continued the P1 missing-`usable_by_cac` audit.
- Investigated **Burning Blast, Force Edge, Final Flash (SS3 DAIMA), and Super Kamehameha (SS4 DAIMA)** plus the broader Future Saga Chapter 2 cohort. Current sources confirm their DAIMA character/PQ provenance, but do not explicitly establish Future Warrior eligibility for the individual moves. The repository therefore leaves `usable_by_cac` null rather than incorrectly marking them false or true. 
- This follows the repository's evidence rule: character-equipped skill lists are not sufficient proof of CaC availability, because Xenoverse 2 has race/gender/transform-specific restrictions. 
- Coverage investigation commit: `79e5e23a659df0b4eb73fb73bb505f0f6d4ea953`.
- Exact next task: continue the unresolved Future Saga/DAIMA cohort using explicit Future Warrior/CaC evidence, then audit remaining null `usable_by_cac`, `race_restriction`, and DLC/version fields as a complete census. Do not promote records to `verified` without resolving acquisition/reward semantics as well.


### 2026-09-19 cycle update — additional Future Warrior skill evidence
- Reconciled **Phantom Fist, Shield Barrier, Assault Vanish, Fighting Pose K, Death Ball, Supernova, Divine Lasso, Lightning Impact, and Prominence Flash** with explicit Future Warrior evidence. 
- Skills commit: `550556f9385263b468fd2153ca38bdc0b98dda4e`.
- Coverage commit: `7ec129d63d11c6353e3d82995d614ffe44e9b193`.
- Live null-`usable_by_cac` census before this batch contained 35 records; this batch removes nine explicit-evidence gaps while preserving the `partially_verified` evidence standard.
- Exact next task: continue the remaining 26 null-CaC records, prioritizing Future Saga/DAIMA and other recent DLC skills, then audit the 190 CaC records still lacking explicit `race_restriction` values. Do not infer race scope from generic CaC availability.


### 2026-09-19 cycle update — Future Warrior/form-exclusive reconciliation
- Continued the null-`usable_by_cac` audit using the current Future Warrior technique corpus. The source explicitly documents that Future Warrior techniques can be race/gender/transform restricted, so form-specific access is represented rather than flattened into universal availability. 
- Reconciled **Surging Spirit, Dragon Fist, Divine Ray Bomb, Dragon Thunder, Final Rampage, Godly Display, Supreme Fury, and Victory Rush**. `Surging Spirit` is specifically recorded as usable through Ultra Instinct Future Warrior access.
- Skills commit: `6f1a988f2eee96c59e137999f6842cd628b49c73`; coverage commit: `96ff82019d1d8be3abf05805e6346cd8e6e89f81`.
- Exact next task: recalculate the remaining null-CaC cohort and continue explicit-evidence research. Then begin the 190-record race-restriction census, prioritizing known race/gender/form-specific techniques instead of assigning `All CaC races` by default.


### 2026-09-19 cycle update — explicit race restriction audit
- Shifted from null CaC eligibility into the next mandated race-restriction workstream.
- Reconciled **Saiyan Spirit, Explosive Buu Buu Punch, Zigzag Express, Ill Bomber, Candy Beam, Buu Buu Ball, Shining Slash, Burning Slash, Evil Flight Strike, Darkness Rush (Melee), and Darkness Rush (Ranged)** using the Future Warrior technique corpus. 
- Skills commit: `e6c352c9423aa2a42a6fa271644b3d68f5306902`.
- Coverage commit: `dbe618bb14ab12938df39f32edf3e526baa51780`.
- Exact next task: continue the race-restriction census, prioritizing records whose source text explicitly names a race or gender, then revisit the remaining null-CaC cohort. Do not replace an explicit multi-race restriction with `All CaC races`.


### 2026-09-19 cycle update — unresolved recent DLC evidence
- Recalculated the live census: **18 null-CaC skills** and **184 CaC-eligible skills with null race restriction**.
- Reviewed recent DLC candidates without over-promoting ambiguous records. Dark Inscription, Emperor's Cannon, and Chaotic Time Impact are documented on Golden Frieza (Ultra Supervillain); Burst Blitz, Dragon Spark, and Soaring Rush are documented on Goku (Mini). Current evidence does not establish CaC access for these records, so they remain null. 
- Skills commit: `b9a8e3ae8baa7c8acbe11c150266a01b1f0c747b`.
- Coverage commit: `865fb30619def2d79296b5cb767dbe2576c069e6`.
- Next: continue the 18-record null-CaC cohort, then resume the 184-record race-restriction census using explicit race/gender/form evidence only.


### 2026-09-19 cycle update — explicit Future Warrior corrections
- Recalculated and re-audited the null-CaC cohort. **Mystic Flash** and **Thunder Flash** are explicitly included in the Future Warrior technique corpus and were corrected to `usable_by_cac: true`; race scope remains unresolved rather than being guessed. 
- Skills commit: `cbb114e5cef2b499450dc937367d3b95e7a1e202`.
- Coverage commit: `4db0b54773c7bdf8964ec74d47356436fdc28250`.
- Next: continue the remaining null-CaC cohort, then resume the explicit race-restriction census.


### 2026-09-19 cycle update — Requiem of Destruction
- Confirmed **Requiem of Destruction** as an explicit Future Warrior/CaC technique. Its technique page identifies Future Warrior as a user and gives New Parallel Quest 104 as the acquisition route. 
- Skills commit: `6cc97745e9856af45e52d148aa3d40f6f14f7184`.
- Coverage commit: `2a6a05a09584ebfcd7ef0936015969123ae25d74`.
- The null-CaC cohort is now **15 records**. Continue explicit-evidence review; do not infer CaC eligibility from a character's equipped moves alone.


### 2026-09-19 cycle update — DLC evidence boundary re-audit
- Re-audited the remaining unresolved DLC cohort. Character movesets and PQ reward tables were verified, but those sources do not by themselves establish CaC eligibility. God of Destruction's Plaything/Poise remain tied to Belmod; Force Edge/Burning Blast remain tied to SS3 Vegeta (DAIMA) in the current evidence. 
- Skills commit: `dd675147e02a668b79a8b94b2293a8d55d27fbf9`.
- Coverage commit: `f38f3e3544682ab7d107c2ba1de5e10b8dbb6b87`.
- Next: seek explicit Future Warrior/CaC references for the remaining 15 records; if unavailable, keep them unresolved and move to the race-restriction census rather than guessing.


### 2026-09-19 cycle update — DAIMA CaC evidence
- Reconciled **Force Edge, Burning Blast, Final Flash (SS3 DAIMA), and Super Kamehameha (SS4 DAIMA)** to `usable_by_cac: true` based on explicit CaC-focused coverage and CaC build/combo evidence. 
- Skills commit: `9db1be415b06fbfde8288f0eb8e47548477b30f6`.
- Coverage commit: `9ef664e50f208c1a3e8b955ee10f199e3ef40806`.
- Remaining null-CaC cohort is now **11 records**. Continue explicit evidence research before moving to the race-restriction census.


### 2026-09-19 cycle update — CaC build evidence correction
- Corrected **God of Destruction's Plaything** to `usable_by_cac: true` after finding explicit custom-character build evidence. 
- Skills commit: `c4c98ee41354038d4e0701c8d82a0f18c52b0df3`.
- Coverage commit: `a18eed0e500cf2c18818743a5a80d02daab5b3fa`.
- Remaining null-CaC cohort is now **10 records**. Continue explicit evidence research; do not infer eligibility from PQ rewards alone.


### 2026-09-19 cycle update — second-pass DLC CaC reconciliation
- Reconciled **Blaster Stream, God of Destruction's Poise, Full Power Destruction, Soaring Rush, Burst Blitz, and Dragon Spark** to `usable_by_cac: true` using explicit Future Warrior/CaC evidence. 
- Skills commit: `6bb28b3140b30047c04a22436593cfc4feb55157`.
- Coverage commit: `e876a3a75fd039bdac4a381e621043f771290060`.
- Remaining null-CaC cohort is now **4 records**: Dark Inscription, Emperor's Cannon, Heat Wave, and Chaotic Time Impact. Continue those four with the same evidence standard before beginning the race-restriction census.


### 2026-09-19 cycle update — Heat Wave CaC evidence
- Confirmed **Heat Wave** as CaC-usable from a documented player custom-character build. 
- Skills commit: `7e4650b290fdf48c6b1c237286b1a7772ff6cd25`.
- Coverage commit: `b029dc646ccacea77c579212bddff201ed1e204b`.
- Remaining null-CaC cohort is now **3 records**: Dark Inscription, Emperor's Cannon, and Chaotic Time Impact.
- Next: exhaust those three with explicit evidence, then begin the race-restriction census in earnest.


### 2026-09-19 cycle update — final null-CaC cohort closed
- Closed **Dark Inscription, Emperor's Cannon, and Chaotic Time Impact** as `usable_by_cac: true` based on explicit DLC 20 CaC-focused evidence. 
- Skills commit: `256d88f05c339da6bfcab7a7c7b3f1d18bd68a1e`.
- Coverage commit: `dbf067c9586b4c654c59821edba06fe36a09b342`.
- The explicit null-CaC census is now complete. Next priority is the **race-restriction census**: recompute the live cohort, identify every CaC-usable skill with `race_restriction: null`, and reconcile restrictions in evidence-backed batches without inferring from character ownership alone.


### 2026-09-19 cycle update — race restriction census kickoff
- Live census: **283 skills / 270 CaC-usable / 202 CaC-usable with race restriction still null**.
- Reconciled **Majin Kamehameha → Majin-only** using explicit Future Warrior technique documentation rather than merely its Majin character association. 
- Skills commit: `574e87cde26b8e8ed1bdaa410e7b59786e3e4305`.
- Coverage commit: `e636115236dad51830fbfcf96f9759bbf0176d7c`.
- Next priority: systematically identify additional explicit race/gender restrictions, beginning with skills whose Future Warrior documentation directly names a race restriction; do not blanket-mark character-origin skills.


### 2026-09-19 cycle update — universal CaC race batch
- Reconciled nine unrestricted CaC skills: **Kamehameha, Masenko, Energy Charge, Solar Flare, Afterimage Strike, Rise to Action, Wall of Defense, Destructo-Disc, Galick Gun** → `All CaC races`, based on explicit Future Warrior technique documentation. 
- Skills commit: `d248c4be6598c338181efd83a9c5edbe1472e496`.
- Coverage commit: `648330db2fbe3bb5c6502b0fc2c54a26034b8647`.
- Continue the race census with explicit race-specific entries; avoid treating a skill's character_source as proof of a CaC race lock.


### 2026-09-19 cycle update — universal race batch 2
- Reconciled **Candy Beam (Super), Petrifying Spit, and Kai Kai** → `All CaC races` using explicit Future Warrior/CaC evidence. 
- Skills commit: `dc4fc4234876c747429e81a73cf8be8be4c946e6`.
- Coverage commit: `2f3f95939e96e990b1da81ea76b91988e3aaaf79`.
- Continue the census with explicit race/gender/form-exclusive evidence; unresolved records remain untouched until evidence clears the threshold.


### 2026-09-19 cycle update — explicit restriction batch
- Reconciled **Zigzag Express → Majin male** and **Namek Finger → Namekian** using explicit Future Warrior restrictions. 
- Skills commit: `8425c7ed5804608fdbd38df7668d9495e94642a8`.
- Coverage commit: `f594df1729fe0bbc4e95f7b8ecb46e552939720d`.
- Continue the race census with the same strict evidence threshold, prioritizing explicit Future Warrior race/gender wording.


### 2026-09-19 cycle update — race provenance hardening
- Live race backlog: **189** CaC-usable records with `race_restriction` still unset.
- Hardened provenance for the existing explicit race-restriction cohort by adding the dedicated Future Warrior technique reference to ten records; no new restrictions were inferred without explicit evidence. 
- Skills commit: `7dad27d834189474438cae340de541b1ad1ca168`.
- Coverage commit: `1f8b558bc012640a4517507251886894ff62f3c4`.
- Next priority: continue mining the Future Warrior reference for any explicit race/gender/transform restrictions that map to the remaining 189 records; otherwise preserve null rather than guessing.


### 2026-09-19 cycle update — Pure Majin form batch
- Reconciled **Angry Shout, Vanishing Ball, Super Vanishing Ball, Teleporting Vanishing Ball, Pearl Flash, and Buu Buu Ball** as `Majin (Pure Majin form)` using explicit form-exclusive Future Warrior documentation. 
- Skills commit: `156e8fce946ffd4085ebb86e0accb41e943b0706`.
- Coverage commit: `21015527a5f032c42b9ad02768bedbd8717160e6`.
- Continue prioritizing explicit form/race/gender entries, with ordinary character-origin techniques remaining null until the evidence actually establishes a CaC restriction.


### Correction — Pure Majin batch representation
- Verified live skill records after the previous batch. Only **Angry Shout, Buu Buu Ball, Vanishing Ball, and Teleporting Vanishing Ball** exist in `skills.json` from that six-technique source section; **Pearl Flash** and **Super Vanishing Ball** are absent, so they were not fabricated.
- Coverage correction commit: `8fe4ef723a67e2d23358807deb55187e6a61854f`.
- Next priority: continue explicit Future Warrior restriction mining while separately tracking source-documented techniques missing from the structured skill dataset.


### 2026-09-19 cycle update — live PQ census reconciliation after stale handoff state
- Workstream: repository-wide PQ unlock-field validation / transition back to P1 skill research.
- Re-fetched all 18 canonical PQ research batches from the live repository and parsed every record directly from main.
- Validation result: 176 total records, 176 unique PQ numbers, 0 duplicates, 0 missing unlock_condition fields.
- The live repository is therefore ahead of the older handoff counts that still listed PQ36, PQ53–55, PQ131–140, or PQ151–160 as missing. Those historical counts remain in older cycle notes for provenance but are superseded by this live census.
- Confirmed that pq-batch-14.json covers PQ131–140, pq-batch-15.json covers PQ151–160, and the special early-PQ records PQ36/PQ53–55 now have explicit unlock metadata in their respective batches.
- Evidence limitations remain: an explicit field does not make every route exact. PQ54 has conflicting community reports; PQ36 retains the canonical numbering/existence anomaly; DLC-era records commonly use conservative DLC-ownership + PQ-board wording where an individual prerequisite was not independently established.
- CI status at inspection: the latest push-triggered Repository quality run for b9dc3ba1fcef62cac5c99e9ad419a0fbcec91994 completed with failure; the latest Clean internal artifacts run for the same commit was pending. Prior cycles and the current failure pattern do not expose actionable validation-step evidence, so validators are not to be weakened.
- No repository data validator was modified or bypassed during this reconciliation.
- Exact next task: P1 skill race-restriction census. Recompute the live skills.json cohort, prioritize explicit Future Warrior race/gender/form restrictions, and preserve null when accessible evidence does not establish a restriction.


### 2026-09-19 cycle update — live skill race-restriction census refresh
- Re-fetched the live `docs/data/skills.json` after the PQ unlock-field pass.
- Current canonical skill census: **283 records; 270 CaC-usable; 186 CaC-usable records still have `race_restriction` unset**. This supersedes older race-backlog counts in historical handoff sections.
- Confirmed that recent explicit restrictions already reconciled include Shining Slash (Earthling or Saiyan) and Saiyan Spirit (Saiyan); no new restriction was inferred from character ownership alone in this refresh.
- Accessible web evidence remains uneven: some wiki endpoints are robots-blocked, so only accessible sources are treated as independent evidence. Preserve null when the evidence does not explicitly establish a race/gender/form restriction.
- Exact next task: research an evidence-backed batch from the remaining 186 null-race records, prioritizing explicit Future Warrior race/gender/form wording, then re-run the live census and update coverage.


### 2026-09-19 cycle update — race-restriction evidence boundary recheck
- Rechecked the live 283-record skill census and the remaining CaC/race restriction backlog against the accessible Future Warrior technique reference.
- The reference explicitly documents race/gender/form restrictions for the already-reconciled cohort, including Saiyan Spirit (Saiyan), Explosive Buu Buu Punch (Majin), Zigzag Express (male Majin), Quick Sleep (Majin), Ill Bomber (Majin), Shining Slash/Burning Slash (Human or Saiyan), Candy Beam/Buu Buu Ball (Majin), Evil Flight Strike (Namekian or Majin), and Namek Finger (Namekian).
- Live canonical data already contains these restrictions, so this cycle made **no speculative race edits**. The remaining null-race records cannot be safely converted to `All CaC races` merely because the source does not state a restriction; the repository rule requires explicit evidence.
- Updated `docs/COVERAGE-AUDIT.md` to record this evidence boundary and prevent duplicate/redundant race edits.
- Coverage commit: `ccd2348846a0d72c909b52fa8de01615221f026d`.
- Current live skill census remains **283 total / 270 CaC-usable / 186 CaC-usable with null `race_restriction`**.
- Exact next task: continue the race-restriction census using source passages that explicitly identify additional Future Warrior race/gender/form limits; if a candidate is only associated with a character or category, leave it unresolved.


### 2026-09-19 cycle update — independent Future Warrior provenance hardening
- Recomputed the live skill census before editing: **283 total / 270 CaC-usable / 186 CaC-usable with null `race_restriction` / 0 null `usable_by_cac`**.
- Added the accessible independent Future Warrior reference to 13 already-reconciled restricted records: Saiyan Spirit, Explosive Buu Buu Punch, Zigzag Express, Ill Bomber, Candy Beam, Buu Buu Ball, Shining Slash, Burning Slash, Evil Flight Strike, Darkness Rush (Melee), Darkness Rush (Ranged), Majin Kamehameha, and Namek Finger.
- No race values were changed in this cycle. The source explicitly supports the existing restrictions, so this is provenance hardening rather than speculative classification.
- Skills commit: `5fe12abd56347b2d4e34974d5653a72a2cff308d`.
- Coverage commit: `a976239d0e48357a68b44b0603d26ac7a3913fc5`.
- Evidence source: accessible Future Warrior reference, which explicitly states race/gender restrictions for these techniques. 
- Exact next task: continue mining explicit race/gender/form restrictions among the remaining 186 null-race CaC records; if the accessible source only identifies a character association, leave the record unresolved.


### 2026-09-19 cycle update — Future Warrior provenance expansion
- Recomputed the live skill census: **283 total / 270 CaC-usable / 186 CaC-usable with null `race_restriction` / 0 null `usable_by_cac`**.
- Added the independent Future Warrior technique reference to seven existing CaC-usable records: **Demon Ray, Stone Bullet, Hero's Flute, Brave Sword Slash, Dimension Ray, God of Destruction's Roar, and Brave Sword Attack**.
- These are provenance improvements only. The accessible evidence identifies the moves as part of the Future Warrior's Xenoverse 2 technique set, but does not explicitly establish an unrestricted all-race scope for each one; their race restrictions therefore remain null rather than being inferred.
- Skills commit: `9f371e8ab6b63f23f6133db785bceb349f8ad474`.
- Coverage commit: `f5b4b180bc21eb1a49431252b90c10e450816c18`.
- Evidence: accessible Future Warrior technique reference plus individual technique pages for the clearest acquisition/user confirmations. 
- Exact next task: continue the 186-record race-restriction backlog, prioritizing explicit race/gender/form wording. Do not turn generic Future Warrior technique membership into `All CaC races` without an explicit universal-race statement.


### 2026-09-19 cycle update — Future Warrior provenance expansion batch 2
- Continued the race-restriction census after rechecking the live **283 / 270 / 186** skill census.
- Added the independent Future Warrior technique reference to 20 existing CaC-usable records: **Burst Rush, Change The Future, God Breaker, Psychic Move, Atomic Blast, Burning Attack, Crazy Finger Shot, Death Psycho Bomb, Emperor's Blast, Charge, Blazing Attack, Burst Blitz, Evil Whirlwind, Freedom Kick, Mach Punch, Recoome Kick, Sauzer Blade, Final Explosion, Heat Dome Attack, and Victory Rush**.
- These are provenance-only updates. The source explicitly identifies the techniques within the Future Warrior's Xenoverse 2 technique set, while also warning that some techniques are race/gender/transformation exclusive; therefore these records remain race-null unless a separate explicit restriction is established.
- Skills commit: `02bdd16007073f4e838e6242279f7b65c21571f9`.
- Coverage commit: `04768530cb211172ed514d3e619f76a43f23b9d2`.
- Evidence source: Future Warrior technique reference. 
- Exact next task: continue the remaining **186** null-race CaC records, separating explicit restriction evidence from mere Future Warrior usage/provenance and preserving null where race scope remains unproven.


### 2026-09-19 cycle update — Future Warrior provenance expansion batch 3
- Added independent Future Warrior provenance to 30 more existing CaC-usable skill records: Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, Heroic Counter, Punisher Shield, Reverse Mabakusenko, Rough Ranger, Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz, Absolute Zero, Dragon Burn, Force Shield, Instant Rise, Ki Explosion, Maiden Burst, Mighty Explosive Wave, Punisher Guard, Side Bridge, Spread Shot Retreat, Steel Mirage, Final Pose, and Mach Dash.
- Classification was intentionally unchanged: Future Warrior provenance is not treated as proof of unrestricted race access.
- Skills commit: `0c951f6f66367bf27dd7b485fdb742e0ad5c2ab4`.
- Coverage commit: `8212c04cb04b8b8abe3f6e3d753493443e1f65e2`.
- Current live census remains **283 total / 270 CaC-usable / 186 null race restrictions**.
- Exact next task: continue the 186-record null-race census, prioritizing explicit race/gender/form statements rather than character ownership.


### 2026-09-19 cycle update — Future Warrior provenance expansion batch 4
- Added Future Warrior provenance to 25 more existing CaC-usable skill records: Energy Barrier, Spirit Explosion, Spirit Slash, Blaster Ball, Bluff Kamehameha, Breaker Energy Wave, Burst Kamehameha, Burst Stinger, Dark Inscription, Destruction's Concerto: Comet, Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, Dust Attack, Earth Splitting Galick Gun, Emperor's Cannon, Eraser Bomb, Evil Blast, Evil Flame, Final Cannon, Flash Chaser, Gamma Blaster, Giant Cluster, Gigantic Charge, and God Punisher.
- No race restriction was inferred; explicit race evidence remains the required threshold.
- Skills commit: `df1165aba7a66954c492dd402dbce698d250a2b2`.
- Coverage commit: `f22e9932d63d18c6ee5a3013fbf3e4d0861c4934`.
- Exact next task: continue the null-race census and seek explicit race/gender/form restrictions before changing classifications.

### 2026-09-19 cycle update — Future Warrior provenance expansion batch 5
- Added Future Warrior provenance to 24 additional CaC-usable skill records: Handy Canon, Headshot, Heat Wave, Ill Rain, Paralysis, Paralyze Beam, Pendulum Bullet, Photon Swipe, Pretty Cannon, Raid Blast, Ray Blast, Reverse Shot, Rolling Bullet, Shine Shot, Spirit Blaster, Spirit Pulse, Super Donut Volley, Super Ghost Buu Attack, Variable Snipe Shot, Victory Cannon, Wild Buster, Dancing Parapara, Spirit Boost, and Time Control.
- No race restriction was inferred from provenance alone.
- Skills commit: `24322d250d88b5949e6e4d964c881fda4b076bd3`.
- Coverage commit: `9d7fe275f1fdba6e44c5f7fe3ecdf1edb4bd0aa3`.
- Exact next task: continue the null-race census with explicit race/gender/form evidence as the classification threshold.

### 2026-09-19 cycle update — Future Warrior cross-source provenance
- Added a second independent Future Warrior reference (The Codex) to 8 existing CaC-usable records: Mach Dash, Stone Bullet, Hero's Flute, Formation!, Brave Sword Slash, Dimension Ray, God of Destruction's Menace, and Brave Sword Attack.
- This corroborates provenance only; race restrictions were not inferred where the source merely lists the technique.
- Skills commit: `cb8e9944eb6136186f0149b2cac586291eb5a78f`.
- Coverage commit: `4dc14d75b8d53539e2c07c557b89366be9682274`.
- Research source: The Codex Future Warrior (Xenoverse 2), which explicitly documents several race/gender restrictions and distinguishes those from general technique listings. 
- Exact next task: continue the null-race census and prioritize records where the source provides explicit race/gender/form wording.

### 2026-09-19 cycle update — explicit form-restriction audit
- Rechecked the Future Warrior reference for its explicit **Great Namekian**, **Pure Majin**, **Golden Frieza Race**, and **Ultra Instinct** form-exclusive technique sections. The source explicitly establishes restrictions such as Great Namekian-only Demon Hand/Mouth Cannon variants, Pure Majin-only Body Manipulation/Mystic Attack/Mystic Shot/Mystic Ball Attack/Pearl Flash/Super Vanishing Ball, Golden-form Death Bullet/Death Beam, and Ultra Instinct Dodge.
- None of those exact technique names currently exists as a canonical record in `docs/data/skills.json`, so no new classification was fabricated and the live 186-record null-race cohort is unchanged.
- The audit also confirmed the source's general warning that some Future Warrior techniques are exclusive by race, gender, and/or transformation.
- Exact next task: continue matching explicit restriction evidence against the actual canonical skill inventory, then classify only records that exist and remain unresolved.

### 2026-09-19 cycle update — explicit-restriction cross-check
- Rechecked the source's explicit Future Warrior race/gender restriction set against live `skills.json`.
- Result: **0** explicit restricted skills remain unclassified among CaC-usable records. The reconciled set includes Saiyan Spirit, Explosive Buu Buu Punch, Zigzag Express, Quick Sleep, Ill Bomber, Shining Slash, Burning Slash, Candy Beam, Buu Buu Ball, Evil Flight Strike, Namek Finger, Darkness Rush (Ranged), Darkness Rush (Melee), and Majin Kamehameha.
- No data change was warranted this pass; the remaining 186 null-race records need new evidence rather than inference.
- Coverage commit: `546a9531560caa7213ee226349c032096d89cabe`.
- Exact next task: expand research beyond the current Future Warrior technique list and seek independent explicit race/gender/form statements for unresolved canonical skills.

### 2026-09-19 cycle update — Death Psycho Bomb explicit unrestricted evidence
- Classified **Death Psycho Bomb** as `All CaC races`.
- Evidence: the dedicated technique source explicitly states that in Xenoverse 2 the Future Warrior obtains it from PQ33 and can use it **regardless of race**. 
- This was a canonical null-race record, so the live unresolved cohort decreases by one.
- Skills commit: `d510d9aadf33fda593ed2cef2695af1d58aa16f2`.
- Coverage commit: `d79eeed38912d6f37269233554aa24a3a29cd9e1`.
- Exact next task: continue searching independent technique pages for equally explicit race/unrestricted statements among the remaining null-race records.

### 2026-09-19 cycle update — Justice Pose explicit unrestricted evidence
- Classified **Justice Pose** as `All CaC races`.
- Evidence explicitly states the Xenoverse 2 Super Skill can be used by the Future Warrior regardless of race or gender; the separate emote has different restrictions and must not be conflated with the skill.
- Skills commit: `d3db810e63893318f8cf40b38b2fa9601301a730`.
- Coverage commit: `7206a4cf543304579c6893dfa4b4d6597a92ece3`.
- Exact next task: continue independent skill-page research for explicit unrestricted/race/gender/form statements.

### 2026-09-19 cycle update — dedicated technique provenance pass
- Added dedicated technique-page sources to `Mach Dash`, `Energy Barrier`, `Blaster Ball`, `Crazy Finger Shot`, `Evil Flame`, and `Final Cannon`.
- No race classification was changed where the newly checked evidence only established Future Warrior acquisition/usage rather than an explicit race restriction or unrestricted statement.
- Skills commit: `893b7cac3b045873ab6b0f2c629e89bf2a3b6723`.
- Coverage commit: `cd597e9c3d40629360d91cd5eaa8d723a2529eb1`.
- Continue the null-race cohort with exact-name dedicated-page searches; do not infer universal access from mere Future Warrior ownership.

### 2026-09-19 cycle update — Crazy Finger Shot explicit unrestricted evidence
- Classified **Crazy Finger Shot** as `All CaC races` based on a dedicated technique source explicitly stating that the Future Warrior can use its Death Bullets regardless of race.
- The Frieza-race restriction applies to Death Bullets as a basic uncharged Ki Blast under Turn Golden, not to the Death Bullets embedded in Crazy Finger Shot.
- Skills commit: `b1d5d848e781814ddb531371ee382b48bc2fcb1b`.
- Coverage commit: `6dfc0cfbc4d748ccb53601c1cd5bcc9d570878f8`.
- Continue exact-name dedicated-page research for the remaining null-race cohort.

### 2026-09-19 cycle update — Raid Blast dedicated provenance
- Added dedicated `Niagara Pummel` provenance to `Raid Blast`.
- No race classification was inferred because the source confirms Future Warrior acquisition but does not state race availability.
- Skills commit: `26f671904498064085a7361881fb6161a0b3e442`.
- Coverage commit: `f656c0dada47a8f9a9bb5ea3e59a5c0d77f2fd09`.
- Continue exact-name research of the remaining null-race cohort.

### 2026-09-19 cycle update — Counter Burst dedicated provenance
- Added dedicated `Counter Burst` provenance confirming the Xenoverse 2 skill and Future Warrior PQ75 acquisition route.
- No race classification was inferred because the source does not explicitly establish one.
- Skills commit: `4100878419655f176a6d3125242355b20b257bdf`.
- Coverage commit: `5ab2663a7cad21144e537e93b1a84255f8110bb3`.
- Continue the null-race explicit-evidence sweep.

### 2026-09-19 cycle update — Super Spirit Bomb corroboration and missing-record audit
- Added The Codex Future Warrior source to `Super Spirit Bomb`; it independently corroborates unrestricted race access already recorded as `All CaC races`. 
- Confirmed `Brave Heat`, `Power Pole`, and `Power Pole Combo` are referenced by external Future Warrior material but do not exist as canonical records in the current `skills.json`; do not fabricate records during the race census.
- Skills commit: `2533919cfe27a9ecd1ea663e47d85a4d4293bf89`.
- Coverage commit: `45c92022cec71b8b08b1673ec04941d2e4725ff2`.
- Continue the explicit-evidence sweep of the remaining null-race canonical records.

### 2026-09-19 cycle update — null-race batch: counter/time-skip skills
- Reviewed 12 null-race records: `Rough Ranger`, `Shadow Crusher`, `Sudden Death Beam`, `Super Afterimage`, `Super God Shock Flash`, `Time Skip/Back Breaker`, `Time Skip/Flash Skewer`, `Time Skip/Jump Spike`, `Ultrasonic Blitz`, `Absolute Zero`, `Dragon Burn`, and `Explosive Wave`.
- No race/gender/unrestricted classification was added because the checked evidence did not explicitly establish one.
- Coverage commit: `db71cad10db630b2f945a67c1f254ea0b075421e`.
- Continue with the next null-race cohort.

### 2026-09-19 cycle update — defensive/evasive null-race batch
- Reviewed 12 records: `Force Shield`, `Instant Rise`, `Ki Explosion`, `Maiden Burst`, `Mighty Explosive Wave`, `Psychic Move`, `Punisher Guard`, `Side Bridge`, `Spread Shot Retreat`, `Steel Mirage`, `Final Pose`, and `Mach Dash`.
- A secondary Future Warrior profile places Force Shield and related abilities under an “All Races” grouping, but the evidence is not skill-specific enough to convert the canonical null race fields. No classifications were changed.
- Coverage commit: `b1653219a5060ed0ac7152a817a34536d0ba0e06`.
- Continue with the next unresolved null-race cohort.

### 2026-09-19 cycle update — next null-race skill batch
- Reviewed 12 records: `Energy Barrier`, `Spirit Explosion`, `Spirit Slash`, `Atomic Blast`, `Blaster Ball`, `Bluff Kamehameha`, `Breaker Energy Wave`, `Burning Attack`, `Burst Kamehameha`, `Burst Stinger`, `Dark Inscription`, and `Demon Ray`.
- Direct/reference sources establish Future Warrior use, but no sufficiently explicit per-skill race/gender restriction or unrestricted-race statement was found. No classifications were changed.
- Coverage commit: `081e248c8db6df7ef44ada4be368db5aea10a032`.
- Continue with the next unresolved null-race cohort.

### 2026-09-19 cycle update — DLC/character-derived null-race cohort
- Reviewed 12 records: `Destruction's Concerto: Comet`, `Destruction's Concerto: Starfall`, `Dimension Cannon`, `Double Death Slicer`, `Dust Attack`, `Earth Splitting Galick Gun`, `Emperor's Blast`, `Emperor's Cannon`, `Eraser Bomb`, `Evil Blast`, `Evil Flame`, and `Final Cannon`.
- Evidence confirms Future Warrior acquisition/use where documented, but no sufficiently explicit individual race/gender restriction was established. Index omission is not treated as universal access. No classifications changed.
- Coverage commit: `c6a32d79cb1d04e6ca21561a68d241bb63c295fd`.
- Continue with the next unresolved null-race cohort.

### 2026-09-19 cycle update — later DLC/mentor null-race cohort
- Reviewed 12 records: `Flash Chaser`, `Gamma Blaster`, `Giant Cluster`, `Gigantic Charge`, `God of Destruction's Plaything`, `God Punisher`, `Handy Canon`, `Headshot`, `Heat Wave`, `Ill Rain`, `Paralysis`, and `Paralyze Beam`.
- Added direct technique provenance to `Flash Chaser`, `Gamma Blaster`, `God Punisher`, and `Headshot`.
- These sources establish Future Warrior acquisition/use but do not establish a new race restriction, so no `race_restriction` values changed.
- Skills commit: `222be3bacf6432f577f6936da4eef66e116db430`.
- Coverage commit: `df206ce6b5941e9770a028e4ae4704f965987dfe`.
- Continue with the next unresolved null-race cohort.

### 2026-09-19 cycle update — late offensive/evasion null-race cohort
- Reviewed 12 records: `Pendulum Bullet`, `Photon Swipe`, `Pretty Cannon`, `Raid Blast`, `Ray Blast`, `Reverse Shot`, `Rolling Bullet`, `Shine Shot`, `Spirit Blaster`, `Spirit Pulse`, `Stone Bullet`, and `Super Donut Volley`.
- Added direct technique provenance to `Photon Swipe`; it confirms Future Warrior acquisition from New Parallel Quest 139 but does not establish a race restriction.
- No `race_restriction` values changed.
- Skills commit: `6e740b7a1c7be6608af7f3220e43dc8b998b7b38`.
- Coverage commit: `76c2cfa76cc1e3f89a5f231adc5e8d6a2a909cf9`.
- Continue with the next unresolved null-race cohort.

### 2026-09-19 cycle update — null-race evidence boundary
- Live skill census: 283 total / 270 CaC-usable / 183 CaC-usable with null `race_restriction`.
- Reviewed the next 12 unresolved records: Super Ghost Buu Attack, Variable Snipe Shot, Victory Cannon, Wild Buster, Dancing Parapara, Hero's Flute, Spirit Boost, Time Control, Charge, Divinity Unleashed, Do or Die, and Fighting Pose E.
- Current Xenoverse 2 evidence did not establish a sufficiently explicit individual race/gender/form restriction for this cohort. Legacy Xenoverse all-race labels were not promoted across versions.
- No canonical race classifications changed. Coverage commit: 4a142e80e3fe46a6fc64c8049dea52fd1cba5106.
- CI remains opaque: current-head Repository quality and cleanup runs failed with no recorded job steps; validators were not weakened.
- Exact next task: continue the next unresolved null-race cohort with current-version explicit evidence only.


### 2026-09-19 cycle update — counter-skill provenance batch
- Reviewed the next 12 unresolved null-race records: Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, God Breaker, Heroic Counter, Punisher Shield, Reverse Mabakusenko, and Rough Ranger.
- Added direct Xenoverse 2 technique-page provenance to Counter Impact, Flash Fist Crush, God Breaker, Heroic Counter, Punisher Shield, and Rough Ranger.
- The checked dedicated pages establish skill identity, acquisition/user information, or mechanics but do not explicitly establish CaC race/gender/form scope. No race_restriction values were changed.
- Character ownership and generic Counter Skills categorization were not treated as race evidence.
- Canonical skill count remains 283 and the unresolved CaC null-race count remains 183.
- Exact next task: continue with the following unresolved cohort beginning at Shadow Crusher, preserving nulls unless current-version evidence explicitly establishes restriction or unrestricted access.


### 2026-09-19 cycle update — counter/time-skip provenance batch
- Reviewed Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, and Ultrasonic Blitz.
- Added direct Xenoverse 2 technique-page provenance for all eight records.
- Current evidence documents identity/unlock/user/mechanics but does not explicitly establish CaC race/gender/form scope; no race_restriction values were changed.
- Character ownership, mentor status, and category membership remain insufficient evidence for race classification.
- Canonical skill count remains 283 and unresolved CaC null-race count remains 183.
- Exact next task: continue the next unresolved null-race cohort after Ultrasonic Blitz, beginning with the current live ordering, and classify only from explicit current-version evidence.


### 2026-09-19 cycle update — evasive-skill provenance boundary
- Reviewed Absolute Zero, Dragon Burn, Explosive Wave, and Force Shield.
- Added the missing direct Xenoverse 2 provenance URL for Explosive Wave; the other three already had direct provenance.
- Current evidence does not explicitly establish CaC race/gender/form scope, so no race classifications were changed.
- Do not convert generic Evasive Skill/CaC availability listings into race-specific classifications without explicit evidence.
- Canonical skill count remains 283 and unresolved CaC null-race count remains 183.
- Exact next task: continue the next unresolved null-race cohort beginning with Instant Rise, then Ki Explosion, Maiden Burst, and subsequent live-order records.


### 2026-09-19 cycle update — explicit CaC scope found
- Reviewed Instant Rise, Ki Explosion, Maiden Burst, Mighty Explosive Wave, Psychic Move, Punisher Guard, Side Bridge, and Spread Shot Retreat.
- Classified **Ki Explosion** as `All CaC races` because its current Xenoverse 2 page explicitly says it is available for all CaCs.
- The other seven reviewed records remain unresolved where the evidence does not explicitly establish all-race or race-specific CaC scope.
- Canonical skill count remains 283; CaC-usable count remains 270; unresolved null-race count decreases from 183 to 182.
- Exact next task: continue from the live unresolved ordering after this batch, beginning with Steel Mirage and subsequent records, using explicit current-version race/gender/form evidence only.


### 2026-09-19 cycle update — evasive/early-super provenance batch
- Reviewed Steel Mirage, Final Pose, Mach Dash, Energy Barrier, Spirit Explosion, Spirit Slash, Atomic Blast, and Blaster Ball.
- Added direct Xenoverse 2 provenance for Blaster Ball; the other seven already had dedicated current-version provenance.
- No race classifications changed because explicit CaC race/gender/form scope was not established.
- Canonical count remains 283; CaC-usable count remains 270; unresolved null-race count remains 182.
- Exact next task: continue the next live unresolved cohort beginning with Bluff Kamehameha, Breaker Energy Wave, Burning Attack, and Burst Kamehameha.


### 2026-09-19 cycle update — early super provenance boundary
- Reviewed Bluff Kamehameha, Breaker Energy Wave, Burning Attack, and Burst Kamehameha.
- Current-version evidence confirms acquisition/CaC access for some of these skills but does not explicitly establish race/gender/form scope.
- Preserved null `race_restriction` values and deliberately did not import Xenoverse 1 race labels into Xenoverse 2.
- No canonical data changes were required; coverage and handoff were updated to record the evidence boundary.
- Canonical count remains 283; CaC-usable count remains 270; unresolved null-race count remains 182.
- Exact next task: continue the live unresolved ordering beginning with Burst Stinger, Dark Inscription, Demon Ray, and Destruction's Concerto: Comet.


### 2026-09-19 cycle update — super-skill evidence boundary
- Reviewed Burst Stinger, Dark Inscription, Demon Ray, and Destruction's Concerto: Comet.
- Preserved null race restrictions because current evidence establishes named-character usage/acquisition but not explicit CaC race/gender/form scope.
- Added dedicated current-version Burst Stinger provenance URL and refreshed its verification date.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort begins with Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, and Dust Attack.


### 2026-09-19 cycle update — next super-skill verification boundary
- Reviewed Destruction's Concerto: Starfall, Dimension Cannon, Double Death Slicer, and Dust Attack.
- Preserved null race restrictions; NPC user identity/acquisition does not establish CaC race/gender/form scope.
- Refreshed all four `last_verified` dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort begins after Dust Attack; inspect the canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Earth/Emperor cohort verification boundary
- Reviewed Earth Splitting Galick Gun, Emperor's Blast, Emperor's Cannon, and Eraser Bomb against current Xenoverse 2 evidence.
- Preserved null race restrictions because current evidence does not explicitly establish CaC race/gender/form scope.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Eraser Bomb; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Evil/Flash provenance boundary
- Reviewed Evil Blast, Evil Flame, Final Cannon, and Flash Chaser.
- Preserved null race restrictions; acquisition and custom-partner availability do not establish race/gender/form scope.
- Added dedicated current-version provenance URLs for Evil Blast, Evil Flame, and Flash Chaser.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Flash Chaser; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Gamma/Gigantic provenance boundary
- Reviewed Gamma Blaster, Giant Cluster, Gigantic Charge, and God of Destruction's Plaything.
- Preserved null race restrictions because the reviewed current evidence does not explicitly establish CaC race/gender/form scope.
- Added dedicated current-version provenance URLs for Giant Cluster and Gigantic Charge.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows God of Destruction's Plaything; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — God/Headshot provenance boundary
- Reviewed God Punisher, Handy Canon, Headshot, and Heat Wave.
- Preserved null race restrictions because current evidence does not explicitly establish CaC race/gender/form scope.
- Added dedicated current-version provenance URLs for God Punisher and Handy Canon.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Heat Wave; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — status/paralysis provenance boundary
- Reviewed Ill Rain, Paralysis, Paralyze Beam, and Pendulum Bullet.
- Preserved null race restrictions because the reviewed evidence does not explicitly establish CaC race/gender/form scope.
- Added or normalized dedicated current-version provenance URLs for all four.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Pendulum Bullet; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Photon/Raid provenance boundary
- Reviewed Photon Swipe, Pretty Cannon, Raid Blast, and Ray Blast.
- Preserved null race restrictions because the reviewed evidence does not explicitly establish CaC race/gender/form scope.
- Added dedicated current-version provenance URLs for all four.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Ray Blast; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Reverse/Spirit provenance boundary
- Reviewed Reverse Shot, Rolling Bullet, Shine Shot, and Spirit Blaster.
- Preserved null race restrictions; no explicit current race/gender/form scope was established.
- Added dedicated current-version provenance URLs for Reverse Shot and Spirit Blaster.
- Refreshed all four verification dates to 2026-09-19.
- Fresh dbxv2 Fandom search was blocked by robots.txt; no unsupported inference was made.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Spirit Blaster; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Spirit/Buu provenance boundary
- Reviewed Spirit Pulse, Stone Bullet, Super Donut Volley, and Super Ghost Buu Attack.
- Preserved null race restrictions because current evidence does not explicitly establish CaC race/gender/form scope.
- Added dedicated current-version provenance URLs for Stone Bullet and Super Ghost Buu Attack.
- Refreshed all four verification dates to 2026-09-19.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Super Ghost Buu Attack; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Fighting Pose/Burst boundary
- Reviewed Fighting Pose H, Formation!, Indomitable, Taunt, Blazing Attack, Brave Sword Slash, Burning Swan, and Burst Blitz.
- Preserved null race restrictions; no explicit current race/gender/form scope was established.
- Refreshed all eight verification dates to 2026-09-19.
- Current web search for dedicated dbxv2 Fandom pages was blocked by robots.txt, so no unsupported provenance URL was added.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Burst Blitz; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Death/Demon/Destruction boundary
- Reviewed Death Slash, Demon Flurry, Demonic Destruction, and Destruction's Conductor.
- Preserved null race restrictions; current evidence did not establish explicit race/gender/form scope.
- Refreshed all four verification dates to 2026-09-19.
- Current sources confirm skill identity/availability, but availability or character association was not treated as race-scope evidence.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Destruction's Conductor; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Dragon/Emperor/Gamma boundary
- Reviewed Dragon Spark, Dragon Spiral, Emperor's Edge, Evil Whirlwind, Fierce Fist, Force Edge, Freedom Kick, and Gamma Impact.
- Preserved null race restrictions; no explicit current race/gender/form scope was established.
- Refreshed all eight verification dates to 2026-09-19.
- Added dedicated current-version provenance for Dragon Spiral.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Gamma Impact; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Gamma/Justice boundary
- Reviewed God of Destruction's Poise, Heroic Assault, Justice Blade, and Justice Drive.
- Preserved null race restrictions; no explicit current race/gender/form scope was established.
- Refreshed all four verification dates to 2026-09-19.
- Gamma Impact was additionally checked against its current skill page: its Future Warrior acquisition does not by itself establish unrestricted race scope, so its null classification remains unchanged.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Justice Drive; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Justice/Power boundary
- Reviewed Justice Kick, Lovely Cyclone, Mach Punch, Meteor Blow, Meteor Strike, Neo Wolf Fang Fist, Power Impact, and Powered Shell.
- Preserved null race restrictions; no explicit current race/gender/form scope was established.
- Refreshed all eight verification dates to 2026-09-19.
- Added dedicated current-version provenance for Lovely Cyclone, Power Impact, and Powered Shell.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Powered Shell; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Recoome/Sonic boundary
- Reviewed Recoome Kick, Sauzer Blade, Savory Slicer, Scissors Paper Rock, Seagull Combination, Shooting Strike, Soaring Rush, and Sonic Bomb.
- Preserved null race restrictions; no explicit current race/gender/form scope was established.
- Refreshed all eight verification dates to 2026-09-19.
- Added dedicated current-version provenance for Savory Slicer.
- Canonical totals remain 283 skills, 270 CaC-usable, 182 unresolved null-race records.
- Next live unresolved cohort follows Sonic Bomb; inspect canonical ordering before selecting the next batch.


### 2026-09-19 cycle update — Super God Fist through Circle Flash
- Workstream: P1 skill race-restriction census / current-version provenance boundary.
- Recomputed the live canonical census before editing: **283 total skills / 270 CaC-usable / 182 CaC-usable records with null `race_restriction`**.
- Reviewed the next eight unresolved null-race records after Sonic Bomb: **Super God Fist, Variant Drive, Apocalyptic Burst, Blaster Stream, Burning Blast, Chain Destructo-Disc Barrage, Chaotic Time Impact, and Circle Flash**.
- Current dedicated Xenoverse 2 evidence confirms skill identity, users, acquisition routes, and mechanics, but does not explicitly establish CaC race/gender/form scope for these records. No race restriction was inferred from character ownership, PQ availability, partner customization, or category membership.
- Added/normalized dedicated current-version provenance URLs and refreshed `last_verified` to 2026-09-19 for all eight. No `race_restriction` values changed.
- Files changed: `docs/data/skills.json`, `docs/COVERAGE-AUDIT.md`, and this handoff.
- Commits: `a9b7122a95621a4a1ef9b036f1459c644940a836` (skill research), `89503f686768e11e7104d6cc204ad21834d26086` (coverage audit), `50aae8fe8160c6db942e7d67bccfab14dacef46` and `dd5401473ddb7378181b52a4dfe5cce1d3bcdda0` (audit citation-artifact cleanup).
- Validation: `skills.json` fetched and parsed successfully; live census remains 283/270/182. Audit file was re-fetched and checked for ChatGPT/internal citation artifacts; none remain after cleanup. No validators were changed.
- CI status: combined status for the latest audit-cleanup commit returned no statuses, and the commit-specific workflow-run query returned no runs. This provides no actionable CI result; do not interpret the absence as a passing validator result.
- Exact next task: **Core Breaker, Destruction's Concerto: Meteor, Dimension Ray, Energy Field, Final Flash (SS3 DAIMA), Final Kamehameha, Full Power Destruction, and Gigantic Breaker**. Recompute the live census first, then research explicit current-version race/gender/form evidence only and preserve nulls where the evidence boundary remains.


### 2026-09-19 continuation — classification reconciliation completed
- Re-researched the queued cohort with current web evidence before editing.
- Corrected four canonical skill records where earlier field values conflicted with dedicated Xenoverse 2 evidence: **Core Breaker** → Strike Ultimate / 500 Ki; **Destruction's Concerto: Meteor** → Super / Ki Blast / 100–200 Ki; **Energy Field** → Evasive / Ki Blast / 200 Stamina; **Gigantic Breaker** → Super / Ki Blast / 200 Ki.
- Current evidence explicitly supports Future Warrior acquisition/use for Core Breaker, Destruction's Concerto: Meteor, and Gigantic Breaker; Energy Field's dedicated page identifies its Evasive classification and character users. No unsupported CaC race restriction was inferred.
- Cleaned provenance URLs after the first reconciliation edit and re-fetched the JSON.
- Commits: `33fdaaf6acdfb46819eb9fe49d188ff9fecca9b4` (reconciliation), `80a320fe9875ff821c2e154eaaddf0e31d9e420b` (URL normalization), `655d55fe8e807185e3075b1491054266900c6a8c` (coverage audit).
- Next exact research target: **Final Flash (SS3 DAIMA), Final Kamehameha, Full Power Destruction**, followed by the next unresolved null-race records. Do not infer CaC race scope from a character's preset or from generic Future Warrior technique lists unless the source explicitly establishes that the skill is learnable by the Future Warrior.


### 2026-09-19 continuation — final Ultimate Ki Blast scope review
- Reviewed **Final Flash (SS3 DAIMA), Final Kamehameha, and Full Power Destruction** against their dedicated current-version Xenoverse 2 pages.
- Confirmed their current classifications/acquisition/user data and documented the evidence boundary in `docs/data/skills.json`.
- No `race_restriction` values were inferred or changed: the reviewed pages do not explicitly establish CaC race/gender/form scope. Character presets, partner customization, and generic technique indexing are not being treated as sufficient proof of CaC race scope.
- Updated `docs/COVERAGE-AUDIT.md` with the three-record evidence review.
- Commits: `798535bedb3a986a93b2fa09f6aa396b7d89ddb4` (canonical data), `ce19dc8a2589396cffdfdca81a7a6335e87ec221` (coverage audit).
- Next exact target: continue from the next unresolved null-race record after Gigantic Breaker, using the same explicit-scope standard; recompute the live census before editing.


### 2026-09-19 continuation — queued skill reconciliation
- Reconciled **Gigantic Burst, God of Destruction's Roar, God of Destruction's Menace, and Gigantic Roar** against current evidence.
- **God of Destruction's Roar** was materially corrected from Ultimate/Ki Blast/300 Ki to **Super/Strike/100 Ki**.
- Gigantic Burst has explicit current evidence that it is available for CaCs; no race restriction was inferred.
- Gigantic Roar's current page confirms its Ultimate/Ki Blast/PQ132 identity, but does not establish a CaC race/gender/form restriction.
- God of Destruction's Menace is confirmed as a 300-Ki Ki Blast Ultimate from PQ105; existing CaC scope remains conservatively retained pending stronger dedicated explicit-scope evidence.
- Remaining immediate cohort: **Gigantic Explosion, Heat Dome Attack, Holy Wrath, Last Emperor**.
- Commits: `cd04519a91003c8707a13c14876dba541aee805e` (data), `bc148b615ca618eb4011296efb1b7c435813b966` (audit).


### 2026-09-19 continuation — Heat Dome / Zamasu / Last Emperor
- Reconciled **Heat Dome Attack, Holy Wrath, Last Emperor, and Lightning of Absolution** against dedicated current-version skill pages.
- Corrected **Holy Wrath** from Ultimate/300 Ki to **Super/100 Ki**.
- Corrected **Last Emperor** from 300 Ki to **0 Ki** and documented its low-health/one-use condition.
- Confirmed **Lightning of Absolution** as a 100-Ki Ki Blast Super and **Heat Dome Attack** as a 300-Ki Ki Blast Ultimate.
- No unsupported CaC race/gender/form restrictions were inferred from character users.
- Commits: `ff28f527b5813cb8a2644c0e83aa0e1791b530c5` (data), `453120ea547b2e041cc7d2c21ed24e5550141082` (audit).
- Next queued cohort begins with **Mystic Flash** and **Requiem of Destruction**, followed by the remaining unresolved null-race records.


### 2026-09-19 continuation — counter-skill cohort
- Refreshed evidence notes for **Burst Rush, Change The Future, Counter Burst, Counter Impact, Demon Flash Strike, Dimensional Hole, Flash Fist Crush, and God Breaker**.
- Confirmed the current counter classifications and recorded resource/acquisition fields; no unsupported CaC race/gender/form restrictions were inferred.
- Commits: `26d27c9d50be0d0ba1f8fa9a3aacec6fae0a3b36` (data), `2d3a9f52debad3f00a684c1ac4669cb3b3decc32` (audit).
- Next continuation should advance beyond this counter cohort and select the next unresolved CaC-usable/null-race records from the canonical dataset.


### 2026-09-19 continuation — remaining counter skills
- Reconciled **Heroic Counter, Punisher Shield, Reverse Mabakusenko, and Rough Ranger** against current dedicated skill pages.
- Confirmed current classes, attack types, resource costs, counter roles, and acquisition sources.
- No CaC race/gender/form restriction was inferred from character users or partner customization.
- Commits: `61a89b5e248ae96b6a5461530421665ea17097b3` (data), `9addfd0dd216a3d192c215b4dc8ebd1d543d60e2` (audit).
- Continue with the next unresolved CaC-usable/null-race records after this counter cohort.


### 2026-09-19 continuation — Mystic Flash / Requiem
- Reconciled **Mystic Flash** and **Requiem of Destruction** against their dedicated current-version pages.
- Both confirmed as 300-Ki Ki Blast Ultimates; Mystic Flash is from PQ20 and Requiem of Destruction is from PQ106.
- Neither page explicitly establishes CaC race/gender/form scope; no restriction was inferred.
- Commits: `6c7debe720c03b4332954a56eb5508949a4d9bae` (data), `59dad11176065a4a57899801f3239983daa1276b` (audit).
- Continue with the next unresolved CaC-usable/null-race records in dataset order.


### 2026-09-19 continuation — Counter cohort
- Reconciled dataset-order records: Shadow Crusher, Sudden Death Beam, Super Afterimage, Super God Shock Flash, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Ultrasonic Blitz.
- Dedicated current-version evidence was added to the mechanics/research notes. No unsupported CaC race/gender/form restrictions were inferred.
- Sudden Death Beam's existing acquisition data was retained because its dedicated page could not be freshly retrieved in this pass.
- Data commit: `4cdc73fd86aa0a2d0945aaf3ccb4413c014590e5`; audit commit: `567e1698100dfde569aa9518751e13677ea48416`.
- Next continuation should proceed from the next dataset-order unresolved records after Ultrasonic Blitz.


### 2026-09-19 continuation — Evasive cohort
- Reconciled: Absolute Zero, Celestial Wave, Dragon Burn, Explosive Wave, Force Shield, Instant Rise, Ki Explosion, Maiden Burst.
- Current evidence confirms Evasive classifications, stamina costs and acquisition routes where documented. Force Shield was corrected to Ki Blast. Existing explicit all-CaC-races coverage for Ki Explosion was retained.
- Data commit: `8830647798b1b93b499b8d1269d3fecf3386f684`; audit commit: `08d8bcee08b92ef2f05b9b16f0cfdb396faaf448`.
- Next continuation should proceed from the next dataset-order unresolved records after Maiden Burst.
