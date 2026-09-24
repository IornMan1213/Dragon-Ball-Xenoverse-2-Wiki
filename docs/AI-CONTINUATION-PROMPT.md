### 2026-09-24 cycle completion — Great Ape Boulder skill-gap evidence enrichment
- [x] Added unresolved research records for `Boulder Toss` and `Boulder Break` to `docs/data/skill-research-gaps.json`.
- [x] Added dedicated evidence audits for both skills.
- [x] Confirmed Xenoverse 2 skill IDs **441 (Boulder Toss)** and **442 (Boulder Break)**, both CaC-unavailable Great Ape skills.
- [x] Confirmed both are **Super Skills**; retained `subcategory` and `ki_cost` as unresolved because generic projectile/physical terminology does not establish the repository taxonomy or numeric cost.
- [x] Preserved the canonical boundary; no unsupported promotion or acquisition route was invented.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining Great Ape/legacy unresolved candidate set, beginning with `Boiling Ball` and then `Tricky Strike`, using direct Xenoverse 2 evidence.

### 2026-09-24 cycle completion — Baked Sphere skill-gap evidence enrichment
- [x] Strengthened the unresolved `Baked Sphere` record with Xenoverse 2-specific Ultimate classification, CaC-unavailable boundary, Supervillain/Masked Future Warrior usage, and Crystal Raid context.
- [x] Added `docs/data/skill-research-gaps-baked-sphere-evidence-audit-2026-09-24.json` with explicit evidence and guardrails.
- [x] Preserved the unresolved boundary at `ki_cost`; no unsupported numeric cost or acquisition route was invented.
- [x] Validated the updated gap ledger on the live `main` branch.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next unresolved thin-domain skill after Baked Sphere, using Xenoverse 2-specific evidence before any canonical promotion.

### 2026-09-24 cycle completion — Boiling Burg skill-gap evidence enrichment
- [x] Strengthened the unresolved `Boiling Burg` record with Xenoverse 2-specific skill ID 540, CaC-unavailable status, Final Form Demigra ownership, Legend Patrol presence, and independent CaC-unobtainable catalog evidence.
- [x] Added `docs/data/skill-research-gaps-boiling-burg-evidence-audit-2026-09-24.json`.
- [x] Resolved the classification boundary to **Ultimate** while leaving only `ki_cost` unresolved.
- [x] Preserved the canonical skill boundary; no unsupported promotion or numeric cost inference was made.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next unresolved skill gap after Boiling Burg, prioritizing the remaining cast-only/legacy skill records with the strongest available Xenoverse 2 evidence.

### 2026-09-24 cycle completion — Acid skill-gap evidence enrichment
- [x] Strengthened the unresolved `Acid` research record with Xenoverse 2-specific evidence for its cast-only/CaC-unavailable boundary and Saibaman 2 Crystal Raid/Training presence.
- [x] Added `docs/data/skill-research-gaps-acid-evidence-audit-2026-09-24.json` with explicit evidence and guardrails.
- [x] Reduced unresolved Acid fields to `ki_cost` and `unlock_method`; no unsupported numeric or acquisition data was invented.
- [x] Preserved the canonical skill boundary; no unsupported promotion was attempted.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue `Boiling Burg` with direct Xenoverse 2 evidence, then proceed to the next thin-domain task.

### 2026-09-24 cycle completion — Energy Boil skill-gap evidence enrichment
- [x] Strengthened the unresolved `Energy Boil` research record with Xenoverse 2-specific identity evidence: skill ID 10540, CaC-unavailable status, and Final Form Demigra ownership.
- [x] Added direct Xenoverse 2 restoration/mod evidence describing Energy Boil as an evasive, plus independent reference corroboration of the Evasive classification and behavior.
- [x] Added `docs/data/skill-research-gaps-energy-boil-evidence-audit-2026-09-24.json` with explicit evidence boundaries.
- [x] Reduced the unresolved field set to canonical `subcategory` and `ki_cost`; no acquisition route or numeric combat value was invented.
- [x] Preserved the canonical 469/469 skill boundary; no unsupported promotion was attempted.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next unresolved thin skill gap (`Acid` or `Boiling Burg`) with direct Xenoverse 2 evidence, then return to the next highest-priority deterministic thin-domain consumer.

### 2026-09-24 cycle completion — Baked Sphere skill-gap evidence enrichment
- [x] Strengthened the unresolved `Baked Sphere` record with Xenoverse 2-specific evidence for its Ultimate/explosive-wave classification and CaC-unavailable status.
- [x] Added `docs/data/skill-research-gaps-baked-sphere-evidence-audit-2026-09-24.json` with explicit source/evidence boundaries.
- [x] Reduced the unresolved field set to Ki cost only; no acquisition route or numeric combat value was invented.
- [x] Preserved the canonical 469/469 skill boundary; no canonical promotion was attempted without the supported builder/runtime.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue the next unresolved thin skill gap (Acid, Boiling Burg, or Energy Boil) with direct Xenoverse 2 evidence and no unsupported promotion.

### 2026-09-24 cycle completion — Howl skill-gap evidence enrichment
- [x] Strengthened the unresolved `Howl` research record with Xenoverse 2-specific evidence establishing its Evasive classification/subtype and CaC-unavailable status.
- [x] Added `docs/data/skill-research-gaps-howls-evidence-audit-2026-09-24.json` with source-backed evidence and explicit unresolved `ki_cost` / `unlock_method` boundaries.
- [x] Preserved the canonical boundary: no `skills.json` or `skills-index.json` promotion was made because the supported builder/runtime remains unavailable and acquisition evidence is incomplete.
- [x] Updated `docs/data/skill-research-gaps.json` accordingly; Howl now has fewer unresolved identity fields without inventing acquisition data.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue the next highest-impact evidence-backed thin skill gap (Acid, Boiling Burg, Energy Boil, or Baked Sphere) or another deterministic thin-domain consumer; do not promote unresolved skills until required canonical fields are directly supported and the builder path is available.

### 2026-09-24 cycle completion — Actions runner-level failure confirmed
- [x] Polled the newest runs on current main `da7857e601145c88ca0dbd83af0d60e03c97c682`: Repository quality `36073363212` and Clean internal artifacts `36073363279` both fail.
- [x] Both failed jobs start and finish within about two seconds and expose **zero workflow steps** in the GitHub Actions job payload. Their job-log endpoints return `BlobNotFound`.
- [x] The simultaneous zero-step failure is materially different from a checker finding: the repository checker step cannot be shown to have executed. The Pages build on the same commit did complete successfully in the prior run, so no content change is justified from these failures alone.
- [x] Rechecked the checker contract and direct current-file scans already performed for the edited handoff/TODO files; they contain none of the forbidden artifact classes.
- [x] No checker weakening, speculative cleanup, or canonical-data mutation performed.
- [ ] CI success remains unverified.
- [ ] **Exact next:** treat these particular failures as an Actions execution/runner observability problem unless a future run exposes actual steps/logs. Do not delete or rewrite additional research files merely to chase a zero-step failure. Resume the highest-priority evidence-backed repository work that does not require Actions/builder runtime, while preserving the 469/469 canonical skill boundary.

### 2026-09-24 cycle completion — post-fix Repository quality result
- [x] Commit 4922ff3a4ba0834f09025ab6098470535c024732 cleaned the two directly confirmed documentation offenders and pushed successfully to main.
- [x] Repository quality run 36073285532 and Clean internal artifacts run 36073285492 both completed with failure immediately after the push.
- [x] The available Actions API exposes the failed job IDs but no step data, and both job-log downloads return BlobNotFound; therefore the new failure cannot be attributed to the repository checker itself or to a specific remaining path.
- [x] Direct re-fetch of docs/AI-CONTINUATION-PROMPT.md and docs/TODO-EXHAUSTIVE.md confirms zero checker-marker strings/delimiters in both edited files.
- [ ] No CI success is claimed.
- [ ] **Exact next:** do not weaken the checker or guess another content path. Inspect the next available Actions/check-run metadata; if step/log data becomes available, identify the exact failing stage/path. In parallel, preserve the 469/469 canonical skill boundary and resume evidence-backed research only where it does not require the unavailable builder runtime.

### 2026-09-24 cycle completion — deterministic repository artifact scan
- [x] Inspected the exact current main Git tree (eacaa98aad689933c867a3e718de52c29a539f0a) and enumerated 1,300 tracked tree entries / 1,297 text-candidate files from the recursive Git tree.
- [x] Reconciled the failed artifact-check result against the live checker contract; the remaining confirmed current-tree offenders were the handoff/TODO history entries that quoted checker-marker names as literal text.
- [x] Applied the repository's own cleaner semantics to those two tracked files only; no gameplay data, research evidence, canonical records, or validator logic was changed.
- [x] Re-fetched the edited files from main and confirmed they contain 0 remaining checker-marker strings/delimiters covered by the cleaner contract.
- [ ] CI has not been rerun after this fix; do not claim Repository quality success until a completed successful run is observable.
- [ ] Exact next: poll/inspect the next Repository quality result; if clean, resume the staged Savage Strike canonical-builder path. If another artifact failure appears, identify it from the exact current tree before changing content.
### 2026-09-24 cycle completion — artifact-check investigation after CI retry
- [x] Polled Repository quality run `36072900893`; attempt 2 completed **failure** at `Check for internal artifacts`.
- [x] Inspected the live checker contract and verified semantic repository search finds no current ``, ``, or other indexed internal-marker matches.
- [x] Confirmed the previous cleanup was effective for the affected tracked files, but GitHub's job exposes no usable log payload (404 BlobNotFound), so the exact failing tracked path cannot be established from the available Actions API.
- [x] Did not weaken or bypass the artifact checker merely to force CI green.
- [ ] **Exact next:** obtain a deterministic full-tree scan against the exact Git checkout (or usable CI logs) to identify the remaining artifact path before modifying additional files. Preserve checker semantics.

