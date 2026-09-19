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
- PQ71–80: exact unlock routes researched and recorded; sequential PQ dependencies and story/NPC gates were preserved where supported.
- PQ161–186: later-batch reward/unlock semantics enriched; exact unknown percentages remain unresolved rather than fabricated.
- PQ184 Chaotic Time Impact: documented as a 50% Ultimate Finish bonus-slot drop.

**Next exact PQ task: PQ81–90.**
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
2. Research **PQ61–70** individually.
3. Prioritize NPC, story, and prerequisite-PQ evidence.
4. Do not manufacture sequential prerequisites.
5. Update the relevant batch.
6. Update `docs/COVERAGE-AUDIT.md`.
7. Update this file with the new state.
8. Commit the complete cycle.

### Latest known PQ unlock census
Latest audit reference after PQ71–80: **72 records without an explicit unlock condition**. Recompute from the live 18 PQ batch files before making decisions.

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

### 2026-09-19 cycle update — PQ71–80
- Workstream: Parallel Quest unlock-route research.
- Changed: `pq-batch-08.json`, `docs/COVERAGE-AUDIT.md`, and this handoff file.
- Research: verified PQ71–80 against independent PQ references, including explicit prerequisite chains and story/NPC gates.
- Evidence limitations: none of the ten entries required an invented prerequisite; exact wording is normalized from source evidence.
- Commits: `5a68cbf35b6aae022ae71acaff1faec07d45c775` (PQ71–80), `cec93e91d5e72a2952a95499b1a28320c612d19d` (coverage), plus this handoff update.
- Current unlock-gap reference: 72; recompute live before next decisions.
- Next exact task: PQ81–90.

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
