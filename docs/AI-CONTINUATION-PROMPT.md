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