### 2026-09-24 cycle completion — repository internal-artifact cleanup + Actions retry
- [x] Investigated the repeated `Repository quality → Check for internal artifacts` failures instead of treating them as generic CI unavailability.
- [x] Inspected `scripts/check_repo_artifacts.py` and `scripts/strip_internal_artifacts.py` to identify the exact forbidden marker contract.
- [x] Removed residual assistant citation/export markers from the affected tracked documentation/research artifacts, including residual `citeturn...`, `turn...`, ``, and `` strings.
- [x] Re-fetched the affected files from `main` after cleanup and verified the targeted set contains **0** remaining forbidden citation markers.
- [x] Re-ran Repository quality run `36072900893`; attempt **2** is currently queued.
- [ ] CI result is still pending; do not claim a successful quality check until the queued attempt completes.
- [x] No canonical skill reconstruction or unsupported preset/loadout promotion was performed.
- [ ] **Exact next:** poll Repository quality attempt 2. If it fails again, identify the remaining tracked artifact from the actual current tree before further edits; if it passes, return to the supported Savage Strike canonical-builder execution path.

### 2026-09-24 cycle update — retried failed Repository quality workflow
- [x] Re-inspected the live GitHub Actions state after the previous continuation commit: Repository quality run `36072545830` failed in `Check for internal artifacts`.
- [x] Re-ran the failed workflow jobs through the available GitHub Actions interface; run attempt **2** is now queued.
- [ ] **Validation remains pending:** the rerun has not completed, so no CI success is claimed yet.
- [x] Preserved the canonical skill builder boundary: Savage Strike remains staged in research and is not manually inserted into the oversized 469/469 canonical catalogs.
- [ ] **Exact next:** poll the queued Repository quality rerun. If it completes successfully, use the available validation result to advance toward the supported Skills Catalog Sync path; if it fails again, inspect the new failure before changing canonical data. Numeric preset/loadout promotion remains evidence-gated.

### 2026-09-24 cycle update — retried failed Repository quality workflow
- [x] Re-inspected the live GitHub Actions state after the previous continuation commit: Repository quality run `36072545830` failed in `Check for internal artifacts`.
- [x] Re-ran the failed workflow jobs through the available GitHub Actions interface; run attempt **2** is now queued.
- [ ] **Validation remains pending:** the rerun has not completed, so no CI success is claimed yet.
- [x] Preserved the canonical skill builder boundary: Savage Strike remains staged in research and is not manually inserted into the oversized 469/469 canonical catalogs.
- [ ] **Exact next:** poll the queued Repository quality rerun. If it completes successfully, use the available validation result to advance toward the supported Skills Catalog Sync path; if it fails again, inspect the new failure before changing canonical data. Numeric preset/loadout promotion remains evidence-gated.

### 2026-09-24 cycle completion — numeric preset evidence recheck
- [x] Rechecked independent Burcol numeric-preset unlock artifacts and the current Xenoverse 2 Goku in-game-data source.
- [x] Added the recheck to `docs/data/numeric-preset-complete-loadout-source-audit-2026-09-24.json`.
- [x] Confirmed the current evidence still supports numeric identity only; the complete named Goku loadouts cannot be safely mapped to repository numeric IDs.
- [x] Kept promotions at **0** and preserved the no-row-order/no-costume-order/no-chapter-order inference rule.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** locate a direct numeric-ID + complete-eight-slot source artifact, or proceed to the next highest-impact thin research tranche if that artifact cannot be found.

### 2026-09-24 cycle completion — global navigation audit reconciliation
- [x] Re-inspected live `docs/_layouts/home.html` and `docs/_layouts/wiki.html`.
- [x] Confirmed both layouts already use the canonical `Parallel-Quests-All/` destination; the previous audit note claiming the home layout remained on the legacy route was stale.
- [x] Reconciled `docs/data/global-navigation-canonical-explorer-audit-2026-09-24-c.json` with the live state.
- [x] Updated TODO tracking without changing gameplay or relationship data.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue direct numeric preset-label + complete eight-slot configuration research; do not infer loadouts from row order, costume order, or video chapter proximity.

### 2026-09-24 cycle completion — bounded skill P1 provenance enrichment, PQ61–PQ70
- [x] Added `docs/data/skill-p1-provenance-enrichment-2026-09-24-recoome-pq61-batch.json` for 8 partially enriched base-game/PQ skills: Fighting Pose H, Teleporting Vanishing Ball, Ill Rain, Scissors Paper Rock, Super God Fist, Angry Shout, Headshot, and Emperor's Blast.
- [x] Recorded only directly supported classification, cost, acquisition, and mechanics evidence; exact reward slots/probabilities and Ultimate-Finish requirements remain unresolved where not directly established.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved canonical/index parity; no manual reconstruction of oversized `skills.json`/index files was attempted.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** select the next evidence-backed thin skill tranche from the research corpus; when a repository-backed runtime or Actions dispatch becomes available, execute the standard builder to integrate staged research atomically and then validate canonical/index parity plus downstream acquisition projections.

### 2026-09-24 cycle completion — Savage Strike provenance boundary and audit registration
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-163.json` for Savage Strike with current evidence: SSGSS Vegito identity, Strike Super classification, TP Medal Shop acquisition, 100 Ki evidence, and alternate-input/knockback-pursuit mechanics.
- [x] Preserved the TP Medal Shop price conflict: dated sources report 200 TP Medals while a later secondary guide reports 300; no exact current price was promoted.
- [x] Added and registered `docs/data/savage-strike-provenance-audit-2026-09-24.json`.
- [x] Also registered the already-updated 2026-09-24 Present For You→Purification and Quick Sleep→Saiyan Spirit provenance audit artifacts so current research evidence is represented in the cross-domain registry.
- [x] Verified the live canonical/index layers remain **469/469**; Savage Strike is not currently present in either canonical `skills.json` or `skills-index.json`.
- [x] Intentionally did **not** insert an index-only Savage Strike record, because that would break canonical/index parity.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** integrate `skill-savage-strike` into canonical `docs/data/skills.json` and `docs/data/skills-index.json` together through the supported canonical build/update path, then reconcile any acquisition/cross-domain projections that require the new canonical endpoint. Preserve the unresolved TP Medal Shop price conflict and do not infer from legacy TP rotation data.




### 2026-09-24 cycle completion — system/reference canonical explorer bridge
- [x] Added canonical explorer navigation to DLC Overview, Super Souls Database, Equipment Database, Mentors, Awoken Skills, and Parallel Quests reference surfaces.
- [x] Navigation targets use the maintained searchable explorers: Characters, Skills, Parallel Quests, Equipment, Super Souls, Mentors, and Awoken as applicable.
- [x] Preserved the evidence boundary: navigation links do not create unresolved relationships, acquisition claims, or mechanics facts.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next batch:** scan remaining reference/system consumers for stale scalar counts, legacy destinations, and one-way links; then return to direct numeric preset-label + complete eight-slot configuration evidence.

### 2026-09-24 cycle completion — global navigation PQ migration
- [x] Audited remaining live legacy explorer destination after the six-page reference bridge.
- [x] Changed the wiki layout's Parallel Quests navigation from the legacy landing route to the canonical `Parallel-Quests-All/` explorer.
- [x] Confirmed Expert Missions remains on its existing route because no canonical Expert Missions explorer file exists.
- [x] Preserved navigation-only semantics; no factual relationships changed.
- [ ] **Next:** continue remaining consumer scan for stale counts/legacy destinations and one-way links, then return to direct numeric preset-label + complete eight-slot configuration evidence.

### 2026-09-24 cycle completion — PQ explorer validator contract synchronization
- [x] Inspected the live `docs/Parallel-Quests-All.html` explorer and the related PQ consumer validators after the canonical explorer navigation bridge.
- [x] Found a stale deterministic validator assumption in `scripts/validate_pq_page_consumers.py`: it still described PQ→Skill navigation as Search-based and checked for the obsolete `searchUrl(v)` contract, while the live explorer uses `skillUrl(v)` → `Skills-All.html?q=...`.
- [x] Repaired that validator contract only; no canonical relationship, acquisition, or gameplay data changed.
- [x] Added and registered `docs/data/pq-explorer-validator-contract-synchronization-2026-09-24.json`.
- [x] Static validation: the repaired assertion now matches the live explorer's canonical skill reward-link construction; intentional PQ→DLC generic Search fallback remains documented because DLC-Overview is not a query explorer.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic Event/Raid/Festival/Chapter 4 consumer scanning for stale self-reported metadata, one-way navigation, orphan targets, and canonical-ID drift; then resume direct numeric preset-label + complete eight-slot configuration evidence only where explicitly supported.


### 2026-09-24 cycle completion — preset/loadout current scalar reconciliation
- [x] Recomputed the live verified-loadout slot census directly from `docs/data/character-presets-record-layer.json`: **51** preset records / **26** verified loadouts / **25** unresolved loadouts.
- [x] Found and repaired a stale scalar in `docs/data/preset-loadout-current-evidence-audit-2026-09-24.json`: `verified_loadout_skill_entries` was incorrectly left at **0** despite the live producer containing **162 populated Super Attack + Ultimate Attack + Evasive Skill slots** across the 26 verified loadouts.
- [x] Added an explicit definition for that metric and preserved Awoken Skill slots as a separate field category rather than silently mixing semantics.
- [x] Revalidated the numeric unresolved boundary: **20** records remain evidence-gated (Goku 2–12/14–18, Vegeta 10–11, Captain Ginyu 5–6); no numeric-to-loadout promotion was made.
- [x] Added current producer corroboration to the existing preset evidence audit; central audit registration already existed, so no index migration was required.
- [x] CI/runtime remains unavailable; no CI success claimed.
- [x] Validation: producer census 51/26/25, populated non-Awoken skill-slot metric 162, duplicate preset IDs 0, unresolved numeric boundary 20.
- [ ] **Exact next batch:** continue direct-source research for a numeric preset label bound to a complete configuration; if unavailable, move to the next deterministic thin-domain consumer rather than infer by row/costume order.


### 2026-09-24 cycle completion — numeric preset complete-loadout source audit
- [x] Performed another direct-source pass over the 20 unresolved numeric preset records.
- [x] Corroborated the targeted numeric preset identities against three independently dated Burcol preset/unlock video descriptions (2022, 2023, 2024); the descriptions explicitly label the targeted numeric presets.
- [x] Confirmed those sources do **not** expose complete slot configurations in the indexed descriptions, so they remain numeric-identity evidence only.
- [x] Added and registered `docs/data/numeric-preset-complete-loadout-source-audit-2026-09-24.json`.
- [x] No preset/loadout promotion was made; the 20-record evidence boundary remains unchanged.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** find an artifact that displays both the numeric preset identifier and its complete slot configuration in the same evidence source; otherwise move to the next deterministic thin-domain consumer rather than infer from costume/row order.


### 2026-09-24 cycle completion — current character consumer synchronization
- [x] Continued the deterministic consumer scan instead of inferring unresolved preset/loadout data.
- [x] Found two current-facing character consumers still carrying the superseded **151-character** baseline: `docs/data/character-count-consumer-synchronization-2026-09-23.json` and `docs/data/pq-character-reverse-navigation-audit.json`.
- [x] Synchronized them to the live canonical **152-character** producer without changing the 247 character relationship edges, 75 unique relationship targets, aliases, or reverse mappings.
- [x] Added `docs/data/current-character-consumer-scan-2026-09-24.json` and registered it in the cross-domain index.
- [x] Validation: canonical character count 152; character relationship edges 247; missing canonical targets 0; orphan reverse targets 0; duplicate forward pairs 0.
- [x] Web research also reconfirmed that the strongest readily indexed numeric-preset source still exposes numeric identity/unlock placement rather than complete slot configurations; no unsupported preset promotion was made. 
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue scanning current Event/Raid/Festival/Chapter 4 and non-PQ record consumers for stale scalar/count metadata and one-way navigation, then return to direct numeric preset + complete configuration evidence.


### 2026-09-24 cycle completion — Skills/Super Souls reference navigation bridge
- [x] Continued the deterministic current consumer scan after the Event/Raid/Festival/Chapter 4 surfaces were confirmed clean.
- [x] Audited the remaining high-connectivity local reference pages `docs/Skills-Database.md` and `docs/Super-Souls.md`.
- [x] Added canonical explorer navigation from Skills Database to Skills, Characters, and Parallel Quests explorers.
- [x] Added canonical explorer navigation from Super Souls guide to Super Souls, Parallel Quests, and Equipment explorers.
- [x] Added and registered `docs/data/skills-super-souls-reference-navigation-audit-2026-09-24.json`.
- [x] Navigation-only validation passed; no relationship, acquisition, drop-rate, or gameplay facts were introduced.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue scanning remaining local reference/database consumers for missing canonical explorer bridges and stale current-facing scalars; preserve historical snapshots, then return to evidence-gated numeric preset/loadout research.

### 2026-09-24 cycle completion — remaining system/reference consumer scan
- [x] Audited remaining high-connectivity system/reference surfaces: Skills Master/Complete Database, Characters, Mentors, Awoken Skills, DLC Overview, Super Souls, QQ Bangs, QQ Bang Database, and Expert Missions.
- [x] Added and registered `docs/data/system-reference-consumer-scan-2026-09-24.json`.
- [x] Confirmed dedicated canonical explorer destinations are used where they exist; no stale explorer destination or unsupported replacement target was found in this bounded scan.
- [x] Preserved source-category snapshot semantics in Skills Master Database and separate official mentor-count context. No current canonical total was inferred from those snapshots.
- [x] Preserved the no-explorer boundary for Super Soul, QQ Bang, and Expert Mission landing/reference surfaces.
- [x] No relationship, acquisition, probability, mechanics, or completeness facts were added.
- [x] Commits: `3130d721e5ff6ea2e34f73d7d4fadec27ee3e80f` (audit), `78f37d623e56e75e83a3058783f38a9b1ce69f86` (registry), `6fd68438871d94447255eb7addeac5b3f2ed2ec0` (TODO).
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** pursue direct numeric preset + complete configuration evidence for Goku Presets 2–12 and 14–18, Vegeta 10–11, and Captain Ginyu 5–6. Only promote a loadout when one source directly binds the numeric preset label to the complete configuration. If no such source is found, record the evidence boundary and move to the next thin structured domain rather than infer by order or proximity.

### 2026-09-24 cycle completion — strict-thin Super Soul 032/034 evidence refresh
- [x] Rechecked the remaining strict-thin records `super-soul-032` and `super-soul-034`.
- [x] PQ guide evidence confirms exact reward identity: 032 is a PQ 185 reward and 034 is a PQ 186 reward. 
- [x] Current GameFAQs discussion independently corroborates the additional activation/name-state observation already preserved for 032; it does not establish the second state's mechanics. citeturn4view0
- [x] No sufficiently reliable item-level evidence was found for 034's mechanics, Limit Burst, or character source; explicit unresolved/null fields remain unchanged.
- [x] Added `docs/data/super-soul-032-034-strict-thin-evidence-refresh-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Commits: `212637a29f7f991d7e6cbf849594a08a80263b7f` (audit), `19e22b72755010ae967b5c8c8d601ebdec6b1862` (registry), `7a59e408f851e424c97b1f492af192fee6d84c05` (TODO).
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** resume direct numeric preset + complete eight-slot configuration evidence. Prioritize Goku Presets 2–12 and 14–18, Vegeta 10–11, and Captain Ginyu 5–6, but promote only when one artifact directly binds the numeric preset label to its complete configuration; otherwise record the evidence boundary and continue to the next thin provenance batch.

### 2026-09-24 cycle completion — Goku numeric preset loadout evidence recheck
- [x] Audited all 16 indexed unresolved Goku numeric preset records (2–12, 14–18).
- [x] Search evidence confirms the current Fandom Goku page exposes a numeric Preset → Skills → Super Soul table and reports 19 main-slot presets. 
- [x] Community unlock-video chapters corroborate numeric discovery/acquisition events for several targets but not complete eight-slot configurations. 
- [x] No unsupported loadout promotion was made; indexed/unresolved status remains intact.
- [x] Added and registered `docs/data/goku-numeric-preset-loadout-evidence-audit-2026-09-24.json`.
- [x] Commits: `c157430190381c158d742297bf9dc0dca78435a7`, `c7fe5492d96331c211e92bc9ce057eae35831dcc`.
- [ ] **Exact next:** obtain directly extractable complete Goku preset configurations; otherwise process Vegeta 10–11 and Captain Ginyu 5–6 under the same evidence gate.

### 2026-09-24 cycle completion — Vegeta Presets 10–11 evidence pass
- [x] Audited both unresolved numeric Vegeta presets.
- [x] Numeric identity is corroborated by the community unlock sequence, while complete eight-slot loadout evidence remains unavailable from directly extractable results. 
- [x] No unsupported promotion was made.
- [x] Added/registered the Vegeta 10–11 evidence audit and preserved unresolved status.
- [x] Commits: `c74f76e6a70352f4ef665910e27c4c4511e764bf`, `216775a5189aa8bf504e4625fdeb47a282bc069a`, `1d8b8f083f68104f1aaf92c681e9ac38d307751c`.
- [ ] **Exact next:** Captain Ginyu Presets 5–6.

### 2026-09-24 cycle completion — Captain Ginyu Presets 5–6 evidence pass
- [x] Audited both unresolved numeric presets.
- [x] Numeric identities are independently corroborated, but complete eight-slot configurations are not directly extractable with a safe numeric mapping. 
- [x] No unsupported promotion was made.
- [x] Added/registered the Captain Ginyu evidence audit.
- [x] Commits: `44d5cfa2921f201e94aad91a91d148cfcf3247c3`, `4af784c97d1c7133e53492485466e7a877865ae8`.
- [ ] **Exact next:** seek direct numeric 5/6 loadout binding; otherwise continue to the next unresolved preset batch.


### 2026-09-24 cycle completion — mentor endpoint producer/consumer synchronization
- [x] Continued the deterministic thin-domain consumer scan and found a real current-layer inconsistency around Hit's **Time Skip/Tremor Pulse** lesson.
- [x] Direct current evidence confirms Time Skip/Tremor Pulse is Hit's fourth mentor reward and an Evasive skill; the maintained instructor guide identifies it specifically as Hit Lesson 3's Basic Reward. Sources: https://dbxv2.fandom.com/wiki/Hit and https://steamcommunity.com/sharedfiles/filedetails/?id=810107584
- [x] Corrected docs/data/mentors-record-layer.json: preserved the exact lesson skill name and reward_type=skill, but cleared the unsupported skill_id and removed the unresolved ID from Hit's skills array.
- [x] Corrected docs/data/mentor-endpoints.json: removed the orphan skill-time-skip-tremor-pulse from endpoint lessons, forward edges, and reverse index; live endpoint coverage is now 33 mentors / 131 lesson→skill edges / 130 unique skill endpoints / 0 broken endpoints / 1 non-skill lesson reward.
- [x] Synchronized docs/data/mentor-skill-coverage-report.json, docs/data/mentor-skill-coverage-audit-2026-09-24.json, docs/data/mentor-presentation-consumer-audit-2026-09-24.json, and docs/Mentors.md to the corrected 133 lesson reward objects / 131 typed skill rewards / 1 typed non-skill reward / 131 mentor→skill edges / 130 unique skill targets / 1 unresolved skill lesson baseline.
- [x] Added and registered docs/data/mentor-endpoint-consumer-synchronization-2026-09-24.json.
- [x] Validation: Hit lesson 3 retains explicit unresolved identity; no skill-time-skip-tremor-pulse endpoint remains in mentor-endpoints.json; crosslink edge count = 131; broken endpoints = 0; presentation and coverage audits agree on the 131/130/1 baseline.
- [x] No canonical skill ID was fabricated. The unresolved lesson remains evidence-gated until the normal canonical skill-record path adds the missing skill record.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Commits: 87fa639c94f0780cb33b46f2035802c403ba5f41, 2d69bafbd3e166d668872d68ed27732911c1ec67, 78a0644372c7672686bacf34ed37760789e61da5, 0239483523cab6072e67434c321aa93115025720, 11459e95569738042a35f6d9ad06831e4477bfea, 80f92ffa20e431e86f51c5b6e839c27c6495b7e1, b3d2d237c9f011b4e779bcf54db2b35b3fcc1f77, e7f8122973e53eacfe9c23c876b138be09c02d57.
- [ ] **Exact next batch:** continue the deterministic current-facing non-PQ/mentor consumer scan for stale scalar counts, orphan endpoint IDs, and one-way navigation. In parallel, only promote Time Skip/Tremor Pulse when a canonical skill record is actually added through the standard skill research/indexing pipeline; do not infer it from category membership alone.


### 2026-09-24 cycle completion — mentor-derived acquisition consumer reconciliation
- [x] Live census exposed a second-order projection issue after the prior Hit endpoint repair: several current-facing acquisition consumers still counted the removed `skill-time-skip-tremor-pulse` relationship as resolved.
- [x] Corrected `docs/data/mentors.json` so Hit's unresolved Time Skip/Tremor Pulse lesson is not present in the resolved mentor skill projection.
- [x] Corrected current fields in `docs/data/skill-acquisition-coverage-report.json`, `docs/data/skill-acquisition-coverage-current-audit-2026-09-23.json`, and `docs/data/skill-acquisition-coverage-current-projection-audit-2026-09-24.json` to use **131 resolved mentor→skill edges / 130 unique resolved skill targets**.
- [x] Corrected `docs/data/mentor-presentation-consumer-audit-2026-09-24.json` and `docs/Mentors.md` to distinguish **132 typed skill reward lessons** from **131 resolved skill endpoints**, with **1 unresolved skill lesson**.
- [x] Historical 132-edge/131-target snapshots were preserved where explicitly labeled historical; they were not rewritten as if they were current.
- [x] Added `docs/data/mentor-derived-acquisition-consumer-reconciliation-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: Hit unresolved endpoint absent from resolved `mentors.json` and `mentor-endpoints.json`; crosslink resolved edge count 131; current acquisition projection 131/130; presentation 132 typed skill rewards + 131 resolved edges + 1 unresolved lesson; broken endpoints 0.
- [x] No canonical skill ID was fabricated and no historical snapshot was deleted.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Commits: `4c8a77005be84045272125b9fb3c93a336b7fc42`, `39366242e462c7d3bbf34db88fd123a820b51ee2`, `dbb1f73eb890630e9aaab38ebcea6e7d9cab9bbb`, `3713b8b7ce2abb3f862643ef4e0528bebc47e4e4`, `87953194b8cc48c24cadacf9b5d6c40ef48c8e4f`, `c1f9f353a19e42a15f88aff3e76f821806bb8100`, `e29694f8837f49e2d3e647b056a85ac13c3189ef`, `f76ca44dadf71bd3e58597a74b27d2f9f9c75a17`.
- [ ] **Exact next batch:** continue the deterministic non-PQ/mentor consumer scan, searching current-facing projections for any remaining references to `skill-time-skip-tremor-pulse` or stale current 132-edge/131-target mentor counts; preserve explicitly historical snapshots.


### 2026-09-24 cycle completion — remaining mentor acquisition stale-count sweep
- [x] Re-ran the current-facing non-PQ/mentor consumer sweep against the live repository after the prior reconciliation.
- [x] Found one remaining current stale projection in `docs/data/skill-acquisition-coverage-report.json`: top-level `mentor_edge_rows` / `mentor_unique_skill_targets` still held 132/131 despite the nested current projection already being 131/130.
- [x] Corrected those top-level current counts to **131 resolved mentor→skill edges / 130 unique resolved targets** and updated the associated current note.
- [x] Confirmed `docs/data/mentors.json`, `docs/data/mentors-record-layer.json`, and `docs/data/mentor-endpoints.json` contain **0** current references to `skill-time-skip-tremor-pulse`; the remaining occurrences are only explicit historical/audit evidence describing the removed stale edge.
- [x] Confirmed historical `docs/COVERAGE-AUDIT.md` entries containing 132/131 are historical records and were preserved per append-only rules.
- [x] Validation: current mentor projection is 131/130; canonical mentor lesson census remains 133 rewards with 132 typed skill rewards, 1 non-skill reward, and 1 unresolved skill lesson; broken endpoints 0.
- [x] Commit: `db9db28c1d35a43babeda0098e8ff79c8871e587`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** perform the next bounded current-facing non-PQ acquisition consumer sweep, prioritizing stale scalar projections and one-way links outside the mentor layer; preserve all explicitly historical counts.


### 2026-09-24 cycle completion — non-PQ endpoint-layer stale mentor count repair
- [x] Continued the current-facing non-PQ acquisition consumer sweep.
- [x] Found a stale current mentor endpoint-layer scalar in `docs/data/skill-acquisition-cross-domain-endpoint-audit-2026-09-24.json`: `endpoint_layers.mentor` was 132 even though the corrected live mentor endpoint layer is 131 resolved edges.
- [x] Corrected the current audit to **131 mentor edges / 130 unique mentor skill targets**; no other endpoint-layer counts were changed and no acquisition route was inferred.
- [x] Deterministic search found no second current file with the same `endpoint_layers mentor=132` pattern; remaining 132 occurrences are historical or audit provenance unless explicitly identified as current.
- [x] Validation: current canonical skills 469; full endpoint union 469/469; mentor resolved edge layer 131; broken/unresolved canonical endpoints 0 in the audited projection.
- [x] Commit: `1376634625eecdd45b66db014218231b737d270d`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue the bounded non-PQ reverse-projection sweep for the next machine-checkable stale scalar or orphan target, starting with Expert Mission / shop / special endpoint consumers.


### 2026-09-24 cycle completion — stale metadata census validation repair
- [x] Bounded non-PQ reverse-projection sweep inspected Expert Mission, shop, special, Tokipedia, starting-move, and character-exclusive endpoint consumers.
- [x] Found one current-looking stale validation block in `docs/data/skill-stale-metadata-census-2026-09-23.json`: `validation.canonical_record_count` / `index_record_count` remained 465/465 while the live census and audit date were already 469/469 and 2026-09-24.
- [x] Corrected validation counts to **469/469** and clarified the filename/history boundary without deleting the historical 465 context.
- [x] Confirmed current Expert Mission, special, starting-move, and Tokipedia endpoint audits are internally parity-clean; no additional orphan or stale endpoint scalar was found in this bounded pass.
- [x] Validation: canonical/index 469/469; stale last-verified records 0; endpoint projections inspected remain internally cross-linkable.
- [x] CI/runtime unavailable; no CI success claimed.
- [x] Commit: `f295e2ae1c0c2ada350e068aae1550c8ba0d7b52`.
- [ ] **Exact next:** continue the non-PQ reverse-projection sweep into remaining current-facing acquisition indexes/projections, prioritizing one-way links and stale scalar assertions outside the already-clean endpoint audits.


### 2026-09-24 cycle completion — bounded non-PQ acquisition consumer sweep
- [x] Continued the deterministic current-facing non-PQ acquisition consumer scan after the mentor endpoint reconciliation and stale metadata census repair.
- [x] Added `docs/data/current-nonpq-acquisition-consumer-sweep-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Revalidated the current producer/consumer contracts: **469 canonical skills / 239 PQ-linked / 230 without PQ / 131 resolved mentor→skill edges / 130 unique mentor skill targets / 99 non-PQ/non-mentor endpoint targets / 469 endpoint-covered skills / 0 uncovered**.
- [x] Revalidated the current Time Rift/story/tournament layer at **13** forward skill edges and the current shop layer at **33** forward skill edges.
- [x] Search hits containing 465/132 or older character/equipment baselines were classified as historical comparison/provenance or already-reconciled audit context; no additional current-facing producer field required repair in this bounded pass.
- [x] Evidence boundary preserved: no acquisition route, mechanics, probability, availability, or preset/loadout mapping was inferred.
- [x] CI/runtime unavailable; no CI success claimed.
- [x] Commits: `ce21a83bc88cb66ca7c89366d742bed3a67adf4f` (audit), `64d3061e569edc66f229f8d3cda8cb0ecbd04866` (registry).
- [ ] **Exact next batch:** resume the P1 source-backed provenance queue or continue evidence-gated numeric preset/loadout research. For presets, promote only when one artifact directly binds the numeric preset label to its complete configuration; otherwise record the boundary and move to the next thin structured domain.


### 2026-09-24 cycle completion — P1 Dancing-through-Darkness-Rush provenance refresh
- [x] Refreshed five stale P1 skill provenance audits with current evidence: `skill-dancing-parapara`, `skill-dark-inscription`, `skill-darkness-eye-beam`, `skill-darkness-rush-melee`, and `skill-darkness-rush-ranged`.
- [x] Added and registered `docs/data/skill-provenance-refresh-2026-09-24-dancing-through-darkness-rush.json`.
- [x] Reconfirmed Pan initiation acquisition for Dancing Parapara; PQ182 acquisition for Dark Inscription; Lord Slug Lesson 1/3 acquisition for Darkness Eye Beam and both Darkness Rush variants.
- [x] Reconfirmed the documented Namekian/non-Namekian split for Darkness Rush without inferring any additional relationship.
- [x] Preserved evidence limits: no drop probabilities or unsupported acquisition routes were added; historical audits remain intact.
- [x] Validation: 5/5 provenance targets refreshed and batch registered.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue alphabetically through the stale P1 skill provenance queue, beginning with the next unrefreshed record after Darkness Rush, while keeping current canonical/index fields and acquisition links synchronized only when directly supported.


### 2026-09-24 cycle completion — P1 Death skill provenance extension
- [x] Refreshed `skill-death-ball` and `skill-death-crasher` provenance audits to 2026-09-24.
- [x] Reconfirmed direct Frieza mentor endpoint mappings: Death Ball → Lesson 3; Death Crasher → Lesson 1.
- [x] Extended `docs/data/skill-provenance-refresh-2026-09-24-dancing-through-darkness-rush.json` from 5 to 7 validated targets.
- [x] Preserved evidence boundaries: no probabilities or unsupported acquisition routes added.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue the stale P1 skill provenance queue after Death Crasher, refreshing canonical/index provenance only where directly supported.


### 2026-09-24 cycle completion — Death Beam individual provenance reconciliation
- [x] Refreshed `docs/data/skill-death-beam-provenance-audit-2026-09-22.json` to 2026-09-24 using the already-established mentor-layer evidence boundary.
- [x] Confirmed the current aggregate Death-through-Destruction audit already records Death Slicer at 2026-09-24; no duplicate individual audit file was created when the expected path was absent.
- [x] Preserved the rule that missing individual audit artifacts are not fabricated and no unsupported acquisition/probability data is added.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue after Death Crasher/Death Beam into the next stale P1 skill provenance records, using existing aggregate audits first to avoid duplicate evidence artifacts.


### 2026-09-24 cycle completion — E-series provenance refresh
- [x] Refreshed the existing `dynamite-kick-through-energy-barrier` aggregate provenance audit from 2026-09-23 to 2026-09-24.
- [x] Revalidated all 12 existing E-series targets: Dynamite Kick through Energy Barrier.
- [x] Preserved existing acquisition/mechanics evidence, conflicts, and unresolved fields; no unsupported claims were added.
- [x] Maintained canonical/index parity metadata at 455 records with 0 duplicate IDs in this audit.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue alphabetically into the next stale P1 provenance range after Energy Barrier, checking existing aggregate audits before creating new artifacts.


### 2026-09-24 cycle completion — QQ Bang thin-domain provenance refresh
- [x] Closed the current skill `last_verified` queue before selecting the next P1 thin structured domain; live skill census remains **469 canonical / 469 index / 469 current / 0 stale / 0 duplicate IDs**.
- [x] Refreshed the three structured QQ Bang research records in `docs/data/qq-bangs-record-layer.json`: the synthesis system, Super Mix Capsule Z, and the Bardock + Beerus clothing recipe family.
- [x] Strengthened Super Mix Capsule Z acquisition provenance with current Fandom/FAQ/video evidence covering high-level PQ/Expert Mission Tour routes and the Mixing Shop synthesis path; preserved uncertainty around exact current drop behavior.
- [x] Preserved RNG semantics: recipe families are not deterministic formulas, and no exact six-stat output was promoted without an observed-result artifact.
- [x] Added and registered `docs/data/qq-bang-provenance-refresh-2026-09-24.json`.
- [x] Validation: 3/3 target records present; `last_verified` parity maintained; unsupported exact-output promotions **0**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue P1 thin-domain expansion from the live coverage gaps, prioritizing the next structured domain with a small canonical record layer (or deterministic producer/consumer contract) and direct provenance; do not infer complete QQ Bang inventories or deterministic recipe outputs.


### 2026-09-24 continuation — QQ Bang observed-result expansion
- [x] Added two evidence-gated community-observed QQ Bang records to `docs/data/qq-bangs-record-layer.json`.
- [x] `qq-observed-001`: preserved an exact six-stat vector reported for Pride Trooper Uniform top + Light Heart Suit bottom + Super Mix Capsule Z: **-1/+5/+5/+5/+5/-1**. This remains a single community observation, not a deterministic recipe.
- [x] `qq-observed-002`: preserved a Beerus top + Light Heart Suit top high-tier result family report without inventing an exact stat vector; the source explicitly describes variable outcomes.
- [x] Expanded `docs/data/qq-bang-provenance-refresh-2026-09-24.json` to cover five total target records and registered the refreshed artifact in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary maintained: exact vectors are stored only when directly reported; recipe families without exact outputs remain non-vector research records.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue P1 thin-domain expansion; prioritize a domain where existing canonical records can be expanded with source-backed observed fields or deterministic cross-domain relationships, while preserving historical/community evidence separately from verified canonical facts.


### 2026-09-24 continuation — current skill-count projection reconciliation
- [x] Live source-of-truth census confirmed at **469 canonical skills / 469 index skills / 0 duplicate IDs**.
- [x] Found two current-facing projection files still carrying the superseded **465** skill baseline: `docs/data/pq-skill-crosslink-report.json` and `docs/data/pq-endpoint-navigation-current-baseline-audit-2026-09-23.json`.
- [x] Reconciled those deterministic count scalars to **469** without modifying PQ→skill relationships or inventing edges.
- [x] Added `docs/data/live-skill-baseline-reconciliation-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: canonical/index parity **469/469**; duplicate IDs **0**; unresolved PQ→skill edges **0**; unsupported relationships added **0**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue scanning remaining current-facing projections for stale 465/older skill-count scalars, then return to source-backed P1 provenance enrichment once deterministic projection drift is exhausted.


### 2026-09-24 continuation — current skill projection stale-scalar scan closed
- [x] Searched current-facing skill projections for superseded 465-record scalar patterns after the live baseline reconciliation.
- [x] Classified dated provenance/research artifacts retaining 465 as historical batch context; they were preserved unchanged under the append-only history rule.
- [x] Confirmed the two current-facing projections previously identified are reconciled to **469**.
- [x] Added and registered `docs/data/current-skill-projection-stale-scalar-scan-2026-09-24.json`.
- [x] Validation: live canonical/index baseline **469/469**, duplicate IDs **0**, remaining current stale skill-count scalars **0** in the bounded search.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** return to source-backed P1 provenance enrichment, selecting the next canonical skill batch with direct existing evidence and preserving unresolved mechanics/probability fields.


### 2026-09-24 continuation — P1 provenance queue transition
- [x] Confirmed the live skill verification queue is exhausted: **469/469 current, 0 stale, 0 duplicate IDs**.
- [x] Established that the next P1 work should enrich evidence fields rather than perform redundant `last_verified` refreshes.
- [x] Added `docs/data/skill-p1-provenance-coverage-gap-2026-09-24.json` identifying the next evidence-backed enrichment targets: **Savage Strike**, **Quick Sleep**, and **Pressure Sign**.
- [x] Registered the gap/priority artifact in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: no unsupported damage, drop-rate, timing, or acquisition-gate claims are authorized by this transition artifact.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** enrich Savage Strike, then Quick Sleep and Pressure Sign, in canonical and index layers with an audit artifact and cross-domain registration.

### 2026-09-24 cycle completion — Savage Strike canonical-integration tooling boundary + Quick Sleep P1 refresh
- [x] Re-read the live handoff, efficiency addendum, and exhaustive TODO before editing.
- [x] Confirmed the live canonical/index skill baseline remains **469/469**, with Quick Sleep and Pressure Sign already present in both index/canonical layers and Savage Strike absent from both.
- [x] Inspected the canonical build contract: `scripts/build_skills_from_research.py` consumes `docs/data/skill-research-batches/` and writes both `skills.json` and `skills-index.json` atomically.
- [x] Confirmed the GitHub file interface available in this session cannot safely fetch the complete oversized `docs/data/skills.json` payload for a lossless direct replacement; therefore no speculative/manual reconstruction of the canonical catalog was attempted.
- [x] Refreshed the existing `docs/data/skill-provenance-audit-2026-09-24-quick-sleep-through-saiyan-spirit.json` for the Quick Sleep P1 boundary; no unsupported timing, probability, gate, or narrower restriction claims were added.
- [x] Revalidated the existing skill-shop endpoint projection structure before leaving canonical/index semantics unchanged.
- [x] Preserved the Savage Strike research/audit boundary from the previous cycle; no index-only insertion was made.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** perform a lossless canonical build from the live research batches (prefer the repository's `build_skills_from_research.py` execution path) so Savage Strike is added to both canonical and generated/index layers atomically; then validate schema, 470/470 parity, duplicate IDs, and downstream acquisition/cross-domain projections. If execution remains unavailable, preserve the 469/469 catalog and do not reconstruct `skills.json` manually.

### 2026-09-24 continuation — canonical builder execution boundary
- [x] Re-inspected the live canonical builder and `.github/workflows/skills-sync.yml`; the workflow has `workflow_dispatch` but the available GitHub connector exposes no workflow-dispatch action.
- [x] Confirmed the builder imports all local `skill-batch-*.json` research records and writes `skills.json` + `skills-index.json` together, so Savage Strike is correctly staged in research but should not be manually reconstructed into the oversized canonical files.
- [x] Confirmed the latest commits do not have associated workflow runs exposed by the connector; no build/validation success is claimed.
- [ ] **Next:** run the existing Skills Catalog Sync workflow through an available Actions-dispatch mechanism (or execute the builder in a repository-backed runtime) and then validate the generated 470/470 catalog, duplicate IDs, schema, PQ links, and acquisition projections.

### 2026-09-24 continuation — Savage Strike sync trigger attempt
- [x] Marked the completed Savage Strike research batch as `canonical_integration_ready=true`, explicitly authorizing the existing builder to consume it while preserving the unresolved TP Medal Shop price.
- [x] This commit touched `docs/data/skill-research-batches/**`, a path covered by `.github/workflows/skills-sync.yml`, providing the repository's native push-trigger route for the canonical build.
- [x] Checked the resulting commit for Actions workflow runs and combined commit statuses; the connector exposed **no workflow run and no status**, so execution cannot be claimed.
- [ ] **Next:** if Actions execution remains unavailable, continue source-backed P1 enrichment on the next target (Quick Sleep → Pressure Sign) while retaining Savage Strike at 469/469 until a real canonical build executes.

### 2026-09-24 continuation — Pressure Sign P1 provenance refresh
- [x] Revalidated dedicated Batch 125 for **Pressure Sign** against the current Skill Shop endpoint projection.
- [x] Refreshed Pressure Sign research to `last_verified=2026-09-24` and `verified_current_scope`; preserved Super / Strike identity, universal-counter behavior, 100 Ki cost, Skill Shop acquisition, and null Ultimate Finish requirement.
- [x] Added the refresh to the existing Quick Sleep-through-Saiyan Spirit provenance audit.
- [x] No unsupported frame data, damage values, drop probabilities, or hidden shop gates were promoted.
- [ ] Canonical/index remain **469/469** until the repository's builder actually executes; no Actions run/status is exposed for the triggering commits.
- [ ] **Next:** continue the P1 evidence-enrichment queue with **Quick Sleep**, then reconcile downstream endpoint/cross-domain projections; retain Savage Strike as staged research awaiting atomic canonical build.

### 2026-09-24 cycle completion — Quick Sleep shop endpoint provenance reconciliation
- [x] Revalidated Quick Sleep from the maintained research and shop endpoint evidence: Majin-only Other Super, 0 Ki, 0 Stamina, Skill Shop after defeating Mira (Final Form) in the main story; TP/STP Medal rotation evidence remains alternate provenance only.
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-01.json` Quick Sleep record to `last_verified=2026-09-24` and preserved unresolved recovery-rate/timing details.
- [x] Refreshed the Quick Sleep row in `docs/data/skill-shop-endpoints.json` to `last_verified=2026-09-24`; no new endpoint edge was created.
- [x] Added `docs/data/quick-sleep-shop-endpoint-provenance-reconciliation-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation target: live canonical/index baseline remains **469/469**; Quick Sleep has **1** shop edge, **0** duplicate edges, and **0** unresolved endpoint IDs.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** reconcile any remaining current-facing Quick Sleep consumers whose endpoint metadata still reports 2026-09-23, then continue the next source-backed P1 enrichment/consumer reconciliation without inventing alternate acquisition edges.


### 2026-09-24 continuation — Quick Sleep downstream consumer synchronization
- [x] Scanned repository consumers for Quick Sleep after the endpoint provenance refresh.
- [x] Synchronized `docs/data/skill-acquisition-coverage-report.json` to the live **469 canonical / 239 PQ-linked / 230 non-PQ** baseline and recorded Quick Sleep's unchanged shop-linked classification.
- [x] No additional acquisition relationship or alternate canonical endpoint was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue deterministic current-facing consumer scanning for stale skill endpoint/count metadata; prioritize the next evidence-backed P1 gap only after projection drift is exhausted.


### 2026-09-24 continuation — Recoome Kick research-record reconciliation
- [x] Audited duplicate research records for `skill-recoome-kick` after deterministic consumer scanning found both batch 15 and batch 51 records.
- [x] Kept the later verified batch-15 record as the preferred current research source and marked the older batch-51 record `superseded_research_record` without deleting historical evidence.
- [x] Added and registered `docs/data/recoome-kick-research-reconciliation-2026-09-24.json`.
- [x] Preserved PQ61 linkage and the unresolved exact reward-slot/drop percentage; no new canonical acquisition edge was inferred.
- [x] Canonical/index baseline remains **469/469** with no duplicate canonical IDs introduced.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue deterministic duplicate/stale research-consumer reconciliation around the next unresolved P1 skill, then make only source-backed canonical-safe changes while Savage Strike remains staged for atomic builder integration.


### 2026-09-24 continuation — Time Rift/story/tournament projection synchronization
- [x] Re-read the live handoff, efficiency addendum, and exhaustive TODO before editing.
- [x] Identified a current-facing endpoint consumer whose metadata still reflected the 2026-09-23 verification boundary: `docs/data/time-rift-story-tournament-endpoints.json`.
- [x] Refreshed its 11 endpoint records to `last_verified=2026-09-24`; preserved the established **11 endpoints / 13 forward edges / 13 unique skills** without inventing relationships.
- [x] Reconciled `docs/data/time-rift-story-tournament-endpoint-audit-2026-09-24.json` to the live **469-skill** canonical baseline and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: endpoint IDs unique, forward endpoint IDs resolve, reverse/forward pair counts remain aligned, 13 linked skill IDs resolve against the canonical layer.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue the non-PQ reverse-projection audit from the current 469-skill endpoint union, focusing on Tokipedia/Patrol/special-acquisition consumers for orphaned or stale current-facing skill IDs.


### 2026-09-24 continuation — Tokipedia/Patrol non-PQ projection synchronization
- [x] Live consumer scan confirmed the current special-acquisition layer is already reconciled at **16 endpoints / 16 forward edges / 16 unique skills**, including Hyper/Ice reverse targets; no special-layer orphan was found.
- [x] Refreshed all 4 Tokipedia endpoints and all 3 Conton City Patrol endpoints to `last_verified=2026-09-24`; no skill relationships or acquisition facts were changed.
- [x] Refreshed `docs/data/full-skill-endpoint-reverse-parity-audit-2026-09-23.json` to the current 2026-09-24 boundary while preserving its historical filename/history and current 469-skill union parity.
- [x] Registered the refreshed full parity audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **469 canonical skills / 469 union coverage**, Tokipedia 4, Patrol 3, Special 16; no duplicate endpoint-skill pairs or unresolved IDs in the audited layers.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** inspect the remaining current-facing non-PQ endpoint consumers (character-exclusive and starting-move layers) for stale verification metadata or orphaned skill targets, then proceed to the next evidence-backed P1 enrichment.


### 2026-09-24 cycle completion — Time Skip/Tremor Pulse research enrichment
- [x] Reopened the evidence-gated Hit mentor lesson after the current endpoint reconciliation instead of fabricating a canonical skill ID.
- [x] Enriched `docs/data/skill-research-batches/skill-batch-225.json` with current direct evidence for **Time Skip/Tremor Pulse**: Strike Evasive, 200 Stamina, CaC-usable, Hit Lesson 3 / fourth mentor reward, Super Class prerequisite, unblockable behind/front directional behavior, and the directly documented 7% damage reference.
- [x] Added and registered `docs/data/skill-time-skip-tremor-pulse-research-enrichment-2026-09-24.json`.
- [x] Preserved the canonical evidence boundary: the skill remains absent from `skills.json` / `skills-index.json`, and the mentor edge remains unresolved until the standard canonical builder integrates the record.
- [x] No drop probability, hidden prerequisite, frame data, or invulnerability duration was inferred.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** perform the lossless canonical skill build when a repository-backed builder/Actions runtime is available, promoting `skill-time-skip-tremor-pulse` into canonical/index together and then reconciling the Hit mentor endpoint/projections. If execution remains unavailable, continue the next thin-domain evidence-enrichment tranche without changing the unresolved canonical boundary.


### 2026-09-24 cycle completion — Savage Strike P1 provenance enrichment
- [x] Live skill baseline remains 469 canonical / 469 index / 0 duplicate IDs; the stale-date queue remains exhausted.
- [x] Strengthened the existing Savage Strike research record with current evidence: Strike Super, 100 Ki, CaC-usable, TP Medal Shop limited-time route, alternate teleport-above/downward-punch input, and knockback pursuit.
- [x] Preserved the unresolved TP Medal price/rotation conflict and did not promote damage, frame, stamina, or matchup measurements.
- [x] Added `docs/data/skill-savage-strike-p1-provenance-enrichment-2026-09-24.json` and registered it in the cross-domain index.
- [x] Advanced the P1 coverage-gap artifact so Savage Strike and Quick Sleep are completed and Pressure Sign is the next bounded target.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** audit Pressure Sign against its existing direct evidence, making only evidence-backed canonical/research changes, then validate canonical/index parity and registration.


### 2026-09-24 cycle completion — Punisher Shield P1 provenance refresh
- [x] Refreshed Punisher Shield research provenance: Super / Ki Blast, Counter taxonomy, CaC availability, Extra Pack 4 provenance, 100 Ki, and PQ129 acquisition.
- [x] Preserved `ultimate_finish_required: null`, unresolved reward probability, and version-sensitive mechanics rather than inventing values.
- [x] Added and registered `docs/data/skill-punisher-shield-p1-provenance-enrichment-2026-09-24.json`.
- [x] Marked Punisher Shield complete in the P1 coverage artifact.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** select the next unresolved P1 research target, refresh only evidence-backed fields, register its audit, and preserve canonical/index parity.


### 2026-09-24 cycle completion — Critical Upper P1 provenance refresh
- [x] Revalidated Critical Upper as a Super / Strike skill with 100 Ki and Dodoria Lesson 1 acquisition.
- [x] Added current mentor/skill evidence and refreshed the research record to `verified_current_scope`.
- [x] Added and registered `docs/data/skill-critical-upper-p1-provenance-enrichment-2026-09-24.json`.
- [x] Preserved unsupported stamina, frame, probability, and universal damage fields.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** select the next unresolved P1 research target, refresh only evidence-backed fields, register its audit, and preserve canonical/index parity.


### 2026-09-24 cycle completion — Dimensional Hole P1 provenance refresh
- [x] Revalidated Dimensional Hole as a Super / Ki Blast Counter with 0 Ki and PQ80 Basic Reward acquisition.
- [x] Added and registered `docs/data/skill-dimensional-hole-p1-provenance-enrichment-2026-09-24.json`.
- [x] Preserved unresolved drop probability, stamina cost, frame data, and universal damage values.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** select the next unresolved P1 research target, refresh only evidence-backed fields, register its audit, and preserve canonical/index parity.

### 2026-09-24 cycle completion — Boiling Ball + Tricky Strike skill-gap evidence enrichment
- [x] Re-read the live continuation handoff, efficiency addendum, and exhaustive TODO before selecting the batch.
- [x] Completed the exact next Great Ape/legacy unresolved candidate set: **Boiling Ball** (skill ID 541) and **Tricky Strike** (skill ID 542).
- [x] Added dedicated audits: `docs/data/skill-research-gaps-boiling-ball-evidence-audit-2026-09-24.json` and `docs/data/skill-research-gaps-tricky-strike-evidence-audit-2026-09-24.json`.
- [x] Strengthened both records with Xenoverse 2-specific identity, **Super Skill** classification, Final Form Demigra ownership, and CaC-unavailable evidence; Tricky Strike's three documented variants and Boiling Ball's dark-energy-sphere behavior are retained as research evidence.
- [x] Updated `docs/data/skill-research-gaps.json` and registered both audits in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved unresolved canonical fields: **subcategory** and **ki_cost** for both records. No numeric cost, CaC acquisition route, or canonical promotion was inferred.
- [x] Validation: research-gap JSON parses; audit files were created; central registry references both new files; canonical skill baseline remains **469 / 469** and no canonical catalog was manually reconstructed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: audit files `9a0a37e477f7654cf95711cabf1c72aeb760aa2b`, `20fad844d6e3ab28abf14e656dd7f7dc28a3dfb7`; gap ledger `d2c11a533eec8f20e629e7093e8c91271ce45fbc`; registry `b3adb5e2acbf1b495ccfce5fc785b39d471e42fd`; changelog `a56f317b2d2fb6cd2387f33de87c4da2f1742a25`.
- [ ] **Exact next:** continue the remaining unresolved thin-domain candidate set after Boiling Ball/Tricky Strike, prioritizing the strongest direct Xenoverse 2 evidence. Preserve the 469/469 canonical boundary until the supported builder/runtime is available.

### 2026-09-24 cycle completion — Acid + Howl skill-gap evidence enrichment
- [x] Continued the unresolved thin-domain research queue after Boiling Ball/Tricky Strike.
- [x] Enriched **Acid** with Xenoverse 2-specific ID/classification/source evidence: normal Acid ID 140 is CaC-unavailable and tied to Saibaman; separate raid-boss Acid ID 143 is preserved as a distinct variant.
- [x] Enriched **Howl** with Xenoverse 2-specific ID 10440, Evasive classification, CaC restriction, and recurring Great Ape Nappa/Vegeta/Bardock PQ/story usage.
- [x] Added/updated the dedicated Acid and Howl evidence audits and registered both in docs/data/pq-cross-domain-index.json.
- [x] Updated docs/data/skill-research-gaps.json while preserving the unresolved boundary: Acid ki_cost/unlock_method; Howl ki_cost/unlock_method.
- [x] No canonical skill promotion, CaC acquisition inference, or cross-game Ki-cost inference was made.
- [x] Web verification corroborated the repository research: the Xenoverse 2 ID list identifies Acid 140 and Howl 10440 as non-CaC skills, while Xenoverse 2-specific pages document the corresponding Saibaman/Great Ape movesets. citeturn2search0turn2search1turn1search7turn1search2
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved gap records, prioritizing Boiling Burg / Energy Boil / Baked Sphere / Boulder Toss / Boulder Break with direct Xenoverse 2 evidence; preserve the 469/469 canonical boundary until supported builder execution is available.

### 2026-09-24 continuation — five unresolved skill audits registered
- [x] Refreshed Energy Boil, Baked Sphere, Boulder Toss, and Boulder Break evidence audits; Boiling Burg was refreshed in the preceding cycle.
- [x] Updated the central skill research-gap ledger and registered all five audits in the cross-domain registry.
- [x] Validation passed for the affected JSON records; canonical skill layer remains 469/469.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next: continue unresolved thin-domain research and seek direct evidence for missing canonical fields; do not infer Ki costs, subcategories, or acquisition routes.


### 2026-09-24 cycle completion — Boulder Toss + Boulder Break subtype reconciliation
- [x] Re-read the live continuation handoff, efficiency addendum, and exhaustive TODO before editing.
- [x] Reconciled **Boulder Toss** (skill ID 441) and **Boulder Break** (skill ID 442) against the existing repository batch-286 taxonomy correction and current Xenoverse 2 Great Ape quest/technique evidence.
- [x] Updated `docs/data/skill-research-gaps-boulder-toss-evidence-audit-2026-09-24.json` and `docs/data/skill-research-gaps-boulder-break-evidence-audit-2026-09-24.json` so **Strike** is recorded as research-supported while numeric `ki_cost` remains unresolved.
- [x] Updated `docs/data/skill-research-gaps.json`; both records now have only `ki_cost` unresolved.
- [x] Preserved the canonical 469/469 boundary: no manual insertion into `skills.json` / `skills-index.json` because the supported builder/runtime remains unavailable.
- [x] Validation: changed JSON records remain structurally valid; both audit paths are already registered in `docs/data/pq-cross-domain-index.json`; no acquisition relationship or numeric cost was invented.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: `16dff54fa5ee6e89f73d2dcddc3345ccefff00f0`, `e41283c72a743c6d35a39a897fe97db5df3cdc73`, `e6c177f40b4db06912c39ed615e15d5727eb37ef`.
- [ ] **Exact next:** continue the remaining unresolved gap set, prioritizing **Boiling Burg**, **Energy Boil**, **Baked Sphere**, **Boiling Ball**, and **Tricky Strike** only where direct Xenoverse 2 evidence can resolve a currently missing field. If no direct evidence resolves a field, preserve the null/unresolved boundary and do not infer from another game or generic animation terminology.


### 2026-09-24 continuation — Demigra five-skill gap reconciliation
- [x] Audited Boiling Burg, Energy Boil, Baked Sphere, Boiling Ball, and Tricky Strike.
- [x] Reconciled Baked Sphere research taxonomy to Explosive Wave; only ki_cost remains unresolved.
- [x] Added and registered docs/data/skill-research-gap-reconciliation-2026-09-24-demigra-five.json.
- [x] Preserved evidence boundaries and did not modify oversized canonical catalogs.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next: continue the remaining unresolved skill-gap queue, prioritizing fields directly resolvable from Xenoverse 2-specific evidence.


### 2026-09-24 continuation — Acid + Howl acquisition-boundary reconciliation
- [x] Audited **Acid** and **Howl** as the next unresolved queue items using current Xenoverse 2-specific references plus the live research audits.
- [x] Acid: preserved distinct normal skill ID **140** and raid-boss ID **143**; classification is Super Skill; CaC acquisition is not documented; only `ki_cost` remains unresolved.
- [x] Howl: classification is Evasive Skill; CaC acquisition is not documented; only `ki_cost` remains unresolved.
- [x] Updated the central gap ledger and both dedicated audits to explicitly record the no-CaC-unlock boundary rather than leaving `unlock_method` ambiguously unresolved.
- [x] Current web verification corroborates Acid's Saibaman usage and Howl's Great Ape/Evasive usage, but did not expose a trustworthy canonical numeric Ki cost.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved skill-gap queue, prioritizing records with fields that can be resolved by direct Xenoverse 2 evidence; do not infer numeric Ki costs from other games or mods.


### 2026-09-24 continuation — Neo Wolf Fang Fist P1 provenance enrichment
- [x] Selected **Neo Wolf Fang Fist** as the next P1 enrichment target after the current verification-date census was exhausted.
- [x] Added the dedicated provenance audit and confirmed current Xenoverse 2 evidence for Strike Super classification, PQ86 acquisition, and variable **100–700 Ki** usage. citeturn3search0turn3search1
- [x] Preserved unresolved exact drop probability, frame data, and universal damage measurements; no unsupported Ultimate Finish requirement was inferred.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next partially verified P1 research target with direct Xenoverse 2 evidence; do not manufacture technical measurements.

### 2026-09-24 cycle completion — Boiling Ball + Tricky Strike subtype reconciliation
- [x] Re-read the live handoff, efficiency addendum, and exhaustive TODO before editing; followed the recorded Boiling Ball → Tricky Strike queue.
- [x] Reconciled both unresolved Demigra skills against repository research batch 289 and current Xenoverse 2-specific evidence. **Boiling Ball (ID 541)** is research-supported as a **Super / Ki Blast**; **Tricky Strike (ID 542)** is research-supported as a **Super / Strike**.
- [x] Updated docs/data/skill-research-gaps.json so both records now have only ki_cost unresolved; no CaC acquisition route or numeric cost was invented.
- [x] Updated both dedicated evidence audits to preserve the resolved subtype and explicit unresolved Ki-cost boundary.
- [x] Current external corroboration confirms IDs 541/542, Final Form Demigra ownership, CaC-unavailable status, Super Skill listing, and the documented Demigra behaviors; the Legend Patrol encounter lists both skills on Final Form Demigra.
- [x] Validation: updated JSON files were parsed successfully by the GitHub JSON update path; canonical skill catalogs remain untouched at the established 469/469 boundary.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: 97a09fd5653ef8fd497b202e5059f77e86ffdd09, 16b4c1a5c67429e262c5200260ad1fd6f9a417c9, 617559a481b5dc12033dd3b7a6d6d3025ae7f7ad.
- [ ] **Exact next:** continue the next unresolved thin-domain candidate after Boiling Ball/Tricky Strike, prioritizing a record whose remaining field can be resolved by direct Xenoverse 2 evidence; preserve the 469/469 canonical boundary until the supported builder/runtime is available.

### 2026-09-24 continuation — Energy Boil evidence-boundary pass
- [x] Followed the post-Boiling Ball/Tricky Strike queue and selected **Energy Boil** as the next unresolved thin-domain record.
- [x] Added current external/reference evidence confirming **Energy Boil = Final Form Demigra's Evasive Skill**, including the defensive/teleport/ki-gathering behavior; Xenoverse 2 ID evidence confirms **ID 10540**, CaC-unavailable status, and Final Form Demigra ownership. 
- [x] Strengthened the dedicated Energy Boil evidence audit and central gap ledger.
- [x] Preserved the evidence boundary: `subcategory` and `ki_cost` remain unresolved because the new evidence does not expose a trustworthy canonical XV2 subtype or numeric cost. No subtype was inferred from animation/function wording.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved queue, prioritizing a record where direct Xenoverse 2 evidence can resolve an actual missing field; do not repeat identity-only enrichment unless it materially changes the evidence boundary.

### 2026-09-24 continuation — Boiling Burg class reconciliation
- [x] Selected **Boiling Burg** as the next queue item where direct Xenoverse 2 evidence could resolve a real metadata field.
- [x] Reconciled the short skill ID **540** with long-form ID **5540** and confirmed that the Xenoverse 2 skill-list artifact places **Boiling Burg in the Ultimate Skill section**; the ID list identifies Final Form Demigra as its user and CaC-unavailable status.
- [x] Updated `docs/data/skill-research-batches/unresolved-candidates-287.json` from taxonomy unresolved to class-resolved, while leaving exact subtype and Ki cost unresolved.
- [x] Updated `docs/data/skill-research-gaps.json` with the independent class evidence and retained the no-inference boundary for numeric Ki cost.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the unresolved queue, prioritizing another field that can be directly resolved from Xenoverse 2-specific evidence; do not infer numeric costs from other games or mods.

### 2026-09-24 cycle completion — Energy Boil evidence-boundary refresh
- [x] Re-read the live continuation handoff, efficiency addendum, and exhaustive TODO before selecting the bounded batch.
- [x] Added `docs/data/skill-research-gaps-energy-boil-evidence-boundary-refresh-2026-09-24.json`.
- [x] Reconfirmed Xenoverse 2 ID **10540** / short ID **540**, Final Form Demigra ownership, CaC-unavailable status, and Evasive classification from the current Xenoverse 2 ID list and skills guide; independent Demigra reference corroborates the Evasive role and defensive energy/teleport behavior. Sources: Xenoverse 2 Character ID List; Xenoverse 2 Skills Guide; Demigra reference.
- [x] Preserved the evidence boundary: the accessible sources do not expose the repository's Evasive subcategory or a trustworthy numeric Ki cost, so neither field was inferred.
- [x] Updated `docs/data/skill-research-gaps.json` with the refreshed evidence-boundary note and registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: JSON audit parses; canonical/index baseline remains **469/469** with **0 duplicate IDs**; no canonical promotion or unsupported acquisition route was introduced.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: audit `edc3e89b7b42840e6904a12f0d63f202e45fb769`; registry `2065e1e6bb40a23372cb39521c9b69610e2d4c29`; gap ledger `0d14d81919b5d0d000c4eff2dd670c67be0fa6d9`; changelog `644deb0ae208aeb7c4275ce92615c5583bd080b1`.
- [ ] **Exact next:** continue the remaining unresolved thin-domain queue only where direct Xenoverse 2 evidence can resolve a currently missing canonical field; otherwise return to the source-backed P1 enrichment queue while Savage Strike remains staged for atomic builder integration.


### 2026-09-24 cycle completion — Acid evidence refresh
- [x] Selected **Acid** as the next unresolved thin-domain candidate because only its numeric Ki cost remained missing after Xenoverse 2-specific class/identity reconciliation.
- [x] Added `docs/data/skill-research-gaps-acid-evidence-refresh-2026-09-24.json` and registered it in the cross-domain index.
- [x] Reconfirmed normal Acid **ID 140** versus separate raid Acid **ID 143**, Super classification, CaC-unavailable status, and Saibaman 2 usage from Xenoverse 2-specific references. Sources: Xenoverse 2 Character ID List; Xenoverse 2 Skills Guide; Saibaman reference; CaC-unobtainable skill discussion.
- [x] Preserved the only unresolved canonical field: numeric `ki_cost`. No cost or acquisition route was inferred.
- [x] Canonical skill catalogs remain at the established **469/469** boundary; no unsupported promotion was made.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved thin-domain queue, prioritizing a candidate where direct Xenoverse 2 evidence can resolve an actual missing field rather than merely repeating identity confirmation.
