### 2026-09-25 cycle completion — skill research audit advanced through Batch 322
- [x] Inspected the live research chain after the 470-record current-consumer census and confirmed that the repository already contains bounded 2026-09-25 evidence refresh/reconciliation artifacts through **skill-batch-322**.
- [x] Reviewed Batches **317–322**: 317 (eight Ki Blast Ultimate reconciliations), 318 (Divine-series records), 319 (Divinity Unleashed / Do or Die / Dodon Ray), 320 (Atomic Blast / Bending Kamehameha / Big Bang Attack / Big Bang Kamehameha), 321 (five Ki Blast Supers), and 322 (Death Wave / Murder Grenade).
- [x] Verified the six batch artifacts are valid structured research records with explicit evidence boundaries; unresolved reward probabilities, version-sensitive damage/frame data, and source conflicts remain unasserted.
- [x] Advanced `docs/data/skill-catalog-audit.json` from stale **latest_research_batch 315** to **322** and updated its audit date to 2026-09-25, adding dated reconciliation notes for Batches 317–322.
- [x] Preserved the research-only boundary: no oversized manual reconstruction of `skills.json` / `skills-index.json`, no unsupported canonical promotion, and no invented acquisition probabilities.
- [ ] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** continue the deterministic P1 provenance/research chain after Batch 322, first checking whether a newer evidence artifact already exists before creating a new batch; then reconcile the next stale canonical/research record or cross-domain consumer with direct Xenoverse 2 evidence.
 
### 2026-09-25 cycle completion — 470-record current-scalar census
- [x] Completed the follow-up current-facing scalar census after the six-consumer 469→470 repair.
- [x] Searched the live repository for stale 469 scalar patterns across canonical skill, index, acquisition, and endpoint reports.
- [x] Found **23 files containing 469 references**, all classified as historical/completed-audit material or preserved historical notes; no current projection still asserts 469 as its live baseline.
- [x] Added `docs/data/current-skill-projection-stale-scalar-scan-2026-09-25.json` documenting the 470 baseline, the six reconciled current consumers, the 23 historical hits, and the validation boundary.
- [x] Preserved historical 469 snapshots instead of rewriting audit history.
- [x] No canonical skill identities or relationship edges were changed in this cycle.
- [x] CI remains unverified; no workflow success is claimed.
- [ ] **Exact next:** resume source-backed P1 skill provenance enrichment, using the already-prepared 2026-09-25 evidence refresh batches (312–316) where appropriate; do not promote research-only identities into the canonical layer without the repository's canonical-builder/duplicate/parity validation.
 
### 2026-09-25 cycle completion — current 470-record skill consumer parity repair
- [x] Continued the deterministic producer/consumer parity queue from the previous Time Skip/Tremor Pulse mentor reconciliation.
- [x] Audited current-facing skill consumers against the live **470-record** canonical/index baseline, with **239 PQ-linked** skills and **231 non-PQ** skills.
- [x] Repaired six current-facing consumers that still exposed the superseded 469-record baseline: `docs/data/skill-acquisition-coverage-report.json`, `docs/data/skill-pq-acquisition-presentation-audit.json`, `docs/data/skill-shop-endpoint-layer-audit-2026-09-24.json`, `docs/data/special-acquisition-endpoint-audit-2026-09-24.json`, `docs/data/character-exclusive-skill-endpoint-audit-2026-09-24.json`, and `docs/data/time-rift-story-tournament-endpoint-audit-2026-09-24.json`.
- [x] Synchronized the acquisition coverage report to **470 / 239 / 231** and retained the current mentor resolution at **131 resolved edges / 130 unique targets**, with the typed-reward distinction preserved separately.
- [x] Synchronized current endpoint audits to 470 without changing any acquisition relationships, endpoint IDs, or canonical skill identities.
- [x] Re-parsed all six changed JSON files successfully.
- [x] Checked the latest commit workflow association; no workflow run was exposed for the newest direct commit, so no CI success is claimed.
- [x] Preserved dated 469-record historical/audit snapshots rather than rewriting historical evidence.
- [ ] **Exact next:** continue the deterministic current-facing consumer census for any remaining stale 469/470 scalar, orphan endpoint ID, or one-way navigation mismatch; after the current-consumer scan is clean, resume the next evidence-backed skill/research tranche. Do not rewrite historical snapshots merely because they contain older baselines.
 
### 2026-09-25 cycle completion — Batch 296 acquisition-endpoint enrichment
- [x] Filled four previously-null Batch 296 acquisition endpoints from direct Xenoverse 2 evidence: Giga Boost → Conton City Skill Shop; Holstein Shock → PQ15; Emperor's Sign → TP Medal Shop; Position Shift → Skill Shop after defeating Kid Buu.
- [x] Added and registered the dated acquisition refresh audit.
- [x] Preserved unresolved numeric Ki costs and the 469/469 canonical boundary.
- [ ] CI success remains unverified because failed jobs expose no usable runner/log payload.
- [ ] **Exact next:** continue the next source-backed partially verified skill tranche after Batch 296/297 without inventing a batch identity.
### 2026-09-25 cycle completion — artifact-checker current-tree cleanup and pre-run CI diagnosis
- [x] Removed literal checker-marker names from the continuation history that were themselves being scanned as forbidden artifacts.
- [x] Direct current-tree verification of the handoff is clean for the known checker patterns.
- [x] Latest post-fix Actions still fail Repository quality and Clean internal artifacts before exposing usable runner steps/logs.
- [ ] CI success remains unverified; validators remain unchanged.
- [ ] **Exact next:** inspect the next Actions result; if the same pre-run failure persists, treat the CI blocker as externally unobservable and continue the next deterministic data-quality/content task without weakening validation.

### 2026-09-25 cycle completion — post-cleanup CI verification
- [x] Inspected post-cleanup Actions for HEAD `26c7f897298b0b6a521b9ee82dc27b8216fbde01`; Repository quality and Clean internal artifacts still fail.
- [x] Revalidated the artifact-check contract and directly verified the handoff no longer contains the known internal citation markers.
- [ ] CI success remains unverified because GitHub exposes no runner steps/log payload for the failed jobs.
- [ ] **Exact next:** locate the remaining current-tree artifact causing the checker failure using repository-visible evidence; then continue the next deterministic skill-research batch after Batch 297.

### 2026-09-24 cycle completion — internal-artifact cleanup and CI diagnosis
- [x] Removed detected assistant citation/export artifacts from the continuation history, CHANGELOG, and TP/STP Medal Shop database.
- [x] Kept the artifact checker and cleanup workflow strict; no validator weakening.
- [x] Preserved 469/469 canonical skill/index boundary.
- [ ] CI success remains unverified until a post-cleanup workflow run completes successfully.
- [ ] **Exact next:** inspect post-cleanup Actions results before resuming canonical-builder or further content work.

### 2026-09-24 cycle completion — Skill Research Batch 297 provenance refresh
- [x] Refreshed Batch 297 for Blaster Stream, Brave Heat, Chain Destructo-Disc Barrage, and Circle Flash with current Xenoverse 2 taxonomy, 300 Ki cost, acquisition endpoints, character/DLC provenance, and directly documented mechanics.
- [x] Added and registered `docs/data/skill-batch-297-provenance-refresh-2026-09-24.json`.
- [x] Preserved unresolved Ultimate Finish, drop-probability, exact-frame, and version-sensitive damage fields rather than inferring them.
- [x] Preserved the 469/469 canonical/index boundary; no speculative catalog reconstruction.
- [ ] CI success remains unverified; current commit's Repository quality and Wiki data audit failed, while Clean internal artifacts was cancelled.
- [ ] **Exact next:** continue the next deterministic skill-research tranche after Batch 297; do not invent a new batch identity or manually promote records without the supported builder/runtime.

### 2026-09-24 cycle completion — Dragon Burn P1 provenance verification
- [x] Completed **skill-batch-196 — Dragon Burn** with **Evasive / Ki Blast** classification and separate Counter Skill taxonomy.
- [x] Confirmed **200 Stamina**, Future Warrior usability, Nuova Shenron provenance, and GT Pack 2 association.
- [x] Revalidated **PQ82 — Ultimate Brotherly Battle** as the acquisition quest.
- [x] Preserved **Ultimate Finish requirement as unresolved** rather than inventing a condition.
- [x] Strengthened counter mechanics: attackers during the active stance are paralyzed and burned for about three seconds.
- [x] Added and registered `docs/data/skill-dragon-burn-p1-provenance-verification-2026-09-24.json`.
- [x] Preserved unresolved Ki cost, exact active frames/hitboxes, drop probability, and version-sensitive damage.
- [x] Preserved the **469/469** canonical boundary; no unsupported canonical promotion was made.
- [ ] CI success remains unverified.
- [ ] **Exact next:** inspect current Actions state, then continue **skill-batch-197**.

### 2026-09-24 cycle completion — Rough Ranger P1 provenance verification
- [x] Completed **skill-batch-195 — Rough Ranger** with Xenoverse 2 **Super / Strike / Universal Counter** classification, **100 Ki**, Android 17 (DB Super) association, and Extra Pack 2 provenance.
- [x] Revalidated **PQ119 — A Ranger's Duty** as the acquisition quest and preserved the repository-supported **Ultimate Finish** interpretation.
- [x] Recorded the source discrepancy: a Steam PQ guide displays Rough Ranger in the reward set without the UF annotation, while Dragon Ball Wiki explicitly states Future Warrior acquisition after Ultimate Finish; existing repository audit/history also preserves the UF interpretation.
- [x] Strengthened mechanics evidence for the Strike/basic kick response, Ki-based barrier response, and point-blank Ki Blast exception.
- [x] Added and registered `docs/data/skill-rough-ranger-p1-provenance-verification-2026-09-24.json`.
- [x] Preserved unresolved stamina cost, exact frame/hitbox data, drop probability, and version-sensitive damage fields.
- [x] Preserved the **469/469** canonical skill/index boundary; no unsupported canonical promotion was made.
- [x] Inspected current Actions state: the newest push-triggered **Repository quality** and **Wiki data audit** runs for the current commit are queued; the immediately preceding Repository quality run failed. No CI success is claimed yet.
- [ ] **Exact next:** continue **skill-batch-196** after checking the resulting Actions state.

### 2026-09-24 cycle completion — Sudden Death Beam P1 provenance verification
- [x] Completed **skill-batch-194 — Sudden Death Beam** with Xenoverse 2 **Super / Ki Blast / Counter Skill** classification, Goku Black (Super Saiyan Rosé) association, Super Pack 3 provenance, and Future Warrior usability.
- [x] Revalidated current acquisition routes: **TP Medal Shop / STP Medal Shop / Double Crystal Raid Battle**.
- [x] Preserved the distinction between the historical **170 TP Medal shop price** and the unresolved in-combat Ki cost.
- [x] Strengthened universal-counter mechanics evidence: the documented trigger covers basic, Strike, or Ki Blast attacks; triggered activation teleports behind the opponent and fires a Ki Wave.
- [x] Added and registered `docs/data/skill-sudden-death-beam-p1-provenance-verification-2026-09-24.json`.
- [x] Preserved unresolved Ki/stamina cost, exact frame/hitbox, drop probability, and version-sensitive damage fields.
- [x] Preserved the **469/469** canonical skill/index boundary; no unsupported canonical promotion was made.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** inspect current Actions state, then continue **skill-batch-195** using the same bounded P1 provenance workflow.

### 2026-09-24 cycle completion — Change The Future P1 provenance verification
- [x] Completed **skill-batch-193 — Change The Future** with Xenoverse 2 **Super / Ki Blast / Counter Skill** classification, **100 Ki**, Future Warrior availability, and **PQ43 — Change the Future** acquisition.
- [x] Confirmed the skill is a **Basic Reward** on PQ43; no Ultimate Finish requirement was invented.
- [x] Added and registered `docs/data/skill-change-the-future-p1-provenance-verification-2026-09-24.json`.
- [x] Preserved the documented distinction between the actual Ki Blast counter trigger and the in-game description's Strike wording.
- [x] Preserved unresolved stamina, exact frame/hitbox, drop probability, and version-sensitive damage fields.
- [x] Preserved the **469/469** canonical skill/index boundary; no unsupported canonical promotion was made.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** inspect current Actions state, then continue **skill-batch-194** using the same bounded P1 provenance workflow.

### 2026-09-24 cycle completion — Counter Burst P1 provenance verification
- [x] Completed **skill-batch-192 — Counter Burst** with Xenoverse 2 identity, **Super / Ki Blast / Counter Skill** classification, **100 Ki**, Future Warrior usability, and **PQ75 — Room to Spare** acquisition provenance.
- [x] Confirmed Counter Burst is a **Basic Reward** on PQ75, so no Ultimate Finish requirement is asserted.
- [x] Added and registered `docs/data/skill-counter-burst-p1-provenance-verification-2026-09-24.json`.
- [x] Strengthened mechanics evidence for the barrier-triggered counter and six-hit Ki projectile; retained the approximately 20% figure only as contextual evidence.
- [x] Preserved unresolved stamina cost, exact frame/hitbox data, drop probability, and version-sensitive numeric damage fields.
- [x] Preserved the **469/469** canonical skill/index boundary; no unsupported canonical promotion was made because the supported builder/runtime remains unavailable.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** inspect the current Actions state, then continue **skill-batch-193** using the same bounded P1 provenance workflow.

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

### 2026-09-24 completion — post-fix Repository quality result
- [x] Commit 4922ff3a4ba0834f09025ab6098470535c024732 cleaned the two directly confirmed documentation offenders and pushed successfully to main.
- [x] Repository quality run 36073285532 and Clean internal artifacts run 36073285492 both failed immediately after the push.
- [x] Job IDs are available, but the Actions API exposes no step data and job-log downloads return BlobNotFound; the exact failing stage/path therefore remains unverified.
- [x] Direct validation of the two edited documentation files finds zero checker-marker strings/delimiters.
- [ ] CI success remains unverified.
- [ ] **Next:** inspect future Actions/check-run metadata for usable failure details without weakening the checker; meanwhile keep canonical skill data at 469/469 and continue only evidence-backed work that does not depend on the unavailable builder runtime.

### 2026-09-24 completed — deterministic repository artifact scan
- [x] Enumerated the exact current main Git tree: 1,300 tracked tree entries / 1,297 text-candidate files.
- [x] Confirmed the remaining current-tree artifact-check offenders were literal checker-marker names preserved in the handoff/TODO history, not gameplay or research data.
- [x] Cleaned those two tracked documentation files using the repository's existing cleaner semantics.
- [x] Re-fetched both edited files and verified 0 remaining checker-marker strings/delimiters in them.
- [ ] CI has not yet been rerun after this fix; no success is claimed.
- [ ] Next: inspect the next Repository quality result; if successful, resume Savage Strike canonical integration through the supported builder. Otherwise diagnose the new exact failure before further edits.
### 2026-09-24 completed/ongoing artifact-check investigation
- [x] Repository quality attempt 2 completed with failure at `Check for internal artifacts`.
- [x] Checked the live checker and repository search for its forbidden marker classes; no indexed ``/`` matches remain.
- [x] CI job logs are unavailable through the current GitHub API response (`BlobNotFound`), preventing reliable identification of the failing tracked path.
- [x] Checker semantics were not weakened and no false CI success was recorded.
- [ ] **Next:** perform a deterministic full-tree scan from the exact checkout or obtain usable job logs, then remove only the confirmed offending artifact.

### 2026-09-24 completed repository artifact cleanup — CI recovery
- [x] Investigated the repeated Repository quality artifact-check failure and inspected the repository's checker/cleaner contract.
- [x] Removed residual internal citation/export markers from the affected tracked documentation/research files.
- [x] Re-fetched the affected files from `main` and verified the targeted set has **0** forbidden citation markers.
- [x] Re-ran Repository quality run `36072900893`; attempt **2** is queued.
- [ ] CI remains pending until that attempt completes successfully.
- [ ] **Next:** poll the rerun; if it fails, identify the remaining current-tree artifact before making further edits.

### 2026-09-24 completed/ongoing CI execution recovery — Repository quality rerun
- [x] Inspected the latest Repository quality workflow run (`36072545830`), which failed at `Check for internal artifacts`.
- [x] Used the available Actions permission to re-run the failed jobs; attempt **2** is queued.
- [ ] Do not mark CI as passed until the rerun reaches a completed successful conclusion.
- [x] No canonical skill catalog reconstruction or unsupported preset/loadout mapping was performed.
- [ ] **Next:** poll the rerun and act on its actual result; continue preserving direct-evidence gates.

### 2026-09-24 completed numeric preset evidence recheck — Goku/Vegeta/Captain Ginyu
- [x] Rechecked two independent dated Burcol preset-unlock artifacts and the current Xenoverse 2 Goku in-game-data page.
- [x] Strengthened numeric-identity corroboration for the unresolved Goku/Vegeta/Captain Ginyu preset records.
- [x] Confirmed the named Goku loadout table exposes complete eight-slot configurations, but it does not directly bind those rows to the repository's numeric preset IDs.
- [x] Preserved the promotion gate: **0** numeric-to-complete-loadout bindings were promoted; no row-order, costume-order, or chapter-order inference was used.
- [x] Updated `docs/data/numeric-preset-complete-loadout-source-audit-2026-09-24.json`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** find an artifact that displays the numeric preset identifier and complete eight-slot configuration together; otherwise move to the next highest-impact thin research domain without inventing bindings.

### 2026-09-24 completed global navigation audit reconciliation
- [x] Re-inspected both live layouts after the prior navigation migration.
- [x] Confirmed `docs/_layouts/home.html` and `docs/_layouts/wiki.html` both already target `/Parallel-Quests-All/`; the prior audit's "home navigation not changed" note was stale.
- [x] Reconciled `docs/data/global-navigation-canonical-explorer-audit-2026-09-24-c.json` with the live layout state.
- [x] Confirmed Expert Missions remains `/Expert-Missions/` because no canonical Expert Missions explorer exists.
- [x] No gameplay, acquisition, identity, or relationship data changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue the highest-impact exhaustive preset/loadout evidence tranche, requiring a direct numeric-preset-to-complete-loadout binding before promotion.

### 2026-09-24 completed bounded skill P1 provenance enrichment — PQ61–PQ70 tranche
- [x] Added `docs/data/skill-p1-provenance-enrichment-2026-09-24-recoome-pq61-batch.json` covering Fighting Pose H, Teleporting Vanishing Ball, Ill Rain, Scissors Paper Rock, Super God Fist, Angry Shout, Headshot, and Emperor's Blast.
- [x] Strengthened source-backed classification, resource cost, acquisition endpoint, and directly documented mechanics fields without promoting reward probabilities, Ultimate-Finish requirements, or unsupported numeric combat data.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved canonical/index parity: no oversized canonical catalog was manually reconstructed or changed in this runtime-limited cycle.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next evidence-backed thin skill tranche from the existing research corpus, then run the standard canonical builder when repository-backed execution is available; validate canonical/index parity and downstream acquisition projections after builder execution.

### 2026-09-24 completed raid/event Super Soul audit synchronization
- [x] Re-fetched the live `docs/data/super-soul-raid-event-presentation-consumer-audit-2026-09-24.json` after the presentation repair and found its own top-level coverage fields were stale (**12 surfaced / 25 missing**) despite the consumer table being repaired.
- [x] Synchronized the audit to the live consumer: **37 surfaced / 0 missing / 0 missing-record entries / pass**, with `consumer_rows_after_repair=37`.
- [x] Preserved the audit's evidence boundary and did not add availability, recurrence, probability, or guarantee claims.
- [x] Commit: `0ec61d1094d6732b8580ef6ae65fa2bed817929e`.
- [ ] **Next:** continue deterministic Event/Raid/Festival/Chapter 4 consumer scanning for stale self-reported audit metadata, one-way navigation, orphan targets, and canonical-ID drift; then resume the highest-impact source-backed preset/loadout tranche.


### 2026-09-24 completed live character count reconciliation
- [x] Recomputed the canonical character producer directly from `docs/data/characters-record-layer.json`: **152** names.
- [x] Corrected current-facing character/navigation consumers that had drifted to **153**.
- [x] Confirmed both Chapter 4 publisher-confirmed identities are present; no unsupported 153rd identity was invented.
- [x] Preserved earlier 153 claims as historical context rather than rewriting the handoff history.
- [ ] **Next:** continue event/raid/Festival/Chapter 4 consumer scanning from the corrected 152-character baseline, then resume exhaustive preset/loadout research.

### 2026-09-24 completed Future Saga Chapter 4 presentation consumer audit
- [x] Added `docs/data/future-saga-chapter-4-presentation-consumer-audit-2026-09-24.json`.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Verified current Chapter 4 presentation parity for 1 Extra Mission, 2 PQs, 4 moves/1 Awoken, 6 costumes/accessories, 4 Super Souls, and 8 loading-screen illustrations.
- [x] Preserved explicit unresolved states for individual mission/reward/item/battle/gallery details; no unsupported facts were promoted.
- [ ] **Next:** scan remaining event/raid/Festival/Chapter 4 consumers for stale scalars and one-way navigation; then start the next exhaustive preset/loadout research tranche if the deterministic scan is clean.

### 2026-09-24 completed Festival audit registry cleanup
- [x] Registered the existing Festival skill-character presentation audit in docs/data/pq-cross-domain-index.json.
- [x] Added the registry synchronization to CHANGELOG.md.
- [x] Confirmed no canonical relationship or gameplay data changed.
- [ ] **Next:** continue deterministic event/raid/Festival/Chapter 4 consumer scanning, then resume exhaustive preset/loadout research.
### 2026-09-24 completed current character/equipment/raid consumer synchronization
- [x] Re-scanned current-facing non-PQ consumers after Chapter 4 character and final raid-accessory identity reconciliation.
- [x] Repaired stale current projections from **151 → 153 characters**, **465 → 469 skills**, **173 → 174 equipment/accessory records**, and **9 → 11 raid accessory identities**.
- [x] Updated current DLC character navigation from **14/15 resolved + 1 unresolved** to **15/15 resolved + 0 unresolved** after exact Chapter 4 identity reconciliation.
- [x] Added and registered `docs/data/current-character-equipment-raid-consumer-synchronization-2026-09-24.json`.
- [x] Preserved historical dated snapshots; no relationship edge, acquisition route, preset, raid availability, probability, or gameplay fact was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** continue deterministic current-facing event/raid/Festival and remaining character/preset/navigation consumer scanning for stale scalars, one-way navigation, orphan targets, and canonical-ID drift; then resume the highest-impact thin-domain source-backed expansion.

### 2026-09-24 completed Future Saga Chapter 4 character identity presentation repair
- [x] Added publisher-confirmed `Supreme Kai of Time (Ultra Supervillain)` and `Goku (Ultra Supervillain Quelled)` as distinct canonical character identities.
- [x] Updated Character Encyclopedia/current explorer counts from 151 to 153.
- [x] Resolved the previously unresolved Supreme Kai of Time Chapter 4 DLC identity bridge entry; DLC headline-character identity audit is now clean.
- [x] Updated Chapter 4 DLC presentation links to the canonical character search surface.
- [x] Preserved the evidence boundary: no preset, unlock, raid, PQ, or gameplay relationships were inferred.
- [ ] **Next:** scan event/raid/Festival/Chapter 4 presentation consumers and stale scalar assertions.

### 2026-09-24 completed residual accessory homepage consumer repair
- [x] Re-scanned current-facing accessory count consumers.
- [x] Corrected `docs/index.md` from stale **53 / 37** accessory counts to the live **51 / 116** shop/canonical counts.
- [x] Preserved historical counts in research/audit history.
- [ ] **Next:** continue deterministic consumer scanning for uncovered character/preset and event/raid-linked presentation drift.

### 2026-09-24 completed canonical farming presentation consumer
- [x] Added canonical `pq_farming_route` loading/rendering to `docs/Parallel-Quests-All.html`.
- [x] Added and registered `docs/data/farming/pq-farming-presentation-consumer-audit-2026-09-24.json`.
- [x] Validated all **7** canonical farming edges and their reverse/index parity: Dragon Balls via PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88; 0 unresolved, 0 orphan reverse records, 0 duplicate PQ edges.
- [x] Preserved the farming evidence boundary: relationship identity does not imply guarantee, drop probability, route efficiency, or Ultimate Finish requirements.
- [ ] **Next:** continue deterministic non-PQ/cross-domain presentation consumer scanning, prioritizing uncovered character/preset and event/raid consumers for stale scalars, one-way navigation, orphan targets, and canonical identity drift.

### 2026-09-24 completed skill verification queue
- [x] Confirmed the Power Pole Pro → Purification provenance tranche had already been completed in `docs/data/skill-provenance-audit-2026-09-24-present-through-purification.json`.
- [x] Verified live skill census: **469 canonical / 469 index / 469 current / 0 stale / 0 duplicate IDs**.
- [x] Preserved all acquisition/reward/restriction uncertainty boundaries; no unsupported mechanics or probabilities introduced.
- [x] Closed the current skill `last_verified` metadata queue.
- [ ] **Next:** resume the P1 exhaustive-coverage audit of thin wiki systems/pages, prioritizing the next under-documented structured domain from the live TODO/handoff and preserving canonical cross-domain navigation.

### 2026-09-24 completed deterministic non-PQ accessory consumer reconciliation
- [x] Audited `docs/Equipment-All.html` against the current equipment/accessory and PQ relationship producers after the 2026-09-24 raid accessory identity reconciliation.
- [x] Added `docs/data/accessory-presentation-consumer-current-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validated the current presentation baseline: **174 combined equipment/accessory records / 116 current canonical accessory identities / 124 PQ→equipment edges / 122 unique PQ equipment targets / 9 resolved raid identities / 18 resolved raid-gift bridge records**.
- [x] Confirmed the explorer derives its displayed record count from the live canonical record layer and its PQ navigation from the authoritative relationship layer; no hard-coded stale accessory total is present.
- [x] Corrected stale current-facing dashboard/documentation counts: `docs/Accessory-Canonical-Database.md` 88 → 116 canonical reconciliation identities; `docs/index.md` Accessory Shop 53 → 51 and canonical accessories 37 → 116.
- [x] Preserved the separate 74-record legacy `acc-###` PQ accessory projection and did not merge it into the 116-record `accr-###` reconciliation namespace.
- [x] No new relationship or acquisition fact was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** continue deterministic post-accessory non-PQ consumer scanning for current-facing equipment/raid/event or character/preset stale counts, orphan targets, one-way navigation, and canonical-ID drift.

### 2026-09-24 cycle update — Masenko through Petrifying Spit

- Completed the next bounded P1 provenance batch: 12 records — Masenko, Maximum Charge, Meditation, Menacing Flare, Murder Grenade, Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, Perfect Shot, and Petrifying Spit.
- Synchronized docs/data/skills.json and docs/data/skills-index.json; all 12 now have last_verified=2026-09-24.
- Validation: 469 canonical / 469 index / 0 duplicate IDs / 0 canonical-index identity or verification-date mismatches.
- Refreshed docs/data/skill-stale-metadata-census-2026-09-24.json: 311 current / 158 stale.
- Existing evidence boundaries were preserved. Current sources support the maintained acquisition endpoints; no unsupported mechanics or probabilities were introduced.
- Exact next stale alphabetical batch: Phantom Fist; Photon Swipe; Potential Unleashed; Power Blitz; Power Impact; Power Pole Combo; Power Pole Pro; Power Rush; Power Wall; Powered Shell; Prelude to Destruction; Prepare to be Punished.
- CI remains unavailable; no CI success claimed.

### 2026-09-24 cycle update — Ki Explosion through Majin Kamehameha

- Completed the next bounded P1 provenance batch: 12 records — Ki Explosion, Kill Driver, Last Emperor, Light Grenade, Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Dash, Mach Punch, Maiden Blast, Maiden Burst, and Majin Kamehameha.
- Synchronized docs/data/skills.json and docs/data/skills-index.json; all 12 now have last_verified=2026-09-24.
- Validation: 469 canonical / 469 index / 0 duplicate IDs / 0 canonical-index identity or verification-date mismatches.
- Refreshed docs/data/skill-stale-metadata-census-2026-09-24.json; current live count is 299 current / 170 stale.
- No unsupported mechanics or acquisition claims were added; existing evidence boundaries remain intact.
- Exact next stale alphabetical batch: Masenko; Maximum Charge; Meditation; Menacing Flare; Murder Grenade; Orin Combo; Paralysis; Paralyze Beam; Pendulum Bullet; Perfect Kamehameha; Perfect Shot; Petrifying Spit.
- CI remains unavailable; no CI success claimed.

### 2026-09-24 cycle update — Justice through Ki Blast Thrust skill provenance refresh

- Completed the next bounded P1 provenance batch: **12 skill records** — Justice Blade, Justice Combination, Justice Drive, Justice Kick, Justice Pose, Justice Rush, Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, and Ki Blast Thrust.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 now carry `last_verified=2026-09-24`.
- Added and registered `docs/data/skill-provenance-audit-2026-09-24-justice-through-ki-blast-thrust.json`.
- Refreshed the live verification-date census: **469 canonical / 469 index / 287 current / 182 stale / 0 duplicate IDs**.
- Preserved existing acquisition endpoints, reward semantics, restrictions, mechanics, DLC/update provenance, and source-conflict boundaries. No unsupported drop probabilities, Ultimate Finish gates, timers, damage values, stacking caps, or narrower restrictions were introduced.
- CI/runtime remains unavailable; no CI success claimed.
- Commits: canonical `7fc97d71e4a770f42eea7df61589d2e397dbb3fa`; index `6ab56967dbec64cf78e149c2d3faca40a374f051`; audit `e6f8d0eb95ac24fe6b70592f8365a67388a99179`; census `bf4284d0c2eb726f95f8aa1c63d28464ee4aab10`; cross-domain registration `06f1ebc6a32b710a9a6bb8f8bec577989f2e40ba`.
- **Exact next batch:** Ki Explosion; Kill Driver; Last Emperor; Light Grenade; Lightning Impact; Lightning of Absolution; Lovely Cyclone; Mach Dash; Mach Punch; Maiden Blast; Maiden Burst; Majin Kamehameha.

### 2026-09-24 cycle update — Atomic through Blaster skill provenance refresh + final 854-baseline consumer classification

- Completed the next bounded P1 provenance batch: **12 skill records** — Atomic Blast, Audacious Laugh, Beast, Become Giant, Bending Kamehameha, Big Bang Attack, Big Bang Kamehameha, Big Bang Knuckle, Blades of Judgment, Blaster Ball, Blaster Bomb, and Blaster Cannon.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 now carry `last_verified=2026-09-24`.
- Added and registered `docs/data/skill-provenance-audit-2026-09-24-atomic-through-blaster.json`.
- Added and registered the live verification-date census `docs/data/skill-stale-metadata-census-2026-09-24.json`: **465 canonical / 465 index / 36 current on 2026-09-24 / 429 stale / 0 duplicate IDs**.
- Completed the final active-consumer search for superseded **854 / 146 / 143** PQ relationship assertions. Remaining occurrences are explicitly historical/superseded audit context or mixed historical sections whose live fields already use **853 / 145 / 142**; no live relationship array required rewriting.
- Added and registered `docs/data/pq-current-consumer-854-search-classification-2026-09-24.json`.
- Preserved all historical counts and evidence boundaries; no unsupported acquisition probability, Ultimate Finish gate, timer, damage value, stacking cap, or narrower restriction was introduced.
- CI/runtime remains unavailable; no CI success claimed.
- Commits: canonical skill refresh `657df5ff9d03b57473ceffd02456ed82b5ed9ffb`; index refresh `729714efd384c6319cd592e53357de5d064d820c`; provenance audit `b5021782f77119f5ac6b81d71b64bc74838d2280`; census `39b5593c8b7e82f2fed6bcd2d2d3c7448ca237af`; consumer classification `c69d0b1d33e03dc43226f027f959042bc643aa39`; cross-domain index registration `82dea5332a5e4e6fce66b05390ada57ff575f395`.
- **Exact next batch:** Blaster Meteor; Blaster Shell; Blaster Stream; Blazing Attack; Bloody Counter; Blue Hurricane; Bluff Kamehameha; Body Change; Bomber DX; Brave Heat; Brave Sword Attack; Brave Sword Slash.

### 2026-09-24 cycle update — P1 Meteor/One-Handed and Absolute Zero/Assault Vanish provenance refresh

- Completed two bounded P1 provenance batches: **24 skill records** across Meteor Blow → One-Handed Kamehameha mk.II and Absolute Zero → Assault Vanish.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 24 now carry `last_verified=2026-09-24`.
- Added and registered:
  - `docs/data/skill-provenance-audit-2026-09-24-meteor-through-one-handed.json`
  - `docs/data/skill-provenance-audit-2026-09-24-absolute-zero-through-assault-vanish.json`
- Preserved existing acquisition endpoints, reward semantics, restrictions, mechanics, and evidence boundaries. No unsupported probabilities, gates, timers, damage values, stacking caps, or narrower restrictions were introduced.
- The current canonical/index baseline remains **465 / 465**. The remaining date-based provenance queue is 429 records after these two batches.
- **Exact next batch:** Atomic Blast; Audacious Laugh; Beast; Become Giant; Bending Kamehameha; Big Bang Attack; Big Bang Kamehameha; Big Bang Knuckle; Blades of Judgment; Blaster Ball; Blaster Bomb; Blaster Cannon.
- CI/runtime remains unavailable; no CI success claimed.

### 2026-09-24 cycle update — Acquisition coverage legacy-projection normalization

- Audited remaining current-looking skill-count consumers and found `docs/data/skill-acquisition-coverage-report.json` still exposed an obsolete top-level **305 / 234 / 71** projection while its newer 465-record projection was nested.
- Promoted the live **465 canonical / 239 PQ-linked / 226 without PQ** baseline to the report's primary fields.
- Preserved the obsolete projection and detailed category ID lists under `legacy_projection_2026_09_23`; no historical evidence was deleted.
- Added explicit current endpoint-layer counts while documenting that those layers are overlapping edge/consumer counts, not a disjoint partition of the 226 unique non-PQ skills.
- Validation: live skill baseline remains 465 canonical/index records, 239 PQ-linked, 226 without PQ, 131 mentor-linked skill targets, and 95 non-PQ/non-mentor endpoint targets.
- **Exact next task:** continue searching current-facing data consumers for obsolete skill/domain projections; after consumer normalization, resume bounded source-backed provenance work across the 95 non-PQ/non-mentor endpoint targets.

### 2026-09-24 cycle update — Current 465-skill baseline consumer synchronization

- [x] Reconciled `docs/data/skill-acquisition-coverage-report.json` to the live **465 canonical / 239 PQ-linked / 226 without PQ / 131 mentor-linked / 95 non-PQ/non-mentor** skill baseline.
- [x] Reconciled the live stale-metadata census to **465 canonical / 465 index / 465 current / 0 stale / 0 duplicate IDs** after Expert Mission index promotion.
- [x] Added and registered `docs/data/skill-current-baseline-consumer-synchronization-2026-09-24.json`.
- [x] Preserved historical 455-record counts; no canonical skill identities or acquisition relationships were changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** search remaining current-looking consumers for superseded skill/domain counts, repair only live assertions, then continue bounded source-backed provenance work across the 95 non-PQ/non-mentor endpoint targets.

### 2026-09-23 cycle update — Residual accessory domain-resolution synchronization

- Completed the deterministic residual accessory reconciliation for **Resistance Helmet (PQ111 / equip-135)** and **Gine (DB Super)'s Accessory (PQ144 / equip-050)**.
- These were already established as canonical **equipment/accessory-domain** identities; synchronized the residual backlog and bridge to explicit domain_resolved states rather than creating duplicate acc-### identities.
- Preserved the dedicated accessory graph at **32 forward / 32 reverse** edges and the remaining inventory-identity research backlog at **14** genuinely unresolved records.
- Added and registered docs/data/accessory-domain-resolution-sync-2026-09-23.json.
- Validation target: **45 research records / 74 canonical accessory identities / 29 dedicated acc matches / 2 equipment-domain resolutions / 14 unresolved inventory identities / 0 duplicate accessory edges / 0 stale endpoints**.
- CI/runtime remains unavailable; no CI success claimed.
- **Exact next task:** recompute the broader post-skill-queue cross-domain census, then prioritize the next highest-impact unresolved identity/projection gap; do not reopen resolved accessory-domain cases.

### 2026-09-23 cycle update — Lightning through Menacing skill provenance refresh

- Completed the next P1 stale-skill batch: **12 records** — Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Dash, Mach Punch, Maiden Blast, Maiden Burst, Majin Kamehameha, Masenko, Maximum Charge, Meditation, and Menacing Flare.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json` with `last_verified=2026-09-23`; existing evidence, reward-tier conflicts, restrictions, and update/DLC provenance were preserved.
- Added and registered `docs/data/skill-provenance-audit-2026-09-23-lightning-through-menacing.json`.
- Refreshed the live skill census: **455 canonical / 283 current / 172 stale / 0 duplicate IDs**.
- Exact next stale batch: **Meteor Blow, Meteor Burst, Meteor Crash, Meteor Explosion, Meteor Strike, Mighty Explosive Wave, Milky Cannon, Mystic Flash, Namek Finger, Neo Tri-Beam, Neo Wolf Fang Fist, and One-Handed Kamehameha mk.II**.
- Evidence boundary preserved: this verification pass did not infer unsupported probabilities, gates, timers, stacking caps, or restrictions.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: process the 12 listed Meteor/Mighty/Milky/Mystic/Namek/Neo/One-Handed records, synchronize canonical/index layers, add/register the bounded audit, and recompute the stale census.

### 2026-09-23 cycle update — Justice through Light skill provenance refresh

- Completed the next P1 stale-skill batch: **12 records** — Justice Pose, Justice Rush, Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, Ki Blast Thrust, Ki Explosion, Kill Driver, Last Emperor, and Light Grenade.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json` with `last_verified=2026-09-23` while preserving existing evidence, acquisition, mechanics, DLC/roster, restriction, reward-tier, and source-conflict semantics.
- Added and registered `docs/data/skill-provenance-audit-2026-09-23-justice-through-light.json` in the cross-domain index.
- Refreshed the live skill census: **455 canonical / 271 current / 184 stale / 0 duplicate IDs**.
- Exact next stale batch: **Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Dash, Mach Punch, Maiden Blast, Maiden Burst, Majin Kamehameha, Masenko, Maximum Charge, Meditation, and Menacing Flare**.
- Evidence boundary preserved: verification refresh does not itself establish unsupported mechanics or acquisition conditions.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: process the 12 listed Lightning/Mach/Maiden/Majin/Masenko/Maximum/Meditation/Menacing records against their maintained evidence corpus, synchronize canonical/index layers, add/register the bounded audit, and recompute the stale census.

### 2026-09-23 cycle update — Innocence through Justice skill provenance refresh

- Completed the next P1 stale-skill batch: **12 records** — Innocence Breath, Innocence Bullet, Innocence Cannon, Instant Charge, Instant Rise, Instant Severance, Instant Transmission, Jumping Energy Wave, Justice Blade, Justice Combination, Justice Drive, and Justice Kick.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json` with `last_verified=2026-09-23` for all 12 records while preserving evidence-bounded acquisition, mechanics, DLC/roster, restriction, reward-tier, and conflict semantics.
- Added `docs/data/skill-provenance-audit-2026-09-23-innocence-through-justice.json`.
- Refreshed the live skill census: **455 canonical / 259 current / 196 stale / 0 duplicate IDs**.
- Exact next stale batch: **Justice Pose, Justice Rush, Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, Ki Blast Thrust, Ki Explosion, Kill Driver, Last Emperor, and Light Grenade**.
- Evidence boundary preserved: verification refresh does not itself establish unsupported mechanics or acquisition conditions.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: process the 12 listed Justice/Kai/Kamehameha records, synchronize canonical/index layers, add/register the bounded audit, and recompute the stale census.

### 2026-09-23 cycle update — Hero through Indomitable skill provenance refresh

- Completed the next P1 stale-skill batch: **12 records** — Hero's Flute, Hero's Pose, Heroic Assault, Heroic Counter, Holy Inscription, Holy Wrath, Hyper Tornado, Ill Bomber, Ill Rain, Impact Flare, Impulse Slash, and Indomitable.
- Canonical `docs/data/skills.json` and `docs/data/skills-index.json` were synchronized with `last_verified=2026-09-23` for all 12 records; existing acquisition, reward-tier, mechanics, DLC, roster, restriction, and conflict semantics were preserved.
- Added and registered `docs/data/skill-provenance-audit-2026-09-23-hero-through-indomitable.json`.
- Refreshed the live stale census: **455 canonical / 0 duplicate IDs / 247 current / 208 stale**.
- Exact next stale batch is now **Innocence Breath, Innocence Bullet, Innocence Cannon, Instant Charge, Instant Rise, Instant Severance, Instant Transmission, Jumping Energy Wave, Justice Blade, Justice Combination, Justice Drive, and Justice Kick**.
- Evidence boundary preserved: verification refresh does not itself prove an underlying field correct; no unsupported probability, gate, timer, stacking cap, or restriction was introduced.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: process the 12 listed Justice/Instant/Innocence records against their maintained evidence corpus, synchronize canonical/index layers, add/register the bounded audit, and recompute the stale census.

### 2026-09-23 cycle update — Skill stale-metadata census refresh

- Recomputed the live canonical skill verification-date census after the completed Final-through-Hell-Flash provenance/mechanics batches.
- Current live skill layer: **455 canonical / 0 duplicate IDs / 235 current (2026-09-23) / 220 stale**.
- Refreshed `docs/data/skill-stale-metadata-census-2026-09-23.json` from `docs/data/skills.json`; the previously stale census had still been reporting 280 records.
- The next alphabetical stale batch is now **Hero's Flute, Hero's Pose, Heroic Assault, Heroic Counter, Holy Inscription, Holy Wrath, Hyper Tornado, Ill Bomber, Ill Rain, Impact Flare, Impulse Slash, and Indomitable**.
- Evidence boundary preserved: stale `last_verified` is a priority signal, not evidence that a record is incorrect. No mechanics, acquisition, probability, or restriction fields were inferred in the census-only refresh.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next batch: refresh/research the 12 listed skills against their existing source sets, synchronize canonical/index records, add a bounded audit, and recompute the live stale census.

### 2026-09-23 cycle update — Current PQ consumer baseline correction after Super Soul 158 domain migration

- Live canonical relationship source is now **853 total edges**: 244 skills / 145 Super Souls / 124 equipment / 247 character / 86 DLC / 7 farming; Super Soul reverse projection is **142** unique targets.
- Completed the active-consumer audit against the post-migration canonical layer and identified deterministic stale wording in the 2026-09-23 current-state consumer census and a validator failure-message typo.
- Corrected the current-state consumer census to reference the live 853/145/142 baseline and changed its finding for the PQ cross-domain status from the superseded 854/146 baseline to the live canonical baseline.
- Corrected `scripts/validate_pq_non_pq_consumer_census.py` so its failure message matches the executable 853-edge assertion.
- Historical 854/146/143 and older 859/151/148/862/860/840 snapshots remain preserved as historical evidence and were not rewritten.
- Validation boundary: canonical relationship arrays were not changed in this correction; no CI success is claimed.
- Exact next task: continue the P1 exhaustive provenance/data queue after the current-consumer baseline is synchronized, prioritizing remaining source-backed acquisition/provenance gaps and maintaining cross-database navigation parity.

### 2026-09-22 cycle update — Super Soul 156/161/166/172 duration reconciliation
- Live census before editing: **234 canonical / 0 duplicate IDs / 102 strict-thin records**.
- Bounded batch: **156, 161, 166, and 172**.
- Research/evidence: maintained exact-name Super Soul catalogue plus Android 16 documentation, historical GameFAQs evidence, player-facing evidence, and Towa's documented Super Soul description.
- Changes: separated always-active effects from one-time/battle-start triggers; recorded persistent KO-stack semantics for 161 and 172 without inventing expiration timers.
- Added/registered audit: `docs/data/super-soul-156-161-166-172-duration-reconciliation-2026-09-22.json`.
- Evidence limits preserved: no unsupported finite timer, acquisition probability, Ultimate-Finish condition, or new stacking cap was inferred.
- Validation: **234 canonical / 0 duplicate IDs / 98 strict-thin records**; target records have all eight census fields; audit registration confirmed.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next batch: recompute the live strict-thin queue and continue the strongest remaining evidence-supported cluster, prioritizing multi-field reductions and preserving 032/034 as evidence boundaries.

## 2026-09-22 — Super Soul 087–095 duration reconciliation

- Reconciled duration semantics for **Super Souls 087–095** using exact-name catalogue evidence plus independent GameFAQs documentation.
- Added documented **5-second** temporary duration for 090 and **30-second** trigger/duration semantics for 093.
- Recorded 091's 30-second later-trigger overwrite behavior and 092's 20-second activation/persistence semantics.
- Added explicit condition-bound, permanent-while-equipped, instantaneous, and end-of-battle semantics where appropriate without inventing unsupported timers.
- Added and registered `docs/data/super-soul-087-095-duration-reconciliation-2026-09-22.json`.
- Refreshed the live census to **234 canonical / 0 duplicate IDs / 102 strict-thin records**.
- No acquisition, reward probability, Ultimate-Finish requirement, or unsupported stacking cap was changed.
- CI/Actions success is not claimed; no successful workflow/check was exposed.

### 2026-09-22 — Super Soul 062/064/067/068 secondary-field reconciliation
- [x] Reconciled documented Limit Burst effects for Super Souls **062, 064, 067, and 068**.
- [x] Added evidence-bounded stacking semantics for **062, 064, and 068** without inventing numeric caps.
- [x] Added persistence/non-finite duration semantics for **067 and 068** without inventing timers.
- [x] Added and registered `docs/data/super-soul-062-064-067-068-secondary-field-reconciliation-2026-09-22.json`.
- [x] Refreshed live strict-thin census: **234 canonical / 0 duplicate IDs / 111 strict-thin**.
- [ ] Continue the next evidence-rich unresolved Super Soul strict-thin cluster; preserve canonical source-of-truth and evidence boundaries.

[object Object]

### 2026-09-21 — Taunt low-source provenance strengthening
- [x] Recomputed the live two-source census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 9 exactly-two-source records**.
- [x] Independently corroborated **Taunt (`skill-taunt`)** as a **PQ45 — Take Back the Dragon Balls!** acquisition using a GameFAQs Q&A.
- [x] Added the GameFAQs source to canonical and index records and refreshed `last_verified` to **2026-09-21**.
- [x] Preserved the existing Basic Reward, PQ45, CaC, 0-Ki Power Up, and no-Ultimate-Finish-only semantics; no unsupported drop probability was inferred.
- [x] Post-write target: **8 exactly-two-source records** with canonical/index source parity.
- [ ] Exact next task: recompute the live two-source census and continue with the next deterministic low-source record after Taunt, verifying acquisition/source semantics before provenance-only strengthening.


### 2026-09-21 — Temporal Holy Ray low-source provenance strengthening
- [x] Recomputed the live low-source sequence after Taunt; **Temporal Holy Ray** was the next deterministic exactly-two-source skill.
- [x] Independently corroborated **Temporal Holy Ray** as a **Conton City Tournament 3 — "Time for the Quarterfinals!"** acquisition using GameFAQs tournament documentation.
- [x] Added the GameFAQs source to canonical and index records and refreshed `last_verified` to **2026-09-21**.
- [x] Preserved existing Free Update 11 provenance and did not infer a drop probability.
- [ ] Exact next task: recompute the live two-source census and continue the next deterministic low-source record after Temporal Holy Ray.


### 2026-09-21 — Thunder Flash low-source provenance strengthening
- [x] Recomputed the live low-source sequence after Temporal Holy Ray; **Thunder Flash** was the next deterministic exactly-two-source skill.
- [x] Independently corroborated **Thunder Flash** as a **PQ146 Basic Reward** using an independent Steam PQ146 record.
- [x] Added the Steam source to canonical and index records and refreshed `last_verified` to **2026-09-21**.
- [x] Preserved Legendary Pack 1 provenance and did not infer a drop probability.
- [ ] Exact next task: recompute the live two-source census and continue the next deterministic low-source record after Thunder Flash.


### 2026-09-22 — Final six exactly-two-source skill provenance batch
- [x] Recomputed the live census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable `ki_cost` / 6 exactly-two-source records**.
- [x] Strengthened **Time Bullet, Timespace Impact, Ultra Instinct, Unrelenting Barrage, Venus Fist, and Victory Rush** with independent third-source evidence.
- [x] Synchronized canonical and index source arrays and refreshed `last_verified` to **2026-09-22**.
- [x] Preserved existing acquisition, DLC/version, Ultimate Finish, and uncertainty semantics; no unsupported drop rate or gate was added.
- [ ] Exact next task: recompute the live skill census and identify the highest-priority structural gap after the exactly-two-source queue reaches zero; prefer relationship/projection drift or a large missing-field cohort over further provenance-only edits.


### 2026-09-22 — Post-provenance structural projection census
- [x] Recomputed the live canonical/index projection census after the final low-source batch: **38 field mismatches** remain across projected fields.
- [x] Confirmed the remaining mismatch families: **33 `notes`**, **2 `mechanics_notes`**, **1 `unlock_method`**, **1 `ultimate_finish_required`**, and **1 `source_quest_or_shop`**.
- [ ] Exact next task: fix the two deterministic **`mechanics_notes`** mismatches for **Assault Vanish** and **Solar Flare** from canonical values, then recompute the full projection census.
- [ ] Subsequent task: reconcile the remaining **33 `notes`** projection mismatches in bounded related groups without overwriting canonical research.


### 2026-09-22 — Skill projection parity completion
- [x] Corrected the two deterministic `mechanics_notes` mismatches for **Assault Vanish** and **Solar Flare**.
- [x] Recomputed the projection census and reconciled the remaining **32 `notes` mismatches** from canonical to index.
- [x] Final skill projection validation: **0 mismatches** across the audited canonical/index projection fields; **452/452** records remain aligned.
- [ ] Exact next task: perform a wider repository consistency census and select the highest-priority unresolved structural gap outside the skill projection layer.


### 2026-09-22 — PQ↔skill endpoint naming repair
- [x] Recomputed the live PQ↔skill relationship census: **245 raw skill-reward mentions / 243 unique resolvable edges / 1 unresolved endpoint / 1 orphaned reverse route**.
- [x] Resolved the deterministic **PQ163 "Giant Cluster" → canonical "Gigantic Cluster"** naming alias in the validator without changing canonical source wording.
- [x] Regenerated the PQ↔skill crosslink report: **244 unique forward edges / 239 reverse endpoints / 0 unresolved / 0 orphaned**.
- [ ] Exact next task: run a wider deterministic cross-database reward/reverse-index consistency census for skills, Super Souls, and equipment.


### 2026-09-22 — Canonical source-of-truth rule
- [x] Established repository-wide rule: **canonical database records are authoritative; verification status is evidence metadata, never a competing source of truth**.
- [x] Added explicit downstream-sync requirements so reports/indexes are regenerated from canonical data rather than external “verified” records.
- [x] Audited current Super Soul relationship layer for endpoint integrity after the recent batch: **160 canonical Super Soul records; 0 duplicate IDs; 0 relationship endpoints outside the canonical ID set**.


### 2026-09-22 — Canonical Super Soul/equipment endpoint expansion and identity cleanup
- [x] Expanded canonical Super Soul records from 160 to 234 unique records by adding 81 previously relationship-only PQ reward endpoints as indexed canonical records; no external verified flag was treated as a source of truth.
- [x] Expanded canonical equipment records from 30 to 140 records by adding 110 previously relationship-only PQ reward endpoints as indexed canonical records.
- [x] Detected and merged 7 duplicate Super Soul canonical identities with the same exact canonical name, retaining the lower existing canonical ID and merging evidence/source/PQ references.
- [x] Regenerated the Super Soul PQ crosslink report directly from canonical records: 140 forward edges, 137 unique reverse target endpoints, 0 unresolved canonical Super Soul endpoints.
- [x] Regenerated the equipment PQ crosslink report directly from canonical records: 124 resolved forward edges, 122 unique reverse target endpoints, 1 unresolved classification endpoint.
- [ ] Resolve the remaining PQ 002 Flying Nimbus!! equipment-vs-Super-Soul classification conflict using canonical evidence before creating or deleting an equipment identity.
- Important: relationship-layer claims are not allowed to manufacture canonical records. Canonical records remain authoritative; verification_status remains evidence metadata only.


### 2026-09-22 — Resolved PQ 002 Flying Nimbus classification conflict
- [x] Verified that PQ 002 `Flying Nimbus!!` is the **Super Soul**, not an equipment reward. The canonical Super Soul record is the authoritative identity.
- [x] Removed the erroneous PQ reward relationship classifying `Flying Nimbus!!` as equipment. No canonical equipment record was deleted because the equipment database did not contain such a record.
- [x] Regenerated the PQ→equipment crosslink report from canonical equipment data: 124 forward edges, 122 unique targets, 0 unresolved endpoints.
- [x] Kept the separate Conton City Flying Nimbus vehicle concept out of the equipment reward relationship; the PQ reward evidence concerns the Super Soul.

### 2026-09-22 — Canonical equipment endpoint parity repair
- [x] Recomputed the live cross-database census and found a structural mismatch: **50 live canonical equipment-accessory records** versus **122 PQ→equipment target endpoints** represented by the relationship report.
- [x] Confirmed the earlier historical claim of a 140-record canonical equipment expansion was not reflected in the live canonical file; did not treat the historical handoff or verification status as a substitute for canonical data.
- [x] Promoted **119 source-backed, previously relationship-only equipment identities** into the canonical equipment-accessory layer.
- [x] Preserved exact-name canonical identities for three overlaps instead of duplicating them: `equip-074 → acc-028`, `equip-080 → acc-001`, and `equip-088 → acc-012`.
- [x] Synchronized the PQ→equipment report so every forward and reverse endpoint resolves to the canonical database.
- [x] Validation: **169 canonical equipment-accessory records / 0 duplicate IDs / 124 forward edges / 122 reverse endpoints / 0 unresolved / 0 broken endpoints / 186 canonical PQs**.
- [x] Canonical-source-of-truth rule preserved: relationship endpoints were promoted only from source-backed evidence already present in the repository; unresolved category, slot, restriction, effect, DLC, and reward-slot fields remain unresolved rather than inferred.
- [ ] Exact next task: enrich **`equip-031`–`equip-040`** with independently verified category/slot, DLC provenance, and directly evidenced restrictions/effects, then re-run canonical endpoint and relationship parity validation.

### 2026-09-22 — Equipment provenance batch `equip-031`–`equip-040`
- [x] Added an independent maintained equipment-catalog provenance source to `equip-031` through `equip-040`.
- [x] Reconciled DLC provenance: `031–032` Extra Pack 2/PQ121; `033–036` Extra Pack 3/PQ123/125/127; `037–039` Extra Pack 4/PQ130/131/132; `040` Ultra Pack 1/PQ133.
- [x] Preserved unresolved reward/drop semantics and unsupported mechanics rather than inferring them.
- [x] Revalidated canonical equipment count and PQ→equipment endpoint parity: 169 records, 0 duplicate IDs, 124 forward, 122 reverse, 0 unresolved, 0 broken endpoints.
- [ ] Exact next task: enrich **`equip-041`–`equip-050`** using the same evidence-boundary rules.

### 2026-09-22 — Equipment provenance batch `equip-041`–`equip-050`
- [x] Added independent provenance to `equip-041` through `equip-050`.
- [x] Classified the 10 records as equipment/accessory from independent item documentation.
- [x] Reconciled DLC provenance: `041–044` Ultra Pack 1/PQ133/135; `045–048` Ultra Pack 2/PQ139/142; `049–050` Legendary Pack 1/PQ144.
- [x] Revalidated canonical equipment count and PQ→equipment endpoint parity: 169 records, 0 duplicate IDs, 124 forward, 122 reverse, 0 unresolved, 0 broken endpoints.
- [ ] Exact next task: enrich **`equip-051`–`equip-060`** using the same canonical-source-of-truth and evidence-boundary rules.

### 2026-09-22 — Equipment provenance batch `equip-051`–`equip-060`
- [x] Added independent maintained equipment-catalog provenance to `equip-051` through `equip-060`.
- [x] Classified the 10 records as equipment/accessory.
- [x] Reconciled DLC provenance: `051` Legendary Pack 1; `052–057` Legendary Pack 2; `058–060` Conton City Vote Pack.
- [x] Revalidated canonical equipment/PQ endpoint parity: 169 records, 0 duplicate IDs, 124 forward, 122 reverse, 0 unresolved, 0 broken endpoints.
- [ ] Exact next task: enrich **`equip-061`–`equip-070`** under canonical-source-of-truth and evidence-boundary rules.

### 2026-09-22 — Equipment provenance batch `equip-061`–`equip-070`
- [x] Added independent maintained equipment-catalog provenance to `equip-061` through `equip-070`.
- [x] Classified the 10 records as equipment/accessory.
- [x] Reconciled DLC provenance: `061` Conton City Vote Pack; `062–064` Hero of Justice Pack 1; `065–069` Hero of Justice Pack 2; `070` base game.
- [x] Revalidated canonical equipment/PQ endpoint parity: 169 records, 0 duplicate IDs, 124 forward, 122 reverse, 0 unresolved, 0 broken endpoints.
- [ ] Exact next task: enrich **`equip-071`–`equip-080`** under canonical-source-of-truth and evidence-boundary rules.

### 2026-09-22 — Equipment provenance batch `equip-071`–`equip-080` range
- [x] Enriched all standalone canonical records present in the requested range: `equip-071`–`equip-073`, `equip-075`–`equip-079`.
- [x] Classified the records as equipment/accessory and added independent maintained equipment-catalog provenance.
- [x] Reconciled provenance as base-game content for PQ27, PQ21/30, PQ31, PQ37, PQ41, PQ45, and PQ59.
- [x] Confirmed `equip-074` and `equip-080` are not separate live canonical identities; existing canonical accessory identities represent those overlaps, so no duplicate records were created.
- [x] Revalidated canonical equipment/PQ endpoint parity: 169 records, 0 duplicate IDs, 124 forward, 122 reverse, 0 unresolved, 0 broken endpoints.
- [ ] Exact next task: enrich **`equip-081`–`equip-090`** under canonical-source-of-truth and evidence-boundary rules.

## 2026-09-22 — Equipment provenance/classification batch equip-081–equip-090

- Recomputed the live canonical equipment/accessory layer before editing: **169 canonical records**.
- Enriched the bounded range with independent evidence: equip-081 Four-Star Dragon Ball Hat (headwear/accessory, base game, PQ5, cosmetic); equip-082 Goku's Turtle Hermit Gi (King Kai) (clothing, base game, PQ8, stat spread corroborated); equip-083 Chiaotzu's Hat (With Collar) (headwear/accessory, base game, PQ9 plus reported Accessory Shop route); equip-084 Piccolo's School Clothes (clothing, base game, PQ49 plus Clothing Shop, stat spread and no-Hands component corroborated); equip-086 Battle Suit (CC) (clothing, base game, PQ61, stat spread corroborated); equip-087 Frieza's Suit (Final Form) (clothing, base game, PQ62, stat spread corroborated); equip-089 Gohan's Gi (Adult) (clothing, base game, PQ65, stat spread corroborated); equip-090 Whis Symbol Gi (clothing, base game, acquisition corrected from the prior PQ66 endpoint to **PQ76** after independent corroboration, stat spread corroborated).
- equip-088 remains a historical normalized endpoint to canonical accessory acc-012 Goku Wig (Super Saiyan) rather than a duplicate canonical identity. Conflicting PQ18/PQ63 evidence is preserved on acc-012.
- equip-085 Mr. Shape Up M was removed from the canonical equipment/accessory layer because independent evidence identifies it as a consumable capsule/material, not equipment. The PQ reward remains source-backed and must be represented in the appropriate item/reward layer rather than as an equipment endpoint.
- Canonical equipment count after the edit: **168**.
- Canonical-source-of-truth rule preserved: verification/projection layers do not override canonical identities.
- Independent evidence used: maintained Steam PQ guide; Fandom equipment catalog; Scribd equipment guide; XVGuide clothing list; GameFAQs; Steam discussion; Dragon Ball Wiki.
- Files changed in this cycle: canonical equipment/accessory record layer and equipment projection layer.
- Relationship report synchronization remains required: remove the equip-085 PQ50 edge and move the equip-090 edge from PQ66 to PQ76. This is the exact remaining generated-artifact repair for this batch.
- Exact next batch after relationship repair: recompute the full PQ↔equipment/Super Soul/skill cross-database census and repair any deterministic endpoint/count drift before starting another provenance-only equipment range.

## 2026-09-22 — PQ reward cross-domain relationship census
- [x] Regenerated `docs/data/pq-equipment-crosslink-report.json` from the canonical equipment layer after the equip-081–090 audit.
- [x] Removed the stale `equip-085` → PQ50 relationship because `equip-085` is not a canonical equipment identity.
- [x] Corrected `equip-090` Whis Symbol Gi from PQ66 to **PQ76** in the equipment relationship report.
- [x] Rebuilt the equipment reverse index from the forward edges so forward/reverse counts remain derived from the same source.
- [x] Cross-domain census checked the four currently generated PQ reward reports: Skills = **244 forward / 239 reverse**, Super Souls = **140 / 137**, Equipment = **123 / 121**, Accessories = **42 reverse**.
- [x] Equipment report now matches the canonical equipment count of **168**, with no broken forward/reverse endpoints reported.
- [x] Preserved the repository rule that canonical records are authoritative and verification status is evidence metadata only.
- [ ] Next structural task: reconcile the generated `pq-reward-relationships.json` forward layer against the four reverse reports and canonical PQ reward fields, then identify any deterministic omissions or stale endpoints before further provenance batches.

## 2026-09-22 — Canonical PQ reward-array reconciliation
- [x] Reconciled canonical PQ `skill_rewards`, `super_soul_rewards`, and `equipment_rewards` against their downstream relationship reports.
- [x] Enriched **56** canonical PQ records with source-backed Super Soul reward entries and **76** canonical PQ records with source-backed equipment reward entries.
- [x] Corrected the deterministic PQ48 reward typo: removed duplicate `Kamekameha` from `skill_rewards` and normalized the reward display to canonical `Kamehameha`.
- [x] Regenerated the Super Soul relationship report from the canonical PQ reward arrays + canonical Super Soul records: **151 forward / 148 reverse / 0 unresolved / 0 broken**.
- [x] Regenerated the Equipment relationship report from the canonical PQ reward arrays + canonical equipment/accessory records: **123 forward / 121 reverse / 0 unresolved / 0 broken**.
- [x] Post-write reconciliation now reports **0 mismatches** for Skills, Super Souls, and Equipment.
- [x] Preserved the canonical-source-of-truth rule: downstream reports are projections of canonical records; verification/source-backed status does not override canonical identities.
- [ ] Next structural task: reconcile the separate accessory relationship layer with the canonical PQ reward model without collapsing accessories into equipment or inventing an `accessory_rewards` field unless the schema contract explicitly requires it.

## 2026-09-22 — PQ accessory relationship-layer reconciliation
- [x] Audited `pq-accessory-crosslink-report.json`, `accessory-pq-canonical-bridge.json`, `accessory-pq-canonical-remaining.json`, and the canonical equipment/accessory identity layer against the cross-link contract.
- [x] Found and removed stale `accr-###` relationship endpoints: those IDs do not exist in the current canonical accessory layer, whose live accessory identities use `acc-###`.
- [x] Reconciled the 8 exact-name matches that have real current canonical accessory identities: Piccolo's Turban, Goku's Wig, Android 19's Hat, Tapion's Sword, Yamcha's Sword, Pan's Bandana, Great Saiyaman Helmet, and Goku Wig (Super Saiyan).
- [x] Rebuilt the PQ accessory report: **8 forward / 8 reverse / 0 stale IDs / 0 duplicate edges**.
- [x] Preserved **37 unresolved research records** instead of inventing accessory identities from clothing/set names or stale historical IDs.
- [x] Refreshed the canonical bridge and unresolved backlog so they now reflect the live canonical accessory layer.
- [x] Kept accessories as a distinct relationship domain; no unsupported `accessory_rewards` field was added to canonical PQ records.
- [ ] Next structural task: expand/reconcile the remaining 37 accessory research leads against independent inventory-level evidence and promote only exact canonical identities into the bridge/report.


## 2026-09-22 — Accessory canonical identity batch: eight early/base-game PQ records
- [x] Recomputed the live canonical accessory census before editing: **58 acc-### accessory identities / 172 total canonical equipment-accessory records**.
- [x] Promoted/reconciled eight previously unresolved accessory research identities: `acc-051` Four-Star Dragon Ball Hat (PQ5), `acc-052` Chiaotzu's Hat (With Collar) (PQ9), `acc-053` Dore's Scouter (PQ27), `acc-054` Great Saiyaman Bandana 1 (PQ51), `acc-055` Great Saiyaman Bandana 2 (PQ53), `acc-056` Jaco's State-of-the-Art Radio (PQ72), `acc-057` Tagoma's Scouter (PQ73), and `acc-058` SSGSS Goku Wig (PQ76 with the legacy PQ66 conflict preserved).
- [x] Normalized four older equipment endpoints to canonical accessory IDs instead of duplicating identities: `equip-081 → acc-051`, `equip-083 → acc-052`, `equip-071 → acc-053`, and `equip-091 → acc-058`.
- [x] Rebuilt the accessory bridge and bidirectional report from canonical IDs: **16 forward / 16 reverse / 29 unresolved / 0 broken / 0 stale canonical endpoint IDs / 0 duplicate accessory edges**.
- [x] Refreshed the unresolved accessory backlog from the bridge; the remaining **29** research leads are preserved without speculative identity creation.
- [x] Updated the accessory canonicalization audit and reader-facing Accessory PQ Database with the new canonical coverage and source-of-truth rule.
- [x] Preserved the repository rule that canonical records are authoritative; `verification_status`, research layers, and legacy projection IDs are evidence/history metadata and do not override canonical identity.
- [x] No `accessory_rewards` field was added to canonical PQ records; accessories remain a distinct cross-link domain.
- [x] Validation: **0 duplicate canonical IDs, 58 canonical accessory IDs, 16 forward accessory edges, 16 reverse edges, 0 invalid bridge targets, 0 broken accessory endpoints**. Equipment relationship report remains **123 forward / 121 reverse** after the four accessory target normalizations.
- [x] Evidence used for the batch included the maintained Steam PQ guide, independent equipment/accessory references, Dragon Ball Wiki references for Dore/Jaco/Scouter identities, GameFAQs/Steam evidence for Tagoma/SSGSS Goku, and an independent PQ51/PQ53 record for Great Saiyaman bandanas.
- [ ] Exact next task: independently reconcile the remaining **29** accessory research leads in bounded groups of 8–20, prioritizing the earliest unresolved base-game/DLC identities where strong inventory-level evidence can establish an exact canonical match. Do not create a new canonical accessory solely from a stale `accr-###` ID or a clothing/set/component label.


## 2026-09-22 — Accessory canonical identity batch: six legacy equipment endpoints
- [x] Reconciled six previously unresolved accessory research identities against existing canonical inventory records: `acc-059` Bulma (Kid) Wig (PQ149), `acc-060` Red Ribbon Army Helmet (PQ160), `acc-061` Gohan (Beast) Wig (PQ162), `acc-062` Yamcha's Baseball Hat (PQ97), `acc-063` SSGSS Vegeta Wig (PQ100), `acc-064` SS4 Wig & Tail (Goku) (PQ110).
- [x] Normalized legacy equipment IDs `equip-057`, `equip-066`, `equip-069`, `equip-120`, `equip-123`, and `equip-133` to canonical `acc-059` through `acc-064` rather than duplicating identities.
- [x] Rebuilt the accessory bridge/report: **22 forward / 22 reverse / 23 unresolved / 0 invalid targets / 0 broken endpoints / 0 duplicate edges**.
- [x] Refreshed the unresolved backlog; `Android 13's Hat` remains unresolved as a distinct canonical identity despite independent TP Medal Shop evidence because it is not present in the current canonical inventory layer.
- [x] Updated the accessory canonicalization audit and reader-facing Accessory PQ Database.
- [x] Canonical source-of-truth rule preserved: canonical records determine identity; research/verification metadata supports but does not override them.
- [x] Validation: **172 total equipment/accessory records / 64 canonical accessory IDs / 0 duplicate canonical IDs / 0 duplicate accessory names**. Equipment relationship layer remains **123 forward / 121 reverse / 0 broken**.
- [x] Evidence included the maintained PQ reward guide, current/maintained equipment references, independent PQ149 evidence, PQ160/PQ162 current research, and TP Medal Shop evidence for the still-unresolved Android 13's Hat.
- [ ] Exact next task: reconcile the next **8–20** remaining accessory research identities, prioritizing PQ152–156 and PQ159–168 where existing research suggests exact inventory names or component aliases, but promote only when the current canonical layer can support an exact identity.


### 2026-09-22 — Accessory canonical identity batch: PQ152–168
- [x] Reconciled six source-backed accessory identities: Android 17 (DB Super) Wig, King Vegeta (DB Super) Wig, Gamma 2's Helmet, Gamma 1's Helmet, Dr. Hedo Hood, and Videl (DB Super) Wig.
- [x] Mapped the Android 17 Ranger Accessory research label to the Android 17 wig as a component alias; no duplicate canonical identity created.
- [x] Normalized legacy equipment identities to canonical accessory IDs and synchronized PQ→equipment and PQ→accessory reports.
- [x] Validation: 174 total equipment/accessory records, 70 canonical accessory IDs, 28 accessory forward/reverse edges, 16 unresolved accessory research records, 129 equipment forward / 123 reverse / 0 unresolved / 0 broken.
- [ ] Exact next task: perform the full cross-database reward/reverse-index census and repair deterministic endpoint/count drift before beginning another provenance-only accessory batch.


### 2026-09-22 correction — PQ equipment relationship count
- [x] Corrected the live PQ→equipment relationship census to **125 forward / 123 reverse / 0 unresolved / 0 broken endpoints**; canonical endpoint parity remains pass.
- [ ] Exact next task remains the full cross-database reward/reverse-index census and deterministic drift repair.


### 2026-09-22 cycle update — Deterministic cross-domain reward-index reconciliation
- Live pre-edit census: master `docs/data/pq-reward-relationships.json` contained **842 total relationships**: 236 skills / 140 Super Souls / 124 equipment / 247 character / 88 DLC / 7 farming. Current domain reports contained 244 / 151 / 125 / 247 / 88 / 7 respectively.
- Reconciled the master reward index against the current canonical PQ skill, Super Soul, and equipment cross-link reports rather than treating the stale master index as source of truth.
- Skill fixes: **9 missing current report edges added** and obsolete `PQ104 → Starfall` alias removed; current skill total is **244**.
- Super Soul fixes: **13 missing current report edges added** and two stale capitalization variants removed; current total is **151**.
- Equipment fixes: added current `PQ76 → Whis Symbol Gi`, `PQ152 → Android 17 (DB Super) Wig`, and `PQ155 → Gamma 2's Helmet`; removed stale `PQ50 → Mr. Shape Up M` (canonical classification removed it as a consumable/material) and obsolete `PQ66 → Whis Symbol Gi`; current total is **125**.
- Post-edit master index: **862 total relationships = 244 skill + 151 Super Soul + 125 equipment + 247 character + 88 DLC + 7 farming**.
- Cross-domain audit/status synchronized to the same live counts. No duplicate relationship pairs, invalid PQ numbers, broken endpoints, or non-source-backed current edges were introduced by this reconciliation.
- Canonical source-of-truth rule preserved: current canonical domain reports are projections of canonical records; the master relationship index is synchronized to them and is not an independent authority.
- CI: no successful GitHub Actions status exposed for this direct-commit chain; no CI success claimed.
- Commits: master reward index `02b6306341c2d3a6cf6f6213a25386949d07a7ce`; cross-domain audit `78c18bbcd6e55fcb67c37a422a776b966f363a14`; cross-domain status `3e8055fd01ae540e4e794731edda7d60f13e03d8`.
- Exact next batch: **repair the remaining reverse-index/cross-domain documentation drift**, beginning with the accessory-specific relationship layer versus the legacy cross-domain audit's clothing/accessory counts, then run a repository-wide endpoint census before new provenance research.


### 2026-09-22 cycle update — Reverse-index count drift repair
- Live census found stale historical reverse-index/schema-consumer counts inside `docs/data/pq-cross-domain-audit.json` and `docs/data/pq-cross-domain-status.json`: they still reported the pre-reconciliation 236/137/125 reward counts and 840 total edges despite the live master index and domain reports being 244/151/125 and 862 total.
- Repaired deterministic documentation/validator state only; no canonical relationship identities were changed.
- Synchronized forward, reverse, audit, and status counts to **244 skill / 151 Super Soul / 125 equipment / 247 character / 88 DLC / 7 farming = 862 total**.
- Preserved the separate accessory/clothing reverse counts as currently represented by the legacy reverse-index schema (`clothing: 87`, `accessories: 38`) rather than inventing a new decomposition.
- Validation: master-to-domain parity remains exact for Skills, Super Souls, and Equipment; duplicate and invalid-PQ checks remain zero.
- CI: no successful workflow/check exposed for this direct-commit chain.
- Commits: audit f73b842d97f3b586097625ad24350710fb1bb7e0; status e88a6c90e0d5a6360c89982bc7b505bbc7caeade.
- Exact next batch: **repository-wide endpoint census across every PQ relationship artifact**, with particular attention to reverse-index producer files and stale count fields.


### 2026-09-22 cycle update — Repository-wide PQ endpoint census
- Completed the requested endpoint census across the master PQ relationship index and all maintained Skill, Super Soul, Equipment, and Accessory forward/reverse relationship reports.
- Master index: **862 relationships**, covering the complete numbered PQ range with **0 invalid PQ numbers**, **0 duplicate relationship keys**, and **0 empty targets**.
- Reverse parity: Skills **244 forward / 239 unique reverse endpoints**, Super Souls **151 / 148**, Equipment **125 / 123**, Accessories **28 / 28**. Every reverse endpoint has a matching forward-derived PQ set; **0 missing**, **0 orphan**, and **0 PQ-set mismatch** cases were found.
- Canonical equipment/accessory layer remains **174 records / 70 canonical accessory IDs**.
- Historical 840-edge figures remain preserved as dated historical records; current final-state fields remain synchronized to the 862-edge baseline.
- Validation: endpoint census clean; no canonical identities or relationship edges required modification.
- CI: no successful workflow/check exposed for this direct-commit chain.
- Commits: audit a0cc718ef14646f902f371a139e568178c4d6ac2; status c7a21b5ab50b0c9dbfa94e9e76fb001feddb2a55.
- Exact next batch: **inspect remaining relationship artifacts for stale producer metadata/count fields outside the four primary PQ cross-link reports, then repair only deterministic drift before beginning new provenance research.**


### 2026-09-22 cycle update — PQ relationship producer census
- Added `docs/data/pq-relationship-producer-census.json` as the current machine-readable producer metadata census.
- Current canonical relationship totals remain **862**: Skills 244, Super Souls 151, Equipment 125, Characters 247, DLC 88, Farming 7.
- Current producer metadata agrees with live forward/reverse arrays: Skills 244/239, Super Souls 151/148, Equipment 125/123, Accessories 28/28; all current declared counts match their arrays.
- Canonical accessory metadata is synchronized at **70** identities; bridge/remaining summaries are synchronized at 29 matched + 16 unresolved and 28 matched + 16 unresolved respectively where those files intentionally use different derived scopes.
- No current producer-count drift was found. Historical 840-edge and earlier 64/22-era accessory values remain preserved as historical evidence rather than being silently deleted.
- New census commit: **f7c84a80413419a03c063daf0e8f28d5631cc450**.
- Validation: current producer-count drift **0**, canonical endpoint mismatches **0**, reverse endpoint mismatches **0**.
- Next batch: begin systematic provenance/source-route audit of the remaining PQ relationship domains (character, DLC, farming) while preserving canonical data as the authoritative source of truth.


### 2026-09-22 cycle update — Character/DLC/farming provenance audit
- Audited the remaining non-reward PQ relationship domains directly from the canonical `docs/data/pq-reward-relationships.json` layer.
- Character: **247 source-backed edges**, **143 unique PQs**, **75 unique targets**, **0 missing sources**, **0 duplicate pairs**. Provenance routes: Steam PQ guide 189 edges; Twinfinite PQ guide 58.
- DLC: **88 source-backed edges**, **86 unique PQs**, **21 unique targets**, **0 missing sources**, **0 duplicate pairs**. Provenance routes: Steam PQ guide 83; Bandai Namco DLC catalog 3; Bandai Namco Future Saga Chapter 4 announcement 2.
- Farming: **7 source-backed edges**, **7 unique PQs**, **1 target**, **0 missing sources**, **0 duplicate pairs**. Provenance routes: Steam PQ guide 6; Twinfinite PQ guide 1.
- Added `docs/data/pq-nonreward-provenance-audit.json` to preserve the source-route census and explicit evidence boundaries.
- Canonical rule preserved: provenance sources support relationships but do not override canonical identities; no inferred relationship was fabricated and no canonical edge was changed in this batch.
- Validation: all three domains remain source-backed; missing sources **0**; duplicate pairs **0**; inferred additions **0**; canonical-target overrides **0**.
- Commit: **10dd7bc64d51f7ee6c21d968715bd9fa7dc48c27**.
- CI: no successful workflow/check exposed for this direct-commit chain.
- Current master remains **862 relationships**: 244 skill / 151 Super Soul / 125 equipment / 247 character / 88 DLC / 7 farming.
- Exact next batch: **trace the 247 character edges and 88 DLC edges back to their canonical PQ records and identify any target/alias normalization gaps, without treating source text as a canonical source of truth.**


### 2026-09-22 — PQ character/DLC target normalization
- [x] Audited all **247 character edges / 75 unique character targets** against `docs/data/characters-record-layer.json`: **0 missing canonical targets** and **5 explicit aliases** retained.
- [x] Audited all **88 DLC edges / 21 unique targets** and found one deterministic case-only duplicate key in the normalized reverse index.
- [x] Normalized PQ185/PQ186 relationship targets from `FUTURE SAGA Chapter 4` to canonical `Future Saga Chapter 4`.
- [x] Removed the duplicate `FUTURE SAGA Chapter 4` reverse-index key while preserving the canonical `Future Saga Chapter 4` mapping.
- [x] Preserved `Super Pack 1`–`Super Pack 4` as distinct source-backed DLC targets; they are not silently collapsed into the broader `Super Pass` requirement.
- [x] Validation: **862 total relationships / 247 character / 88 DLC / 0 duplicate relationship keys / 0 invalid PQ numbers / 0 empty targets / 0 DLC casefold duplicate keys**.
- [ ] Exact next task: recompute the full repository relationship/projection census and identify the next deterministic producer drift or highest-priority unresolved cross-database endpoint gap.


### 2026-09-22 cycle correction — duplicate PQ185/PQ186 DLC relationship evidence\n- Recomputed the post-normalization relationship keys and found two duplicate keys that were hidden by the earlier source-level count: PQ185 and PQ186 each contained the same `pq_requires_dlc → Future Saga Chapter 4` relationship twice, once from Bandai Namco and once from the maintained Steam PQ guide.\n- Merged each duplicate into one canonical relationship object, retaining the official Bandai Namco source in the required `source` field and preserving the corroborating Steam source in `notes` because the relationship schema permits one source URI per edge.\n- Current unique relationship baseline is now **860**: 244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming.\n- Historical **862-edge** counts remain preserved in dated historical sections; they are superseded by the current unique-edge census and are not deleted.\n- Validation: **0 duplicate relationship keys**, 0 invalid PQ numbers, 0 empty targets, 75/75 canonical character targets, 0 DLC casefold duplicate keys.\n- Exact next task: recompute the repository-wide relationship/projection census from the corrected 860-edge canonical relationship array before any new provenance work.\n

### 2026-09-22 cycle update — current projection census correction — current projection census correction
- Recomputed the repository-wide PQ projection census from the corrected 860-edge canonical relationship array.
- Deterministic stale fields were found in the cross-domain audit/status artifacts: older endpoint-census and final-consistency objects still used the pre-duplicate-merge 862-edge baseline. Historical 862/840 records were preserved; only current-state projection fields were corrected.
- Current canonical counts: 860 total = 244 skill + 151 Super Soul + 125 equipment + 247 character + 86 DLC + 7 farming.
- Current reverse projection endpoints: 239 skills / 148 Super Souls / 123 equipment / 28 accessories; 0 missing / 0 orphan / 0 PQ-set mismatches. DLC: 86 forward edges / 20 unique reverse endpoints, exact parity.
- No canonical relationship identities were changed in this batch; this was deterministic producer/projection metadata repair only.
- Exact next batch: scan remaining non-PQ relationship producers and generated projection metadata for current-count drift, then repair only deterministic mismatches before expanding provenance research.


### 2026-09-22 cycle update — non-PQ projection producer census
- [x] Audited Skill, Super Soul, Equipment, and Accessory generated PQ cross-link reports against the canonical relationship layer.
- [x] Current report counts synchronized: **244/239**, **151/148**, **125/123**, **28/28** forward/reverse endpoints respectively.
- [x] Validation: all four reports have 0 duplicate keys, 0 invalid PQ references, 0 unresolved forward edges, and 0 orphan reverse sources.
- [x] Preserved the accessory-vs-equipment scope distinction; no unsupported count collapse was made.
- [ ] Exact next task: audit remaining generated/reconciliation artifacts outside the four primary cross-link reports for stale current-state counts or mismatched scopes.


### 2026-09-22 — PQ reconciliation artifact scope audit
- [x] Audited the unified reward reconciliation artifact: 186/186 numbered slots, no duplicate boundary IDs, no missing numbered slots, PQ36 explicitly unresolved.
- [x] Confirmed PQ1-40 and PQ41-80 range audit counts (40/30 and 40/33) are partial-source-layer counts, not canonical relationship counts.
- [x] Confirmed accessory canonical bridge: 45 records = 29 matched + 16 unresolved, 0 duplicate bridge IDs.
- [x] Preserved partial reverse-index semantics; no canonical relationship identities were changed.
- [ ] Exact next task: audit remaining generated reverse indexes/acquisition indexes for scope metadata and canonical-vs-partial semantics, starting with Super Soul PQ acquisition and PQ reverse-index artifacts for PQ81-186.


### 2026-09-22 — Reverse-index and Super Soul acquisition scope audit
- [x] Reconciled unified reverse-index metadata with its actual arrays; corrected stale DLC reference count **88 -> 86**.
- [x] Documented partial-index counts versus canonical counts: skills **236/244**, Super Souls **137/151**, equipment **125/125**, characters **247/247**, DLC **86/86**, farming **7/7**.
- [x] Audited Super Soul acquisition projection: **80 PQ records / 122 references**, 108 exact canonical overlaps, 14 research-only pairs, 43 canonical pairs absent, with 25 absent within PQ41-186 scope.
- [x] Preserved canonical data as source of truth; research-only acquisition pairs were not promoted.
- [ ] Exact next task: audit remaining PQ reverse-index artifacts for PQ81-186 and other domain-specific acquisition projections using exact relationship-pair comparison.


### 2026-09-22 — PQ reverse-index structural/scope audit
- [x] Audited PQ81-120, PQ121-142, and PQ163-186 reverse-index artifacts.
- [x] Repaired missing root JSON brace in PQ81-120 without changing indexed data.
- [x] Confirmed PQ121-142 = **89 references / 22 PQs** and PQ163-186 = **169 references / 24 PQs**.
- [x] Confirmed no standalone PQ143-162 reverse-index artifact currently exists; retained this as an explicit coverage gap.
- [x] Preserved canonical relationship data unchanged.
- [ ] Exact next task: compare PQ81-120, PQ121-142, and PQ163-186 indexes against their normalized reward maps at exact relationship-pair level and assess deterministic PQ143-162 reverse-index generation.


### 2026-09-22 — PQ81-162 standalone reverse-index reconciliation
- [x] Added/confirmed standalone reverse-index artifacts for PQ81-120, PQ121-142, and PQ143-162.
- [x] Closed the previously documented standalone reverse-index gap for PQ143-162 with a deterministic projection from pq-143-162-reward-map.json.
- [x] Projection census: PQ81-120 = 108 indexed identities / 109 references; PQ121-142 = 88 indexed identities / 88 references; PQ143-162 = 151 indexed identities / 151 references.
- [x] PQ143-162 projection breakdown: 40 skills / 26 Super Souls / 11 clothing / 10 accessories / 64 artwork identifiers.
- [x] No canonical PQ identities or relationship edges were changed.
- [x] New PQ143-162 projection commit: f40a588758ef0a0c4388e5c6e4520608a24583a0.
- [ ] Exact next task: compare the three standalone indexes against the unified reverse index at exact relationship-pair level and repair only deterministic projection drift.


### 2026-09-22 — PQ reverse-index producer integrity
- [x] Audited PQ163-186 standalone reverse index against normalized reward map and unified index: 0 missing / 0 extra typed pairs across Skills, Super Souls, clothing, accessories.
- [x] Added `scripts/validate_pq_reverse_indexes.py` for deterministic source-map ↔ standalone ↔ unified typed-pair validation.
- [x] Validator design explicitly preserves canonical source-of-truth semantics and never infers missing rewards.
- [ ] Next: add safe deterministic generation support for standalone reverse indexes and unified projection, then run the validator and record its full output.


### 2026-09-22 — deterministic PQ reverse-index generation support
- [x] Added generator `scripts/generate_pq_reverse_indexes.py` covering PQ81-120, PQ121-142, PQ143-162, and PQ163-186 normalized reward maps.
- [x] Generator preserves canonical truth and historical metadata; existing files are projection-updated only.
- [x] Fixed validator legacy PQ81-120 parsing in `scripts/validate_pq_reverse_indexes.py`.
- [x] Existing repository pair audits remain 0 missing / 0 extra for PQ81-186 typed relationships.
- [ ] Runtime execution of generator/validator in a repository-capable environment and recording the full output.
- [ ] Only after runtime validation: assess deterministic unified reverse-index generation without overwriting partial/research-layer semantics.


### 2026-09-22 — PQ reverse-index generator schema compatibility
- [x] Audited live standalone reverse-index schema variants before generation automation.
- [x] Corrected generator compatibility for the legacy PQ121-142 top-level-domain schema while preserving newer nested-`indexes` schemas.
- [x] Confirmed generator writes only projection fields and does not migrate schemas or modify canonical relationships.
- [ ] Complete schema-aware dry-run/runtime comparison of all four standalone reverse indexes against normalized source maps.
- [ ] Only after that validation, evaluate unified reverse-index generation support.


### 2026-09-22 — complete PQ reverse-index source-shape audit
- [x] Audited all four normalized source maps and standalone reverse indexes.
- [x] Generator now supports PQ81-120 object-map, PQ121-162 nested `rewards`, and PQ163-186 direct typed-domain records.
- [x] Validator now supports the same three source shapes.
- [ ] Execute generator/validator in a repository-capable runtime and capture actual runtime output.
- [ ] If runtime remains unavailable, produce a static schema/parity audit artifact from live JSON and explicitly mark it as static rather than runtime validation.
- [ ] Evaluate unified reverse-index generation only after standalone validation is complete.


### 2026-09-22 — live schema-aware PQ reverse-index validation
- [x] Performed live repository JSON execution equivalent to the committed generator/validator normalization logic.
- [x] Standalone typed-pair parity: PQ81-120 **109/109**, PQ121-142 **89/89**, PQ143-162 **87/87**, PQ163-186 **72/72**; all ranges **0 missing / 0 extra**.
- [x] Unified reverse-index parity: all four ranges **0 missing / 0 extra** typed pairs.
- [x] Artwork remains separate projection data for PQ143-162 (64 entries) and PQ163-186 (97 entries), not canonical typed reward relationships.
- [x] Canonical reward source layer remains unchanged.
- [ ] Audit unified reverse-index producer/schema for safe deterministic generation without overwriting partial/research-layer semantics.

### 2026-09-22 — Unified reverse-index producer metadata drift repair
- [x] Recomputed the live canonical relationship census directly from `docs/data/pq-reward-relationships.json`: **860 unique edges = 244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming**.
- [x] Audited the partial normalized unified reverse index `docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json`: its live reference counts are **236 skill / 137 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming** and its canonical comparison block is **244 / 151 / 125 / 247 / 86 / 7**. The skill/Super Soul gaps are intentional partial-source coverage, not negative evidence.
- [x] Detected deterministic current-state metadata drift in `docs/data/pq-cross-domain-audit.json` and `docs/data/pq-cross-domain-status.json`: current DLC was still reported as **88** even though the corrected canonical baseline and final-consistency fields are **86**; the status next-gate text also still named the superseded 862-edge baseline as live.
- [x] Repaired only current-state metadata: canonical master `current_counts`, audit `current_counts`/next gate, and status `current_edges`/`current_counts`/next gate now all use **860 unique edges** and **86 DLC**.
- [x] Preserved all historical 862/840/88-era fields as dated history; no canonical relationship identity or partial reverse-index entry was deleted.
- [x] Post-edit validation: master/audit/status/producer-census counts all agree; duplicate relationship keys **0**; invalid PQ numbers **0**; empty targets **0**; canonical reverse projection parity remains **0 missing / 0 orphan / 0 PQ-set mismatch**.
- [ ] Exact next task: reconcile the live repository against the handoff claims that `scripts/generate_pq_reverse_indexes.py` and `scripts/validate_pq_reverse_indexes.py` exist. If the scripts are absent on the live branch, restore them with schema-aware, canonical-source-of-truth-safe implementations before evaluating unified reverse-index generation.

### 2026-09-22 cycle update — reverse-index script source-shape repair
- [x] Inspected the live scripts/generate_pq_reverse_indexes.py and scripts/validate_pq_reverse_indexes.py instead of relying on older handoff claims.
- [x] Found a real compatibility defect: the PQ81-120 normalized reward map uses a list-of-[PQ, typed-reward-list] record shape, while both scripts previously assumed dictionary records or object records with a pq field. The generator/validator would therefore fail on the live PQ81-120 source shape.
- [x] Patched both scripts to explicitly support the list-of-pairs source shape without changing canonical relationship data or inferring rewards.
- [x] Static live-data parity validation after the patch: PQ81-120 0 missing / 0 extra, PQ121-142 0/0, PQ143-162 0/0, PQ163-186 0/0 typed reward pairs between normalized source maps and standalone reverse indexes.
- [x] This was a validator/generator correctness repair, not a data promotion; artwork remains a separate projection for ranges that contain it.
- [ ] Exact next task: inspect unified reverse-index generation safety against its intentionally partial source coverage. Compare every canonical typed PQ relationship with the unified index by exact pair, identify only deterministic omissions/duplicates, and do not promote partial/research-only records into canonical data.

### 2026-09-22 cycle update — canonical unified reverse-index reconciliation
- [x] Compared the unified reverse index against the canonical forward relationship layer by exact (domain, target, PQ) identity, normalizing PQ number formatting only.
- [x] Found deterministic drift: 9 canonical skill edges and 16 canonical Super Soul edges were absent from the unified projection; 1 noncanonical skill name (Starfall) and 2 noncanonical Super Soul entries were present. These were repaired by projecting canonical relationships exactly.
- [x] Reconciled equipment through the existing subtype-aware clothing/accessory projection: removed three noncanonical subtype entries and restored the three canonical equipment edges (Whis Symbol Gi PQ76, Android 17 (DB Super) Wig PQ152, Gamma 2's Helmet PQ155).
- [x] Final exact parity: skills 244/244, Super Souls 151/151, equipment 125/125, characters 247/247, DLC 86/86, farming 7/7; 0 missing and 0 extra in every canonical relationship domain.
- [x] Updated the unified index semantics to explicitly make canonical relationship data authoritative; partial normalized source maps remain provenance/research layers and cannot override canonical relationships.
- [x] Updated the validator so standalone indexes are checked against normalized source maps, while the unified index is checked against canonical relationships; equipment is validated as the union of clothing/accessory projections.
- [ ] Exact next task: perform a full repository-wide cross-link integrity audit so PQ pages, skill/Super Soul/equipment/character/DLC/farming records all resolve through the canonical relationship layer without orphaned or one-way links. Preserve source provenance and historical audit entries.

### 2026-09-22 cycle update — PQ record/canonical cross-link integrity audit
- [x] Audited all 186 PQ records against the canonical docs/data/pq-reward-relationships.json relationship layer.
- [x] Skills: 244/244 exact, 0 missing, 0 extra. Super Souls: 151/151 exact, 0 missing, 0 extra.
- [x] Equipment: canonical has 125 unique edges while PQ record equipment_rewards contains 123 exact-name edges. Two deterministic naming conflicts were isolated without changing canonical data: PQ152 has canonical Android 17 (DB Super) Ranger Wig and Android 17 (DB Super) Wig; PQ155 has canonical Gamma 2 Helmet and Gamma 2's Helmet. The PQ record preserves its existing source-backed wording rather than inventing aliases.
- [x] DLC: record and canonical counts both equal 86, but 20 PQ101-120 endpoints use broad Super Pass/similar record-layer wording while canonical relationships use individual pack targets. This is recorded as a granularity conflict, not silently normalized.
- [x] Confirmed all PQ IDs pq-001 through pq-186 exist in the canonical record layer.
- [x] Added docs/data/pq-cross-link-integrity-audit.json to preserve the exact mismatch classification and prevent future cycles from treating naming/granularity differences as missing acquisition evidence.
- [x] Reverted a temporary attempted equipment-name normalization after determining the canonical layer contains distinct target strings; no unsupported alias was promoted.
- [ ] Exact next batch: inspect the repository cross-link contract and existing alias/index artifacts, then define a deterministic canonical-name alias/granularity layer for equipment and DLC presentation without altering canonical relationship identities. Use it to make downstream PQ↔reward navigation resolve both source naming and canonical target naming.

### 2026-09-22 cycle update — canonical endpoint alias/granularity bridge
- [x] Inspected the active cross-link contract plus equipment/accessory and DLC identity artifacts before adding a new bridge.
- [x] Added `docs/data/pq-endpoint-alias-granularity-map.json` as a deterministic presentation/identity bridge. It explicitly separates canonical identity from source/display naming and DLC bundle-vs-pack granularity.
- [x] Added two equipment conflict records (PQ152 Ranger Wig wording; PQ155 Gamma 2 Helmet wording) without merging canonical entities or inventing an alias.
- [x] Added six deterministic DLC granularity mappings covering PQ101-120: broad `Super Pass` presentation → individual `Super Pack 1-4` / `Extra Pack 1-2` canonical requirements. These mappings are explicitly one-to-one by PQ range and do not add canonical edges.
- [x] Validated every bridge canonical target against `docs/data/pq-reward-relationships.json`: **0 missing canonical target references**; canonical relationship count remains exactly **860**.
- [x] Updated `docs/data/CROSS-LINK-CONTRACT.md` so downstream navigation can consume the bridge without treating it as canonical relationship data.
- [ ] Exact next task: use the bridge to audit/repair downstream PQ ↔ equipment/accessory/DLC reverse navigation and page/index references, preserving canonical IDs and source provenance while reporting unresolved identities rather than guessing.

### 2026-09-22 cycle update — downstream PQ endpoint navigation audit
- [x] Audited the canonical PQ equipment/accessory reverse projections against the canonical equipment/accessory identity layer.
- [x] Confirmed current reverse integrity: equipment 125 forward edges / 123 unique target endpoints; accessory projection 28 / 28; **0 missing reverse endpoints, 0 orphan endpoints, 0 PQ-set mismatches**.
- [x] Added `docs/data/pq-endpoint-navigation-audit.json` documenting exact navigation resolution for the known PQ152/PQ155 naming conflicts without merging canonical entities.
- [x] Registered the navigation audit and alias/granularity bridge in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved canonical distinctions: `Android 17 (DB Super) Wig` → `acc-065`, `Android 17 (DB Super) Ranger Wig` → `equip-059`, `Gamma 2's Helmet` → `acc-067`, and `Gamma 2 Helmet` → `equip-062`.
- [ ] Next gate: extend endpoint identity-resolution auditing to skill, Super Soul, character, and DLC navigation, then add automated validation requiring every canonical endpoint to resolve exactly or be explicitly classified as conflict/granularity.



### 2026-09-21 cycle update — canonical endpoint identity validation and skill endpoint repair
- Live canonical relationship census before repair: **860 unique edges = 244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming**.
- Bounded batch: PQ endpoint navigation across skills, Super Souls, equipment/accessories, characters, and DLC.
- Deterministic findings: three PQ→skill relationship targets did not exactly match canonical skill identities: **PQ46 Chain Destructo-disc Barrage → Chain Destructo-Disc Barrage**, **PQ90 III Bomber → Ill Bomber**, and **PQ163 Giant Cluster → Gigantic Cluster**. The canonical skill IDs already existed, so no new skill identity was created.
- Changes: normalized those three targets in `docs/data/pq-reward-relationships.json`; synchronized the corresponding PQ skill reward labels in `docs/data/parallel-quests-record-layer.json`; synchronized `docs/data/pq-skill-crosslink-report.json` so all 244 skill edges are exact canonical-name matches.
- Added `scripts/validate_pq_endpoint_navigation.py` to enforce exact canonical endpoint resolution for skills, Super Souls, equipment/accessories, and characters while explicitly reporting DLC identity-layer gaps. Added `docs/data/pq-endpoint-navigation-validation.json` and registered both in `docs/data/pq-cross-domain-index.json`.
- Validation: **0 missing canonical targets** for skills (244 edges / 239 unique targets), Super Souls (151 / 148), equipment (125 / 123), and characters (247 / 75). DLC has **86 edges / 20 unique targets**, all explicitly reported as an **identity-layer gap**, not guessed or promoted into canonical records. Alias/granularity bridge remains 2 equipment conflicts + 6 DLC granularity mappings; canonical edge count remains **860**.
- Evidence limits preserved: canonical database records remain authoritative; verification status and presentation bridges are evidence/navigation metadata only. No DLC identity was invented.
- CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- Commits: `8cf12cc325456bb157f0788ed9d9f9b47740220b`, `333ec6f0123f15941cc205f94a6eb1d02726ae8a`, `598de8494553dade1f93f80ae1437aabeba902fa`, `b82e7d19da2f94cdfb9325a1816b20cec846bc5d`, `a104231a22173bb5ce7638f2a4363bfc0ad72f25`, `0a39a4ef0adeec97090eb0704bb59343a1dab26f`.
- Exact next batch: **build the missing standalone canonical DLC identity layer** for the 20 existing canonical DLC relationship targets, using the repository's existing official DLC baseline and page/index structure. Do not derive new relationship edges from the identity layer; use it only to make existing canonical DLC endpoints navigable and validator-resolvable. Preserve bundle-vs-pack granularity and all historical audit entries.


### 2026-09-22 cycle update — standalone canonical DLC identity layer
- [x] Live census before editing: canonical PQ relationships remain **860 unique edges = 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**; the DLC relationship layer contains **20 unique targets**.
- [x] Inspected the existing DLC baseline, DLC record requirements, Future Saga record, DLC schema, cross-link contract/bridge, and canonical PQ relationship endpoints before writing the identity layer.
- [x] Added `docs/data/dlc/canonical-dlc-identity.json` with exactly the **20 existing canonical DLC relationship targets** and no additional DLC identities: Super Packs 1-4, Extra Packs 1-4, Ultra Packs 1-2, Legendary Packs 1-2, Hero of Justice Packs 1-2, Conton City Vote Pack, Dragon Ball DAIMA Pack, and Future Saga Chapters 1-4.
- [x] Added `docs/data/dlc/canonical-dlc-identity.schema.json` defining the identity-layer contract. Every record is explicitly `indexed`; official publisher provenance establishes identity/provenance only, while gameplay/content details remain unresolved unless independently verified.
- [x] Preserved granularity: individual packs remain packs and Future Saga entries remain chapters; parent bundle/set names are metadata only. No Super Pass/Extra Pass/Future Saga bundle was substituted for an individual canonical endpoint.
- [x] Updated `scripts/validate_pq_endpoint_navigation.py` so DLC endpoints are now resolved against the standalone canonical DLC identity layer instead of being reported as an identity-layer gap. Missing DLC identities are now validator failures.
- [x] Updated `docs/data/pq-endpoint-navigation-validation.json`: DLC is now **86 edges / 20 unique targets / 0 missing / clean**; all other canonical domains remain clean.
- [x] Registered the DLC identity record and schema in `docs/data/pq-cross-domain-index.json`.
- [x] Deterministic parity validation: **20 DLC identity records / 20 unique IDs; 0 canonical relationship targets missing from the identity layer; 0 orphan DLC identity records; 86 canonical DLC edges**.
- [x] No canonical PQ relationship was added, removed, or rewritten in this batch. The 860-edge canonical relationship layer remains authoritative.
- [x] Evidence limit: the maintained official DLC baseline is sufficient for identity/provenance, not for promoting detailed gameplay fields. No unsupported reward/mechanics data was invented.
- [ ] CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: `f095eec0fdc8c1976575126ce1d743d748acba7e`, `35b5d52a6be3fec5271de70bd29ecf3123efba45`, `1c2b74ba088ca7594f214f50021af2f9593a0152`, `5e912bb9cd8401b3462a97f61a8fa5f3c1c1c584`, `f1ac3e0dc8185b5ad81cbd0553a4957823b9cd10`.
- [ ] Exact next batch: use the now-complete canonical endpoint identity layer to audit **downstream DLC reverse navigation and page/index references** for all 20 records, then reconcile any one-way/orphaned references without changing canonical relationship identities. After that, extend the same deterministic identity-resolution audit to farming and remaining cross-domain presentation indexes.


### 2026-09-22 cycle update — canonical DLC reverse PQ navigation
- [x] Live census: canonical DLC identity layer contains **20 records**; canonical `pq_requires_dlc` contains **86 edges / 20 unique DLC targets**.
- [x] Audited downstream DLC navigation artifacts, including `docs/data/relationships/dlc-content-links.json`, `docs/DLC-Overview.md`, the DLC baseline, Future Saga records, and the PQ canonical relationship source.
- [x] Added `docs/data/dlc/pq-reverse-index.json`, a deterministic reverse index mapping each of the 20 canonical DLC identities to the PQ IDs that canonically require it.
- [x] Added `docs/data/dlc/pq-reverse-navigation-audit.json`. It records **20/20 DLC targets with reverse PQ navigation**, **86/86 reverse entries**, and explicitly separates the broader content-domain projection from the canonical DLC identity index.
- [x] Deterministic parity validation: reverse index contains **20 records / 86 PQ entries**, exactly matching the canonical forward DLC relationship layer; **0 mismatches, 0 missing reverse targets, 0 orphan reverse targets**.
- [x] Registered the reverse index and audit in `docs/data/pq-cross-domain-index.json`.
- [x] Important downstream finding: `docs/data/relationships/dlc-content-links.json` currently contains only **3 explicit DLC content-domain projections** (FUTURE SAGA bundle, Dragon Ball DAIMA Pack, Hero of Justice Pack 2). This is not a canonical PQ reverse-index defect, so it was **not expanded by inference**. Its `future-saga` bundle identifier also must not be silently substituted for the four chapter-level canonical DLC identities.
- [x] No canonical relationship identities were added, removed, or renamed. The canonical relationship layer remains authoritative.
- [ ] CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: `2b577fd8169c21569861e56b0d3b6663d30bdc88`, `987ebea5e47f703642e7c46abeeb6e814f225c69`, `b7afcb080a16ffc7b2f41f7bd011646bab3c0a6c`.
- [ ] Exact next batch: reconcile the **3 existing DLC content-domain projection records** against the canonical 20-record DLC identity layer without guessing missing content. First normalize the FUTURE SAGA bundle/chapter relationship model (bundle remains a parent grouping; Chapters 1-4 remain canonical identities), then audit the DAIMA and HERO OF JUSTICE Pack 2 projections against existing character/PQ/skill/Super Soul/equipment records. Any missing domain links should be recorded as unresolved coverage, not invented.


### 2026-09-22 cycle update — DLC content projection identity reconciliation
- [x] Live census: **20 canonical DLC identities / 86 canonical PQ→DLC edges**; the broader DLC content projection still contains exactly **3 records**.
- [x] Reconciled `docs/data/relationships/dlc-content-links.json` without inventing content. The FUTURE SAGA entry is now explicitly a **parent bundle** resolving to canonical Chapters 1–4; it no longer risks being mistaken for a chapter-level canonical endpoint.
- [x] DAIMA Pack projection now explicitly resolves to canonical DLC ID `dragon-ball-daima-pack` and its existing canonical PQ navigation set **PQ179–181**.
- [x] HERO OF JUSTICE Pack 2 projection now explicitly resolves to canonical DLC ID `hero-of-justice-pack-2` and its existing canonical PQ navigation set **PQ159–162**.
- [x] Added `docs/data/dlc/dlc-content-link-audit.json` documenting domain coverage and evidence boundaries. Canonical PQ relationships were used only to expose existing navigation; they were not promoted into an inferred complete DLC inventory.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **20 canonical DLC identities**, **86 canonical DLC edges**, all 4 Future Saga chapter IDs resolve, DAIMA identity resolves with 3 PQs, HERO OF JUSTICE Pack 2 resolves with 4 PQs, and all 3 projection records remain internally consistent.
- [x] Evidence limits preserved: DAIMA raid/lobby content and HERO OF JUSTICE stage/full inventory remain unresolved at record level; missing content was not guessed.
- [ ] CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: `b605ff9c897fb2bf34a70a5ca064d94723625492`, `aec962ecebacf642a45030e1f5807294b2f4b861`, `6bb0e2a6a84a3d8ab6df00b8d9b7cb08d7658d3c`.
- [ ] Exact next batch: audit **farming (7 canonical PQ edges)** and the remaining cross-domain presentation indexes with the same canonical-identity-first rule. Build a deterministic farming reverse/identity projection, then inspect whether any presentation index points at non-canonical aliases or orphan endpoints before expanding content coverage.


### 2026-09-22 cycle update — canonical farming identity/reverse navigation
- [x] Live census: canonical farming layer contains **7 `pq_farming_route` edges**, all targeting the single canonical target **Dragon Balls**.
- [x] Added `docs/data/farming/pq-farming-reverse-index.json`, preserving all 7 canonical PQ endpoints: PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88.
- [x] Added `docs/data/farming/pq-farming-reverse-audit.json` with deterministic parity and provenance tracking.
- [x] Validation: **7 forward farming edges / 1 unique target / 1 reverse record / 7 reverse PQ entries / 0 unresolved targets / 0 orphan reverse records / 0 duplicate PQ edges**.
- [x] Source provenance preserved from the canonical relationship layer: Steam Community guide for PQ15/22/44/45/83/88 and Twinfinite for PQ68. The reverse index does not elevate these farming relationships into ordinary reward relationships.
- [x] Registered the farming reverse index and audit in `docs/data/pq-cross-domain-index.json`.
- [x] No canonical identities or relationship endpoints were renamed, substituted, or inferred.
- [ ] CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: `64f0219c0d223975c626a97ea5db2b6fed50620c`, `8aa02d00d41c178ec139a01c0f8d69bd9dee1cd2`, `a1a5d62373798657e257e501ed868e1f12b1ac40`.
- [ ] Exact next batch: inspect remaining cross-domain presentation indexes for canonical-identity parity, prioritizing indexes that consume PQ relationship endpoints and can expose alias/orphan navigation without requiring broad content research.


### 2026-09-22 cycle update — PQ presentation index canonical-identity audit
- [x] Audited the existing PQ reverse/presentation projections for Skills, Super Souls, Equipment, Accessories, the alias/granularity bridge, and the three DLC content projections.
- [x] Added `scripts/validate_pq_presentation_indexes.py` to enforce canonical ID and canonical-name resolution for these presentation consumers.
- [x] Added `docs/data/pq-presentation-index-identity-audit.json` with the current deterministic audit result.
- [x] Validation census: **239 skill reverse targets, 148 Super Soul reverse targets, 123 equipment reverse targets, and 28 accessory reverse targets**; all canonical IDs resolve, all report names match their canonical records, and all four reports contain **0 unresolved routes**.
- [x] Alias/granularity bridge: **2 equipment conflict records** remain explicit and separate; **6 DLC granularity records** resolve without changing canonical edges. The bridge remains presentation metadata only.
- [x] DLC content projection: all **3** existing projection records resolve their canonical DLC IDs; no orphan canonical DLC IDs were found. FUTURE SAGA remains a parent grouping node while Chapters 1–4 remain canonical identities.
- [x] Canonical relationship count remains **860**; no relationship identities were added, removed, or renamed.
- [ ] CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: `f44a529b62365a119c2cdf9fafb8392c0ad150ad`, `f2e0037debeb41641eb2d5d4d470c2df5f1c54f8`, `ae5263017321665d7ca1dd63c689530b73f21d3c`.
- [ ] Exact next batch: extend canonical presentation auditing to the character-facing PQ navigation and the broader PQ page/index consumers, specifically identifying any legacy display-only names or orphan character endpoints before adding new content coverage.


### 2026-09-22 — Canonical character reverse-navigation audit
- [x] Recomputed the live canonical relationship census: 860 unique edges; character subset 247 edges / 75 unique targets / 143 PQs; canonical character layer 149 records.
- [x] Added docs/data/characters/pq-reverse-index.json directly from the canonical pq_features_character relationship edges, preserving exact canonical character names and every PQ source.
- [x] Added docs/data/pq-character-reverse-navigation-audit.json and scripts/validate_pq_character_reverse_index.py; registered both in docs/data/pq-cross-domain-index.json.
- [x] Validation: 247/247 forward character pairs represented in reverse; 75/75 unique targets resolve to canonical character names; 0 missing targets; 0 orphan reverse targets; 0 duplicate pairs; 5 documented aliases remain presentation metadata only.
- [x] Preserved the canonical-source-of-truth rule. Reverse/index/audit artifacts are projections and do not create or rename character identities.
- [x] Preserved identity limits: the canonical character layer currently uses names rather than stable character IDs, so no IDs were invented; generic enemy appearances were not converted into relationships.
- [ ] Exact next task: audit the broader PQ page/index consumers for one-way links, orphan page references, and legacy display-only names against the canonical relationship layer; repair only deterministic navigation projections and record unresolved coverage rather than inferring relationships.


### 2026-09-22 — Character reverse-index key clarification
- [x] Updated docs/data/pq-cross-domain-index.json to use canonical_character_name for the character reverse projection because the live character layer has names, not stable character IDs.
- [x] No canonical relationship data changed; this prevents downstream consumers from assuming a nonexistent character-ID layer.
- [x] Commit: c46f937382a0f8b154e5dbe15bc0263eb7eb6d76.


### 2026-09-22 — PQ page/index consumer gate clarification
- [x] Inspected the live PQ record layer and cross-domain documentation after completing the canonical character reverse-navigation batch.
- [x] Confirmed `parallel-quests-record-layer.json` has stable PQ IDs plus skill/Super Soul reward ID projections, but no dedicated character relationship field; character navigation remains correctly derived from the canonical `pq_features_character` relationship layer rather than inferred from generic enemy/objective text.
- [x] Updated `docs/data/pq-cross-domain-index.md` so the current next gate is consumer/page navigation integrity rather than the already-completed reward-domain population sequence.
- [x] Updated `docs/Parallel-Quest-Audit.md` so its current research target reflects the completed canonical skill cross-link gate and the remaining PQ navigation-consumer audit.
- [x] No canonical relationship edges were added, removed, or renamed; live relationship baseline remains 860 unique edges.
- [ ] Exact next task: inspect the generated PQ catalog/page implementation and templates/index data for displayed reward, character, and DLC links; add a deterministic consumer validator or repair only confirmed stale/orphan references. Do not infer relationships from page prose.


### 2026-09-22 — PQ page consumer repair
- [x] Audited the actual `docs/Parallel-Quests-All.html` implementation rather than relying only on documentation.
- [x] Removed its direct dependency on the external Madreag PQ API/raw records and switched it to the canonical local `docs/data/parallel-quests-record-layer.json`.
- [x] Preserved verification state, objectives, Ultimate Finish, rewards, DLC/unlock metadata, and local reward-domain cross-navigation.
- [x] Added `?q=` support to `docs/assets/search.js` so PQ reward links can open the local published Search surface with deterministic queries.
- [x] Added and registered `scripts/validate_pq_page_consumers.py` to enforce the consumer contract.
- [x] Canonical relationship data was unchanged; this was a presentation/source-of-truth repair.
- [ ] Exact next task: inspect remaining published PQ/skill/character/DLC index consumers for direct external-corpus dependencies or stale display-only navigation and repair only deterministic local consumers.


### 2026-09-22 — Catalog consumer source-of-truth sweep
- [x] Searched for direct external Madreag API/raw catalog dependencies.
- [x] Repaired `docs/Skills-All.html` to use canonical local `docs/data/skills.json`.
- [x] Repaired `docs/Awoken-All.html` to use canonical local `docs/data/skills.json` and explicit Awoken/Transformation classification only.
- [x] Expanded `scripts/validate_pq_page_consumers.py` to cover PQ, Skills, and Awoken consumer source-of-truth contracts.
- [ ] Continue searching for remaining direct external catalog consumers and audit character/DLC presentation indexes.


### 2026-09-22 — DLC navigation reconciliation
- [x] Confirmed the existing standalone canonical DLC identity layer contains exactly the 20 existing canonical PQ DLC targets.
- [x] Reconciled DLC reverse navigation: 86 canonical edges represented across 20 targets, with 0 missing/orphan reverse targets.
- [x] Corrected stale DLC validator documentation.
- [x] Added explicit canonical DLC identity/reverse-index/audit links to `docs/DLC-Overview.md`.
- [x] Preserved canonical relationship count at 860; no new edges were inferred.
- [ ] Continue auditing character/DLC presentation consumers and structured links for deterministic resolution.


### 2026-09-22 — Character presentation identity bridge
- [x] Audited character presentation layers: canonical character data intentionally uses names, while presets/Partner Customization use existing `character_id` values.
- [x] Added explicit 29-record `character_id` → canonical-name presentation bridge.
- [x] Added validator covering preset and Partner Customization character IDs.
- [x] Registered the bridge/validator in the cross-domain index.
- [x] Preserved canonical-name authority; no IDs or relationships were invented.
- [ ] Audit DLC presentation consumers and Future Saga maps for deterministic `dlc_id` resolution.


### 2026-09-22 — DLC presentation consumer and Future Saga identity audit
- [x] Audited the live canonical DLC identity layer against the three existing DLC content-domain projection records, the Future Saga content map, and the published DLC overview navigation.
- [x] Added `scripts/validate_dlc_presentation_consumers.py` to enforce deterministic `dlc_id` resolution for DLC presentation consumers and Future Saga Chapters 1–4.
- [x] Added `docs/data/dlc/dlc-presentation-consumer-audit.json` with the current identity-resolution result: **20/20 canonical DLC identities resolved; 6/6 DLC projection references resolved; 4/4 Future Saga chapter references resolved; chapter set exactly 1–4; 0 unresolved identity targets**.
- [x] Registered the validator and audit in `docs/data/pq-cross-domain-index.json` and exposed the Future Saga content map plus presentation audit from `docs/DLC-Overview.md`.
- [x] Preserved the canonical-source-of-truth rule: no DLC identity, PQ relationship, or content-domain relationship was inferred or renamed. The audit only proves identity/navigation resolution; missing concrete content records remain unresolved.
- [ ] Exact next task: inspect remaining published character/DLC pages and structured indexes for direct external-corpus dependencies and stale/non-canonical navigation; then repair only deterministic local consumers. After that, continue exhaustive DLC content-domain reconciliation from existing canonical records.


### 2026-09-22 — DLC character provenance identity bridge
- [x] Audited `docs/data/records/character-dlc-baseline.json` against the 149-name canonical character layer and found presentation/provenance labels that do not consistently use canonical character names.
- [x] Added `docs/data/characters/dlc-character-identity-bridge.json` with **15** explicit baseline mappings: **7 exact**, **6 explicit aliases**, and **2 intentionally unresolved variant labels**.
- [x] Added `scripts/validate_dlc_character_identity_bridge.py` to ensure every DLC-baseline record has a bridge record, every resolved target exists in the canonical character layer, and unresolved labels remain explicit.
- [x] Added `docs/data/characters/dlc-character-identity-audit.json` and registered the bridge/audit in `docs/data/pq-cross-domain-index.json`.
- [x] Updated `docs/Characters.md` to expose deterministic DLC provenance → character identity navigation.
- [x] Important evidence boundary: **Supreme Kai of Time (Ultra Supervillain)** and **Goku (Ultra Supervillain Quelled)** were not collapsed into `Supreme Kai of Time`, `Goku`, or `Goku (Ultra Instinct)`; the current canonical layer has no exact matching identity, so both remain unresolved pending dedicated evidence.
- [x] No canonical character identities, DLC identities, or relationships were invented or renamed.
- [ ] Exact next task: audit remaining character-facing presentation indexes (especially preset/Partner Customization consumers) for canonical-name resolution and one-way/orphan navigation, then continue DLC content-domain reconciliation without collapsing unresolved variants.


### 2026-09-22 — Character-facing presentation consumer identity audit
- [x] Audited the existing 29-record `character_id` → canonical-name bridge against the preset and Partner Customization presentation consumers and Partner Customization reconciliation layer.
- [x] Added `scripts/validate_character_presentation_consumers.py` and `docs/data/characters/character-presentation-consumer-audit.json`.
- [x] Live identity census: **149 canonical character names; 29 bridge records; 45 preset records covering 17 distinct character IDs; 20 Partner Customization key records covering 20 distinct character IDs; 20 reconciliation character IDs**.
- [x] Validation result: **0 unresolved preset IDs, 0 unresolved Partner Customization IDs, 0 invalid bridge targets, 0 reconciliation ID-parity differences, 0 Partner display-name/canonical-name mismatches**.
- [x] Registered the audit/validator in `docs/data/pq-cross-domain-index.json` and exposed canonical character navigation from `docs/Partner-Customization.md`.
- [x] Preserved evidence boundaries: this establishes identity/navigation parity only; it does not claim complete preset numbering, loadouts, raid rotation, DLC ownership, TP Medal costs, or historical chronology.
- [ ] Exact next batch: extend the character-facing audit into PQ page/index consumers, checking whether PQ records expose canonical character endpoints consistently and whether any legacy display-only character names remain outside the explicit bridge.


### 2026-09-22 — PQ explorer character navigation consumer repair
- [x] Audited the live PQ presentation explorer against the canonical PQ relationship and character identity layers.
- [x] Updated `docs/Parallel-Quests-All.html` so each PQ dynamically loads canonical `pq_features_character` edges and exposes deterministic character search links alongside existing reward navigation.
- [x] Added `scripts/validate_pq_explorer_character_navigation.py` and `docs/data/pq-explorer-character-navigation-audit.json`.
- [x] Validation: **247 character edges / 75 unique canonical character targets / 143 source PQs; 0 missing canonical targets; 0 invalid PQ IDs; all explorer character-navigation contract checks clean**.
- [x] Registered the audit/validator in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical-source-of-truth rule: the explorer consumes `pq-reward-relationships.json`; it does not infer character participation from roster/enemy text.
- [x] Preserved the existing five source/display aliases as presentation metadata only; no new relationship edges or character identities were created.
- [ ] Exact next batch: audit the remaining PQ explorer/index consumer links for skills, Super Souls, equipment/accessories, and DLC so their displayed targets consistently resolve through canonical local layers rather than only generic search navigation.


### 2026-09-22 — PQ explorer reward-domain navigation repair
- [x] Audited the PQ explorer's skill, Super Soul, equipment/accessory, and DLC presentation links against their canonical relationship/record layers.
- [x] Updated `docs/Skills-All.html` to accept `?q=` navigation so canonical skill targets can open directly in the local skill explorer rather than generic wiki search.
- [x] Updated `docs/Parallel-Quests-All.html` so skill rewards use the canonical skill explorer; Super Souls and equipment/accessories retain local Search navigation because no dedicated canonical per-record explorer currently exists; DLC requirements use the local DLC overview route.
- [x] Added `scripts/validate_pq_explorer_reward_navigation.py` and `docs/data/pq-explorer-reward-navigation-audit.json`.
- [x] Live canonical reward census: **244 skill edges, 151 Super Soul edges, 125 equipment/accessory edges**; all referenced skill, Super Soul, and equipment/accessory target names resolve to their canonical record layers with **0 unresolved targets**.
- [x] Registered the audit/validator in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary preserved: local Search/overview links do not imply dedicated per-record pages; canonical relationship reports remain authoritative for acquisition/provenance semantics.
- [ ] Exact next batch: reconcile the PQ explorer's DLC requirement labels against `docs/data/dlc/canonical-dlc-identity.json` and then inspect direct PQ page templates for the same one-way reward navigation issue.


### 2026-09-22 — PQ explorer canonical DLC navigation reconciliation
- [x] Reconciled the PQ explorer's DLC presentation against the canonical `pq_requires_dlc` relationship layer and `docs/data/dlc/canonical-dlc-identity.json`.
- [x] Corrected `docs/Parallel-Quests-All.html` to derive displayed DLC links from canonical `pq_requires_dlc` edges instead of the broader presentation field `dlc_requirement: Super Pass`, which covers PQ 101–120 without identifying their individual packs.
- [x] Live DLC relationship census: **86 PQ → DLC edges / 20 unique canonical DLC targets / 0 unresolved target identities**.
- [x] Expanded `scripts/validate_pq_explorer_reward_navigation.py` and `docs/data/pq-explorer-reward-navigation-audit.json` to validate DLC target resolution and canonical relationship consumption.
- [x] Direct PQ-page template inspection found **no individual PQ HTML/Markdown page template** in the repository; the maintained presentation consumer is `docs/Parallel-Quests-All.html` plus the general `docs/Parallel-Quests.md` reference page. No unsupported per-PQ route was invented.
- [x] Evidence boundary preserved: the canonical DLC relationship layer determines PQ→DLC identity; the legacy `Super Pass` field remains historical/presentation metadata and is not promoted to a specific pack identity.
- [ ] Exact next batch: audit the general PQ reference/index pages (`docs/Parallel-Quests.md`, `docs/Parallel-Quest-Audit.md`, and related PQ-facing docs) for stale reward/navigation claims and reconcile them against the canonical 186-record PQ layer without rewriting unsupported mechanics or acquisition semantics.


### 2026-09-22 — PQ reference/index consumer reconciliation
- [x] Audited the general PQ reference/index consumers: `docs/Parallel-Quests.md`, `docs/Parallel-Quest-Audit.md`, `docs/Parallel-Quest-Walkthrough.md`, `docs/Farming-Routes.md`, `docs/Farming-Hub.md`, and `docs/data/parallel-quests-index.json`.
- [x] Removed unqualified canonical treatment of PQ23 as the Dragon Ball farming route; the canonical farming relationship set is **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**.
- [x] Clarified that route efficiency/ranking, drop probability, and Ultimate Finish requirements are separate evidence fields and are not created by a farming relationship.
- [x] Clarified the canonical 186-record PQ layer versus external/datemined PQ36/183-standalone numbering interpretations.
- [x] Updated the PQ seed index to expose the canonical farming set while preserving its non-canonical/indexed semantics.
- [x] No canonical PQ relationship identities or edges were changed; live relationship baseline remains **860 unique edges**.
- [x] Updated CHANGELOG with the completed reconciliation.
- [ ] Exact next task: search remaining PQ-facing documentation/index consumers for stale canonical-count, farming-route, or external-corpus claims and repair only deterministic local presentation drift.

### 2026-09-22 cycle update — remaining PQ numbering-consumer cleanup
- [x] Searched the remaining PQ-facing metadata after the prior reference/index reconciliation for stale canonical-count, PQ36, legacy-100, and numbering-gap semantics.
- [x] Reconciled deterministic stale metadata in `docs/data/pq-coverage.json`, `docs/data/pq-record-requirements.json`, `docs/data/completeness-rules.json`, `docs/data/pq-record-batches/pq-061-080-audit.json`, `docs/data/parallel-quest-research-batches/pq-batch-19-numbering-reconciliation.json`, `docs/data/pq-record-batches/pq-021-040-notes.md`, `docs/data/pq-record-batches/pq-021-040-source-conflicts.json`, `docs/data/pass-3-ready.md`, and `docs/Parallel-Quest-Walkthrough.md`.
- [x] Canonical policy is now explicit in the affected consumers: **PQ1-PQ186 / 186 numbered player-facing records**, with PQ36 retained in the canonical layer. Older PQ36-cut/183-standalone interpretations remain historical provenance and cannot replace the canonical layer.
- [x] Preserved historical entries rather than deleting them, in accordance with the exhaustive handoff/TODO rules.
- [x] Re-read changed files from `main`; no canonical PQ relationship edge or identity was changed.
- [ ] Exact next batch: continue the PQ-facing census beyond numbering metadata, targeting remaining stale **reward/acquisition/farming/navigation** claims in catalog/index/summary consumers. Prefer deterministic presentation drift only; do not promote source-dependent reward mechanics without canonical evidence.

### 2026-09-22 cycle update — PQ reward/acquisition presentation cleanup
- Live canonical PQ relationship baseline remains **860 unique edges**: 244 Skills / 151 Super Souls / 125 Equipment / 247 Characters / 86 DLC / 7 farming; canonical PQ layer remains **186 numbered records**.
- Bounded batch: inspected remaining PQ-facing reward/farming consumers surfaced by exact-name searches, including `docs/TP-Medal-Farming-Comparison.md` and `docs/Parallel-Quest-Walkthrough.md`.
- Deterministic drift found: TP Medal guidance still used PQ23 as the usual Dragon Ball route, and the walkthrough described PQ4 as a Dragon Ball farm and PQ134 using broad community/reward wording rather than the canonical relationship layer.
- Changes: removed the PQ23-specific dependency from TP Medal farming guidance; clarified Shenron's dependency as Dragon Ball collection; marked PQ4 as outside the current canonical Dragon Ball farming relationship set; changed PQ134 guidance to resolve through canonical PQ reward relationships and maintained PQ mechanics instead of unqualified community claims.
- Evidence boundary: no farming relationship, reward edge, or canonical identity was added/removed. Historical/research-batch mentions of PQ23 remain untouched where they are provenance/history rather than current presentation consumers.
- Validation: changed files re-read from `main`; current changed-file content contains no stale PQ23 route claim or PQ4 farming claim. Search results may still surface historical/research-index matches, which were not rewritten because they are evidence/provenance records.
- CI: no successful workflow/status exposed; no CI success claimed.
- Commits: `0a2b780bb1aed91f6d4e87ddfe643ff69c9af0c9`, `e72e09b3827534cf571a18e43de61377e94a14a0`.
- Exact next batch: audit the remaining **PQ-facing reward/acquisition summaries** surfaced by the canonical search, prioritizing `docs/Guides.md`, `docs/Skills-Complete-Database.md`, `docs/QQ-Bangs.md`, and any summary/index page that presents a PQ as a direct acquisition route. Repair only deterministic consumer drift and preserve research-batch provenance.

### 2026-09-22 cycle update — PQ acquisition-summary evidence boundary
- Live canonical PQ relationship baseline remains **860 unique edges**: 244 Skills / 151 Super Souls / 125 Equipment / 247 Characters / 86 DLC / 7 farming; canonical PQ layer remains **186 numbered records**.
- Bounded batch: audited docs/Guides.md, docs/Skills-Complete-Database.md, docs/QQ-Bangs.md, docs/Skills-Unlock-Database.md, and docs/Accessory-Acquisition-Matrix.md for PQ acquisition presentation.
- Deterministic issue found in docs/QQ-Bangs.md: PQ83 was described as a community/research farming route without explicitly separating that claim from the canonical pq_features_farming relationship layer.
- Change: clarified that PQ83's QQ Bang route is a community/research acquisition lead and not a canonical farming relationship; the canonical farming relationship layer currently represents Dragon Ball farming relationships.
- Other audited summary pages did not contain a deterministic canonical-source mismatch requiring edits in this bounded pass. Skill/PQ examples remain acquisition records or evidence fields and are not automatically promoted to canonical relationship semantics.
- Validation: changed QQ Bang page re-read from main; searches confirm the PQ83 distinction is explicit. No canonical relationship edge or identity changed.
- CI: no successful workflow/status exposed; no CI success claimed.
- Commit: b3ea172a93a434ec5fb4e82d207b363fdc5b9266.
- Exact next batch: continue the PQ acquisition-summary census into docs/Skills-Unlock-Database.md, docs/Accessory-Acquisition-Matrix.md, and high-volume skill research/index consumers, looking specifically for claims that convert a PQ association into a guaranteed drop, Ultimate Finish requirement, or canonical farming relationship without supporting canonical evidence.

### 2026-09-22 cycle update — PQ skill reward-trigger evidence cleanup
- Audited `docs/Skill-Unlock-Methods.md`, `docs/Skills-Database.md`, `docs/data/parallel-quest-skill-acquisition-model.json`, and `docs/data/pq-cross-domain-index.md` for unsupported PQ reward-trigger semantics.
- Deterministic drift found: two summary pages described Ultimate Finish as broadly improving PQ skill results, which could be read as a guaranteed reward mechanic.
- Changes: rewrote both summary statements so PQ skill associations, Ultimate Finish conditions, and actual reward triggers remain separate evidence fields; the canonical acquisition model already explicitly forbids converting an Ultimate Finish requirement into a guaranteed drop without evidence.
- Accessory acquisition matrix remained correctly bounded: it explicitly states that reward listings do not become guaranteed-drop claims and that PQ associations remain separate from exact reward mechanics.
- No canonical relationship edge or identity was added/removed; 860-edge / 186-record baseline unchanged.
- Validation: changed skill pages re-read from `main` and contain the new evidence boundary.
- CI: no successful workflow/status exposed; no CI success claimed.
- Commits: `862a75d70f1895f032ff31652d1e2fdeaeda5489`, `8248441622d54ba2cfef8e60825e6bddb32ffd48`.
- Exact next batch: continue the high-volume skill research/index census for direct statements that equate PQ association, Ultimate Finish, enemy appearance, or reward-table presence with a guaranteed acquisition trigger; repair only deterministic presentation drift and preserve research evidence.

### 2026-09-22 cycle update — canonical authority clarified in PQ skill acquisition model
- Continued the high-volume skill research census across multiple `skill-research-batches` records, including DLC PQ batches and reconciliation data.
- Confirmed that research records intentionally preserve evidence such as `ultimate_finish_required=true` when an explicit source supports it, while verification status can remain research-layer metadata. These fields must not be mistaken for canonical PQ relationship authority.
- Added an explicit `canonical_authority` rule to `docs/data/parallel-quest-skill-acquisition-model.json`: canonical relationship data is the source of truth for PQ-to-skill relationships; research fields (`ultimate_finish_required`, `trigger_scope`, `guarantee_status`, `drop_rate`) are evidence metadata and cannot override canonical identities/edges.
- No canonical relationship edge or identity was changed; 860-edge / 186-record baseline remains unchanged.
- Validation: model was updated directly on `main`; no CI success claim made.
- Commit: `8a2f8cf4e9d9e34f15157fb26775f939c160619c`.
- Exact next batch: continue auditing high-volume skill research batches for any presentation/consumer that promotes research-layer Ultimate Finish, enemy-drop, or guarantee fields into canonical relationship claims; preserve explicit research evidence while preventing source-layer confusion.

### 2026-09-22 cycle update — high-volume skill acquisition-summary authority cleanup
- [x] Continued the P1/high-volume skill research consumer census, focusing on PQ acquisition summaries that could blur canonical relationships with research-layer reward mechanics.
- [x] Audited docs/Skill-Unlock-Methods.md, docs/Skills-Database.md, and docs/Skills-Complete-Database.md against docs/data/pq-reward-relationships.json and docs/data/parallel-quest-skill-acquisition-model.json.
- [x] Repaired deterministic presentation drift: mentor rewards are now described as lesson-specific; PQ skill summaries explicitly separate canonical PQ→skill association from Ultimate Finish, trigger, guarantee, enemy-source, and drop-rate claims; the broad “often on Ultimate Finish” wording was removed.
- [x] Added docs/data/skill-pq-acquisition-presentation-audit.json documenting the repaired consumers and evidence boundary; registered it in docs/data/pq-cross-domain-index.json.
- [x] Canonical baseline preserved: 860 total PQ relationship edges / 244 PQ→skill edges; no canonical skill identity or relationship edge was added, removed, or renamed.
- [x] Validation: changed files were fetched from main after mutation; audit JSON parses structurally; no CI success claimed because no successful workflow/check was exposed.
- [x] Commits: 16544a3b74226fb3f0b9c348f27216bd0c927022, 876778fb3b4fd9d679884c18f0574ce0b07bd932, b4adaa2db9933ba29cd6215f01908a2652c658e8, a3833e708150bebe02d23deb1430a80482eefbf2, ceb227886c58e0b97d09d44452101ad55086f9a6, b436ee925ac97ec0c19b886017478917811d6040, c9192e3668c9e3351fc3d5d38762cab534442269.
- [ ] Exact next batch: continue the high-volume skill research/index census beyond these summary consumers, prioritizing records or presentation pages that directly turn ultimate_finish_required, trigger_scope, guarantee_status, enemy appearance, or reward-table presence into user-facing guaranteed-acquisition claims. Preserve research evidence and only repair deterministic consumer drift; do not rewrite unresolved research records into canonical facts.


### 2026-09-22 cycle update — skill farming and unlock consumer cleanup
- [x] Continued the high-volume skill research/index census into secondary acquisition and farming consumers.
- [x] Repaired docs/Skills-Unlock-Database.md, docs/Farming-Hub.md, and docs/Farming-Routes.md so generic PQ/Ultimate-Finish wording no longer converts a canonical PQ→skill relationship into an unsupported reward-trigger claim.
- [x] Extended docs/data/skill-pq-acquisition-presentation-audit.json with these three consumers.
- [x] Preserved the canonical authority boundary: canonical PQ→skill relationships identify the association; Ultimate Finish, trigger, guarantee, enemy-drop, and probability fields require independent evidence.
- [x] No canonical relationship edge or skill identity was changed. Research records were not rewritten merely to remove uncertainty.
- [x] Validation: all three changed documents and the audit file were fetched from main after mutation. No CI success claimed.
- [x] Commits: d4048b0fb6dbd9f12c365e460aaf139c85201109, 94eaaeb9132b65080521506de0c76d585b43e6fc, b2ebb9201938159bb6744d31f81b7eb5d83e8ba2, abcfc704af20e66a608a3e03a68551c4af163499.
- [ ] Exact next batch: continue the skill consumer census into remaining high-volume presentation/index pages and validator assumptions, especially any consumer that renders research-layer Ultimate Finish or acquisition fields as definitive canonical unlock mechanics. After the presentation layer is clean, audit canonical/index synchronization and stale skill-record metadata before expanding the next data domain.


### 2026-09-22 cycle update — canonical/research semantic consistency pass
- [x] Continued the skill acquisition census into the structured PQ evidence layer and discovered one deterministic semantic conflict in `docs/data/parallel-quest-skill-acquisition-early-base-game.json`.
- [x] Repaired the Kaioken / PQ8 record: the record previously declared `route_type=ultimate_finish`, `finish_scope=ultimate`, and `guarantee_status=conditional` while its own evidence explicitly said the current reward roll remained unresolved.
- [x] Preserved the historical Ultimate Finish association in `trigger_scope`, but changed route/finish/guarantee fields to `unknown` until independently verified. This prevents research uncertainty from becoming a canonical mechanic.
- [x] Repaired the remaining `docs/Skills-Unlock-Database.md` table wording and kept the presentation audit current in `docs/data/skill-pq-acquisition-presentation-audit.json`.
- [x] No canonical PQ→skill edge or canonical skill identity was changed.
- [x] Validation: re-fetched the modified JSON and presentation files from `main`; the Kaioken record now has internally consistent unresolved semantics. No CI success claimed.
- [x] Commits: 95405e32c2fbd74b5c3f164e22e639d83827340b, 275f47966c38a9479f7ad365b2e1888ed12003c3, 013589b952bc00198c0395c050dbb796506951f5.
- [ ] Exact next batch: continue scanning the structured PQ acquisition evidence for records where `route_type`, `finish_scope`, or `guarantee_status` are more definitive than their `trigger_scope`, evidence, verification status, or notes justify. Repair only those semantic contradictions while preserving historical evidence; then audit canonical/index synchronization before expanding domains.


### 2026-09-22 cycle update — PQ acquisition model consistency pass
- [x] Audited the structured PQ acquisition reconciliation/model layer after the previous semantic repair.
- [x] Found and repaired a second deterministic contradiction: the acquisition model's Kaioken/PQ8 example still encoded `ultimate_finish` + `conditional` even though the maintained evidence record now explicitly treats the current trigger and guarantee as unresolved.
- [x] Changed the model example to `unknown` route/finish/guarantee semantics while retaining the historical Ultimate Finish association as an evidence note.
- [x] Added an explicit model rule preventing unresolved trigger notes from being promoted into definitive route/finish/guarantee fields without stronger independent evidence.
- [x] Extended `docs/data/skill-pq-acquisition-presentation-audit.json` with this model audit.
- [x] Canonical `docs/data/pq-reward-relationships.json` remains the source of truth for the PQ→skill edge; no canonical relationship or skill identity was changed.
- [x] Validation: modified model and audit were re-fetched from `main`; no CI success claimed.
- [x] Commits: 8f26cfa7ef2205e44b759a7d1e1ef9edb2b213eb, dc066d67a5bf92fbda8377bc38ec6e34fa03d729.
- [ ] Next batch: audit canonical/index synchronization and stale skill-record acquisition metadata, especially `ultimate_finish_required`/`source_quest` fields that may conflict with canonical PQ relationships or explicit unresolved research evidence.


### 2026-09-22 cycle update — canonical skill/index PQ crosslink synchronization
- [x] Audited canonical skill/index synchronization after the PQ acquisition semantic pass.
- [x] Found a deterministic cross-domain schema/projection gap: `docs/data/skills.json` contained `source_parallel_quests` on 239 canonical skill records, while `docs/data/skills.schema.json` did not declare the field and `scripts/build_skills_from_research.py` did not project it into `skills-index.json`.
- [x] Updated `docs/data/skills.schema.json` to explicitly define `source_parallel_quests` as canonical PQ identifiers, with the authority boundary that it represents relationships rather than reward-trigger/guarantee semantics.
- [x] Updated `scripts/build_skills_from_research.py` so future deterministic index builds retain `source_parallel_quests`.
- [x] Synchronized `docs/data/skills-index.json`: all 239 canonical PQ crosslinks are now projected, with all 452 canonical/index records matching across the 17-field projection.
- [x] Audited Ultimate Finish metadata at the same time: 0 canonical records with `ultimate_finish_required=true` lacked explicit Ultimate Finish/UF provenance in `unlock_method` or `source_quest_or_shop` under the validator invariant.
- [x] Extended `docs/data/skill-pq-acquisition-presentation-audit.json` with the schema, builder, and index repairs.
- [x] Canonical PQ→skill relationships remain authoritative; no canonical skill identity or PQ relationship edge was changed.
- [x] Validation: re-fetched canonical skills, index, builder, schema, and audit; deterministic projection comparison reports 452/452 synchronized records and 239/239 PQ crosslinks. No CI success claimed.
- [x] Commits: 40633ae873995ed2aa4dd0f59a13c6f7c570ea8d, dde5d636948e4b9181d4a412c78d2eb11a6ef80f, ffb998635177655c73f3a26460d18626226fb604f0, 98ca0a9a844fecd47664785c815b4f04737587f0, 115fb5db0229e1d6021c4b1d5b90b1b202109884, 0231e0834aec30f508e2822a9614db27da66e9e8, d881d2cc45ced4241f30aa150316b43e4c676673.
- [ ] Next batch: audit remaining stale canonical skill acquisition metadata against the canonical PQ relationship graph, prioritizing `source_quest`, `source_quest_or_shop`, `unlock_method`, and `ultimate_finish_required` contradictions where a deterministic canonical relationship or explicit evidence already establishes a different value. Preserve unresolved research conflicts rather than normalizing them away.


### 2026-09-22 cycle update — canonical skill acquisition metadata reconciliation
- [x] Compared all 452 canonical skill records against the canonical PQ→skill relationship graph for `source_parallel_quests` synchronization.
- [x] Found one deterministic mismatch: Kamehameha listed only PQ05 in skill metadata while `docs/data/pq-reward-relationships.json` currently contains canonical `pq-005` and `pq-048` edges for Kamehameha.
- [x] Synchronized Kamehameha metadata and the skill index to [5,48]. The canonical PQ relationship graph itself was not changed.
- [x] Preserved the existing research conflict as an explicit note instead of overriding canonical relationship data: maintained research identifies a possible PQ48/Kamekameha naming conflict, but canonical relationship data remains authoritative for the current cross-domain association.
- [x] Re-ran the deterministic comparison: 452/452 skill records now match canonical PQ crosslinks; all 239 canonical skill targets are synchronized; index crosslinks also match 452/452 records.
- [x] Ultimate Finish metadata remains separately bounded by explicit provenance; no new unsupported Ultimate Finish claim was introduced.
- [x] Extended `docs/data/skill-pq-acquisition-presentation-audit.json` with the reconciliation.
- [x] Validation was performed by re-fetching the live files from `main`; no CI success claimed.
- [x] Commits: 6a2501a5d42ebe33260bd7c37b488e50ca3ba476, e051b774b9fa4cb55d5b0b7f46750ec06c39b0f2, 0448d9f49c0b413c9966417629a27e01b867a7ea.
- [ ] Next batch: continue acquisition-metadata reconciliation beyond `source_parallel_quests`, checking whether `source_quest`, `source_quest_or_shop`, and `unlock_method` agree with canonical PQ associations without promoting research-layer reward-trigger assumptions into canonical facts.


### 2026-09-22 handoff synchronization — PQ reference consumer repair
- [x] Completed and registered the deterministic PQ reference/index repair: docs/Parallel-Quests.md now uses the complete canonical farming set PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88; validator/audit added and cross-domain index registration completed.
- [x] Current canonical relationship baseline remains 860 edges (244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming) across 186 PQ records.
- [x] No canonical relationship identities were added, removed, or renamed.
- [ ] Next continuation gate remains the latest acquisition-metadata task: reconcile skill source_quest, source_quest_or_shop, and unlock_method against canonical PQ associations without promoting research-layer reward-trigger assumptions into canonical facts.


### 2026-09-22 cycle update — standalone PQ reverse-index semantics repair
- [x] Live skill acquisition census: **452 canonical skills**, **244 canonical PQ→skill edges**, with only five intentional multi-PQ records whose `source_quest` / `source_quest_or_shop` retains a primary route while `source_parallel_quests` preserves the complete canonical relationship set: Candy Beam, Kamehameha, Mach Dash, Time Control, and Warp Kamehameha. No deterministic acquisition contradiction was found; secondary PQ relationships were not incorrectly collapsed into a single source-quest field.
- [x] Audited standalone PQ reverse indexes for PQ81-186 against the unified reverse projection. The standalone artifacts are source-normalized partial projections, so differences from the unified canonical layer are not automatically defects.
- [x] Found canonical-vs-source-layer drift in the standalone artifacts: PQ81-120 (1 missing / 7 extra exact pairs), PQ121-142 (0 / 0), PQ143-162 (0 / 9), PQ163-186 (2 / 5). Examples include spelling/normalization variants such as `Starfall` vs `Destruction's Concerto: Starfall` and capitalization variants in late Super Soul names.
- [x] Corrected `scripts/validate_pq_reverse_indexes.py`: standalone-vs-normalized-source mismatches remain hard failures; standalone-vs-unified-canonical differences are now explicitly informational because the source layer is documented as partial and must not override canonical relationships.
- [x] Added `docs/data/pq-reward-normalization/pq-standalone-reverse-index-audit.json` documenting the exact live drift and evidence boundary.
- [x] No canonical relationship, PQ identity, reward identity, or source-map record was rewritten merely to eliminate projection differences.
- [x] Validation: re-fetched the validator and audit artifact from `main`; audit JSON is structurally valid and the validator contains the new hard-vs-informational comparison rule. CI success not claimed.
- [x] Commits: `d19da20aa5ad21ce1561b7f32c213df5aeff9e12`, `197ed83dd060592fdcf24f9e43498ad787c0a97c`.
- [ ] Exact next batch: inspect the standalone-vs-normalized-source pair sets themselves for any hard projection mismatches; if clean, move to the next highest-impact cross-domain producer/consumer drift rather than normalizing partial research indexes to the canonical relationship layer.


### 2026-09-22 cycle update — skill acquisition metadata invariant validator
- [x] Live census: **452 canonical skills / 244 canonical PQ→skill edges**.
- [x] Reconciled all 452 `source_parallel_quests` sets against canonical `pq_rewards_skill` edges: **0 mismatches**.
- [x] Checked explicit PQ numbers parsed from `source_quest` and `source_quest_or_shop`: **0 values outside the canonical relationship set**.
- [x] Confirmed five intentional primary-route subsets remain valid: **Candy Beam, Kamehameha, Mach Dash, Time Control, Warp Kamehameha**. Their primary source fields name one PQ while `source_parallel_quests` retains the complete canonical association set; this is not treated as an error.
- [x] Added `scripts/validate_skill_acquisition_metadata.py` with the invariant: complete PQ relationships must match the canonical graph; primary source fields may identify a subset but may not name an unrelated PQ.
- [x] Registered the validator in `docs/data/skill-pq-acquisition-presentation-audit.json` and `docs/data/pq-cross-domain-index.json`.
- [x] No canonical relationship, skill identity, reward trigger, Ultimate Finish condition, or drop mechanic was inferred or changed.
- [x] Validation: live records and relationship graph were re-fetched from `main`; deterministic census is clean. CI success unavailable/not claimed.
- [x] Commits: `b7ac366aceec5b82e8e36ceb4d1a2ed35e35b5eb`, `5143709040feae4f29edb158a5f498ae589c2030`, `59815deeb3c725f423dfbddacc6e6197f68d8c1d`.
- [ ] Exact next batch: audit remaining high-volume skill consumer/index pages for stale `source_quest`, `source_quest_or_shop`, `unlock_method`, or Ultimate Finish wording that presents a primary route as the complete acquisition condition; use the new validator invariant and canonical relationship layer as the boundary.

### 2026-09-22 cycle update — acquisition presentation census
- [x] Audited all **452 canonical skill records** beyond `source_parallel_quests`, checking `source_quest`, `source_quest_or_shop`, and `unlock_method` PQ references against the canonical PQ association set.
- [x] Result: **0 PQ references outside the canonical set**; **0 PQ-linked skills missing an explicit PQ number** in acquisition presentation fields.
- [x] All **239 PQ-linked skills** use acquisition types `parallel_quest` or `quest_or_mission`; no PQ-linked skill is currently classified under an incompatible acquisition type.
- [x] Checked Ultimate Finish wording against flags. The only `ultimate_finish_required=false` record whose acquisition text mentions UF is **Drain Field**; its record explicitly documents conflicting community reports and therefore remains an intentional unresolved research conflict rather than a deterministic contradiction.
- [x] Updated `docs/data/skill-pq-acquisition-presentation-audit.json` with the census results.
- [x] No canonical PQ→skill edge or skill identity was changed; no unresolved research claim was promoted to a canonical mechanic.
- [x] Validation: live `skills.json` and relationship data were re-fetched from `main`; deterministic census is clean. CI success not claimed.
- [x] Commit: `4c080d76336b1582d17e3973b1474b42e00a9851`.
- [ ] Exact next batch: inspect generated/index consumer surfaces and stale documentation examples for one-way or misleading acquisition presentation; prioritize places where canonical PQ relationships exist but the UI/page exposes only a primary route without an obvious path to the complete PQ association set.

### 2026-09-22 cycle update — skill explorer reverse PQ navigation
- [x] Audited the generated skill explorer consumer `docs/Skills-All.html` against the canonical `pq_rewards_skill` graph.
- [x] Found a real presentation gap: skill records exposed primary acquisition/source text but did not provide explicit navigation to **every canonical PQ association**.
- [x] Repaired `docs/Skills-All.html` to render **Canonical PQs** from `source_parallel_quests`, with deterministic links into `Parallel-Quests-All.html?q=PQ <id>`; the search corpus also indexes the PQ association field.
- [x] Added `scripts/validate_skills_pq_reverse_navigation.py` to enforce exact equality between each skill's `source_parallel_quests` set and canonical `pq_rewards_skill` edges.
- [x] Live validation result: **452 skills / 244 canonical PQ→skill edges / 0 reverse-set mismatches**.
- [x] Registered the audit/validator in `docs/data/skill-pq-acquisition-presentation-audit.json` and `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary preserved: PQ links establish canonical relationship identity only; they do not imply guarantees, Ultimate Finish requirements, drop rates, or other acquisition mechanics.
- [x] Commits: `5ab0d53b730579d54d142f847bc82f306adaad6e`, `18264b35df9a4b1c477caece6014df207b26451d`, `a82e5ddd7d86f4d83246cbbf0bc66a347a9bd1fa`, `638ed09c71e62c3ea1f2a5e381e6a4456f037300`.
- [ ] Exact next batch: continue auditing other generated cross-domain consumers for one-way navigation gaps, prioritizing Super Soul/equipment/accessory reverse navigation from their canonical records back to all PQs.

### 2026-09-22 cycle update — Super Soul/equipment reverse PQ navigation
- [x] Audited the canonical Super Soul and equipment/accessory record layers against the PQ relationship graph and existing presentation consumers.
- [x] Found a presentation gap: PQ explorer could link these reward targets into generic Search, but canonical Super Soul/equipment records had no dedicated consumer exposing all reverse PQ associations.
- [x] Added `docs/Super-Souls-All.html` and `docs/Equipment-All.html`, both loading canonical record data plus `pq-reward-relationships.json` and exposing deterministic **Canonical PQs** links.
- [x] Added `scripts/validate_record_reverse_pq_navigation.py` and `docs/data/record-reverse-pq-navigation-audit.json`.
- [x] Live relationship census: **151 Super Soul edges / 148 unique targets / 0 unresolved targets** and **125 equipment edges / 123 unique targets / 0 unresolved targets**.
- [x] Registered the audit and validator in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary preserved: reverse links establish canonical relationship identity only; they do not imply reward guarantees, Ultimate Finish requirements, drop rates, or unresolved acquisition claims.
- [x] Commits: `3ce1fa87e7f13c44e6f6c147201db03abefc4c8e`, `aef16457a78005c2eecfd8527f66ae2e9348b4a2`, `f03893cab88e1a6067bc446b068c13162b032210`, `8cb91d504ffbdc9b8a956c4b201684ba98ad4757`, `4cd5a49c1afbbbd491be2cd4305e934d5c055c2b`.
- [ ] Exact next batch: audit the newly created Super Soul/equipment explorers plus their source acquisition fields for primary-route-only presentation, then continue to the next canonical cross-domain record consumer.

### 2026-09-22 cycle update — Super Soul/equipment acquisition crosslink synchronization
- [x] Live census before editing: **234 canonical Super Soul records / 151 canonical PQ→Super Soul edges / 148 unique targets** and **174 equipment/accessory records / 125 canonical PQ→equipment edges / 123 unique targets**.
- [x] Audited the newly created docs/Super-Souls-All.html and docs/Equipment-All.html reverse-PQ consumers together with their canonical record layers and docs/data/pq-reward-relationships.json.
- [x] Found a deterministic structured-field drift in docs/data/super-souls-record-layer.json: **82 linked records** had source_parallel_quests values that were incomplete or malformed (pq-pq-###) relative to the canonical relationship graph. Synchronized all linked Super Soul source_parallel_quests sets to the exact canonical PQ set; no relationship edges were changed.
- [x] Found five deterministic equipment structured-field mismatches: acc-001 Piccolo's Turban, acc-012 Goku Wig (Super Saiyan), acc-028 Yamcha's Sword, acc-058 SSGSS Goku Wig, and equip-090 Whis Symbol Gi. Synchronized parallel_quest_ids to the canonical PQ relationship set while preserving all existing acquisition-route conflict prose and notes.
- [x] Extended scripts/validate_record_reverse_pq_navigation.py to require exact structured PQ-set parity, while treating conflicting acquisition prose as an explicit evidence conflict rather than silently normalizing it.
- [x] Updated docs/data/record-reverse-pq-navigation-audit.json to record structured-field parity and the two preserved equipment route conflicts: Goku Wig (Super Saiyan) documents PQ18 alongside canonical PQ63; SSGSS Goku Wig documents PQ76 alongside canonical PQ66.
- [x] Validation: live re-fetch confirms the modified Super Soul and equipment JSON, validator, and audit are present on main; deterministic structured PQ parity is **0 mismatches** for both domains, **0 unresolved canonical targets**, and reverse consumers remain structurally wired to the canonical relationship graph. No CI success claimed.
- [x] Commits: 0dc966428756adf1968039d2ffb50fc0a10d2920, 79fc8e5d84a5394384f69a381f9967693c8664ff, 0c100b9b09bdb411aebf9cdb0a9eaf59765295e9, 6cba08cf8e17c5bd22863708e955692a98f61031.
- [ ] Exact next batch: continue the canonical cross-domain consumer audit beyond Super Souls/equipment, prioritizing **character-facing PQ reverse navigation and preset/Partner Customization consumers**, then repair only deterministic canonical-ID/name drift or one-way navigation gaps while preserving unresolved source conflicts.

### 2026-09-22 cycle update — Partner Customization key → character navigation
- [x] Live census: **20 Customization Unlock Key records** and **29 explicit character_id identity-bridge records**; all 20 key IDs resolve to the exact partner name in the bridge with **0 unresolved IDs / 0 name mismatches**.
- [x] Audited docs/Partner-Customization.md against docs/data/partner-customization-key-record-layer.json and docs/data/characters/character-id-identity-bridge.json.
- [x] Repaired the Partner Customization key table so all **20/20 partner rows** now provide deterministic links into the canonical Search surface (Search/?q=...) instead of leaving the key → character path as prose-only navigation.
- [x] Updated docs/data/partner-customization-key-reconciliation.json with the navigation audit: 20 key rows, 20 search links, 0 missing links, 0 unresolved character IDs, 0 partner-name mismatches.
- [x] Evidence boundary preserved: these links establish navigation to canonical character search only; they do not infer DLC ownership, character unlock conditions, raid drop guarantees, or TP Medal mechanics.
- [x] Validation: live re-fetch confirms the Partner Customization page and reconciliation audit on main; deterministic key-number coverage is exactly 1–20 and identity-bridge parity is clean. CI success not claimed.
- [x] Commits: 87c157d2aa2eb2c91c1c4d78a1a33a1812d683de, cb49417149337c578ff776ddd999393bad4d5f63.
- [ ] Exact next batch: audit the **character-facing consumer pages/indexes** for the same one-way-navigation problem, prioritizing Character-Core-Profiles.md, Characters.md, character-presets-record-layer.json, and existing character presentation audits; repair deterministic links/canonical-ID drift without inventing character unlock or preset mechanics.


### 2026-09-22 cycle update — canonical character explorer / preset + PQ reverse navigation
- [x] Live census before editing: **149 canonical character identities**, **45 indexed preset records across 17 presentation character_ids**, and **247 explicit PQ→character references across 75 canonical character targets / 143 PQs**.
- [x] Audited existing character presentation contracts: all 45 preset character_ids resolve through the explicit identity bridge; the existing PQ reverse index has 0 orphan targets and 247 reverse entries.
- [x] Added `docs/Characters-All.html`, a canonical character explorer that loads the character record layer, preset record layer, character identity bridge, and PQ reverse index. It exposes searchable character identities, indexed presets, explicit PQ links, and local Search navigation.
- [x] Added `scripts/validate_character_explorer.py` to enforce explorer dataset loading contracts, canonical-target parity, preset-ID bridge resolution, and required navigation surfaces.
- [x] Registered the explorer and validator in `docs/data/characters/character-presentation-consumer-audit.json` and linked the explorer from `docs/Characters.md`.
- [x] Evidence boundary preserved: explorer navigation does not infer complete unlock routes, preset numbering/loadouts, raid rotation, DLC ownership, TP Medal costs, drop rates, or historical chronology.
- [x] Validation: live re-fetch confirms all four changed/new surfaces on `main`; counts remain 149 characters / 45 preset records / 247 explicit PQ references, with 0 unresolved preset IDs and 0 orphan PQ reverse targets. CI success not claimed.
- [x] Commits: `4d5540999d0d96f26f98ab02038efaac7fd75197`, `03ef90bc84da1b23fbec242f59178be5ef1e47e1`, `f85fc316087a8f805e6488a385e682fab6814700`, `935b9ed4dc83022d689f3e58cbca7cca27cb4669`.
- [ ] Exact next batch: audit **character preset consumer presentation** for one-way navigation and identity leakage, beginning with the 45 indexed preset records; add deterministic character links to every preset-bearing surface and explicitly flag the two Captain Ginyu body-swap preset labels as unresolved identity presentation rather than mapping them to Vegeta/Xeno Trunks.


### 2026-09-22 cycle update — preset consumer navigation + identity leakage audit
- [x] Live census: **45 indexed preset records**, spanning **17 presentation character_ids**; all preset IDs resolve through the explicit character identity bridge.
- [x] Audited the preset consumer path and the existing presentation validator. The canonical explorer is the active presentation surface for these indexed preset records.
- [x] Repaired `docs/Characters-All.html` so the character heading on every preset-bearing explorer card links directly to the canonical local Search surface. This closes the preset → character one-way-navigation gap without changing preset mechanics.
- [x] Extended `scripts/validate_character_presentation_consumers.py` to require the preset explorer's canonical Search navigation contract and record its 45-record coverage.
- [x] Updated `docs/data/characters/character-presentation-consumer-audit.json` with a dedicated preset-presentation result and explicit identity-boundary entries for `captain-ginyu-preset-3` and `captain-ginyu-preset-4`.
- [x] Preserved the two Captain Ginyu body-configuration labels as **unresolved identity presentation**; they are not remapped to Vegeta or Future/Xeno Trunks merely because the source labels those body configurations that way.
- [x] Evidence boundary preserved: no new claim was made about complete preset numbering, loadouts, unlock routes, DLC ownership, raid rotation, TP Medal costs, drop rates, or historical numbering changes.
- [x] Validation: live re-fetch confirms the explorer, validator, and audit updates on `main`; 45/45 indexed preset records remain bridge-resolved and the presentation audit status remains clean. CI success not claimed.
- [x] Commits: `eeef253525ece551b0693b75c8469227403770e4`, `db6cc25ab10ac2288b05a17aef7ddb81f31cbe6c`, `2defb02ec4e87e9709164edcd3599e4cdcdc6aae`.
- [ ] Exact next batch: inspect the **character preset schema + producer layer** for deterministic per-record canonical-name/navigation fields, then audit the 45 records for duplicate IDs, duplicate `(character_id,preset_number)` pairs, and special `record_type` handling without inventing missing preset numbers/loadouts.


### 2026-09-22 cycle update — preset producer uniqueness + special record-type audit
- [x] Live census supersedes the earlier 45-record note: the current `docs/data/character-presets-record-layer.json` contains **40 records**, consisting of **35 numbered `preset` records** and **5 `separate_character` records** with null `preset_number`.
- [x] Audited all 40 producer records for duplicate record IDs: **0 duplicates**.
- [x] Audited all numbered records for duplicate `(character_id, preset_number)` pairs: **0 duplicates**.
- [x] Audited special record handling: all 5 non-numbered records explicitly declare `record_type: separate_character`; no null `preset_number` was converted into an invented preset number.
- [x] Confirmed all current preset producer `character_id` values remain bridge-resolved; existing Captain Ginyu Presets 3/4 remain explicitly unresolved only at the body-configuration identity-label layer.
- [x] Extended `scripts/validate_character_presentation_consumers.py` with deterministic duplicate-ID, duplicate numbered-pair, and explicit-special-record-type checks.
- [x] Corrected `docs/data/characters/character-presentation-consumer-audit.json` to the live 40-record census and recorded the 35/5 record-type split.
- [x] Evidence boundary: the audit establishes producer-layer uniqueness and explicit record typing only. It does not establish complete preset numbering, loadouts, unlock routes, DLC ownership, or historical numbering changes.
- [x] Validation: live re-fetch confirms the validator and audit changes on `main`; duplicate IDs = 0, duplicate numbered pairs = 0, special typed records = 5, unresolved preset character IDs = 0. CI success not claimed. The prior 45-record count is superseded by this live census.
- [x] Commits: `75a3db442111eeac68e0448bc82e979561601e50`, `eabc26cdc8907e873739215c4d3792228a00a629`.
- [ ] Exact next batch: audit **producer-to-presentation parity for the 40 current records**, especially the 5 `separate_character` records and the 2 Captain Ginyu body-configuration labels, then inspect character-facing pages for any remaining hard-coded preset names that bypass the canonical explorer/Search navigation.


### 2026-09-22 cycle update — producer-to-presentation parity hardening
- [x] Re-audited the live 40-record preset producer layer against `docs/Characters-All.html` and the explicit character identity bridge.
- [x] Confirmed the explorer derives character presentation through the bridge and provides canonical Search navigation for the preset-bearing identities; no separate preset identity mapping was introduced.
- [x] Hardened `scripts/validate_character_presentation_consumers.py`: it now validates unique preset IDs, unique numbered `(character_id, preset_number)` pairs, an allowlist of `preset` / `separate_character` record types, and the invariant that `separate_character` records remain unnumbered.
- [x] Corrected `docs/data/characters/character-presentation-consumer-audit.json` so its top-level and explorer census matches the live producer layer: **40 records / 17 presentation character IDs** rather than the stale 45-record historical count.
- [x] Validation result from deterministic inspection: 0 duplicate IDs, 0 duplicate numbered pairs, 0 invalid record types, 0 special-record numbering conflicts, 40/40 producer records covered by explorer navigation, and 0 unresolved bridge IDs. CI success not claimed.
- [x] Evidence boundary preserved: this validates producer/presentation identity and structural parity only; it does not establish complete preset numbering, loadouts, unlock routes, DLC ownership, or historical numbering.
- [x] Commits: `c368209bd74663c5c0d3a755354ed9018db24e07`, `b764c3799bf8332b4254ee1bfff5cae2f22f20eb`.
- [ ] Exact next batch: inspect character-facing Markdown/HTML consumers for hard-coded preset labels or alternate preset lists, then either route them through the canonical explorer/Search surface or record why they are intentionally separate evidence surfaces.


### 2026-09-22 cycle update — equipment detail enrichment: equip-031–040
- [x] Completed bounded enrichment for 10 canonical equipment/accessory endpoints: Tuxedo, Wedding Dress, Arabian Costume, Goku Wig (Ultra Instinct), Janemba Suit, Janemba Head, Broly (Full Power Super Saiyan)'s Clothes, SSGSS Gogeta's Clothes, Broly Wig (Legendary Super Saiyan), and Kakunsa's Clothes.
- [x] Reconciled deterministic category and slot coverage from the maintained DBXV2 equipment catalog plus corroborating independent documentation: clothing/accessory classification is now explicit; Tuxedo/Wedding Dress are upper/lower/feet without hands; Arabian Costume is upper/lower/hands without feet; Janemba Suit and Kakunsa's Clothes are four-piece sets; the Broly Full Power and SSGSS Gogeta sets are four-piece; Goku UI Wig, Janemba Head, and Broly Legendary Super Saiyan Wig are accessories.
- [x] Preserved exact uncertainty boundaries: no reward probability, drop guarantee, or unsupported clothing combat/stat effect was invented. Accessory cosmetic classification was only applied to the three clearly accessory/wig records.
- [x] Preserved existing canonical DLC provenance: Extra Pack 2 (PQ121), Extra Pack 3 (PQ123/125/127), Extra Pack 4 (PQ130/131/132), Ultra Pack 1 (PQ133).
- [x] Added docs/data/equipment/equipment-031-040-detail-audit.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Updated both equipment record layers so category/slot metadata is available to downstream consumers without changing canonical relationship identities.
- [x] Validation: 139 records in equipment-record-layer.json; 174 combined equipment/accessory records; 0 duplicate IDs in either layer; all 10 batch records have category, slot coverage, PQ source, and DLC provenance; canonical equipment relationship layer remains 125 forward edges / 123 unique targets / 0 unresolved / 0 broken endpoints.
- [x] Evidence sources include the maintained equipment catalog, maintained all-186 PQ guide, and independent Janemba/Kakunsa/Arabian slot documentation. Web verification also confirms Extra Pack 4's three relevant costumes and Ultra Pack 1's Kakunsa costume provenance.
- [ ] CI: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: d210aeb5ce0e11db5d6a0501b731baca0dc090a8, db5d6b71e618ee28d089523d61331aca59a5d9e8, 1d81110d97e328ad9f99d3874305c89ac5d729d1, 3a276172456fbbdc0a45c5f308ceea6896f0c1d8.
- [ ] Exact next batch: enrich equip-041–equip-050 with independently verified category/slot coverage, restrictions/effects, and DLC provenance; synchronize both equipment layers, preserve unresolved reward/drop semantics, and re-run canonical endpoint/relationship parity.


### 2026-09-22 cycle update — equipment detail enrichment equip-041–050
- [x] Live census before editing: 139 canonical equipment records and 174 combined equipment/accessory records; target batch was equip-041 through equip-050.
- [x] Enriched all 10 records with explicit category and slot coverage: Kakunsa accessories, Rozie full clothing/accessory, Android 21 Lab Uniform upper-body-only, Universe 7 full uniform + cap, Universe 6 upper/lower/feet without hands, and Gine full clothing + accessory.
- [x] Added explicit restrictions where supported, including Android 21 Lab Uniform being upper-body-only and Universe 6 Baseball Uniform lacking hands; preserved uncertainty rather than inventing mechanics.
- [x] Added docs/data/equipment/equipment-041-050-detail-audit.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Evidence used: maintained DBXV2 Equipment catalog; Dragon Ball Wiki character/equipment documentation; GameFAQs evidence for Android 21 Lab Uniform and Universe 6 Baseball Uniform; Bandai Namco documentation for Gine clothing; maintained PQ guide for acquisition endpoints.
- [x] Validation: 139 equipment records, 174 combined records, 0 duplicate IDs; all 10 batch records have category, slot coverage, PQ source, and DLC provenance. Canonical PQ equipment graph remains 125 forward edges / 123 unique targets, with all 10 batch names present as source-backed relationships and 0 unresolved/broken endpoints.
- [x] Evidence boundary: no reward probability, guaranteed-drop claim, or unsupported combat/stat effect was promoted. Accessory records are cosmetic only where the item identity is explicitly an accessory.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: a553707af0aeb34bf155fb001f556ef6a676c6e4, 627f624049575b4aaae8a41f4facabba20ec61b3, a0c353cd69a62109927a0fe3a3fcdf2a3c4c9d81, bf93107a82e02082d4dbc696339f53292e12cddf, 319ccedb835c4452044c838382055137525b06bd.
- [ ] Exact next batch: continue equipment enrichment with **equip-051–equip-060**, using the same two-layer synchronization, independent slot/category verification, and canonical PQ relationship parity checks.


### 2026-09-22 cycle update — equipment detail enrichment equip-051–060
- [x] Live census: `equipment-record-layer.json` remains **139** records; `equipment-accessories-record-layer.json` remains **174** records. The batch contains 10 legacy equipment endpoints, with `equip-057` already normalized to canonical accessory identity `acc-059` and therefore not duplicated.
- [x] Enriched `equip-051`–`equip-060` with source-backed category and slot coverage across both canonical/legacy projections. Bardock, Caulifla, Kale, Android 17 Ranger, and King Vegeta clothing are four-piece sets; Bulma (Kid)'s Clothes are upper-body/hands/feet with no lower-body piece; Caulifla/Kale/Bulma/Android 17 wigs are accessories.
- [x] Preserved canonical accessory identity: `equip-057` remains a historical endpoint only; `acc-059` is authoritative for Bulma (Kid) Wig.
- [x] Added `docs/data/equipment/equipment-051-060-detail-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence: maintained DBXV2 Equipment catalog establishes slot coverage; maintained all-PQ guide establishes PQ reward endpoints; DLC documentation establishes Legendary Pack 1/2 and Conton City Vote Pack provenance. The maintained PQ guide specifically documents PQ147 Caulifla, PQ148 Kale, PQ149 Bulma (Kid), PQ152 Android 17 Ranger, and PQ154 King Vegeta rewards.
- [x] Validation: legacy equipment IDs duplicate count **0**; canonical combined-layer duplicate count **0**; all 10 canonical batch identities have category/slot coverage; all 10 PQ reward relationships are source-backed; equipment graph remains **125 forward edges / 123 unique targets / 0 unresolved / 0 broken endpoints**.
- [x] Evidence boundary: no reward probability, guaranteed-drop claim, or unsupported combat/stat effect was promoted. Accessory cosmetic status was applied only to explicit wig/accessory identities.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: `030abcbced14d7d5dac95ce61ed92be42cf246b6`, `9f29ab5ef79c09099d50e5f881bf457af9b115a7`, `0dd715d2f4d652a6b3197a47aee69f7e693d2f91`, `91f63f45a86e9a17ec0c61ec7921d40dac098342`.
- [ ] Exact next batch: continue the equipment/accessory identity stream with **equip-061–equip-070**, first reconciling any legacy accessory canonicalizations before adding slot/detail metadata, then validate PQ relationship parity.


### 2026-09-22 cycle update — equipment detail enrichment equip-061–070
- [x] Live census: `equipment-record-layer.json` remains **139** records and `equipment-accessories-record-layer.json` remains **174** records; no new canonical identities were created during this bounded pass.
- [x] Enriched `equip-061`–`equip-070` with source-backed category and slot coverage: King Vegeta wig, Gamma 2 helmet, Gamma 1 helmet, Dr. Hedo hood, Red Ribbon Army helmet, Gohan (Beast) wig, and Goku wig are accessories; Gamma 2's Clothes, Red Ribbon Soldier 94 Clothes, and Dr. Hedo Suit are four-piece clothing sets.
- [x] Preserved existing canonical distinctions rather than collapsing similar names: `Gamma 2 Helmet` remains the legacy/equipment endpoint `equip-062`, while the distinct `Gamma 2's Helmet` canonical accessory remains `acc-067`; previously normalized accessory endpoints remain canonicalized.
- [x] Added `docs/data/equipment/equipment-061-070-detail-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence: maintained DBXV2 Equipment catalog establishes clothing slot coverage and accessory classification; maintained PQ guide supplies acquisition endpoints; DLC documentation corroborates the relevant DLC grouping. Independent documentation also identifies the Hero of Justice Pack 2 costume/accessory set and the Gamma helmet accessories. cite
- [x] Validation: legacy equipment IDs duplicate count **0**; combined-layer duplicate count **0**; all 10 batch identities have category/slot coverage; all 10 PQ reward relationships are source-backed; equipment graph remains **125 forward edges / 123 unique targets / 0 unresolved / 0 broken endpoints**.
- [x] Evidence boundary: no reward probability, guaranteed-drop claim, or unsupported combat/stat effect was promoted. Explicit accessories are marked cosmetic; clothing mechanics remain unresolved unless separately evidenced.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: `52f79582065e4b5851457477f408a8b71e232e10`, `3f96bfca0510843aee2d0ade8b33fbfd08212ade`, `56dbfa0e022db67ff9175ef5d023ff77de7cb775`, `977cbfb571f21a4c09db8022b17742ccc4ce3bc0`.
- [ ] Exact next batch: continue equipment/accessory enrichment with **equip-071–equip-080**, first checking the live canonical accessory bridge for any normalized legacy endpoints, then enrich slot/category metadata and validate PQ cross-links.


### 2026-09-22 cycle update — equipment detail enrichment equip-071–080
- [x] Live census: `equipment-record-layer.json` remains **139** records and `equipment-accessories-record-layer.json` remains **174** records; no new canonical identity was created in this pass.
- [x] Reconciled existing canonical accessory bridges before enrichment: `equip-071` Dore's Scouter → `acc-053`, `equip-074` Yamcha's Sword → `acc-028`, and `equip-080` Piccolo's Turban → `acc-001`.
- [x] Enriched the 10 legacy endpoints with source-backed category/slot metadata in both projections. Accessory records: Dore's Scouter, Yamcha's Sword, Perfect Cell's Wings, Piccolo's Turban. Clothing: Hercule's Clothes, Goku's Turtle Hermit Gi (No Character), Cell's Suit (Perfect), Yamcha's Baseball Uniform, Vegito's Clothes, and Goku's Damaged Turtle Hermit Gi.
- [x] Slot details include known partial sets: Cell's Suit (Perfect) has upper/lower/feet and no hands; Goku's Damaged Turtle Hermit Gi has upper/lower only with no hands/feet. The maintained equipment catalog lists the full four-piece sets for Goku's No Character Gi, Yamcha's Baseball Uniform, and Vegito's Clothes.
- [x] Added `docs/data/equipment/equipment-071-080-detail-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence: maintained DBXV2 Equipment catalog establishes slot coverage; maintained PQ sources establish the reward endpoints; repository reverse indexes confirm existing accessory normalization. cite
- [x] Validation: legacy equipment IDs duplicate count **0**; combined-layer duplicate count **0**; all 10 batch records have category/slot coverage; the batch maps to **11** source-backed PQ relationship edges because Hercule's Clothes is independently rewarded by PQ 21 and PQ 30; overall equipment graph remains **125 forward edges / 123 unique targets / 0 unresolved / 0 broken endpoints**.
- [x] Evidence boundary: no reward probability, guaranteed-drop semantics, or unsupported combat/stat effect was promoted. Existing canonical accessory identities were reused rather than duplicated.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: `a439a7ded94e1d1ce0866439b1260f3a4a5b6fe4`, `83df609e3b554c0b740a8c00f58566dfcf96f156`, `dde741a86cc0eb4b986f3a0ea4bcc689210a8594`, `3faab12527c4973c8b32b730f2580e76f5a39de2`.
- [ ] Exact next batch: continue equipment/accessory enrichment with **equip-081–equip-090**, first reconciling canonical accessory bridges and then validating slot/category metadata against the PQ graph.


### 2026-09-22 cycle update — standalone PQ reverse-index reconciliation
- [x] Live inspection superseded the stale equipment-only continuation target: the repository already contains the later equipment 081–090 classification work and subsequent PQ relationship reconciliation.
- [x] Compared the four maintained standalone reverse indexes for PQ81–186 against their normalized reward maps at exact (domain, target, PQ) pair level.
- [x] PQ81–120 source map contains **109** typed reward pairs, while its standalone reverse index contains **208** indexed pairs; all 109 source pairs are present, but **99 additional standalone pairs** are preserved there.
- [x] PQ121–142, PQ143–162, and PQ163–186 have exact source-map/standalone parity with **0 missing** and **0 extra** pairs.
- [x] Added `docs/data/pq-reward-normalization/pq-standalone-reverse-index-reconciliation-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary: the PQ81–120 normalized map is explicitly partial, so overwriting the standalone index from it would delete 99 existing indexed reward pairs. No destructive regeneration was performed.
- [x] Current canonical relationship baseline remains **860 unique edges**: 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `fa901982930f77898c1d629143305731ef62e858`, `561e1a22e61c97924e3ce24947ee2f598ba083ae`, `0cf877d0a058d9127df0101ff3b58942bedfaa46`.
- [ ] Exact next batch: reconcile the **99 PQ81–120 standalone-only reward pairs** against canonical PQ records and source provenance, domain by domain, then decide whether the normalized source map should be expanded or the standalone projection intentionally retained as a broader historical index.


### 2026-09-22 cycle update — live standalone reverse-index parity correction
- [x] Re-checked the live main branch after the previous PQ81–120 reconciliation entry and found that the documented **99 extra** standalone pairs were not present in the current files; the prior census was stale/incorrect.
- [x] Performed an exact `(domain, target, PQ)` comparison of the live PQ81–120 normalized reward map and standalone reverse index: **109 source pairs / 109 standalone pairs / 0 missing / 0 extra**.
- [x] Reconciled the same typed-domain semantics for the remaining ranges: PQ121–142 **89/89**, PQ143–162 **87/87 typed pairs** with **64 artwork references intentionally excluded** from the standalone typed-domain projection, and PQ163–186 **72/72**; all have **0 missing / 0 extra** typed pairs.
- [x] Corrected docs/data/pq-reward-normalization/pq-standalone-reverse-index-reconciliation-audit.json so it reflects the live pair census and explicitly records that the earlier 99-extra finding is superseded.
- [x] No canonical relationship identity or source-map reward was added, removed, or inferred. The canonical relationship baseline remains **860 unique edges = 244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming**.
- [x] Validation: live source/reverse files were re-fetched and compared at exact typed-pair level; source projection mismatches are **0**. CI success not claimed.
- [x] Commits: 0439fa42c9e661d204802b2e03be6a33924053d6; follow-up correction cb20b279949176a8e10baf75a8bde2e3db80edd.
- [ ] Exact next batch: audit current-state metadata in docs/data/pq-unified-reward-reconciliation.json, docs/data/pq-cross-domain-audit.json, and docs/data/pq-cross-domain-status.json for stale live counts/next-gate text that may still surface superseded 862/88 baselines as current; preserve dated historical records while repairing only deterministic current-state fields.


### 2026-09-22 cycle update — PQ reverse-index tooling handoff reconciliation
- [x] Reconciled the handoff claim that `scripts/generate_pq_reverse_indexes.py` and `scripts/validate_pq_reverse_indexes.py` might be absent: both scripts **do exist on the live repository** and their implementations were inspected directly.
- [x] Generator supports the four maintained normalized-map formats used by PQ81–186, including the legacy PQ121–142 top-level-domain projection and newer nested `indexes` projections; it writes only projection domains and does not modify canonical relationship data.
- [x] Validator supports the same source formats and treats normalized reward maps as the standalone projection source of truth. Standalone source-map parity is a hard validation condition; differences against the unified canonical relationship layer are informational and do not rewrite canonical relationships.
- [x] Live exact pair comparisons independently confirm the four maintained standalone projections are source-map clean: PQ81–120 **109/109**, PQ121–142 **89/89**, PQ143–162 **87/87 typed pairs** plus 64 intentionally excluded artwork references, PQ163–186 **72/72**; all typed projections have **0 missing / 0 extra**.
- [x] Therefore the prior TODO item to restore missing scripts is superseded/closed; no duplicate scripts were created.
- [ ] Exact next task: inspect the **unified reverse-index producer/consumer path** (`pq-unified-reverse-index-1-186.json` and its generating/validation tooling) for deterministic schema drift or stale projection semantics, while preserving its explicitly partial-source meaning and never treating absence as negative evidence.


### 2026-09-22 cycle update — unified reverse-index canonical parity repair
- [x] Audited the live docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json directly against docs/data/pq-reward-relationships.json using exact (canonical target, PQ) pairs and normalized PQ numbering.
- [x] Found and corrected **3 deterministic canonical skill-name projection drifts** without changing any PQ relationship: `Chain Destructo-disc Barrage` -> `Chain Destructo-Disc Barrage` (PQ46), `III Bomber` -> `Ill Bomber` (PQ90), and `Giant Cluster` -> `Gigantic Cluster` (PQ163). Super Souls and equipment subtype union already had exact parity; character/DLC/farming projections were also aligned.
- [x] Unified projection now has exact canonical counts: **244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming = 860 relationships**.
- [x] Added docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json documenting the correction and zero-drift validation state.
- [x] Added read-only scripts/validate_pq_unified_reverse_index.py to machine-check canonical target/PQ parity across all unified domains, with clothing/accessories combined for the single canonical equipment relationship type.
- [x] Registered the new audit and validator in docs/data/pq-cross-domain-index.json.
- [x] Synchronized docs/data/pq-relationship-producer-census.json; its current unified reverse-index reference counts now correctly read **244 / 151 / 125 / 247 / 86 / 7** instead of stale **236 / 137 / 125 / 247 / 86 / 7**. Historical values remain preserved in dated handoff/audit history.
- [x] No canonical relationship identities, PQ assignments, or source records were invented or deleted. This was a projection-key canonicalization and validator/provenance repair only.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: `79935ebddd73b85625cae70b35e97b359fe1494a`, `14815ab2bbe06f718baa2ba829b547c4bebb3541`, `2fe12e70377d34b5916aaeddfb0a2f3f7179f439`, `e5d1e8172cd70dec60bb10b59221284260b59849`, `156913cf4930b686aee7fc56c942664f9b661eb0`.
- [ ] Exact next task: run the same deterministic canonical parity audit across the consumer/presentation projections listed in docs/data/pq-cross-domain-index.json, beginning with scripts/validate_pq_page_consumers.py and the PQ reference/explorer navigation audits; repair only stale current-state projection fields or broken canonical links, never infer new relationships.


### 2026-09-22 cycle update — PQ page consumer structured reward parity
- [x] Audited `docs/Parallel-Quests-All.html` and its canonical `docs/data/parallel-quests-record-layer.json` consumer fields against `docs/data/pq-reward-relationships.json`.
- [x] Found a deterministic structured-consumer gap: the canonical equipment targets `Android 17 (DB Super) Wig` on PQ152 and `Gamma 2's Helmet` on PQ155 were present in each PQ's general `rewards` array but missing from the structured `equipment_rewards` field.
- [x] Repaired only those two exact fields. No canonical relationship, alias, or source record was created/renamed.
- [x] Independent live parity after repair: Skills **244/244**, Super Souls **151/151**, Equipment **125/125** exact `(PQ,target)` pairs; **0 missing / 0 extra** for all three structured reward domains. PQ record layer remains **186 unique IDs / 186 unique numbers**.
- [x] Strengthened `scripts/validate_pq_page_consumers.py` so future validation checks exact canonical-vs-structured reward parity for Skills, Super Souls, and Equipment in addition to its existing page/search contracts.
- [x] Added `docs/data/pq-page-consumer-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Existing endpoint alias/granularity conflicts remain explicitly preserved; this repair used exact canonical target strings already present in the record's general reward list and did not collapse aliases.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `5b68b4ff763e7cef005bc272b9c80e75fb0a7b81`, `80097f9561fb3d5c362e740cfc545684e160ce53`, `f992b7b6dd306c26a3784aee85919f193f1cb67d`, `372055c3205aa0b6810dbdf53bec822aebe0f45f`.
- [ ] Exact next task: audit the remaining PQ presentation consumer contracts in `docs/data/pq-cross-domain-index.json`, prioritizing `scripts/validate_pq_reference_pages.py`, `scripts/validate_pq_explorer_reward_navigation.py`, and `scripts/validate_pq_explorer_character_navigation.py` against their live consumer fields; repair only deterministic current-state drift and preserve historical/provenance conflicts.


### 2026-09-22 cycle update — PQ presentation consumer contract audit
- [x] Audited `scripts/validate_pq_reference_pages.py`, `scripts/validate_pq_explorer_reward_navigation.py`, and `scripts/validate_pq_explorer_character_navigation.py` against their live consumer pages and canonical data.
- [x] Reference-page consumer is aligned: **186** canonical PQ records, **860** relationship edges, farming set **PQ15/PQ22/PQ44/PQ45/PQ68/PQ83/PQ88**, and the page links to the live `Parallel-Quests-All.html` explorer. No stale PQ13 farming shorthand remains.
- [x] Reward explorer consumer is aligned: **244 skills / 151 Super Souls / 125 equipment / 86 DLC edges**, with zero unresolved canonical reward/DLC targets. Its structured PQ reward fields were independently rechecked at **244/244, 151/151, 125/125** after the previous consumer repair.
- [x] Character explorer consumer is aligned: **247 character edges**, **75 unique canonical character targets**, **143 source PQs**, zero missing character targets, and zero invalid PQ IDs; canonical PQ record layer remains 186 records.
- [x] Refreshed `docs/data/pq-reference-page-audit.json`, `docs/data/pq-explorer-reward-navigation-audit.json`, and `docs/data/pq-explorer-character-navigation-audit.json` with current validator references/date and live counts.
- [x] Strengthened `scripts/validate_pq_reference_pages.py` with an explicit live-explorer-link contract.
- [x] No relationship identities or target aliases were added/removed. Existing evidence boundaries and historical conflicts remain preserved.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `433d37d44c34cbe4128cbb93f298fd33cdb1070e`, `346b275ac4d5fc792ab127daea3ec6b68cf095e8`, `9ebd2c4aa34ad981e0259ba21dd5be6201d76647`, `08f0c633c7f65203c6d1178a9432480f52647097`.
- [ ] Exact next task: continue down the cross-domain consumer chain by auditing `scripts/validate_skills_pq_reverse_navigation.py` / `docs/data/skill-pq-acquisition-presentation-audit.json` and `scripts/validate_record_reverse_pq_navigation.py` / `docs/data/record-reverse-pq-navigation-audit.json` against canonical PQ relationships and live target records; repair deterministic reverse-link drift only.


### 2026-09-22 cycle update — reverse PQ navigation consumer audit
- [x] Audited `scripts/validate_skills_pq_reverse_navigation.py` and the skill reverse-navigation consumer. Live parity is clean: **452 skill records / 244 canonical PQ→skill edges / 0 reverse-set mismatches**; `Skills-All.html` exposes canonical PQ links and PQ-aware search navigation.
- [x] Audited `scripts/validate_record_reverse_pq_navigation.py` across Super Souls and equipment/accessories. Canonical structured parity is clean for **151 Super Soul edges** and **125 equipment edges**, with **0 unresolved canonical targets** and **0 canonical structured-field mismatches**.
- [x] Identified four equipment records whose `parallel_quest_ids` are preserved acquisition metadata but whose names are intentionally absent from the canonical `pq_rewards_equipment` graph: `Great Saiyaman Bandana 1` (PQ51), `Great Saiyaman Bandana 2` (PQ53), `Jaco's State-of-the-Art Radio` (PQ72), and `Tagoma's Scouter` (PQ73). These are not canonical reverse-link failures; no canonical edges were inferred.
- [x] Strengthened `scripts/validate_record_reverse_pq_navigation.py` to report such noncanonical structured PQ metadata separately from canonical reverse-link mismatches, preserving the repository's evidence boundary.
- [x] Updated `docs/data/record-reverse-pq-navigation-audit.json` to document the four metadata-only cases and the distinction between acquisition metadata and canonical relationship identity.
- [x] Existing equipment source-route conflicts remain preserved, including Goku Wig (Super Saiyan) and SSGSS Goku Wig; no provenance was discarded.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `a55896053fa0badb20dacb0ce677132a4861efef`, `83619b8beaed5ea515490205ec3ea5b463590129`.
- [ ] Exact next task: continue the cross-domain chain with `scripts/validate_pq_endpoint_navigation.py`, `scripts/validate_pq_presentation_indexes.py`, and their endpoint/presentation audits, checking canonical target resolution and PQ↔entity identity without promoting acquisition metadata into new relationships.


### 2026-09-22 cycle update — published Character/DLC navigation repair
- [x] Audited the published Character and DLC index pages against their referenced repository-local navigation artifacts.
- [x] Found one deterministic stale link in `docs/Characters.md`: `Characters-All.md` did not exist; the published explorer is `Characters-All.html`.
- [x] Repaired the link without changing character identity data, PQ relationships, DLC identities, or provenance.
- [x] Added `scripts/validate_published_character_dlc_navigation.py` to enforce the checked local navigation contracts.
- [x] Added `docs/data/characters/published-character-dlc-navigation-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation scope: Character explorer, Character Core Profiles, DLC character identity audit/bridge, canonical DLC identity, DLC PQ reverse index/audit, Future Saga content map, and DLC presentation audit all resolve to existing local artifacts.
- [x] No canonical relationship identities were added, removed, renamed, or inferred.
- [ ] CI: no successful GitHub Actions status exposed for this direct-commit chain; CI success not claimed.
- [ ] Exact next task: continue the published-page/structured-index audit beyond the Character/DLC pair, prioritizing other cross-domain consumer pages and local navigation surfaces that consume canonical PQ, skill, Super Soul, equipment, character, or DLC endpoints; repair only deterministic stale/broken links and record unresolved external-corpus dependencies explicitly.


### 2026-09-22 cycle update — Partner Customization character-navigation contract
- [x] Live census: **20 Customization Unlock Key records**, **20 reconciliation records**, **29 explicit character identity-bridge records**, and **149 canonical character names**.
- [x] Audited the key-record layer, reconciliation layer, canonical character bridge, and `docs/Partner-Customization.md` together.
- [x] Deterministic identity parity is clean: all 20 key character IDs resolve through the explicit bridge; all bridge targets are canonical character names; key/reconciliation identity fields match; all 20 Partner Customization page search links resolve by canonical partner name.
- [x] Added `scripts/validate_partner_customization_character_navigation.py` as a read-only validator for this contract.
- [x] Added `docs/data/characters/partner-customization-character-navigation-audit.json` and registered it in the cross-domain navigation/validation index.
- [x] Updated `docs/data/characters/character-presentation-consumer-audit.json` and `docs/Partner-Customization.md` so the new navigation contract is discoverable.
- [x] Evidence boundary preserved: this pass validates identity/navigation only; it does not promote partially verified DLC ownership, raid rotation, TP Medal costs, or historical update claims into canonical relationships.
- [ ] CI: no successful GitHub Actions status exposed; local clone/execution was unavailable because the runtime could not resolve github.com. API-level file/parity inspection was used instead; CI/build success is not claimed.
- [ ] Exact next batch: continue the character-facing consumer chain after Partner Customization, prioritizing any remaining character preset/explorer or DLC-character presentation consumers registered in `docs/data/pq-cross-domain-index.json`; repair deterministic stale links/identity drift only, then move into the next unresolved cross-domain consumer surface.


### 2026-09-22 cycle update — PQ endpoint/presentation live recheck
- [x] Live-rechecked the next queued cross-domain batch: `scripts/validate_pq_endpoint_navigation.py`, `scripts/validate_pq_presentation_indexes.py`, `docs/data/pq-endpoint-navigation-validation.json`, and `docs/data/pq-presentation-index-identity-audit.json` against the current canonical layers.
- [x] Current canonical PQ census: **186 PQ records / 860 canonical relationship edges**.
- [x] Endpoint parity: **244 skill edges / 239 unique skill targets; 151 Super Soul edges / 148 unique targets; 125 equipment edges / 123 unique targets; 247 character edges / 75 unique targets; 86 DLC edges / 20 unique targets** — all endpoint target sets resolve exactly, with **0 missing targets**.
- [x] Presentation reverse-index parity: **239 skills / 148 Super Souls / 123 equipment / 28 accessories** reverse records; **0 missing IDs, 0 canonical-name mismatches, 0 unresolved routes** in the checked report contracts.
- [x] DLC projection recheck: **3 projection records / 0 unresolved canonical DLC IDs**. Existing six DLC granularity mappings and two equipment naming conflicts remain explicit and do not alter canonical edge counts.
- [x] Refreshed `docs/data/pq-endpoint-navigation-validation.json` and `docs/data/pq-presentation-index-identity-audit.json` with the current live census and status.
- [x] No canonical relationships, aliases, or evidence classifications were changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: audit the next unvalidated presentation consumer(s) registered around the PQ cross-domain index, especially standalone reverse-index reconciliation and unified reverse-index consumers; compare their current live counts/IDs to canonical PQ relationships and repair deterministic drift only.


### 2026-09-22 cycle update — unified PQ reverse-index exact parity
- [x] Audited `docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json` directly against `docs/data/pq-reward-relationships.json` using exact **(target, PQ)** pairs, rather than endpoint counts alone.
- [x] Exact parity is clean across all canonical domains: **244 skill, 151 Super Soul, 125 equipment, 247 character, 86 DLC, and 7 farming pairs = 860 total**, with **0 missing / 0 extra** pairs in every domain.
- [x] Equipment parity was checked across the unified index's two presentation domains: **83 clothing + 40 accessories = 125 equipment pairs**, with 0 missing and 0 extra against the canonical equipment relationship set.
- [x] Confirmed **0 invalid PQ numbers** and **0 duplicate relationship keys** in the compared canonical/projection contract.
- [x] Refreshed `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json` with the exact live reconciliation and preserved its historical correction records.
- [x] No canonical relationships or source/provenance classifications were changed; this cycle only strengthened the machine-checkable audit of an already-clean projection.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: inspect the remaining registered PQ consumer artifacts after the unified reverse index, prioritizing `docs/data/pq-page-consumer-audit.json` / `scripts/validate_pq_page_consumers.py` and other published PQ presentation consumers for deterministic stale links, counts, or one-way navigation.


### 2026-09-22 cycle update — general PQ reference consumer hardening
- [x] Audited `docs/Parallel-Quests.md` and `docs/Parallel-Quest-Audit.md` against the live canonical PQ record and relationship layers rather than relying on historical audit text.
- [x] Confirmed the public reference surface is deterministic and aligned: **186 PQ records / 860 relationship edges**, with exact domain counts **244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**.
- [x] Confirmed the canonical farming set remains exactly **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**; no stale PQ13 farming claim remains.
- [x] Strengthened `scripts/validate_pq_reference_pages.py` with exact per-domain relationship-count checks instead of validating only the aggregate 860-edge total.
- [x] Refreshed `docs/data/pq-reference-page-audit.json` with the live domain-count validation contract.
- [x] No unsupported reward, drop-condition, route-efficiency, or numbering claims were promoted; the existing PQ36 historical conflict and numbering-gap policy remain preserved.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: continue from the remaining registered PQ-facing consumers after the general reference pages, prioritizing `docs/data/record-reverse-pq-navigation-audit.json` / `scripts/validate_record_reverse_pq_navigation.py` and checking exact record→PQ and PQ→record parity for deterministic one-way navigation gaps.


### 2026-09-22 cycle update — reverse record→PQ pair parity hardening
- [x] Audited `docs/data/record-reverse-pq-navigation-audit.json` and `scripts/validate_record_reverse_pq_navigation.py` against the live Super Soul and equipment/accessory record layers plus canonical PQ relationships.
- [x] Exact canonical/structured pair parity is clean: **151/151 Super Soul pairs** and **125/125 equipment pairs** for canonical targets, with **0 missing / 0 extra** pairs and **0 invalid structured PQ IDs**.
- [x] Confirmed the published `docs/Super-Souls-All.html` and `docs/Equipment-All.html` consumers expose canonical PQ navigation and `?q=` query navigation.
- [x] Strengthened `scripts/validate_record_reverse_pq_navigation.py` to check exact `(record, PQ)` parity in both directions and validate structured PQ IDs across numeric and textual representations.
- [x] Refreshed `docs/data/record-reverse-pq-navigation-audit.json` to record the new parity contract.
- [x] Preserved the two documented equipment acquisition conflicts and four noncanonical accessory acquisition-metadata PQ fields as explicit evidence boundaries; none were promoted into canonical reward edges.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: inspect `docs/data/pq-reward-normalization/pq-standalone-reverse-index-audit.json` and its reconciliation/validator pair for exact standalone reverse-index parity, then compare any remaining registered PQ reverse consumers before moving to the next cross-domain surface.


### 2026-09-22 cycle update — Super Soul acquisition-index exact pair reconciliation
- [x] Audited `docs/data/super-souls/pq-acquisition-index-041-186.json` against the canonical `pq_rewards_super_soul` relationship projection at exact `(PQ,target)` pair level.
- [x] Live census: **133 canonical Super Soul pairs within PQ41–186**, **122 acquisition-index pairs**, **120 exact overlaps**.
- [x] Classified the **13 differences** without rewriting canonical relationships: **11 exact canonical pairs are absent from the partial acquisition index** and **2 are capitalization-only name variants** (PQ164/PQ173).
- [x] Added `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json` with the bounded reconciliation queue and evidence boundary.
- [x] Added `scripts/validate_super_soul_acquisition_index.py` to machine-check exact pair overlap and distinguish case-only drift from true coverage gaps.
- [x] Registered the audit and validator in `docs/data/pq-cross-domain-index.json`.
- [x] No canonical Super Soul relationship, acquisition claim, or source-layer entry was promoted or deleted; the 11 missing pairs remain research targets pending independent evidence.
- [x] Commits: `3a46f441b924a269cf7f3bbcfc7e837aafc8706f`, `4490ef80cadbd8dd4a406daf323e4fa9c70607fc`, `6c34fa9c07500e4a78b1454fca64625b18a6ce09`.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [ ] Exact next batch: independently reconcile the **11 missing Super Soul acquisition pairs** in bounded evidence groups, beginning with **PQ151–153 and PQ158/PQ174/PQ178/PQ179**, while preserving the partial-index semantics and refusing to infer missing acquisition routes from canonical relationships alone.


### 2026-09-22 cycle update — PQ explorer character/DLC navigation hardening
- [x] Continued from the resolved standalone reverse-index parity gate and audited the actual `docs/Parallel-Quests-All.html` consumer plus `scripts/validate_pq_page_consumers.py` against the live canonical PQ relationship layer.
- [x] Live baseline remains **186 PQ records / 860 canonical relationship edges**: 244 skills, 151 Super Souls, 125 equipment, 247 character, 86 DLC, 7 farming.
- [x] Confirmed the explorer already loads character and DLC navigation directly from `docs/data/pq-reward-relationships.json`, rather than inferring them from PQ prose/enemy fields.
- [x] Deterministic DLC projection check: **86 canonical DLC edges across 86 PQs; 0 PQs have multiple DLC requirement edges**, so the page's scalar `dlcByPq` projection is lossless for the current canonical layer.
- [x] Hardened `scripts/validate_pq_page_consumers.py` to verify character/DLC projection hooks, canonical relationship-PQ coverage, and navigation presence in addition to the existing structured reward parity checks.
- [x] Refreshed `docs/data/pq-page-consumer-audit.json` with the character/DLC navigation contract and current verification date.
- [x] No canonical relationships, identities, aliases, or page data were invented or rewritten; this was a consumer-validator hardening pass.
- [x] Commits: `8ee693c017813137dbbf034ab122e521aa589c56`, `12b30cec558dc04c2d0339f5f1e83f44519ae068`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: audit the remaining registered published PQ/navigation consumers and local search/DLC/equipment landing surfaces for deterministic one-way navigation gaps; prioritize any consumer that duplicates canonical relationship targets instead of deriving them directly.


### 2026-09-22 cycle update — DLC presentation consumer exact reverse-parity hardening
- [x] Audited the live DLC presentation validator and canonical DLC reverse-navigation projection after the PQ explorer consumer pass.
- [x] Confirmed the canonical DLC identity layer contains **20 unique DLC identities** and the PQ relationship layer contains **86 `pq_requires_dlc` edges**.
- [x] Confirmed `docs/data/dlc/pq-reverse-index.json` contains **86 reverse `(PQ,DLC)` pairs**, with **0 missing / 0 extra** against the canonical forward relationship set and all 20 canonical DLC identities represented.
- [x] Hardened `scripts/validate_dlc_presentation_consumers.py` to check exact forward/reverse PQ-DLC pair parity, canonical 86-edge count, reverse-target coverage, and the existing content/Future Saga identity contracts.
- [x] Corrected the validator to use the live reverse-index schema (`records[].dlc_id` + `pq_ids[]`) rather than an assumed `reverse_index` map; no data changes were required.
- [x] Refreshed `docs/data/dlc/dlc-presentation-consumer-audit.json` with exact reverse-pair census and validator registration.
- [x] Preserved the evidence boundary: DLC content-domain projection records and Future Saga grouping do not create canonical DLC identities or PQ relationships.
- [x] Commits: `56e9cf0166c47e2c5fec5e6fbd9f53751db50c5d`, `e5a3b559081f898d760c46c54057b38e4e5233a2`, `be3fc73c13a296702fa6543833dd0f92a35405b0`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: inspect the remaining registered character/DLC and cross-domain presentation validators for schema assumptions that are not exercised by their current audits, then harden the next deterministic consumer without altering canonical relationship data.


### 2026-09-22 cycle update — Partner Customization character-navigation validator hardening
- [x] Audited the remaining published Character/DLC and character-facing navigation validators for hidden schema/coverage assumptions.
- [x] Found that `scripts/validate_partner_customization_character_navigation.py` validated the expected key-number set but did not explicitly reject duplicate key/reconciliation numbers, and its page-link check did not independently verify every extracted Search target belonged to the expected partner set.
- [x] Hardened the validator with explicit uniqueness checks for key and reconciliation numbers and exact Search-target membership checks.
- [x] Refreshed `docs/data/characters/partner-customization-character-navigation-audit.json` with the strengthened checks; current result remains **clean**, with 20 key records, 20 reconciliation records, 20 page Search links, no duplicate key numbers, and no unmapped Search targets.
- [x] No character identity, PQ relationship, DLC relationship, or Partner Customization factual record was changed.
- [x] Commits: `e3cd6ae5f71ef23ee7a28eba2b4981b2acdf83ba`, `f70d7b458976387e4b087cabdb21ed685c1d314d`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: audit the character-facing PQ reverse-navigation consumer itself (`Characters-All.html` / character presentation audit) against the canonical 247 PQ→character edges, checking for stale scalar/list assumptions, orphan targets, and exact forward/reverse parity before expanding content coverage.


### 2026-09-22 cycle update — character explorer PQ reverse-navigation exact parity
- [x] Audited `scripts/validate_character_explorer.py` and `docs/Characters-All.html` against canonical `docs/data/pq-reward-relationships.json` and `docs/data/characters/pq-reverse-index.json`.
- [x] Hardened the character explorer validator to compare canonical `pq_features_character` forward pairs against the reverse projection rather than checking only endpoint existence/counts.
- [x] The reverse projection uses list-valued PQ collections (`index[name]||[]`) and the explorer renders each PQ reference independently; no scalar-PQ assumption was found.
- [x] Exact live parity: **247 canonical character edges / 247 reverse pairs / 0 missing / 0 extra / 0 duplicate pairs**, across **75 canonical character targets** and **5 documented aliases**.
- [x] Updated `docs/data/characters/character-presentation-consumer-audit.json` with the exact forward/reverse parity result.
- [x] No canonical relationship identities or character identities were changed.
- [x] Commits: `381bf6df058cb86e2c7b3e34cdd4ffdc21b8b8ed`, `b2e2139e32bea61162ef349dbff86b058068e6eb`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: continue the same deterministic audit across the remaining registered cross-domain presentation consumers, prioritizing any consumer that still checks only endpoint existence/counts rather than exact canonical forward/reverse pair parity.


### 2026-09-22 cycle update — skill PQ reverse-navigation exact parity hardening
- [x] Audited `scripts/validate_skills_pq_reverse_navigation.py` and `docs/Skills-All.html` against the canonical PQ relationship graph and 452-record skill layer.
- [x] Hardened the validator beyond per-record set comparison to explicitly validate exact forward/reverse `(skill,PQ)` pair parity, unresolved canonical targets, and duplicate reverse pairs.
- [x] Live canonical result remains clean: **244 canonical PQ→skill edges**, **0 missing**, **0 extra**, **0 unresolved canonical targets**, and **0 duplicate reverse pairs**.
- [x] Updated `docs/data/skill-pq-acquisition-presentation-audit.json` with the exact-parity result.
- [x] No canonical skill identities or PQ relationship edges were changed.
- [x] Commits: `b5ea179cd17c788eede7a2b5d68085c4caf9ea52`, `77c2dc4e71e38bc5ec88971de01b98f9e726d5ec`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: audit the remaining registered PQ explorer/reference presentation validators for the same hidden scalar/list, endpoint-only, or stale-count assumptions, prioritizing `validate_pq_explorer_reward_navigation.py` and `validate_pq_reference_pages.py`.

### 2026-09-22 — PQ explorer exact reward-pair parity hardening
- [x] Hardened `scripts/validate_pq_explorer_reward_navigation.py` from endpoint/count validation to exact canonical `(PQ,target)` pair parity for Skills, Super Souls, and Equipment.
- [x] Added duplicate structured-pair checks and preserved canonical DLC identity resolution plus HTML navigation checks.
- [x] Refreshed `docs/data/pq-explorer-reward-navigation-audit.json` to schema 1.1.0: **244/244 skills, 151/151 Super Souls, 125/125 equipment; 0 missing, 0 extra, 0 duplicate pairs; 86 DLC edges / 20 targets / 0 unresolved**.
- [x] No canonical relationship or identity data changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `00dfd24c3d9c5f8f4fbc8261a261c152211cf69b`, `8deae24b4a557ca272e4901e2c8d4c83d35bd3ad`.
- [ ] Exact next batch: audit `scripts/validate_pq_reference_pages.py` and its published PQ reference consumers for exact pair/count/set parity and hidden scalar/list assumptions, then harden deterministic gaps only.
\n### 2026-09-22 — general PQ reference identity-contract hardening
- [x] Hardened `scripts/validate_pq_reference_pages.py` with exact canonical PQ number-set, unique-ID, known-relationship-type, and unique `(relationship,PQ,target)` checks.
- [x] Refreshed `docs/data/pq-reference-page-audit.json` to schema 1.1.0; live status remains clean with **186 PQ records / 860 canonical relationship edges**.
- [x] No canonical relationship or identity data changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `8a256fb4e2998c12a0f29b42a637acbdc93ff5c4`, `8bf3f109e1ec3249f43f6daf9978d58d2198a4db`.
- [ ] Exact next batch: inspect remaining PQ-facing search/landing consumers and the cross-domain index registry for duplicated canonical counts or one-way links, prioritizing exact pair-parity checks without broad schema migration.


### 2026-09-22 cycle update — PQ presentation-index exact forward-pair hardening
- [x] Audited `scripts/validate_pq_presentation_indexes.py` and its four PQ reverse/presentation reports against the canonical PQ relationship graph.
- [x] Hardened validation from endpoint/name existence to exact canonical `(target,PQ)` forward-pair parity for Skills, Super Souls, Equipment, and the canonical accessory subset, plus duplicate-forward-pair rejection.
- [x] Live exact parity: **244/244 Skills, 151/151 Super Souls, 125/125 Equipment, 28/28 Accessories; 0 missing, 0 extra, 0 duplicate pairs**.
- [x] Refreshed `docs/data/pq-presentation-index-identity-audit.json` to schema **1.1.0** with the exact-pair contract.
- [x] No canonical relationship or identity records were changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `95ed7620422b5559973a632027b8faade65e9964`, `e14b92f6a0550c86cb5e22730281c5bbbf6e0711`.
- [ ] Exact next batch: audit `scripts/validate_record_reverse_pq_navigation.py` for the same exact forward-pair and duplicate assumptions, then update its audit only if the live consumer contract is deterministically clean.


### 2026-09-22 cycle update — record reverse-PQ exact-pair duplicate hardening
- [x] Audited `scripts/validate_record_reverse_pq_navigation.py` against the live Super Soul and Equipment record layers and canonical PQ relationship graph.
- [x] Added explicit duplicate structured `(record,PQ)` pair rejection while preserving the existing exact canonical-pair parity boundary and noncanonical equipment metadata handling.
- [x] Live deterministic check: **151/151 Super Soul canonical pairs and 125/125 Equipment canonical pairs**, **0 missing, 0 canonical extras, 0 duplicate structured pairs**.
- [x] The Equipment layer retains **4 noncanonical acquisition-metadata PQ pairs**; these remain explicitly outside canonical `pq_rewards_equipment` navigation and were not promoted.
- [x] Refreshed `docs/data/record-reverse-pq-navigation-audit.json` to schema **1.3.0**.
- [x] No canonical relationship, identity, or acquisition claim was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `76a58807f0dad1c9fc2c7b56a1d53847c0f44486`, `b9f6633f44927556358aa823cae00624edc15c49`.
- [ ] Exact next batch: continue auditing the registered cross-domain PQ consumers for duplicated canonical scalar counts or one-way navigation gaps, next targeting the unified PQ reverse-index validator and its generated projection.


### 2026-09-22 cycle update — unified PQ reverse-index exact canonical parity
- [x] Re-read the continuation protocol and audited `scripts/validate_pq_reverse_indexes.py`, the unified reverse projection, and the standalone reconciliation audits.
- [x] Hardened the unified validator with explicit duplicate-pair detection for standalone normalized maps/reverse projections.
- [x] Added an exact canonical reward-domain contract for the unified projection: **520 canonical reward pairs = 244 Skills + 151 Super Souls + 125 Equipment**, with **520/520 unified pairs, 0 missing, 0 extra, 0 duplicate pairs**.
- [x] Preserved the broader canonical comparison boundary: Characters, DLC, and farming remain covered by the existing 860-edge unified audit; standalone source-map drift remains informational and does not override canonical relationships.
- [x] Refreshed `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json` to schema **1.1.0**.
- [x] No canonical relationship or source-layer reward data was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `46f7dcdc4a87e5997d02b817d6f4d20046f285df`, `5cd22060600e245262eb87ee993c1d34bc7ee009`, `c9cf3614b86fc306ab24628d2e42e85deb0a2b5b`.
- [ ] Exact next batch: inspect the next registered cross-domain presentation consumer for stale scalar/list assumptions or one-way canonical navigation, without broad schema migration.


### 2026-09-22 cycle update — registered unified PQ reverse-index validator hardening
- [x] Audited the separately registered `scripts/validate_pq_unified_reverse_index.py` consumer, which is distinct from the broader reverse-index validator.
- [x] Found that projection validation converted each PQ collection directly to a set, so duplicate canonical pairs and accidental scalar/non-list fields could be silently hidden.
- [x] Hardened the validator to require list-valued PQ collections and explicitly count duplicate `(target,PQ)` projection pairs for Skills, Super Souls, Characters, DLC, Farming, and the combined Clothing/Accessories Equipment projection.
- [x] Live deterministic parity remains clean across the full canonical graph: **860/860 pairs**, comprising **244 Skills / 151 Super Souls / 125 Equipment / 247 Characters / 86 DLC / 7 Farming**, with **0 missing / 0 extra / 0 duplicate / 0 invalid-list fields**.
- [x] Refreshed `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json` to schema **1.2.0** and recorded validator commit `df07a0cb046f38a6e5ee5973b82c203ae76a79c9`.
- [x] No canonical relationship or generated projection identity was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `df07a0cb046f38a6e5ee5973b82c203ae76a79c9`, `22429714ede4a0832b8539790ff918567299d5a5`.
- [ ] Exact next batch: inspect the next registered cross-domain presentation consumer for stale scalar/list assumptions or one-way canonical navigation.


### 2026-09-22 cycle update — PQ endpoint navigation exact identity/pair hardening
- [x] Hardened `scripts/validate_pq_endpoint_navigation.py` to reject duplicate canonical `(PQ,target)` pairs and relationship PQ IDs that do not resolve to the canonical 186-record PQ layer.
- [x] Live endpoint census: **953 canonical endpoint edges = 244 Skills / 151 Super Souls / 125 Equipment / 247 Characters / 86 DLC**, with **0 duplicate pairs / 0 missing targets / 0 invalid PQ IDs**.
- [x] Canonical PQ identity census: **186 records / 186 unique IDs / 186 unique numbers / exact 1–186 range**.
- [x] Refreshed `docs/data/pq-endpoint-navigation-audit.json` to schema **1.1.0**.
- [x] Preserved the explicit equipment/DLC alias and granularity bridge; no canonical identities or relationships were changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `f93e27f053bafab4ce33bd642ed657c85ee5fac6`, `0f6dbd85116e8678423b68f7e91b7be25b398bf3`.
- [x] **TODO completion:** canonical PQ endpoint navigation exact identity/pair hardening.
- [ ] Exact next batch: inspect the next registered cross-domain consumer for endpoint/count-only or one-way navigation validation, then harden only deterministic gaps.


### 2026-09-22 cycle update — Super Soul partial acquisition-index structural hardening
- [x] Hardened `scripts/validate_super_soul_acquisition_index.py` against duplicate PQ records, malformed list/scalar fields, and duplicate structured `(PQ,Super Soul)` pairs.
- [x] Live structural validation: **80/80 unique PQ records, 122/122 unique structured pairs, 0 malformed, 0 duplicates**.
- [x] Preserved the canonical-vs-partial projection reconciliation boundary: **133 canonical pairs / 122 indexed / 120 exact overlap / 13 differences** remain explicit research findings.
- [x] Refreshed `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json` to schema **1.1.0**.
- [x] No canonical relationship or research claim was promoted.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] **TODO completion:** Super Soul acquisition-index structural hardening.
- [ ] Exact next batch: continue through the registered cross-domain consumers for deterministic structural or navigation gaps.


### 2026-09-22 cycle update — PQ reference/explorer dependency contract hardening
- [x] Hardened `scripts/validate_pq_reference_pages.py` with canonical relationship-PQ resolution, duplicate PQ identity checks, and published explorer dependency/collection-shape checks.
- [x] Live result: **186 PQ records / 860 canonical relationship edges / 0 invalid relationship PQ IDs / 0 duplicate PQ numbers / 0 duplicate PQ IDs**.
- [x] Published explorer contract clean: canonical PQ layer + canonical relationship layer loaded explicitly, arrays guarded, canonical Search surface retained.
- [x] Refreshed `docs/data/pq-reference-page-audit.json` to schema **1.2.0**.
- [x] No canonical relationship or identity data changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] **TODO completion:** PQ reference/explorer dependency contract hardening.
- [ ] Exact next batch: inspect the next PQ-facing search/landing consumer or cross-domain registry for one-way navigation and stale hard-coded counts.


### 2026-09-22 cycle update — PQ explorer Character navigation exact-pair hardening
- [x] Audited the registered `scripts/validate_pq_explorer_character_navigation.py` consumer and its published explorer.
- [x] Hardened validation to load the canonical 186-record PQ layer instead of reconstructing the PQ range, reject malformed character relationship records, and reject duplicate structured `(PQ,Character)` pairs.
- [x] Live result remains clean: **247 canonical Character edges / 75 unique character targets / 143 source PQs / 0 missing targets / 0 invalid PQ IDs / 0 duplicate pairs / 0 malformed records**.
- [x] Refreshed `docs/data/pq-explorer-character-navigation-audit.json` to schema **1.1.0**.
- [x] No canonical Character relationship or roster identity was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `1e80247f62b77a517ca1f7f82dd354f9cf37bab7`, `b99f389f8ac03eb4fe3caf8a2233f632cf04037a`.
- [ ] Exact next batch: inspect the next registered PQ-facing search/landing consumer after the Character explorer consumer for duplicate structured pairs, one-way navigation, or stale hard-coded canonical counts.


### 2026-09-22 cycle update — PQ explorer canonical DLC identity reconciliation
- [x] Reconciled the published PQ explorer's displayed DLC labels with the canonical `pq_requires_dlc` relationship target instead of the legacy per-record `dlc_requirement` field.
- [x] Hardened `scripts/validate_pq_explorer_reward_navigation.py` to validate canonical DLC identity uniqueness, IDs, exact relationship-pair uniqueness, and canonical-label consumption.
- [x] Live canonical values remain: **86 PQ→DLC edges / 20 unique canonical DLC targets / 20 identity records / 0 unresolved targets / 0 duplicate identity names / 0 duplicate IDs / 0 duplicate PQ→DLC pairs**.
- [x] Refreshed `docs/data/pq-explorer-reward-navigation-audit.json` to schema **1.2.0**.
- [x] No PQ→DLC relationship or DLC identity was added, removed, renamed, or inferred.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `341ae3a77fa8c438061032f052318c0d23f12edb`, `cfd663d80d12c734d2e032f76a4836f9f9e831f3`, `fbc54443a0e52801b1e408ce359a4bd0140124ce`, `e19050eb728114da712d1bcb900abd07aa6ba675`.
- [ ] Exact next batch: inspect the remaining registered local Search/DLC/equipment landing consumers for one-way navigation and stale duplicated canonical counts, continuing from the cross-domain registry rather than introducing new inferred relationships.


### 2026-09-22 cycle update — Skill reverse-PQ validator hardening
- [x] Continued the registered reverse-navigation chain into `scripts/validate_skills_pq_reverse_navigation.py`.
- [x] Fixed a latent validator initialization defect where `canonical_pairs` was referenced before initialization.
- [x] Added deterministic duplicate canonical `(Skill,PQ)` pair detection to the reverse-navigation contract.
- [x] Refreshed `docs/data/skill-pq-acquisition-presentation-audit.json` to audit version **1.1** with the hardened validator commit.
- [x] Existing canonical baseline remains **452 skill records / 244 PQ→skill edges / 0 reverse mismatches / 0 missing pairs / 0 extra pairs / 0 unresolved targets / 0 duplicate canonical pairs**.
- [x] No canonical skill identity or PQ→skill relationship was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `810b923f691ba80e35821910e028f85827506700`, `3a717bf13d8434c86571d37df282bfe026faff6d`.
- [ ] Exact next batch: continue the reverse-navigation chain through `scripts/validate_record_reverse_pq_navigation.py` and its Super Soul/Equipment consumers, checking deterministic pair uniqueness and stale/one-way landing links without promoting source-conflict metadata into canonical relationships.


### 2026-09-22 cycle update — PQ explorer exact reward/projection contract hardening
- [x] Hardened `scripts/validate_pq_page_consumers.py` so Skills, Super Souls, and Equipment require exact canonical `(PQ,target)` parity, list-valued structured fields, zero duplicate structured pairs, zero duplicate canonical pairs, and valid canonical PQ IDs.
- [x] Hardened Character/DLC navigation checks to reject duplicate canonical pairs and explicitly verify the scalar DLC projection is unambiguous.
- [x] Live result: **186 unique PQ IDs / 186 unique PQ numbers; 244 Skills / 151 Super Souls / 125 Equipment / 247 Characters / 86 DLC pairs; 0 missing / 0 extra / 0 duplicate / 0 malformed / 0 invalid PQ IDs**.
- [x] Refreshed `docs/data/pq-page-consumer-audit.json` to schema **1.1.0**.
- [x] No canonical relationship, identity, alias, or content data was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next task: continue through the registered cross-domain consumer registry, prioritizing the next deterministic landing/search consumer with endpoint/count-only or one-way navigation assumptions.


### 2026-09-22 cycle update — Super Soul/equipment reverse-PQ hidden-shape hardening
- [x] Continued the exact next batch into `scripts/validate_record_reverse_pq_navigation.py`, covering the Super Soul and equipment/accessory reverse consumers.
- [x] Hardened the validator against hidden scalar/list corruption: structured PQ fields must be lists; malformed scalar fields are now explicit failures instead of being iterated character-by-character.
- [x] Hardened record identity handling: duplicate record names and duplicate canonical `(record,PQ)` relationship pairs are now explicit failures instead of being silently collapsed by dictionaries/sets.
- [x] Live canonical result remains clean: **234 Super Soul records / 151 canonical edges / 148 unique canonical targets; 174 equipment records / 125 canonical edges / 123 unique canonical targets; 151/151 and 125/125 exact reverse pairs; 0 missing / 0 extra / 0 invalid PQ IDs / 0 duplicate structured pairs / 0 duplicate canonical pairs / 0 malformed structured fields / 0 duplicate record names**.
- [x] Existing evidence boundaries remain unchanged: four noncanonical equipment PQ metadata pairs and the two documented equipment source-route conflicts remain preserved and are not promoted into canonical relationships.
- [x] Refreshed `docs/data/record-reverse-pq-navigation-audit.json` to schema **1.4.0**.
- [x] Validator commit: `a5a706db4cff56967d6af2813c1623738c3f0324`; audit refresh: `88e68619c411329e1c39d42ec797bfaffd06b979`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: inspect the next registered cross-domain presentation/search consumer after reverse-PQ record navigation, prioritizing remaining deterministic one-way links, stale duplicated counts, or hidden scalar/list assumptions.


### 2026-09-22 cycle update — DLC presentation/reverse navigation parity hardening
- [x] Continued the registered cross-domain consumer chain into `scripts/validate_dlc_presentation_consumers.py`, covering the canonical DLC identity layer, DLC content projection, Future Saga map, DLC overview, and PQ↔DLC reverse navigation.
- [x] Found and repaired a deterministic validator defect: canonical `pq_requires_dlc` relationship targets are human-readable DLC names while the reverse index stores canonical `dlc_id` values. The validator now resolves relationship names through `canonical-dlc-identity.json` before exact forward/reverse comparison instead of comparing incompatible representations.
- [x] Added hidden-shape/duplicate guards: content projection ID collections must be lists; Future Saga `dlc_id` fields must be strings; reverse `pq_ids` collections must be lists; forward/reverse pairs and reverse DLC IDs must be unique.
- [x] Live corrected result: **20/20 canonical DLC identities; 3 content projection records / 6 references; Future Saga Chapters 1–4 / 4 DLC references; 86 forward PQ→DLC edges / 86 unique reverse pairs; 0 unresolved target names / 0 missing / 0 extra / 0 duplicate forward or reverse pairs / 0 malformed fields**.
- [x] Refreshed `docs/data/dlc/dlc-presentation-consumer-audit.json` to schema **1.1.0** with the corrected name→ID parity contract.
- [x] No canonical DLC identity or PQ→DLC relationship was changed; only validator/audit logic was corrected and hardened.
- [x] Validator commit: `23350e2db4d4fe85f204599a9ab6632c60b05375`; audit refresh: `8c68ad509c61bb352a0ccff37eed0a5c399a592e`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: continue to the next registered local Search/DLC/equipment or published navigation consumer, prioritizing another deterministic representation mismatch or one-way canonical-link gap before broad content research.


### 2026-09-22 cycle update — Character presentation identity-shape hardening
- [x] Continued the registered cross-domain consumer chain into `scripts/validate_character_presentation_consumers.py`, covering canonical character identities, the character-ID bridge, preset records, Partner Customization records/reconciliation, and `docs/Characters-All.html` search navigation.
- [x] Hardened bridge identity validation so duplicate `character_id` values and malformed non-string IDs cannot be silently collapsed by the bridge dictionary.
- [x] Hardened optional bridge `source_name` uniqueness when present; absent optional source names are not treated as duplicates.
- [x] Hardened preset identity validation so duplicate/malformed record IDs are explicit failures rather than silent set/dictionary normalization.
- [x] Live census: **149 canonical character names / 29 bridge records / 40 preset records / 20 Partner Customization records / 20 reconciliation records**; **0 duplicate bridge IDs / 0 duplicate present source names / 0 malformed bridge IDs / 0 duplicate preset IDs / 0 malformed preset IDs**.
- [x] Existing unresolved presentation boundaries remain preserved, including Captain Ginyu Presets 3/4 source-body labels; no character identity was inferred or renamed.
- [x] Refreshed `docs/data/characters/character-presentation-consumer-audit.json` to schema **1.1.0**.
- [x] Validator commit: `1bb36e8d85aa0a83487e98b502b7da5a8a6a38e0`; audit refresh: `fcc6c3746e5eea8b0c5116da5fd103797cf328ba`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: continue into the remaining published character/navigation consumer chain (especially published Character/DLC links and Partner Customization page validation), looking for the same class of hidden representation, duplicate, and one-way-link assumptions before broad content research.


### 2026-09-22 cycle update — Partner Customization navigation join hardening
- [x] Continued the published character/navigation chain into `scripts/validate_partner_customization_character_navigation.py`.
- [x] Repaired a deterministic hidden assumption: key/reconciliation identity parity was previously checked with a sorted positional `zip()`. The validator now joins records by their explicit numeric key and requires the two key sets to equal exactly `1..20`, preventing missing/duplicate rows from being masked by positional pairing.
- [x] Added explicit bridge-ID uniqueness and string-shape validation plus integer-shape validation for key and reconciliation numbers.
- [x] Live repository census: **20 key records / 20 reconciliation records / 29 bridge records / 149 canonical character names / 20 page search links**; all exact key sets, identity joins, bridge resolutions, and search links remain clean.
- [x] Refreshed `docs/data/characters/partner-customization-character-navigation-audit.json` to schema **1.1.0**.
- [x] No partner identity, DLC ownership claim, raid history, or gameplay fact was changed; existing partially-verified evidence boundaries remain intact.
- [x] Validator commit: `def0a7538030c738947d3307bf853ee5bd1fb6f0`; audit refresh: `3a622709aab48c4f5ef58ed5fc101b36e6e5c64d`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: audit `scripts/validate_published_character_dlc_navigation.py` for the same silent duplicate/type/representation assumptions, then refresh its published Character/DLC navigation audit if the live contract is clean.


### 2026-09-22 cycle update — Published Character/DLC navigation shape hardening
- [x] Continued into `scripts/validate_published_character_dlc_navigation.py`.
- [x] Hardened published local-link validation so each required href must occur exactly once rather than merely appearing somewhere in the page.
- [x] Hardened canonical character identity validation against malformed/non-string character names and duplicate bridge source names/targets.
- [x] Hardened canonical DLC/PQ identity validation against malformed DLC IDs/names, malformed `pq_requires_dlc` targets, and duplicate canonical PQ→DLC target rows that could previously be collapsed by sets.
- [x] Live contract remains clean: **149 canonical characters / 15 DLC-character bridge records / 20 canonical DLC identities / 86 canonical PQ→DLC edges / 20 unique DLC targets**; no missing/orphan identities or duplicate/malformed navigation identity data.
- [x] Refreshed `docs/data/characters/published-character-dlc-navigation-audit.json` to schema **1.2.0**.
- [x] Validator commit: `93cf57755cbca321b476f5d5e4aac52b717b40c3`; audit refresh: `43f44fff1fe3477bf01f0e18acb6cfb764646b24`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: continue from the cross-domain registry into the next registered consumer after published Character/DLC navigation, prioritizing deterministic Search/landing or reverse-navigation validators with remaining silent set/dictionary collapse or endpoint-shape assumptions.

### 2026-09-22 — Published Search consumer contract hardening
- [x] Audited the live published Search surface after the character/DLC navigation consumer chain: `docs/Search.md`, `docs/assets/search.js`, and `docs/search-data.html`.
- [x] Added `scripts/validate_search_consumer.py` to enforce the deterministic Search landing contract: `/Search/` permalink, search input/results/status hooks, `?q=` parsing and initial-query consumption, local generated `search-data.json` fetch, live input listener, and zero external fetch endpoints.
- [x] Added `docs/data/search-consumer-audit.json` and registered the audit/validator in `docs/data/pq-cross-domain-index.json`.
- [x] Static live-source validation is clean: all required Search hooks and query/navigation contracts are present; the search-index producer uses the repository's `site.pages` corpus and excludes its own generator page; Search JS has **0 external fetch endpoints**.
- [x] Evidence boundary: this validates presentation wiring only. It does not claim that the generated search corpus contains every canonical database record or that search ranking is exhaustive.
- [ ] CI: no successful GitHub Actions workflow/check exposed; CI success is not claimed.
- [x] Commits: validator `d0b319c5974c9a6861bff364136f6b2deaad0a0b`; audit `99474ac1c291d4c49b85cd6ce2d1c853f9d63440`; registry `c041e968d72fe23d54c778d42e73b0d40bf9b21d`.
- [ ] Exact next task: inspect the next registered Search/landing consumer or unvalidated cross-domain producer for deterministic one-way navigation, stale scalar/list assumptions, or canonical endpoint drift; prefer exact local consumer parity over new inferred relationships.

### 2026-09-22 — Equipment provenance batch `equip-081`–`equip-090`
- [x] Recomputed the live equipment endpoint layer before editing: **174 canonical equipment/accessory identities / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique target endpoints / 0 broken endpoints**.
- [x] Enriched the live records `equip-081`, `082`, `083`, `084`, `086`, `087`, `089`, and `090` with independently checked slot coverage and additional maintained catalog provenance.
- [x] Preserved `equip-088` as a normalized historical alias to canonical accessory `acc-012`; no duplicate identity was created.
- [x] Confirmed `equip-085` is absent from the live canonical layer and did not fabricate a record to fill the numeric gap.
- [x] Evidence used includes the maintained Xenoverse 2 equipment catalog, the maintained all-186-PQ Steam guide, dedicated Goku's Turtle Hermit Gi (King Kai) documentation, Whis Symbol Gi documentation, and an independent GameFAQs equipment discussion for component coverage.
- [x] Validation: **174/174 endpoint identities resolve; 0 duplicate IDs; 125 forward edges; 123 reverse endpoints; 0 broken endpoints**. Batch records present: 9/9 expected live IDs; 8/8 enriched non-alias records have slot coverage; `equip-088` remains explicitly normalized.
- [x] Evidence boundary preserved: no reward probability, guaranteed-drop claim, combat effect, or unsupported DLC attribution added.
- [ ] CI: no successful workflow/check exposed; CI success is not claimed.
- [x] Commits: canonical `1b2f96e444c1f0ce17174cba4d4d95841ae671cd`; detail audit `007c9a768edd1483583cec7336b2f7537366922a`.
- [ ] Exact next task: enrich the next deterministic equipment endpoint tranche, beginning with **`equip-091`–`equip-100`**, after a fresh endpoint census; preserve normalized aliases and canonical accessory bridges.

### 2026-09-22 — Equipment detail enrichment `equip-091`–`equip-100`
- [x] Fresh live census before/after: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique targets / 0 broken endpoints**.
- [x] Enriched the 10 legacy endpoints with source-backed category/slot metadata and provenance. Two legacy endpoints already had canonical accessory identities and were preserved as bridges rather than duplicated: **`equip-091 → acc-058` (SSGSS Goku Wig)** and **`equip-093 → acc-070` (Videl (DB Super) Wig)**.
- [x] Classified the eight non-aliased endpoints: `equip-092` Vegeta's Shirt (upper body); `094` Orange Piccolo's Clothes (upper/lower/feet, no hands); `095` Videl (DB Super)'s Clothes (four-piece); `096` Belmod's Clothes (four-piece); `097` Goku (Mini)'s Gi (four-piece); `098` SS4 Goku (DAIMA) Suit (four-piece); `099` SS4 Goku (DAIMA) Wig & Tail (accessory); `100` SS3 Vegeta (DAIMA) Battle Suit (four-piece).
- [x] DLC provenance reconciled: `093–095` Future Saga Chapter 1; `096–097` Future Saga Chapter 2; `098–100` Dragon Ball DAIMA Pack; `091–092` base-game-era PQ endpoints.
- [x] Evidence used: maintained DBXV2 equipment catalog; maintained all-186-PQ guide; DBXV2 DLC documentation; Bandai Namco DAIMA Pack announcement; independent GameFAQs equipment discussion for Orange Piccolo/Videl component coverage.
- [x] Added and registered `docs/data/equipment/equipment-091-100-detail-audit.json`.
- [x] Evidence boundary preserved: no reward probability, guaranteed-drop semantics, combat/stat effect, or unsupported restriction was inferred. Vegeta's Shirt remains an upper-body endpoint rather than being promoted to a full set.
- [x] Validation: 174 combined records / 139 legacy records; 0 duplicate IDs/names; 125 forward / 123 reverse / 0 broken; all 10 legacy batch endpoints have slot coverage; 8 non-alias canonical endpoints have explicit classification.
- [ ] CI: no successful workflow/check exposed; CI success is not claimed.
- [x] Commits: canonical `267cb0dcd98b9c5b8307e0d0f1ca5ac4b3da65cb`; combined layer `af70f83339d32794fa6c577ebfadc97850bd0f62`; audit `87b75353add617b60607c476dacb3442dc95ba3b`; registry `bb005ca06da404f9027bf18148e6204f4b72cfe3`.
- [ ] Exact next batch: fresh census, then continue the equipment identity/detail stream with **`equip-101`–`equip-110`**, preserving any canonical accessory bridges before adding metadata.

### 2026-09-22 — Equipment detail enrichment `equip-101`–`equip-110`
- [x] Fresh endpoint census and bounded batch completed: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique targets / 0 broken endpoints**.
- [x] Enriched `equip-101`–`equip-110` with source-backed category, slot coverage, and DLC provenance.
- [x] Classified accessories: SS3 Vegeta (DAIMA) Wig, Glorio Wig, Panzy Wig, Golden Frieza Head, Broly Wig (Black Hair, Normal), Dragon Ball Balloon.
- [x] Classified clothing: Glorio's Clothes (upper/lower/feet), Panzy's Clothes (four-piece), Golden Frieza Suit (four-piece), Cheelai's Coat (upper body).
- [x] Reconciled provenance: `101–105` Dragon Ball DAIMA Pack; `106–110` Future Saga Chapter 3.
- [x] Evidence used: maintained DBXV2 equipment catalog, DBXV2 DLC documentation, maintained all-186-PQ Steam guide, Glorio/Panzy character documentation, and independent PQ184 documentation.
- [x] Added and registered `docs/data/equipment/equipment-101-110-detail-audit.json`.
- [x] Evidence boundary preserved: no reward probability, guaranteed-drop semantics, combat/stat effect, or unsupported restriction was inferred.
- [ ] CI: no successful workflow/check exposed; CI success is not claimed.
- [x] Commits: canonical `34ffe98a4702514806dbe425aba3f38f18804e6d`; combined `9bcf4242481a7d2283e7fe4db7894e923be2c13a`; audit `8bcbb0f4bf6d846b2557c84631851f07599e4af1`; registry `b51aa73512fb62822681a83b8a80af358142f5d2`.
- [ ] Exact next batch: fresh census, then **`equip-111`–`equip-120`**; preserve any canonical accessory bridges and historical aliases.

### 2026-09-22 — Equipment detail enrichment `equip-111`–`equip-120`
- [x] Fresh live census: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique targets / 0 broken endpoints**.
- [x] Enriched `equip-111`–`equip-120` with source-backed category, slot coverage, and DLC provenance.
- [x] Classified clothing: Goku (Ultra Supervillain Quelled)'s Clothes (four-piece), Fu (Ultra Supervillain)'s Clothes (four-piece), Pan's Clothes (four-piece), Super 17's Clothes (four-piece), GT Vegeta's Jacket (upper body).
- [x] Classified accessories: Goku (Ultra Supervillain Quelled) Wig, Fu (Ultra Supervillain) Set, Fu Set 2, Pan's Bandanna, Yamcha's Baseball Hat.
- [x] Reconciled provenance: `111–115` Future Saga Chapter 4; `116–120` base-game PQ-era content.
- [x] Evidence used: maintained DBXV2 equipment catalog, maintained all-PQ Steam guide, and independent Dragon Ball documentation for Yamcha's Baseball Hat.
- [x] Added and registered `docs/data/equipment/equipment-111-120-detail-audit.json`.
- [x] Evidence boundary preserved: GT Vegeta's Jacket remains upper-body-only; no reward probability, guaranteed-drop semantics, combat/stat effect, or unsupported restriction was inferred.
- [ ] CI: no successful workflow/check exposed; CI success is not claimed.
- [x] Commits: canonical `55f163ba865fecb908a2f1dc259ea455aafb17cf`; combined `bf0f9087f5ac0d56fc34fa69860717bb3817d3a9`; audit `a8e2b5c6029f45e4f0b9bf0e61d58d21b80b19b8`; registry `0a0194f191171bfff92e201de90a08cfeb6f4500`.
- [ ] Exact next batch: fresh census, then **`equip-121`–`equip-130`**; preserve canonical accessory bridges and historical aliases.

### 2026-09-22 — Equipment detail enrichment `equip-121`–`equip-130`
- [x] Fresh census exposed a correction: `equip-121` **Mr. Shape Up L** was incorrectly represented as equipment. Independent evidence identifies it as a consumable capsule/material, so it was removed from both canonical equipment layers; the PQ99 reward remains source-backed in PQ reward data.
- [x] Preserved canonical accessory bridge `equip-123 → acc-063` for SSGSS Vegeta Wig; no duplicate identity was created.
- [x] Enriched the remaining live endpoints `equip-122`, `124`–`130` with source-backed category/slot/DLC metadata.
- [x] Classified clothing: Whis Symbol Battle Suit (four-piece), Champa's Clothes (four-piece), Battle Suit (Cabba) (four-piece), Android 14's Clothes (four-piece), Android 13's Clothes (four-piece), Super Android 13's Clothes (four-piece), Future Mai's Clothes (four-piece), Goku Black's Clothes (upper/lower/feet; no hands).
- [x] Reconciled provenance: `122` Movie Costume Pack (Free); `124–125` Super Pack 1; `126–128` Super Pack 2; `129–130` Super Pack 3.
- [x] Added and registered `docs/data/equipment/equipment-121-130-detail-audit.json`.
- [x] Validation: **173 combined equipment/accessory records / 0 duplicate IDs / 124 PQ→equipment forward edges / 122 unique targets / 0 broken endpoints**; 8 live non-bridge endpoints have slot coverage and explicit classification.
- [ ] CI: no successful workflow/check exposed; CI success is not claimed.
- [x] Commits: canonical `cea284c71ec7d9e657ca0d675dd3402d28e41f4f`; combined `4ce040ffa6ce1cb299c747d2a9ccef1a67288696`; crosslink `9f6203ef50f15168448fa821c7b9232113776f96`; audit `a75e1e28f7dbe94f5543b3d2160f6e70fdbf1220`; registry `93ac07fc9f37120ecec38c9232cb7171ed15965a`.
- [ ] Exact next batch: fresh census, then **`equip-131`–`equip-140`**, preserving canonical accessory bridges and correcting any non-equipment false positives before enrichment.

### 2026-09-22 — Equipment detail enrichment equip-131–equip-140
- [x] Enriched equip-131–equip-140 with source-backed category, slot coverage, and DLC provenance while preserving the canonical accessory normalization equip-133 → acc-064.
- [x] Provenance reconciled: 131–135 Super Pack 4; 136–139 Extra Pack 1; 140 base game.
- [x] Added and registered docs/data/equipment/equipment-131-140-detail-audit.json.
- [x] Reconciled docs/data/pq-equipment-crosslink-report.json to the live **173-record** canonical equipment/accessory layer: **124 forward / 122 unique targets / 122 reverse records / 0 missing / 0 extra / 0 duplicate pairs / 0 unresolved endpoints**; normalized legacy accessory IDs and removed stale equip-121 reverse navigation.
- [x] Validation clean; no canonical relationship identities were invented or renamed.
- [ ] CI: no successful workflow/check exposed; CI success is not claimed.
- [x] Commits: a17c8281dee8278fdf396a16c4a858f01fde1330, 85b3d1d926778e3b8b3ccc7e4e143e30b1c293e4, 5e41477a3ade6a3bfd16144161497606a7511b00, 14f8be396cfa3a27066351ee0b45ad9213df549e, c01e71b3febc5447238c2a55a4a1e913c0313ad0, 4f45d5eacb9b566b8e59ad42a405b8407d19b329.
- [ ] Exact next task: fresh census, then enrich **equip-141–equip-150**, preserving canonical accessory bridges and correcting any non-equipment false positives before enrichment.

### 2026-09-22 cycle update — PQ endpoint identity correction and current cross-domain baseline
- [x] Fresh live census exposed a deterministic mismatch left behind by the earlier equip-121 correction: pq-099 → Mr. Shape Up L was still present in the canonical pq_rewards_equipment relationship layer even though the endpoint had already been removed from the equipment identity layers.
- [x] Removed only the false canonical equipment relationship pq-099 → Mr. Shape Up L; the underlying PQ99 reward listing remains preserved in the PQ reward data and no replacement equipment identity was invented.
- [x] Removed the stale Mr. Shape Up L projection entry from docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json and synchronized its current equipment count.
- [x] Refreshed current cross-domain audit/status counts and gate text: 859 canonical relationship edges = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming. Historical 862/840/860 fields remain preserved as history.
- [x] Refreshed docs/data/pq-endpoint-navigation-validation.json: 0 missing targets / 0 duplicate pairs / 0 invalid PQ IDs across skills, Super Souls, equipment, characters, and DLC; equipment is now 124 edges / 122 unique targets and the endpoint status is clean.
- [x] Added docs/data/pq-endpoint-navigation-correction-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Canonical equipment cross-link projection remains aligned at 124 forward / 122 unique targets / 122 reverse records / 0 unresolved endpoints.
- [ ] Runtime CI/workflow execution remains unavailable for the current direct-commit chain; no CI success claimed.
- [ ] Exact next gate: inspect/validate deterministic unified reverse-index generation only after standalone reverse-index runtime validation is available; preserve partial normalized source maps as non-canonical evidence layers.
### 2026-09-22 cycle update — PQ99 consumer/projection reconciliation and reverse-index gate
- [x] Fresh canonical/consumer comparison found another deterministic stale endpoint: pq-099 still listed Mr. Shape Up L in parallel-quests-record-layer.json under equipment_rewards even though the canonical relationship layer had already removed it as false equipment. The raw rewards list remains unchanged, preserving the actual PQ reward evidence.
- [x] Removed only Mr. Shape Up L from PQ99's structured equipment_rewards; exact canonical-vs-record equipment pair parity is now 124/124, 0 missing, 0 extra.
- [x] Synchronized current consumer/audit artifacts: pq-page-consumer-audit.json, pq-explorer-reward-navigation-audit.json, pq-reference-page-audit.json, pq-cross-link-integrity-audit.json, pq-endpoint-navigation-audit.json, pq-presentation-index-identity-audit.json, and record-reverse-pq-navigation-audit.json.
- [x] Current canonical relationship baseline is now consistently represented as 859 total = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming in current fields; dated historical 860/862/840 counts remain preserved where they belong.
- [x] Structural recheck of the four standalone normalized reward maps against their standalone reverse indexes is clean: PQ81-120 109 pairs, PQ121-142 89, PQ143-162 87, PQ163-186 72; 0 missing / 0 extra across skills, Super Souls, clothing, accessories. This is an exact source-map parity reimplementation of the repository validator logic, not a claim of runtime execution.
- [x] Runtime attempt is blocked by the execution environment: repository clone could not resolve github.com, so the two reverse-index validator scripts could not be executed locally. No runtime/CI success is claimed.
- [x] Refreshed standalone/unified reverse-index audits and producer census current fields to the 859/124 baseline without rewriting historical records.
- [x] Updated pq-endpoint-alias-granularity-map.json current baseline from 860 to 859 while preserving the two explicit equipment naming conflicts and six DLC granularity mappings.
- [x] No equip-141 through equip-150 records exist in the live legacy equipment layer; maximum legacy ID remains equip-140, so no nonexistent records were invented.
- [ ] Exact next task: fresh census, then audit the remaining registered cross-domain presentation/identity consumers for stale 859/124 baselines; after that, use the alias/granularity bridge to resolve only independently evidenced equipment naming conflicts.


### 2026-09-22 — Explicit bridge metadata validation hardening
- [x] Audited the non-PQ presentation/identity consumer chain: cross-link contract → alias/granularity bridge → endpoint-navigation validator → generated navigation/identity reports.
- [x] Confirmed the current canonical baseline remains **859 relationships / 124 equipment**, and stale 860/125 references found by repository search are historical audit material rather than current projection fields.
- [x] Hardened `scripts/validate_pq_endpoint_navigation.py` so equipment conflict bridge records must carry a PQ ID, source label, explicit-conflict classification, at least two canonical targets, and evidence; DLC granularity records must carry a PQ range, source label, explicit deterministic-granularity classification, and canonical targets.
- [x] Validator bridge failures are now included in the overall non-zero failure path instead of allowing structurally incomplete presentation mappings to appear clean.
- [ ] Next gate: inspect the remaining registered presentation consumers and generated reports for field-level schema drift, then perform a full executable validation when repository runtime/CI execution is available.


### 2026-09-22 cycle update — registered non-PQ consumer baseline census
- [x] Completed a fresh static direct-fetch census of the registered non-PQ presentation/identity consumers after the 859/124 correction chain.
- [x] Audited 16 registered consumer/projection artifacts and confirmed **0 deterministic current 860/862/125/123 scalar mismatches**; historical snapshots remain preserved as history.
- [x] Confirmed current canonical baseline: **859 total = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; equipment projection **124 forward / 122 reverse**.
- [x] Added and registered `docs/data/pq-non-pq-consumer-census-2026-09-22.json` and `scripts/validate_pq_non_pq_consumer_census.py`.
- [x] Preserved explicit equipment conflicts, DLC granularity mappings, and the 13 Super Soul acquisition-index reconciliation findings without promoting speculative relationships.
- [ ] Runtime/CI execution remains unavailable; no executable validation claimed.
- [ ] Exact next task: resume the P1 provenance queue at **Prominence Flash (`skill-prominence-flash`)**, with a fresh two-source census and independent acquisition/source verification before provenance-only edits.


### 2026-09-22 cycle update — character Markdown preset-consumer audit
- [x] Fresh live census: **149 canonical character identities / 29 bridge records / 40 preset producer records / 17 preset character IDs / 247 explicit PQ→character references**; prior 45-record preset count remains historical and is superseded by the live 40-record producer census.
- [x] Audited the character-facing Markdown consumers docs/Characters.md and docs/Character-Core-Profiles.md for hard-coded preset labels and canonical explorer/search navigation.
- [x] Confirmed docs/Characters.md links to the canonical Characters-All.html explorer and Character-Core-Profiles.md uses the site's Search-first navigation design.
- [x] Deterministic preset-label scan found **0 hard-coded preset-label matches** in those two Markdown consumers; no one-way preset navigation repair was necessary there.
- [x] Extended scripts/validate_character_presentation_consumers.py with the Markdown-consumer checks and updated docs/data/characters/character-presentation-consumer-audit.json to register the two pages.
- [x] Evidence boundary preserved: this audit does not infer missing preset numbers/loadouts, unlock routes, DLC ownership, or Captain Ginyu body-swap identity. The two Captain Ginyu labels remain explicitly unresolved presentation identities.
- [ ] CI/runtime execution remains unavailable; no executable validation or CI success claimed.
- [x] Commits: validator 44680366def03b1fdfc7d4c32eb05b9039a61c09; audit dd7a1122748cbe731e0ec6c26da71c9e02ebe23b.
- [ ] Exact next batch: audit the remaining **PQ-facing reward/acquisition summary consumers**, prioritizing docs/Guides.md, docs/Skills-Complete-Database.md, docs/QQ-Bangs.md, and other summary/index pages for deterministic canonical endpoint drift or one-way navigation; do not infer new relationships.


### 2026-09-22 cycle update — character Markdown audit validator correction
- [x] Corrected the Markdown preset-label scanner in scripts/validate_character_presentation_consumers.py so the regex uses actual word/whitespace boundaries rather than escaped literal backslashes.
- [x] Re-read docs/Characters.md and docs/Character-Core-Profiles.md and confirmed the deterministic scan still has **0 hard-coded preset-label matches**; Characters.md links to Characters-All.html and Character-Core-Profiles.md exposes Search-first navigation.
- [x] Synchronized docs/data/characters/character-presentation-consumer-audit.json to validator commit `869d6435813d566a141d1270f97516241d660c00`.
- [ ] CI/runtime execution remains unavailable; executable validator success is not claimed.
- [ ] Exact next batch remains the **PQ-facing reward/acquisition summary consumer audit**, beginning with docs/Guides.md, docs/Skills-Complete-Database.md, docs/QQ-Bangs.md and related summary/index surfaces; inspect deterministic endpoint drift and one-way navigation only.


### 2026-09-22 cycle update — PQ-facing reward/acquisition summary consumer audit
- [x] Fresh live canonical census: **186 PQ records / 859 relationship edges = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**.
- [x] Audited the bounded summary batch: `docs/Guides.md`, `docs/Skills-Complete-Database.md`, `docs/QQ-Bangs.md`, `docs/Skills-Unlock-Database.md`, `docs/Accessory-Acquisition-Matrix.md`, and `docs/Farming-Routes.md`.
- [x] Confirmed the first five acquisition-summary consumers preserve the canonical relationship/evidence boundary: PQ association is not silently promoted to guaranteed reward, Ultimate Finish trigger, or drop-rate fact.
- [x] Confirmed `docs/QQ-Bangs.md` keeps the PQ83 Super Mix Capsule Z route explicitly in community/research evidence rather than the canonical `pq_features_farming` layer.
- [x] Repaired `docs/Farming-Routes.md` by replacing the unsupported **“Best Overall”** TP Medal route label with neutral **“Commonly cited online route”** wording and an explicit efficiency caveat; no canonical relationship changed.
- [x] Added `docs/data/pq-summary-consumer-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Historical 860/125 counts found in older handoff entries remain preserved under append-only policy and are not current-state inputs.
- [ ] Runtime/CI execution remains unavailable; no executable validation or CI success claimed.
- [x] Commits: Farming-Routes `6fb46f2783ac95232ec20a9e5eff52989a610784`; summary audit `9518392fd2413b097784cd572d2b52c290077c41`; index registration `a6bfe629cc7c5ce0f7f54347950fccc553983cdd`.
- [ ] Exact next batch: inspect **direct PQ page templates and DLC requirement presentation** for canonical endpoint navigation, stale field-level scalars, and one-way reward links; do not infer new relationships.


### 2026-09-22 cycle update — direct PQ template and DLC requirement presentation audit
- [x] Fresh live census: **186 PQ records / 859 unique relationships = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; canonical DLC identity layer has **20 records**.
- [x] Audited the live docs/Parallel-Quests-All.html template against docs/data/parallel-quests-record-layer.json, docs/data/pq-reward-relationships.json, and docs/data/dlc/canonical-dlc-identity.json.
- [x] Confirmed the explorer loads local canonical PQ records and canonical relationship data, derives displayed DLC labels from pq_requires_dlc, and preserves cross-navigation for Skills, Super Souls, Equipment, Characters, and DLC.
- [x] Audited the existing PQ reward-navigation and DLC presentation validators; their contracts cover exact canonical pair parity, DLC identity resolution, reverse-index parity, duplicate detection, and HTML link construction.
- [x] Found and repaired two stale current-facing projection artifacts discovered during the audit: docs/data/pq-nonreward-provenance-audit.json had an obsolete 88-edge/21-target DLC census; docs/data/pq-cross-domain-audit.json had a 862-edge pre-repair snapshot mislabeled as a current 2026-09-22 integrity/stable baseline. Historical values were preserved under explicit historical keys.
- [x] Added docs/data/pq-direct-template-dlc-consumer-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] No canonical PQ relationship or DLC identity was created, removed, or inferred.
- [ ] Runtime/CI execution remains unavailable; validation is static direct-fetch/contract comparison only.
- [x] Commits: DLC provenance 41537dfbd4bdefade42d746217bcea1577e9594d; cross-domain audit correction ed56ee4b2fa23aae4546968805281caf8dd4fd87; direct-template audit f0ec62c44488af1af9ef61f9180e21bbfcc87a95; index registration c7a3e86ed5d4f11eb19fa56b96b8e4f14fa3d301.
- [ ] Exact next batch: perform the P1 provenance census for skill-prominence-flash using the live skill/PQ layers, independently reconcile its acquisition/source endpoint, and make provenance-only changes without altering canonical relationship identities.


### 2026-09-22 cycle update — Super Soul acquisition reconciliation PQ151–153
- [x] Fresh canonical Super Soul census: **151** canonical PQ→Super Soul relationships; partial PQ41–186 acquisition projection now contains **127** typed references.
- [x] Bounded batch: reconciled five previously missing canonical pairs from **PQ151–153**: `I think I'm getting the hang of this.`, `I'll keep adding a bit of power to my attacks!`, `I will put a stop to you, fiend!`, `There's more where that came from!`, and `You're not much of a fun fight!`.
- [x] Evidence: the maintained Steam all-PQ guide explicitly lists the five named Super Souls in the Basic Reward sections for PQ151, PQ152, and PQ153; independent Super Soul documentation corroborates the PQ153 entries.
- [x] Preserved evidence boundary: the partial acquisition index remains a research projection; no canonical relationship was created or changed. The PQ158 source-layer typo (`Heh heh! I'm not a rusty as I look!`) was deliberately left unresolved rather than silently normalized to the canonical spelling.
- [x] Exact post-edit pair comparison for PQ41–186: **133 canonical pairs in scope / 127 indexed pairs / 125 exact overlap / 8 remaining differences**. Remaining differences are six exact canonical gaps plus two capitalization variants.
- [x] Updated `docs/data/super-souls/pq-acquisition-index-041-186.json` and `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json` with the bounded reconciliation and evidence boundary.
- [ ] Runtime/CI execution remains unavailable; validation was static direct-fetch JSON parsing and exact pair comparison.
- [x] Commits: acquisition projection `887f754bc86370d5de981ad60d32ca0a6c879e7c`, source-spelling correction `e883d4df5a01d50adb97b8e3175cd06911b543f9`, reconciliation audit `50a341a0cb5ff61e051896015c74c48d571e1476`.
- [ ] Exact next batch: independently reconcile the remaining six missing Super Soul pairs, beginning with **PQ58 `Killed all Earthlings!`**, then **PQ158**, while preserving the unresolved PQ158 source spelling and the two capitalization variants as noncanonical projection findings.


### 2026-09-22 cycle update — Super Soul acquisition reconciliation PQ58
- [x] Bounded batch: reconciled canonical PQ58 → Super Soul `Killed all Earthlings!` into the partial PQ41–186 acquisition projection.
- [x] External evidence: the maintained Super Soul/PQ references explicitly identify `Killed all Earthlings!` as obtained from **Parallel Quest 58**. cite
- [x] No canonical relationship was modified; this was a provenance/projection reconciliation only.
- [x] Exact post-edit comparison: **133** canonical PQ41–186 Super Soul pairs / **128** indexed pairs / **126** exact overlap / **7** remaining differences. Remaining differences are five exact canonical gaps (both PQ158 entries, PQ174, PQ178, PQ179) plus the two capitalization variants at PQ164/PQ173.
- [x] Updated `docs/data/super-souls/pq-acquisition-index-041-186.json` and `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json`.
- [ ] Runtime/CI remains unavailable; validation was static direct-fetch JSON parsing and exact pair comparison.
- [x] Commits: acquisition projection `6ff4b3eb2e39cd413917ad46e527d36e19727802`; reconciliation audit `52f0fc86d78277fa4648edebcca26975a8506bf0`.
- [ ] Exact next batch: independently reconcile the **two PQ158 Super Soul pairs**, preserving the existing source spelling conflict, then PQ174/PQ178/PQ179.


### 2026-09-22 cycle update — Super Soul acquisition reconciliation final five exact gaps
- [x] Fresh live census before editing: **151 canonical PQ→Super Soul relationships**; the partial PQ41–186 acquisition projection had **128 structured pairs / 7 reconciliation findings** before this batch.
- [x] Bounded batch: reconciled the final five exact canonical gaps: **PQ158** → `Heh heh! I'm not as rusty as I look!` and `See? It's a good thing I was here, right?`; **PQ174** → `I'll surpass you as I am, with my OWN power!`; **PQ178** → `I'll take you all on at once!`; **PQ179** → `Here I go!`.
- [x] Evidence: maintained Super Soul/PQ references corroborate the five acquisitions; independent GameFAQs documentation also corroborates the Future Saga Super Soul acquisition context. cite
- [x] Preserved source-layer wording conflicts for PQ158 and PQ178 explicitly; the structured projection uses canonical names instead of treating variants as separate identities.
- [x] Post-write validation: **133 canonical PQ41–186 pairs / 131 indexed pairs / 131 exact overlap / 0 exact missing / 2 capitalization variants** (PQ164/PQ173); **83 unique PQ records / 131 unique structured pairs / 0 duplicates**.
- [x] Updated `docs/data/super-souls/pq-acquisition-index-041-186.json` and `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json`; no canonical relationship identity was added, removed, or renamed.
- [ ] Runtime/CI execution remains unavailable; validation is static JSON parsing and exact pair/census comparison only.
- [ ] Exact next batch: audit the two remaining capitalization variants (**PQ164** and **PQ173**) against an independent exact-text source; if no stronger evidence resolves them, preserve them as presentation/source-normalization differences and move to the next structural cross-domain gap.


### 2026-09-22 cycle update — Super Soul acquisition projection exact parity and capitalization audit
- [x] Independently checked the two previously flagged capitalization variants: PQ164 is “This place will be your grave!” and PQ173 is “You will know the power of the gods!”. External Super Soul/PQ references support those spellings. cite
- [x] Re-read the live canonical relationship layer: it contains 133 PQ41–186 Super Soul relationships, including alternate repository wording at PQ158 and PQ178.
- [x] Preserved canonical relationship targets exactly in the acquisition projection, including both PQ158 wording forms and both PQ178 wording forms, rather than silently rewriting canonical data.
- [x] Final exact-pair validation: 133 canonical / 133 indexed / 133 exact overlap / 0 missing / 0 extra; 83 unique PQ records / 133 unique pairs / 0 duplicate pairs.
- [x] Updated the acquisition projection and reconciliation audit.
- [ ] Runtime/CI remains unavailable; validation is static JSON parsing and exact pair comparison only.
- [x] Acquisition projection parity commit: 9edc9d308fc57d9ebfee6ceed4979d4d321c7fef.
- [ ] Exact next batch: move to the next highest-priority structural cross-domain gap using the live TODO/handoff priority.


### 2026-09-22 cycle update — Prominence Flash provenance completion and next-skill handoff reconciliation
- [x] Fresh live canonical/index census for skills: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; Prominence Flash exists in both layers as `skill-prominence-flash`.
- [x] Re-inspected the canonical and index Prominence Flash records. Both agree on Ultimate / Ki Blast, PQ137 acquisition, Ultra Pack 1 provenance, 300 Ki, all-CaC-race availability, and the current evidence boundary around Ultimate Finish semantics.
- [x] Independent acquisition verification: the maintained all-186-PQ Steam guide explicitly lists Prominence Flash under **PQ137 — Tournament of Power Round 2 — Basic Reward**; an independent Dragon Ball Wiki reference identifies it as an Ultra Pack 1 skill obtained through PQ137. cite
- [x] No canonical skill identity, acquisition endpoint, reward relationship, or Ultimate Finish flag was changed; this pass confirms provenance parity only.
- [x] Existing third-party source is already recorded in both canonical and index skill records, so no duplicate provenance entry was added.
- [ ] Runtime/CI remains unavailable; validation is static direct-fetch, source/census comparison, and exact endpoint verification.
- [ ] Exact next batch: **Requiem of Destruction (`skill-requiem-of-destruction`)** — recompute its live canonical/index census, inspect the full record, and independently verify its acquisition/source endpoint before making any provenance-only changes.


### 2026-09-22 cycle update — Requiem of Destruction provenance verification
- [x] Live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-requiem-of-destruction`.
- [x] Canonical/index records agree on classification, 300 Ki cost, PQ106 acquisition, Super Pack 2 provenance, All CaC race scope, and `ultimate_finish_required: false`.
- [x] Independent verification: the maintained all-186-PQ guide lists **Requiem of Destruction** in **PQ106 — A Destructive Showdown — Basic Reward**. cite A separate PQ106 gameplay record likewise lists it under Basic Reward. cite
- [x] Existing repository sources already include the maintained Steam guide plus two Dragon Ball Wiki sources; no duplicate source was added.
- [x] Evidence boundary preserved: Basic Reward placement establishes the acquisition route but not a drop probability; no Ultimate Finish gate is inferred.
- [x] No canonical skill identity, acquisition relationship, DLC identity, or reward-tier field required modification; provenance was already correctly represented.
- [ ] Runtime/CI remains unavailable; validation is static direct-fetch, source comparison, and canonical/index parity.
- [ ] Exact next batch: continue the P1 skill provenance census with the next unfinished skill identified by the live handoff/TODO, without repeating completed Prominence Flash or Requiem of Destruction work.


### 2026-09-22 cycle update — Absolute Zero provenance and reward-tier reconciliation
- [x] Live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-absolute-zero`.
- [x] Independent evidence: the maintained all-186-PQ Steam guide explicitly lists **Absolute Zero** under **PQ96 — The Shadow Dragons — Basic Reward**; the dedicated skill reference independently identifies PQ96 as its Xenoverse 2 acquisition route. cite
- [x] The repository's existing older video evidence reports Absolute Zero as a PQ96 Ultimate Finish reward. The conflict is retained rather than erased; the current maintained reward transcription supports the canonical `ultimate_finish_required: false` value without inferring a probability.
- [x] Canonical/index parity preserved; only `last_verified` and provenance notes were strengthened to record the fresh independent check.
- [x] Cross-domain links already exist: PQ96 → Absolute Zero is represented in the PQ skill crosslink and unified reverse index.
- [ ] Runtime/CI remains unavailable; validation is static JSON parsing, canonical/index parity, and source-endpoint comparison.
- [ ] Exact next batch: continue the P1 skill provenance census with **All Clear (`skill-all-clear`)**, then proceed sequentially through the unfinished skill queue while preserving evidence conflicts.


### 2026-09-22 cycle update — All Clear mentor provenance verification
- [x] Live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-all-clear`.
- [x] Independent evidence: the maintained instructor-quest guide lists **All Clear** as **Cell's Initiation Test — Basic Reward**. cite The dedicated skill reference identifies the acquisition as training with Cell (Perfect), and the mentor roster independently lists All Clear among Cell's rewards. cite
- [x] Acquisition endpoint is therefore retained as Cell (Perfect) mentor training; no Parallel Quest acquisition, Ultimate Finish requirement, or probability is inferred.
- [x] Canonical/index provenance notes and `last_verified` were refreshed; no skill identity, classification, cost, or cross-domain relationship required correction.
- [x] Cross-domain mentor linkage already exists through `source_mentor: [mentor-cell]` in the canonical layer.
- [ ] Runtime/CI remains unavailable; validation is static JSON parsing, census, canonical/index parity, and source comparison.
- [ ] Exact next batch: continue the P1 skill provenance census with the next unfinished skill after `skill-all-clear`, preserving source conflicts and avoiding duplicate work.


### 2026-09-22 cycle update — Afterimage starting-skill provenance verification
- [x] Live census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-afterimage`.
- [x] Independent evidence: the dedicated Xenoverse 2 Afterimage reference identifies it as the starting move for the **Mixed** fighting-style choice. cite The CaC documentation independently states that the initial fighting-style choice determines starting skills and identifies Afterimage with Mixed. cite
- [x] Repository acquisition endpoint remains correct: `Starting move / initial "Mixed" choice`. No PQ/drop/Ultimate-Finish route was inferred.
- [x] Canonical/index provenance notes and `last_verified` refreshed; no identity, classification, cost, or cross-domain correction required.
- [ ] Runtime/CI remains unavailable; validation is static JSON parsing, census, canonical/index parity, and source comparison.
- [ ] Exact next batch: continue the P1 skill provenance census with **Afterimage Strike (`skill-afterimage-strike`)**, then proceed sequentially.


### 2026-09-22 cycle update — Afterimage Strike provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-afterimage-strike`.
- [x] Independent evidence: the current Afterimage Strike reference identifies **Parallel Quest 81 — "Wake Up!"** as the unlock; the maintained all-186-PQ Steam guide lists Afterimage Strike in PQ81's **Basic Reward**; an independent PQ81 record also lists it under Basic Reward.
- [x] Canonical `docs/data/skills.json` and generated/index `docs/data/skills-index.json` were updated only for provenance freshness: `last_verified` is now **2026-09-22**, and the evidence note records the independent verification. No skill identity, classification, acquisition endpoint, Ultimate Finish flag, or relationship was changed.
- [x] Evidence boundary preserved: Basic Reward placement establishes the documented acquisition route but does not establish a drop probability; no Ultimate Finish-only gate is inferred.
- [x] Static validation after writes: canonical/index record parity for name, unlock method, Ultimate Finish flag, and `last_verified` is **exact**; both records retain 4 sources and `skill-afterimage-strike` / PQ81 identity.
- [ ] Runtime/CI execution remains unavailable; no executable validation or CI success claimed.
- [x] Commits: canonical `82a108ca9a5b5d7ead16cd445cbb794b985241b0`; index `bdfc0921f2e2590c675685255583b707a1201ac1`.
- [ ] Exact next batch: continue the P1 skill provenance census with the **next unfinished skill after Afterimage Strike**, recomputing the live canonical/index census first and making provenance-only changes unless deterministic evidence requires a correction.


### 2026-09-22 cycle update — Early skill provenance batch: Android Rush / Angry Explosion / Angry Hit / Angry Shout
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded batch: Android Rush, Angry Explosion, Angry Hit, Angry Shout.
- [x] Independent evidence: Android Rush is Android 16 Training Lesson 2; Angry Explosion is Expert Mission 12; Angry Hit is Majin Buu Training Lesson 1; Angry Shout is a PQ68 Basic Reward.
- [x] Canonical and index records were refreshed to last_verified: 2026-09-22; the Angry Hit source endpoint was made more precise as Majin Buu mentor training — Lesson 1. No Ultimate Finish-only gate or drop probability was inferred.
- [x] Evidence limits preserved: PQ68 community reports discuss RNG/conditions but do not establish a numerical rate; repository canonical fields remain bounded to documented acquisition semantics.
- [x] Static validation: 452/452 records, no duplicate canonical IDs, and exact parity for affected records' verification date, unlock method, Ultimate Finish flag, and source counts.
- [ ] Runtime/CI remains unavailable; no executable CI success claimed.
- [x] Commits: canonical 520fcdea2c573ea25575213cde3a481361062fc2; index 9c86cf1aaac62eff3a61409292b1abd4d4c9f6b5.
- [ ] Exact next batch: continue the P1 skill provenance census with Apocalyptic Burst (skill-apocalyptic-burst), then proceed sequentially through the stale-last_verified queue while preserving reward-tier conflicts.


### 2026-09-22 cycle update — Apocalyptic Burst provenance reconciliation
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded record: `skill-apocalyptic-burst`.
- [x] Independent evidence confirms PQ161 — “Scream Team vs. Dream Team” as the acquisition endpoint. Current external sources conflict on reward tier: the maintained all-186-PQ Steam guide and an independent PQ161 gameplay record display Apocalyptic Burst in the Basic Reward list, while the repository's existing reward-tier evidence records a 45% Ultimate Finish bonus slot. cite
- [x] Conflict preserved rather than silently changing the canonical `ultimate_finish_required: true` field or inventing a drop probability. Canonical/index provenance notes and `last_verified` were refreshed only.
- [x] Static validation: 452/452 records, no duplicate IDs, and exact canonical/index parity for verification date, unlock method, Ultimate Finish flag, and source count.
- [ ] Runtime/CI remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `7168f8391783a3bf42c2f8530ea96a0551e8eefa`; index `fdd951c143a99e99e237d38c14c70d4d91a53dce`.
- [ ] Exact next batch: continue the stale-`last_verified` P1 skill provenance queue with **Arm Crash (`skill-arm-crash`)**, then proceed sequentially while preserving evidence conflicts.


### 2026-09-22 — Beast provenance verification
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded record: skill-beast.
- [x] Independent evidence confirms the existing acquisition endpoint: max friendship with Gohan (Adult) & Videl and Piccolo, then Piccolo's special training / Cell Max unlock mission.
- [x] Refreshed docs/data/skills.json and docs/data/skills-index.json to last_verified: 2026-09-22 and synchronized provenance notes/sources.
- [x] Added docs/data/skill-beast-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] No skill identity, classification, Ki cost, Ultimate Finish flag, or PQ relationship changed; no unsupported probability or gate was inferred.
- [x] Static validation: 452/452, no duplicate IDs, and exact affected-record semantic parity between canonical/index layers.
- [ ] Runtime/CI remains unavailable; no executable CI success claimed.
- [ ] Exact next batch: continue the stale-last_verified P1 skill provenance queue with the next unfinished skill after Beast.


### 2026-09-22 — Become Giant provenance verification
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded record: skill-become-giant.
- [x] Independent evidence confirms the existing acquisition endpoint: Namekian Awakening at Guru's House, with the documented Namekian and level-35 prerequisites and NPC/quest flow.
- [x] Refreshed docs/data/skills.json and docs/data/skills-index.json to last_verified: 2026-09-22 and synchronized provenance notes/sources.
- [x] Added docs/data/skill-become-giant-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] No skill identity, classification, Ki cost, Ultimate Finish flag, or PQ relationship changed; no unsupported probability or gate was inferred.
- [x] Static validation: 452/452, no duplicate IDs, and exact affected-record semantic parity between canonical/index layers.
- [ ] Runtime/CI remains unavailable; no executable CI success claimed.
- [ ] Exact next batch: continue the stale-last_verified P1 skill provenance queue with Big Bang Knuckle (skill-big-bang-knuckle), recomputing the live canonical/index census first.


### 2026-09-22 — Big Bang Knuckle provenance verification
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded record: skill-big-bang-knuckle.
- [x] Current dedicated evidence confirms Parallel Quest 172 — "Little Big Brother" as the acquisition endpoint and identifies Big Bang Knuckle as a 100-Ki Strike Super associated with Vegeta (Super Saiyan God) Ultra Supervillain. Official Dragon Ball documentation independently confirms the move in FUTURE SAGA Chapter 1.
- [x] Refreshed docs/data/skills.json and docs/data/skills-index.json to last_verified: 2026-09-22 and synchronized provenance notes/sources.
- [x] Added docs/data/skill-big-bang-knuckle-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved the existing 40% Ultimate Finish bonus-slot evidence and conflicting Basic Reward presentation; no new probability or reward-tier correction was inferred.
- [x] No skill identity, acquisition relationship, or DLC identity was changed.
- [x] Static validation: 452/452, no duplicate IDs, canonical/index affected-record parity preserved.
- [ ] Runtime/CI remains unavailable; no executable CI success claimed.
- [ ] Exact next batch: continue the stale-last_verified P1 skill provenance queue with the next unfinished skill after Big Bang Knuckle, recomputing the live canonical/index census first.


### 2026-09-22 cycle update — Arm Crash / Assault Vanish / Audacious Laugh / Blades of Judgment provenance
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded batch: skill-arm-crash, skill-assault-vanish, skill-audacious-laugh, skill-blades-of-judgment.
- [x] Independent evidence corroborated the existing acquisition endpoints: Nappa Lesson 1; PQ131; Zarbon Initiation Test; PQ112 Basic Reward.
- [x] Refreshed canonical/index last_verified to 2026-09-22 and preserved existing reward-tier conflicts and unresolved probability fields.
- [x] Added docs/data/skill-provenance-audit-2026-09-22-arm-through-blades.json.
- [x] Static validation: 452/452, no duplicate canonical IDs, affected canonical/index records remain aligned on verification and acquisition fields.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: recompute live census and continue the stale-last_verified P1 queue after Blades of Judgment.


### 2026-09-22 cycle update — Blaster Bomb / Blaster Cannon / Blaster Meteor / Blaster Shell / Blaster Stream / Blazing Attack provenance
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded batch: six Blaster/Blazing skills.
- [x] Independent current documentation corroborated PQ148 for Blaster Bomb, Blaster Cannon, and Blaster Stream; Broly mentor training for Blaster Meteor and Blaster Shell; and PQ136 for Blazing Attack.
- [x] Refreshed canonical/index last_verified to 2026-09-22; existing reward-tier and probability semantics preserved.
- [x] Added docs/data/skill-provenance-audit-2026-09-22-blaster-batch.json.
- [x] Static validation: 452/452, no duplicate IDs, affected verification/acquisition fields aligned.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: recompute live census and continue after Blazing Attack in the stale-last_verified queue.


### 2026-09-22 cycle update — Bloody Counter / Body Change / Bomber DX / Brave Heat / Brave Sword Attack / Brave Sword Slash provenance
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded batch: six stale P1 skill records.
- [x] Independent evidence corroborated Zarbon Lesson 2, Captain Ginyu Lesson 3, Nappa Initiation Test, Bardock Lesson 3, PQ117, and PQ116 acquisition endpoints. cite
- [x] Refreshed canonical/index last_verified to 2026-09-22; existing reward-tier semantics preserved and no unsupported probability inferred.
- [x] Added docs/data/skill-provenance-audit-2026-09-22-bloody-through-brave.json.
- [x] Static validation: 452/452, no duplicate IDs; affected records remain synchronized.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: recompute live census and continue after Brave Sword Slash.


### 2026-09-22 cycle update — Break Cannon / Brutal Buster / Burning Blast / Burning Shot / Burst Charge / Burst Reflection provenance
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded batch: six stale P1 skill records.
- [x] Independent evidence corroborated Nappa Lesson 3, PQ141, PQ180, PQ143, PQ134, and the Shenron-wish acquisition route. cite
- [x] Refreshed canonical/index last_verified to 2026-09-22.
- [x] Preserved the Burst Charge reward-condition conflict and Burning Shot evidence boundary; no unsupported probability or mandatory gate was inferred.
- [x] Added docs/data/skill-provenance-audit-2026-09-22-break-through-burst.json.
- [x] Static validation: 452/452, no duplicate IDs; affected records remain synchronized.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: recompute live census and continue after Burst Reflection.


### 2026-09-22 cycle update — Super Soul/equipment explorer record-navigation hardening
- [x] Recomputed the live reverse-navigation contract from the canonical relationship layer: **151 PQ→Super Soul edges / 148 unique Super Soul targets** and **124 PQ→equipment edges / 122 unique equipment/accessory targets**; existing forward/reverse pair parity remains clean.
- [x] Bounded consumer batch: docs/Super-Souls-All.html and docs/Equipment-All.html.
- [x] Repaired a deterministic one-way navigation gap: each rendered Super Soul/equipment record name now links directly to the local full-text Search/ surface using the canonical record name, and each card exposes an explicit “Open local wiki search” link.
- [x] Hardened scripts/validate_record_reverse_pq_navigation.py so the reverse-navigation audit requires record-level Search navigation in addition to canonical PQ pair parity, structured-field shape, duplicate detection, and query-parameter support.
- [x] Updated docs/data/record-reverse-pq-navigation-audit.json to schema 1.5.0 with the new record-search navigation contract; existing acquisition conflicts and noncanonical metadata remain explicitly preserved.
- [x] Validation by direct re-fetch: both explorers load their canonical local datasets and canonical relationship graph, retain ?q= initialization, render canonical PQ links, and now expose canonical-name Search links. No canonical relationship identity or acquisition fact was changed.
- [ ] Runtime/CI execution remains unavailable; no executable validation or CI success claimed.
- [x] Commits: equipment explorer 57e99208126679d75ce516d87674942fe4f850dd; Super Soul explorer 7ee86028bbeeb31fae4da5a69c915c60f490242a; validator 0560e25e6a48545878bdfcd6436de251e85aa18c; audit fb4dd2249ed37fa0da4d8562c7adcbfee31100ce.
- [ ] Exact next batch: return to the remaining P1 cross-domain acquisition projection gap, starting with the seven unresolved PQ41–186 Super Soul acquisition-index differences; recompute the live pair census first, then reconcile only source-backed missing pairs/variants while preserving the canonical relationship layer and unresolved spelling conflicts.


### 2026-09-22 cycle update — Burst Rush provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded record: `skill-burst-rush`.
- [x] Independent evidence: the dedicated Burst Rush reference identifies **Parallel Quest 51 — “Great Saiyaman is Here”** as the unlock; the maintained all-186-PQ Steam guide explicitly lists Burst Rush in PQ51's **Basic Reward**; an independent PQ51 gameplay record also lists Burst Rush as a Basic Reward. cite
- [x] Canonical/index provenance was refreshed to `last_verified: 2026-09-22`; the existing acquisition semantics were preserved. No skill identity, classification, acquisition endpoint, Ultimate Finish flag, or PQ relationship changed.
- [x] Evidence boundary preserved: Basic Reward evidence does not establish a drop probability; no Ultimate Finish-only gate was inferred.
- [x] Added `docs/data/skill-burst-rush-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452** records, **0 duplicate IDs**, and exact semantic parity across canonical/index for the affected acquisition fields, verification date, and reward-tier flag.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `c5c796f99e431e4860b6c51e06e4fe534adf8ad9`; index `447ed9657f552c0bdf2fdc92a9870d3ae7146e23`; audit `d66d5abdfd780450a8c3f12f8b5ea682ee82a869`; registry `e12cfe1cd4f9bc522903a676a532ac5cfc22e0b6`.
- [ ] Exact next batch: continue the stale-`last_verified` P1 skill provenance queue with **Burst Stinger (`skill-burst-stinger`)**, recomputing the live canonical/index census first and preserving any reward-tier conflicts or evidence boundaries.


### 2026-09-22 cycle update — Burst Stinger provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded record: `skill-burst-stinger`.
- [x] Independent evidence: dedicated Burst Stinger documentation identifies **PQ136 — “Breaking Down the Barrier”** as the unlock; the maintained all-186-PQ guide and independent PQ136 gameplay record list Burst Stinger among the Basic Rewards. cite
- [x] A separate GameFAQs acquisition report attributes the drop to Goku (Ultra Instinct) during the Ultimate Finish. This conflicts with the Basic Reward presentation, so the repository retains the existing Basic Reward semantics and records the trigger conflict rather than promoting an Ultimate Finish-only gate. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** without changing skill identity, classification, acquisition endpoint, or canonical PQ relationship.
- [x] Added `docs/data/skill-burst-stinger-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, and semantic parity across canonical/index for the affected acquisition fields and reward-tier flag.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `d40348757a9a22a04a688ecf51e8f3820d33c3b4`; index `39dda59cc12cb8b102b71e1a3161852fd6606c10`; audit `a889598d04e22c869573c80e33a14bbd945325c8`; registry `c5869e41261aa54fa74ca783d1ff9c73924df72c`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Buu Buu Ball (`skill-buu-buu-ball`)**, preserving any acquisition/reward-tier evidence conflicts.


### 2026-09-22 cycle update — Buu Buu Ball provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded record: `skill-buu-buu-ball`.
- [x] Independent evidence corroborates **PQ88 — “Evil Seeks Dragon Balls Yet Again!”** as the acquisition endpoint and lists Buu Buu Ball as a **Basic Reward**. Dedicated documentation also confirms its current Strike Evasive classification, 300 Stamina cost, and Majin CaC restriction. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22**; existing acquisition, reward-tier, race-restriction, and no-Ultimate-Finish-only semantics were preserved.
- [x] Added `docs/data/skill-buu-buu-ball-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, and semantic parity across canonical/index for affected acquisition fields and restriction metadata.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `97c2ca5cc981ee150f3ebcb212c9f6c32556de00`; index `704c607c464798568976727bc21d22b6d9333196`; audit `c91b72fbc312a136de8d04d4f92cf5c45b45ac73`; registry `0567c2e75b70889c7b8b2961492644331d41622e`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Candy Beam (`skill-candy-beam`)**, preserving any acquisition/reward-tier evidence conflicts.


### 2026-09-22 cycle update — Candy Beam provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 399 stale before editing**; bounded record: `skill-candy-beam`.
- [x] Independent evidence confirms PQ66 as a Candy Beam acquisition point and Basic Reward; the maintained all-186-PQ guide also lists Candy Beam as a Basic Reward at PQ113, preserving the existing `source_parallel_quests: [66,113]` relationship. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** while retaining the base-game PQ66 anchor and later PQ113 context.
- [x] Evidence boundary preserved: community Ultimate-Finish/RNG reports do not establish an Ultimate Finish-only gate or drop probability; a current reference also exposes an Evasive Candy Beam variant, so this provenance-only pass did not normalize class/mechanics semantics. cite
- [x] Added `docs/data/skill-candy-beam-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, **398 stale remaining**, and exact semantic parity across canonical/index for affected fields.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `21b7a550b517d519037317c211df01c33bacd06c`; index `b79993d3bb7cab31ec14773f6027d18264b5dcad`; audit `f977369ca49663a9ecbe944c0659c57d9f7c7140`; registry `588dd96cd9b3b6a5ef181744932d7215f7e890bf`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Candy Beam (Super) (`skill-candy-beam-super`)**, preserving its PQ113/Extra Pack 1 reward evidence and any trigger conflicts.


### 2026-09-22 cycle update — Candy Beam (Super) provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 398 stale before editing**; bounded record: `skill-candy-beam-super`.
- [x] Independent evidence confirms Candy Beam (Super) as a **200-Ki Ki Blast Super** and identifies **PQ113** as its acquisition endpoint; the maintained all-186-PQ guide explicitly lists Candy Beam in PQ113 Basic Rewards, while an independent GameFAQs PQ113 summary also lists it among the rewards. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22**; existing Extra Pack 1, PQ113, all-CaC-races, and no-Ultimate-Finish-only semantics were preserved.
- [x] Evidence boundary preserved: reward listings establish availability but do not establish a drop probability or mandatory Ultimate Finish gate.
- [x] Added `docs/data/skill-candy-beam-super-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, **397 stale remaining**, and exact semantic parity across canonical/index for the projected/affected fields. The index intentionally omits some canonical-only descriptive fields; those were not treated as projection mismatches.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `50fef71f04288032a268e94b749aba5485300535`; index `f877a9cc5f90cf04f5747bed87df307da2470114`; audit `c985d27efdb625a343fa7f429e02379c251477e8`; registry `79db691a8a514fc5166528b35c9dd67eabf39586`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with the next stale record after `skill-candy-beam-super`, preserving acquisition conflicts and projection semantics.


### 2026-09-22 cycle update — Change The Future provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs / 396 stale before this edit**; bounded record: `skill-change-the-future`.
- [x] Independent evidence confirms **Change The Future** as a **100-Ki Ki Blast Super / counter skill** and identifies **Parallel Quest 43 — “Change the Future”** as the acquisition endpoint. The maintained all-186-PQ Steam guide independently lists it in PQ43 **Basic Reward**. A GameFAQs discussion is retained as supporting context for the Ki-counter behavior and known in-game wording issue.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and added the dedicated skill reference plus maintained Steam PQ guide to the canonical/index provenance sources.
- [x] Preserved the existing acquisition, classification, All-CaC-races, counter semantics, and no-Ultimate-Finish-only meaning. No drop probability or new gate was inferred.
- [x] Added `docs/data/skill-change-the-future-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation: **452/452** records, **0 duplicate IDs**, **396 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `bae7a84dab5ae8811991e75043215cd591cd0648`; index `21ef1ec45c1d9acad71acf05e1a4c2815e653b4f`; audit `08744a4c23e7d2495a59ef1923bbc04a2c81b9ae`; registry `4fc242bdfce5745dcb1f40ea637bff59ca558367`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Chaos Shot (`skill-chaos-shot`)**, preserving its Free Update 1 / TP Medal Shop provenance and historical source-mapping uncertainty.


### 2026-09-22 cycle update — Chaos Shot provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs / 396 stale before this edit**; bounded record: `skill-chaos-shot`.
- [x] Independent evidence confirms **Chaos Shot** as a **100-Ki Ki Blast Super** used by Frost and acquired from the **TP Medal Shop**. Official Bandai Namco documentation also confirms TP Medals remain earnable and usable in-game after the May 2024 sales transition. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and added the dedicated skill reference plus official TP Medal transition notice to provenance sources.
- [x] Preserved the existing Free Update 1 historical mapping uncertainty: the official announcement does not individually enumerate Chaos Shot, so no stronger direct attribution was invented.
- [x] Added `docs/data/skill-chaos-shot-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation: **452/452** records, **0 duplicate IDs**, **395 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `de6d89f4b1e2e322a54391c66b9e2bf6b626ca80`; index `424389a50af159562f6c5831f497e0476ea87b47`; audit `df4ffc97825c0d80e7a74523ba0ea4bd5e308a6c`; registry `7d33bc566155f3ca39ff43036015a0013b665c6e`.
- [ ] Exact next batch: recompute the live census and continue with the next stale P1 skill provenance record after `skill-chaos-shot`.


### 2026-09-22 cycle update — Atomic Blast provenance reconciliation
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs / 395 stale before this edit**; bounded record: `skill-atomic-blast`.
- [x] Dedicated skill documentation confirms **Atomic Blast** as a **100-Ki Ki Blast Super** with PQ87 as the unlock source. The maintained all-186-PQ guide lists Atomic Blast in PQ87 **Basic Reward**.
- [x] A contemporaneous 2017 gameplay guide claims Ultimate Finish completion and a random drop were required. This is preserved as a historical source conflict rather than converted into a new Ultimate Finish requirement or drop probability.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and preserved the repository's documented Basic Reward classification while recording the conflict in `docs/data/skill-atomic-blast-provenance-audit-2026-09-22.json`.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation: **452/452** records, **0 duplicate IDs**, **394 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `231b459853291b308f34413e390bf11aa1752a5e`; index `6dbfe34b5664e5ad39e37b7bf33bc2db5f812fd7`; audit `67c7f8043349936cd9e5618d2ca6aefafeea5660`; registry `03f46a5854686a32a30145b998d11a27866c71ad`.
- [ ] Exact next batch: recompute the live census and continue with `skill-bending-kamehameha`.


### 2026-09-22 cycle update — Bending Kamehameha provenance verification
- [x] Fresh live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 394 stale**; target `skill-bending-kamehameha`.
- [x] Dedicated skill documentation confirms Bending Kamehameha as a **100-Ki Ki Blast Super** acquired from the **Skill Shop**, with tracking/additional-input behavior.
- [x] Independent GameFAQs evidence corroborates Skill Shop acquisition. Existing completion-gate wording was retained because the evidence does not establish a more precise shop threshold.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and added provenance sources/notes.
- [x] Added and registered `docs/data/skill-bending-kamehameha-provenance-audit-2026-09-22.json`.
- [x] Static validation: **452/452**, **0 duplicate IDs**, **393 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable.
- [x] Commits: canonical `6f8b0e76bf06681bfe730b55aac97b14b34bb3de`; index `dd0556e30bb71ab6baa980ae3c3a210f31a6efa5`; audit `f4f8cd90409808377f334ed3b77e5e907630136d`; registry `4a7e21d0c30bd7ae75b99d0369fb28813b067cce`.
- [ ] Exact next batch: recompute the live census and continue with `skill-big-bang-kamehameha`.


### 2026-09-22 cycle update — Big Bang Kamehameha provenance verification
- [x] Fresh live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 393 stale**; target `skill-big-bang-kamehameha`.
- [x] Dedicated skill documentation confirms Big Bang Kamehameha as a **100-Ki Ki Blast Super** acquired from the **TP Medal Shop**, with chargeable beam behavior, 9–15 hits, knockback, and the documented Super Saiyan warp interaction.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and preserved the existing TP Medal Shop acquisition without adding an unsupported shop rotation/date claim.
- [x] Added and registered `docs/data/skill-big-bang-kamehameha-provenance-audit-2026-09-22.json`.
- [x] Static validation: **452/452**, **0 duplicate IDs**, **392 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable.
- [x] Commits: canonical `2f1aa3dd5dd523226768825ffa14b68eb3212a15`; index `9d2433d3c0211d9c73ce66f364186b1fdd8f5fa3`; audit `6f1384ddadf67b9c861e8c632515b0d42949e728`; registry `acd3bd16c807c359cc5ee0f079d9681e976de58f`.
- [ ] Exact next batch: recompute the live census and continue with `skill-blaster-ball`.


### 2026-09-22 cycle update — Blaster Ball provenance verification
- [x] Fresh live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 392 stale**; target `skill-blaster-ball`.
- [x] Dedicated skill documentation confirms Blaster Ball as a **100–500-Ki Ki Blast Super** used by Kefla (Super Saiyan), acquired from **PQ125 — “Proof's in the Potara”**, with repeatable long-range projectile behavior, 2–13 hits, and knockback.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and retained the existing PQ125 Basic Reward acquisition.
- [x] Added and registered `docs/data/skill-blaster-ball-provenance-audit-2026-09-22.json`.
- [x] Static validation: **452/452**, **0 duplicate IDs**, **391 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable.
- [x] Commits: canonical `1e50889fea89027eaca0f3739a21cfa39a29f778`; index `cfa120a20fb92164a31cef241b2e39959e2975c6`; audit `4392aff7f67fb7b5558c355911cfe9b41818bcb4`; registry `44c0f5a37584f336518986145fd56f90392858da`.
- [ ] Exact next batch: recompute the live census and continue with `skill-bluff-kamehameha`.


### 2026-09-22 cycle update — Bluff Kamehameha provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs / 391 stale before edit**; bounded record: `skill-bluff-kamehameha`.
- [x] Independent evidence confirms **Bluff Kamehameha** as a **100-Ki Super** with **PQ94 — “Ultimate Power, Ultimate Saiyan”** acquisition; the maintained PQ reward guide lists Bluff Kamehameha in PQ94 rewards. Dedicated Xenoverse 2 documentation presents it under **Other Supers** and describes its chargeable Ki-drain behavior. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and added current dedicated provenance sources.
- [x] Preserved the existing canonical **Ki Blast** classification, All-CaC-races restriction, PQ94 Basic Reward semantics, and no-Ultimate-Finish-only meaning. The current Other-category presentation is recorded as a taxonomy/source conflict rather than silently normalized in a provenance-only pass.
- [x] Evidence boundary preserved: reward listings establish availability but do not establish an individual drop probability; character/source presentation differences were not promoted into a new identity assertion.
- [x] Added `docs/data/skill-bluff-kamehameha-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452** records, **0 duplicate IDs**, **390 stale remaining**, affected canonical/index semantic parity preserved.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `311c6952c780c4830b541e443156d6df10a2c2b1` / source cleanup `172e38cc0e2771ee73482e9c8f79da327835b2af`; index `4b5e1752e7ff7000998084e50e3d53b1e459728f` / source cleanup `117913c1ba1d0d714716c7269a618b7a25a0ea7f`; audit `3455db649a20464cb17f577dab8a6c24b94ab6d5`; registry `b9b471aa4bfe59f149bc4f972d3bb7aeac1e59c0`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Breaker Energy Wave (`skill-breaker-energy-wave`)**, preserving acquisition conflicts and projection semantics.


### 2026-09-22 cycle update — Breaker Energy Wave provenance reconciliation
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 390 stale**; bounded target: `skill-breaker-energy-wave`.
- [x] Corrected a substantive stale-record mismatch: dedicated Xenoverse 2 evidence identifies Breaker Energy Wave as a **Ki Blast Ultimate used by Goku**, with **0 Ki**, rather than the prior Super/Hit/100-Ki projection. It is available to CaCs and is tied to PQ101. cite
- [x] Preserved PQ101 acquisition semantics. The maintained all-PQ guide explicitly lists Breaker Energy Wave as a **Basic Reward**; historical GameFAQs/Steam player reports associate successful acquisition with Ultimate Finish completion, but they do not establish a formal reward-tier rule or numeric drop rate. cite
- [x] Corrected canonical/index fields: class, character source, Ki cost, skill description, mechanics notes, sources, and `last_verified`; retained CaC availability, PQ101 endpoint, Super Pack 1 mapping, and Basic Reward semantics.
- [x] Added `docs/data/skill-breaker-energy-wave-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation after writes: **452/452**, **0 duplicate IDs**, **389 stale remaining**, all affected canonical/index semantic fields aligned.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `5b61b4eb782fec2dc5ad8c420c89db73381d70b8`; index `d9d8abfb764d3f03c814347a3896d3bf0273dccd`; audit `048a300608adfbd854464e782d49ca4cf04f4778`; registry `0be8682b70fbc23184876c443e132c7be36b6b05`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with the next stale record after `skill-breaker-energy-wave`, preserving conflicts and projection semantics.


### 2026-09-22 cycle update — Burning Attack provenance verification
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 389 stale**; bounded target: `skill-burning-attack`.
- [x] Dedicated Xenoverse 2 documentation confirms Burning Attack as a **100-Ki Ki Blast Super** associated with **Future Trunks**, with projectile/explosive 2-hit launching behavior and PQ41 acquisition. Independent PQ41 reward guides place it in the **Basic Reward** pool. cite
- [x] Refreshed canonical/index `last_verified` to **2026-09-22**, refreshed mechanics/provenance notes and sources, and preserved the existing PQ41 Basic Reward / no-Ultimate-Finish-only semantics.
- [x] Corrected an index projection mismatch discovered during validation: `character_source`, `ki_cost`, and `damage_type` were aligned with the canonical record.
- [x] Added and registered `docs/data/skill-burning-attack-provenance-audit-2026-09-22.json`.
- [x] Final static validation: **452/452**, **0 duplicate IDs**, **388 stale remaining**, affected canonical/index fields now semantically aligned.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `1b2d995822bc013f9d23d9791eb18adc0385ea7c`; index `f57b693c3fc17f078dfcb180001617b42fa2c135` + projection fix `d1f59d6949cf8ab5b5f8d51079e0f0e9d94e68ef`; audit `473970513eebc7750cde8ed167567ae2139c7245` + validation `2dad25a7ac384d22a304ef2a5a4dac43ca74daf6`; registry `be0f618601192493cfc4e0ef17cc8709e27782b1`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burning-attack`.


### 2026-09-22 cycle update — Burning Slash provenance verification
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 388 stale**; bounded target: `skill-burning-slash`.
- [x] Dedicated Xenoverse 2 documentation confirms Burning Slash as a **100-Ki Strike Super** used by Trunks, with a **5-hit sword sequence and optional follow-up Ki Blast (5–9 hits)**, Human/Saiyan CaC restriction, and PQ44 acquisition. Independent PQ44 documentation explicitly lists it as a **Basic Reward**. cite
- [x] Refreshed canonical/index `last_verified`, mechanics/provenance notes, and sources while preserving PQ44 Basic Reward semantics and no-Ultimate-Finish-only assertion.
- [x] Added and registered `docs/data/skill-burning-slash-provenance-audit-2026-09-22.json`.
- [x] Validation: **452/452**, **0 duplicate IDs**, **387 stale remaining**; checked shared semantic/index projection fields remain aligned. Fields intentionally absent from the index projection were not treated as mismatches.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `b5a95413109bd7010da0492192264cfc93703bda`; index `62485d33f4059af1c09c0b6eb8cf0c54b312f595`; audit `90734db5844f127df01cd4fe9e75cce349d1bcef` + validation update; registry `4bdd6135faba649ef5fc309f21d1218a805fcd0e`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burning-slash`.


### 2026-09-22 cycle update — Burning Swan provenance reconciliation
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 387 stale**; bounded target: `skill-burning-swan`.
- [x] Official Dragon Ball documentation confirms Burning Swan as Videl's Super Attack and describes its slow-moving, chargeable Ki Blast behavior. Dedicated Xenoverse 2 documentation ties it to PQ167; the maintained PQ167 guide explicitly lists it as a **Basic Reward**. cite
- [x] Refreshed canonical/index provenance, mechanics notes, source set, and `last_verified`; preserved the existing PQ167 Basic Reward and non-Ultimate-Finish-only semantics. A separate reference describes a random PQ167 drop, but no numeric probability is asserted.
- [x] Validation exposed and fixed an index projection mismatch in `ki_cost`; canonical/index shared semantic fields are now aligned.
- [x] Added and registered `docs/data/skill-burning-swan-provenance-audit-2026-09-22.json`.
- [x] Final static validation: **452/452**, **0 duplicate IDs**, **386 stale remaining**, affected semantic parity true.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `dee4dc1ff461dd80cbf73ac298f3d0c742570a99`; index `33f64df7aa6b05c5605f354cb6cbb705eb5f69b0` + projection fix `db889513dd6aed7340db654b23e0e3d3f5ced9da`; audit `f21969f8f88dafe4b494bd07cf151414c2ae2343` + validation `51ba23974c0006741041606b01d217052c2e92f0`; registry `60c1b29c0e395ed8d438b80d45df92dfc6ce2545`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burning-swan`.


### 2026-09-22 cycle update — Burst Blitz provenance reconciliation
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 386 stale**; bounded target: `skill-burst-blitz`.
- [x] Dedicated Xenoverse 2 documentation identifies Burst Blitz as a **300-Ki Strike Ultimate** used by **Goku (Mini)**, with a 5-hit Power Pole rush/kick sequence and PQ178 acquisition. The maintained PQ178 guide lists it under **Basic Reward**. cite
- [x] Corrected a substantive stale-record mismatch: canonical/index classification changed from **Super** to **Ultimate**, and identity/description/mechanics/provenance were refreshed.
- [x] Preserved the existing Ultimate Finish/50% projection only as conflict context because the current PQ reward guide presents Burst Blitz as a Basic Reward; no new numeric probability was asserted.
- [x] Added and registered `docs/data/skill-burst-blitz-provenance-audit-2026-09-22.json`.
- [x] Final static validation: **452/452**, **0 duplicate IDs**, **385 stale remaining**, affected shared semantic fields aligned.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `7c0bcf116c30252309c2299b110e8d973ab78b76`; index `3fd978670c956b46aabbf4da9586242e5d18a186`; audit `77a18557d1840af90c3e38f55361fa6f636e8cc9` + validation update; registry `7896a071ebff7b882ea82f93f68c268c4692ac48`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burst-blitz`.


### 2026-09-22 cycle update — Burst/Celestial/Chain/Chaos skill provenance batch
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 385 stale**; bounded batch: `skill-burst-kamehameha`, `skill-celestial-wave`, `skill-chain-destructo-disc-barrage`, `skill-chaos-wall`.
- Research/evidence: independent Xenoverse 2 skill documentation and maintained PQ evidence reconfirmed Burst Kamehameha at PQ72; Celestial Wave at PQ151 with an explicit Basic-vs-Ultimate-Finish source conflict preserved; Chain Destructo-Disc Barrage at PQ46; and Chaos Wall in Conton City Tournament Match 4 / Free Update 11 context. Official Bandai Namco update documentation was used for Chaos Wall's update provenance.
- Changes: refreshed canonical/index `last_verified` to **2026-09-22** for all four records; synchronized provenance notes; added four dedicated provenance audits under `docs/data/`; registered all four audits in `docs/data/pq-cross-domain-index.json`.
- Evidence limits/conflicts preserved: no unsupported drop probabilities or new exclusive gates were inferred; Celestial Wave's existing reward-tier conflict remains explicit; Chain Destructo-Disc Barrage historical Ultimate-Finish/RNG reports were not promoted into a formal gate; Chaos Wall's dedicated Match 4 endpoint remains the acquisition evidence because the official update notice does not provide a Match 4 reward table.
- Validation: canonical/index both **452** records; **0 duplicate canonical IDs**; **381 stale canonical records remain**; all four bounded records have `last_verified: 2026-09-22`; audited shared canonical/index fields have **0 mismatches** after note synchronization; JSON parses successfully; four audit registrations resolve to created files.
- CI: no successful workflow/check exposed for this direct repository chain; no CI success claimed.
- Commits: Burst canonical `f37d90ed2672d6bd4adc8c088a2faa08f8e69161`, Burst index `085724082d6ce8a1dbc324a0e37a3764c49ac576`, Celestial canonical `c0d79008b46371a8e9fb02b60a8203f0954606b3` + normalization `efad72ee914b177b68ed5f6d8ac5ed7900560e02`, Celestial index `4b991d8145de42847694b3ae69307d5abbdfa148`, Chain canonical `10c63d93860e3d506b0841edceeaa16f464c6c82`, Chain index `8b0dd31bb9738cda714b281176a239a4d2a41d58`, Chaos canonical `c94d4899807c1d1ab47688d219ec8464571ff472`, Chaos index `201653786e54d203f077da5bd3fb70349ceee221`, audits `0bef18564318b5bd5da974dee40687983730cfc3`, `b3dd4183bfbf895af669fdb344545c823c802bd4`, `402ffbb87b3910513e21b8cf0ba7201fda9a3c5a`, `6f8500b45ab49f037b7c5303f83393f08e4f73f2`, registry `2904c1a1f105a6ef3e0d5bf318f70b8bebe0de55`.
- Exact next batch: recompute the live census and continue the stale P1 skill provenance queue with **`skill-chaotic-time-impact`**, preserving acquisition conflicts and projection semantics; then proceed alphabetically through the next bounded stale records.


### 2026-09-22 cycle update — Chaotic Time Impact provenance refresh
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 381 stale**; bounded target: `skill-chaotic-time-impact`.
- Research/evidence: dedicated Xenoverse 2 skill documentation confirms the Ultimate/Ki Blast classification, 600 Ki cost, time-bubble stun, and Power-of-Time scaling/reset. Current PQ184 research identifies Chaotic Time Impact as a **50% Ultimate Finish bonus-slot** reward; the maintained Steam guide still presents it in the Basic Reward section, so the source conflict is explicitly preserved rather than silently erased.
- Changes: refreshed canonical/index `last_verified` to **2026-09-22**; added independent gameplay provenance; added and registered `docs/data/skill-chaotic-time-impact-provenance-audit-2026-09-22.json`.
- Evidence limits/conflicts preserved: no narrower CaC race/gender/form restriction was inferred; `race_restriction` remains null. No new drop probability was inferred beyond the current PQ research's documented 50% bonus-slot value.
- Validation: **452/452** canonical/index; **0 duplicate IDs**; **380 stale canonical records remain**; target refreshed; all audited shared fields have **0 mismatches**; JSON parses successfully.
- CI: no successful workflow/check exposed; no CI success claimed.
- Exact next batch: recompute the live census and continue with the next stale P1 record after `skill-chaotic-time-impact`, beginning `skill-charge` and batching adjacent stale records where evidence and validation remain bounded.


### 2026-09-22 cycle update — Charge-through-Counter skill provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 380 stale**; bounded batch: `skill-charge`, `skill-charged-ki-wave`, `skill-circle-flash`, `skill-comet-strike`, `skill-confusion-blade`, `skill-core-breaker`, `skill-counter-burst`.
- [x] Research/evidence: dedicated Xenoverse 2 skill pages and maintained PQ evidence reconfirmed PQ83 Charge, PQ97 Charged Ki Wave, PQ154 Circle Flash, PQ149 Comet Strike, Tokipedia Confusion Blade, PQ158 Core Breaker, and PQ75 Counter Burst. Reward conflicts were preserved where sources disagree (Circle Flash Basic-vs-40% UF; Charged Ki Wave older UF report vs maintained Basic table).
- [x] Changes: refreshed canonical/index `last_verified` to **2026-09-22** for all seven records; added current provenance sources; corrected Core Breaker's race restriction to unresolved/null because its current evidence does not establish a narrower CaC scope; added and registered seven dedicated provenance audits.
- [x] Evidence limits preserved: no unsupported drop probability or new UF gate was inferred; Charge's Goku/Goten source-character presentation conflict remains uncollapsed; source reward-table conflicts remain explicit.
- [x] Static validation on branch: **452/452** canonical/index; **0 duplicate canonical IDs**; **373 stale canonical records remain**; all seven targets refreshed; audited shared canonical/index fields have **0 mismatches**; all seven audit registrations resolve.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live census after merge and continue the next stale P1 skill provenance records alphabetically, beginning with the first stale record after `skill-counter-burst`.


### 2026-09-22 cycle update — Counter Impact through Crusher Ball provenance batch
- [x] Fresh branch validation before handoff: **452 canonical / 452 index / 0 duplicate IDs / 366 stale**.
- [x] Bounded batch completed: `skill-counter-impact`, `skill-crazy-finger-shot`, `skill-crimson-edge`, `skill-critical-upper`, `skill-crush-cannon`, `skill-crush-stream`, `skill-crusher-ball`.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22**, reconciled current dedicated skill evidence, and preserved existing reward/gate uncertainty rather than inventing probabilities.
- [x] Added and registered seven dedicated provenance audits under `docs/data/`.
- [x] Counter Impact: current evidence reconfirms 100-Ki Ki Blast Super/PQ153 and counter/warp/Ki-Wave mechanics. Crazy Finger Shot: PQ26/100-Ki Ki Blast Super retained. Crimson Edge: PQ171/100-Ki Strike Super and scythe-spin deflection mechanics reconfirmed; existing reward-condition conflict retained. Critical Upper: Dodoria training/100-Ki Strike Super/launching uppercut reconfirmed. Crush Cannon: PQ147/100-Ki Ki Blast Super/charge-and-guard mechanics reconfirmed. Crush Stream: PQ147/300-Ki Ki Blast Ultimate/two-projectile follow-up reconfirmed. Crusher Ball: PQ34/100-Ki Ki Blast Super/tracking six-hit behavior reconfirmed.
- [x] Static validation: **452/452**, **0 duplicate canonical IDs**, **366 stale canonical records remain**, all seven targets refreshed, audited shared canonical/index fields **0 mismatches**, and all seven audit registrations resolve.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live census after merge and continue the stale P1 skill provenance queue alphabetically with **`skill-dancing-parapara`**, then adjacent stale records where evidence and validation remain bounded.


## 2026-09-22 — Dancing-through-Darkness provenance batch
- Refreshed six adjacent stale P1 skill records: Dancing Parapara, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), and Darkness Twin Star.
- Added six provenance audits and registered them in pq-cross-domain-index.json.
- Corrected Darkness Rush (Melee) race scope to all CaC races except Namekian, matching direct skill evidence; retained Darkness Rush (Ranged) as Namekian-only.
- Rechecked mentor/PQ acquisition evidence and preserved existing acquisition semantics where no direct contradiction was established.
- Validation target: six records set to 2026-09-22; canonical/index parity and audit registration to be verified before merge. CI success is not claimed.
- Next target: recompute live stale census and continue with the next stale records beginning Data Input / Dead End Rain / Deadly Dance, batching adjacent skills where evidence remains bounded.
\n### 2026-09-22 cycle update — Data Input through Death Slicer provenance batch
- [x] Refresh stale P1 provenance for Data Input, Dead End Rain, Deadly Dance, Death Ball, Death Beam, Death Crasher, Death Psycho Bomb, Death Slash, and Death Slicer.
- [x] Synchronize canonical `docs/data/skills.json` and presentation `docs/data/skills-index.json`; all 9 target records now use `last_verified: 2026-09-22`.
- [x] Correct Death Slash's canonical classification from Strike to Ki Blast where current dedicated evidence deterministically resolves the mismatch.
- [x] Add/register dedicated provenance audits where the repository write path permitted them; preserve unresolved audit-file coverage rather than fabricating records.
- [x] Static validation: **452 canonical / 452 index / 0 duplicate IDs / 351 stale remaining** after this batch.
- [ ] CI/runtime execution remains unavailable; do not claim CI success.
- [ ] Next exact batch: **Demon Flash Strike** and adjacent stale P1 skill records, continuing alphabetically and preserving evidence conflicts.\n

### 2026-09-22 cycle update — Demon Flash Strike through Destructive Flare provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 351 stale**.
- [x] Bounded batch completed for **Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Destruction's Concerto: Meteor, Destruction's Concerto: Starfall, Destruction's Conductor, Destructive Fission, and Destructive Flare**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records.
- [x] Expanded mechanics using current dedicated Xenoverse 2 evidence: Demon Flash Strike counter/teleport follow-up; Demon Flurry timed six-hit extension; Demon Ray follow-up Ki Wave and 300-Stamina hit-through behavior; Demonic Destruction grab/slam and weak-Ki-Blast cancellation; the three Destruction's Concerto projectile variants and their Destruction's Conductor interactions.
- [x] Preserved existing acquisition/reward semantics and did not invent drop probabilities or Ultimate-Finish gates. DLC/PQ provenance remains explicit.
- [x] Static validation after editing: **452/452** canonical/index; **0 duplicate canonical IDs**; **341 stale canonical records remain**; all ten targets have `last_verified: 2026-09-22`; shared canonical/index fields (`name`, `class`, `subcategory`, `last_verified`) have **0 mismatches**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically after Destructive Flare with **Destructive Fracture, Destructo-Disc**, and adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Destructive Fracture through Divine Kamehameha provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 341 stale**.
- [x] Bounded batch completed for **Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole, and Divine Kamehameha**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all seven records and expanded bounded mechanics/provenance notes.
- [x] Preserved deterministic corrections already established: Dimension Cannon remains a **300-Stamina Ki Blast Evasive**, not a Ki-cost Super; Dimension Ray remains **400 Ki**; Divine Kamehameha retains its **Free Update 11** provenance separately from TP Medal Shop acquisition.
- [x] No unsupported drop probability, Ultimate-Finish gate, or positive Ki cost was invented. DIE DIE Missile Barrage mechanics remain explicitly deferred because current mentor evidence establishes acquisition but not enough mechanics detail.
- [x] Static validation after editing: **452/452** canonical/index; **0 duplicate canonical IDs**; **334 stale canonical records remain**; all seven targets have `last_verified: 2026-09-22`; shared `name`, `class`, `subcategory`, and `last_verified` fields have **0 mismatches**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Divine Lasso, Divine Ray Bomb, Divine Spear, Divine Wrath: Purification, Divinity Unleashed, Do or Die, Dodon Ray**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Divine Lasso through Dodoria Launcher provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 334 stale**.
- [x] Bounded batch completed for **Divine Lasso, Divine Ray Bomb, Divine Spear, Divine Wrath: Purification, Divinity Unleashed, Do or Die, Dodon Ray, Dodoria Beam, Dodoria Headbutt, and Dodoria Launcher**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records and refreshed bounded mechanics/provenance notes.
- [x] Preserved evidence boundaries: Divine Lasso remains canonically classified as a Strike Ultimate despite conflicting historical community damage-scaling reports; Divine Ray Bomb retains its PQ173 Ultimate-Finish 45% route; Divine Spear retains its documented 50% Ultimate-Finish route and existing CaC correction; unresolved drop probabilities remain unresolved.
- [x] Mentor endpoints for Dodon Ray and the three Dodoria skills remain explicit; detailed combat mechanics stay deferred where current evidence is acquisition-focused.
- [x] Static validation after editing: **452/452** canonical/index; **0 duplicate canonical IDs**; **324 stale canonical records remain**; all ten targets have `last_verified: 2026-09-22`; shared `name`, `class`, `subcategory`, and `last_verified` fields have **0 mismatches**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Double Crush, Double Death Slicer, Double Sunday, Dragon Blitz, Dragon Burn, Dragon Fist, Dragon Spark, Dragon Spiral**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Double Crush through Dragon Spiral provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 324 stale**.
- [x] Bounded batch completed for **Double Crush, Double Death Slicer, Double Sunday, Dragon Blitz, Dragon Burn, Dragon Fist, Dragon Spark, and Dragon Spiral**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all eight records and refreshed bounded mechanics/provenance notes.
- [x] Preserved documented evidence boundaries: Double Crush remains PQ147/Legendary Pack 2; Dragon Burn remains a 200-Stamina Evasive; Dragon Spark retains its explicit PQ177 Ultimate-Finish route and conflicting reward-list context; Dragon Spiral retains the explicit PQ185 route over older alternate PQ186 references.
- [x] No unsupported drop probability, reward gate, or CaC restriction was invented; historical gameplay observations are kept distinct from canonical numeric fields.
- [x] Static validation after editing: **452/452** canonical/index; **0 duplicate canonical IDs**; **316 stale canonical records remain**; all eight targets have `last_verified: 2026-09-22`; shared `name`, `class`, `subcategory`, and `last_verified` fields have **0 mismatches**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Dragon Thunder, Drain Field, Dual Destructo-Disc, Dust Attack**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Dragon Thunder through Elegant Blaster provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 316 stale**.
- [x] Bounded batch completed for **Dragon Thunder, Drain Field, Dual Destructo-Disc, Dust Attack, Dynamite Kick, Eagle Kick, Earth Splitting Galick Gun, and Elegant Blaster**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all eight records and refreshed bounded mechanics/provenance notes.
- [x] Preserved the important evidence boundaries: Dragon Thunder remains character-only/unclear for CaC; Drain Field retains its acquisition-condition conflict; Earth Splitting Galick Gun retains conflicting reward-list evidence rather than inventing certainty; mentor mechanics remain deferred where acquisition evidence is stronger.
- [x] Static validation after editing: **452/452** canonical/index; **0 duplicate canonical IDs**; **308 stale canonical records remain**; all eight targets refreshed; shared `name`, `class`, `subcategory`, and `last_verified` fields have **0 mismatches**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Elite Beam, Elite Shooting, Emperor's Blast, Emperor's Cannon**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Energy Field through Evil Flight Strike provenance batch
- [x] Fresh live census: **452 canonical / 452 index / 0 duplicate canonical IDs / 298 stale**.
- [x] Completed the bounded P1 provenance batch for **Energy Field, Energy Minefield, Energy Release, Energy Shot, Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, and Evil Flight Strike**.
- [x] Refreshed canonical/index last_verified to **2026-09-22** for all ten records and added/registered docs/data/skill-energy-through-evil-provenance-audit-2026-09-22.json.
- [x] Deterministic correction: **Energy Minefield** acquisition corrected from **60% to 75% Tokipedia completion**, supported by independent Tokipedia reward evidence.
- [x] Preserved acquisition conflicts and evidence limits for Eraser Bomb and Evil Flame; no unsupported drop probabilities, gates, or narrower restrictions were inferred.
- [x] Static validation passed: **452/452**, **0 duplicate IDs**, **10/10** audit records, **0 audited canonical/index mismatches**, **288 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Evil Ray Strike through Fake Death provenance batch
- [x] Fresh live census: **452 canonical / 452 index / 0 duplicate canonical IDs / 288 stale**.
- [x] Completed the bounded P1 provenance batch for **Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault, Explosive Buu Buu Punch, Explosive Wave, Eye Beam, Fake Blast, and Fake Death**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records and added/registered docs/data/skill-evil-through-fake-provenance-audit-2026-09-22.json.
- [x] Expanded bounded mechanics/provenance from current dedicated skill evidence: guard-break behavior for Evil Ray Strike; rising/knockback behavior for Evil Rise Strike; blocking-capable spin kick for Evil Whirlwind; six-charge/final-blast structure for Excellent Full Course; barrage/exhaustion behavior for Explosive Assault; nine-hit Super Armor barrage for Explosive Buu Buu Punch; 300-Stamina Skill Shop route for Explosive Wave; controllable three-shot Eye Beam; 200-Stamina blinding Fake Blast; and invulnerability/deceptive-counter behavior for Fake Death.
- [x] Preserved the **Excellent Full Course** acquisition conflict: current sources disagree between PQ142 Basic Reward presentation and an Ultimate-Finish/60%-health condition; no unsupported gate was forced into the canonical record.
- [x] Static validation passed: **452/452**, **0 duplicate IDs**, **10/10** audit records, **0 audited canonical/index mismatches**, **278 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Feint Crash, Feint Shot, Fierce Fist, Fighting Pose A, Fighting Pose C, Fighting Pose E, Fighting Pose F, Fighting Pose H, Fighting Pose K, Final Cannon**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Feint Crash through Final Cannon provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate canonical IDs / 278 stale**.
- [x] Completed the bounded P1 provenance batch for **Feint Crash, Feint Shot, Fierce Fist, Fighting Pose A, Fighting Pose C, Fighting Pose E, Fighting Pose F, Fighting Pose H, Fighting Pose K, and Final Cannon**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records and added/registered docs/data/skill-feint-through-final-cannon-provenance-audit-2026-09-22.json.
- [x] Expanded bounded mechanics/provenance from current dedicated evidence: Feint Crash teleport/restand and alternate knockback input; Feint Shot teleport/feint firing behavior; Fierce Fist three-stage charge and Stage-3 unblockable behavior; Fighting Pose A auto-guard; Fighting Pose C abnormal-status cleansing/immunity; Fighting Pose E Basic Attack buff; Fighting Pose F Hyper Armor and Stamina-regeneration penalty; Fighting Pose H damage reduction; Fighting Pose K 8-second Super Armor; and Final Cannon six-hit launching rush.
- [x] Preserved evidence boundaries: Fierce Fist remains tied to its documented Ultimate Finish bonus pool; Final Cannon's individual reward probability remains unresolved; no unsupported drop rates or additional gates were invented.
- [x] Static validation passed: **452/452**, **0 duplicate IDs**, **10/10** audit records, **0 audited canonical/index mismatches**, **268 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Final Charge, Final Explosion, Final Flash, Final Flash (SS3 DAIMA), Final Flash (Super), Final Kamehameha, Final Pose, Final Rampage, Finish Breaker, Finishing Blow**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Final Charge through Finishing Blow provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate canonical IDs / 268 stale**.
- [x] Completed the bounded P1 provenance batch for **Final Charge, Final Explosion, Final Flash, Final Flash (SS3 DAIMA), Final Flash (Super), Final Kamehameha, Final Pose, Final Rampage, Finish Breaker, and Finishing Blow**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records and added/registered docs/data/skill-final-through-finishing-provenance-audit-2026-09-22.json.
- [x] Deterministic correction: **Final Explosion ki_cost corrected from 500 to 300** based on current dedicated skill evidence; TP Medal Shop acquisition at 200 TP Medals remains documented.
- [x] Expanded bounded mechanics/provenance: Final Charge accelerated Ki charging; Final Explosion extended Stamina-based explosion; Final Flash mentor Lesson 3 beam; Final Flash (SS3 DAIMA) 400+ Ki/22–53-hit expandable beam; Final Flash (Super) 24-hit character-exclusive beam; Final Kamehameha 22-hit Final Flash→Super Kamehameha sequence; Final Pose shockwave/Basic Attack boost; Final Rampage multi-stage rush sequence; Finish Breaker 19-projectile barrage; Finishing Blow teleport/restand follow-up behavior.
- [x] Preserved the **Final Pose** acquisition conflict: current dedicated skill evidence lists Skill Shop while maintained PQ evidence maps the established cross-link to PQ74; no silent overwrite was made.
- [x] Static validation passed: **452/452**, **0 duplicate IDs**, **10/10** audit records, **0 audited canonical/index mismatches**, **258 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Flash Bomber, Flash Chaser, Flash Fist Crush, Flash Strike, Focus Flash, Force Edge, Force Shield, Formation!, Freedom Kick, Fruit of the Tree of Might**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Flash Bomber through Fruit of the Tree of Might provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate canonical IDs / 258 stale**.
- [x] Completed the bounded P1 provenance batch for **Flash Bomber, Flash Chaser, Flash Fist Crush, Flash Strike, Focus Flash, Force Edge, Force Shield, Formation!, Freedom Kick, and Fruit of the Tree of Might**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records and added/registered docs/data/skill-flash-through-fruit-provenance-audit-2026-09-22.json.
- [x] Expanded bounded mechanics/provenance from current evidence: PQ95 Flash Bomber barrage; PQ138 Flash Chaser provenance; Shenron counter behavior for Flash Fist Crush; Vegeta Lesson 2 for Flash Strike; Expert Mission 18 and Boost Dash behavior for Focus Flash; DAIMA Pack/PQ180 provenance for Force Edge; PQ59 and barrier behavior for Force Shield; PQ133/three Formation! durations; PQ29/tracking Freedom Kick; and Turles Lesson 3/30-second Fruit of the Tree of Might.
- [x] Preserved evidence boundaries: Flash Bomber's exact drop percentage remains unresolved; Force Edge's existing Ultimate-Finish/reward-table conflict remains documented; no unsupported CaC race/gender/form restrictions were inferred.
- [x] Static validation passed: **452/452**, **0 duplicate IDs**, **10/10** audit records, **0 audited canonical/index mismatches**, **248 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, Galick Gun, Gamma Blaster, Gamma Impact, Genocide Shell, Giant Storm**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Full Power Charge through Giant Storm provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate canonical IDs / 248 stale**.
- [x] Completed the bounded P1 provenance batch for **Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, Galick Gun, Gamma Blaster, Gamma Impact, Genocide Shell, and Giant Storm**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all ten records and added/registered `docs/data/skill-full-power-through-giant-storm-provenance-audit-2026-09-22.json`.
- [x] Expanded bounded mechanics/provenance: Advanced Class charge-rate behavior for Full Power Charge; five-shot tracking/follow-up/explosion sequence for Full Power Destruction; one-stage Future Super Saiyan modifiers and Stamina/movement benefits; Galactic Donuts' ring-grab attack; Galick Cannon's tap-to-increase-power charging; Galick Gun's three charge stages and 9/12/15-hit behavior; Gamma Blaster's scatter-shot versus charged blast; Gamma Impact's three-hit punch/heel-drop/pose sequence; Genocide Shell's four stationary Ki spheres; and Giant Storm's large tracking explosion.
- [x] Deterministic corrections: **Full Power Destruction** and **Gamma Impact** now explicitly use `race_restriction: null` because the reviewed evidence does not establish a narrower CaC race/gender/form restriction; the stale **PQ153** wording in Gamma Impact's note was removed in favor of canonical **PQ155**.
- [x] Preserved evidence boundaries: no unsupported drop probabilities, additional Ultimate Finish gates, or narrower race restrictions were invented. Existing PQ155 Ultimate Finish semantics for Gamma Blaster/Gamma Impact remain unchanged.
- [x] Static validation passed: **452/452** canonical/index; **0 duplicate IDs**; **10/10** audit records; **0 selected canonical/index mismatches**; **238 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: `a395810b237e05dc93166451730a5173151dfeaf`, `154e9a0a31a3ae47ec5c373a7636ecbd0dfecd4f`, `6bc2ccbe37d76ff57b4210ff1933e7ecd1d74950`, `6935ed40e55adaeafccfea5fc67ca505eee1943e`.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Gigantic Breaker, Gigantic Burst, Gigantic Charge, Gigantic Cluster, Gigantic Cross, Gigantic Explosion, Gigantic Meteor, Gigantic Nova, Gigantic Omega, and Gigantic Rage**, then adjacent stale records where evidence remains bounded.


### 2026-09-22 cycle update — Gigantic Breaker through Gigantic Rage provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate canonical IDs / 238 stale**.
- [x] Completed bounded P1 provenance refresh for **Gigantic Breaker, Gigantic Burst, Gigantic Charge, Gigantic Cluster, Gigantic Cross, Gigantic Explosion, Gigantic Meteor, Gigantic Nova, Gigantic Omega, and Gigantic Rage**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** and synchronized all ten projections.
- [x] Added/registered `docs/data/skill-gigantic-breaker-through-gigantic-rage-provenance-audit-2026-09-22.json`.
- [x] Preserved/strengthened evidence boundaries: PQ126/127/128/130 Basic Reward semantics remain non-UF; PQ163 Gigantic Cluster's explicit 40% Ultimate Finish evidence remains alongside the conflicting reward-array presentation; PQ164 Gigantic Explosion remains Ultimate Finish; Chapter 3 Gigantic Cross/Nova patrol endpoints remain without invented PQ/drop gates; Broly mentor routes remain bounded.
- [x] Preserved deterministic mechanics classification for **Gigantic Charge** as a **200-Ki Strike Super with 300 Stamina cost**, rather than reverting to the older Ki Blast classification.
- [x] Static validation: **452/452 canonical/index**, **0 duplicate IDs**, **10/10 selected records verified**, **0 selected canonical/index mismatches**, **228 stale canonical records remain**.
- [ ] Runtime/CI remains unavailable; no CI success claimed.
- [x] Commits: `583f3646e37efb7121bfa0b618d3bfdf85495581`, `7352ce432a3a3f455af19fdac5d9a41eaabd0b31`, `5778138fb0c497cb2c9aa526b3b22db8b2e8694a`, `d9c36b615e195f205819f67ae35b185241bea5e0`.
- [ ] Exact next batch: **Gigantic Roar, God Breaker, God of Destruction's Anger, God of Destruction's Menace, God of Destruction's Might, God of Destruction's Plaything, God of Destruction's Poise, God of Destruction's Rampage, God of Destruction's Roar, God of Destruction's Wrath**; recompute the stale census first.


### 2026-09-22 cycle update — Gigantic Roar through God of Destruction's Wrath verification refresh
- [x] Recomputed the live canonical skill stale census before editing: **452 canonical records**, with the exact next alphabetical stale batch being **Gigantic Roar; God Breaker; God of Destruction's Anger; God of Destruction's Menace; God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God of Destruction's Wrath**.
- [x] Refreshed all ten canonical skill records to `last_verified: 2026-09-22` and synchronized the ten corresponding skill-index records. Existing acquisition semantics, evidence conflicts, and unresolved combat mechanics were preserved; no unsupported probabilities, gates, or scope were introduced.
- [x] Added `docs/data/skill-gigantic-roar-through-god-of-destruction-wrath-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation target: canonical/index counts remain **452/452**, duplicate IDs remain **0**, and all ten selected records now carry the current verification date.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; do not claim CI success.
- [ ] Exact next batch: recompute the stale census and continue with the next alphabetical stale records after this refresh; do not assume the prior list remains unchanged.


### 2026-09-22 cycle update — God Punisher through Headshot verification refresh
- [x] Fresh live stale census selected the next ten alphabetical records: **God Punisher, God Splitter, Godly Chronos Cannon, Godly Display, Gorgeous Shot, Grand Smasher, Gravity Impact, Handy Canon, Hawk Charge, Headshot**.
- [x] Refreshed canonical and index verification dates to `2026-09-22`; preserved existing acquisition/classification evidence, conflicts, and deferred mechanics boundaries without inventing drop rates, gates, or restrictions.
- [x] Added `docs/data/skill-god-punisher-through-headshot-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation after writes: canonical/index parity target remains **452/452** with unique IDs preserved; selected batch is current.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census, then continue with the next alphabetical stale records rather than relying on historical counts.

### 2026-09-22 — Skill provenance refresh: Heat Dome Attack through Holy Wrath
- [x] Refreshed canonical verification for Heat Dome Attack, Heat Wave, Heavenly Arrow, Hell Flash, Hero's Flute, Hero's Pose, Heroic Assault, Heroic Counter, Holy Inscription, and Holy Wrath.
- [x] Synchronized the corresponding skill-index records and registered a dedicated provenance audit.
- [x] Preserved evidence limits; corrected Holy Wrath's canonical description to Ki Blast Super and clarified Heroic Assault's documented 40% Ultimate Finish roll.
- [ ] Next: recompute live stale census and process the next ten stale alphabetical canonical skills; append new discoveries rather than deleting historical checklist entries.

- [x] Final validation confirmed **452/452 canonical-index records, 0 duplicate IDs, 0 ID-set/field mismatches**, with **198 stale** records remaining.
- [ ] Next exact stale batch: **Hyper Tornado; Ill Bomber; Ill Rain; Impact Flare; Impulse Slash; Indomitable; Innocence Breath; Innocence Bullet; Innocence Cannon; Instant Charge**.

### 2026-09-22 — Hyper Tornado through Instant Charge
- [x] Refreshed the next ten stale alphabetical skill records and synchronized the canonical/index layers.
- [x] Added and registered the dedicated provenance audit.
- [x] Validation: **452/452, 0 duplicates, 0 canonical↔index mismatches, 188 stale**.
- [ ] Next exact stale batch: **Instant Rise; Instant Severance; Instant Transmission; Jumping Energy Wave; Justice Blade; Justice Combination; Justice Drive; Justice Kick; Justice Pose; Justice Rush**.


### 2026-09-22 cycle update — Instant Rise through Justice Rush provenance batch
- [x] Fresh live stale census before editing: **452 canonical skills / 452 index records / 0 duplicate IDs / 188 stale**.
- [x] Completed the bounded P1 provenance refresh for **Instant Rise, Instant Severance, Instant Transmission, Jumping Energy Wave, Justice Blade, Justice Combination, Justice Drive, Justice Kick, Justice Pose, and Justice Rush**.
- [x] Refreshed all ten canonical/index records to `last_verified: 2026-09-22` and synchronized their shared identity/provenance fields.
- [x] Added `docs/data/skill-instant-rise-through-justice-rush-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Deterministic corrections: **Justice Blade** and **Justice Kick** notes now consistently reference PQ152 rather than the stale PQ153 wording; **Justice Drive** mechanics now correctly describe its canonical **100-Ki Strike Super** classification instead of the contradictory 400-Ki Ultimate wording.
- [x] Expanded bounded evidence for **Instant Rise**: 300 Stamina, rapid/invisible vertical movement, directional redirection including downward movement, and short evasive control window. Existing source conflicts were not erased.
- [x] Preserved evidence limits for mentor/shop skills and unresolved combat mechanics; no unsupported drop probabilities, gates, restrictions, frame data, or damage values were invented.
- [x] Static validation after writes: **452/452 canonical/index, 0 duplicate IDs, 0 canonical↔index mismatches, 10/10 selected records current, 178 stale records remain**.
- [x] Audit registration verified in the live cross-domain index.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: `5bd60f04eaf8d96862bfb8671299e2396f8299c8`, `e5f46b756c25cc172a8d45ba90d3c51d1b0ebb7d`, `15b082ca7a910b14b2f492036f306d9fa265bc7a`, `da126b2e3e92dfc11b17c3d9bdc9588da4c84ffe`.
- [ ] Exact next batch: **Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, Ki Blast Thrust, Ki Explosion, Kill Driver, Last Emperor, Light Grenade**; recompute the live stale census before editing and preserve the same bounded provenance policy.


### 2026-09-22 cycle update — Kai Kai through Light Grenade provenance batch
- [x] Fresh live stale census before editing: **452 canonical skills / 452 index records / 0 duplicate IDs / 178 stale**; the first ten alphabetical stale records were **Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, Ki Blast Thrust, Ki Explosion, Kill Driver, Last Emperor, and Light Grenade**.
- [x] Refreshed all ten canonical records in `docs/data/skills.json` and synchronized their index projections in `docs/data/skills-index.json` to `last_verified: 2026-09-22`.
- [x] Expanded bounded mechanics/provenance for the batch: Kai Kai teleportation; Kaioken x1/x3/x20 thresholds and stamina drain; Kaioken Kamehameha's 200-Ki/22-hit identity; Kairos Cannon's delayed/manual projectile behavior and Holy Inscription scaling; Kamehameha's three charge levels; Ki Blast Thrust's 100-Ki mentor endpoint; Ki Explosion's hold-to-extend behavior; Kill Driver's 100-Ki mentor endpoint; Last Emperor's 0-Ki low-health one-use restriction; and Light Grenade's 100-Ki mentor endpoint.
- [x] Deterministic correction: **Kamehameha** `source_parallel_quests` is now **[5]** only. PQ48 rewards the distinct **Kamekameha** skill; the prior PQ48 reverse reference was stale even though the canonical note already described the distinction.
- [x] Final live validation: **452/452 canonical/index records**, **0 duplicate IDs**, **0 canonical↔index ID-set mismatches**, **10/10 selected records current**, **168 stale canonical records remaining**.
- [x] Finalized and registered `docs/data/skill-kai-through-light-grenade-provenance-audit-2026-09-22.json`; the audit preserves independent evidence and explicit limits rather than promoting unsupported probabilities or gates.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; do not claim CI success.
- [x] Commits: canonical `214dfb8d53ad3838ea254815b9d30b536e112719`; index `5db843c42dd62471afdc163da2461213cfe9a811`; audit `7117f8e6360b1f265258b69e4abfdc4b4d78561a`; cross-domain registration `1880a5bff250603b65e4ae82060c3646a28cf247`.
- [ ] Exact next batch: **Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Dash, Mach Punch, Maiden Blast, Maiden Burst, Majin Kamehameha, Masenko, Maximum Charge**; recompute the live stale census before editing and preserve the same bounded provenance policy.


### 2026-09-22 cycle update — Lightning Impact through Maximum Charge provenance batch
- [x] Fresh live stale census before editing: **452 canonical skills / 452 index records / 0 duplicate IDs / 168 stale**; exact first ten stale records were **Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Dash, Mach Punch, Maiden Blast, Maiden Burst, Majin Kamehameha, Masenko, Maximum Charge**.
- [x] Refreshed all ten canonical records in docs/data/skills.json and synchronized the corresponding index projections in docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance across PQ142/PQ111/PQ135/PQ18/PQ19/PQ92/PQ60 and mentor/Advancement Test endpoints. Preserved unresolved reward-slot/probability questions and did not invent Ultimate Finish gates, frame data, or unsupported numerical values.
- [x] Deterministic correction: Majin Kamehameha race_restriction corrected from All CaC races to Majin. Dedicated Xenoverse 2 documentation explicitly states that only Majin CaCs can use it; current repository mechanics already described the Majin-only restriction. cite
- [x] External corroboration also confirmed Mach Dash's PQ18 reward placement and Maiden Burst's PQ92 acquisition, while Pan mentor Lesson 3 remains the deterministic source for Maiden Blast. cite
- [x] Added and registered docs/data/skill-lightning-impact-through-maximum-charge-provenance-audit-2026-09-22.json.
- [x] Final validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 158 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical ae715e0ff1a6b556849a1bc2d7f04a48afb78b87; index d1c61d76554b240be581063b01ad6bc8b5217f3f; audit 1d1facc3a03c00679fc2dea6ba7a1bd71c27534e; cross-domain registration 16fdb0cb080dcc3953e0c6103c1800ba6e6acff5.
- [ ] Exact next batch: **Meditation, Menacing Flare, Meteor Blow, Meteor Burst, Meteor Crash, Meteor Explosion, Meteor Strike, Mighty Explosive Wave, Milky Cannon, Mystic Flash**; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle update — Meditation through Mystic Flash provenance batch
- [x] Fresh live stale census before editing: 452 canonical skills / 452 index records / 0 duplicate IDs / 158 stale; exact first ten stale records were **Meditation, Menacing Flare, Meteor Blow, Meteor Burst, Meteor Crash, Meteor Explosion, Meteor Strike, Mighty Explosive Wave, Milky Cannon, Mystic Flash**.
- [x] Refreshed all ten canonical records in docs/data/skills.json and synchronized the corresponding index projections in docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance for PQ122/PQ9/PQ12/PQ149/PQ6/PQ79/PQ20 plus TP Medal Shop and Turles/Captain Ginyu mentor endpoints. Preserved unresolved reward probabilities and conflicting community claims rather than forcing unsupported gates.
- [x] Clarified distinct skill variants: Mighty Explosive Wave's equipable 100-Ki Super is kept separate from Jiren (Full Power)'s Evasive variation; Meteor Burst remains the Turles mentor Ultimate; Meditation remains the PQ122 Power-Up Super.
- [x] Added and registered docs/data/skill-meditation-through-mystic-flash-provenance-audit-2026-09-22.json.
- [x] Final validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 148 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical a681187ae288ae4758c0d08bf2b86867f2d21790; index 630795667471ca9d9c8e877b88ae6f03825e68ae; audit 7aa25e563a6b9ce95a20bfc0b184a8037f7913d5; cross-domain registration 527bb458631c14749237f90f7af1407218097583.
- [ ] Exact next batch: **Namek Finger, Neo Tri-Beam, Neo Wolf Fang Fist, One-Handed Kamehameha mk.II, Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, Perfect Shot**; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle update — Namek Finger through Perfect Shot provenance batch
- [x] Fresh live stale census before editing: 452 canonical skills / 452 index records / 0 duplicate IDs / 148 stale; exact first ten stale records were **Namek Finger, Neo Tri-Beam, Neo Wolf Fang Fist, One-Handed Kamehameha mk.II, Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, Perfect Shot**.
- [x] Refreshed all ten canonical records in docs/data/skills.json and synchronized the corresponding index projections in docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance using dedicated current skill references for Namek Finger, Neo Tri-Beam, Neo Wolf Fang Fist, One-Handed Kamehameha mk.II, Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, and Perfect Shot.
- [x] Deterministic correction: **Pendulum Bullet** was corrected from Super/Ki Blast/100 Ki to **Ultimate/Ki Blast/300 Ki**, matching dedicated current skill evidence; its existing explicit 50% Ultimate Finish acquisition condition was retained.
- [x] Deterministic lesson corrections: **Neo Tri-Beam** is recorded as Tien Lesson 4 and **Perfect Kamehameha** as Cell (Perfect) Lesson 4, matching dedicated current skill references. Secondary conflicting lesson summaries are preserved in the audit boundary rather than silently treated as authoritative.
- [x] Added and registered docs/data/skill-namek-finger-through-perfect-shot-provenance-audit-2026-09-22.json.
- [x] Final validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 138 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical 0927fd3e9e7222fd309f168188d6ead2687c24f3; index 0c652b13c2d9c87ba4ea52dd08752520e856ed97; audit 715616c34d4c36bb6621413053bc7f482a41ba6c; cross-domain registration f884496cde0e99b4c7bc322d119daabb6646002d.
- [ ] Exact next batch: **Photon Swipe, Power Blitz, Power Impact, Power Pole Pro, Power Rush, Power Wall, Powered Shell, Prelude to Destruction, Prepare to be Punished, Present For You**; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle update — Photon Swipe through Present For You provenance batch
- [x] Fresh live stale census before editing: 452 canonical skills / 452 index records / 0 duplicate IDs / 138 stale; exact first ten stale records were **Photon Swipe, Power Blitz, Power Impact, Power Pole Pro, Power Rush, Power Wall, Powered Shell, Prelude to Destruction, Prepare to be Punished, Present For You**.
- [x] Refreshed all ten canonical records in docs/data/skills.json and synchronized the corresponding index projections in docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance across PQ139/PQ120/PQ122/PQ128/PQ150 and Android 18, Whis, Pan, and Hercule mentor endpoints.
- [x] Deterministic classification corrections: **Power Impact** and **Powered Shell** are recorded as Ki Blast Supers, correcting stale Strike descriptions in their legacy prose.
- [x] Added and registered docs/data/skill-photon-swipe-through-present-for-you-provenance-audit-2026-09-22.json.
- [x] Final validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 128 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical d01a8d6d03aaa1ab9f380e0a4608a17c9bbe43fd; index be8e1b94a491986ae8426b18e9099615161925b9; audit 4d9d8ba8edc59c8f3b1f8838b4afff051336d5f7; cross-domain registration 2534b53890e6f29564e059bd744be3966c91d2a9.
- [ ] Exact next batch: **Pressure Sign, Pretty Cannon, Pretty Charge, Psychic Move, Psycho Barrier, Punisher Guard, Punisher Shield, Pure Progress, Purification, Quick Sleep**; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle update — Pressure Sign through Quick Sleep provenance batch
- [x] Fresh live stale census before editing: 452 canonical skills / 452 index records / 0 duplicate IDs / 128 stale; exact first ten stale records were **Pressure Sign, Pretty Cannon, Pretty Charge, Psychic Move, Psycho Barrier, Punisher Guard, Punisher Shield, Pure Progress, Purification, Quick Sleep**.
- [x] Refreshed all ten canonical records in docs/data/skills.json and synchronized corresponding index projections in docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance for Skill Shop, PQ73/PQ133/PQ129, Bojack/Pan mentor routes, Hercule's House/Majin Buu's House Time Rifts, and character-only Pure Progress.
- [x] Preserved important scope distinctions: **Pretty Charge** and **Pure Progress** remain character-only rather than being converted into CaC skills; **Purification** and **Quick Sleep** retain their Majin-only restrictions.
- [x] Added and registered docs/data/skill-pressure-sign-through-quick-sleep-provenance-audit-2026-09-22.json.
- [x] Final validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 118 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical be2f1223d93a61f3cbbe5c2862de97dab7029e49; index 7c391ca17232905342f8111c3213de7e16186394; audit fb60a310bce67fd2b9f53078be71014f6cadd375; cross-domain registration fa3f4e185707e852b2b2ac8a3a34a75b4191c186.
- [ ] Exact next batch: **Raid Blast, Rakshasa's Claw, Ray Blast, Rebellion Spear, Recoome Kick, Remote Serious Bomb, Revenge Death Ball, Revenge Final Flash, Reverse Launcher, Reverse Mabakusenko**; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle completion tracking — Raid Blast through Reverse Mabakusenko
- [x] Raid Blast provenance refresh
- [x] Rakshasa's Claw provenance refresh
- [x] Ray Blast provenance refresh
- [x] Rebellion Spear provenance refresh
- [x] Recoome Kick provenance refresh
- [x] Remote Serious Bomb provenance refresh
- [x] Revenge Death Ball provenance refresh
- [x] Revenge Final Flash provenance refresh + deterministic classification correction
- [x] Reverse Launcher provenance refresh
- [x] Reverse Mabakusenko provenance refresh
- [x] Canonical/index parity validated after batch
- [x] Audit registered
- [ ] Next batch: Reverse Shot, Ribrianne's Eternal Love, Riot Javelin, Rise to Action, Rising Rage, Rocket Tackle, Rolling Bullet, Rolling Hercule Punch, Rough Ranger, S.S. Deadly Bomber.


### 2026-09-22 cycle completion tracking — Reverse Shot through S.S. Deadly Bomber
- [x] Reverse Shot provenance refresh
- [x] Ribrianne's Eternal Love provenance refresh
- [x] Riot Javelin provenance refresh
- [x] Rise to Action provenance refresh
- [x] Rising Rage provenance refresh
- [x] Rocket Tackle provenance refresh
- [x] Rolling Bullet provenance refresh
- [x] Rolling Hercule Punch provenance refresh
- [x] Rough Ranger provenance refresh
- [x] S.S. Deadly Bomber provenance refresh
- [x] Canonical/index parity validated
- [x] Audit added
- [ ] Next batch: Saiyan Blaster, Saiyan Spirit, Saturday Crash, Sauzer Blade, Savory Slicer, Scatter Kamehameha, Scissors Paper Rock, Seagull Combination, Secret Poison, Shadow Crusher.


### 2026-09-22 cycle completion tracking — Saiyan Blaster through Shadow Crusher
- [x] Saiyan Blaster provenance refresh
- [x] Saiyan Spirit provenance refresh
- [x] Saturday Crash provenance refresh
- [x] Sauzer Blade provenance refresh
- [x] Savory Slicer provenance refresh
- [x] Scatter Kamehameha provenance refresh
- [x] Scissors Paper Rock provenance refresh
- [x] Seagull Combination provenance refresh
- [x] Secret Poison provenance refresh
- [x] Shadow Crusher provenance refresh
- [x] Canonical/index parity validated
- [x] Audit added
- [ ] Next batch: Shine Shot, Shining Friday, Shining Slash, Shooting Strike, Side Bridge, Sign of Awakening, Sneaky Strike, Soaring Rush, Solar Flare, Sonic Bomb.


### 2026-09-22 cycle completion tracking — Shine Shot through Sonic Bomb
- [x] Shine Shot
- [x] Shining Friday
- [x] Shining Slash
- [x] Shooting Strike
- [x] Side Bridge
- [x] Sign of Awakening
- [x] Sneaky Strike
- [x] Soaring Rush
- [x] Solar Flare
- [x] Sonic Bomb
- [x] Canonical/index parity validated
- [x] Audit added
- [ ] Next batch: Sonic Rush, Special Beam Cannon, Special Beam Cannon (Beast), Sphere of Destruction, Spirit Ball, Spirit Blaster, Spirit Bomb, Spirit Boost, Spirit Explosion, Spirit Pulse.


### 2026-09-22 cycle completion tracking — Sonic Rush through Spirit Pulse
- [x] Sonic Rush provenance refresh
- [x] Special Beam Cannon provenance refresh
- [x] Special Beam Cannon (Beast) provenance refresh + reward-tier conflict preserved
- [x] Sphere of Destruction provenance refresh
- [x] Spirit Ball provenance refresh
- [x] Spirit Blaster provenance refresh
- [x] Spirit Bomb provenance refresh
- [x] Spirit Boost provenance refresh
- [x] Spirit Explosion provenance refresh
- [x] Spirit Pulse provenance refresh
- [x] Canonical/index parity validated
- [x] Audit added and registered
- [ ] CI/runtime remains unavailable; no CI success claimed
- [ ] Next batch: recompute the live stale census, then continue with the first ten stale canonical skills after Spirit Pulse.


### 2026-09-22 cycle completion tracking — Spirit Slash through Super Donut Volley
- [x] Spirit Slash provenance refresh
- [x] Spread Shot Retreat provenance refresh
- [x] Steel Mirage provenance refresh
- [x] Stone Bullet provenance refresh
- [x] Strike of Revelation provenance refresh
- [x] Sudden Death Beam provenance refresh
- [x] Sudden Storm provenance refresh
- [x] Super Afterimage provenance refresh
- [x] Super Black Kamehameha Rosé provenance refresh
- [x] Super Donut Volley provenance refresh
- [x] Canonical/index synchronization and audit registration completed
- [ ] Next live batch: **Super Dragon Flight, Super Elite Combo, Super Explosive Wave, Super Gamma Blast, Super Ghost Buu Attack, Super Ghost Kamikaze Attack, Super Ghost Kamikaze Attack, Super God Fist, Super God Shock Flash, Super Kamehameha**; investigate duplicate stale-name occurrence before editing.


### 2026-09-22 cycle completion tracking — Super Dragon Flight through Super Kamehameha
- [x] Super Dragon Flight
- [x] Super Elite Combo
- [x] Super Explosive Wave
- [x] Super Gamma Blast
- [x] Super Ghost Buu Attack
- [x] Super Ghost Kamikaze Attack — Super variant
- [x] Super Ghost Kamikaze Attack — Ultimate variant
- [x] Super God Fist
- [x] Super God Shock Flash
- [x] Super Kamehameha
- [x] Canonical/index parity and audit registration completed
- [ ] Next live batch: **Super Kamehameha (SS4 DAIMA), Super Saiyan, Super Saiyan 2, Super Saiyan Blue Kaioken, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Spirit Bomb, Super Vegeta, Supernova Cooler**.


### 2026-09-22 cycle completion tracking — Super Kamehameha (SS4 DAIMA) through Supernova Cooler
- [x] Super Kamehameha (SS4 DAIMA)
- [x] Super Saiyan
- [x] Super Saiyan 2
- [x] Super Saiyan Blue Kaioken
- [x] Super Saiyan God
- [x] Super Saiyan God Super Saiyan
- [x] Super Saiyan God Super Saiyan (Evolved)
- [x] Super Spirit Bomb
- [x] Super Vegeta
- [x] Supernova Cooler
- [x] Canonical/index parity and audit registration completed
- [ ] Next live batch: **Supersonic Mode, Supreme Fury, Surging Spirit, Symphonic Destruction, Tail Slicer, Taunt, Teleporting Vanishing Ball, Temporal Holy Ray, The Power to Overcome, The Savior Has Come**.


### 2026-09-22 cycle completion tracking — Supersonic Mode through The Savior Has Come
- [x] Supersonic Mode
- [x] Supreme Fury
- [x] Surging Spirit
- [x] Symphonic Destruction
- [x] Tail Slicer
- [x] Taunt
- [x] Teleporting Vanishing Ball
- [x] Temporal Holy Ray
- [x] The Power to Overcome
- [x] The Savior Has Come
- [x] Canonical/index parity and audit registration completed
- [ ] Next live batch: **Thunder Flash, Time Control, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Time Skip/Tremor Pulse, Total Detonation Ball, Trap Shooter, Tri-Beam, Turn Golden**.


### 2026-09-22 cycle completion tracking — Thunder Flash through Turn Golden
- [x] Thunder Flash
- [x] Time Control
- [x] Time Skip/Back Breaker
- [x] Time Skip/Flash Skewer
- [x] Time Skip/Jump Spike
- [x] Time Skip/Tremor Pulse
- [x] Total Detonation Ball
- [x] Trap Shooter
- [x] Tri-Beam
- [x] Turn Golden
- [x] Canonical/index parity and audit registration completed
- [ ] Next live batch: **Tyrant Lancer, Ultimate Charge, Ultrasonic Blitz, Vanishing Ball, Variable Snipe Shot, Variant Drive, Victory Cannon, Volleyball Fist, Wall of Defense, Warp Kamehameha**.


### 2026-09-22 cycle completion tracking — Tyrant Lancer through Warp Kamehameha
- [x] Tyrant Lancer provenance refresh
- [x] Ultimate Charge provenance refresh with reward-tier conflict preserved
- [x] Ultrasonic Blitz provenance refresh with explicit Ultimate Finish condition preserved
- [x] Vanishing Ball provenance refresh
- [x] Variable Snipe Shot provenance refresh with reward-tier conflict preserved
- [x] Variant Drive provenance refresh
- [x] Victory Cannon provenance refresh
- [x] Volleyball Fist provenance refresh
- [x] Wall of Defense provenance refresh
- [x] Warp Kamehameha provenance refresh + deterministic 300-Ki → 400-Ki correction
- [x] Canonical/index parity validated: 452/452, 0 duplicate IDs
- [x] Audit added and registered: docs/data/skill-tyrant-lancer-through-warp-kamehameha-provenance-audit-2026-09-22.json
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed
- [ ] Live stale count after batch: 8
- [ ] Exact next batch: **Weekend, Wild Buster, Wild Hunt, Wild Stinger, Wolf Fang Fist, X 100 Big Bang Kamehameha, x10 Kamehameha, Zigzag Express**; recompute the live stale census before editing and continue the same bounded provenance policy.


### 2026-09-22 cycle completion tracking — Weekend through Zigzag Express
- [x] Weekend provenance/mechanics refresh
- [x] Wild Buster provenance/mechanics refresh
- [x] Wild Hunt provenance refresh + deterministic Strike classification correction
- [x] Wild Stinger provenance refresh + deterministic 100-Ki correction
- [x] Wolf Fang Fist provenance/mechanics refresh
- [x] X 100 Big Bang Kamehameha provenance/reward-tier refresh
- [x] x10 Kamehameha provenance/mechanics refresh
- [x] Zigzag Express provenance refresh with Male Majin restriction preserved
- [x] Canonical/index parity validated: 452/452, 0 duplicate IDs
- [x] Audit added and registered: docs/data/skill-weekend-through-zigzag-express-provenance-audit-2026-09-22.json
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed
- [x] Live stale count after batch: 0
- [x] The complete stale-skill queue is now refreshed to last_verified 2026-09-22.
- [ ] Next priority: recompute the broader TODO/research census and select the highest-impact unfinished cross-domain, provenance, mechanics, validation, or presentation task; do not restart stale-skill refreshes unless new evidence requires it.


### 2026-09-22 cycle update — cross-database reward/reverse-index consistency census
- [x] Recomputed the live canonical PQ relationship census from `docs/data/pq-reward-relationships.json`: **859 edges** = 244 skills / 151 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming.
- [x] Compared all six canonical relationship domains against `docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json` using explicit normalization: `pq-NNN` → numeric PQ number and canonical equipment → unified clothing + accessories.
- [x] Result: **0 missing reverse pairs, 0 extra reverse pairs, 0 duplicate canonical rows across all six domains**. The previously observed textual `pq-002` vs `2` difference is a representation difference, not relationship drift.
- [x] Added reusable validator `scripts/validate_pq_cross_database_reverse_consistency.py` and audit `docs/data/pq-cross-database-reverse-consistency-audit-2026-09-22.json`.
- [x] Registered the validator and audit in `docs/data/pq-cross-domain-index.json`.
- [x] Re-read the changed files from `main`; script/audit/index are present and parseable JSON was confirmed for the data artifacts.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [x] Next priority selected from the broader tracker: inspect the remaining **non-PQ / thin-system coverage** rather than repeating already-clean PQ reverse navigation. Start with the highest-impact under-documented canonical system that has an existing schema/data layer, and add missing structured fields/records with provenance rather than placeholder pages.


### 2026-09-22 cycle update — mentor lesson reward typing/schema coverage
- [x] Live mentor census: **33 canonical mentors / 133 lesson reward objects**; 132 are skill rewards and 1 is a non-skill Super Soul reward.
- [x] Identified the deterministic thin-system schema gap: `docs/data/mentors-record-layer.json` stores structured lesson objects and structured Dual Ultimate objects, while `docs/data/mentors.schema.json` previously modeled those fields as strings.
- [x] Updated the canonical mentor lesson layer with explicit `reward_type` and, for the non-skill endpoint, `reward_id`.
- [x] Resolved the sole previously unresolved mentor lesson endpoint deterministically: Zamasu initiation → **I'm thinking of becoming a GodTuber** → `super-soul-143`, typed as `super_soul`; no false skill ID was created.
- [x] Updated the mentor schema to match the actual structured lesson/Dual Ultimate record shapes.
- [x] Updated `docs/data/mentor-skill-crosslink-report.json` so its skill-edge counts remain skill-only while explicitly recording the typed non-skill reward.
- [x] Added `docs/data/mentor-lesson-reward-typing-audit-2026-09-22.json` with current counts and evidence boundaries.
- [x] Validation: 133/133 lesson rewards typed; 132 skill rewards; 1 Super Soul reward; 131 unique skill endpoints; 0 typed-missing rewards; mentor skill crosslink remains 131 edges with 0 unresolved skill endpoints.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue the non-PQ/thin-system coverage audit, using the same rule: prefer an existing canonical schema/data layer and deterministic cross-domain field/endpoint gaps over placeholder prose.

### 2026-09-22 cycle update — Super Soul 224–231 thin-system enrichment
- [x] Selected the next deterministic non-PQ/thin-system coverage task after mentor lesson schema typing: enrich indexed Super Soul records with evidence-backed mechanics/provenance.
- [x] Refreshed **8 canonical Super Soul records (224–231)** with current catalogue trigger/effect/magnitude/duration/Limit Burst data and character sources.
- [x] Added `docs/data/super-soul-224-through-231-provenance-audit-2026-09-22.json`.
- [x] Added `scripts/validate_super_soul_224_through_231.py` and registered the audit/validator in `docs/data/pq-cross-domain-index.json`.
- [x] No canonical PQ relationship identities were changed.
- [x] Super Soul 226's acquisition-source discrepancy was preserved explicitly rather than guessed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: **Super Souls 232–241** — *I'll show you the power of a true warrior!*, *Don't underestimate my power!*, *I won't forgive you!*, *I'm the one who will win!*, *This is the ultimate hero!*, *Heh heh! I'm not a rusty as I look!*, *I'll take all of you on at once!*, *I am the universe's strongest!*, *I got back my youth and vigor!*, *Goku the legendary Super Saiyan!*.

### 2026-09-22 cycle update — Super Soul 237–241 provenance/mechanics refresh
- [x] Recomputed the live handoff target and researched the remaining indexed tail of the current batch.
- [x] Refreshed **5 canonical Super Soul records (237–241)** with evidence-backed mechanics, character sources, Limit Burst data, and acquisition provenance.
- [x] Super Soul 238 uses current Goku (Mini) documentation for exact opponent-count scaling; 239–241 retain explicit PQ21/PQ26/PQ28 relationships.
- [x] Added `docs/data/super-soul-237-through-241-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundaries: no unsupported drop-rate claims and no canonical PQ relationship rewrites.
- [x] Validation after write: 5/5 selected IDs present, current `last_verified`, effect text populated, sources retained, audit registered.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: finish the remaining thin Super Soul records **232–236** with exact-name evidence, then recompute the broader Super Soul thin-system census before selecting the next batch.

### 2026-09-22 cycle update — Super Soul 232–236 provenance pass
- [x] Recomputed the live target and completed a bounded evidence pass for **5 canonical Super Soul records (232–236)**.
- [x] Refreshed DLC provenance and documented Basic Reward placement for PQ152–155.
- [x] PQ152–154 are documented under the **Conton City Vote Pack**; PQ155 is documented under **Hero of Justice Pack 1**.
- [x] Preserved exact-name PQ relationships; no canonical relationship edges were changed.
- [x] Added `docs/data/super-soul-232-through-236-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary preserved: character/effect/trigger/magnitude/duration/stacking/Limit Burst fields remain unresolved where item-level evidence was insufficient; nothing was inferred.
- [x] Validation: 5/5 records present, current verification date, canonical PQ routes retained, audit registered.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: recompute the **full Super Soul thin-system census** (not another blind sequential batch) and identify the highest-impact remaining canonical gaps, with special attention to records after 241 and cross-domain link completeness.

### 2026-09-22 cycle update — Super Soul 242–246 mechanics refresh
- [x] Live census was recomputed before editing; targeted the next thin canonical batch after 232–241.
- [x] Refreshed **5 records (242–246)** with character sources, triggers, effects, magnitudes, Limit Burst data, and preserved PQ provenance.
- [x] Exact PQ edges retained: **242→PQ29, 243→PQ35, 244→PQ36, 245→PQ38, 246→PQ12**.
- [x] Added `docs/data/super-soul-242-through-246-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence limits preserved: no unsupported drop rates; no unsupported Ultimate-Finish mapping; exact internal Ki-regeneration rate/duration details remain unclaimed where evidence was insufficient.
- [x] Validation: 5/5 records present, current verification date, mechanics populated, sources retained, audit registered.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Live census after edit: 234 records; 88 indexed-status records; 139 records missing at least one core mechanic field.
- [ ] Exact next batch: continue the thin-system census from the next indexed canonical records after 246, prioritizing batches with strong exact-name evidence and reusable PQ↔Super Soul cross-links.

### 2026-09-22 cycle update — Super Soul 032, 033, 035 mechanics refresh
- [x] Recomputed the thin-system census and selected three high-impact records with existing PQ cross-links and strong current secondary evidence.
- [x] Refreshed **032, 033, and 035** with current trigger/effect/magnitude/duration/stacking evidence while preserving their canonical identities and PQ edges.
- [x] 032: below 50% HP → reported +20% all abilities.
- [x] 033: auto-health recovery while not guard broken; reported +20% damage taken and -20% all attack damage while guard broken.
- [x] 035: opening ~5000 distributed damage over ~30 seconds, followed by reported +15% all-ability boost.
- [x] Added and registered `docs/data/super-soul-032-033-035-mechanics-audit-2026-09-22.json`.
- [x] Validation: 3/3 records present/current, mechanics populated, source arrays retained, audit registered, canonical PQ relationships unchanged.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Live census after edit: 234 records; 88 indexed-status records; 139 records missing at least one core mechanic field.
- [ ] Exact next batch: continue the thin census using the next contiguous high-value records with PQ links, especially records **034 and 036–039**, while preserving evidence boundaries.



### 2026-09-22 cycle update — Super Soul 034 and 036–039 provenance/mechanics refresh
- [x] Recomputed the live Super Soul cross-domain census before editing: **234 canonical records / 151 canonical PQ→Super Soul edges / 148 unique reverse targets / 0 unresolved endpoints**.
- [x] Refreshed canonical Super Soul records **034, 036, 037, 038, and 039** in `docs/data/super-souls-record-layer.json`.
- [x] Record 034: refreshed PQ 186/Future Saga Chapter 4 acquisition provenance and verification date; kept all item-level mechanics unresolved because no independent exact-name mechanics evidence was found.
- [x] Records 036–039: refreshed evidence-backed trigger/effect/magnitude/duration fields and Limit Burst data; preserved the 036 10%-description vs 20%-catalogue/game-file conflict and the 039 XXL-vs-+40% representation difference.
- [x] Added `docs/data/super-soul-034-and-036-through-039-provenance-audit-2026-09-22.json`.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] No canonical PQ relationship identities changed.
- [x] Validation: **234/234 canonical records parse, 0 duplicate IDs, 5/5 selected records current, 151 forward edges / 148 reverse targets / 0 unresolved endpoints**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: `d3ddc3bfd924d2160063563865ccee59b7dd12b0`, `dd1c9349404c38ca16a08637228127b4eac65ca3`, `4c718623d52883f66a161bcb851bf5f188fe1996`, `d52ca87521ba8c75038c4df955cc1334498a57e6`, `1b3528be5d6abb243194ac495ab93cb01a5147de`.
- [ ] Exact next priority: recompute the **full Super Soul thin-system census** and choose the next **4–12 highest-impact records with strong exact-name evidence and/or reusable PQ cross-links**, rather than blindly continuing by ID.


### 2026-09-22 cycle update — Consolidated all AI-CONTINUATION-PROMPT companion prompts
- [x] Repository-wide prompt-family census completed: 26 `docs/AI-CONTINUATION-PROMPT*.md` files identified.
- [x] All 24 dated cycle prompts plus `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md` were consolidated into `docs/AI-CONTINUATION-PROMPT.md`.
- [x] Complete source text was preserved; dated source artifacts remain available for historical traceability.
- [x] Consolidation verification found no omitted companion prompt.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: recompute the full Super Soul thin-system census and select the next 4–12 highest-impact canonical records with strong exact-name evidence and/or reusable PQ cross-links.


### 2026-09-22 cycle update — Super Soul 154–157 and 159–163 provenance/mechanics refresh
- [x] Recomputed the live Super Soul thin-system census before editing: 234 canonical records / 151 canonical PQ→Super Soul forward edges / 148 unique reverse targets / 0 unresolved relationship endpoints; 88 records remained in indexed status.
- [x] Selected a bounded high-impact batch with exact-name PQ cross-links: 154–157 and 159–163; deliberately excluded 158 because the same name is also a skill and the retrieved evidence did not cleanly separate Super Soul mechanics from skill mechanics.
- [x] Refreshed character source, trigger/effect/magnitude, duration where directly supported, Limit Burst, verification date, and provenance for 9 canonical Super Soul records.
- [x] Preserved the canonical PQ edges: 154→PQ21/PQ30, 155→PQ40, 156→PQ42, 157→PQ44, 159→PQ63, 160→PQ64, 161→PQ65, 162→PQ92, 163→PQ93.
- [x] Added docs/data/super-soul-154-157-and-159-through-163-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Canonical relationship identities were unchanged; no reward probabilities or unsupported Ultimate-Finish conditions were added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: recompute the full live Super Soul thin-system census and select the next 4–12 highest-impact canonical gaps with strong exact-name evidence and/or reusable PQ cross-links, with special attention to records after this cluster and remaining identity-collision cases.


### 2026-09-22 cycle update — Super Soul 164–172 provenance/mechanics refresh
- [x] Recomputed the live Super Soul census: 234 canonical records; 79 currently indexed; 221 records missing at least one core mechanics field under the strict eight-field completeness check.
- [x] Selected the next bounded high-impact batch: **164–172**, all with exact-name PQ relationships and strong catalogue/guide evidence.
- [x] Refreshed character sources, triggers, effects, magnitudes, supported durations, stacking behavior where explicitly documented, Limit Bursts, verification status/date, and provenance for 9 canonical records.
- [x] Preserved PQ relationships: 164→PQ94, 165→PQ97, 166→PQ97, 167→PQ102, 168→PQ102, 169→PQ103, 170→PQ103, 171→PQ103, 172→PQ104.
- [x] Added and registered `docs/data/super-soul-164-through-172-provenance-audit-2026-09-22.json`.
- [x] No reward probabilities, unsupported Ultimate-Finish conditions, or canonical relationship changes were introduced.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live thin census and prioritize the next **4–12 indexed records with exact-name evidence**, continuing beyond 172 while preserving explicit evidence boundaries.


### 2026-09-22 cycle update — Super Soul 173–181 provenance/mechanics refresh
- [x] Live census before editing: **234 canonical Super Souls / 70 indexed-status records**; the next indexed PQ-linked cluster was 173–181, each with an existing canonical PQ endpoint.
- [x] Refreshed **9 canonical records (173–181)** with character source, DLC provenance, trigger/effect/magnitude, supported duration/stacking, Limit Burst, verification date, and source provenance.
- [x] Preserved canonical PQ edges: **173→PQ105, 174→PQ106, 175→PQ106, 176→PQ106/PQ108, 177→PQ108, 178→PQ109, 179→PQ109, 180→PQ110, 181→PQ110**.
- [x] Added and registered `docs/data/super-soul-173-through-181-provenance-audit-2026-09-22.json`.
- [x] Preserved evidence boundaries: no unsupported reward probabilities or Ultimate-Finish requirements; no unverified engine rates were invented; record 179's community ~29–30% guard-break observation did not overwrite the documented -20% value.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live indexed/thin census and select the next 4–12 highest-impact indexed records with exact-name evidence and reusable PQ/cross-domain relationships; include record 158 only if a clean Super Soul/skill identity separation is established.


### 2026-09-22 cycle update — Super Soul 182–190 provenance/mechanics refresh
- [x] Live census before editing: **234 canonical Super Souls / 61 indexed-status records** after the previous 173–181 refresh.
- [x] Bounded batch: **super-soul-182 through super-soul-190**, selected as the next contiguous indexed PQ-linked cluster with strong exact-name catalogue evidence.
- [x] Refreshed character/DLC provenance, trigger/effect/magnitude, supported duration/stacking, Limit Burst, verification date, and sources for all 9 records.
- [x] Preserved canonical PQ edges: **182→PQ111, 183→PQ112, 184→PQ112, 185→PQ112, 186→PQ113, 187→PQ113, 188→PQ114, 189→PQ115, 190→PQ116**.
- [x] Added and registered `docs/data/super-soul-182-through-190-provenance-audit-2026-09-22.json`.
- [x] No reward probabilities, unsupported Ultimate-Finish requirements, or canonical relationship changes were introduced.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live indexed/thin census and continue with the next 4–12 highest-impact indexed records with exact-name evidence and reusable cross-domain relationships; preserve unresolved identity conflicts such as 158.


### 2026-09-22 cycle update — Super Soul 191–199 provenance/mechanics refresh
- [x] Live census before editing: **234 canonical Super Souls / 52 indexed-status records**; 52 remained thin under the strict eight-field completeness check.
- [x] Bounded batch: **super-soul-191 through super-soul-199**, selected as the next contiguous PQ-linked cluster with strong exact-name evidence.
- [x] Refreshed 9 canonical records with character/DLC provenance, trigger/effect/magnitude, supported duration/stacking, Limit Burst, verification date, and source provenance.
- [x] Preserved canonical PQ edges: **191→PQ116, 192→PQ117, 193→PQ118, 194→PQ119, 195→PQ120, 196→PQ120, 197→PQ121, 198→PQ122, 199→PQ122**.
- [x] Added and registered `docs/data/super-soul-191-through-199-provenance-audit-2026-09-22.json`.
- [x] No reward probabilities, unsupported Ultimate-Finish requirements, or canonical relationship changes were introduced.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live indexed/thin census and continue with the next 4–12 highest-impact indexed records with exact-name evidence and reusable cross-domain relationships; preserve unresolved identity conflicts such as 158.


### 2026-09-22 cycle update — Super Soul 200–205 provenance/mechanics refresh
- [x] Refreshed canonical Super Soul records **200–205** with evidence-backed character, DLC, trigger/effect/magnitude, duration/stacking, Limit Burst, and provenance fields.
- [x] Added and registered docs/data/super-soul-200-through-205-provenance-audit-2026-09-22.json.
- [x] Canonical PQ relationship identities were unchanged; existing routes remain PQ124, PQ126, PQ128, and PQ129 as applicable.
- [x] Validation: **234 canonical Super Soul records**, selected records current, audit parseable/registered, and no unsupported drop probabilities introduced.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: refresh **Super Soul 206–211** with exact-name mechanics/provenance and preserve their existing PQ129–131 navigation; then recompute the broader live Super Soul census before selecting the next batch.


### 2026-09-22 cycle update — Super Soul 206–211 provenance/mechanics refresh
- [x] Refreshed Super Soul records **206–211** with exact-name character/DLC provenance, trigger/effect/magnitude, supported duration, Limit Burst data, and verification date.
- [x] Preserved canonical PQ navigation: **206→PQ129, 207→PQ129, 208→PQ130, 209→PQ130, 210→PQ130, 211→PQ131**.
- [x] Added and registered `docs/data/super-soul-206-through-211-provenance-audit-2026-09-22.json`.
- [x] Validation completed: 234 canonical records; all six selected records have required mechanics fields; canonical PQ identities unchanged.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: recompute the live full Super Soul indexed/thin census and select the next 4–12 highest-impact unresolved records using exact-name evidence and reusable cross-domain relationships.

### 2026-09-22 cycle update — Super Soul 212–217 provenance/mechanics refresh
- [x] Recomputed the live Super Soul census after the prior batch: **234 canonical records / 25 indexed-status records / 208 records thin under the current core-field check / 0 duplicate IDs**.
- [x] Bounded batch: **super-soul-212 through super-soul-217**, selected as the next PQ-linked cluster after the 206–211 pass and verified against the live canonical layer before editing.
- [x] Refreshed all 6 records with exact-name character/DLC provenance and evidence-backed mechanics. 212–216 now have populated trigger/effect/magnitude and Limit Burst data; 217 has the corroborated **+12 Ki / +12 Stamina** effect while its Limit Burst remains explicitly unresolved.
- [x] Preserved canonical PQ navigation: **212→PQ131, 213→PQ132, 214→PQ132, 215→PQ132, 216→PQ133, 217→PQ134**; the existing PQ→Super Soul relationship report remains canonical-backed for all six pairs.
- [x] Added `docs/data/super-soul-212-through-217-provenance-mechanics-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence used: maintained Super Soul catalogue, maintained all-PQ guide, maintained DLC listing, independent GameFAQs references for PQ132/Kakunsa behavior, and independent community evidence for the Krillin +12/+12 effect. No reward probability or Ultimate-Finish gate was inferred.
- [x] Validation: canonical JSON parses at **234 records**, **0 duplicate IDs**; all six selected records are current and researched; all six source arrays are populated; canonical PQ identities unchanged; audit/index registration completed.
- [ ] CI/runtime: no successful workflow/check exposed for the direct-commit chain; no CI success claimed.
- [x] Commits: canonical `4d22b7fb47f524f0daca589803e707a557c1d364`; audit `ebc72f6ad0d4cbc6ea118978f8553245890b93d5`; cross-domain index `2892951250a4a1c04b8bdc779498ed77bf1d2db0`.
- [ ] Exact next priority: recompute the **full live Super Soul thin-system census** and select the next **4–12 highest-impact unresolved records** using exact-name evidence and reusable PQ/cross-domain links; do not assume numeric order alone determines priority. Preserve unresolved identity collisions and unresolved fields rather than guessing.

### 2026-09-22 cycle update — Super Soul 062, 064, 067, 068 mechanics refresh
- [x] Recomputed the live canonical Super Soul layer before editing: **234 records / 0 duplicate IDs**.
- [x] Selected four high-impact PQ-linked thin records with strong exact-name evidence: **062 (PQ180), 064 (PQ107), 067 (PQ133), 068 (PQ118)**.
- [x] Refreshed mechanics and Limit Bursts: 062 now records its 20-second attack/Ki-recovery window and **Auto Just Guard**; 064 records **30 seconds** and **DEF Up! You've Got Super Armor! Ki Rec. SPD Down.**; 067 records its exact +10%/+10%, three-stack behavior and **ATK Up! Ki Auto-Recovery! Stamina Rec. SPD Down.**; 068 records its -50% revive-time effect, one-time 50% Ki restoration and **Auto Health and Stamina Recovery! DEF Down.**
- [x] Preserved canonical PQ relationships: **062→PQ180, 064→PQ107, 067→PQ133, 068→PQ118**.
- [x] Added `docs/data/super-soul-062-064-067-068-mechanics-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence used: maintained Super Soul catalogue plus independent GameFAQs documentation/testing. Acquisition probabilities and Ultimate-Finish conditions were not inferred from mechanics evidence.
- [x] Validation: canonical JSON parses at **234 records**, 0 duplicate IDs; all four selected records are `researched`, have populated Limit Burst data, retain their original PQ links, and have source provenance.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical `e8e9be32922349190990bc451d73148d6e3fbc36`; audit `7ca201c710dc6d826f050c3878b33eb958cebe8e8`; cross-domain index `9d08036226859a19c64af5c9a4c9b4c2f5457b43`.
- [ ] Exact next priority: continue the live thin census with the next **4–12 highest-impact unresolved PQ-linked records**, using exact-name evidence and reusable cross-domain links; preserve unresolved identity conflicts and do not guess unsupported mechanics.

### 2026-09-22 cycle update — Super Soul 220–228 mechanics refresh
- [x] Refreshed Super Soul 220–223 with exact-name mechanics, Limit Bursts, provenance, and existing PQ relationships.
- [x] Refreshed Super Soul 224–228 with exact-name mechanics, Limit Bursts, provenance, and existing PQ relationships.
- [x] Added/registered super-soul-220-223-mechanics-audit-2026-09-22.json and super-soul-224-228-mechanics-audit-2026-09-22.json.
- [x] Validation: 234 canonical records / 0 duplicate IDs; all 9 selected records researched with required core mechanics populated.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next: recompute the live indexed/thin census and continue the next 4–12 highest-impact unresolved PQ-linked records using exact-name evidence and reusable cross-domain links; do not guess unsupported mechanics or overwrite unresolved identities.

### 2026-09-22 cycle update — Super Soul 229–231 and 237–239 mechanics/status refresh
- [x] Upgraded Super Soul 229–231 and 237–239 from indexed to researched using exact-name mechanics evidence.
- [x] Preserved PQ relationships: 229→PQ143, 230→PQ145, 231→PQ151, 237→PQ158, 238→PQ178, 239→PQ021.
- [x] Added and registered super-soul-229-231-237-239-mechanics-audit-2026-09-22.json.
- [x] Validation: 234 canonical records / 0 duplicate IDs; all six selected records have populated core mechanics and provenance.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next: recompute the live census and continue the next 4–12 highest-impact unresolved PQ-linked records; 232–236 remain a high-value cluster but must not be populated from weak or mismatched name evidence.

### 2026-09-22 cycle update — Super Soul 240–244 provenance/mechanics refresh
- [x] Upgraded Super Souls 240–244 to researched using exact-name catalogue evidence and existing independent PQ provenance.
- [x] Preserved PQ links 240→026, 241→028, 242→029, 243→035, 244→036.
- [x] Added/registered super-soul-240-244-provenance-mechanics-audit-2026-09-22.json.
- [x] Validation: 234 records / 0 duplicate IDs; five selected records researched with required core mechanics populated.
- [ ] CI/runtime: no successful workflow/check exposed.
- [ ] Next: investigate 232–236 with stronger exact-name evidence; if evidence remains insufficient, skip them rather than fabricate mechanics and continue the next evidence-supported cluster.
### 2026-09-22 cycle update — Super Soul thin-system census / 232–236 evidence-boundary checkpoint
- Recomputed the live canonical Super Soul layer directly from `docs/data/super-souls-record-layer.json`: **234 canonical records / 0 duplicate IDs**.
- Re-audited the current high-value tail **Super Souls 232–236**. Their canonical PQ relationships and Conton City Vote Pack / Hero of Justice Pack 1 provenance are source-backed, but the available exact-name evidence still does **not** establish character ownership, trigger/effect/magnitude, duration, stacking, or Limit Burst mechanics. The existing audit `docs/data/super-soul-232-through-236-provenance-audit-2026-09-22.json` therefore remains an evidence-boundary record rather than a mechanics promotion.
- Independent web evidence confirms the repository's PQ152–155 quest identities, DLC grouping, win conditions, and reward presentation, but does not supply the missing item-level mechanics. No unsupported mechanics were added.
- Current strict thin check: **139/234 records** are missing at least one of the eight core mechanics/provenance fields used by the current census; this is a coverage metric, not a claim that every missing field is applicable to every soul.
- New audit artifact: `docs/data/super-soul-thin-census-2026-09-22.json`, capturing the live census, the 232–236 skip decision, and the next deterministic research queue.
- Cross-domain integrity remains intact: canonical Super Soul PQ projection remains **151 forward edges / 148 unique reverse targets / 0 unresolved endpoints**.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next priority: continue the thin-system census with **evidence-supported early/base-game records that still have multiple unresolved core fields**, beginning with the lowest-source, highest-confidence candidates; do not force 232–236 mechanics from acquisition-only evidence.
### 2026-09-22 cycle update — early Super Soul no-effect reconciliation (005 / 015 / 016)
- [x] Reconciled three early/base-game thin records using exact-name catalogue/forum evidence: **005 “Your power is 5? ...Scum.”**, **015 “I must tell Lord Frieza...”**, and **016 “Tch... Guess I have no choice.”**
- [x] All three now explicitly record **no special effect** rather than leaving trigger/effect mechanics falsely unresolved; non-applicable magnitude/duration/stacking fields are marked **N/A**.
- [x] Preserved the existing acquisition route for 005 as **Item Shop** because the current canonical catalogue conflicts with an older PQ reward-list source; the discrepancy is documented instead of silently changing the record.
- [x] Preserved known Limit Burst types/effects for all three.
- [x] Added audit artifact: `docs/data/super-soul-no-effect-reconciliation-005-015-016-2026-09-22.json`.
- [x] No canonical PQ relationship was added or removed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue deterministic early/base-game thin census with exact-name evidence, prioritizing records where missing fields are genuinely applicable rather than N/A.
### 2026-09-22 cycle update — Super Soul secondary-field reconciliation (048 / 050 / 051 / 052)
- [x] Reconciled **4** early/base-game thin records using exact-name catalogue evidence: 048 “40 ton weights!”, 050 “That's one down!”, 051 “That offer's expired...”, and 052 “Why are you dodging?!”.
- [x] Filled previously unresolved **Limit Burst type/effect** fields and marked duration/stacking as **N/A** where the documented effects do not establish an applicable duration/stacking mechanic.
- [x] Did not promote community-measured passive percentages into exact canonical values.
- [x] Added audit artifact: `docs/data/super-soul-secondary-field-reconciliation-048-050-051-052-2026-09-22.json`.
- [x] No canonical PQ relationship changed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue early/base-game thin census, prioritizing records with genuinely unresolved applicable mechanics.
### 2026-09-22 cycle update — Super Soul secondary-field reconciliation (069 / 074)
- [x] Reconciled **2** early/base-game thin records: 069 “Just win, okay?” and 074 “Goku! Time for dinner!”.
- [x] Filled Limit Burst type/effect fields and marked duration/stacking as **N/A** where no applicable timed/stacking mechanic is documented.
- [x] Preserved existing passive mechanics and acquisition data; no unsupported percentages or acquisition changes were introduced.
- [x] Added audit artifact: `docs/data/super-soul-secondary-field-reconciliation-069-074-2026-09-22.json`.
- [x] No canonical PQ relationship changed.
- [ ] CI/runtime: no successful workflow/check exposed.
- [ ] Next priority: continue the deterministic early/base-game thin census, prioritizing genuinely unresolved applicable mechanics.

### 2026-09-22 cycle update — Super Soul 245–246 research promotion
- [x] Promoted **Super Soul 245** ("This fight...is truly pointless...") and **246** ("I actually felt that one...") from `partially_verified` to `researched`.
- [x] Reconfirmed exact-name character, mechanics, Limit Burst, and PQ provenance: **245→PQ038**, **246→PQ012**.
- [x] Preserved unresolved engine-level timing/rate details and did not add unsupported reward probabilities or Ultimate-Finish requirements.
- [x] Updated and registered `docs/data/super-soul-242-through-246-provenance-audit-2026-09-22.json` in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **234 canonical Super Souls / 0 duplicate IDs**; both selected records are researched and retain canonical PQ edges.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: recompute the live Super Soul thin-system census with the established repository definition and select the next **4–12 highest-impact unresolved records**. Keep **232–236** as evidence-boundary records unless exact-name mechanics evidence becomes sufficient; otherwise move to another evidence-supported cluster.

### 2026-09-22 cycle update — Raid Super Souls 054/057/058/063 evidence strengthening
- [x] Strengthened **054, 057, 058, 063** with independent raid/effect evidence.
- [x] Promoted **057, 058, 063** to `verified_secondary` after corroborating Limit Burst/effect data.
- [x] Kept **054** `partially_verified` because Limit Burst evidence remains unresolved.
- [x] Refreshed the live Super Soul thin census: **234 records / 0 duplicate IDs / 182 strict-thin records** under the current eight-field definition.
- [x] Preserved evidence boundaries; no unsupported timing, probability, or engine-rate claims added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next: continue the deterministic partially-verified census with the next evidence-supported cluster; do not invent unresolved fields.

### 2026-09-22 cycle update — Super Souls 049/060 evidence strengthening
- [x] Added independent historical GameFAQs Super Soul guide evidence to **049** and **060**.
- [x] Promoted both to `verified_secondary`.
- [x] Preserved the documented effect-wording discrepancy on 060 and did not invent duration/stacking values.
- [x] Live census remains **234 / 0 duplicates / 182 strict-thin** under the current eight-field definition.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next: continue the deterministic partially-verified census, prioritizing high-source-count records with unresolved core fields; keep 034 evidence-bound until item-level mechanics are independently established.

### 2026-09-22 — Super Soul 191/194/196 evidence strengthening
- [x] Strengthened Super Souls **191, 194, 196** with exact-name/historical evidence.
- [x] Promoted all three to `verified_secondary`; preserved unresolved durations where evidence does not establish a separate timing rule.
- [x] Recorded non-stacking as N/A where directly supported.
- [x] Preserved 194's current +25% all-attacks value; historical +35% reports were not promoted.
- [x] Refreshed live census: **234 canonical / 0 duplicate IDs / 182 strict-thin**.
- [ ] CI/runtime: no successful workflow/check exposed.
- [ ] Next: continue deterministic partially-verified Super Soul reconciliation, prioritizing 032, 155, 173–175, 177, 179, 186, 187, 197, and 199.

### 2026-09-22 — Super Soul 174/177/186/199 evidence strengthening
- [x] Added independent historical/community evidence and promoted **174, 177, 186, 199** to `verified_secondary`.
- [x] Preserved unresolved duration/stacking fields where evidence did not establish an applicable value.
- [x] Live census: **234 canonical / 0 duplicate IDs / 182 strict-thin**.
- [ ] CI/runtime: no successful workflow/check exposed.
- [ ] Next: reconcile **155, 173, 175, 179, 187, 197, 032** using exact-name evidence and strict evidence boundaries.


### 2026-09-22 cycle completion — Super Soul 155/173/175/179/187/197 + 032 evidence boundary
- [x] Reconciled **155, 173, 175, 179, 187, and 197** with exact-name mechanics/acquisition evidence and promoted them to `verified_secondary`.
- [x] Preserved canonical PQ navigation: **155→PQ040, 173→PQ105, 175→PQ106, 179→PQ109, 187→PQ113, 197→PQ121**.
- [x] Preserved evidence boundary for **032→PQ185**: acquisition is corroborated, but item-level mechanics remain secondary/community-tested; no unsupported Limit Burst or engine timing was added.
- [x] Added/registered `docs/data/super-soul-155-173-175-179-187-197-032-evidence-reconciliation-2026-09-22.json`.
- [x] No canonical relationship identities, reward probabilities, or unsupported Ultimate-Finish requirements changed.
- [x] Live canonical Super Soul layer: **234 records / 0 duplicate IDs**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: recompute the live strict-thin census and select the next **4–12 highest-impact evidence-supported partially-verified records** with genuinely unresolved applicable fields. Preserve unresolved identity/evidence boundaries and do not manufacture values.

### 2026-09-22 cycle close — live Super Soul thin queue
- [x] Recomputed the live canonical Super Soul census: **234 records / 0 duplicate IDs / 182 strict-thin records** under the eight-field definition.
- [x] Selected the next evidence-supported queue from the live layer: **054** (4 missing fields), **034** (3; evidence boundary), **157**, **159**, **163**, **164** (2 each).
- [ ] Next: investigate **054** Limit Burst first; if evidence remains insufficient, preserve it and continue with **157/159/163/164**. Do not force 034 mechanics without exact-name evidence.

### 2026-09-22 — Super Soul 054 reconciliation
- [x] Reconciled **054 — “Leave my daddy alone!”** with independent raid evidence.
- [x] Populated the documented **3-second** Strike Skill boost duration and **ATK Up! Ki Auto-Recovery! Stamina Rec. SPD Down.** Limit Burst.
- [x] Promoted 054 to `verified_secondary`; preserved the description-vs-game-data percentage discrepancy and did not infer stacking, reward probability, or Ultimate-Finish requirements.
- [x] Added and registered `docs/data/super-soul-054-reconciliation-2026-09-22.json`.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue with **157, 159, 163, and 164**; keep **034** evidence-bound unless exact-name item-level mechanics evidence improves.

### 2026-09-22 — Super Souls 157/159/163/164 evidence reconciliation
- [x] Promoted **157, 159, 163, and 164** to `verified_secondary` after independent catalogue, character/stat-sheet, GameFAQs, and/or PQ evidence reconciliation.
- [x] Preserved null duration where effects are persistent/threshold-based rather than inventing finite timers; preserved unresolved stacking behavior.
- [x] Added and registered `docs/data/super-soul-157-159-163-164-reconciliation-2026-09-22.json`.
- [x] No canonical PQ relationship identities changed and no unsupported reward probabilities or Ultimate-Finish requirements were added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: inspect **034** evidence boundary, then recompute the strict-thin queue for the next 4–12 records.

### 2026-09-22 — Super Souls 167/169/170/171 evidence reconciliation
- [x] Promoted **167, 169, 170, and 171** to `verified_secondary` after exact-name catalogue and independent historical/PQ evidence reconciliation.
- [x] Preserved applicable-state/event semantics without inventing finite timers or stacking rules.
- [x] Added and registered `docs/data/super-soul-167-169-170-171-reconciliation-2026-09-22.json`.
- [x] No canonical PQ relationship identities changed; no unsupported reward probabilities or Ultimate-Finish requirements were added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: recompute the live strict-thin census and select the next evidence-supported batch; **034 remains an explicit evidence boundary** rather than a forced completion target.

### 2026-09-22 — Super Souls 055/061 evidence reconciliation
- [x] Promoted **055** and **061** to `verified_secondary` after independent catalogue/research evidence reconciliation.
- [x] Preserved 055's documented 30-second Ki Auto-Recovery and 061's five-stack accumulation without inventing unrelated timers or stacking rules.
- [x] Added and registered `docs/data/super-soul-055-061-reconciliation-2026-09-22.json`.
- [x] No canonical PQ relationship identities changed; no unsupported reward probabilities or Ultimate-Finish requirements were added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: recompute the strict-thin census and continue the deterministic low-field queue; **034 remains evidence-bound** until item-level mechanics are independently established.


### 2026-09-22 — Super Soul secondary-field reconciliation (024–031)
- Reconciled the missing **Limit Burst effect** field for **024–031** using exact-name Fandom and independent GameFAQs evidence.
- Populated all eight documented Limit Burst effects without altering acquisition routes, canonical PQ relationships, trigger/effect mechanics, durations, or stacking behavior.
- Added and registered `docs/data/super-soul-secondary-field-reconciliation-024-031-2026-09-22.json`.
- Refreshed the thin census to **234 canonical records / 0 duplicate IDs / 174 strict-thin records**.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next priority: recompute the live strict-thin queue and select the next **4–12 evidence-supported partially-verified records**; keep **034** evidence-bound unless exact-name item-level mechanics evidence improves.


### 2026-09-22 — Super Soul Limit Burst reconciliation (053 / 056 / 059 / 065)
- Reconciled **053, 056, 059, and 065** with exact-name Fandom and independent GameFAQs evidence.
- Populated their documented Limit Burst type/effect fields; duration and stacking remain unresolved where the evidence does not establish them.
- Added and registered `docs/data/super-soul-053-056-059-065-limit-burst-reconciliation-2026-09-22.json`.
- No canonical PQ relationship, acquisition identity, reward probability, or Ultimate-Finish requirement changed.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next task: continue the live strict-thin queue with the next evidence-supported partially verified records; preserve unresolved fields rather than guessing.


### 2026-09-22 queue correction — live Super Soul thin queue after 053/056/059/065
- [x] Recomputed the live canonical layer: **234 records / 0 duplicate IDs / 174 strict-thin records**.
- [x] Completed the bounded 024–031 and 053/056/059/065 Limit Burst field reconciliations without changing canonical PQ relationships.
- [ ] **034** remains an explicit evidence boundary (3 missing core fields); do not force completion.
- [ ] Next actionable queue: **032** if exact-name Limit Burst evidence is independently established; otherwise advance to the next evidence-supported partially-verified cluster, preserving unresolved fields.


### 2026-09-22 — Super Soul 202 (GAAAGH!) mechanics reconciliation
- Reconciled **Super Soul 202 — GAAAGH!** against exact-name catalogue/community evidence.
- Clarified that the **-25% guard-break time** is a duration modifier, not a timed buff; `duration` is therefore explicitly marked not applicable rather than left falsely unresolved.
- Recorded the stacking field as not reported as stackable; no stacking behavior was invented.
- Promoted the record to **verified_secondary** and added a bounded audit artifact.
- No acquisition route, reward tier, drop probability, or unrelated mechanic changed.
- Exact next task: continue the live partially-verified queue, preserving **032** as evidence-bound unless exact-name Limit Burst evidence is independently established.


### 2026-09-22 — Super Soul 201 (Alright! Let's go wreck some faces!) reconciliation
- Strengthened **Super Soul 201** with exact-name independent mechanics evidence.
- Confirmed the two separate +5% effects and their independent four-stack caps; the duration remains explicitly unresolved because consulted evidence does not establish a timed expiration.
- Promoted the record to **verified_secondary** and added a bounded audit artifact.
- No acquisition route, reward probability, Ultimate Finish condition, or unsupported duration was inferred.
- Exact next task: continue the live partially-verified queue; **032** remains evidence-bound for Limit Burst fields.


### 2026-09-22 — Super Souls 200 / 203–209 stacking semantics reconciliation
- Reconciled the unresolved `stacking_behavior` field for **200 and 203–209** against the maintained exact-name Super Soul catalogue.
- The catalogue does not report a numeric stack cap or stacking rule for these records, so the field is now explicitly **“Not reported as stackable”** rather than left null or assigned an invented value.
- Added and registered `docs/data/super-soul-200-203-209-stacking-reconciliation-2026-09-22.json`.
- No acquisition, reward probability, Ultimate Finish condition, duration, magnitude, or unrelated mechanic was changed.
- Exact next task: recompute the live strict-thin census and continue the next evidence-supported unresolved fields; preserve **032/034** as evidence boundaries where exact-name Limit Burst mechanics remain insufficient.


### 2026-09-22 — Super Souls 070–086 secondary-field reconciliation
- Reconciled **070, 071, 075, 076, 078, 080, 082, 083, 085, and 086** using exact-name player-facing catalogue/stat-sheet evidence.
- Populated the documented **Limit Burst types/effects** for all ten records.
- Populated explicit timed durations where the evidence states them: **075/076 = 10s; 082 = 20s; 083 = 10s; 085 = 15s; 086 = 15s**.
- Set `stacking_behavior` to **Not reported as stackable** where the source provides no stack cap; untimed records retain null duration rather than receiving invented timers.
- Added and registered `docs/data/super-soul-070-071-075-076-078-080-082-083-085-086-reconciliation-2026-09-22.json`.
- No acquisition, reward probability, Ultimate Finish condition, or unsupported duration was inferred.
- Exact next task: recompute the live strict-thin census and continue the next evidence-supported high-impact records; preserve **032/034** as evidence boundaries.


### 2026-09-22 — Super Souls 087–094 secondary-field reconciliation
- Reconciled **087–094** against exact-name Super Soul catalogue evidence.
- Populated all eight documented **Limit Burst** type/effect fields.
- Recorded `stacking_behavior` as **Not reported as stackable** because no numeric cap/rule is provided by the consulted exact-name catalogue.
- Left duration unresolved where no explicit timer is documented rather than inventing one.
- Added and registered `docs/data/super-soul-087-094-reconciliation-2026-09-22.json`.
- No acquisition route, reward probability, Ultimate Finish condition, or unsupported duration was inferred.
- Exact next task: recompute the live strict-thin census and continue the next evidence-supported unresolved cluster; preserve **032/034** as evidence boundaries.


### 2026-09-22 — Super Souls 095 / 144–150 secondary-field reconciliation
- Reconciled **095 and 144–150** against exact-name catalogue evidence, with independent corroboration for 095 and 148.
- Populated documented **Limit Burst** type/effect fields for all eight records.
- Recorded explicit **20-second durations for 144, 145, and 146** where the catalogue states them.
- Preserved unresolved timers elsewhere rather than promoting community-only measurements; recorded stacking as **Not reported as stackable** where no stack rule is documented.
- Added and registered `docs/data/super-soul-095-144-150-reconciliation-2026-09-22.json`.
- No unsupported acquisition probability, reward semantics, or mechanics were inferred.
- Exact next task: recompute the live strict-thin census and continue the next evidence-supported cluster; preserve **032/034** as evidence boundaries.


### 2026-09-22 — Super Souls 104 / 151–153 reconciliation
- Corrected **104 — Looks like I mixed up the capsules...**: exact-name evidence identifies its Limit Burst as **Revive Gauge Auto-Recovery!**, replacing the incorrect prior Auto Just Guard value.
- Reconciled **151–153**: 151 now records the documented **7-second** immunity window and Revive Gauge Auto-Recovery; 152 now records **Rush / ATK Up! Ki Auto-Recovery! Stamina Rec. SPD Down.**; 153 now records the documented **10-second** Health Auto-Recovery window and **Power / Auto Just Guard**.
- Preserved 152's stack-limited semantics without inventing a timer.
- Added and registered `docs/data/super-soul-104-151-153-reconciliation-2026-09-22.json`.
- **217 remains unresolved** because exact-name Limit Burst evidence was not independently established in this pass.
- Exact next task: continue the next evidence-supported unresolved cluster; preserve **032/034** as evidence boundaries.


### 2026-09-22 — Super Soul 218–219 mechanics/provenance reconciliation
- [x] Recomputed the live canonical Super Soul layer: **234 records / 0 duplicate IDs / 152 strict-thin records** under the current eight-field definition.
- [x] Reconciled **218 — “Pathetic”** and **219 — “Justice is nothing to me now.”** with exact-name catalogue and independent Xenoverse 2 evidence.
- [x] 218: populated **Vegeta (Super Saiyan God)**, **Ultra Pack 1**, Blazing Attack trigger, **+10% Strike Skills / +10% Ki Blast-based skills / +10% Ki restored**, **3-stack cap**, and **Auto Just Guard** Limit Burst.
- [x] 219: populated **Toppo**, **Ultra Pack 1**, below-50%-Health trigger, **+20% all damage / +15% defense / +10% stamina recovery speed**, guard-seal downside, and **Super Armor** Limit Burst.
- [x] Preserved canonical **PQ136** acquisition relationships and did not infer reward probability, Ultimate-Finish requirements, duration, or unsupported stacking semantics.
- [x] Added and registered `docs/data/super-soul-218-219-mechanics-reconciliation-2026-09-22.json`.
- [x] Both records remain strict-thin because 218 lacks an explicit duration and 219 lacks independently established duration/stacking semantics; the census was not artificially reduced.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: investigate the highest-impact one-field gaps with strong exact-name evidence — **191, 194, 192, and 196** — for explicit duration/stacking evidence; preserve unresolved fields if the evidence does not establish them, then continue with the next evidence-supported cluster.


### 2026-09-22 — Super Soul 192 stacking-field reconciliation
- [x] Reconciled **192 — “Get serious, would you?”** using the maintained exact-name Super Soul catalogue/stat sheet plus independent historical evidence.
- [x] Recorded `stacking_behavior: "Not reported as stackable"` because the documented effect set contains no stacking mechanic; no numeric cap was invented.
- [x] Preserved the 10-second Ki Blast-based-skill boost, -10 Stamina Just Guard effect, Auto Just Guard Limit Burst, and PQ117 acquisition relationship.
- [x] Live census after edit: **234 canonical / 0 duplicate IDs / 151 strict-thin records**.
- [x] Added and registered `docs/data/super-soul-192-stacking-reconciliation-2026-09-22.json`.
- [ ] Exact next priority: continue with the next evidence-supported unresolved Super Soul field; preserve genuinely unresolved duration/stacking semantics rather than manufacturing values.


### 2026-09-22 — Super Soul 191/194/196 duration reconciliation
- [x] Reconciled duration semantics for **191 — “Earth is in your hands now!”**, **194 — “Time to get serious, I guess.”**, and **196 — “You and this planet are history!”** against the maintained Super Soul catalogue.
- [x] 191: recorded the effect window as **while Hero's Flute is active**.
- [x] 194: recorded the movement-speed effect as tied to the **below-75%-Health condition**, without inventing a numeric duration.
- [x] 196: recorded the documented **30-second** temporary Ki Blast-based-skill boost.
- [x] Live census: **234 canonical / 0 duplicate IDs / 148 strict-thin records**.
- [x] Added and registered `docs/data/super-soul-191-194-196-duration-reconciliation-2026-09-22.json`.
- [ ] Next: continue the remaining evidence-supported thin-field cluster; do not manufacture stacking or duration values.


### 2026-09-22 — Super Soul 176/182/183/184/188/189 stacking reconciliation
- [x] Reconciled stacking fields for **176, 182, 183, 184, 188, and 189** as **Not reported as stackable** where the maintained effect sets document no stacking mechanic or numeric cap.
- [x] Preserved existing triggers and durations; no unsupported numeric stack caps were invented.
- [x] Live census: **234 canonical / 0 duplicate IDs / 142 strict-thin records**.
- [x] Added and registered `docs/data/super-soul-176-182-183-184-188-189-stacking-reconciliation-2026-09-22.json`.
- [ ] Next: continue evidence-rich unresolved Super Soul thin-field records.


### 2026-09-22 — Super Soul 177/186/197/199 reconciliation
- [x] Reconciled **177, 186, 197, and 199** duration/stacking fields using maintained catalogue evidence plus independent historical evidence.
- [x] 177: activation at 90 seconds; no separate expiration documented.
- [x] 186: activation at 60 seconds; no separate expiration documented.
- [x] 197: active while Health is above 75%.
- [x] 199: active while Super Saiyan 2 or Super Vegeta 2 is active.
- [x] Stacking recorded as **Not reported as stackable** for all four; no numeric caps invented.
- [x] Live census: **234 canonical / 0 duplicate IDs / 138 strict-thin records**.
- [x] Added and registered `docs/data/super-soul-177-186-197-199-reconciliation-2026-09-22.json`.
- [ ] Next: continue the remaining evidence-rich unresolved Super Soul fields.


### 2026-09-22 — Super Soul secondary-field queue update
- [x] Reconciled duration/stacking semantics for **049, 053, 056, 058, 059, 060, 063, and 065** using maintained exact-name catalogue evidence plus independent historical evidence.
- [x] Added explicit non-timed/condition-bound duration semantics where applicable and `Not reported as stackable` where no stacking rule/cap is documented.
- [x] Added and registered `docs/data/super-soul-049-053-056-058-059-060-063-065-secondary-field-reconciliation-2026-09-22.json`.
- [x] Refreshed live strict-thin census: **234 canonical / 0 duplicate IDs / 130 strict-thin records**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: recompute the live strict-thin queue and continue the next evidence-supported early/base-game/high-impact cluster; preserve **032/034** as evidence boundaries unless exact-name mechanics evidence improves.


### 2026-09-22 — Super Soul secondary-field queue update
- [x] Reconciled **044, 045, 046, 054, 055, 178, and 185** using exact-name and independent evidence.
- [x] Populated Limit Burst effects for **044–046** and explicit non-timed duration semantics for **178/185**.
- [x] Set **054/055** stacking behavior to **Not reported as stackable** without inventing numeric caps.
- [x] Added and registered `docs/data/super-soul-044-045-046-054-055-178-185-secondary-field-reconciliation-2026-09-22.json`.
- [x] Refreshed live strict-thin census: **234 canonical / 0 duplicate IDs / 123 strict-thin records**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: recompute the live strict-thin queue and continue the next evidence-supported one-field cluster; preserve genuine evidence boundaries and the known 044 wording conflict.


### 2026-09-22 — Super Soul duration queue update
- [x] Reconciled duration semantics for **070, 071, 078, and 080** using exact-name catalogue/stat-sheet evidence.
- [x] Added and registered `docs/data/super-soul-070-071-078-080-duration-reconciliation-2026-09-22.json`.
- [x] Refreshed live strict-thin census: **234 canonical / 0 duplicate IDs / 119 strict-thin records**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: recompute the live strict-thin queue and continue the next evidence-supported one-field cluster, starting with the strongest exact-name candidates.


### 2026-09-22 — Super Soul stacking queue update
- [x] Reconciled stacking fields for **154, 160, 162, and 165** as **Not reported as stackable** where the evidence documents no stacking mechanic/cap.
- [x] Added and registered `docs/data/super-soul-154-160-162-165-stacking-reconciliation-2026-09-22.json`.
- [x] Refreshed live strict-thin census: **234 canonical / 0 duplicate IDs / 115 strict-thin records**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue the next evidence-supported duration cluster, beginning with **156, 161, 166, 172**, while preserving genuine evidence boundaries.
### 2026-09-22 cycle update — Super Soul 061/096/097/098/099 duration-stacking reconciliation
- Live census before editing: **234 canonical / 0 duplicate IDs / 98 strict-thin records**.
- Bounded batch: **061, 096, 097, 098, and 099**.
- Research/evidence: maintained exact-name Super Soul catalogue, Madreag research corpus, and independent GameFAQs evidence for the throw-stack mechanics.
- Changes: 061 and 098 now explicitly preserve accumulated stacks without an undocumented expiration timer; 096 records its 3-second temporary window; 097 records its 30-second boost and once-only trigger; 099 records its battle-start-to-low-health state transition.
- Added/registered audit: `docs/data/super-soul-061-096-097-098-099-duration-stacking-reconciliation-2026-09-22.json`.
- Evidence limits preserved: no unsupported timer, stack reset, or new cap was inferred.
- Validation: **234 canonical / 0 duplicate IDs / 93 strict-thin records**; audit registration confirmed; JSON census refresh succeeded.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next batch: recompute the live strict-thin queue and continue the next evidence-supported cluster, prioritizing records with explicit duration/stacking evidence and preserving 032/034 as evidence boundaries.



### 2026-09-23 — Unified PQ reverse-index exact-pair census
- [x] Compared all canonical typed PQ relationship pairs in `docs/data/pq-reward-relationships.json` against `docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json` at exact target/PQ pair level.
- [x] Equipment was compared as the union of the unified `clothing` and `accessories` domains, preserving the domain distinction.
- [x] Live parity: **859 canonical / 859 unified / 0 missing / 0 extra / 0 duplicate projection pairs / 0 invalid PQ numbers / 0 invalid list fields**.
- [x] Current counts: **244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**.
- [x] Found and repaired deterministic audit metadata drift in `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json`: current equipment projection split is **84 clothing / 40 accessories = 124**; the prior 83/41 split was stale and is retained only in historical audit context.
- [x] No canonical relationship identities were changed; partial normalized-source omissions were not promoted into canonical relationships.
- [ ] Runtime execution of `scripts/validate_pq_unified_reverse_index.py` remains an environment gate; do not claim Python runtime or CI success from this structural connector census.
- [ ] Exact next task: scan remaining generated/reconciliation artifacts for stale **current-state** producer metadata/counts outside the already audited PQ relationship reports; repair only deterministic drift and preserve historical scope/count records before starting new provenance research.

### 2026-09-23 — Current PQ metadata drift repair
- [x] Scanned generated/reconciliation artifacts for stale current-state PQ relationship metadata.
- [x] Repaired `pq-cross-domain-status.json` target-normalization total **860 → 859**.
- [x] Repaired `pq-reward-relationships.json` current equipment **125 → 124** and current reconciliation **860 total / 125 equipment → 859 total / 124 equipment**.
- [x] Preserved historical 840/860/862 snapshots.
- [x] Updated `pq-current-baseline-field-drift-audit-2026-09-22.json` with the resolution.
- [x] Re-read edited JSON files and confirmed current metadata matches **859 / 244 / 151 / 124 / 247 / 86 / 7**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next priority: recompute the live strict-thin Super Soul census and continue the next evidence-supported high-impact one-field cluster; preserve **032/034** as evidence boundaries.

### 2026-09-23 — Super Soul 087–095 canonical secondary-field synchronization
- [x] Reconciled/synchronized canonical duration fields for **087–090 and 092–095**; 091 was already synchronized.
- [x] Set stacking behavior to **Not reported as stackable** for **087–095** where no documented stacking mechanic/cap exists.
- [x] Preserved 089's unresolved finite timer and did not invent stack caps.
- [x] Refreshed strict-thin census from **93 → 85**.
- [x] Registered canonical-sync metadata in the existing 087–095 reconciliation audit and refreshed the live thin-census artifact.
- [x] All nine batch records now have all eight strict-core fields populated.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next priority: recompute the strict-thin queue and continue the next evidence-supported early/base-game/high-impact cluster; preserve **032/034** as evidence boundaries.

### 2026-09-23 — Super Soul 051, 096–099 reconciliation
- [x] Reconciled duration/stacking fields for **051, 096, 097, 098, 099**.
- [x] Preserved evidence boundaries; only the explicit **3-stack** cap for 096 was promoted.
- [x] Strict-thin census reduced **85 → 80**.
- [x] Re-read canonical JSON and confirmed **234 records / 0 duplicate IDs / 80 strict-thin**.
- [ ] CI/runtime remains unavailable.
- [ ] Next: recompute strict-thin queue and continue the next evidence-supported early/base-game cluster; preserve **032/034** evidence boundaries.

### 2026-09-23 — Super Soul 100–107 reconciliation
- [x] Reconciled duration/stacking fields for **100–107**.
- [x] Preserved evidence boundaries; explicit **5-stack** cap retained only for 107.
- [x] Strict-thin multi-missing queue reduced **64 → 56**.
- [x] Canonical JSON validated: **234 records / 0 duplicate IDs**.
- [ ] CI/runtime remains unavailable.
- [ ] Next: recompute strict-thin queue and continue the next evidence-supported cluster; preserve **032/034** boundaries.

### 2026-09-23 — Super Soul 121–128 reconciliation
- [x] Reconciled duration/stacking fields for **121–128**.
- [x] Preserved evidence boundaries; no unsupported numeric timers or stacking caps introduced.
- [x] Strict-thin count reduced **56 → 48**.
- [x] Canonical JSON validated: **234 records / 0 duplicate IDs**.
- [ ] CI/runtime remains unavailable.
- [ ] Next: recompute strict-thin queue and continue the next evidence-supported cluster; preserve **032/034** boundaries.


### 2026-09-23 cycle update — Super Soul 129–143 secondary-field reconciliation
- [x] Recomputed the live canonical Super Soul layer after the prior 121–128 pass: **234 canonical records / 0 duplicate IDs / 60 strict-thin records** under the eight-field census definition.
- [x] Bounded batch: **Super Souls 129–143**.
- [x] Evidence: maintained exact-name Super Soul catalogue plus the independent Madreag Xenoverse 2 research corpus; current web corroboration also confirms the relevant exact-name mechanics, including the explicit stack cap for 133 and explicit timed effects for 134, 136, 140, and 142. cite
- [x] Changes: populated evidence-bounded stacking_behavior for all 129–143; retained explicit caps for **133 (5 stacks)** and **135 (10 Super-Attack-trigger stacks / 3 Ultimate-Attack-trigger stacks)**; recorded explicit durations for **134 (10s), 136 (20s), 140 (10s), and 142 (20s)**.
- [x] Evidence limits preserved: unresolved finite timers for the remaining records stay null; no unsupported timer, reset rule, or numeric stack cap was inferred.
- [x] Added audit artifact: docs/data/super-soul-129-143-secondary-field-reconciliation-2026-09-23.json.
- [x] Refreshed docs/data/super-soul-thin-census-2026-09-22.json to the live **60 strict-thin** count and recorded the remaining queue.
- [x] Commits: canonical d22392aa50d452d45c24d64b865543590959ae70; audit 8f31867b905357061fb18d129a3f44e7aaad6469; thin census ce30cba025c28b769d2f14fdfd1fdcfe09bb96fa.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next priority: recompute the live strict-thin queue before editing again, then take the strongest remaining evidence-rich cluster. Preserve **032/034** as evidence boundaries and keep indexed-only **158/232–236** separate from fully researched records.


### 2026-09-23 cycle update — Super Soul 148/150 and 155–187 secondary-field reconciliation
- [x] Live census before this bounded pass: **234 canonical / 0 duplicate IDs / 60 strict-thin records**; after synchronization: **58 strict-thin records**.
- [x] Bounded batch: **148, 150, 155, 157, 159, 163, 164, 167, 169, 170, 171, 173, 174, 175, 179, 187**.
- [x] Evidence: maintained exact-name Super Soul catalogue plus independent research/guide sources; exact-name current catalogue confirms **148 = 3s/5s**, **150 = 5s**, while the other selected records lack documented stack caps in the consulted evidence. cite
- [x] Changes: recorded **148 = 3 seconds after Super Attack / 5 seconds after Ultimate Attack** and **150 = 5 seconds**; set evidence-bounded stacking semantics for 155, 157, 159, 163, 164, 167, 169, 170, 171, 173, 174, 175, 179, and 187 to **Not reported as stackable**.
- [x] Evidence boundary preserved: the 30-second values for 159 and 174 are activation delays, not asserted buff durations; no unsupported duration was inferred for the remaining records.
- [x] Added audit: `docs/data/super-soul-148-150-155-187-secondary-field-reconciliation-2026-09-23.json`.
- [x] Refreshed live thin census to **58 strict-thin** records.
- [x] Commits: canonical `f37de0e94a504d576cf9cd1f6af510d9711a8f80`; audit `c8a2779236bace89e3dbe4686d3997d2c9aa1ccd`; thin census `6fb1775798e14ef211172a61549f4701b471b4ba`.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next priority: recompute the live queue before editing again. Highest-value unresolved areas are the remaining duration-only records (129–133, 135, 137–139, 141, 143, 147, 149, 155, 157, 159, 163, 164, 167, 169–171, 173–175, 179, 187, 201, 229, 237, 239, 240–241, 246), while **032/034** and indexed-only **158/232–236** remain explicit evidence boundaries.


### 2026-09-23 cycle update — Super Soul 129–143 duration reconciliation
- [x] Live census before editing: **234 canonical / 0 duplicate IDs / 58 strict-thin records**.
- [x] Bounded batch: **129–143**, targeting duration-only gaps while preserving prior stacking work.
- [x] Research/evidence: maintained exact-name Super Soul catalogue and corroborating character/form pages; the catalogue exposes the documented timed effects, while trigger/condition text was not converted into invented timers. cite
- [x] Changes: recorded **20-second** durations for **130, 132, 133, 135, 137, 138, 139, 141, and 143**.
- [x] Evidence limits preserved: **129 and 131 remain duration-unresolved**; no numeric timer was inferred for either.
- [x] Added audit: `docs/data/super-soul-129-143-duration-reconciliation-2026-09-23.json`.
- [x] Refreshed live thin census: **58 → 49 strict-thin records**.
- [x] Validation: canonical JSON reread/parsed; **234 records / 0 duplicate IDs**; census matches live strict-thin calculation.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Commits: canonical `9a721da0567ff91e773f32695f14fbf11422cfd7`; audit `b1027f7133177c0da8a7bf977ef211ca9de94398`; census `e1782aa168920525a981f83f2af286119df271dc`.
- [ ] Exact next batch: recompute the queue, then continue the strongest remaining duration-only cluster (**147, 149, 155, 157, 159, 163, 164, 167, 169–171, 173–175, 179, 187, 201, 229, 237, 239–241, 246**) before revisiting 032/034 or indexed-only 158/232–236.


### 2026-09-23 cycle update — Super Soul semantic-duration normalization
- [x] Live census before editing: **234 canonical / 0 duplicate IDs / 49 strict-thin records**.
- [x] Bounded batch: semantic-duration cleanup for **155, 157, 163, 164, 167, 169–171, 173, 175, 179, 201, 229, 237, 239, 246**.
- [x] Research/evidence: repository source URLs plus current maintained Super Soul references were checked. Evidence supports distinguishing permanent, condition-bound, and instantaneous effects from finite timed buffs. cite
- [x] Changes: populated the `duration` field with explicit semantic states where appropriate instead of leaving it null solely because the effect has no finite timer.
- [x] Evidence boundary preserved: **no numeric duration was invented**; 159/174 activation delays remain distinct from durations, and unresolved stack-expiry timers for 201/237/239 remain explicitly non-numeric.
- [x] Added audit: `docs/data/super-soul-semantic-duration-reconciliation-2026-09-23.json`.
- [x] Refreshed live census: **49 → 34 strict-thin records**.
- [x] Validation: canonical JSON reread/parsed; **234 records / 0 duplicate IDs**; census matches live strict-thin calculation.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Commits: canonical `56757428417d3cb04f227b13e396b74a9230633d`; audit `90c3fdda3f1938b763a3c7a9e7770fc42426e837`; census `3b046d7d117b2dd26ad5beccc9b7088d21edb72e`.
- [ ] Exact next batch: recompute the queue and prioritize the remaining **duration-only** records **129, 131, 147, 149, 159, 212, 216, 217, 218, 219, 229, 237, 239–241, 246** where evidence can distinguish permanent/instantaneous/finite behavior. Keep **032/034** and indexed-only **158/232–236** as explicit evidence boundaries.


### 2026-09-23 cycle update — Super Soul second semantic-duration pass
- [x] Recomputed live state: **234 canonical / 0 duplicate IDs / 34 strict-thin** before this pass.
- [x] Bounded batch: **129, 131, 147, 149, 159, 212, 216, 217, 218, 219, 240, 241**.
- [x] Populated duration semantics only where the record's trigger/effect structure supports it: instantaneous reward/resource events, permanent effects, condition-bound effects, or stack-lifetime statements. No unsupported finite timer was invented.
- [x] Preserved the important distinction that **159's 30-second value is an activation delay, not the buff duration**.
- [x] Refreshed census: **34 → 29 strict-thin**; canonical remains **234 / 0 duplicates**.
- [x] Validation: canonical JSON reread/parsed and live strict-thin count independently recomputed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Commits: canonical `b87f227ac130c25bbbcb75683e6318efd1364cae`; census `71eb757df10c3c744d69effb27a2a240f2e94551`.
- [ ] Exact next batch: remaining duration-only queue, beginning **242, 244, 246** plus any newly recomputed duration-only records; keep 032/034 and indexed-only 158/232–236 as evidence boundaries.


### 2026-09-23 cycle update — Super Soul stacking-semantic pass
- [x] Recomputed live state: **234 canonical / 0 duplicate IDs / 29 strict-thin** before editing.
- [x] Bounded batch: **210, 212, 240, 241, 242, 244, 246**.
- [x] Changes: recorded once-only/no-stacking semantics for 210 and 212; recorded `Not reported as stackable` for 240, 241, 242, 244, and 246. No unsupported numeric cap was inferred.
- [x] Refreshed census: **29 → 23 strict-thin**; canonical remains **234 / 0 duplicates**.
- [x] Validation: canonical JSON reread/parsed; live strict-thin calculation independently recomputed; stored census updated.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Commits: canonical `4d79ea0a4b87765438fb631d30d8c5681fc4f699`; census `9e0c5651b5617292bc2050106d305829545196fc`.
- [ ] Exact next priority: recompute queue again. Remaining concentrated gaps are **032/034**, indexed-only **158/232–236**, and records with missing Limit Burst effects/stacking fields; prioritize evidence-backed Limit Burst effect completion where the maintained source corpus already identifies the burst type.


### 2026-09-23 — TODO completion update — Super Soul 211–223 secondary-field reconciliation
- Recomputed the live canonical layer before editing: **234 canonical / 0 duplicate IDs / 23 strict-thin records**.
- Bounded batch: **211–223**, excluding the already evidence-bound indexed-only 232–236 cluster from mechanics inference.
- Reconciled evidence-backed secondary fields: 211 no-stacking; 212 Limit Burst effect; 213–215 no-stacking plus Limit Burst effects; 216 Limit Burst effect; 217 no-stacking; 218 Limit Burst effect; 219 no-stacking plus Limit Burst effect; 220–223 Limit Burst effects.
- Preserved evidence boundaries: **217 remains unresolved for Limit Burst fields**; no unsupported timer or numeric stack cap was invented; 032/034 and indexed-only 158/232–236 remain separate evidence boundaries.
- Added audit: `docs/data/super-soul-211-223-secondary-field-reconciliation-2026-09-23.json`.
- Refreshed `docs/data/super-soul-thin-census-2026-09-22.json`: **23 → 11 strict-thin records**.
- Validation: canonical record layer reread; 234 records and 0 duplicate IDs; stored thin census matches the recomputed 11-record queue.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next priority: recompute the live 11-record queue, then resolve the strongest evidence-supported remaining field(s), beginning with **174/187 duration** or **217 Limit Burst** if exact-name evidence is available. Keep **032/034**, **158**, and **232–236** as explicit evidence boundaries unless stronger item-level evidence appears.


### 2026-09-23 — TODO completion update — Super Soul 174/187 duration reconciliation
- [x] Recomputed live state before editing: **234 canonical / 0 duplicate IDs / 11 strict-thin records**.
- [x] Bounded batch: **174 and 187**, targeting the remaining duration-only gaps with evidence-backed semantic states.
- [x] **174**: recorded the documented 30-second post-battle-start activation delay separately from duration; no documented expiration was found, so the record now states post-delay/no documented expiration rather than inventing a timer.
- [x] **187**: recorded condition-bound Stamina-recovery semantics while Ki is maxed and explicitly noted that the temporary Ki Auto-Recovery component has no documented finite duration in the consulted evidence.
- [x] Added audit: `docs/data/super-soul-174-187-duration-reconciliation-2026-09-23.json`.
- [x] Refreshed live thin census: **11 → 9 strict-thin records**.
- [x] Validation: canonical JSON reread/parsed; **234 records / 0 duplicate IDs**; stored census matches the independently recomputed 9-record queue.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining queue: **032, 034, 158, 217, 232–236**. Keep 032/034 and indexed-only 158/232–236 as explicit evidence boundaries. **217 Limit Burst** remains the focused unresolved item-level gap; do not infer a burst from absence of evidence.


### 2026-09-23 — TODO completion update — Do or Die same-name collision boundary
- [x] Recomputed live canonical state: **234 records / 0 duplicate IDs / 9 strict-thin records**.
- [x] Investigated **Super Soul 158 — “Do or Die”** against the repository's PQ, skill, and Super Soul crosslink layers plus external PQ evidence.
- [x] Confirmed an important data-quality boundary: **PQ 49 is also the canonical source for the Super Skill “Do or Die.”** The Super Soul record must not inherit the skill's mechanics merely because the names and PQ endpoint collide.
- [x] Preserved the PQ↔Super Soul relationship for navigation, but added an explicit evidence note preventing mechanics/character-source promotion until item-level evidence distinguishes the records.
- [x] Added audit: `docs/data/super-soul-158-do-or-die-name-collision-audit-2026-09-23.json`.
- [x] Updated `docs/data/pq-super-soul-crosslink-report.json` with the evidence-boundary metadata and refreshed its recomputation date.
- [x] No unsupported mechanics were added to Super Soul 158.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining strict-thin queue: **032, 034, 158, 217, 232–236**. Continue with evidence-backed item-level Limit Burst research for **217** before revisiting unresolved indexed records.


### 2026-09-23 — TODO completion update — Super Soul 032 activation-state evidence refresh
- [x] Added current evidence showing **Super Soul 032** has a second activation/name-state after the user is KO'd: the displayed name changes to “Using this power should be no sweat for you guys.”
- [x] Preserved the evidence boundary: the source establishes the additional activation/name-state but does **not** establish its mechanical effect, so no Limit Burst or second-state effect was inferred.
- [x] Updated the canonical record's source list, version notes, and `last_verified` date.
- [x] Added audit: `docs/data/super-soul-032-activation-state-audit-2026-09-23.json`.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining strict-thin queue remains **032, 034, 158, 217, 232–236**. Next priority remains evidence-backed item-level research for **217 Limit Burst**; do not infer unresolved fields from absence of evidence.


### 2026-09-23 — TODO completion update — Super Soul 217 Limit Burst evidence boundary
- [x] Performed a focused web evidence pass for **Super Soul 217 — “Power! A lotta power! It's great!”**.
- [x] Added independent community evidence corroborating its +12 Ki/+12 Stamina utility and PQ 134 association.
- [x] No consulted source identified the Soul's **Limit Burst** effect or trigger.
- [x] Preserved the unresolved Limit Burst fields; no effect was inferred from absence of evidence.
- [x] Added audit: `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json`.
- [x] Updated `last_verified` and canonical source provenance.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] The former strict-thin **232–236** entries were resolved as duplicate/misattributed placeholders and removed from the canonical layer; the live strict-thin queue is **032, 034, 158, 217**.


### 2026-09-23 — Super Soul 034 provenance boundary refresh
- [x] Recomputed/inspected the remaining strict-thin boundary: **032, 034, 158, 217, 232–236**.
- [x] Bounded batch: **Super Soul 034 — “The final battle begins now.”**
- [x] Research/evidence: current Steam PQ186 evidence confirms the exact-name reward entry; official Nintendo FUTURE SAGA Chapter 4 documentation confirms the DLC contains **4 Super Souls** and **2 Parallel Quests**.
- [x] Strengthened canonical provenance and verification date without promoting mechanics or character-source claims that the evidence does not establish.
- [x] Updated `docs/data/super-soul-034-and-036-through-039-provenance-audit-2026-09-22.json` to record the four-Super-Soul DLC inventory as corroborating context and the remaining item-identity boundary.
- [x] Evidence limits preserved: trigger, effect, magnitude, duration, stacking, Limit Burst, exact reward tier, drop probability, and independently established character source remain unresolved for 034.
- [x] Validation: canonical JSON reread/parsed; record 034 remains present and partially_verified; no strict-thin reduction claimed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: canonical `0c98d6f4734865455ead5a7ed07ba7af6e164a24`; audit `89adf93a6ded0e838565bb92c1f86dd40808a6da`.
- [ ] Exact next priority: resolve **034 item identity/mechanics** only with item-level evidence (game-data identifier, exact-name mechanics source, or equivalent). Otherwise move to **232–236 identity resolution** and keep all unresolved boundaries explicit.


### 2026-09-23 — TODO completion update — Super Soul 232-236 identity correction
- [x] Audited queued **Super Souls 232-236** against current catalogue evidence, maintained PQ reward evidence, and existing canonical records.
- [x] Confirmed the numeric 232-236 positions collide with existing canonical raid Souls 040/036/041/042/043; the queued records were duplicate/misattributed placeholders.
- [x] Removed canonical records 232-236 and five erroneous PQ152-PQ155 Super Soul relationships; preserved prior provenance history.
- [x] Corrected PQ151-155 reward projections and reverse indexes to source-backed identities.
- [x] Added `docs/data/super-soul-232-through-236-identity-correction-2026-09-23.json` and live census `docs/data/super-soul-thin-census-2026-09-23.json`.
- [x] Live strict-thin queue is now **032, 034, 158, 217**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next work: continue 032/034/158/217 with exact-name/item-level evidence; do not recreate 232-236 without a distinct game-data identity key.


### 2026-09-23 — TODO checkpoint — remaining strict-thin Super Souls
- [x] Recomputed live queue after 232-236 correction: **032, 034, 158, 217**.
- [x] Completed a bounded exact-name evidence pass across all four remaining records without guessing missing mechanics.
- [x] Added docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json.
- [x] Preserved evidence boundaries for 032, 034, 158, and 217; no strict-thin reduction claimed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next priority: **034 item-level mechanics/Limit Burst**, then **217 Limit Burst**.

- [x] Continued the strict-thin **034** pass. Current PQ186 evidence establishes that the two exact-name Super Souls are “The final battle begins now.” and “I'll use this power to protect everyone!”; July 2026 community evidence distinguishes the former as **Fu's** Soul and the latter as Chronoa's. The canonical 034 record now uses **Fu (Ultra Supervillain)** as its character source, while all mechanics/Limit Burst fields remain unresolved because no authoritative item-level specification was found.
- [x] No mechanics were inferred from the community discussion; the record remains `partially_verified`.
- [ ] Next priority remains obtaining authoritative/item-level mechanics and Limit Burst data for **034**, then **217 Limit Burst**.

### 2026-09-23 cycle update — Super Soul 034 evidence-boundary correction
- [x] Re-ran the exact-name/item-level search for **034 — “The final battle begins now.”** using current September 2026 web evidence.
- [x] No authoritative item-level mechanics or Limit Burst evidence was found.
- [x] The prior community-based **Fu** character attribution was not independently substantiated by the fresh search, so the canonical `character_source` was restored to **unresolved** rather than retaining an unsupported attribution.
- [x] Updated `docs/data/super-souls-record-layer.json` and `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json`.
- [x] Validation: changed JSON parsed successfully; strict-thin queue remains **032, 034, 158, 217**; no unsupported mechanics or character source promoted.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: canonical `e3421e3db84fcc2f039f9d3ea7dab5d710189ae8`; checkpoint `8d70bb80f3244e0d353177a21f0c37a7885ef8d9`.
- [ ] Exact next batch: continue **034** only with item-level/game-data evidence; if still blocked, move to **217 Limit Burst** and preserve the 034 evidence boundary.

### 2026-09-23 cycle update — Super Soul 217 Limit Burst targeted refresh
- [x] Performed another exact-name **“Power! A lotta power! It's great!” + Limit Burst** search using current web evidence.
- [x] Fresh results continue to corroborate the Soul's +12 Ki/+12 Stamina/XXL utility and PQ134 association, but did **not** establish an exact Limit Burst effect or trigger. citeturn1reddit2
- [x] Updated `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json` with the fresh evidence boundary.
- [x] No generic/same-name Limit Burst was substituted; canonical 217 Limit Burst fields remain unresolved.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue **217** only with item-level/game-data or exact-name Limit Burst evidence; otherwise move to another high-impact deterministic Super Soul/index reconciliation rather than guessing.

### 2026-09-23 — TODO completion update — Super Soul 217 fresh evidence boundary
- [x] Recomputed live canonical state: **229 records / 0 duplicate IDs / 228 strict-thin records**.
- [x] Performed another exact-name/item-level Limit Burst search for **Super Soul 217**.
- [x] No new authoritative/item-level Limit Burst type, trigger, or effect evidence was found; generic utility discussion was not promoted into mechanics.
- [x] Appended the fresh evidence-boundary result to `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json`.
- [x] Preserved the unresolved Limit Burst fields and the existing strict-thin queue: **001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 067, 068, 069, 070, 071, 074, 075, 076, 078, 080, 082, 083, 085, 086, 087, 088, 089, 090, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next priority: leave 217 as an evidence boundary and continue the next deterministic high-impact reconciliation; do not infer unresolved fields.

### 2026-09-23 — TODO correction — strict-thin census definition
- [x] Corrected the prior cycle note's raw-null scan: it was not the repository's strict-thin definition and is superseded.
- [x] Authoritative live census remains **229 canonical / 0 duplicate IDs / 4 strict-thin**, queue **super-soul-032, super-soul-034, super-soul-158, super-soul-217**.
- [x] No canonical mechanics were changed by the raw-null scan.

### 2026-09-23 — TODO completion update — current PQ relationship producer-field drift
- [x] Audited remaining current-looking PQ relationship producer/status metadata.
- [x] Corrected the stale **854 / 146 Super Soul** current reconciliation in `docs/data/pq-reward-relationships.json` to **859 / 151**.
- [x] Corrected the stale **860** target-normalization current field in `docs/data/pq-cross-domain-status.json` to **859**.
- [x] Preserved dated historical counts unchanged.
- [ ] Recompute the live strict-thin Super Soul census and continue the strongest evidence-supported unresolved cluster.

### 2026-09-23 — TODO completion update — current PQ relationship producer-field drift
- [x] Audited remaining current-looking PQ relationship producer/status metadata.
- [x] Corrected stale **854 / 146 Super Soul** current reconciliation to **859 / 151**.
- [x] Corrected stale **860** target-normalization current field to **859**.
- [x] Preserved dated historical counts unchanged.
- [ ] Recompute the live strict-thin Super Soul census and continue the strongest evidence-supported unresolved cluster.


### 2026-09-23 — Strict-thin census/checkpoint consistency completion
- [x] Recomputed the authoritative Super Soul strict-thin census: **229 canonical / 0 duplicate IDs / 4 strict-thin** (**032, 034, 158, 217**).
- [x] Explicitly superseded the earlier raw-null/228-record scan; it is not the repository's strict-thin definition.
- [x] Audited all four remaining thin records without promoting unsupported mechanics.
- [x] Corrected the current strict-thin checkpoint's contradictory duplicate **034** entry; canonical 034 remains character_source **unresolved** and mechanics/Limit Burst unresolved.
- [x] Preserved all historical handoff/TODO entries rather than deleting stale history.
- [x] Validation: checkpoint parses and matches the authoritative stored queue; canonical Super Soul duplicate-ID count remains **0**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: one compact item-level/game-data evidence pass for **034**, then **217 Limit Burst** if 034 remains blocked; otherwise choose the next deterministic high-impact reconciliation rather than infer values.


### 2026-09-23 — Super Soul 034 item-level evidence boundary finalized
- [x] Completed the final compact repository evidence pass for **034**.
- [x] Confirmed Future Saga Chapter 4 evidence leaves 034 effect, trigger, item identifier, Limit Burst, and character source unresolved.
- [x] Did not infer Fu attribution from the surrounding PQ186 Fu costume inventory.
- [x] Updated the strict-thin checkpoint with the final evidence boundary.
- [x] Live strict-thin queue remains **032, 034, 158, 217**; canonical count **229**, duplicate IDs **0**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: **217 Limit Burst** item-level/game-data evidence pass; if blocked, move to deterministic high-impact reconciliation.


### 2026-09-23 — Super Soul 217 Limit Burst evidence boundary finalized
- [x] Completed the final compact item-level/game-data evidence pass for **217**.
- [x] Confirmed PQ134 exact-name reward identity; Limit Burst type/trigger/effect remain unsupported by checked repository item-level/canonical evidence.
- [x] Preserved the distinction between the Super Soul and the separate **Burst Charge** skill reward.
- [x] Updated the 217 evidence audit and handoff.
- [x] Live strict-thin remains **032, 034, 158, 217**; canonical Super Soul count **229**, duplicate IDs **0**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Next: choose a deterministic high-impact producer/index/projection reconciliation or evidence-supported multi-record batch rather than forcing unresolved thin fields.


### 2026-09-23 cycle update — PQ relationship coverage field clarification
- [x] Audited `docs/data/pq-cross-domain-status.json` against the canonical relationship audit and live producer census.
- [x] Found a deterministic semantic mismatch: `relationship_PQ_coverage` reported **182/186** because it was reflecting the reward-batch directory's missing PQ 1/12/13/14 files, while the canonical relationship layer itself covers **186/186** PQs.
- [x] Corrected the status projection to distinguish **canonical relationship coverage (186/186)** from **canonical reward-batch directory coverage (182/186)**; no relationship edge or source claim was added or removed.
- [x] Preserved the four missing batch files as an explicit scope limitation rather than treating them as missing canonical relationships.
- [x] Live relationship baseline remains **859 total = 244 skill + 151 Super Soul + 124 equipment + 247 character + 86 DLC + 7 farming**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- Commit: `f7b0a6b0da4961b7e67f51b014ac8aa2abf97135`.
- [ ] Exact next batch: continue the deterministic cross-domain coverage/projection audit, prioritizing a machine-checkable current-field mismatch rather than speculative gameplay data.


### 2026-09-23 cycle update — PQ relationship coverage status semantic repair
- Live canonical relationship coverage is **186/186 PQs**; the authoritative relationship layer is `docs/data/pq-reward-relationships.json`.
- Found and corrected a deterministic semantic mismatch in `docs/data/pq-cross-domain-status.json`: `relationship_PQ_coverage` was still reporting **182/186** because it reflected the partial reward-batch directory rather than canonical relationship coverage.
- Changed only the current status projection to **186/186** and preserved the partial research/source-layer limitation separately as **182/186**, missing batch files **PQ1, PQ12, PQ13, PQ14**.
- No canonical relationship edge, reward identity, or provenance claim was added or removed.
- Added and registered `docs/data/pq-relationship-coverage-status-repair-2026-09-23.json`.
- Validation target: **859 total canonical relationships = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; relationship coverage **186/186**; reward-batch directory coverage **182/186**.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next batch: continue the deterministic cross-domain coverage/projection audit from the live registry, prioritizing another machine-checkable current-field mismatch or a bounded multi-record navigation/projection repair; do not invent gameplay data.


### 2026-09-23 cycle update — Super Soul thin-census current projection repair
- [x] Recomputed the live canonical PQ→Super Soul relationship baseline against the authoritative relationship producer: **151 forward edges / 148 unique reverse targets**.
- [x] Found deterministic current-field drift in `docs/data/super-soul-thin-census-2026-09-23.json`: its `cross_domain.canonical_pq_super_soul_edges` still said **146**, reflecting the earlier 232–236 identity-correction snapshot rather than the current canonical relationship layer.
- [x] Corrected the live thin-census projection to **151/148** and clarified the next method; no canonical Super Soul relationship was added or removed.
- [x] Added and registered `docs/data/super-soul-thin-census-current-projection-repair-2026-09-23.json`.
- [x] Preserved the historical 146 after-count in the dated identity-correction artifact; historical records were not rewritten.
- [x] Validation: thin census parses; canonical Super Soul count remains **229**; strict-thin queue remains **032, 034, 158, 217**; current PQ→Super Soul baseline matches producer/status layers at **151 forward / 148 reverse**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue deterministic high-impact reconciliation outside the exhausted thin queue, prioritizing current projection/index drift or another reusable cross-domain/navigation repair; do not infer unresolved mechanics.


### 2026-09-23 cycle update — Super Soul crosslink count metadata repair
- [x] Live census found another stale current scalar: docs/data/pq-reward-relationships.json reported current_counts.super_soul = 146 while its canonical pq_rewards_super_soul relationship count and all current producer/status/navigation layers report 151.
- [x] Audited docs/data/pq-super-soul-crosslink-report.json: 151 forward edge records / 148 reverse endpoints; the relationship arrays themselves were already current.
- [x] Synchronized canonical current_counts.super_soul and the dedicated crosslink report current validation metadata to 151 forward / 148 reverse without changing relationship records.
- [x] Added and registered docs/data/pq-super-soul-crosslink-count-metadata-repair-2026-09-23.json.
- [x] Validation: JSON parses; canonical relationship count remains 859 total with 244/151/124/247/86/7 domain counts; Super Soul report arrays remain 151/148; no unresolved target routes or orphan reverse endpoints reported.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: audit remaining current metadata in dedicated cross-domain reports/producers for scalar-vs-array drift, then move to deterministic navigation/index repairs.


### 2026-09-23 correction — Super Soul 151/146 source-projection discrepancy discovered
- [x] Revalidated the prior cycle's Super Soul count repair at raw-array level and found the earlier assumption was too strong: `docs/data/pq-reward-relationships.json` currently contains **146** `pq_rewards_super_soul` entries in `verified_relationships`, and `docs/data/pq-super-soul-crosslink-report.json` contains **146 forward / 143 reverse** entries.
- [x] At the same time, `pq-page-consumer-audit.json`, `pq-endpoint-navigation-validation.json`, and other current reconciliation metadata declare **151 forward / 148 reverse**. This is a genuine unresolved **five-edge source/projection discrepancy**.
- [x] Corrected the live reconciliation note and crosslink validation status to prevent the prior cycle's mistaken 151 promotion from being treated as proven canonical array state.
- [x] Added `docs/data/pq-super-soul-crosslink-count-discrepancy-correction-2026-09-23.json` documenting the discrepancy and evidence boundary.
- [x] No relationship edge was added, deleted, renamed, or inferred.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: identify the five Super Soul pairs represented by the 151/148 consumer audits but absent from `verified_relationships`, compare them against canonical PQ structured rewards and source-backed records, then either add only evidence-backed relationships or correct stale consumer metadata.


### 2026-09-23 cycle update — PQ151 Super Soul consumer parity + 151/148 metadata correction
- [x] Identified the two concrete canonical/structured Super Soul parity gaps: **PQ151 → “I'll never forgive you!”** and **PQ151 → “I'm not gonna die until I defeat you!”**.
- [x] Added both exact reward targets to `docs/data/parallel-quests-record-layer.json` from the already-present general PQ151 rewards and source-backed canonical relationships; no Super Soul IDs, gates, probabilities, or mechanics were inferred.
- [x] Recomputed the real consumer contract: **146 canonical pairs / 146 structured pairs / 0 missing / 0 extra**.
- [x] Corrected stale `151/148` Super Soul counts in the consumer/navigation validation layer to the verified current **146 forward / 143 reverse** state.
- [x] Added `docs/data/pq-super-soul-consumer-parity-repair-2026-09-23.json` documenting the exact repair.
- [x] Canonical relationship edge count remains **859**; no canonical relationship rows were modified.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: inspect remaining cross-domain validation files for stale Super Soul 151/148 projections, then continue deterministic navigation parity repairs.


### 2026-09-23 — Verified Super Soul source baseline propagated
- [x] Confirmed authoritative `verified_relationships`: **854 total / 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; Super Soul reverse targets **143**.
- [x] Propagated the verified 854/146/143 baseline into current status, audit, producer, presentation, reference-page, and validator layers.
- [x] Updated the current consumer-baseline correction artifact; prior 859/151 values remain historical where explicitly preserved.
- [x] No canonical relationship rows were invented or deleted.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: scan remaining current-looking artifacts for stale **859/151** projections and reconcile deterministic fields only.


### 2026-09-23 cycle update — Deterministic current PQ navigation/reverse-index baseline propagation
- [x] Scanned remaining current-looking PQ consumer/navigation artifacts for stale 859/151 projections after the verified 854/146 canonical source correction.
- [x] Synchronized current/live fields in endpoint navigation, endpoint identity resolution, cross-database reverse consistency, endpoint alias/granularity, and the superseded thin-census projection.
- [x] Updated the current-baseline single-source reconciliation artifact so its authoritative live baseline is 854 / 244 / 146 / 124 / 247 / 86 / 7 and its stale-current field queue is empty; dated 859/151/860/862/840 evidence remains historical where explicitly retained.
- [x] Revalidated the authoritative docs/data/pq-reward-relationships.json raw array: 854 total, including 146 pq_rewards_super_soul relationships.
- [x] Preserved exact-pair evidence boundaries; no relationship row was invented, deleted, renamed, or inferred in this cycle.
- [ ] Runtime/CI remains unavailable; no executable validation success claimed.
- [ ] Exact next priority: scan the remaining generated/current-facing PQ presentation and reverse-index artifacts for any stale 859/151 scalar or prose explicitly labeled current/live, then continue reusable cross-database navigation parity repairs. Preserve historical snapshots.


### 2026-09-23 cycle update — Current PQ presentation/validator drift repair
- [x] Repaired remaining explicitly current-facing PQ summary/reference/unified-reverse-index/cross-domain/skill-acquisition audit fields to the authoritative 854/146 baseline.
- [x] Updated `scripts/validate_pq_current_consumer_baseline.py` so current validation no longer consumes the superseded 859/151 historical correction artifact as its expected baseline.
- [x] Updated `docs/Parallel-Quest-Audit.md` current structured coverage statement to 854 relationships; historical evidence remains preserved.
- [x] No canonical relationship rows were added, deleted, renamed, or inferred.
- [ ] Runtime/CI remains unavailable; no executable validation success claimed.
- [ ] Exact next priority: inspect remaining current-facing PQ page templates and DLC requirement presentation for one-way navigation, stale scalars, and endpoint identity drift; repair deterministic navigation gaps only.


### 2026-09-23 cycle update — PQ explorer deep-link/DLC navigation repair
- [x] Fixed `docs/Parallel-Quests-All.html` inbound `?q=` deep-link initialization.
- [x] Routed PQ→DLC links through the query-aware `/Search/` surface instead of a non-filtering `DLC-Overview/?q=` destination.
- [x] Added validator checks for PQ explorer query deep-link support and the new PQ→DLC search destination.
- [x] Recorded the repair in the PQ explorer/direct-template navigation audits.
- [ ] Runtime/CI remains unavailable; no executable validation success claimed.
- [ ] Exact next priority: inspect character and Super Soul reverse-navigation destinations for the same query/deep-link contract and repair deterministic gaps.


### 2026-09-23 cycle update — Dedicated Character/Super Soul reverse-navigation parity
- [x] Changed PQ→Character links to the dedicated `/Characters-All/?q=` explorer.
- [x] Changed PQ→Super Soul links to the dedicated `/Super-Souls-All/?q=` explorer.
- [x] Added validator checks for both dedicated reverse-navigation destinations and recorded the repair in the PQ explorer audit.
- [x] No canonical relationship rows were changed.
- [ ] Runtime/CI remains unavailable; no executable validation success claimed.
- [ ] Exact next priority: inspect Equipment/DLC reverse-navigation presentation and generated content pages for one-way destinations, then repair deterministic navigation gaps.


### 2026-09-23 — TODO completion update — Equipment/DLC reverse-navigation presentation
- [x] Audited `docs/Equipment-All.html` for one-way DLC/PQ navigation and repaired the deterministic DLC presentation gap by adding local-search links for populated DLC provenance values.
- [x] Audited `docs/DLC-Overview.md` and added player-facing reverse navigation from all canonical DLC identities to their canonical PQ sets through the local PQ explorer.
- [x] Added `docs/data/equipment-dlc-reverse-navigation-presentation-audit-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the canonical-source-of-truth boundary; no relationship or gameplay data was inferred.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next priority: continue published character/DLC presentation-index and generated-content navigation audits, then resume deterministic DLC content-domain reconciliation.


### 2026-09-23 — TODO completion update — Super Soul 036–047 secondary fields
- [x] Recomputed the live thin-system census and bounded the next evidence-supported batch to Super Souls 036–047.
- [x] Filled missing DLC requirement fields with `None identified` where no paid DLC requirement is established.
- [x] Reconciled stacking fields to `Not reported as stackable` without inventing numeric caps.
- [x] Added/registered `docs/data/super-soul-036-through-047-secondary-field-reconciliation-2026-09-23.json`.
- [x] Refreshed verification dates and added Free Update evidence.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: recompute the remaining 24-record thin queue; prioritize 032, 034, 158, and 217, then continue the strongest evidence-supported gaps.

### 2026-09-23 — TODO completion update — DLC → character navigation
- [x] Audited remaining published character/DLC presentation consumers after the Equipment/DLC navigation repair.
- [x] Added deterministic DLC headline-character → local character Search navigation to `docs/DLC-Overview.md` using the existing identity bridge.
- [x] Preserved both unresolved Chapter 4 character labels as unresolved; no nearby identity was substituted.
- [x] Extended `scripts/validate_published_character_dlc_navigation.py` and updated its audit report.
- [x] No canonical DLC or character relationship was added or modified.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: continue deterministic DLC content-domain reconciliation, prioritizing pack-level content matrices and missing downstream record links.


### 2026-09-23 — TODO completion update — DLC reverse validator schema repair
- [x] Audited the DLC presentation validator against the live reverse-index schema.
- [x] Repaired the reverse-navigation completeness check to use `records[].dlc_id` rather than nonexistent `reverse_index` data.
- [x] Added explicit canonical-target coverage reporting; current projection covers **20/20** canonical DLC identities.
- [x] Updated the DLC presentation consumer audit with the repair.
- [x] No canonical DLC identity or PQ relationship changed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: reconcile existing DAIMA and HERO OF JUSTICE Pack 2 content projections against concrete downstream records.


### 2026-09-23 — TODO completion update — DLC pack record-link integrity
- [x] Audited downstream equipment records for DAIMA and HERO OF JUSTICE Pack 2.
- [x] Corrected 7 malformed pq_sources identifiers to canonical pq-NNN IDs.
- [x] Recorded the repair in docs/data/dlc/dlc-content-link-audit.json.
- [x] Preserved the evidence boundary; no new DLC/content relationship was inferred.
- [ ] Non-PQ pack inventory remains unresolved and must be reconciled from concrete canonical records.


### 2026-09-23 — TODO completion update — DLC pack content matrix / concrete downstream anchors
- [x] Audited the remaining unresolved DAIMA and HERO OF JUSTICE Pack 2 non-PQ content projections against the live canonical PQ/reward/equipment/character layers and official publisher announcements.
- [x] Added `docs/data/dlc/dlc-pack-content-matrix-2026-09-23.json` with bounded, source-backed pack scope, canonical PQ sets, concrete downstream navigation anchors, and explicit unresolved inventory domains.
- [x] Preserved the paid-vs-free DAIMA boundary: the official DAIMA announcement separately identifies the paid pack and its free update content.
- [x] Preserved the existing evidence boundary: PQ-backed anchor counts are navigation evidence, not a complete DLC ownership manifest.
- [x] Registered the matrix in `docs/data/pq-cross-domain-index.json` and linked it from the DLC content-link audit.
- [x] Validation by live re-fetch: matrix JSON structure is valid; DAIMA resolves to PQ179–181 and HERO OF JUSTICE Pack 2 resolves to PQ159–162; canonical DLC identity layer remains 20 records / 86 PQ→DLC edges; no canonical relationship row changed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: use the new matrix to reconcile the strongest concrete non-PQ DAIMA/HOJ2 downstream record cohort, starting with existing equipment/accessory records and then skills/Super Souls; do not fill unresolved raid/lobby/stage inventories without record-level evidence.


### 2026-09-23 — TODO completion update — DAIMA downstream accessory normalization readiness
- [x] Reconciled the DAIMA Pack's concrete equipment/accessory downstream layer: equip-098–equip-105 already provide exact source-backed costume/accessory identities for PQ179–181.
- [x] Identified four exact-name accessory namespace promotions: equip-099 → candidate acc-071, equip-101 → acc-072, equip-104 → acc-073, equip-105 → acc-074.
- [x] Added docs/data/dlc/daima-accessory-normalization-audit-2026-09-23.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Extended the DAIMA pack matrix with concrete combined-layer record IDs and accessory promotion candidates.
- [x] Preserved the no-duplicate/no-inference rule: this is namespace normalization of already existing exact identities, not creation of new content.
- [ ] Exact next batch: perform the four accessory promotions atomically across equipment-accessories-record-layer.json, accessory-pq-canonical-bridge.json, pq-accessory-crosslink-report.json, reverse indexes, aliases, and presentation consumers; then validate all endpoint navigation before moving to the next pack/domain.


### 2026-09-23 — TODO completion update — DAIMA accessory canonicalization
- [x] Promoted the four exact-name DAIMA accessory identities into canonical `acc-071`–`acc-074` in `equipment-accessories-record-layer.json`.
- [x] Retained `equip-099`, `equip-101`, `equip-104`, and `equip-105` as legacy equipment-layer alias projections pointing to the canonical accessory IDs.
- [x] Updated `accessory-pq-canonical-bridge.json` and resolved `pqacc-034`–`pqacc-037` to canonical IDs.
- [x] Updated `accessory-pq-canonical-remaining.json`, regenerated `pq-accessory-crosslink-report.json`, and expanded the canonicalization audit/census.
- [x] Post-write target state: 74 canonical accessory IDs, 32 accessory PQ forward/reverse edges, 12 unresolved research bridge entries; no duplicate canonical IDs introduced.
- [ ] Exact next batch: run the repository's accessory/presentation validators against the normalized graph; then reconcile the next unresolved concrete DAIMA/HOJ2 skill or Super Soul cohort.


### 2026-09-23 — TODO completion update — DAIMA / HERO OF JUSTICE Pack 2 skill and Super Soul anchors
- [x] Audited all concrete canonical skill and Super Soul PQ edges for PQ159–162 and PQ179–181.
- [x] Recorded **13 skill edges** and **7 Super Soul edges** as concrete downstream navigation anchors.
- [x] Added `docs/data/dlc/daima-hoj2-skill-super-soul-downstream-audit-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Expanded the DLC content matrix with individual canonical skill and Super Soul IDs for both packs.
- [x] Preserved the ownership boundary: these are PQ-linked navigation anchors, not a complete DLC inventory and not evidence for free-update DAIMA ownership.
- [ ] Exact next batch: reconcile the remaining concrete HOJ2/DAIMA non-PQ skill/Super Soul inventory against canonical records, prioritizing records advertised by the official pack scope but not yet represented by PQ-backed anchors.


### 2026-09-23 — TODO completion update — official DAIMA / HOJ2 skill and Super Soul count reconciliation
- [x] Reconciled DAIMA Pack against publisher-listed counts: **6 moves / 6 canonical skills** and **2 Super Souls / 2 canonical Super Souls**.
- [x] Reconciled HERO OF JUSTICE Pack 2 against publisher-listed counts: **7 moves / 7 canonical skills** and **5 Super Souls / 5 canonical Super Souls**.
- [x] Added `docs/data/dlc/daima-hoj2-official-skill-super-soul-count-reconciliation-2026-09-23.json` with official-source URLs and exact canonical IDs.
- [x] Registered the count audit and updated the DLC content matrix.
- [x] Closed the skill/Super Soul completeness gap for these two paid packs; no unsupported records were invented.
- [ ] Exact next batch: move to the remaining paid-DLC content domains (HOJ2 costumes/accessories and stage/missions, then DAIMA non-skill/Super-Soul inventory) using official count checks and canonical cross-links.


### 2026-09-23 — TODO completion update — HERO OF JUSTICE Pack 2 paid content reconciliation
- [x] Reconciled the Pack 2 paid costume/accessory inventory against the official count of 5 and five exact canonical PQ-backed records: acc-069 Dr. Hedo Hood, acc-060 Red Ribbon Army Helmet, equip-067 Red Ribbon Soldier 94 Clothes, equip-068 Dr. Hedo Suit, and acc-061 Gohan (Beast) Wig.
- [x] Reconciled the official 1 new stage identity as Red Ribbon Army (Yard) at pack scope without creating a synthetic stage record.
- [x] Reconciled the official 2 Extra Missions count at pack scope without creating synthetic mission IDs because no dedicated extra-mission record layer exists.
- [x] Preserved the paid/free boundary: Cell Max raid costume/accessory rewards remain outside the paid five-item Pack 2 inventory.
- [x] Added and registered docs/data/dlc/hero-of-justice-pack-2-paid-content-reconciliation-2026-09-23.json and updated the DLC content matrix/link audit.
- [x] Existing skill/Super Soul count reconciliation remains 7/7 skills and 5/5 Super Souls.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue DAIMA paid non-skill/Super-Soul inventory reconciliation, starting with the concrete costume/accessory cohort and official pack-level scope; do not merge free-update records or invent unresolved raid/lobby/stage entries.


### 2026-09-23 — TODO completion update — DAIMA paid costume/accessory completeness
- [x] Reconciled the official DAIMA Pack **8 Costumes/Accessories** count against all eight canonical paid downstream identities: equip-098, acc-071/equip-099 alias, equip-100, acc-072/equip-101 alias, equip-102, acc-073/equip-104 alias, equip-103, and acc-074/equip-105 alias.
- [x] Confirmed the four costume identities: SS4 Goku (DAIMA) Suit, SS3 Vegeta (DAIMA) Battle Suit, Glorio's Clothes, and Panzy's Clothes.
- [x] Confirmed the four canonical accessory identities: SS4 Goku (DAIMA) Wig & Tail, SS3 Vegeta (DAIMA) Wig, Glorio Wig, and Panzy Wig.
- [x] Added docs/data/dlc/daima-paid-costume-accessory-completeness-reconciliation-2026-09-23.json and registered it in the PQ cross-domain index.
- [x] Removed the resolved paid costume/accessory gap from the DAIMA pack matrix while preserving unresolved free-update/loading-screen/raid/lobby domains.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue remaining DAIMA paid domains only where concrete canonical records and official scope permit; prioritize loading-screen completeness if a canonical illustration layer can be reconciled, otherwise audit the next unresolved paid content domain without crossing into free-update ownership.


### 2026-09-23 — TODO completion update — DAIMA paid illustration scope
- [x] Reconciled the official DAIMA Pack paid illustration/loading-screen count as **8** using publisher/platform listings.
- [x] Verified that the live repository currently has **no dedicated canonical illustration/loading-screen record layer**; no synthetic illustration IDs or identities were created.
- [x] Documented the paid/free boundary: Bandai Namco separately identifies free-update loading screens and lobby items, so those are not merged into the paid eight.
- [x] Added and registered `docs/data/dlc/daima-paid-illustration-scope-reconciliation-2026-09-23.json`.
- [ ] Build a canonical illustration/loading-screen record layer once individual eight paid identities can be source-backed; then cross-link each record to DAIMA Pack/PQ acquisition data.
- [ ] CI/runtime remains unavailable; no CI success claimed.


### 2026-09-23 — TODO completion update — accessory/presentation validation after DAIMA canonicalization
- [x] Validated the live accessory canonical layer: **173 total equipment records / 74 canonical accessories**, with zero duplicate accessory IDs or canonical names.
- [x] Validated the PQ accessory presentation report: **32 forward / 32 reverse edges**, zero duplicate forward edges, zero stale endpoints, zero null PQ edges, and 12 unresolved research records intentionally retained.
- [x] Confirmed DAIMA canonical accessory endpoints `acc-071`–`acc-074` resolve to PQ179–181 with exact identities and no duplicate canonical IDs.
- [x] Refreshed `docs/data/accessory-canonicalization-audit.json` with the live 74-record validation summary.
- [x] Added `docs/data/accessory-presentation-validation-2026-09-23.json` as the durable validation result.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: reconcile the next unresolved concrete DAIMA/HOJ2 paid content domain, preserving canonical cross-navigation and refusing unsupported reward/ownership inference.


### 2026-09-23 — TODO completion update — HERO OF JUSTICE Pack 2 stage/Extra Mission evidence
- [x] Reconciled the official Pack 2 scope of **1 stage and 2 Extra Missions** using Bandai Namco's current DLC listing.
- [x] Confirmed the stage identity **Red Ribbon Army (Yard)** at pack scope without inventing a stage record.
- [x] Added source-backed evidence for **Extra Mission 14 — The Activation of Cell Max**; because no dedicated Extra Mission record layer exists, the identity remains evidence-only and is not promoted to a synthetic canonical record.
- [x] Added `docs/data/dlc/hero-of-justice-pack-2-stage-mission-evidence-2026-09-23.json` and linked it from the DLC pack matrix.
- [x] Preserved the unresolved mission/stage record-layer tasks rather than fabricating IDs or fields.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the remaining concrete paid-DLC inventory gap, with illustration/loading-screen identities as the next evidence-led domain where individual records can be source-backed.


### 2026-09-23 — TODO completion update — DAIMA / HERO OF JUSTICE Pack 2 playable-character count reconciliation
- [x] Reconciled official paid-DLC playable-character counts against the existing canonical character layer: DAIMA **2/2** and HERO OF JUSTICE Pack 2 **3/3**.
- [x] Exact canonical identities confirmed: DAIMA — SS4 Goku (DAIMA), SS3 Vegeta (DAIMA); HOJ2 — Gohan (Beast), Orange Piccolo, Piccolo (Power Awakening).
- [x] Added `docs/data/dlc/daima-hoj2-playable-character-count-reconciliation-2026-09-23.json` and registered the reconciliation in the DLC pack matrix.
- [x] Preserved the evidence boundary: count reconciliation does not infer additional DLC ownership, character variants, or PQ reward relationships.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: reconcile the next concrete paid-DLC domain with an existing canonical record layer; prioritize a deterministic cross-domain completeness gap over creating a new illustration layer without individually source-backed identities.


### 2026-09-23 — TODO completion update — HERO OF JUSTICE Pack 2 paid illustration scope
- [x] Reconciled the official **15 paid illustrations** count from Steam, Nintendo, and Bandai Namco's Xenoverse 2 DLC listing.
- [x] Confirmed the live repository still has no dedicated canonical illustration/loading-screen record layer; no synthetic illustration IDs, names, acquisition routes, or PQ reward slots were created.
- [x] Added `docs/data/dlc/hero-of-justice-pack-2-paid-illustration-scope-reconciliation-2026-09-23.json`, registered it in `docs/data/pq-cross-domain-index.json`, and updated the DLC pack/content-link matrices.
- [x] Preserved the paid-content boundary; this count does not absorb unrelated/free-update loading screens.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the next concrete paid-DLC gap backed by an existing canonical record layer; do not create an illustration layer until individual identities are source-backed.


### 2026-09-23 — TODO completion update — Time Patrol Support Pack paid-content reconciliation
- [x] Reconciled the separately sold Time Patrol Support Pack storefront content: **10 Super Attacks, 3 Ultimate Attacks, 8 costumes, 2 accessories, 3 Super Souls, 1 CC Mascot, and the listed consumable quantities**.
- [x] Cross-linked exact existing canonical records: equip-024 Battle Suit (Bardock), equip-087 Frieza's Suit (Final Form), acc-038 Frieza's Head (Final Form), acc-039 Korin Wig with Ears & Tail, plus super-soul-029 The ultimate power is mine!.
- [x] Reconciled six existing PQ skill endpoints from the advertised skill list without treating PQ provenance as exclusive DLC ownership.
- [x] Added docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved the architectural boundary: Time Patrol Support Pack is not inserted into the PQ-requirement canonical DLC identity layer because it is a separately sold value pack rather than an existing pq_requires_dlc endpoint.
- [ ] Two advertised Super Souls, six advertised costume names, several advertised skills, and Puar remain unresolved at canonical-record level; no IDs were invented.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: resolve the remaining Time Patrol Support Pack canonical identity gaps only with record-level evidence, beginning with the two unresolved Super Souls and unmatched costume records; then return to the DAIMA/HOJ2 unresolved non-PQ domains.


### 2026-09-23 — TODO completion update — Time Patrol Support Pack Super Soul identity promotion
- [x] Promoted the two previously unresolved pack Super Souls to canonical records: `super-soul-247` **I hope you're reborn as someone good this time.** and `super-soul-248` **You must die by my hand!**.
- [x] Added source-backed mechanics/provenance for both; preserved ordinary in-game acquisition routes instead of treating the paid pack as exclusive ownership.
- [x] Added and registered `docs/data/dlc/time-patrol-support-pack-super-soul-identity-reconciliation-2026-09-23.json`.
- [x] Canonical layer now represents all 3 officially advertised Time Patrol Support Pack Super Souls.
- [ ] Remaining Time Patrol Support Pack gaps: six costume names, several advertised skill endpoints, and Puar/CC Mascot; no unsupported IDs will be inferred.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: reconcile the six unmatched costume names against canonical equipment aliases/source records, then resolve remaining skill and Puar gaps only where dedicated canonical layers/evidence exist.


### 2026-09-23 — TODO completion update — Time Patrol Support Pack costume identity audit
- [x] Audited all **6 previously unmatched costume names** from the official Time Patrol Support Pack storefront scope.
- [x] Confirmed **Vegito Clothes → equip-078** as an exact existing canonical equipment identity through the PQ59 reward/equipment crosslink layers.
- [x] Confirmed **Gogeta Clothes → PQ57** and **Broly Clothes → PQ47** as source-backed repository reward identities, while preserving them as non-canonical because no exact canonical equipment records currently exist.
- [x] Confirmed **Future Trunks' Clothes (Super)** exists in equipment-catalog-index.json, but no exact canonical record was found; it was not aliased to another Trunks outfit.
- [x] Confirmed official storefront identities for **Master Korin's Suit** and **Orange Star High School Outfit**, while preserving them as evidence-only because no exact canonical equipment/catalog records were found.
- [x] Added docs/data/dlc/time-patrol-support-pack-costume-identity-reconciliation-2026-09-23.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Preserved the equipment architecture boundary: the live legacy equipment layer ends at equip-140; no equip-141+ IDs were invented.
- [x] Preserved evidence limits: no reward probability, drop slot, shop rotation, stats, restrictions, or exclusive-DLC ownership was inferred.
- [x] Validation: audit JSON parses; official costume count remains 8; batch exact canonical match is 1; five target identities remain without exact canonical records; cross-domain audit registration is present.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: resolve the five remaining Time Patrol Support Pack costume identities only when individually source-backed and compatible with the existing equipment architecture; then continue unmatched pack skills/Puar without inventing IDs.


### 2026-09-23 — TODO completion update — Time Patrol Support Pack skill identity reconciliation
- [x] Audited all **13 advertised Support Pack attacks** against the live canonical skill layer and official Steam/Nintendo/Xbox pack scope.
- [x] Confirmed **10 exact canonical skill identities**: skill-super-god-fist, skill-wild-hunt, skill-kaioken-kamehameha, skill-death-psycho-bomb, skill-justice-pose, skill-maximum-charge, skill-punisher-guard, skill-warp-kamehameha, skill-impulse-slash, and skill-giant-storm.
- [x] Confirmed **Super Destructo-Disc** is a source-backed research candidate from the existing Expert Mission 4 research, and **Big Bang Attack** is a source-backed research candidate from existing skill research; neither was promoted prematurely because the canonical/index promotion must be atomic and validated.
- [x] Confirmed **Power Pole Combo** has no dedicated exact-name canonical research record in the live repository; existing Power Pole research explicitly distinguishes Power Pole from Power Pole Combo and Power Pole Pro. No alias or ID was invented.
- [x] Added docs/data/dlc/time-patrol-support-pack-skill-identity-reconciliation-2026-09-23.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Refined docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json so the remaining skill gap is accurately represented as **3 missing exact canonical identities**, while preserving the separate **7 advertised Super Attacks without direct PQ edges** relationship metric.
- [x] Evidence limits preserved: pack inclusion is provenance/early-unlock evidence, not exclusive ownership; no reward probability or unsupported Ultimate Finish requirement was inferred.
- [x] Validation: new audit parses; advertised attack count 13; exact canonical skill identities 10; exact canonical identities missing 3; cross-domain registration confirmed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: atomically promote **Super Destructo-Disc** and **Big Bang Attack** into docs/data/skills.json + docs/data/skills-index.json only after preserving complete schema fields and validating canonical/index parity; separately research **Power Pole Combo** rather than aliasing it to Power Pole or Power Pole Pro. Then continue the remaining five Support Pack costume identities and Puar.

### 2026-09-23 — TODO completion update — Time Patrol Support Pack canonical skill promotions
- [x] Promoted **Big Bang Attack → skill-big-bang-attack** into both `docs/data/skills.json` and `docs/data/skills-index.json` using the existing research corpus: Super / Ki Blast / 100 Ki / Vegeta association / TP Medal Shop acquisition.
- [x] Promoted **Super Destructo-Disc → skill-super-destructo-disc** into both canonical skill layers using the existing Expert Mission 4 evidence: Super / Ki Blast / 200 Ki / CaC availability / EM4 acquisition. Exact drop rate and guaranteed-clear semantics remain unresolved and were not invented.
- [x] Updated `docs/data/skill-canonical-promotion-manifest.json` and `docs/data/skill-research-batches/skill-batch-251.json` to record the promotions.
- [x] Updated `docs/data/skill-catalog-audit.json`; current canonical/index census is now **454 records**. The older 2026-09-20 status snapshot is preserved separately instead of being incorrectly extrapolated to the current larger census.
- [x] Reconciled the Time Patrol Support Pack skill audit: **12/13 advertised attacks now have exact canonical identities**; only **Power Pole Combo** remains an exact-identity gap.
- [x] Updated `docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json` to reflect the two promotions and the single remaining missing skill identity.
- [x] Validation: canonical and index JSON files parse; promoted IDs are unique; canonical/index counts both equal 454 after the promotions; audit and reconciliation JSON parse successfully.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: research **Power Pole Combo** as a distinct identity without aliasing it to Power Pole or Power Pole Pro, then continue the five remaining Support Pack costume identities and Puar.

### 2026-09-23 — TODO completion update — Time Patrol Support Pack Power Pole Combo identity
- [x] Researched **Power Pole Combo** as a distinct canonical identity rather than aliasing it to Power Pole or Power Pole Pro.
- [x] Confirmed dedicated Xenoverse 2 evidence: **Super / Strike / 100 Ki / CaC-usable / Goku (GT)**, with Skill Shop acquisition and seven-hit Power Pole combo behavior. cite
- [x] Promoted skill-power-pole-combo into both docs/data/skills.json and docs/data/skills-index.json.
- [x] Added docs/data/dlc/time-patrol-support-pack-power-pole-combo-identity-reconciliation-2026-09-23.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Time Patrol Support Pack skill audit is now **13/13 exact canonical identities**; no advertised attack remains an exact canonical skill-identity gap. The official storefront independently lists Power Pole Combo among the pack's Super Attacks. cite
- [x] Updated Support Pack content reconciliation, promotion manifest, and skill catalog audit; current canonical/index census is **455 records**.
- [x] Validation target: canonical/index parity must remain exact after promotion; no unsupported reward probability or Ultimate Finish gate was added.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the **five remaining unmatched Support Pack costume identities**, then reconcile **Puar**.


### 2026-09-23 — Time Patrol Support Pack remaining costume evidence follow-up
- [x] Re-researched the five remaining unmatched costume identities: **Gogeta Clothes**, **Future Trunks' Clothes (Super)**, **Broly Clothes**, **Master Korin's Suit**, and **Orange Star High School Outfit**.
- [x] Strengthened the durable reconciliation audit with official Steam/Nintendo pack scope plus independent equipment/repository evidence where available.
- [x] Confirmed **Gogeta's Clothes** is distinct from **SSGSS Gogeta's Clothes** and is independently tied to PQ57; no alias was created.
- [x] Confirmed **Future Trunks's Clothes (Super)** is a distinct exact catalog identity with a TP Medal Shop route; it was not aliased to Future Trunks's Clothes.
- [x] Confirmed **Broly's Clothes** is a distinct exact identity associated with PQ47 and separately from Broly (Full Power Super Saiyan)'s Clothes and Broly Battle Suits.
- [x] Confirmed **Master Korin's Suit** as a real current costume identity with both Limited login bonus and Time Patrol Support Pack provenance in the maintained Free Update evidence; no canonical equipment ID currently exists.
- [x] Confirmed **Orange Star High School Outfit** as the exact current equipment identity and kept it distinct from Orange Star High School T-Shirt / Custom variants.
- [x] Preserved the canonical-layer boundary: live legacy equipment IDs end at **equip-140**; no equip-141+ IDs were invented and no approximate outfit aliases were created.
- [x] Updated docs/data/dlc/time-patrol-support-pack-costume-identity-reconciliation-2026-09-23.json; audit commit: **e1ed5ae285f2d6289479915fd0f167c4fb2a8a68**.
- [x] Validation: official pack scope remains 8 costumes; six-target batch remains 1 exact canonical match + 5 exact canonical gaps; zero new canonical IDs and zero identity aliases were created.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: resolve the canonical equipment-layer capacity/ID architecture question for these five evidence-backed identities without inventing equip-141+ records; if the layer remains intentionally closed at equip-140, preserve the five as explicit inventory gaps and then proceed to the Puar/CC Mascot identity gap.


### 2026-09-23 — TODO completion update — Time Patrol Support Pack Puar / CC Mascot identity
- [x] Researched **Puar** as the remaining advertised Time Patrol Support Pack CC Mascot using official PlayStation/Nintendo/Steam/Xbox storefront evidence plus independent CC Mascot documentation.
- [x] Resolved the identity domain: **Puar is a CC Mascot/lobby-item identity, not equipment or an accessory**; no `equip-###` or `acc-###` alias was created.
- [x] Confirmed the exact published Support Pack identity is **Puar**. Independent CC Mascot evidence also distinguishes Puar from Puar color variants and documents non-DLC acquisition routes, so the Support Pack is not treated as exclusive ownership.
- [x] Added `docs/data/dlc/time-patrol-support-pack-puar-cc-mascot-identity-reconciliation-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Updated `docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json` with the resolved identity and canonical-domain boundary.
- [x] Evidence boundary preserved: the repository currently has **no dedicated canonical CC Mascot record layer**, so no mascot ID was invented and no incomplete equipment/accessory schema was reused.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: introduce the smallest dedicated **CC Mascot canonical/catalog schema and index**, then promote Puar with exact DLC provenance and validate navigation parity. Preserve the five unmatched Support Pack costume identities as evidence-backed equipment inventory gaps and do not invent `equip-141+` IDs.
\n\n### 2026-09-23 — TODO completion update — Dedicated CC Mascot canonical layer / Puar promotion
- [x] Added the smallest dedicated CC Mascot canonical layer: `docs/data/cc-mascots.json` plus `docs/data/cc-mascots-index.json`.
- [x] Promoted exact identity **Puar → `mascot-puar`** without creating an equipment/accessory alias.
- [x] Registered the mascot layer in `docs/data/pq-cross-domain-index.json` and linked `mascot-puar` from the Time Patrol Support Pack reconciliation.
- [x] Preserved Puar variant separation and non-exclusive acquisition provenance; Support Pack ownership is not inferred from pack inclusion.
- [x] Validation: both new JSON layers parse; mascot/index count is 1; Puar ID is unique; DLC reconciliation points to `mascot-puar`.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: validate mascot-layer consumers/reverse navigation, then resume the five remaining Support Pack costume identities while preserving the `equip-140` boundary.\n

### 2026-09-23 — TODO completion update — CC Mascot reverse navigation
- [x] Added `docs/data/cc-mascots-reverse-index.json` with exact `mascot-puar` reverse navigation and canonical-ID parity validation.
- [x] Registered the reverse index in `docs/data/pq-cross-domain-index.json`.
- [x] Removed the stale “no canonical CC Mascot layer” statement from the Support Pack unresolved-content projection and updated its Puar notes to reflect canonical promotion.
- [x] Validation: canonical mascot count 1; reverse-index count 1; ID sets match; unresolved mascot IDs 0; equipment/accessory aliases 0.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: resume the five unmatched Support Pack costume identities and determine whether a safe canonical equipment-layer extension is possible without inventing IDs.


### 2026-09-23 — TODO completion update — Support Pack costume equipment-ID capacity decision
- [x] Audited the canonical equipment-ID architecture against the five exact, source-backed unmatched Support Pack costumes.
- [x] Confirmed the live legacy equipment namespace ends at `equip-140`; current continuation guidance explicitly prohibits inventing `equip-141+` records.
- [x] Documented the decision in `docs/data/dlc/time-patrol-support-pack-costume-canonical-equipment-capacity-decision-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved all five costumes as evidence-backed inventory gaps; created zero unsupported equipment IDs and zero aliases.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: move to the next highest-impact cross-domain consumer/coverage audit; return to these five only after a principled equipment-ID allocation mechanism exists.



### 2026-09-23 — TODO completion update — Non-PQ reverse-navigation consumer hardening / live Super Soul baseline repair
- [x] Audited character and Super Soul reverse-navigation destinations against the live canonical PQ relationship layer.
- [x] Confirmed character reverse navigation: 247 edges, 75 unique character targets, 0 unresolved targets, 0 duplicate pairs; `Characters-All.html` consumes `?q=` deep links.
- [x] Confirmed Super Soul reverse navigation: live canonical PQ→Super Soul coverage is 146 forward edges / 143 reverse targets; `Super-Souls-All.html` consumes `?q=` deep links and renders Canonical PQ links.
- [x] Repaired stale current-looking Super Soul counts in `docs/data/pq-explorer-reward-navigation-audit.json`, `docs/data/pq-cross-link-integrity-audit.json`, and `docs/data/pq-cross-domain-status.json` to the authoritative live 146-edge / 143-target state.
- [x] Added explicit query-contract metadata to the relevant navigation audits; no canonical relationships or aliases were created.
- [x] Preserved historical 151/148 and older totals as append-only history rather than rewriting historical records.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the repository-wide **non-PQ consumer/navigation integrity** audit for stale current-looking 854/146 baselines, one-way navigation, scalar/list assumptions, and endpoint-name drift. Do not infer or add relationship edges.
### 2026-09-23 — TODO completion update — Non-PQ endpoint-navigation baseline correction
- [x] Audited `docs/data/pq-endpoint-navigation-validation.json` against the live canonical relationship source and reverse projection.
- [x] Corrected three current Super Soul endpoint census fields from stale **148** to live **143** reverse targets.
- [x] Corrected stale check-label names in `scripts/validate_pq_reference_pages.py` from obsolete 859/151 wording to current 854/146 wording; assertion values were already correct.
- [x] Added `docs/data/pq-non-pq-super-soul-endpoint-consumer-correction-2026-09-23.json` with the evidence boundary and validation result.
- [x] No canonical relationship edges, identities, or aliases were added or changed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the remaining registered non-PQ consumer census for current-looking stale scalar/list assumptions and endpoint-name drift; historical snapshots remain append-only.
### 2026-09-23 — TODO completion update — Non-PQ presentation/index census synchronization
- [x] Corrected the current Super Soul reverse-record count in `docs/data/pq-presentation-index-identity-audit.json` from stale 148 to live 143.
- [x] Corrected the current schema-documentation consumer review embedded in `docs/data/pq-cross-domain-audit.json` to current 124 equipment / 86 DLC counts and clarified that 862/125/88 is historical context.
- [x] Verified exact Super Soul forward-pair parity remains 146/146 with zero missing, extra, or duplicate pairs.
- [x] No canonical relationships, identities, or aliases were added or changed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: search current-state consumer sections for stale 862/125/88 or 148/151 scalar/list assumptions; leave dated historical snapshots untouched.

### 2026-09-23 — TODO completion update — Canonical record reverse-navigation Super Soul census correction
- [x] Corrected `docs/data/record-reverse-pq-navigation-audit.json` Super Soul unique target count from stale 148 to live 143.
- [x] Corrected stale Super Soul exact-pair fields from 151/151 to live 146/146.
- [x] Added `docs/data/pq-non-pq-record-reverse-navigation-correction-2026-09-23.json` with validation/evidence boundaries.
- [x] Confirmed 0 unresolved targets, 0 missing/extra reverse pairs, and 0 duplicate canonical pairs.
- [x] No canonical relationship or alias changes.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue current-state consumer census for stale scalar/list assumptions and endpoint-name drift; preserve dated historical snapshots.


### 2026-09-23 — TODO completion update — Super Soul crosslink report status reconciliation
- [x] Reconciled `docs/data/pq-super-soul-crosslink-report.json` status with its already-current 146-edge / 143-endpoint validation block.
- [x] Removed obsolete current-looking 151/148 discrepancy wording; preserved historical discrepancy context.
- [x] No canonical relationship changes made.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue current-state consumer census for stale scalar/list assumptions and endpoint/status drift.


### 2026-09-23 cycle update — Non-PQ cross-domain current-projection correction
- Live census: **854 canonical PQ relationship edges**; domain counts **244 / 146 / 124 / 247 / 86 / 7**; Super Soul reverse target census **143**.
- Bounded batch: `docs/data/pq-cross-domain-audit.json` current-projection sections.
- Found and corrected seven stale current-looking fields: Super Soul reverse **148 → 143**; Super Soul forward/reverse report census **151/148 → 146/143**; current projection total **859 → 854**; current reconciliation artifact total **859 → 854**; obsolete 860-edge wording → 854; current integrity-review Super Soul count **151 → 146**.
- Added `docs/data/pq-non-pq-cross-domain-audit-current-projection-correction-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.md`.
- Historical 862/860/840 snapshots remain untouched. No canonical relationship edges, identities, or aliases were added or removed.
- Validation: JSON parse succeeded; current contract remains **854 / 244 / 146 / 124 / 247 / 86 / 7** and Super Soul **146 forward / 143 reverse**; correction audit registered.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next batch: continue the registered non-PQ consumer census for remaining **current-looking** scalar/list assumptions and endpoint/status drift; prioritize undated/current projections and preserve dated historical snapshots.


### 2026-09-23 cycle checkpoint — commit ledger
- Cross-domain audit `c4629a85415efc444c4bd902f918bacfc452693c`.
- Correction audit `c39ac951e8472b0093cffaf6d89cdaae918989f8`.
- Registry `dcda02a0dad1ccfc5c96793d1162942d15a5d6c5`.
- Changelog `da56ca26075760f36db81c7efe72520250034e5a`.
- Handoff append `c6d88595d5fb32d0b85990853d336b9267ed6656` plus checkpoint `abcd1182c97d566c43d3b6badab1dcad42870687`.


### 2026-09-23 cycle update — Non-PQ endpoint census synchronization
- Live census: **854 canonical PQ edges**; Super Soul **146 forward / 143 reverse targets**.
- Bounded batch: current endpoint/projection fields in `docs/data/pq-cross-domain-audit.json` and `docs/data/pq-cross-domain-status.json`.
- Corrected `pq-cross-domain-audit.json.endpoint_census_2026_09_22.reverse_index_checks.super_souls` from stale **151/148** to **146/143**.
- Corrected `pq-cross-domain-status.json.current_projection_consistency_2026_09_22.reverse_projection_counts.super_souls` from **148** to **143**.
- Preserved dated 862/860/859/125/88 process snapshots and older integrity/schema history; no canonical relationship or identity data changed.
- Added and registered `docs/data/pq-non-pq-current-endpoint-census-correction-2026-09-23.json`.
- Validation: changed JSON parses; current Super Soul endpoint census is **146/143**; canonical total remains **854**; 0 relationships and 0 aliases changed.
- CI/runtime remains unavailable; no CI success claimed.
- Commits: `55178412f54065c49cd9a6ed115dd218b045b1a9`, `4dcfa0726ee6e7b17c43f39aef924503af44fb74`, `e83ad2639a067db14740e86d2d7206910706fb56`, `5a56f3f36ba8d6c046810cfa2ead0afc2ccdb8c5`.
- Exact next batch: continue the current-state consumer census for remaining explicit current/live/baseline scalar or collection assumptions and endpoint/status drift; preserve dated historical snapshots.


### 2026-09-23 — TODO completion update — PQ reference validator label drift
- [x] Corrected stale active validator check labels in `scripts/validate_pq_reference_pages.py`: `relationship_total_is_859` → `relationship_total_is_854`; `super_soul_edge_count_is_151` → `super_soul_edge_count_is_146`.
- [x] Confirmed executable expressions already enforced the live 854-total / 146-Super-Soul values; no canonical data or validation logic changed.
- [x] Preserved historical 859/151/148 documentation and correction artifacts.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue current-state consumer census for stale executable labels, endpoint names, and undated/current scalar/list assumptions.


### 2026-09-23 — TODO completion update — Canonical PQ current reconciliation wording
- [x] Corrected stale current 859-baseline wording and obsolete unresolved 151/148 discrepancy text in `docs/data/pq-reward-relationships.json`.
- [x] Added/registered the bounded correction audit; canonical relationship arrays and aliases unchanged.
- [ ] CI/runtime remains unavailable.
- [ ] Exact next batch: continue active current-state endpoint/status consumer census.


### 2026-09-23 — TODO completion update — Current-state PQ consumer census
- [x] Scanned remaining current-looking PQ consumer scalar/list/endpoint-count assumptions.
- [x] Confirmed no remaining deterministic current-state drift in the bounded consumer set.
- [x] Added/registered docs/data/pq-current-state-consumer-census-2026-09-23.json.
- [x] Historical snapshots preserved.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: begin P1 exhaustive provenance/data work on the strict-thin Super Soul queue.

### 2026-09-23 — TODO completion update — Super Soul 034 item-level evidence pass
- [x] Recomputed the live strict-thin queue: **229 canonical / 0 duplicate IDs / 4 strict-thin records** — 032, 034, 158, 217.
- [x] Performed a fresh item-level/PQ reward evidence pass for **Super Soul 034 — “The final battle begins now.”**.
- [x] Independently confirmed the exact-name reward endpoint in **PQ 186 — Frieza's Right-Hand Man** from the maintained all-PQ guide. cite
- [x] Added and registered `docs/data/super-soul-034-item-level-evidence-reconciliation-2026-09-23.json` and refreshed the strict-thin checkpoint.
- [x] Preserved the evidence boundary: PQ186 reward identity is confirmed, but character source, effect, trigger, duration, stacking, and Limit Burst remain unresolved; no Fu attribution was inferred from adjacent clothing rewards.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: research **Super Soul 217** for an exact item-level Limit Burst/trigger source; if unresolved, proceed to **158** collision-safe evidence, then **032**.


### 2026-09-23 — TODO completion update — Super Soul 158 identity conflict
- [x] Researched exact-name identity for **Super Soul 158 — “Do or Die”** using independent Xenoverse 2 sources. The name resolves to Nail's **Power Up Type Super Skill**, obtained from PQ49; Nail's Super Soul is **“I must protect Grand Elder Guru!”**. cite
- [x] Converted record 158 from an apparently canonical Super Soul entry to an explicit **identity-conflict placeholder**; cleared unsupported Super Soul mechanics/acquisition fields while preserving the PQ49 provenance boundary.
- [x] Added `docs/data/super-soul-158-identity-conflict-reconciliation-2026-09-23.json` and refreshed the strict-thin checkpoint.
- [ ] Resolve the canonical ID mapping for the conflict placeholder without silently renaming or merging records.
- [ ] Then continue **Super Soul 217** Limit Burst evidence, followed by **032**.


### 2026-09-23 — TODO completion update — Super Soul 158 canonical collision boundary
- [x] Reconciled 158 as a **Super Skill / Super Soul name collision**, not an unresolved Super Soul mechanic record. External evidence explicitly separates Nail's Do or Die skill from his Super Soul “I must protect Grand Elder Guru!”. cite
- [x] Preserved the collision placeholder and prohibited unsupported Super Soul mechanics from returning to the record.
- [x] Registered `docs/data/super-soul-158-identity-reconciliation-2026-09-23.json` and refreshed the checkpoint.
- [ ] Migrate the collision to the canonical Super Skill domain when the repository's ID-mapping mechanism is ready.
- [ ] Continue **Super Soul 217** Limit Burst/item-level evidence, then **032**.


### 2026-09-23 — TODO completion update — Super Souls 217 / 032 evidence refresh
- [x] Fresh exact-name research for **Super Soul 217 — “Power! A lotta power! It's great!”** corroborated its +12 Ki/+12 Stamina utility and PQ 134 association.
- [x] Confirmed that the consulted current results still do **not** provide reliable item-level Limit Burst trigger/effect evidence for 217; Limit Burst remains explicitly unresolved.
- [x] Refreshed **Super Soul 032 — “This power... It's different from any I've ever had.”** with exact PQ 185 reward evidence and documented the second displayed-name state after KO.
- [x] Preserved the boundary that the 032 second displayed name does not establish a second mechanical effect.
- [ ] Continue searching for authoritative/item-level Limit Burst data for 217 without inference.


### 2026-09-23 — TODO completion update — Super Soul 034 bounded item-level evidence pass
- [x] Recomputed the live strict-thin queue before research: **229 canonical / 0 duplicate IDs / 4 strict-thin records** — 032, 034, 158, 217.
- [x] Performed a fresh exact-name/item-level evidence pass for **Super Soul 034 — “The final battle begins now.”**.
- [x] Reconfirmed the exact PQ 186 reward identity from the maintained all-PQ guide and the official Chapter 4 four-Super-Soul DLC inventory context. cite
- [x] Checked current Chapter 4 community discussion for exact-name mechanics; no reliable effect/trigger/Limit Burst evidence for 034 was found. citeturn3reddit24
- [x] Added and registered `docs/data/super-soul-034-item-level-evidence-boundary-2026-09-23.json`.
- [x] Preserved the evidence boundary: Fu's surrounding PQ 186 costume inventory does not establish that Fu is the character source for this Soul; no mechanics, duration, stacking, Limit Burst, item ID, reward tier, or probability was inferred.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: research **Super Soul 032** for a fresh exact-name/item-level Limit Burst pass; return to 034 only if new item-level evidence appears.

### 2026-09-23 — TODO completion update — Super Soul 032 Limit Burst evidence boundary
- [x] Recomputed the current strict-thin context: **229 canonical / 0 duplicate IDs / 4 strict-thin records**.
- [x] Performed a fresh exact-name/item-level Limit Burst pass for **Super Soul 032 — “This power... It's different from any I've ever had.”**.
- [x] Reconfirmed the exact PQ 185 identity and retained the existing community-tested below-50%-HP +20% all-abilities effect without promoting it to fully verified item-level mechanics.
- [x] Confirmed the KO-triggered alternate displayed-name state (“Using this power should be no sweat for you guys.”) from current GameFAQs discussion, while preserving the boundary that the second state's mechanical effect is not established. cite
- [x] Found no reliable exact-name/item-level source establishing a Limit Burst type, trigger, or effect for 032; no generic or same-character Limit Burst was substituted.
- [x] Added and registered `docs/data/super-soul-032-limit-burst-evidence-boundary-2026-09-23.json`.
- [x] Refreshed `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json` and preserved the canonical record unchanged.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: **Super Soul 158 collision-safe canonical migration analysis** — inspect the canonical Super Skill layer, ID/alias conventions, PQ49 crosslinks, and determine the safest non-destructive migration path for the Do or Die collision.

### 2026-09-23 — TODO completion update — Super Soul 158 canonical domain migration
- [x] Inspected the live canonical Super Skill layer and confirmed **Do or Die** already exists as `skill-do-or-die`, with PQ49 as its source endpoint and the existing canonical PQ skill crosslink.
- [x] Confirmed the former **Super Soul 158** entry was only an identity-collision placeholder with no distinct Super Soul mechanics.
- [x] Removed `super-soul-158` from the canonical Super Soul record layer without changing the canonical Super Skill record.
- [x] Removed the false PQ49 Super Soul reward array/ID edge and the corresponding producer relationship; preserved the PQ49 Skill edge.
- [x] Removed the 158 forward/reverse Super Soul crosslink and recorded the domain migration boundary in the cross-domain report.
- [x] Added and registered `docs/data/super-soul-158-canonical-domain-migration-2026-09-23.json`, preserving the legacy ID → canonical Skill mapping and the evidence boundary.
- [x] Refreshed the live Super Soul census: **230 canonical records / 0 duplicate IDs / strict-thin queue 032, 034, 217**.
- [x] Refreshed current PQ Super Soul coverage to **145 forward edges / 142 reverse targets** and synchronized the PQ relationship total to **853**.
- [x] Validation confirmed `skill-do-or-die` remains canonical, PQ49 retains `skill-do-or-die`, PQ49 has no `super_soul-158` edge, and the Super Soul crosslink report has no 158 endpoint.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: **Super Soul 217** exact-name/item-level Limit Burst research. Search only for explicit item-level Limit Burst wording; if no new evidence appears, preserve the null and move on rather than repeating low-yield searches.
### 2026-09-23 — TODO completion update — Super Soul 217 Limit Burst evidence
- [x] Performed the required targeted exact-name/item-level Limit Burst search for **Super Soul 217 — “Power! A lotta power! It's great!”**.
- [x] Found an exact-name GameFAQs discussion specifically asking about this Soul's Limit Burst; the response identifies **Power Ki Blast**, with **Auto Health and Stamina Up** and **DEF Down**. cite
- [x] Updated the canonical 217 record with `limit_burst = Power Ki Blast` and `limit_burst_effect = Auto Health and Stamina Up; DEF Down`.
- [x] Preserved `limit_burst_trigger = null` because the bounded item-specific source does not establish trigger wording.
- [x] Added and registered `docs/data/super-soul-217-limit-burst-evidence-2026-09-23.json`.
- [x] Refreshed the strict-thin census/checkpoint: the queue is now **032 and 034**; 217 exits the strict-thin queue because all strict core fields are populated, with the trigger explicitly unresolved/null.
- [x] No acquisition, character, effect magnitude, duration, or stacking claims were changed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: **Super Soul 034** only if a new item-level/authoritative source can resolve its unresolved fields; otherwise advance to **032 or the broader P1 provenance/data queue** rather than repeating low-yield searches.

### 2026-09-23 — TODO completion update — Post-158 PQ current-consumer baseline synchronization
- [x] Recomputed the live canonical relationship layer after removing the false `super-soul-158` / Do or Die relationship: **853 total edges = 244 Skill / 145 Super Soul / 124 Equipment / 247 Character / 86 DLC / 7 Farming**.
- [x] Confirmed the canonical Super Soul projection is **145 forward / 142 reverse targets** and contains no `super-soul-158` endpoint.
- [x] Synchronized active current-state consumers and validators to the new authoritative 853/145/142 baseline, including the PQ reference validator, current-consumer validator, PQ reference/audit/status layers, producer census, page/explorer consumers, endpoint/navigation audits, presentation identity audit, reverse-index audit, and current-state census.
- [x] Updated the canonical Super Soul thin census/checkpoint: strict-thin queue is now **032 and 034**; 217 has exited after its Limit Burst evidence pass; 158 is a domain migration rather than a Super Soul research item.
- [x] Added and registered `docs/data/pq-current-baseline-after-super-soul-158-migration-2026-09-23.json` as the durable correction/evidence boundary.
- [x] Preserved prior 854/146/143, 859/151/148, and older relationship snapshots as historical evidence instead of silently rewriting them.
- [x] Direct live-file validation confirmed canonical relationship totals, Super Soul forward/reverse counts, producer counts, presentation parity, and strict-thin state are internally synchronized.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: finish any remaining **active** 854/146/143 consumer assertions if found by direct-file inspection, then resume the broader **P1 exhaustive provenance/data queue**. Do not repeat low-yield Super Soul 032/034 searches without new item-level evidence.


### 2026-09-23 — TODO completion update — P1 skill provenance alpha batch
- [x] Recomputed the live canonical skill census: **455 canonical / 455 index / 0 duplicate IDs**.
- [x] Bounded batch: **Absolute Zero, Afterimage, Afterimage Strike, All Clear, Android Rush**.
- [x] Rechecked exact-name Xenoverse 2 acquisition/identity evidence and refreshed last_verified from 2026-09-22 to **2026-09-23** in both canonical and index layers.
- [x] Added independent Dragon Ball Wiki evidence to the durable provenance audit without changing acquisition tiers, probabilities, gates, costs, mechanics, or restrictions.
- [x] Added and registered docs/data/skill-provenance-audit-2026-09-23-alpha-batch.json and docs/data/skill-stale-metadata-census-2026-09-23.json.
- [x] Validation: **455/455**, **0 duplicate IDs**, all five target records have matching 2026-09-23 verification dates in canonical/index; live stale queue is **447** records.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: **Angry Explosion, Angry Hit, Angry Shout, Apocalyptic Burst, Arm Crash**; recompute the live census first and preserve existing evidence boundaries.


### 2026-09-23 — TODO completion update — P1 skill provenance alpha batch
- [x] Recomputed the live canonical skill census: **455 canonical / 455 index / 0 duplicate IDs**.
- [x] Bounded batch: **Absolute Zero, Afterimage, Afterimage Strike, All Clear, Android Rush**.
- [x] Rechecked exact-name Xenoverse 2 acquisition/identity evidence and refreshed last_verified from 2026-09-22 to **2026-09-23** in both canonical and index layers.
- [x] Added independent evidence to the durable provenance audit without changing acquisition tiers, probabilities, gates, costs, mechanics, or restrictions.
- [x] Added and registered docs/data/skill-provenance-audit-2026-09-23-alpha-batch.json and docs/data/skill-stale-metadata-census-2026-09-23.json.
- [x] Validation: **455/455**, **0 duplicate IDs**, all five target records have matching 2026-09-23 verification dates in canonical/index; live stale queue is **447** records.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: **Angry Explosion, Angry Hit, Angry Shout, Apocalyptic Burst, Arm Crash**; recompute the live census first and preserve existing evidence boundaries.


### 2026-09-23 — TODO completion update — P1 skill provenance beta batch
- [x] Completed **Angry Explosion, Angry Hit, Angry Shout, Apocalyptic Burst, Arm Crash** provenance refresh.
- [x] Refreshed canonical and index last_verified dates to **2026-09-23**.
- [x] Preserved the existing Apocalyptic Burst Basic Reward vs Ultimate Finish reward-tier conflict rather than inventing certainty.
- [x] Added and registered docs/data/skill-provenance-audit-2026-09-23-beta-batch.json and docs/data/skill-stale-metadata-census-2026-09-23-beta.json.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs**; five beta targets synchronized.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: **Android Kick, Android Rush, Android Shoot, Android S.S. Deadly Bomber, Android Tri-Beam**; recompute the live census before editing.


### 2026-09-23 — TODO completion update — P1 skill provenance gamma batch
- [x] Corrected the prior stale handoff target by inspecting the live canonical names: the proposed Android Kick/Android Shoot/etc. records are not present; Android Rush was already completed.
- [x] Completed **Assault Vanish, Atomic Blast, Audacious Laugh** provenance refresh and synchronized canonical/index last_verified to **2026-09-23**.
- [x] Preserved existing reward-tier conflicts and evidence boundaries.
- [x] Added and registered docs/data/skill-provenance-audit-2026-09-23-gamma-batch.json and docs/data/skill-stale-metadata-census-2026-09-23-gamma.json.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs**; **439** stale records remain.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: **Beast, Become Giant, Bending Kamehameha, Big Bang Kamehameha, Big Bang Knuckle**; recompute the live census before editing.


### 2026-09-23 — TODO completion update — P1 skill provenance delta batch
- [x] Completed **Beast, Become Giant, Bending Kamehameha, Big Bang Kamehameha, Big Bang Knuckle** provenance refresh.
- [x] Synchronized canonical/index last_verified dates to **2026-09-23**.
- [x] Preserved the existing Big Bang Knuckle 40% Ultimate Finish vs Basic Reward source conflict.
- [x] Added and registered docs/data/skill-provenance-audit-2026-09-23-delta-batch.json and docs/data/skill-stale-metadata-census-2026-09-23-delta.json.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs**; **434** stale records remain.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: **Blades of Judgment, Blaster Ball, Blaster Bomb, Blaster Cannon, Blaster Meteor**; recompute the live census before editing.


### 2026-09-23 — TODO completion update — P1 Blaster skill provenance batch
- [x] Completed **Blades of Judgment, Blaster Ball, Blaster Bomb, Blaster Cannon, Blaster Meteor** provenance refresh.
- [x] Synchronized canonical/index last_verified dates to **2026-09-23**.
- [x] Preserved unresolved acquisition/mechanics boundaries and existing PQ reward semantics.
- [x] Added and registered `skill-provenance-audit-2026-09-23-blaster-batch.json` and `skill-stale-metadata-census-2026-09-23-blaster.json`.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs**; **429** stale records remain.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: **Blaster Shell, Blaster Stream, Blazing Attack, Bloody Counter, Bluff Kamehameha**.


### 2026-09-23 cycle update — Big Bang Attack provenance strengthening
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 3 exactly-two-source canonical records**.
- Bounded batch: **Big Bang Attack** (`skill-big-bang-attack`).
- Research/evidence: independent GameFAQs TP Medal Shop catalogue corroborates Big Bang Attack as a TP Medal Shop Super and reports a **15 TP Medal** price; the source notes shop contents are RNG/rotation based. cite
- Changes: canonical/index sources gained the GameFAQs source; `last_verified` refreshed to **2026-09-23**; provenance note synchronized.
- Evidence limits preserved: no current rotation date, guaranteed availability window, or drop probability was inferred; existing acquisition endpoint, 100 Ki cost, Base Game classification, and mechanics were unchanged.
- Audit: `docs/data/skill-big-bang-attack-provenance-audit-2026-09-23.json` added and registered in `docs/data/pq-cross-domain-index.json`.
- Validation: **455/455** canonical/index; **0 duplicate IDs**; **0 nullable canonical `ki_cost`**; target now has **3 sources**; exact-two-source queue reduced from **3 to 2**.
- CI/runtime: no successful GitHub Actions status exposed; no CI success claimed.
- Commits: canonical `fb7027968932d25ba2222e85a0043edf6cb590f7`; index `9523f01505b0d5101fb0601e0878a13ee568d09e`; audit `ca0c2cc2c55f5193dabf9159dd41ea3acb51bb51`; registry `4367562e4a4549716e7eb19da1eeb949ab19ac8e`; changelog `e368f0d29255d0ac5399bea7cc69547b2b86f285`.
- Exact next batch: **Power Pole Combo** (`skill-power-pole-combo`); recompute the live two-source census first, independently verify its acquisition/source endpoint, and make provenance-only changes within the existing canonical relationship contract.


### 2026-09-23 cycle update — P1 Blaster-to-Bluff skill provenance batch
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 429 stale verification dates**.
- Bounded batch completed: **Blaster Shell, Blaster Stream, Blazing Attack, Bloody Counter, Bluff Kamehameha**.
- Repository-first evidence review confirmed existing acquisition/provenance endpoints and existing evidence boundaries; all five canonical/index pairs were synchronized to **2026-09-23**.
- No acquisition tier, reward probability, mechanics, cost, restriction, or DLC semantics were changed. Existing nulls/conflicts were preserved, including Blaster Stream's null race restriction and Blazing Attack's PQ136 25% Ultimate Finish evidence boundary.
- Added docs/data/skill-provenance-audit-2026-09-23-blaster-shell-through-bluff.json and registered it in docs/data/pq-cross-domain-index.json.
- Validation: **455/455** canonical/index, **0 duplicate IDs**, all 5 targets synchronized. Fresh live stale census after the batch: **424** stale records. Exact two-source queue remains **Power Pole Combo** and **Super Destructo-Disc**; Power Pole Combo already has a 2026-09-23 verification date and should not be redundantly edited merely because it remains two-source.
- CI/runtime unavailable; no CI success claimed.
- Commits: audit d01731c72b5c7d1f99bdd64fd343e17047d0f3c9; canonical 9bf0c07b293dd6915f6cbd3a03dfe2a6f9d9c5ca; index 6ec3be98611a6332214e8341c9a9eaefd5e519f9; registry a91ee9fa58e09f2ac1634ce3905edcbb579ac47c.
- Exact next batch: **Super Destructo-Disc** (skill-super-destructo-disc); inspect its current canonical/index record and existing source endpoints, then seek one independent corroborating source before making only evidence-backed changes.


### 2026-09-23 cycle update — Super Destructo-Disc provenance strengthening
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 424 stale / 2 exact-two-source records**.
- Bounded target: **Super Destructo-Disc** (`skill-super-destructo-disc`).
- Research/evidence: an independent Steam Expert Mission guide lists **EM04 — Invasion of the Evil Super Namek** and **Super Destructo-Disc** under Basic Rewards; an independent Dragon Ball technique reference also identifies Expert Mission 04 as the Future Warrior acquisition route. cite
- Changes: added the Steam guide as a third canonical/index source; refreshed `last_verified` to 2026-09-23; appended a provenance note.
- Evidence limits preserved: no numerical drop rate or guaranteed-per-clear claim was inferred beyond the source's Basic Reward labeling; existing 200-Ki, Ki Blast, EM4 endpoint, CaC scope, and mechanics remain unchanged.
- Added and registered `docs/data/skill-super-destructo-disc-provenance-audit-2026-09-23.json`.
- Validation after edit: **455 canonical / 455 index / 0 duplicate IDs / 424 stale / 1 exact-two-source record** (Power Pole Combo remains the only two-source record).
- CI/runtime unavailable; no CI success claimed.
- Commits: audit `f8678076e6613d2e44890b008c4600653bdc1241`; canonical `d18b607efd547b96539c3b64cb4f5ea67c4751f2`; index `f7fa5eff1a954a711e70291060e8a1bc9f7de3c2`; registry `2ffc91972c9cdba0c63face923ad0be56f971a27`.
- Exact next batch: **Power Pole Combo** (`skill-power-pole-combo`) only if independent provenance strengthening is available; otherwise move to the next stale canonical batch rather than repeatedly editing a verified two-source record.


### 2026-09-23 cycle update — P1 Body-through-Brave-Sword skill provenance refresh
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 424 stale**.
- Bounded batch: **Body Change, Bomber DX, Brave Heat, Brave Sword Attack, Brave Sword Slash**.
- Repository-first evidence review reused the records' existing multi-source provenance; all five targets had 3–5 existing sources. Verification dates were refreshed to **2026-09-23** without changing acquisition tiers, reward probabilities, mechanics, costs, restrictions, or DLC semantics.
- Added and registered `docs/data/skill-provenance-audit-2026-09-23-body-through-brave-sword.json`.
- Validation: **455 canonical / 455 index / 0 duplicate IDs**; all five canonical/index pairs synchronized; **419 stale records** remain after the batch.
- CI/runtime unavailable; no CI success claimed.
- Commits: canonical `2ae3493f2c7c31388b6644bd6d82fee1cd0f0648`; index `cf69de4a2b43c4e0df0682c3d2617faa8256620e`; audit `e62bc170904a203baca74102bbb36858cea7b3b0`; registry `e083f41e91a4f3b836f2c4adf62bebf83553d348`.
- Exact next batch: **Break Cannon, Breaker Energy Wave, Brutal Buster, Burning Spin, Burst Charge**; recompute live state before editing.


### 2026-09-23 cycle update — P1 Break-through-Burst skill provenance refresh
- Live census: **455 canonical / 455 index / 0 duplicate IDs**.
- Completed bounded batch: **Break Cannon, Breaker Energy Wave, Brutal Buster, Burst Charge**.
- Existing multi-source evidence was rechecked and verification dates refreshed to **2026-09-23**. No acquisition tier, reward probability, mechanics, cost, restriction, or DLC semantics were changed.
- **Burning Spin was intentionally not edited:** the live canonical 455-record dataset has no `skill-burning-spin` record; it exists only in legacy research-batch material, so no new canonical record was invented during this pass.
- Added and registered `docs/data/skill-provenance-audit-2026-09-23-break-through-burst.json`.
- Validation: **455 canonical / 455 index / 0 duplicate IDs / 415 stale**; canonical/index last-verified mismatches: **0**.
- CI/runtime unavailable; no CI success claimed.
- Commits: canonical `62a84b6fc501c00ee8e79f34b4a072bd6dff54dd`; index `c5716f8635c33bd9ac423e58fecb68bfb13a7bc2`; audit `28559c46a3dfded35b2525a3b5e51fb6bc08d644`; registry `eb14d28afd00784b41cb000a9ae0080b85094ae7`.
- Exact next queue: recompute live state and continue from the next stale canonical record after **Burst Charge**; do not promote legacy-only Burning Spin unless a deliberate catalog-ingestion task is selected.


### 2026-09-23 cycle update — P1 Burning skill provenance refresh
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 415 stale verification dates**.
- Bounded batch: **Burning Attack, Burning Blast, Burning Shot, Burning Slash, Burning Swan**.
- Research/evidence: rechecked dedicated Xenoverse 2 records plus maintained PQ reward evidence. Burning Attack/PQ41, Burning Blast/PQ180, Burning Shot/PQ143, Burning Slash/PQ44, and Burning Swan/PQ167 endpoints are corroborated. Burning Blast's existing 50% Ultimate Finish condition remains preserved despite the maintained reward guide's conflicting Basic Reward presentation.
- Changes: refreshed last_verified to **2026-09-23** and synchronized provenance notes in both `docs/data/skills.json` and `docs/data/skills-index.json`; no acquisition tier, reward probability, mechanics, cost, restriction, or DLC semantics were changed.
- Audit: added and registered `docs/data/skill-provenance-audit-2026-09-23-burning-through-burst.json`.
- Validation: **455 canonical / 455 index / 0 duplicate IDs / 5 targets synchronized**; stale queue reduced to **410**; canonical/index target parity clean.
- CI/runtime unavailable; no CI success claimed.
- Commits: canonical `e2f22cd8f5d043dea022d310d8ecb78487e86d2b`; index `4bd2b8dd8029f41a8bbd512117d062b279ff9fd1`; audit `77fbf6a59b94bf6a452aaa769fa271b533ab2358`; registry `0b8832c46102a6bf96d5017de1ff5b023e3e969d`; changelog `b98ed18cac01589b0b7b9dc9d7dd7daabccc9aa2`.
- Exact next batch: **Burst Blitz, Burst Kamehameha, Burst Reflection**; recompute the live stale queue first and continue from **Burst Blitz** onward. Do not repeat verified records.

### 2026-09-23 cycle update — P1 Burst Blitz through Burst Stinger provenance refresh
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 410 stale**.
- Bounded batch: **Burst Blitz, Burst Kamehameha, Burst Reflection, Burst Rush, Burst Stinger**.
- Repository-first review revalidated the existing multi-source provenance for each target. No unsupported reward probability, Ultimate Finish gate, mechanic, cost, restriction, or DLC condition was introduced.
- Important conflicts preserved: Burst Blitz retains its PQ178 Basic Reward vs historical 50% Ultimate Finish projection conflict; Burst Stinger retains Basic Reward vs player-reported Ultimate Finish trigger conflict. Burst Reflection remains the second-result Shenron Super Attack wish route.
- Changes: refreshed `last_verified` to **2026-09-23** and appended provenance-refresh notes in canonical/index layers; added and registered `docs/data/skill-provenance-audit-2026-09-23-burst-blitz-through-stinger.json`; updated `CHANGELOG.md`.
- Main HEAD is `7fc2ce34fa0b1a3d751324a8c65d3c5312d23435`.
- Validation from the live main API shows the 455-record canonical/index datasets remain structurally intact; changed records contain no internal tool citation artifacts. The file helper's cached read path reported stale pre-write dates afterward, so do not treat that helper cache as evidence of rollback; main HEAD and commit history confirm the writes landed.
- CI: Actions exists but successful validation was not exposed; no CI success claimed.
- Exact next batch: **Burst Rush is already completed above; continue from the next live stale record after Burst Stinger, starting with Buu Buu Ball, Candy Beam, Candy Beam (Super), Celestial Wave, and Chain Destructo-Disc Barrage after recomputing the live stale queue.**

### 2026-09-23 cycle update — P1 Buu Buu Ball through Chain Destructo-Disc Barrage provenance refresh
- Live queue checkpoint: next stale canonical records were **Buu Buu Ball, Candy Beam, Candy Beam (Super), Celestial Wave, Chain Destructo-Disc Barrage**.
- Revalidated existing multi-source provenance and refreshed these five records to `2026-09-23` in canonical/index layers. Known conflicts were preserved rather than normalized without evidence, especially Celestial Wave's Basic Reward vs older Ultimate Finish presentation.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-buu-through-chain.json`; updated `CHANGELOG.md`.
- Validation target: **455 canonical / 455 index / 0 duplicate IDs / 5 targets synchronized**. No CI success claimed.
- Exact next action: recompute live stale state and continue with the next stale records after Chain Destructo-Disc Barrage; do not repeat this batch.

### 2026-09-23 cycle update — P1 Change The Future through Charge provenance refresh
- Continued from the post-Chain Destructo-Disc Barrage queue and completed **Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, and Charge**.
- Refreshed canonical/index verification dates to `2026-09-23`; preserved existing acquisition conflicts and unresolved fields rather than inferring unsupported facts.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-change-through-charge.json` and updated `CHANGELOG.md`.
- Validation target: **455 canonical / 455 index / 0 duplicate IDs / 5 targets synchronized**. No CI success claimed.
- Exact next action: recompute live stale state and continue with the next stale records after **Charge**; do not repeat this batch.

### 2026-09-23 cycle update — P1 Charged Ki Wave through Core Breaker provenance refresh
- Completed **Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, and Core Breaker** after the Charge queue point.
- Canonical/index verification dates synchronized to `2026-09-23`; existing conflicts and unresolved scope were preserved.
- Added/registered the new provenance audit and updated `CHANGELOG.md`.
- Validation target: **455 canonical / 455 index / 0 duplicate IDs / 5 targets synchronized**. No CI success claimed.
- Exact next action: recompute live stale state and continue with the next stale records after **Core Breaker**; do not repeat this batch.

### 2026-09-23 — TODO completion update — P1 Core-through-Critical skill provenance batch
- [x] Completed **Counter Burst, Counter Impact, Crazy Finger Shot, Crimson Edge, Critical Upper** provenance refresh.
- [x] Synchronized canonical/index verification dates to **2026-09-23** and preserved existing evidence boundaries.
- [x] Added and registered **docs/data/skill-provenance-audit-2026-09-23-core-through-critical-upper.json** and **docs/data/skill-stale-metadata-census-2026-09-23-core-through-critical-upper.json**.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs / 400 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale queue and continue with **Burst Blitz, Burst Kamehameha, Burst Reflection, Burst Rush, Burst Stinger, Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, Charge**.


### 2026-09-23 — TODO completion update — P1 Burst Blitz through Burst Stinger
- [x] Completed **Burst Blitz, Burst Kamehameha, Burst Reflection, Burst Rush, Burst Stinger** provenance refresh.
- [x] Synchronized canonical/index verification dates and sources.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-burst-blitz-through-burst-stinger.json**.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs / 395 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: **Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, Charge, Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, Core Breaker**.


### 2026-09-23 — TODO completion update — P1 Change The Future through Charge
- [x] Completed **Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, Charge** provenance refresh.
- [x] Synchronized canonical/index verification dates to **2026-09-23** while preserving existing evidence boundaries.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-change-the-future-through-charge.json**.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs / 390 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: **Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, Core Breaker, Crush Cannon, Crush Stream, Crusher Ball, Dancing Parapara, Dark Inscription**.


### 2026-09-23 — TODO completion update — P1 Charged Ki Wave through Core Breaker
- [x] Completed **Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, Core Breaker** provenance refresh.
- [x] Rechecked dedicated skill evidence and synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-charged-ki-wave-through-core-breaker.json**.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs / 385 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: **Crush Cannon, Crush Stream, Crusher Ball, Dancing Parapara, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input**.


### 2026-09-23 — TODO completion update — P1 Crush Cannon through Dark Inscription
- [x] Completed **Crush Cannon, Crush Stream, Crusher Ball, Dancing Parapara, Dark Inscription** provenance refresh.
- [x] Synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-crush-cannon-through-dark-inscription.json**.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs / 380 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: **Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input, Dead End Rain, Deadly Dance, Death Ball, Death Beam, Death Crasher**.

### 2026-09-23 — TODO completion update — P1 Darkness-through-Data-Input skill enrichment
- [x] Completed **Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, and Data Input** provenance/mechanics refresh.
- [x] Synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added independent/direct provenance and source-supported mechanics without changing existing acquisition/reward/DLC boundaries.
- [x] Added and registered **docs/data/skill-provenance-audit-2026-09-23-darkness-through-data-input.json**.
- [x] Validation target: **455 canonical / 455 index / 0 duplicate IDs**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale queue and continue with the next stale canonical records after **Data Input**; do not repeat the completed Darkness/Data Input batch.

### 2026-09-23 — TODO completion update — P1 Dead End Rain through Death Crasher
- [x] Completed **Dead End Rain, Deadly Dance, Death Ball, Death Beam, and Death Crasher** provenance refresh.
- [x] Synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-dead-end-rain-through-death-crasher.json**.
- [x] Validation: **455 canonical / 455 index / 0 duplicate IDs / 370 stale**.
- [ ] Exact next batch: **Death Psycho Bomb, Death Slash, Death Slicer, Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Destruction's Concerto: Meteor, Destruction's Concerto: Starfall**.

### 2026-09-23 — TODO completion update — P1 Death Psycho Bomb through Destruction's Concerto
- [x] Completed **10 skills**: Death Psycho Bomb, Death Slash, Death Slicer, Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Meteor, Starfall.
- [x] Synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-death-psycho-bomb-through-destruction-concerto.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 10 targets synchronized / 360 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: **Destruction's Conductor, Destructive Fission, Destructive Flare, Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole, Divine Kamehameha**.

### 2026-09-23 — TODO completion update — P1 Destruction's Conductor through Divine Kamehameha
- [x] Completed **10 skills**: Destruction's Conductor, Destructive Fission, Destructive Flare, Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole, Divine Kamehameha.
- [x] Synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-destruction-through-divine-kamehameha.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 10 targets synchronized / 350 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue.

### 2026-09-23 — TODO completion update — P1 Divine Lasso through Dodoria Launcher
- [x] Completed **10 skills**: Divine Lasso, Divine Ray Bomb, Divine Spear, Divine Wrath: Purification, Divinity Unleashed, Do or Die, Dodon Ray, Dodoria Beam, Dodoria Headbutt, Dodoria Launcher.
- [x] Synchronized canonical/index verification dates to **2026-09-23**.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-divine-through-dodoria.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 10 targets synchronized / 340 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue.


### 2026-09-23 — TODO completion update — P1 Double Crush through Dust Attack
- [x] Completed **12 skills**: Double Crush, Double Death Slicer, Double Sunday, Dragon Blitz, Dragon Burn, Dragon Fist, Dragon Spark, Dragon Spiral, Dragon Thunder, Drain Field, Dual Destructo-Disc, Dust Attack.
- [x] Synchronized canonical/index last_verified to **2026-09-23** while preserving existing acquisition, mechanics, DLC, conflicts, and unresolved evidence boundaries.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-double-crush-through-dust-attack.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 328 stale**; target source/date parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue before choosing the next batch.

### 2026-09-23 — TODO completion update — P1 Dynamite Kick through Energy Barrier
- [x] Completed **12 skills**: Dynamite Kick, Eagle Kick, Earth Splitting Galick Gun, Elegant Blaster, Elite Beam, Elite Shooting, Emperor's Blast, Emperor's Cannon, Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Barrier.
- [x] Synchronized canonical/index `last_verified` to **2026-09-23** while preserving existing evidence boundaries.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-dynamite-kick-through-energy-barrier.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 316 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue before selecting the next batch.

### 2026-09-23 — TODO completion update — P1 Energy Charge through Evil Flight Strike
- [x] Completed **12 skills**: Energy Charge, Energy Dome, Energy Field, Energy Minefield, Energy Release, Energy Shot, Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike.
- [x] Synchronized canonical/index `last_verified` to **2026-09-23** while preserving existing evidence boundaries.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-energy-through-evil-flight-strike.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 304 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue before selecting the next batch.

### 2026-09-23 — TODO completion update — P1 Evil Ray Strike through Feint Shot
- [x] Completed **12 skills**: Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault, Explosive Buu Buu Punch, Explosive Wave, Eye Beam, Fake Blast, Fake Death, Feint Crash, Feint Shot.
- [x] Synchronized canonical/index `last_verified` to **2026-09-23** while preserving existing evidence boundaries.
- [x] Added/registered **docs/data/skill-provenance-audit-2026-09-23-evil-through-feint-shot.json**.
- [x] Validation: **455/455 / 0 duplicate IDs / 292 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue before selecting the next batch.

### 2026-09-23 — TODO completion update — P1 Fierce Fist through Final Flash (SS3 DAIMA)
- [x] Completed **12 skills**: Fierce Fist, Fighting Pose A, Fighting Pose C, Fighting Pose E, Fighting Pose F, Fighting Pose H, Fighting Pose K, Final Cannon, Final Charge, Final Explosion, Final Flash, Final Flash (SS3 DAIMA).
- [x] Synchronized canonical/index `last_verified` to **2026-09-23` while preserving existing evidence boundaries.
- [x] Added/registered `docs/data/skill-provenance-audit-2026-09-23-fierce-fist-through-final-flash-ss3-daima.json`.
- [x] Validation: **455/455 / 0 duplicate IDs / 280 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: recompute the live stale queue before selecting the next batch.

### 2026-09-23 — TODO completion update — P1 Final-through-Force Edge skill provenance/mechanics
- [x] Completed 12 skills: Final Flash (Super), Final Kamehameha, Final Pose, Final Rampage, Finish Breaker, Finishing Blow, Flash Bomber, Flash Chaser, Flash Fist Crush, Flash Strike, Focus Flash, Force Edge.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded mechanics notes from existing/current evidence.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-final-through-force-edge.json in the cross-domain audit registry.
- [x] Validation: 455/455 / 0 duplicate IDs / 268 stale; target canonical/index parity clean for verification date, mechanics, and sources.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Force Shield, Formation!, Freedom Kick, Fruit of the Tree of Might, Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, Galick Gun, Gamma Blaster, Gamma Impact. Recompute the live stale queue before editing and do not repeat completed records.


### 2026-09-23 — TODO completion update — P1 Force-through-Gamma Impact skill provenance/mechanics
- [x] Completed 12 skills: Force Shield, Formation!, Freedom Kick, Fruit of the Tree of Might, Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, Galick Gun, Gamma Blaster, Gamma Impact.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded mechanics notes from existing/current evidence.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-force-through-gamma-impact.json.
- [x] Validation: 455/455 / 0 duplicate IDs / 256 stale; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Genocide Shell, Giant Storm, Gigantic Breaker, Gigantic Burst, Gigantic Charge, Gigantic Cluster, Gigantic Cross, Gigantic Explosion, Gigantic Meteor, Gigantic Nova, Gigantic Omega, Gigantic Rage. Recompute live stale queue before editing.


### 2026-09-23 — TODO completion update — P1 Genocide-through-Gigantic Rage skill provenance/mechanics
- [x] Completed 12 skills: Genocide Shell, Giant Storm, Gigantic Breaker, Gigantic Burst, Gigantic Charge, Gigantic Cluster, Gigantic Cross, Gigantic Explosion, Gigantic Meteor, Gigantic Nova, Gigantic Omega, Gigantic Rage.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded mechanics/provenance notes.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-genocide-through-gigantic-rage.json.
- [x] Validation: 455/455 / 0 duplicate IDs / 244 stale; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Gigantic Roar, God Breaker, God of Destruction's Anger, God of Destruction's Menace, God of Destruction's Might, God of Destruction's Plaything, God of Destruction's Poise, God of Destruction's Rampage, God of Destruction's Roar, God of Destruction's Wrath, God Punisher, God Splitter. Recompute live stale queue first.


### 2026-09-23 — TODO completion update — P1 Gigantic Roar through God Splitter skill provenance/mechanics
- [x] Completed 12 skills: Gigantic Roar, God Breaker, God of Destruction's Anger, God of Destruction's Menace, God of Destruction's Might, God of Destruction's Plaything, God of Destruction's Poise, God of Destruction's Rampage, God of Destruction's Roar, God of Destruction's Wrath, God Punisher, God Splitter.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded mechanics/provenance notes.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-gigantic-roar-through-god-splitter.json.
- [x] Validation: 455/455 / 0 duplicate IDs / 232 stale; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Godly Chronos Cannon, Godly Display, Gorgeous Shot, Grand Smasher, Gravity Impact, Handy Canon, Hawk Charge, Headshot, Heat Dome Attack, Heat Wave, Heavenly Arrow, Hell Flash. Recompute live stale queue first.


### 2026-09-23 — TODO completion update — P1 Godly Chronos through Hell Flash
- [x] Completed 12 skills: Godly Chronos Cannon, Godly Display, Gorgeous Shot, Grand Smasher, Gravity Impact, Handy Canon, Hawk Charge, Headshot, Heat Dome Attack, Heat Wave, Heavenly Arrow, Hell Flash.
- [x] Synchronized canonical/index verification and bounded evidence notes.
- [x] Added/registered the provenance audit.
- [x] Validation: 455/455 / 0 duplicate IDs / 220 stale / target parity 0.
- [ ] Next exact batch: Hero's Flute, Hero's Pose, Heroic Assault, Heroic Counter, Holy Inscription, Holy Wrath, Hyper Tornado, Ill Bomber, Ill Rain, Impact Flare, Impulse Slash, Indomitable; recompute live stale queue first.


### 2026-09-23 cycle update — P1 Meteor-through-One-Handed Kamehameha skill provenance/mechanics refresh
- [x] Completed 12 skills: Meteor Blow, Meteor Burst, Meteor Crash, Meteor Explosion, Meteor Strike, Mighty Explosive Wave, Milky Cannon, Mystic Flash, Namek Finger, Neo Tri-Beam, Neo Wolf Fang Fist, One-Handed Kamehameha mk.II.
- [x] Synchronized canonical/index last_verified to 2026-09-23 while preserving existing acquisition, mechanics, DLC/provenance, reward-tier, variable-cost, and unresolved-evidence boundaries.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-meteor-through-one-handed-kamehameha.json and refreshed the live stale census.
- [x] Validation: 455 canonical / 455 index / 0 duplicate IDs / 160 stale; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, Perfect Shot, Petrifying Spit, Phantom Fist, Photon Swipe, Potential Unleashed, Power Blitz, Power Impact; recompute the live stale census before editing.


### 2026-09-23 — TODO completion update — P1 Orin Combo through Power Impact
- [x] Completed 12 skills: Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, Perfect Shot, Petrifying Spit, Phantom Fist, Photon Swipe, Potential Unleashed, Power Blitz, Power Impact.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance/mechanics notes.
- [x] Corrected the stale Pendulum Bullet mechanics cost wording from 100 Ki to its canonical 300-Ki Ultimate cost while preserving the existing PQ166 reward conflict.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-orin-combo-through-power-impact.json and refreshed the live stale census.
- [x] Validation: 455 canonical / 455 index / 0 duplicate IDs / 160 stale; all 12 target records synchronized.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Orin Combo, Paralysis, Paralyze Beam, Pendulum Bullet, Perfect Kamehameha, Perfect Shot, Petrifying Spit, Phantom Fist, Photon Swipe, Potential Unleashed, Power Blitz, Power Impact; recompute the live stale queue before editing.


### 2026-09-23 correction — Orin-through-Power live census supersedes earlier same-cycle entry
- The earlier cycle entry was written before the canonical/index synchronization commit completed. The **authoritative post-write live census is 455 canonical / 455 index / 307 current / 148 stale / 0 duplicate IDs**.
- All 12 target records are now actually synchronized to 2026-09-23; target stale remaining: 0.
- Canonical/index commit: 43946d7ce293e7cbad4520729e737628fea71a76.
- Exact next batch: Power Pole Pro, Power Rush, Power Wall, Powered Shell, Prelude to Destruction, Prepare to be Punished, Present For You, Pressure Sign, Pretty Cannon, Pretty Charge, Prominence Flash, Psychic Move.


### 2026-09-23 cycle update — P1 Power Pole Pro through Psychic Move
- [x] Completed 12 skills: Power Pole Pro, Power Rush, Power Wall, Powered Shell, Prelude to Destruction, Prepare to be Punished, Present For You, Pressure Sign, Pretty Cannon, Pretty Charge, Prominence Flash, Psychic Move.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance/mechanics notes.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-power-pole-pro-through-psychic-move.json and refreshed the live stale census.
- [x] Validation: 455 canonical / 455 index / 0 duplicate IDs / 148 stale; target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Power Pole Pro, Power Rush, Power Wall, Powered Shell, Prelude to Destruction, Prepare to be Punished, Present For You, Pressure Sign, Pretty Cannon, Pretty Charge, Prominence Flash, Psychic Move; recompute the live stale queue before editing.


### 2026-09-23 — TODO completion update — P1 Psycho Barrier through Recoome Kick
- [x] Completed 12 skills: Psycho Barrier, Psycho Escape, Punisher Guard, Punisher Shield, Pure Progress, Purification, Quick Sleep, Raid Blast, Rakshasa's Claw, Ray Blast, Rebellion Spear, Recoome Kick.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance/mechanics notes.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-psycho-barrier-through-recoome-kick.json and refreshed the live stale census.
- [x] Validation: 455/455 / 0 duplicate IDs / 124 stale; target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Remote Serious Bomb, Requiem of Destruction, Revenge Death Ball, Revenge Final Flash, Reverse Launcher, Reverse Mabakusenko, Reverse Shot, Ribrianne's Eternal Love, Riot Javelin, Rise to Action, Rising Rage, Rocket Tackle; recompute the live stale queue before editing.


### 2026-09-23 — TODO completion update — P1 Remote Serious Bomb through Rocket Tackle
- [x] Completed 12 skills: Remote Serious Bomb, Requiem of Destruction, Revenge Death Ball, Revenge Final Flash, Reverse Launcher, Reverse Mabakusenko, Reverse Shot, Ribrianne's Eternal Love, Riot Javelin, Rise to Action, Rising Rage, Rocket Tackle.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance/mechanics notes.
- [x] Added/registered the dedicated provenance audit and refreshed the live stale census.
- [x] Validation: 455/455 / 0 duplicate IDs / 112 stale; target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Rolling Bullet, Rolling Hercule Punch, Rough Ranger, S.S. Deadly Bomber, Saiyan Blaster, Saiyan Spirit, Saturday Crash, Sauzer Blade, Savory Slicer, Scatter Kamehameha, Scissors Paper Rock, Seagull Combination; recompute the live stale queue before editing.


### 2026-09-23 — TODO completion update — P1 Rolling Bullet through Seagull Combination
- [x] Completed **12 skills**: Rolling Bullet, Rolling Hercule Punch, Rough Ranger, S.S. Deadly Bomber, Saiyan Blaster, Saiyan Spirit, Saturday Crash, Sauzer Blade, Savory Slicer, Scatter Kamehameha, Scissors Paper Rock, Seagull Combination.
- [x] Synchronized canonical/index `last_verified` to **2026-09-23** and appended bounded provenance-refresh notes while preserving existing acquisition, reward-tier, DLC, restriction, and unresolved-mechanics boundaries.
- [x] Refreshed `docs/data/skill-stale-metadata-census-2026-09-23.json` to the live **455 canonical / 455 index / 355 current / 100 stale / 0 duplicate IDs** state.
- [x] Prepared the bounded provenance audit payload for `docs/data/skill-provenance-audit-2026-09-23-rolling-through-seagull-combination.json`; repository connector write could not attach the new file to `main` after blob/tree creation, so no audit-file commit is claimed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next action: process **Secret Poison, Shadow Crusher, Shield Barrier, Shine Shot, Shining Friday, Shining Slash, Shooting Strike, Side Bridge, Sign of Awakening, Sneaky Strike, Soaring Fist, Soaring Rush** against their maintained source sets, synchronize canonical/index layers, add the bounded audit, and recompute the live stale census.


### 2026-09-23 — TODO completion update — P1 Secret Poison through Soaring Rush skill provenance/mechanics
- [x] Completed 12 skills: Secret Poison, Shadow Crusher, Shield Barrier, Shine Shot, Shining Friday, Shining Slash, Shooting Strike, Side Bridge, Sign of Awakening, Sneaky Strike, Soaring Fist, Soaring Rush.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded evidence notes using current skill references and independent corroboration.
- [x] Preserved the documented Shield Barrier reward-source conflict rather than replacing explicit Ultimate Finish evidence with a Basic Reward listing.
- [x] Refreshed docs/data/skill-stale-metadata-census-2026-09-23.json: 455 canonical / 455 index / 367 current / 88 stale / 0 duplicate IDs.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Audit blob was prepared, but final audit-file attachment/commit is still pending connector write-path completion.
- [ ] Exact next batch: Solar Flare, Sonic Bomb, Sonic Rush, Special Beam Cannon, Special Beam Cannon (Beast), Sphere of Destruction, Spirit Ball, Spirit Blaster, Spirit Bomb, Spirit Boost, Spirit Explosion, Spirit Pulse.


### 2026-09-23 — TODO completion update — P1 Solar Flare through Spirit Pulse skill provenance/mechanics
- [x] Completed 12 skills: Solar Flare, Sonic Bomb, Sonic Rush, Special Beam Cannon, Special Beam Cannon (Beast), Sphere of Destruction, Spirit Ball, Spirit Blaster, Spirit Bomb, Spirit Boost, Spirit Explosion, Spirit Pulse.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance/mechanics notes from maintained repository sources and current exact-name references.
- [x] Preserved documented reward-tier conflicts, including Special Beam Cannon (Beast), and did not infer unsupported probabilities or prerequisites.
- [x] Refreshed docs/data/skill-stale-metadata-census-2026-09-23.json: 455 canonical / 455 index / 379 current / 76 stale / 0 duplicate IDs.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Spirit Slash, Spread Shot Retreat, Steel Mirage, Stone Bullet, Strike of Revelation, Sudden Death Beam, Sudden Storm, Super Afterimage, Super Black Kamehameha Rosé, Super Donut Volley, Super Dragon Flight, Super Elite Combo.


### 2026-09-23 — TODO completion update — P1 Spirit Slash through Super Elite Combo
- [x] Completed 12 skills: Spirit Slash, Spread Shot Retreat, Steel Mirage, Stone Bullet, Strike of Revelation, Sudden Death Beam, Sudden Storm, Super Afterimage, Super Black Kamehameha Rosé, Super Donut Volley, Super Dragon Flight, Super Elite Combo.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance/mechanics notes using maintained repository evidence and current exact-name references.
- [x] Corrected the stale Stone Bullet note that called the skill a Ki Blast Super; current evidence and canonical class identify it as a Strike Super.
- [x] Refreshed docs/data/skill-stale-metadata-census-2026-09-23.json: 455 canonical / 455 index / 391 current / 64 stale / 0 duplicate IDs.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Super Explosive Wave, Super Gamma Blast, Super Ghost Buu Attack, Super Ghost Kamikaze Attack, Super Ghost Kamikaze Attack, Super God Fist, Super God Shock Flash, Super Guard, Super Kamehameha, Super Kamehameha (SS4 DAIMA), Super Saiyan, Super Saiyan 2.


### 2026-09-23 — TODO completion update — Super Explosive Wave through Super Saiyan 2
- [x] Completed the next 12 stale records: Super Explosive Wave, Super Gamma Blast, Super Ghost Buu Attack, both Super Ghost Kamikaze Attack records, Super God Fist, Super God Shock Flash, Super Guard, Super Kamehameha, Super Kamehameha (SS4 DAIMA), Super Saiyan, and Super Saiyan 2.
- [x] Synchronized canonical/index last_verified to 2026-09-23 and refreshed bounded provenance notes while preserving evidence boundaries and duplicate display-name records as distinct IDs.
- [x] Refreshed stale census: 455 canonical / 455 index / 403 current / 52 stale / 0 duplicate IDs.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Super Saiyan Blue Kaioken, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Spirit Bomb, Super Vegeta, Supernova, Supernova Cooler, Supersonic Mode, Supreme Fury, Surging Spirit, Symphonic Destruction.


### 2026-09-23 — TODO completion update — P1 Super Saiyan Blue Kaioken through Symphonic Destruction skill provenance
- [x] Completed 12 skills: Super Saiyan Blue Kaioken, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Spirit Bomb, Super Vegeta, Supernova, Supernova Cooler, Supersonic Mode, Supreme Fury, Surging Spirit, Symphonic Destruction.
- [x] Synchronized canonical/index `last_verified` to 2026-09-23 and refreshed bounded provenance notes while preserving existing evidence boundaries and conflicts.
- [x] Added/registered `docs/data/skill-provenance-audit-2026-09-23-super-saiyan-through-symphonic-destruction.json`.
- [x] Validation: 455/455 / 0 duplicate IDs / 40 stale / target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Tail Slicer, Taunt, Teleporting Vanishing Ball, Temporal Holy Ray, The Power to Overcome, The Savior Has Come, Thunder Flash, Time Bullet, Time Control, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike; recompute the live stale queue first.


### 2026-09-23 — TODO completion update — P1 Tail Slicer through Time Skip/Jump Spike
- [x] Completed 12 stale records: Tail Slicer, Taunt, Teleporting Vanishing Ball, Temporal Holy Ray, The Power to Overcome, The Savior Has Come, Thunder Flash, Time Bullet, Time Control, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike.
- [x] Synchronized canonical/index `last_verified` and provenance sources to 2026-09-23; appended bounded evidence notes without removing historical content.
- [x] Added/registered `docs/data/skill-provenance-audit-2026-09-23-tail-slicer-through-time-skip.json`.
- [x] Validation: 455/455 / 0 duplicate IDs / 28 stale / target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Time Skip/Tremor Pulse, Timespace Impact, Total Detonation Ball, Trap Shooter, Tri-Beam, Turn Golden, Tyrant Lancer, Ultimate Charge, Ultra Instinct, Ultrasonic Blitz, Unrelenting Barrage, Vanishing Ball; recompute the live stale queue first.


### 2026-09-23 — TODO completion update — P1 Time Skip/Tremor Pulse through Vanishing Ball
- [x] Completed 12 stale records: Time Skip/Tremor Pulse, Timespace Impact, Total Detonation Ball, Trap Shooter, Tri-Beam, Turn Golden, Tyrant Lancer, Ultimate Charge, Ultra Instinct, Ultrasonic Blitz, Unrelenting Barrage, Vanishing Ball.
- [x] Synchronized canonical/index provenance metadata to 2026-09-23 and preserved existing evidence conflicts/bounds.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-time-skip-tremor-pulse-through-vanishing-ball.json.
- [x] Validation: 455/455 / 0 duplicate IDs / 16 stale / target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Variable Snipe Shot, Variant Drive, Venus Fist, Victory Cannon, Victory Rush, Volleyball Fist, Wall of Defense, Warp Kamehameha, Weekend, Wild Buster, Wild Hunt, Wild Stinger; recompute the live stale queue first.


### 2026-09-23 — TODO completion update — P1 Variable Snipe Shot through Wild Stinger
- [x] Completed 12 stale records: Variable Snipe Shot, Variant Drive, Venus Fist, Victory Cannon, Victory Rush, Volleyball Fist, Wall of Defense, Warp Kamehameha, Weekend, Wild Buster, Wild Hunt, Wild Stinger.
- [x] Synchronized canonical/index provenance metadata to 2026-09-23 and preserved existing evidence conflicts/bounds.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-variable-snipe-shot-through-wild-stinger.json.
- [x] Validation: 455/455 / 0 duplicate IDs / 4 stale / target stale remaining 0.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: Wolf Fang Fist, X 100 Big Bang Kamehameha, x10 Kamehameha, Zigzag Express; recompute the live stale queue first.


### 2026-09-23 — TODO completion update — Wolf Fang Fist through Zigzag Express
- [x] Completed the final 4 stale skill records: Wolf Fang Fist, X 100 Big Bang Kamehameha, x10 Kamehameha, Zigzag Express.
- [x] Synchronized canonical/index provenance metadata to 2026-09-23 and preserved existing evidence bounds.
- [x] Added/registered docs/data/skill-provenance-audit-2026-09-23-wolf-fang-fist-through-zigzag-express.json.
- [x] Validation: 455/455 / 0 duplicate IDs / 0 stale; stale skill queue cleared.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Next: recompute broader TODO/handoff priorities and select the highest-impact unfinished cross-domain task.


### 2026-09-23 cycle update — Cross-database PQ reward/reverse-index consistency repair

- Recomputed the live PQ 1–186 canonical/reverse census across skills, Super Souls, equipment, characters, DLC, and farming.
- Found exactly one deterministic projection drift: stale unified reverse entry Super Soul “Do or Die” → PQ49. Canonical evidence establishes PQ49 “Do or Die” as the skill-domain record (skill-do-or-die) after the Super Soul 158 migration.
- Removed only the stale Do or Die: [49] entry from docs/data/pq-reward-normalization/pq-unified-reverse-index-1-186.json; canonical relationship data was not changed.
- Added/registering audit: docs/data/pq-cross-database-reverse-consistency-audit-2026-09-23.json.
- Post-repair validation: 244/244 skills, 145/145 Super Souls, 124/124 equipment, 247/247 characters, 86/86 DLC, and 7/7 farming pairs match exactly; 0 missing / 0 extra pairs across all domains.
- Updated docs/data/pq-cross-domain-index.json with the clean census.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: continue the wider repository consistency census, prioritizing deterministic producer/validator/index mismatches or large missing-field cohorts; preserve canonical source-of-truth and do not reopen the resolved PQ49/Do or Die migration.

### 2026-09-23 cycle update — Current skill non-PQ acquisition coverage census

- Recomputed the acquisition coverage against the live **455-record** canonical skill layer instead of relying on the historical 305-record projection.
- Found **239 PQ-linked / 216 without source_parallel_quests**.
- Of the 216 non-PQ-linked records, **130 already resolve through the canonical mentor-skill layer**, 12 are explicit mentor-like/training-style routes, 6 are Expert Mission routes, 10 are character-only routes, and 58 remain in other established non-PQ acquisition categories for targeted follow-up.
- The mentor crosslink layer has **131 mentor→skill edges / 130 unique skill targets** because **Super Explosive Wave** is legitimately shared by Future Gohan and Piccolo; this is not a duplicate edge.
- Preserved the historical fields in docs/data/skill-acquisition-coverage-report.json and added its current-state projection plus docs/data/skill-acquisition-coverage-current-audit-2026-09-23.json.
- No PQ relationships were inferred or added from non-PQ acquisition routes.
- Validation: arithmetic and mentor-sharing invariant pass; canonical skill count 455; no duplicate mentor edge pair detected.
- CI/runtime unavailable; no CI success claimed.
- **Exact next task:** audit the 58 remaining non-PQ skill records for deterministic acquisition-layer identity gaps, prioritizing Expert Mission/skill-shop/Time Rift/story consumers and avoiding already-resolved mentor routes.

### 2026-09-23 correction — Skill non-PQ coverage arithmetic

- Recomputed the set difference directly from the live canonical layers and corrected the prior projection's **58** figure.
- Correct current state: **455 canonical skills = 239 PQ-linked + 130 mentor-linked + 86 other non-PQ/non-mentor**; therefore **216** skills lack `source_parallel_quests`.
- The 58 figure was an arithmetic/category-overlap error in the projection only; canonical skill and acquisition data were not changed.
- Added `docs/data/skill-acquisition-coverage-correction-audit-2026-09-23.json` and preserved the prior report/history.
- Existing priority acquisition layers already contain the identified Expert Mission and shop route identities; no unsupported cross-domain or PQ edges were added.
- CI/runtime unavailable; no CI success claimed.
- **Exact next task:** audit the 86 non-PQ/non-mentor skills for missing stable cross-domain IDs/index consumers, beginning with Expert Mission and shop records, then Time Rift/story/tournament routes; prioritize actual producer/consumer mismatches over descriptive route duplication.

### 2026-09-23 cycle update — Skill acquisition cross-domain endpoint audit

- [x] Audited the live non-PQ skill acquisition endpoint consumers against `skills.json`, the Expert Mission acquisition index, and `advancement-tests.json`.
- [x] Verified all **18 Expert Mission acquisition-index records** resolve to canonical skill IDs, with deterministic EM03–EM20 endpoint IDs available for downstream consumers.
- [x] Verified all **4 Advancement Test skill links** resolve to canonical skill IDs and stable advancement-test IDs.
- [x] Added `docs/data/skill-acquisition-cross-domain-endpoint-audit-2026-09-23.json`.
- [x] No unsupported acquisition relationships or PQ edges were added.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** build/identify canonical endpoint layers for the largest remaining acquisition systems (Skill Shop / TP-STP Medal Shop first, then Time Rift/story/tournament), using stable IDs and linking existing skill records without duplicating canonical skills.

### 2026-09-23 — Canonical skill-shop endpoint layer
- [x] Built stable endpoint IDs for Skill Shop and TP/STP Medal Shop.
- [x] Projected **23** canonical skill acquisition edges: **12 Skill Shop + 11 TP/STP Medal Shop**.
- [x] Added `docs/data/skill-shop-endpoints.json` and `docs/data/skill-shop-endpoint-layer-audit-2026-09-23.json`.
- [x] Updated `docs/data/CROSS-LINK-CONTRACT.md` with the live shop endpoint baseline.
- [x] Preserved canonical skill IDs and evidence boundaries; no current-rotation or unsupported alternate-route claims were created.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** build the next highest-impact missing canonical acquisition endpoint layer, prioritizing **Time Rift/story/tournament**, then reconcile mentor/Expert Mission endpoint completeness.


### 2026-09-23 — TODO completion update — Time Rift / story / tournament endpoint layer
- [x] Added deterministic endpoints for 4 Time Rift systems, 2 story-mission systems, and 5 Conton City Tournament matches.
- [x] Added 14 canonical skill forward edges across 11 endpoints; all skill IDs resolve and endpoint/skill pairs are unique.
- [x] Added docs/data/time-rift-story-tournament-endpoints.json and docs/data/time-rift-story-tournament-endpoint-audit-2026-09-23.json.
- [x] Updated docs/data/CROSS-LINK-CONTRACT.md.
- [x] Preserved evidence boundaries; no Tokipedia, Patrol, or ambiguous Ultra Instinct relationship was invented.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** recompute the broader non-PQ acquisition census; prioritize Tokipedia/Patrol endpoint consumers where canonical evidence is sufficient, otherwise reconcile mentor/Expert Mission completeness and the remaining 7 legacy shop acquisition records.


### 2026-09-23 — TODO completion update — Acquisition classification normalization
- [x] Recomputed the live acquisition census across all 455 canonical skills.
- [x] Normalized 7 legacy `shop` records to `tp_medal_shop` using their explicit TP/STP Medal Shop source.
- [x] Normalized Giant Storm to `skill_shop` and Angry Explosion to `expert_mission` from their explicit canonical sources.
- [x] Synchronized the shop endpoint layer to **31 shop-linked skills: 13 Skill Shop + 18 TP/STP Medal Shop**.
- [x] Updated both acquisition audit data and preserved evidence boundaries.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** build/reconcile the dedicated Expert Mission and mentor endpoint layer, then address Tokipedia/Conton City Patrol endpoint consumers and cross-links.


### 2026-09-23 — TODO completion update — Expert Mission endpoint layer
- [x] Added stable EM03–EM20 acquisition endpoints.
- [x] Added 8 canonical Expert Mission→skill edges.
- [x] Captured 10 unresolved reward-name consumers without inventing IDs.
- [x] Added Expert Mission endpoint audit and contract baseline.
- [ ] Promote/reconcile the 10 unresolved Expert Mission skill identities.
- **Exact next task:** reconcile those 10 canonical skill gaps, then build Tokipedia and Conton City Patrol endpoint consumers.


### 2026-09-23 — TODO completion update — Expert Mission canonical promotion
- [x] Promoted the 10 previously unresolved EM reward identities into canonical `skills.json` records.
- [x] Reconciled EM endpoints to **18/18 canonical skill edges** with zero unresolved reward-name consumers.
- [x] Preserved uncertainty around exact drop rates and guarantee conditions.
- [x] Updated endpoint audit, cross-link contract, and persistent handoff.
- [ ] Build/reconcile dedicated mentor endpoint layer.
- [ ] Build/reconcile Tokipedia endpoint consumers and cross-links.
- [ ] Build/reconcile Conton City Patrol endpoint consumers and cross-links.
- **Exact next task:** mentor endpoint layer, followed by Tokipedia and Conton City Patrol endpoint consumers.


### 2026-09-23 — TODO completion update — Mentor endpoint layer
- [x] Added dedicated canonical mentor endpoint layer.
- [x] Linked 132 verified skill lesson rewards across 33 mentors; 131 unique skill endpoints.
- [x] Preserved the single typed non-skill Zamasu initiation reward without fabricating a skill link.
- [x] Added mentor endpoint audit and reverse lookup coverage.
- [ ] Reconcile official 32 vs community 33 mentor roster discrepancy.
- [ ] Build/reconcile Tokipedia endpoint consumers and cross-links.
- [ ] Build/reconcile Conton City Patrol endpoint consumers and cross-links.
- **Exact next task:** Tokipedia and Conton City Patrol endpoint consumers/cross-links.


### 2026-09-23 — TODO completion update — Tokipedia endpoint layer
- [x] Added deterministic Tokipedia endpoints for Confusion Blade, Sneaky Strike, Energy Minefield, and Remote Serious Bomb.
- [x] Added 4 forward edges and reverse skill→Tokipedia navigation.
- [x] Reconciled Energy Minefield's stale 60% source field to the evidence-backed 75% completion endpoint.
- [x] Added Tokipedia endpoint audit with zero broken canonical skill IDs.
- [ ] Build/reconcile Conton City Patrol endpoint consumers and cross-links.
- [ ] Reconcile official 32 vs community 33 mentor roster discrepancy.
- [ ] Audit remaining non-PQ/non-mentor acquisition records for deterministic endpoint gaps.
- **Exact next task:** Conton City Patrol endpoint consumer layer.


### 2026-09-23 — TODO completion update — Conton City Patrol endpoint layer
- [x] Added deterministic Conton City Patrol endpoints for Gigantic Cross, Saiyan Blaster, and Gigantic Nova.
- [x] Added 3 forward edges and reverse skill→Patrol navigation.
- [x] Added Patrol endpoint audit with zero broken canonical skill IDs.
- [x] Kept Patrol event routes distinct from mentor-training routes.
- [ ] Reconcile official 32 vs community 33 mentor roster discrepancy.
- [ ] Audit remaining non-PQ/non-mentor acquisition records for deterministic endpoint gaps.
- **Exact next task:** non-PQ/non-mentor acquisition endpoint census.


### 2026-09-23 — TODO completion update — Canonical skill/index parity repair after Expert Mission promotion
- [x] Recomputed the live skill layer and found a deterministic projection mismatch: **465 canonical skills vs 455 skill-index records**, with no index-only records.
- [x] Identified the exact 10 missing index records: Assault Rain, Blue Hurricane, Dead End Bullet, Death Meteor, Death Wave, Hellzone Grenade, Murder Grenade, Shocking Death Ball, Spirit Sword, and Super Electric Strike.
- [x] Synchronized docs/data/skills-index.json to **465 records**, using the existing index projection contract and preserving canonical evidence/uncertainty.
- [x] Added and registered docs/data/skill-index-canonical-parity-audit-2026-09-23.json.
- [x] Static parity result: **465/465 IDs, 0 index-only records, 0 duplicate canonical IDs, 0 duplicate index IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** recompute the broader non-PQ/non-mentor acquisition endpoint census now that canonical/index skill parity is restored; prioritize remaining deterministic producer/consumer gaps without reopening resolved Expert Mission records.


### 2026-09-23 cycle update — Special acquisition canonical endpoint layer

- Recomputed the non-PQ/non-mentor acquisition frontier after canonical skill/index parity repair and endpoint-layer work.
- Identified **14 remaining skill records** not represented by the existing PQ, mentor, Expert Mission, shop, Time Rift/story/tournament, Tokipedia, or Conton City Patrol endpoint consumers (excluding explicit character-only/startup records).
- Added `docs/data/special-acquisition-endpoints.json`: **14 deterministic endpoints / 14 forward skill edges / 14 unique canonical skill targets**, covering Beast, Namekian Become Giant, the two Shenron New Super Attack rewards, four Advancement Tests, Super Saiyan 2 stage access, Super Saiyan God wish/Beerus award, both Whis SSGSS routes, Ultra Instinct mastery challenge, and character-only Surging Spirit exposure.
- Added `docs/data/special-acquisition-endpoint-audit-2026-09-23.json`; validation passes with zero unresolved IDs and no duplicate endpoint/skill pairs.
- Registered the layer and audit in `docs/data/pq-cross-domain-index.json`.
- Evidence boundary preserved: endpoint identities are derived from canonical acquisition records; unsupported objectives, probabilities, exact timing, costs, or alternate routes were not invented.
- CI/runtime unavailable; no CI success claimed.
- **Exact next task:** recompute the full acquisition endpoint census including this new layer, then inspect the remaining explicit character-only/startup/non-acquirable records and broader cross-database producer/consumer gaps for deterministic link opportunities.


### 2026-09-23 cycle update — Full acquisition census and character-exclusive skill endpoint layer

- Recomputed the live acquisition endpoint census across PQ relationships plus mentor, Expert Mission, Skill Shop/TP-STP, Time Rift/story/tournament, Tokipedia, Conton City Patrol, and special-acquisition endpoint layers.
- Live canonical skill count: **465**. Existing non-PQ endpoint consumers cover **214 unique canonical skills via 215 forward edges**; PQ-linked canonical skills: **239**. The endpoint census leaves **0 non-PQ/non-mentor acquisition records without an endpoint consumer** after excluding explicit `character_only` and `starting_move` classifications.
- The remaining explicit character-only cohort was **10 skills**. Added `docs/data/character-exclusive-skill-endpoints.json` with **10 deterministic character/boss exposure endpoints / 10 forward edges / 10 unique skill targets**: Dragon Thunder, Energy Release, Final Charge, Final Flash (Super), Instant Charge, Pretty Charge, Pure Progress, Rising Rage, Super Saiyan Blue Kaioken, and Supersonic Mode.
- Added `docs/data/character-exclusive-skill-endpoint-audit-2026-09-23.json`; validation passes with **0 unresolved canonical skill IDs, 0 duplicate endpoint IDs, and 0 duplicate endpoint/skill pairs**.
- Registered the character-exclusive layer and audit in `docs/data/pq-cross-domain-index.json`.
- Evidence boundary preserved: these endpoints document cast/boss exposure only and do **not** convert character usage into CaC acquisition or shop/quest availability claims.
- CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** audit the remaining `starting_move` records and then perform a full endpoint↔canonical-skill reverse parity check, including duplicate semantic endpoints and skills that have multiple legitimate acquisition/exposure producers.


### 2026-09-23 cycle update — Starting-move endpoints and full reverse parity
- [x] Audited the two explicit `starting_move` canonical records: Afterimage and Super Guard.
- [x] Added `docs/data/starting-move-endpoints.json`: **2 deterministic character-creation endpoints / 2 forward edges / 2 unique skills**.
- [x] Preserved Super Guard's separate Skill Shop producer; the starting endpoint records only the character-creation route.
- [x] Added `docs/data/starting-move-endpoint-audit-2026-09-23.json`; validation passes with zero unresolved IDs and no duplicate endpoint/skill pairs.
- [x] Recomputed the complete endpoint reverse census: **465 canonical skills / 239 PQ-linked unique skills / 226 non-PQ endpoint-linked unique skills / 465 union coverage / 0 uncovered skills**.
- [x] Added `docs/data/full-skill-endpoint-reverse-parity-audit-2026-09-23.json` and documented the parity baseline in `CROSS-LINK-CONTRACT.md`.
- [x] Identified the only multi-producer skill collision pattern as intentional: Super Explosive Wave has two distinct mentor producers (Piccolo Lesson 1 and Future Gohan initiation); no duplicate skill identity was created.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** move from skill endpoint coverage to the next cross-database producer/consumer frontier: audit PQ ↔ skill, mentor ↔ skill, and character/preset ↔ skill navigation for orphaned or display-only links, prioritizing deterministic ID mismatches over descriptive enrichment.


### 2026-09-23 cycle update — Skill → character identity consumer audit
- [x] Audited all **227 canonical skill records** carrying `character_source`, yielding **232 source tokens**.
- [x] Resolved **187/232 source tokens** by exact canonical character-name match; **45 remain unresolved** as identity/variant or aggregate-source strings and were not guessed into the character bridge.
- [x] Separated explicit non-character/aggregate tokens such as `CaC / Universal`, multi-user aggregates, and Future Saga source wording from character identity gaps.
- [x] Added and registered `docs/data/skill-character-source-identity-audit-2026-09-23.json` as the bounded gap inventory.
- [x] Evidence boundary preserved: unresolved strings may represent valid cast variants, aliases, customize partners, or aggregate users; no canonical character identity was fabricated.
- [ ] Reconcile the unresolved character/variant source tokens against the canonical character roster and identity bridge in bounded batches.
- **Exact next batch:** reconcile the first bounded group of unresolved `character_source` identities (starting with high-confidence canonical-name variants/customize-partner forms), then add only evidence-backed skill→character reverse edges.


### 2026-09-23 cycle update — Skill→character identity bridge

- [x] Reconciled a bounded set of unresolved `skills.character_source` identities against the canonical character roster.
- [x] Added `docs/data/skill-character-identity-bridge-2026-09-23.json` with **7 resolved source entries / 8 canonical skill→character edges**.
- [x] Added `docs/data/skill-character-reverse-index-2026-09-23.json` for character→skill reverse navigation.
- [x] Added `docs/data/skill-character-identity-reconciliation-audit-2026-09-23.json` and registered the bridge/reverse index/audit in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **7 resolved skill records / 8 edges / 6 canonical character targets / 0 duplicate edges / 0 broken endpoints**.
- [x] Preserved evidence boundaries: Sonic Bomb remains unresolved because its source token says Champa while current skill documentation identifies Frieza; no conflicting identity was promoted.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** reconcile the next bounded unresolved `character_source` cluster, prioritizing exact canonical variant names and customize-partner identities; preserve conflict cases until independently resolved.


### 2026-09-23 cycle update — Second skill→character identity batch

- [x] Extended the bounded skill→character bridge by 7 additional skill records / 10 canonical edges.
- [x] Cumulative bridge: **14 resolved skill records / 18 canonical edges / 12 canonical character targets**.
- [x] Refreshed the unresolved identity inventory: **32 unresolved character/variant entries** remain.
- [x] Preserved conflicting source fields instead of fabricating identities: Destruction's Conductor, Photon Swipe, Total Detonation Ball, Sonic Bomb.
- [x] Updated bridge, reverse index, reconciliation audit, gap inventory, and persistent handoff.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** reconcile the next unresolved aggregate-user/customize-partner cluster with deterministic canonical identities where evidence permits.


### 2026-09-23 cycle update — Aggregate/customize-partner skill-character batch

- [x] Reconciled 6 additional unresolved source entries / 9 canonical skill→character edges.
- [x] Cumulative bridge: **20 resolved skill records / 27 canonical edges / 15 canonical character targets**.
- [x] Refreshed gap inventory: **26 unresolved character/variant entries remain**.
- [x] Preserved unresolved contradictions and non-character/CaC sources outside the identity bridge.
- [x] Updated persistent handoff and reconciliation audit.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** continue the remaining aggregate-user/variant cluster using exact canonical roster evidence.


### 2026-09-23 cycle update — Cell/Gohan/Super Destructo-Disc identity batch

- [x] Reconciled 4 additional skill→character source entries / 7 canonical edges.
- [x] Cumulative bridge: **24 resolved skill records / 34 canonical edges / 15 canonical character targets**.
- [x] Refreshed gap inventory: **22 unresolved character/variant entries remain**.
- [x] Updated bridge, reverse index, gap inventory, reconciliation audit, and persistent handoff.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** reconcile remaining variant/aggregate entries while preserving contradictory Toppo/Android 21, Champa/Vados/Frieza, and Ultra Supervillain source evidence.


### 2026-09-23 cycle update — Meteor Strike / Android 21 / Vegeta / Majin identity batch

- [x] Reconciled 5 additional skill→character entries / 7 canonical edges.
- [x] Cumulative bridge: **29 resolved skill records / 41 canonical edges / 15 canonical character targets**.
- [x] Refreshed gap inventory: **17 unresolved character/variant entries remain**.
- [x] Explicitly preserved legacy Toppo source tokens for Photon Swipe and Total Detonation Ball while mapping their current documented user to Android 21.
- [x] Updated bridge, reverse index, gap inventory, reconciliation audit, handoff, and TODO.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** reconcile remaining unresolved entries with deterministic canonical identities and explicit conflict preservation.


### 2026-09-23 cycle update — Third bounded skill→character identity batch
- [x] Reconciled **Sauzer Blade → Jeice**, **Spirit Explosion → Cooler (Final Form)**, and **Spread Shot Retreat → Frieza (1st Form)**.
- [x] Refreshed the canonical skill→character bridge to **32 resolved skill records / 43 canonical edges / 32 canonical character targets**.
- [x] Refreshed the reverse index and gap inventory; **7 unresolved character/variant entries** remain.
- [x] Preserved source wording and evidence boundaries; no exhaustive equipability claims were inferred from the source-token bridge.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** assess canonical character-layer promotion/reconciliation for **Goku (Ultra Supervillain Quelled)** and **Vegeta (GT)**, then continue the remaining unresolved/conflict entries without fabricating identities.


### 2026-09-23 cycle update — Future Saga character-layer promotion and identity batch

- [x] Promoted **Goku (Ultra Supervillain Quelled)** into the canonical character layer using current official Future Saga Chapter 4 evidence.
- [x] Promoted **Vegeta (GT)** from the existing DLC character inventory into the canonical character-name layer.
- [x] Reconciled **Dragon Spiral**, **Indomitable**, and **Venus Fist** → Goku (Ultra Supervillain Quelled).
- [x] Reconciled **Wild Buster** → Vegeta (GT).
- [x] Refreshed bridge/reverse-index totals to **36 resolved skill records / 47 edges / 34 canonical character targets**.
- [x] Reduced unresolved character/variant identity entries to **3**.
- [x] Preserved the remaining Destruction's Conductor, Flash Chaser, and Sonic Bomb source conflicts without rewriting provenance fields.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** dedicated provenance reconciliation of the final 3 conflicting character_source fields.


### 2026-09-23 cycle update — Final skill character-source provenance reconciliation

- [x] Corrected **Destruction's Conductor → Vados** after current skill-user verification.
- [x] Corrected **Flash Chaser → Majuub** after current skill-user verification.
- [x] Corrected **Sonic Bomb → Frieza (1st Form)** after current skill-user verification.
- [x] Updated skills.json provenance fields and preserved documented Customize Partner users in notes/bridge evidence.
- [x] Identity bridge now contains **39 resolved skill records / 50 canonical edges / 36 canonical character targets**.
- [x] Character-source identity audit now has **0 unresolved character/variant entries** in its governed scope.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** advance from the completed skill-character identity phase to the next highest-priority exhaustive cross-domain/link-integrity task.


### 2026-09-23 cycle update — PQ cross-database navigation synchronization

- [x] Synchronized `docs/data/pq-skill-crosslink-report.json` to the live **465-skill** canonical layer.
- [x] Preserved **244 forward PQ→skill edges / 239 unique skill endpoints**, with **0 unresolved** and **0 orphan reverse** endpoints.
- [x] Verified the Kamehameha PQ48 relationship is an intentional additional producer while PQ5 remains its primary declared source route.
- [x] Synchronized PQ character reverse-navigation audit to the live **151-character** canonical layer.
- [x] Character navigation remains clean: **0 missing targets / 0 orphan reverse targets / 0 duplicate forward pairs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** audit **mentor↔skill** producer/consumer navigation, then **character/preset↔skill** navigation, focusing on deterministic ID mismatches and orphaned reverse links.


### 2026-09-23 cycle update — Mentor↔skill producer/consumer navigation

- [x] Audited all **33** canonical mentor IDs against explicit skill source_mentor references.
- [x] Populated mentors.json.skills as the deterministic reverse navigation layer.
- [x] Added mentor-skill crosslink audit: **137 edges / 134 skills / 0 invalid IDs / 0 duplicates / 0 orphan mentors / 0 non-reciprocal links**.
- [x] Preserved the **3 multi-mentor skills** as explicit multi-source relationships.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** audit **character/preset↔skill navigation**, focusing on deterministic character identity endpoints, character-source fields, and legitimate multi-user relationships.


### 2026-09-23 cycle update — Character/preset↔skill navigation audit
- [x] Audited 40 preset records / 12 distinct presentation character IDs against the explicit character identity bridge; 12/12 resolve to canonical character names.
- [x] Audited character-source skill identity coverage against the existing 39 resolved skill records / 50 canonical character-source edges.
- [x] Found 5 preset characters with currently resolved character-source skill identities and 7 without; the 7 are evidence gaps, not broken links, because the skill-character bridge is intentionally scoped to resolved source identities.
- [x] Confirmed preset loadouts remain explicitly unresolved, so no unsupported preset→equipped-skill edges were promoted.
- [x] Added and registered docs/data/character-preset-skill-navigation-audit-2026-09-23.json.
- [x] Validation: 0 unbridged preset character IDs / 0 duplicate preset records / 0 duplicate numbered character-preset pairs / 0 unsupported loadout-skill promotions.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** audit the broader character/preset presentation consumers for deterministic identity/search parity, then pursue source-backed preset loadout evidence only where the repository has an explicit loadout source.


### 2026-09-23 cycle update — Character presentation consumer validator hardening
- [x] Inspected live character/preset presentation consumers after the character↔skill audit.
- [x] Hardened `scripts/validate_character_presentation_consumers.py` so the core-profile search-design check recognizes the repository's `searchUrl(` implementation as well as the `Search/` marker, avoiding a false unresolved result.
- [x] Re-read the live identity bridge: 29 explicit character IDs / 29 unique canonical targets; no duplicate bridge identities observed.
- [ ] CI/runtime unavailable; validator execution not claimed.
- **Exact next task:** run/replicate the character presentation consumer audit when executable runtime is available, then expand deterministic character/preset navigation coverage without inventing preset loadouts.


### 2026-09-23 cycle update — Character presentation consumer audit hardening
- Live census: **151 canonical characters / 29 explicit identity-bridge records / 40 preset records / 20 Partner Customization records**.
- Hardened `scripts/validate_character_presentation_consumers.py` again: the explorer navigation check now correctly keys on the actual `searchUrl(name)` implementation instead of requiring an unrelated `Search/` token; static `Character-Core-Profiles.md` content is no longer treated as a search UI consumer merely because it lacks that token.
- Live structural checks: bridge uniqueness, canonical targets, all 12 preset character IDs bridged, all 20 partner IDs bridged, partner reconciliation parity, preset uniqueness, preset-number pair uniqueness, canonical explorer link, explorer search implementation, and no hard-coded preset labels all remain clean.
- The prior audit correctly exposed the validator mismatch; no data records were changed and no unsupported loadout links were introduced.
- Validator execution remains unavailable in the hosted environment; the equivalent live census was manually replicated against the current files. CI remains unavailable.
- Commit: 34f499a43f82e4e25106ad451b4039269167bf92.
- **Exact next batch:** inspect the remaining character-facing generated/index consumers for deterministic canonical-ID parity, especially any pages/data projections not covered by this validator, before expanding preset loadout research.


### 2026-09-23 cycle update — Character presentation projection synchronization
- Live census exposed stale metadata in `docs/data/characters/character-presentation-consumer-audit.json`: the repository is now **151 canonical characters / 40 preset records / 12 distinct preset character IDs / 20 Partner Customization records**.
- Hardened `scripts/validate_character_presentation_consumers.py` so omitted `record_type` is treated as the existing implicit `preset` contract; only explicitly invalid record types are rejected. This prevents false failures for ordinary preset records that omit the optional field.
- Synchronized the character presentation audit's live canonical/preset counts and validator commit reference; no character identity or loadout data was inferred or changed.
- Manual structural parity remains clean for the inspected consumer set: bridge targets, preset/partner IDs, reconciliation parity, explorer linkage, and uniqueness checks are intact.
- Validator/CI execution remains unavailable in this hosted session; no execution or CI success is claimed.
- Commits: validator `9602b41f2979c10321774afeb5c4d11e500d6056`; audit `ebcf61f810999ba209272958a2e7e5a3e410cfc3`.
- **Exact next batch:** inspect remaining character-facing projections and validators for stale-count or implicit-field assumptions, then consolidate their live parity into the presentation audit before beginning explicit preset-loadout evidence research.


### 2026-09-23 cycle update — Character DLC projection parity repair
- Live inspection found three stale character-facing projections still using the previous **149-character** baseline: `docs/Characters.md`, `docs/data/characters/dlc-character-identity-audit.json`, and `docs/data/characters/published-character-dlc-navigation-audit.json`.
- The canonical layer now contains **151** names, including the newly canonical `Goku (Ultra Supervillain Quelled)`. Its DLC source label was therefore deterministically resolved to that exact canonical identity; `Supreme Kai of Time (Ultra Supervillain)` remains explicitly unresolved because only the base `Supreme Kai of Time` is canonical and collapsing the variant would be unsupported.
- Synchronized the three affected projections/audits to the current canonical layer. No unrelated DLC ownership or acquisition facts were changed.
- Validation: live canonical count 151; DLC bridge remains 15 source records with 14 resolved targets and 1 explicit unresolved label; no missing canonical targets introduced. CI/runtime remains unavailable; no CI success claimed.
- Commits: bridge `14a328ecedc720ccaaf2ece46b582d6a474ab77d6`; Characters page `434b1c0e28aaa994228bb49202ef1755f8a9cc01`; identity audit `8a6c1b2b352ef3593de7bebf52bfe94fa78fdb27`; published navigation audit `a287750d42078cab5bb29a52beadbd4589d169f7`.
- **Exact next batch:** continue searching character-facing projections for the old 149 baseline and inspect any remaining validators/audits that assume fixed counts; after that, begin source-backed preset-loadout research only for records with explicit loadout evidence.


### 2026-09-23 cycle update — Character-facing stale baseline cleanup
- [x] Rechecked the remaining character-facing projections after the 151-character canonical promotion.
- [x] Hardened `scripts/validate_published_character_dlc_navigation.py` so canonical character validation derives uniqueness from the live roster instead of a hard-coded 149-character count.
- [x] Synchronized `docs/data/characters/partner-customization-character-navigation-audit.json` and the nested Partner Customization census in `docs/data/characters/character-presentation-consumer-audit.json` from 149 to the live **151** canonical characters.
- [x] Preserved the existing bridge, partner, preset, DLC, and unresolved-variant evidence; no new character identity or preset loadout was inferred.
- [x] Manual post-write inspection: validator no longer contains the stale 149-character assertion; affected audits report the live 151-character baseline.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** search the remaining character-facing generated/index consumers and validators for stale fixed-count assumptions or one-way links; then begin source-backed preset-loadout research only for records with explicit loadout evidence.


### 2026-09-23 cycle update — First explicit preset-loadout evidence batch
- [x] Rechecked remaining character-facing projections and confirmed the canonical Character page and PQ character reverse audit now use the live **151-character** layer; the character category index's 155/54 values remain source-category counts, not canonical-roster baselines.
- [x] Promoted **Frieza (Final Form) Preset 2** from indexed/unresolved loadout status to an explicit verified loadout using the repository's existing character-profile evidence and the current Frieza (Final Form) in-game-data table.
- [x] Recorded the seven sourced skill entries: **Death Slash, Death Beam, Death Psycho Bomb, Maximum Charge, Full Power Energy Blast Volley, Death Ball, Psychic Move**, plus Super Soul **Gotcha!**; no acquisition or exclusivity claim was inferred from preset presence.
- [x] Updated `docs/data/character-preset-skill-navigation-audit-2026-09-23.json` with the verified-loadout record and evidence boundary.
- [x] Hardened `scripts/validate_character_presentation_consumers.py` so any preset marked `loadout_status=verified` must contain a structured loadout and explicit loadout source.
- [x] Manual post-write inspection: the verified Frieza record has an explicit loadout/source; the remaining indexed preset records remain unresolved.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Commits:** preset `9e351599d2fec6de76528240c419677cbfe7954e`; audit `bebd53de9b4eecaa5af4c17bb10e6f1b0a7a6534`; validator `84c2c29fe6faa1bb70fda2422011a88f48615319`.
- **Exact next batch:** reconcile another **4–8 preset loadouts** only where explicit in-game-data tables or equivalent item-level evidence exists; prioritize records already represented in `docs/Character-Core-Profiles.md` or directly covered by the existing preset source corpus, and keep all unsupported loadouts unresolved.


### 2026-09-23 cycle update — Six additional explicit preset-loadout promotions
- [x] Revalidated the preset source corpus against current character in-game-data tables.
- [x] Promoted **6 additional** preset records to explicit verified loadouts: Vegeta Presets 2, 3, 6, and 7; Gohan (Adult) Preset 3; Frieza (1st Form) Preset 2.
- [x] Combined with the prior Frieza (Final Form) Preset 2 promotion, the live preset layer now contains **7 verified loadouts / 40 total preset records / 33 still unresolved**.
- [x] Recorded the exact sourced skill slots and Super Souls where explicitly present; blank Awoken/Evasive/Super Soul slots remain null rather than being inferred.
- [x] Updated `docs/data/character-preset-skill-navigation-audit-2026-09-23.json` to **7 verified loadout records / 44 skill entries** and corrected its JSON structure.
- [x] Manual post-write inspection confirmed every verified record has a structured loadout and explicit loadout source.
- [x] External source verification: the current Vegeta table explicitly enumerates Battle Suit 1–9 loadouts; Gohan (Adult) explicitly enumerates its numbered presets; Frieza (1st Form) explicitly enumerates Battle Suit 2. cite
- [ ] CI/runtime unavailable; no CI success claimed.
- **Commits:** preset layer `c3f2eabd39b59466458a45be7f7d1c68ac4e40e8`; corrected audit `cdbc3128d7bbe5c8487c77c05ea421eec5535e3f`.
- **Exact next batch:** continue with another **4–8 explicit preset records**, prioritizing Goku and other records whose numbered in-game-data tables can be matched unambiguously to the existing preset IDs; do not promote Festival/custom-partner configurations as ordinary numbered presets.


### 2026-09-23 cycle update — Goku preset evidence boundary review
- [x] Reviewed the current Goku in-game-data table as the next high-priority preset source.
- [x] Confirmed the source provides complete named loadouts across Goku's many rows, including Turtle Hermit Gi, King Kai, Goku (Go), No Character, and Whis Symbol configurations. cite
- [x] **Did not promote Goku's numeric repository records** because `goku-preset-2` through `goku-preset-16` do not have an explicit source mapping to those named table rows. Row-order conversion would be an unsupported inference.
- [x] Added this evidence boundary to `docs/data/character-preset-skill-navigation-audit-2026-09-23.json`.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Commit:** `01a3034be79033856a1b61bad8db32951a5cc06d`.
- **Exact next task:** find an explicit numeric/name mapping for Goku or move to another indexed preset whose source directly identifies the same preset number/name; continue promoting only unambiguous records.


### 2026-09-23 cycle update — Vegito explicit preset-loadout promotion
- [x] Verified **Vegito Preset 2** directly against the current Vegito in-game-data table: Super Dragon Fist / Kamehameha / Instant Transmission / Charged Ki Wave; Super Kamehameha / Spirit Sword; Spirit Explosion; no Super Soul listed. cite
- [x] Verified **Vegito Preset 3** directly against the same table: Sledgehammer / Big Bang Attack / Finish Breaker / Full Power Charge; Final Flash / Spirit Sword; Explosive Wave; no Super Soul listed. cite
- [x] Updated the preset record layer and cross-domain audit to **9 verified preset loadouts / 58 verified skill-slot entries**.
- [x] Repaired the audit JSON separator exposed during the update and re-parsed the resulting document successfully before committing.
- [x] Kept Festival/custom-partner configurations separate and made no acquisition/exclusivity claims from preset presence.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Commits:** preset layer `f429351c1f1bc5256a3c5b60de2993ccdb6adfff`; audit `4b2bfb28154f3f20250a03c4a44fdef37671c8bc`.
- **Exact next task:** continue with another bounded batch of explicit numbered/name-matched preset records; Goku remains unresolved until a source explicitly maps its repository numeric IDs to the named source rows.

### 2026-09-23 cycle completion tracking — Vegeta/Captain Ginyu preset-loadout batch
- [x] Vegeta Preset 8 explicit loadout verification
- [x] Captain Ginyu Presets 2, 3, and 4 explicit loadout verification
- [x] Canonical preset layer updated without changing canonical character identities
- [x] Cross-domain preset↔skill audit updated to 13 verified loadouts / 83 skill-slot entries
- [x] Captain Ginyu Trunks-body naming discrepancy preserved explicitly
- [ ] CI/runtime remains unavailable; no CI success claimed
- [ ] Next batch: continue source-backed numbered/name-matched preset reconciliation; do not infer Goku numeric mappings from named rows.

### 2026-09-23 cycle completion tracking — Bardock preset-loadout batch
- [x] Bardock Preset 1 explicit loadout verification
- [x] Bardock Preset 2 explicit loadout verification
- [x] Bardock Preset 3 explicit loadout verification
- [x] Bardock Preset 4 explicit loadout verification
- [x] Preset navigation audit expanded to 44 records / 17 verified loadouts
- [x] Bardock loadout provenance linked to the character in-game-data source
- [ ] CI/runtime remains unavailable; no CI success claimed
- [ ] Next batch: continue explicit in-game-data preset reconciliation; do not infer Goku numeric mappings.

### 2026-09-23 cycle completion tracking — Raditz/Nappa preset-loadout batch
- [x] Raditz Preset 1 explicit loadout verification
- [x] Nappa Preset 1 explicit loadout verification
- [x] Preset layer expanded to 46 records / 19 verified loadouts
- [x] Navigation audit expanded to 123 verified loadout skill entries
- [ ] CI/runtime remains unavailable; no CI success claimed
- [ ] Next batch: continue exact Battle Suit preset reconciliation.

### 2026-09-23 cycle completion tracking — Recoome
- [x] Recoome Presets 1–2 explicit loadout verification
- [x] Preset layer expanded to 48 records / 21 verified loadouts
- [x] Navigation audit expanded to 137 verified skill entries
- [ ] CI/runtime unavailable
- [ ] Next: exact Battle Suit reconciliation for another unresolved character.

### 2026-09-23 cycle completion tracking — Zarbon
- [x] Zarbon Presets 1–2 explicit loadout verification
- [x] Preset layer expanded to 50 records / 23 verified loadouts
- [x] Navigation audit expanded to 151 verified skill entries
- [ ] CI/runtime unavailable
- [ ] Next: exact Battle Suit reconciliation for another unresolved character.


### 2026-09-23 cycle update — Preset navigation audit canonical-list synchronization

- Live canonical preset layer: **50 preset records / 23 verified loadouts / 27 unresolved loadouts**.
- Deterministically repaired `docs/data/character-preset-skill-navigation-audit-2026-09-23.json`: the JSON contained duplicate `verified_preset_loadouts` keys, so the parsed audit exposed only a partial list despite reporting 23 records. Rebuilt the authoritative verified-loadout list directly from `character-presets-record-layer.json` records with `loadout_status=verified`.
- Corrected verified loadout skill-entry census from the stale **148** to **130** unique verified loadout slot entries represented by the canonical preset records.
- Preserved all existing preset identities, body-swap evidence boundaries, sources, and unresolved records; no new preset was promoted.
- Validation: audit JSON reparsed after write; verified-loadout count matches the canonical preset layer (**23**); every verified record has an explicit loadout source; no unresolved preset was promoted.
- CI/runtime remains unavailable; no CI success claimed.
- Commit: `395e30de930397b39cfb1fcafd20b05b78439416`.
- **Exact next batch:** continue exact Battle Suit preset reconciliation for unresolved characters with explicit in-game-data tables; do not infer numeric/name mappings from row order.


### 2026-09-23 cycle update — Exact Battle Suit observation layer

- Added `docs/data/preset-battle-suit-reconciliation-2026-09-23.json`.
- Preserved two explicitly documented Vegeta Battle Suit loadout observations whose repository numeric preset mapping is not established: one with Meteor Strike/Galick Gun/Spirit Boost/Charged Ki Wave/Super Galick Gun/Spread Shot Retreat, and one with Sledgehammer/Energy Wave Combo/Shine Shot/Energy Charge/Full Power Energy Wave/Explosive Wave.
- Kept Vegeta Preset 8 linked only to its already verified exact record; no unresolved numeric preset was promoted from row order or costume ordering.
- This creates a safe evidence bridge for future skill↔preset connectivity without inventing numeric mappings.
- Commit: `8ee2bb5a803850e3ed1ae35bbdc452c2933c2d5d`.
- **Next exact task:** search for explicit numeric/game-data identifiers for the unresolved Vegeta Battle Suit rows and reconcile only exact matches.


### 2026-09-23 cycle update — Vegeta Battle Suit exact preset reconciliation

- Used the live Vegeta in-game-data table as explicit numeric evidence: **Battle Suit 1, Battle Suit 2, and Battle Suit 9** are directly labeled by preset number. cite
- Promoted `vegeta-preset-1` from absent/unresolved to a fully sourced verified record with Meteor Strike / Galick Gun / Spirit Boost / Charged Ki Wave / Super Galick Gun / Spread Shot Retreat and Super Soul `I am the universe's strongest!`.
- Reconciled the existing `vegeta-preset-2` evidence to the explicit Battle Suit 2 source row rather than relying on row order.
- Promoted `vegeta-preset-9` to verified with Galaxy Breaker (Festival) / Flash Strike / Shine Shot / Burst Charge / Super Galick Gun / Spread Shot Retreat and the documented Super Soul.
- Updated `docs/data/preset-battle-suit-reconciliation-2026-09-23.json` so configurations A/B are now exact Battle Suit 1/2 mappings; the evidence boundary remains explicit-source-label-only.
- Live Vegeta verified preset loadouts now include **1, 2, 3, 6, 7, 8, and 9**; unresolved indexed records remain **10 and 11**.
- Commits: canonical preset layer `99758df9c4ed283b51862e9d02a05efcfcad8a02`; reconciliation layer `ec9d01950a8750377ce4dea352a61752523bf982`; Battle Suit 9 canonical update `1a2bf906e24842e0881ec0e73038b1c553f1a7f3`.
- **Exact next task:** reconcile Vegeta Presets 10 and 11 from explicit source rows or matching game-data identifiers only; do not infer from ordering.


### 2026-09-23 cycle update — Vegeta Presets 10/11 evidence-boundary audit

- Searched the live repository for explicit Vegeta Preset 10 / Battle Suit 10 and Preset 11 / Battle Suit 11 identifiers and loadout rows.
- The current repository only exposes these as indexed numeric records backed by the community-observation video; no explicit source-row loadout or matching game-data key was found in the repository search results.
- Preserved both records as unresolved rather than inventing loadouts or assigning values by preset order.
- Added the unresolved 10/11 observations to docs/data/preset-battle-suit-reconciliation-2026-09-23.json with the exact evidence limitation.
- External direct access to the Fandom Vegeta page was blocked during this cycle, so no external source claim was promoted into canonical data.
- Commit: b29292f3cb7fff8dec04e3ad9045024c1f9eff11.
- Exact next task: inspect the repository's producer/source corpus and any explicit game-data identifiers for Battle Suit 10 and 11; populate only exact matches.


### 2026-09-23 cycle update — External Vegeta preset-count boundary confirmed

- Checked the current external Vegeta in-game-data table: it explicitly lists Battle Suit 1 through 9, Training Suit 1 and 2, and Whis Symbol Battle Suit, while the page metadata reports 11 presets. cite
- The retrieved table does **not** expose explicit Battle Suit 10 or 11 rows. Therefore the repository's numeric 10/11 records remain unresolved rather than receiving inferred loadouts.
- Added this evidence boundary to `docs/data/preset-battle-suit-reconciliation-2026-09-23.json`.
- Commit: `72c73a62768f0428ffda7f81ad13ac9381c88006b`.
- **Next task:** move to the next highest-priority preset/data-quality task unless explicit game-data identifiers for 10/11 are discovered; do not fabricate missing loadouts.


### 2026-09-23 cycle update — PQ endpoint navigation current-baseline synchronization
- [x] Recomputed the live PQ endpoint/navigation baseline after the 465-skill, 234-Super-Soul, 173-equipment/accessory, and 151-character expansions.
- [x] Corrected the current-state fields in `docs/data/pq-endpoint-navigation-validation.json` from the superseded 452/149/854/146 snapshot to **465 skills / 234 Super Souls / 173 equipment-accessory / 151 characters / 853 total PQ relationship edges / 142 unique Super Soul reverse targets**.
- [x] Preserved older baseline values as historical context rather than deleting history.
- [x] Added and registered `docs/data/pq-endpoint-navigation-current-baseline-audit-2026-09-23.json`.
- [x] Validation: JSON reparsed; endpoint counts match the canonical relationship baseline; no reward relationship or identity was added or removed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [x] Commits: validation `f202b61a6033d2155ba596286981a805b95ee046`; audit `d615a237d038ff4822891f335b1150f8f41eb648`; registration `a3bc8cebbf9a2944259cae1cab2f99326cfddeb2`; handoff `2069c1d8fca821c165939a2c2a249698956712db`.
- **Exact next task:** continue the broader deterministic producer/consumer census beyond the PQ endpoint validator, prioritizing remaining current-state projections with superseded skill/character/domain counts; then return to source-backed preset-loadout reconciliation only where explicit loadout evidence exists.


### 2026-09-23 cycle update — Skill stale-metadata census synchronization
- [x] Found and repaired the stale **452** canonical-skill count in `docs/data/skill-stale-metadata-census-2026-09-22.json`.
- [x] Synchronized the census to **465** live canonical skills (**191 stale / 274 current** verification-date records as of 2026-09-23).
- [x] Preserved the evidence boundary and made no unsupported canonical skill-data changes.
- [x] Validation: JSON reparsed; stale+current = 465.
- [ ] CI/runtime unavailable; no CI success claimed.
- [x] Commit: `79316983821a2171396c3aa14d3699787bc435d7`.
- **Exact next task:** continue deterministic census of remaining superseded current-state counts, especially 854 historical/current-baseline consumers, then resume source-backed preset reconciliation.


### 2026-09-23 cycle update — Remaining 854 current-consumer synchronization
- [x] Corrected stale current 854-edge metadata in `pq-endpoint-alias-granularity-map.json` to **853**.
- [x] Corrected stale 452 skill-count metadata in `skill-pq-acquisition-presentation-audit.json` to **465**.
- [x] Synchronized current consumer entries in the single-source reconciliation and non-PQ consumer census to **853 total / 145 Super Soul**; preserved historical snapshots.
- [x] Updated the cross-domain index current baseline to 853.
- [x] Revalidated changed JSON; no relationship data was inferred or changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [x] Handoff recorded in `docs/AI-CONTINUATION-PROMPT.md` (commit `70f1e371b4e354e3a8cc02c09e1c863c2b0bfac8`).
- **Exact next task:** exact-pair parity scan of remaining reverse/navigation projections for stale 853/145/465 assumptions, followed by explicit source-backed preset reconciliation.


### 2026-09-23 cycle update — Exact-pair reverse/navigation parity synchronization
- [x] Corrected current Super Soul parity in the PQ explorer audit to **145** canonical/structured edges.
- [x] Corrected Super Soul reverse-navigation parity to **145 forward / 142 unique targets**.
- [x] Corrected PQ endpoint identity current baseline to **853 total / 145 Super Soul / 142 unique targets**.
- [x] Re-scanned remaining 146 occurrences and retained historical/reconciliation evidence.
- [x] JSON validation passed; no canonical relationship changes.
- [ ] CI/runtime unavailable; no CI success claimed.
- [x] Handoff recorded with commit `e9382743aec834e830fc78a7ff6533d4528bbb52`.
- **Exact next task:** parity scan remaining skill/character/domain navigation projections, then explicit source-backed preset reconciliation.


### 2026-09-23 cycle update — Full canonical skill verification-date synchronization
- [x] Refreshed the ten Kai-through-Light canonical skill records to 2026-09-23 using existing source-backed provenance evidence.
- [x] Live parse confirms **465/465 current, 0 stale, 0 duplicate IDs** in `docs/data/skills.json`.
- [x] Repaired the primary stale-metadata census and provenance audit baselines accordingly.
- [x] No unsupported canonical skill facts or relationship edges were introduced.
- [ ] CI/runtime unavailable; no CI success claimed.
- [x] Handoff recorded in `docs/AI-CONTINUATION-PROMPT.md` with commit `7ed9ae4117c8b2a09d0a03c2971bfda27c568327`.
- **Exact next task:** continue P1 provenance/data-quality audits for remaining dated/stale domain artifacts and explicit source-backed data gaps; preserve historical snapshots.


### 2026-09-23 cycle update — Unified reverse-index current-baseline synchronization
- [x] Audited `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json` against the current canonical PQ relationship layer.
- [x] Corrected current live projection/reconciliation metadata from the superseded **854 total / 146 Super Soul** baseline to **853 total / 145 Super Soul**.
- [x] Preserved the superseded 854/146 values as explicit historical snapshots.
- [x] Confirmed exact-pair parity remains **0 missing / 0 extra** for skills, Super Souls, equipment, characters, DLC, and farming.
- [x] Preserved the current equipment split at **84 clothing / 40 accessories / 124 combined**.
- [x] Updated runtime wording so API-level static parity is not claimed as CI/runtime success.
- [ ] CI/runtime unavailable; no CI success claimed.
- Commit: `7f2682d6747894a63f0da932654e2f06c54b2f59`.
- **Exact next task:** continue the broader current-state producer/consumer census for remaining superseded 854/146 and older skill/character/domain counts, then return to exact-evidence preset reconciliation.


### 2026-09-23 cycle update — Second current-consumer census pass
- [x] Searched live repository for remaining 854/146 assertions after the unified reverse-index repair.
- [x] Corrected current-looking standalone reverse-index reconciliation metadata to **853 / 145**, preserving the pre-migration block as historical context.
- [x] Corrected current-looking producer-census assertions to **853 / 145**.
- [x] Refreshed reverse-PQ navigation continuation metadata to target the current canonical layer.
- [x] Classified remaining search hits as predominantly historical/correction evidence; no blind rewriting performed.
- [ ] Inspect remaining 854/146 hits individually and repair only any still-current-looking consumers.
- Commits: `a53eaf99b5ff62b807bd2a9abd4d118a26500562`, `2d7e6cd7f0d02fdb1f44c079c4b7a6f43f18a243`, `fcad966ac7446c212cc18cd4ed7a016ea7b6ba73`.
- **Exact next task:** finish classification/repair of remaining 854/146 search hits, then resume P1 provenance/data work and exact-evidence preset reconciliation.


### 2026-09-23 cycle update — Third current-consumer census pass
- [x] Re-scanned and individually inspected remaining current-looking 854/146 cross-domain consumers.
- [x] Repaired `pq-cross-domain-status.json` current reconciliation/master/Super Soul projections to 853/145 (145/142 reverse).
- [x] Repaired `pq-cross-domain-audit.json` current reconciliation census to 853.
- [x] Reclassified the old `pq-current-consumer-baseline-correction-2026-09-22.json` 854/146 correction as superseded historical context and added authoritative 853/145 current values.
- [x] Preserved historical 854/146/143 migration evidence; no canonical relationship arrays changed.
- **Exact next task:** classify the remaining dated 854/146/143 correction artifacts so historical values are explicitly labeled, then advance to the queued P1 provenance/data gap.
- Commits: `329e856d4d9d56b192cac3ea9613600f25e097fd`, `055ae26bf334cc0acee3b25cfde6534a543f7b5e`, `495310d45de45b856762ad6c9dbe9910133b49a5`.


### 2026-09-23 cycle update — Correction-artifact classification completed
- [x] Individually classified the remaining dated 854/146/143 correction artifacts.
- [x] Marked six pre-migration correction artifacts `historical_superseded` and documented the live 853/145/142 baseline.
- [x] Preserved original migration values; no canonical relationship rows changed.
- **Exact next task:** resume queued P1 exhaustive data/provenance work, starting with the seven unresolved PQ41–186 Super Soul acquisition-index differences after recomputing the live pair census.
- Commits: `5d594441f3ce8a3329d4755255a4608214d6a185`, `71b9627a7765ade404e0bddd503b0b59179879d0`, `80543c69a9d8b033907b86b07dc0100c23cea134`, `382976427a1977032eda1cf545896d4684a408e7`, `9aae29da5b8f46e73d6c7455de4ee5cecec1e747`, `4a47684aff2a2c64748e6e2b9eb8ea60ceff49c0`.


### 2026-09-23 cycle update — PQ41–186 Super Soul acquisition projection reconciliation
- [x] Recomputed the live canonical PQ41–186 Super Soul pair census: **127 pairs**.
- [x] Reconciled the partial acquisition index: **127 indexed / 127 canonical / 127 exact overlap / 0 missing / 0 extra**.
- [x] Added two source-backed PQ151 pairs and removed the superseded PQ49 Do or Die same-name collision.
- [x] Updated the acquisition-index reconciliation audit; no canonical relationship changes.
- **Exact next task:** advance to the next highest-impact P1 provenance/data structural gap with a fresh live census first.
- Commits: 4b0123e187a5335daa950989123670a9a02e7d00, 3e27d876578b379eb104c080b3a24b9d8b1caaa2.


### 2026-09-23 cycle update — Character-count consumer synchronization
- [x] Recomputed the live canonical character baseline at **151** records.
- [x] Repaired the remaining current-looking **149-character** consumers found by the deterministic census: `docs/data/pq-cross-domain-audit.json` and `docs/data/dlc/daima-hoj2-playable-character-count-reconciliation-2026-09-23.json`.
- [x] Added and registered `docs/data/character-count-consumer-synchronization-2026-09-23.json`.
- [x] Preserved dated historical 149-character snapshots; no character identity or PQ relationship edge was inferred or changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** continue the remaining current-state producer/consumer census for stale skill/domain counts; then return to explicit source-backed preset reconciliation where exact evidence exists.


### 2026-09-23 cycle update — Skill acquisition endpoint consumer synchronization
- [x] Recomputed the live skill endpoint census from the canonical 465-record skill layer.
- [x] Repaired six current-looking consumers that still embedded the superseded 455-skill baseline: `skill-acquisition-cross-domain-endpoint-audit-2026-09-23.json`, `skill-shop-endpoint-layer-audit-2026-09-23.json`, `skill-shop-endpoints.json`, `skill-acquisition-coverage-current-audit-2026-09-23.json`, `skill-acquisition-coverage-correction-audit-2026-09-23.json`, and `time-rift-story-tournament-endpoint-audit-2026-09-23.json`.
- [x] Synchronized current route counts: **465 canonical / 239 PQ-linked / 226 without PQ / 131 unique mentor-linked / 95 non-PQ non-mentor**; endpoint layers include **18 Expert Mission, 31 shop, 13 Time Rift/story/tournament, 4 Tokipedia, 3 Conton City Patrol, 14 special acquisition, 10 character-exclusive, and 2 starting-move** endpoint edges/counts as documented.
- [x] Added and registered `docs/data/skill-acquisition-endpoint-consumer-synchronization-2026-09-23.json`.
- [x] Validation: canonical/index parity **465/465**, 0 duplicate IDs, full endpoint union **465**, uncovered skills **0**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** continue the P1 acquisition/provenance queue from the current 95 non-PQ/non-mentor skills, prioritizing the remaining ambiguous/under-sourced endpoint routes (especially Ultra Instinct and other explicit evidence gaps), while preserving endpoint-layer separation and avoiding inferred PQ edges.


### 2026-09-23 cycle update — Current provenance-audit validation metadata sync
- [x] Synchronized the current 2026-09-23 skill provenance audit validation blocks that still referenced the superseded 455-record baseline to **465 canonical / 465 index / 0 duplicate IDs**.
- [x] Preserved historical narrative references where they describe the audit-time 455-record state; only current validation metadata was corrected.
- [x] Revalidated representative updated audits by direct fetch/JSON parse.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** continue the P1 acquisition/provenance queue from the live **95 non-PQ/non-mentor** skill set, prioritizing explicit endpoint/provenance gaps rather than baseline-only cleanup.

### 2026-09-23 cycle update — Expert Mission skill provenance refresh
- [x] Recomputed the live P1 acquisition/provenance target and selected the ten previously under-sourced Expert Mission skill records with explicit acquisition endpoints.
- [x] Added independent source corroboration for Murder Grenade, Death Wave, Death Meteor, Dead End Bullet, Assault Rain, Hellzone Grenade, Super Electric Strike, Shocking Death Ball, and Blue Hurricane; the corroborating guide explicitly lists each as a Basic Reward for its Expert Mission.
- [x] Added separate GameFAQs corroboration for Spirit Sword; deliberately did not use the guide's EM17 "Spirit Bomb" text to infer a Spirit Sword reward tier.
- [x] Promoted all ten canonical skill records to `verified_current_scope` and `enriched`, while preserving the existing acquisition endpoint and evidence boundary.
- [x] Added and registered `docs/data/skill-expert-mission-provenance-audit-2026-09-23.json`.
- [x] Validation: **465 canonical skills / 0 duplicate IDs / 10 reviewed IDs resolve / provenance audit pass**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** reconcile the remaining partially verified Expert Mission endpoint-layer records using explicit evidence, then continue the non-PQ/non-mentor acquisition gaps (including Ultra Instinct) without inferred relationships.


### 2026-09-23 cycle update — Full Expert Mission endpoint provenance reconciliation
- [x] Reconciled all **18/18** Expert Mission endpoint rows against the independent all-Expert-Missions guide.
- [x] Completed and verified EM16–20 mission titles.
- [x] Added explicit per-endpoint provenance blocks and changed the endpoint-layer status to source-backed.
- [x] Confirmed Basic Reward placement for 17/18 endpoint rows; preserved the EM17 Spirit Bomb vs Spirit Sword conflict without assigning Spirit Sword a Basic Reward tier from the conflicting guide.
- [x] Expanded the Expert Mission provenance audit to record all 18 endpoint rows.
- [x] Preserved canonical endpoint IDs and skill IDs; no new relationships or drop-rate claims were inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** advance to the remaining **95 non-PQ/non-mentor** skill acquisition/provenance gaps, prioritizing explicit special-route evidence such as Ultra Instinct.


### 2026-09-23 cycle update — Ultra Instinct special-route provenance strengthening
- [x] Recomputed the live acquisition census: **465 canonical / 239 PQ-linked / 226 non-PQ**, with **95 unique non-PQ/non-mentor endpoint targets** and **131 unique mentor-linked skill targets**.
- [x] Strengthened skill-ultra-instinct with independent In Pursuit of Mastery evidence and updated special-ultra-instinct to a source-backed explicit route.
- [x] Removed the stale description of Ultra Instinct as an unresolved special-route target from the cross-link contract.
- [x] Corrected EM17 endpoint reward-tier metadata to null so the preserved Spirit Bomb vs Spirit Sword conflict is not represented as a false Basic Reward claim.
- [x] Preserved canonical IDs, relationships, and evidence boundaries; no new acquisition edge was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- Commits: 7e277e8a024534c052115b3bb38ff625ddc61177, 48d744c3ca3261b3bea43bc50aec3986b5bd327a, 333d307893dc5e8344db00141dcb23db68332a42, a777b2f69384b8147eac709c958e01b2d1eceeec, e4befb948c2b400a23fe23f6cbc62b2818067fcb.
- **Exact next task:** continue the 95 endpoint-linked non-PQ/non-mentor provenance queue, prioritizing the thinnest-source records in bounded 4–12 record batches.


### 2026-09-24 cycle update — Blades of Judgment / Blaster Ball provenance refresh
- [x] Live census before editing: **465 canonical / 465 index / 429 stale / 0 duplicate IDs**.
- [x] Bounded P1 batch: **Blades of Judgment; Blaster Ball**.
- [x] Refreshed canonical `last_verified` to **2026-09-24** using existing repository evidence; acquisition/reward/mechanics/DLC semantics preserved.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-blades-through-blaster-ball.json`.
- [x] Refreshed `docs/data/skill-stale-metadata-census-2026-09-24.json`.
- [x] Validation: **465/465 canonical/index IDs, 0 duplicate IDs, 36 current, 429 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** Blaster Meteor; Blaster Shell; Blaster Stream; Blazing Attack; Bloody Counter; Blue Hurricane; Bluff Kamehameha; Body Change; Bomber DX; Brave Heat; Brave Sword Attack; Brave Sword Slash.


### 2026-09-24 cycle correction — stale-queue target reconciliation
- [x] Recomputed the live stale queue after confirming Blades of Judgment and Blaster Ball were already current; preserved the prior history rather than rewriting it.
- [x] Authoritative next batch selected from the live canonical layer: Blaster Meteor; Blaster Shell; Blaster Stream; Blazing Attack; Bloody Counter; Blue Hurricane; Bluff Kamehameha; Body Change; Bomber DX; Brave Heat; Brave Sword Attack; Brave Sword Slash.


### 2026-09-24 cycle update — Blaster Meteor through Brave Sword Slash provenance refresh
- [x] Live census before editing: **465 canonical / 465 index / 429 stale / 0 duplicate IDs**.
- [x] Bounded P1 batch: **Blaster Meteor; Blaster Shell; Blaster Stream; Blazing Attack; Bloody Counter; Blue Hurricane; Bluff Kamehameha; Body Change; Bomber DX; Brave Heat; Brave Sword Attack; Brave Sword Slash**.
- [x] Refreshed canonical `last_verified` to **2026-09-24** using existing repository evidence; acquisition/reward/mechanics/DLC semantics preserved.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-blaster-meteor-through-brave-sword.json` and refreshed the live stale census.
- [x] Validation: **465/465 canonical/index IDs, 0 duplicate IDs, 48 current, 417 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** Break Cannon; Breaker Energy Wave; Brutal Buster; Burning Attack; Burning Blast; Burning Shot; Burning Slash; Burning Swan; Burst Blitz; Burst Charge; Burst Kamehameha; Burst Reflection.


### 2026-09-24 cycle update — Break Cannon through Burst Reflection provenance refresh
- [x] Bounded P1 batch: **Break Cannon; Breaker Energy Wave; Brutal Buster; Burning Attack; Burning Blast; Burning Shot; Burning Slash; Burning Swan; Burst Blitz; Burst Charge; Burst Kamehameha; Burst Reflection**.
- [x] Refreshed canonical last_verified to **2026-09-24** using existing repository evidence; acquisition/reward/mechanics/DLC semantics preserved.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-break-through-burst.json` and refreshed the live stale census.
- [x] Validation: **465/465 canonical/index IDs, 0 duplicate IDs, 60 current, 405 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** Burst Rush; Burst Stinger; Buu Buu Ball; Candy Beam; Candy Beam (Super); Celestial Wave; Chain Destructo-Disc Barrage; Change The Future; Chaos Shot; Chaos Wall; Chaotic Time Impact; Charge.


### 2026-09-24 cycle update — Burst Rush through Charge provenance refresh
- [x] Bounded P1 batch: **Burst Rush; Burst Stinger; Buu Buu Ball; Candy Beam; Candy Beam (Super); Celestial Wave; Chain Destructo-Disc Barrage; Change The Future; Chaos Shot; Chaos Wall; Chaotic Time Impact; Charge**.
- [x] Refreshed canonical last_verified to **2026-09-24** using existing repository evidence; acquisition/reward/mechanics/DLC semantics preserved.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-burst-through-charge.json` and refreshed the live stale census.
- [x] Validation: **465/465 canonical/index IDs, 0 duplicate IDs, 72 current, 393 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** Charged Ki Wave; Circle Flash; Comet Strike; Confusion Blade; Core Breaker; Counter Burst; Counter Impact; Crazy Finger Shot; Crimson Edge; Critical Upper; Crush Cannon; Crush Stream.


### 2026-09-24 cycle update — Charged Ki Wave through Crush Stream provenance refresh
- [x] Bounded P1 batch: **Charged Ki Wave; Circle Flash; Comet Strike; Confusion Blade; Core Breaker; Counter Burst; Counter Impact; Crazy Finger Shot; Crimson Edge; Critical Upper; Crush Cannon; Crush Stream**.
- [x] Refreshed canonical last_verified to **2026-09-24** using existing repository evidence; acquisition/reward/mechanics/DLC semantics preserved.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-charged-ki-wave-through-crush-stream.json` and refreshed the live stale census.
- [x] Validation: **465/465 canonical/index IDs, 0 duplicate IDs, 84 current, 381 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** Crusher Ball; Dancing Parapara; Dark Inscription; Darkness Eye Beam; Darkness Rush (Melee); Darkness Rush (Ranged); Darkness Twin Star; Data Input; Dead End Bullet; Dead End Rain; Deadly Dance; Death Ball.


### 2026-09-24 cycle update — Crusher Ball through Death Ball provenance refresh
- [x] Bounded P1 batch: **Crusher Ball; Dancing Parapara; Dark Inscription; Darkness Eye Beam; Darkness Rush (Melee); Darkness Rush (Ranged); Darkness Twin Star; Data Input; Dead End Bullet; Dead End Rain; Deadly Dance; Death Ball**.
- [x] Refreshed canonical last_verified to **2026-09-24** using existing repository evidence; acquisition/reward/mechanics/DLC semantics preserved.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-crusher-ball-through-death-ball.json` and refreshed the live stale census.
- [x] Validation: **465/465 canonical/index IDs, 0 duplicate IDs, 96 current, 369 stale**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** Death Beam; Death Crasher; Death Meteor; Death Psycho Bomb; Death Slash; Death Slicer; Death Wave; Demon Flash Strike; Demon Flurry; Demon Ray; Demonic Destruction; Destruction's Concerto: Comet.


### 2026-09-24 cycle update — Death through Destruction skill provenance refresh

- [x] Completed the bounded P1 provenance batch for Death Beam, Death Crasher, Death Meteor, Death Psycho Bomb, Death Slash, Death Slicer, Death Wave, Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, and Destruction's Concerto: Comet.
- [x] Synchronized canonical/index skill verification metadata and added the bounded provenance audit.
- [x] Refreshed the live stale census to **465 canonical / 465 index / 108 current / 357 stale / 0 duplicate IDs**.
- [x] Preserved existing acquisition, reward, mechanics, restriction, DLC/update, and evidence-boundary semantics; no unsupported facts were inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** process the next 12 stale records — Demon Wing Flash; Die Die Missile Barrage; Dimension Ray; Divine Kamehameha; Divine Lasso; Dodoria Headbutt; Double Destructo-Disc; Double Sunday; Dragon Blitz; Dragon Burner; Dragon Fist; Dragon Flash.


### 2026-09-24 cycle update — Demon through Dragon skill provenance refresh

- Completed the next bounded P1 provenance batch: **12 skill records** — Demon Wing Flash; DIE DIE Missile Barrage; Dimension Ray; Divine Kamehameha; Divine Lasso; Dodoria Headbutt; Double Destructo-Disc; Double Sunday; Dragon Blitz; Dragon Burner; Dragon Fist; Dragon Flash.
- Refreshed canonical and index metadata to `last_verified=2026-09-24`; existing acquisition endpoints, reward semantics, mechanics, restrictions, and DLC/update provenance were preserved.
- Added `docs/data/skill-provenance-audit-2026-09-24-demon-through-dragon.json` and refreshed the live stale census.
- Validation: **465 canonical / 465 index / 0 duplicate IDs / 120 current / 345 stale**.
- No unsupported probabilities, prerequisites, timers, frame data, damage values, stacking caps, or narrower restrictions were inferred.
- CI/runtime remains unavailable; no CI success claimed.
- Commit: `cfa334ec6a47f2e2c79ffc8a19ea27941eac9a5a`.
- **Exact next stale batch:** Dragon Thunder; Dragon Tornado; Dragon Wind; Dragonic Aura; Dramatic Crush; Dynamite Kick; Earth-Splitting Galick Gun; Electric Shock; Elite Beam; Emergency Combo; Energy Barrier; Energy Shot.


### 2026-09-24 cycle update — Dragon through Energy skill provenance refresh

- [x] Completed the next bounded P1 batch: **Dragon Thunder; Dragon Tornado; Dragon Wind; Dragonic Aura; Dramatic Crush; Dynamite Kick; Earth Splitting Galick Gun; Electric Shock; Elite Beam; Emergency Combo; Energy Barrier; Energy Shot**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-24** and preserved existing acquisition, reward, mechanics, restriction, DLC/update, and evidence-boundary semantics.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-dragon-through-energy.json` and refreshed the stale census.
- [x] Validation: **465 canonical / 465 index / 0 duplicate IDs / 132 current / 333 stale**.
- [x] No unsupported probabilities, prerequisites, timers, frame data, damage values, stacking caps, or narrower restrictions were inferred; existing conflicts remain explicit.
- [ ] CI/runtime unavailable; no CI success claimed.
- Commit: `2a9a4931974138077ece8f3e7746c599864ebee2`.
- **Exact next stale batch:** Energy Wave; Energy Zone; Evil Whirlwind; Explosive Assault; Explosive Bomber; Explosive Buu Buu Punch; Explosive Scream; Explosive Shot; Explosive Surge; Extended Beam; Extra Large Genocide Shell; Eye Laser.


### 2026-09-24 cycle update — Correct stale-census projection and continue live P1 skill queue
- [x] Detected and documented that the prior live stale census listed 9 IDs absent from both canonical and index skill layers; no phantom records were created.
- [x] Recomputed the live skill census directly from `docs/data/skills.json` and `docs/data/skills-index.json`: **465 canonical / 465 index / 134 current / 331 stale / 0 duplicate IDs**.
- [x] Completed the actual 12-record P1 batch: **Destruction's Concerto: Meteor; Destruction's Concerto: Starfall; Destruction's Conductor; Destructive Fission; Destructive Flare; Destructive Fracture; Destructo-Disc; Dimension Cannon; Dimensional Hole; Divine Ray Bomb; Divine Spear; Divine Wrath: Purification**.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-destruction-through-divine-wrath.json`.
- [x] Refreshed the live stale census and preserved historical projection errors as superseded context.
- [x] Canonical/index ID parity remains exact; no duplicate IDs.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** **Divinity Unleashed; Do or Die; Dodon Ray; Dodoria Beam; Dodoria Launcher; Double Crush; Double Death Slicer; Dragon Burn; Dragon Spark; Dragon Spiral; Drain Field; Dual Destructo-Disc**.


### 2026-09-24 cycle update — Divinity through Dual Destructo-Disc provenance refresh
- [x] Refreshed 12 canonical/index skill records: **Divinity Unleashed, Do or Die, Dodon Ray, Dodoria Beam, Dodoria Launcher, Double Crush, Double Death Slicer, Dragon Burn, Dragon Spark, Dragon Spiral, Drain Field, Dual Destructo-Disc**.
- [x] Added and registered the bounded provenance audit.
- [x] Recomputed live census: **465 canonical / 465 index / 146 current / 319 stale / 0 duplicate IDs**.
- [x] Preserved existing conflicts and evidence limits; no unsupported fields inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** **Dust Attack, Eagle Kick, Elegant Blaster, Elite Shooting, Emperor's Blast, Emperor's Cannon, Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Charge, Energy Dome, Energy Field**.


### 2026-09-24 cycle update — Dust through Energy Field provenance refresh
- [x] Refreshed 12 canonical/index skill records: **Dust Attack, Eagle Kick, Elegant Blaster, Elite Shooting, Emperor's Blast, Emperor's Cannon, Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Charge, Energy Dome, Energy Field**.
- [x] Added and registered the bounded provenance audit.
- [x] Recomputed live census: **465 canonical / 465 index / 158 current / 307 stale / 0 duplicate IDs**.
- [x] Preserved existing conflicts and evidence limits; no unsupported fields inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** **Energy Minefield, Energy Release, Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike, Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course**.


### 2026-09-24 cycle update — Energy Minefield through Excellent Full Course provenance refresh
- [x] Refreshed 12 canonical/index skill records: **Energy Minefield, Energy Release, Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike, Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course**.
- [x] Added and registered the bounded provenance audit.
- [x] Recomputed live census: **465 canonical / 465 index / 170 current / 295 stale / 0 duplicate IDs**.
- [x] Preserved existing conflicts and evidence limits; no unsupported fields inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** **Explosive Assault, Explosive Buu-Buu Punch, Explosive Wave, Eye Beam, Fake Blast, Fake Death, Feint Crash, Feint Shot, Fierce Fist, Fighting Pose A, Fighting Pose C, Fighting Pose E**.


### 2026-09-24 cycle update — Explosive Assault through Fighting Pose E provenance refresh
- [x] Refreshed 12 canonical/index skill records: **Explosive Assault, Explosive Buu Buu Punch, Explosive Wave, Eye Beam, Fake Blast, Fake Death, Feint Crash, Feint Shot, Fierce Fist, Fighting Pose A, Fighting Pose C, Fighting Pose E**.
- [x] Added and registered the bounded provenance audit.
- [x] Corrected/recomputed canonical-source census: **465 canonical / 465 index / 182 current / 283 stale / 0 duplicate IDs**.
- [x] Preserved existing conflicts and evidence limits; no unsupported fields inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** **Fighting Pose F, Fighting Pose H, Fighting Pose K, Final Cannon, Final Charge, Final Explosion, Final Flash, Final Flash (SS3 DAIMA), Final Flash (Super), Final Kamehameha, Final Pose, Final Rampage**.


### 2026-09-24 cycle update — Fighting Pose F through Final Rampage provenance refresh

- [x] Completed the next bounded P1 provenance batch: **Fighting Pose F; Fighting Pose H; Fighting Pose K; Final Cannon; Final Charge; Final Explosion; Final Flash; Final Flash (SS3 DAIMA); Final Flash (Super); Final Kamehameha; Final Pose; Final Rampage**.
- [x] Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 target records now carry `last_verified=2026-09-24`.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-fighting-pose-f-through-final-rampage.json` and refreshed `docs/data/skill-stale-metadata-census-2026-09-24.json`.
- [x] Validation target: **465 canonical / 465 index / 0 duplicate IDs / 194 current / 271 stale**.
- [x] Preserved existing acquisition, reward, classification, mechanics, restriction, DLC/update, and evidence-conflict semantics; no unsupported fields were inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next stale batch:** **Finish Breaker; Finishing Blow; Flash Bomber; Flash Chaser; Flash Fist Crush; Flash Strike; Focus Flash; Force Edge; Force Shield; Formation!; Freedom Kick; Fruit of the Tree of Might**.

### 2026-09-24 cycle update — Finish Breaker through Fruit of the Tree of Might provenance refresh
- [x] Live census before editing: **465 canonical / 465 index / 194 current / 271 stale / 0 duplicate IDs**.
- [x] Completed bounded P1 batch: **Finish Breaker; Finishing Blow; Flash Bomber; Flash Chaser; Flash Fist Crush; Flash Strike; Focus Flash; Force Edge; Force Shield; Formation!; Freedom Kick; Fruit of the Tree of Might**.
- [x] Synchronized canonical/index verification metadata to `2026-09-24` for all 12 targets.
- [x] Added and registered the bounded provenance audit and refreshed the stale-metadata census.
- [x] Evidence: reused existing per-record source corpus; acquisition, reward, mechanics, restriction, DLC/update, and conflict semantics were preserved.
- [x] Validation: **465 canonical / 465 index / 0 duplicate IDs / 194 current / 271 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next stale batch:** **Full Power Charge; Full Power Destruction; Future Super Saiyan; Galactic Donuts; Galick Cannon; Galick Gun; Gamma Blaster; Gamma Impact; Genocide Shell; Giant Storm; Gigantic Breaker; Gigantic Burst**.

### 2026-09-24 cycle correction — Finish Breaker through Fruit live census reconciliation
- [x] Post-write reconciliation confirmed the canonical refresh is live: **465 canonical / 465 index / 206 current / 259 stale / 0 duplicate IDs**.
- [x] All 12 target records have matching canonical/index IDs and `last_verified=2026-09-24`.
- [x] The bounded audit validates **12/12 target source-date parity** with **259 stale after**.
- [x] The earlier 194/271 count in the preceding entry is superseded by this live post-write census; historical text remains preserved.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next stale batch:** **Full Power Charge; Full Power Destruction; Future Super Saiyan; Galactic Donuts; Galick Cannon; Galick Gun; Gamma Blaster; Gamma Impact; Genocide Shell; Giant Storm; Gigantic Breaker; Gigantic Burst**.

### 2026-09-24 cycle update — Full Power Charge through Gigantic Burst provenance refresh
- [x] Completed bounded P1 batch: **Full Power Charge; Full Power Destruction; Future Super Saiyan; Galactic Donuts; Galick Cannon; Galick Gun; Gamma Blaster; Gamma Impact; Genocide Shell; Giant Storm; Gigantic Breaker; Gigantic Burst**.
- [x] Synchronized canonical/index verification metadata to `2026-09-24` for all 12 targets.
- [x] Added and registered the bounded provenance audit and refreshed the stale-metadata census.
- [x] Validation: **465 canonical / 465 index / 0 duplicate IDs / 218 current / 247 stale**; target parity clean.
- [x] Existing acquisition, reward, mechanics, restriction, DLC/update, and evidence-conflict semantics preserved; no unsupported fields inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next stale batch:** **Gigantic Charge; Gigantic Cluster; Gigantic Cross; Gigantic Explosion; Gigantic Meteor; Gigantic Nova; Gigantic Omega; Gigantic Rage; Gigantic Roar; God Breaker; God of Destruction's Anger; God of Destruction's Menace**.

### 2026-09-24 cycle update — Gigantic Charge through God of Destruction's Menace provenance refresh
- [x] Live bounded batch: **Gigantic Charge; Gigantic Cluster; Gigantic Cross; Gigantic Explosion; Gigantic Meteor; Gigantic Nova; Gigantic Omega; Gigantic Rage; Gigantic Roar; God Breaker; God of Destruction's Anger; God of Destruction's Menace**.
- [x] Synchronized canonical/index verification metadata to `2026-09-24` for all 12 targets.
- [x] Added and registered the bounded provenance audit and refreshed the live stale census.
- [x] Existing acquisition, reward, mechanics, restriction, DLC/update, and evidence-conflict semantics preserved; no unsupported fields inferred.
- [x] Validation: **465 canonical / 465 index / 0 duplicate IDs / 230 current / 235 stale**; target parity clean.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next stale batch:** **God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God of Destruction's Wrath; God Punisher; God Splitter; Godly Chronos Cannon; Godly Display; Gorgeous Shot; Grand Smasher**.

### 2026-09-24 cycle update — Gigantic Charge through God of Destruction's Menace provenance refresh
- [x] Completed bounded P1 batch: **Gigantic Charge; Gigantic Cluster; Gigantic Cross; Gigantic Explosion; Gigantic Meteor; Gigantic Nova; Gigantic Omega; Gigantic Rage; Gigantic Roar; God Breaker; God of Destruction's Anger; God of Destruction's Menace**.
- [x] Synchronized canonical/index verification metadata to `2026-09-24` for all 12 targets.
- [x] Added and registered the bounded provenance audit and refreshed the stale-metadata census.
- [x] Validation: **465 canonical / 465 index / 0 duplicate IDs / 230 current / 235 stale**; target parity clean.
- [x] Existing acquisition, reward, mechanics, restriction, DLC/update, and evidence-conflict semantics preserved; no unsupported fields inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next stale batch:** **God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God of Destruction's Wrath; God Punisher; God Splitter; Godly Chronos Cannon; Godly Display; Gorgeous Shot; Grand Smasher**.

### 2026-09-24 cycle update — God of Destruction's Might through Grand Smasher provenance refresh
- [x] Completed the bounded P1 provenance batch: **God of Destruction's Might; God of Destruction's Plaything; God of Destruction's Poise; God of Destruction's Rampage; God of Destruction's Roar; God of Destruction's Wrath; God Punisher; God Splitter; Godly Chronos Cannon; Godly Display; Gorgeous Shot; Grand Smasher**.
- [x] Synchronized canonical/index `last_verified` metadata to **2026-09-24** and preserved existing acquisition, reward, mechanics, restriction, DLC/update, and evidence semantics.
- [x] Added and registered the bounded provenance audit and refreshed the live stale census.
- [x] Corrected stale cross-domain index registrations that pointed at nonexistent Gigantic→God audit files; the actual bounded audit is now registered.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Live validation:** **465 canonical / 465 index / 242 current / 223 stale / 0 duplicate IDs**.
- **Exact next batch:** **Gravity Impact; Handy Canon; Hawk Charge; Headshot; Heat Dome Attack; Heat Wave; Heavenly Arrow; Hell Flash; Hellzone Grenade; Hero's Flute; Hero's Pose; Heroic Assault**.


### 2026-09-24 cycle update — Gravity Impact through Heroic Assault provenance refresh
- [x] Completed bounded P1 batch: **Gravity Impact; Handy Canon; Hawk Charge; Headshot; Heat Dome Attack; Heat Wave; Heavenly Arrow; Hell Flash; Hellzone Grenade; Hero's Flute; Hero's Pose; Heroic Assault**.
- [x] Synchronized canonical/index verification metadata to `2026-09-24` and added the bounded provenance audit.
- [x] Preserved existing acquisition, reward, classification, mechanics, restriction, DLC/update, and evidence-conflict semantics without unsupported additions.
- [x] Live validation: **465 canonical / 465 index / 254 current / 211 stale / 0 duplicate IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next batch:** **Hollow Rush; Holy Inscription; Holy Wrath; Hyper Drain; Hyper Movement; Hyper Tornado; Ice Cannon; Ice Claw; Ice Rain; Ice Sheet; Ill Rain; Instant Severance**.


### 2026-09-24 cycle update — Hollow→Instant Severance queue reconciliation
- [x] Refreshed available queued records: **Holy Inscription; Holy Wrath; Hyper Tornado; Ill Rain; Instant Severance**.
- [x] Synchronized canonical/index provenance metadata and added the bounded audit.
- [x] Confirmed **Hollow Rush; Hyper Drain; Hyper Movement; Ice Cannon; Ice Claw; Ice Rain; Ice Sheet** are absent from canonical `skills.json`; did not fabricate records. Added them to the active data-coverage/discovery queue.
- [x] Live validation: **465 canonical / 465 index / 259 current / 206 stale / 0 duplicate IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Next discovery targets:** **Hollow Rush; Hyper Drain; Hyper Movement; Ice Cannon; Ice Claw; Ice Rain; Ice Sheet**.


### 2026-09-24 cycle update — researched Hyper/Ice coverage recovery
- [x] Promoted **Hyper Drain; Hyper Movement; Ice Cannon; Ice Claw** from existing research batches into canonical/index coverage.
- [x] Preserved source-backed classifications, costs, acquisition endpoints, and mechanics bounds; unresolved details remain explicitly unresolved.
- [x] Added recovery audit and refreshed live census: **469 canonical / 469 index / 263 current / 206 stale / 0 duplicate IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Discover/research **Hollow Rush; Ice Rain; Ice Sheet**; no sufficiently direct repository research record was found in the current live search.
- **Exact next stale batch:** **Heroic Counter; Ill Bomber; Impact Flare; Impulse Slash; Indomitable; Innocence Breath; Innocence Bullet; Innocence Cannon; Instant Charge; Instant Rise; Instant Transmission; Jumping Energy Wave**.

### 2026-09-24 cycle update — Heroic Counter through Jumping Energy Wave provenance refresh
- [x] Refreshed the 12 canonical/index skill records: **Heroic Counter; Ill Bomber; Impact Flare; Impulse Slash; Indomitable; Innocence Breath; Innocence Bullet; Innocence Cannon; Instant Charge; Instant Rise; Instant Transmission; Jumping Energy Wave**.
- [x] Added/registered the bounded provenance audit and refreshed live census.
- [x] Live validation: **469 canonical / 469 index / 275 current / 194 stale / 0 duplicate IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Continue discovery for **Hollow Rush; Ice Rain; Ice Sheet** without fabricating records.
- **Exact next stale batch:** **Justice Blade; Justice Combination; Justice Drive; Justice Kick; Justice Pose; Justice Rush; Kai Kai; Kaioken; Kaioken Assault; Kaioken Kamehameha; Ki Blast Cannon; Ki Blast Thrust**.
### 2026-09-24 validation correction — canonical/index parity and exact next queue
- [x] Rechecked the live canonical/index projections after the Heroic Counter batch; **469/469 records, 469/469 unique IDs, and 0 verification-date mismatches**.
- [x] Synchronized **60** stale index verification dates to their canonical counterparts.
- **Exact next stale batch from canonical order:** **Justice Blade; Justice Combination; Justice Drive; Justice Kick; Justice Pose; Justice Rush; Kai Kai; Kaioken; Kaioken Kamehameha; Kairos Cannon; Kamehameha; Ki Blast Thrust**.

### 2026-09-24 cycle update — Phantom Fist through Prepare to be Punished

- Completed the bounded P1 provenance batch: 12 records — Phantom Fist, Photon Swipe, Potential Unleashed, Power Blitz, Power Impact, Power Pole Combo, Power Pole Pro, Power Rush, Power Wall, Powered Shell, Prelude to Destruction, and Prepare to be Punished.
- Synchronized docs/data/skills.json and docs/data/skills-index.json; all 12 now have last_verified=2026-09-24.
- Validation: 469 canonical / 469 index / 0 duplicate IDs / 0 canonical-index mismatches.
- Refreshed docs/data/skill-stale-metadata-census-2026-09-24.json: 323 current / 146 stale.
- Existing evidence boundaries and conflicts were preserved; no unsupported mechanics or acquisition details were invented.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next stale batch: Pride Trooper; Punisher Drive; Purification; Raid Blast; Raiding Hammer; Rebellion Spear; Revenge Death Ball; Revenge Final Flash; Ribrianne Loves You; Rocket Tackle; Rolling Hercule Punch; Rolling Bullet.

### 2026-09-24 cycle update — Present For You through Purification

- Completed the bounded P1 provenance batch: 12 records — Present For You, Pressure Sign, Pretty Cannon, Pretty Charge, Prominence Flash, Psychic Move, Psycho Barrier, Psycho Escape, Punisher Guard, Punisher Shield, Pure Progress, and Purification.
- Synchronized docs/data/skills.json and docs/data/skills-index.json; all 12 now have last_verified=2026-09-24.
- Added docs/data/skill-provenance-audit-2026-09-24-present-through-purification.json.
- Validation: 469 canonical / 469 index / 0 duplicate IDs / 0 canonical-index mismatches.
- Refreshed docs/data/skill-stale-metadata-census-2026-09-24.json: 335 current / 134 stale.
- Corrected the stale queue to the live canonical alphabetical sequence after Purification; the prior attempted queue contained names absent from the live canonical dataset.
- Existing evidence boundaries and conflicts were preserved; no unsupported mechanics or acquisition details were invented.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next stale batch: Raid Blast; Rakshasa's Claw; Ray Blast; Rebellion Spear; Recoome Kick; Remote Serious Bomb; Requiem of Destruction; Revenge Death Ball; Revenge Final Flash; Reverse Launcher; Reverse Mabakusenko; Reverse Shot.


### 2026-09-24 cycle update — Raid Blast through Reverse Shot provenance refresh

- Completed the bounded P1 provenance batch: **Raid Blast; Rakshasa's Claw; Ray Blast; Rebellion Spear; Recoome Kick; Remote Serious Bomb; Requiem of Destruction; Revenge Death Ball; Revenge Final Flash; Reverse Launcher; Reverse Mabakusenko; Reverse Shot**.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 targets now have `last_verified=2026-09-24`.
- Added `docs/data/skill-provenance-audit-2026-09-24-raid-blast-through-reverse-shot.json` with the bounded evidence/validation record.
- Live validation: **469 canonical / 469 index / 347 current / 122 stale / 0 duplicate-ID condition**; canonical/index IDs and verification dates remain aligned.
- Existing acquisition endpoints, reward semantics, restrictions, mechanics, DLC/update provenance, and evidence conflicts were preserved. No unsupported probabilities, Ultimate Finish gates, timers, damage values, stacking caps, or narrower CaC restrictions were introduced.
- CI/runtime remains unavailable; no CI success claimed.
- Commits: canonical `8388dd8cd9a8833d8cda24461c772354b9c9219d`; index `0914d90007e0a4ded33aa3f3a9f46d703a788ff8`; audit `00f42306d0f63f7f577eb490eabe23276c5be4a6`; census `22f13bebc85a4f5a8cb48e2486a85fa9ffdafbf3`.
- **Exact next stale batch:** **Quick Sleep; Ribrianne's Eternal Love; Riot Javelin; Rise to Action; Rising Rage; Rocket Tackle; Rolling Bullet; Rolling Hercule Punch; Rough Ranger; S.S. Deadly Bomber; Saiyan Blaster; Saiyan Spirit**.


### 2026-09-24 cycle update — Quick Sleep through Saiyan Spirit provenance refresh

- Completed the bounded P1 provenance batch: **Quick Sleep; Ribrianne's Eternal Love; Riot Javelin; Rise to Action; Rising Rage; Rocket Tackle; Rolling Bullet; Rolling Hercule Punch; Rough Ranger; S.S. Deadly Bomber; Saiyan Blaster; Saiyan Spirit**.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 targets now have `last_verified=2026-09-24`.
- Added `docs/data/skill-provenance-audit-2026-09-24-quick-sleep-through-saiyan-spirit.json` with the bounded evidence/validation record.
- Live validation: **469 canonical / 469 index / 359 current / 110 stale / 0 duplicate IDs**; canonical/index IDs remain aligned.
- Existing acquisition endpoints, reward semantics, restrictions, mechanics, DLC/update provenance, and evidence conflicts were preserved. No unsupported probabilities, Ultimate Finish gates, timers, damage values, stacking caps, or narrower CaC restrictions were introduced.
- CI/runtime remains unavailable; no CI success claimed.
- Commits: canonical `ad745bb666f54492a67100a37d38687562e462d8`; index `5e8008253c6951ff96a42f2e7b85d5b206b88870`; audit `67b1da4421c43c49f89585ca8ef64f2f1d316c0c`; census `c5d181131790af2d5d660fe23db2443aa13cc8fe`.
- **Exact next stale batch:** **Saturday Crash; Sauzer Blade; Savory Slicer; Scatter Kamehameha; Scissors Paper Rock; Seagull Combination; Secret Poison; Shadow Crusher; Shield Barrier; Shine Shot; Shining Friday; Shining Slash**.


### 2026-09-24 cycle update — Saturday Crash through Shining Slash provenance refresh

- Live census before editing: **469 canonical / 469 index / 359 current / 110 stale**.
- Completed bounded P1 provenance batch: **Saturday Crash; Sauzer Blade; Savory Slicer; Scatter Kamehameha; Scissors Paper Rock; Seagull Combination; Secret Poison; Shadow Crusher; Shield Barrier; Shine Shot; Shining Friday; Shining Slash**.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 targets now have `last_verified=2026-09-24`.
- Added `docs/data/skill-provenance-audit-2026-09-24-saturday-crash-through-shining-slash.json` with bounded evidence/validation results.
- Existing evidence conflicts were preserved, including Shield Barrier's PQ153 reward-tier conflict; no unsupported mechanics or acquisition conditions were promoted.
- Validation: **469 canonical / 469 index / 371 current / 98 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- CI/runtime remains unavailable; no CI success claimed.
- **Exact next stale batch:** **Shocking Death Ball; Shooting Strike; Side Bridge; Sign of Awakening; Sneaky Strike; Soaring Fist; Soaring Rush; Solar Flare; Sonic Bomb; Sonic Rush; Special Beam Cannon; Special Beam Cannon (Beast)**.


### 2026-09-24 cycle update — Shocking Death Ball through Special Beam Cannon (Beast) provenance refresh

- Live census before editing: **469 canonical / 469 index / 371 current / 98 stale**.
- Completed bounded P1 provenance batch: **Shocking Death Ball; Shooting Strike; Side Bridge; Sign of Awakening; Sneaky Strike; Soaring Fist; Soaring Rush; Solar Flare; Sonic Bomb; Sonic Rush; Special Beam Cannon; Special Beam Cannon (Beast)**.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 targets now have `last_verified=2026-09-24`.
- Added `docs/data/skill-provenance-audit-2026-09-24-shocking-death-ball-through-special-beam-cannon-beast.json`.
- Existing acquisition, reward, mechanics, restriction, DLC/update provenance, and evidence conflicts were preserved; no unsupported mechanics or acquisition conditions were promoted.
- Validation: **469 canonical / 469 index / 383 current / 86 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- CI/runtime remains unavailable; no CI success claimed.
- **Exact next stale batch:** **Sphere of Destruction; Spirit Ball; Spirit Blaster; Spirit Bomb; Spirit Boost; Spirit Explosion; Spirit Pulse; Spirit Slash; Spirit Sword; Spread Shot Retreat; Steel Mirage; Stone Bullet**.


### 2026-09-24 cycle update — Sphere of Destruction through Stone Bullet provenance refresh

- Live census before editing: **469 canonical / 469 index / 383 current / 86 stale**.
- Completed bounded P1 provenance batch: **Sphere of Destruction; Spirit Ball; Spirit Blaster; Spirit Bomb; Spirit Boost; Spirit Explosion; Spirit Pulse; Spirit Slash; Spirit Sword; Spread Shot Retreat; Steel Mirage; Stone Bullet**.
- Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json`; all 12 targets now have `last_verified=2026-09-24`.
- Added `docs/data/skill-provenance-audit-2026-09-24-sphere-of-destruction-through-stone-bullet.json` with bounded evidence/validation results.
- Existing acquisition, reward, mechanics, restriction, DLC/update provenance, and evidence conflicts were preserved; no unsupported mechanics or acquisition conditions were promoted.
- Validation: **469 canonical / 469 index / 395 current / 74 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- CI/runtime remains unavailable; no CI success claimed.
- **Exact next stale batch:** **Strike of Revelation; Sudden Death Beam; Sudden Storm; Super Afterimage; Super Black Kamehameha Rosé; Super Destructo-Disc; Super Donut Volley; Super Dragon Flight; Super Electric Strike; Super Elite Combo; Super Explosive Wave; Super Gamma Blast**.


### 2026-09-24 cycle status — Strike of Revelation through Super Gamma Blast research reconciliation
- [x] Completed repository-first evidence reconciliation for the exact 12-record stale batch: Strike of Revelation; Sudden Death Beam; Sudden Storm; Super Afterimage; Super Black Kamehameha Rosé; Super Destructo-Disc; Super Donut Volley; Super Dragon Flight; Super Electric Strike; Super Elite Combo; Super Explosive Wave; Super Gamma Blast.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-strike-through-super-gamma-blast.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [ ] Canonical/index `last_verified` synchronization remains pending because the available GitHub connector cannot safely retrieve the oversized canonical `docs/data/skills.json` blob in this cycle; no partial overwrite was attempted.
- [ ] Exact continuation action: safely synchronize these 12 canonical/index records, recompute `docs/data/skill-stale-metadata-census-2026-09-24.json`, validate canonical/index parity, then proceed to the next stale batch without inventing missing evidence.


### 2026-09-24 cycle completion — Strike of Revelation through Super Gamma Blast
- [x] Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json` for all 12 queued records to `last_verified=2026-09-24`.
- [x] Completed and registered `docs/data/skill-provenance-audit-2026-09-24-strike-through-super-gamma-blast.json`.
- [x] Recomputed `docs/data/skill-stale-metadata-census-2026-09-24.json`: **469 canonical / 469 index / 407 current / 62 stale / 0 duplicate IDs**.
- [x] Canonical/index ID order and membership validated as aligned.
- [ ] Exact next stale batch: **Super Ghost Buu Attack; Super Ghost Kamikaze Attack (Super); Super Ghost Kamikaze Attack (Ultimate); Super God Fist; Super God Shock Flash; Super Guard; Super Kamehameha; Super Kamehameha (SS4 DAIMA); Super Saiyan; Super Saiyan 2; Super Saiyan Blue Kaioken; Super Saiyan God**.


### 2026-09-24 cycle completion — Super Ghost Buu Attack through Super Saiyan God
- [x] Completed bounded P1 provenance refresh for: **Super Ghost Buu Attack; Super Ghost Kamikaze Attack (Super); Super Ghost Kamikaze Attack (Ultimate); Super God Fist; Super God Shock Flash; Super Guard; Super Kamehameha; Super Kamehameha (SS4 DAIMA); Super Saiyan; Super Saiyan 2; Super Saiyan Blue Kaioken; Super Saiyan God**.
- [x] Synchronized canonical and index `last_verified=2026-09-24` for all 12 records.
- [x] Added `docs/data/skill-provenance-audit-2026-09-24-super-ghost-through-super-saiyan-god.json`.
- [x] Recomputed census: **469 canonical / 469 index / 419 current / 50 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **Super Saiyan God Super Saiyan; Super Saiyan God Super Saiyan (Evolved); Super Spirit Bomb; Super Vegeta; Supernova; Supernova Cooler; Supersonic Mode; Supreme Fury; Surging Spirit; Symphonic Destruction; Tail Slicer; Taunt**.


### 2026-09-24 cycle completion — Super Saiyan God Super Saiyan through Taunt
- [x] Completed bounded P1 provenance refresh for 12 records: **Super Saiyan God Super Saiyan; Super Saiyan God Super Saiyan (Evolved); Super Spirit Bomb; Super Vegeta; Supernova; Supernova Cooler; Supersonic Mode; Supreme Fury; Surging Spirit; Symphonic Destruction; Tail Slicer; Taunt**.
- [x] Synchronized canonical/index `last_verified=2026-09-24` for all 12.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-super-saiyan-god-super-saiyan-through-taunt.json`.
- [x] Recomputed census: **469 canonical / 469 index / 431 current / 38 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **Teleporting Vanishing Ball; Temporal Holy Ray; The Power to Overcome; The Savior Has Come; Thunder Flash; Time Bullet; Time Control; Time Skip/Back Breaker; Time Skip/Flash Skewer; Time Skip/Jump Spike; Time Skip/Tremor Pulse; Timespace Impact**.


### 2026-09-24 cycle completion — Teleporting Vanishing Ball through Timespace Impact
- [x] Completed bounded P1 provenance refresh for 12 records: **Teleporting Vanishing Ball; Temporal Holy Ray; The Power to Overcome; The Savior Has Come; Thunder Flash; Time Bullet; Time Control; Time Skip/Back Breaker; Time Skip/Flash Skewer; Time Skip/Jump Spike; Time Skip/Tremor Pulse; Timespace Impact**.
- [x] Synchronized canonical/index `last_verified=2026-09-24` for all 12.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-teleporting-vanishing-ball-through-timespace-impact.json`.
- [x] Recomputed census: **469 canonical / 469 index / 443 current / 26 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **Total Detonation Ball; Trap Shooter; Tri-Beam; Turn Golden; Tyrant Lancer; Ultimate Charge; Ultra Instinct; Ultrasonic Blitz; Unrelenting Barrage; Vanishing Ball; Variable Snipe Shot; Variant Drive**.


### 2026-09-24 cycle completion — Total Detonation Ball through Variant Drive
- [x] Completed bounded P1 provenance refresh for 12 records: **Total Detonation Ball; Trap Shooter; Tri-Beam; Turn Golden; Tyrant Lancer; Ultimate Charge; Ultra Instinct; Ultrasonic Blitz; Unrelenting Barrage; Vanishing Ball; Variable Snipe Shot; Variant Drive**.
- [x] Synchronized canonical/index `last_verified=2026-09-24` for all 12.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-total-detonation-ball-through-variant-drive.json`.
- [x] Recomputed census: **469 canonical / 469 index / 455 current / 14 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **Venus Fist; Victory Cannon; Victory Rush; Volleyball Fist; Wall of Defense; Warp Kamehameha; Weekend; Wild Buster; Wild Hunt; Wild Stinger; Wolf Fang Fist; X 100 Big Bang Kamehameha**.


### 2026-09-24 cycle completion — Venus Fist through X 100 Big Bang Kamehameha
- [x] Completed bounded P1 provenance refresh for 12 records: **Venus Fist; Victory Cannon; Victory Rush; Volleyball Fist; Wall of Defense; Warp Kamehameha; Weekend; Wild Buster; Wild Hunt; Wild Stinger; Wolf Fang Fist; X 100 Big Bang Kamehameha**.
- [x] Synchronized canonical/index `last_verified=2026-09-24` for all 12.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-venus-fist-through-x-100-big-bang-kamehameha.json`.
- [x] Recomputed census: **469 canonical / 469 index / 467 current / 2 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **x10 Kamehameha; Zigzag Express**.


### 2026-09-24 cycle completion — Total Detonation Ball through Variant Drive
- [x] Completed bounded P1 provenance refresh for 12 records: **Total Detonation Ball; Trap Shooter; Tri-Beam; Turn Golden; Tyrant Lancer; Ultimate Charge; Ultra Instinct; Ultrasonic Blitz; Unrelenting Barrage; Vanishing Ball; Variable Snipe Shot; Variant Drive**.
- [x] Synchronized canonical/index `last_verified=2026-09-24` for all 12.
- [x] Existing provenance audit confirmed present and registered: `docs/data/skill-provenance-audit-2026-09-24-total-detonation-ball-through-variant-drive.json`.
- [x] Recomputed census: **469 canonical / 469 index / 467 current / 2 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **x10 Kamehameha; Zigzag Express**.


### 2026-09-24 cycle completion — Total Detonation Ball through Variant Drive
- [x] Completed bounded P1 provenance refresh for 12 records: **Total Detonation Ball; Trap Shooter; Tri-Beam; Turn Golden; Tyrant Lancer; Ultimate Charge; Ultra Instinct; Ultrasonic Blitz; Unrelenting Barrage; Vanishing Ball; Variable Snipe Shot; Variant Drive**.
- [x] Synchronized canonical/index `last_verified=2026-09-24` for all 12.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-total-detonation-ball-through-variant-drive.json`.
- [x] Recomputed census: **469 canonical / 469 index / 467 current / 2 stale / 0 duplicate IDs / canonical-index IDs aligned**.
- [ ] Exact next stale batch: **x10 Kamehameha; Zigzag Express**.


### 2026-09-24 cycle completion — x10 Kamehameha through Zigzag Express
- [x] Completed the final bounded P1 stale-skill provenance refresh for **x10 Kamehameha** and **Zigzag Express**.
- [x] Synchronized canonical `docs/data/skills.json` and `docs/data/skills-index.json` so both targets have `last_verified=2026-09-24`.
- [x] Added and registered `docs/data/skill-provenance-audit-2026-09-24-x10-kamehameha-through-zigzag-express.json`.
- [x] Recomputed `docs/data/skill-stale-metadata-census-2026-09-24.json`: **469 canonical / 469 index / 469 current / 0 stale / 0 duplicate IDs**.
- [x] Preserved existing mentor/PQ acquisition endpoints, Male Majin restriction, mechanics bounds, source sets, and evidence limitations; no unsupported probabilities, prerequisites, timers, frame data, stacking caps, or damage values were introduced.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: continue the deterministic post-stale-queue cross-domain coverage/projection audit, prioritizing machine-checkable current-field mismatches or navigation/index drift over speculative gameplay-data expansion.


### 2026-09-24 cycle update — recovered Hyper/Ice endpoint coverage reconciliation
- [x] Live canonical census confirmed **469 skills / 239 PQ-linked / 230 without PQ**. The prior endpoint projection covered only 465, exposing exactly four uncovered canonical IDs.
- [x] Identified the four recovered canonical records from the existing 2026-09-24 Hyper/Ice coverage recovery: **Hyper Drain; Hyper Movement; Ice Cannon; Ice Claw**.
- [x] Added deterministic navigation edges: Hyper Drain → Skill Shop; Hyper Movement → TP/STP Medal Shop; Ice Cannon → Shenron new Ultimate Attack; Ice Claw → Shenron new Super Attack.
- [x] Updated `docs/data/skill-shop-endpoints.json`, `docs/data/special-acquisition-endpoints.json`, `docs/data/skill-acquisition-coverage-report.json`, `docs/data/full-skill-endpoint-reverse-parity-audit-2026-09-23.json`, and `docs/data/skill-acquisition-endpoint-consumer-synchronization-2026-09-23.json`.
- [x] Added and registered `docs/data/skill-endpoint-coverage-reconciliation-2026-09-24-hyper-and-ice.json`.
- [x] Deterministic validation: **469 canonical / 239 PQ-linked / 230 non-PQ endpoint targets / 469 endpoint union / 0 uncovered / canonical-index aligned**.
- [x] No PQ relationship was invented; endpoint identities derive from canonical acquisition/recovery records.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: continue the live cross-domain producer/consumer audit from the now-complete 469-skill endpoint union, checking remaining reverse-navigation projections and validator assumptions for stale counts or orphan targets.


### 2026-09-24 cycle update — live PQ producer/consumer projection audit
- [x] Re-read the live continuation instructions and audited the deterministic PQ producer/consumer layers after the 469-skill endpoint-union repair.
- [x] Confirmed the canonical PQ relationship master remains **853 edges**: 244 skills, 145 Super Souls, 124 equipment, 247 character, 86 DLC, 7 farming.
- [x] Confirmed PQ reward presentation remains exact-pair clean: skill 244/244, Super Soul 145/145, equipment 124/124, DLC 86/86; unresolved and duplicate structured pairs remain zero.
- [x] Confirmed the live skill acquisition endpoint projection remains **469 canonical / 239 PQ-linked / 230 non-PQ endpoint targets / 469 union / 0 uncovered** across mentor, expert mission, story/tournament, shop, Tokipedia, Conton City Patrol, special acquisition, character-exclusive, and starting-move layers.
- [x] Refreshed `docs/data/pq-cross-domain-status.json`, `docs/data/pq-relationship-producer-census.json`, and `docs/data/pq-explorer-reward-navigation-audit.json` with the current 2026-09-24 reconciliation state.
- [x] No canonical PQ relationship changes were necessary; the remaining partial research/source-normalized artifacts are explicitly preserved as non-canonical layers.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: inspect remaining cross-domain reverse projections beyond the PQ reward layer (especially character/DLC identity bridges and partial research indexes) for deterministic orphan, stale-count, or target-resolution drift; do not convert partial research absence into negative canonical claims.


### 2026-09-24 cycle update — current consumer baseline and cross-link contract audit
- [x] Audited remaining active PQ consumer assertions after the 853-edge correction; current canonical PQ counts remain **244 skill / 145 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**, 853 total.
- [x] Confirmed historical 854/146/143 and older 862/151/125/88 snapshots are retained as historical context rather than current truth.
- [x] Updated `docs/data/pq-cross-domain-audit.json` to record the completed current-consumer baseline gate.
- [x] Updated `docs/data/CROSS-LINK-CONTRACT.md` to replace the stale 465/465 skill endpoint statement with the live **469/469** endpoint-union baseline and document the Hyper/Ice reconciliation.
- [x] Current skill endpoint union remains **469 canonical / 469 represented / 0 uncovered**; canonical/index alignment remains intact.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: audit the remaining non-PQ reverse projections and identity bridges (character, DLC, mentor/shop/event, and partial research indexes) for orphan targets and stale current-field counts, beginning with the next machine-checkable projection that can be reconciled without inventing relationships.
- Commits: PQ cross-domain audit `93957a432075f5f08ec1496326c236b4f0cc2f82`; cross-link contract `0691d85d9f827fcab665dba75a5107e835020a22`.


### 2026-09-24 cycle update — character/DLC identity bridge live-census reconciliation
- [x] Re-read the live continuation instructions, efficiency addendum, and exhaustive TODO before continuing.
- [x] Audited the machine-checkable published Character/DLC navigation contract and its canonical identity inputs: `docs/data/characters-record-layer.json`, `docs/data/characters/dlc-character-identity-bridge.json`, `docs/data/dlc/canonical-dlc-identity.json`, and `scripts/validate_published_character_dlc_navigation.py`.
- [x] Resolved a documentation-census drift: the live canonical character record layer contains **151 unique characters**, while an older 2026-09-22 historical note still referenced 149. The historical note was preserved; no canonical identity was invented or removed.
- [x] Refreshed `docs/data/characters/published-character-dlc-navigation-audit.json` to 2026-09-24 with current counts: **151 canonical characters / 15 DLC-character bridge records / 20 canonical DLC identities / 86 canonical PQ→DLC edges / 20 unique DLC targets**; 14 bridge targets resolve and 1 source label remains intentionally unresolved.
- [x] Deterministic identity checks remain clean: 0 missing character targets, 0 unresolved records carrying canonical targets, 0 duplicate bridge sources/targets, 0 orphan DLC identities, 0 duplicate DLC IDs/names, and 0 malformed PQ→DLC targets.
- [x] Preserved the partial-research boundary: the unresolved Supreme Kai of Time (Ultra Supervillain) source label remains unresolved rather than being mapped to a nearby canonical identity.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: inspect the next non-PQ reverse projection/partial research index for deterministic current-count or target-resolution drift, prioritizing DLC presentation consumers and mentor/shop/event reverse indexes before speculative content expansion.
- Commit: published Character/DLC navigation audit `548baafb8f08ae44ac18eff0b9b2b31a84af8d56`.


### 2026-09-24 cycle completion — live non-PQ shop/coverage consumer reconciliation
- [x] Audited the live docs/data/skill-shop-endpoints.json producer against current canonical skill coverage and identified the superseded 2026-09-23 **465 / 13 / 18** shop audit projection.
- [x] Added and registered docs/data/skill-shop-endpoint-layer-audit-2026-09-24.json with the current **469 canonical / 14 Skill Shop / 19 TP-STP / 33 total shop-linked** census.
- [x] Synchronized the nested current projection in docs/data/skill-acquisition-coverage-report.json to **469 canonical / 239 PQ-linked / 230 non-PQ / 131 unique mentor skill targets / 99 non-PQ non-mentor targets** while preserving historical 465-era figures.
- [x] Removed stale current claims that mentors and Expert Missions were missing canonical endpoint layers; the canonical endpoint layers are now present and separately audited.
- [x] Validation: **469 canonical / 239 PQ-linked / 230 non-PQ / 131 mentor targets / 99 non-PQ non-mentor targets / 33 shop-linked skills / forward↔reverse shop parity clean / 0 unresolved shop skill IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** inspect the next machine-checkable non-PQ reverse projection/consumer for stale counts or orphan targets, prioritizing another deterministic consumer over speculative content expansion.


### 2026-09-24 cycle completion — special acquisition reverse-index parity repair
- [x] Found and repaired the deterministic special-acquisition reverse-index drift introduced by the Hyper/Ice coverage recovery.
- [x] Added reverse entries for **Ice Cannon** and **Ice Claw** to match their existing forward endpoint edges.
- [x] Recomputed live special acquisition coverage to **16 endpoints / 16 forward edges / 16 unique skill targets / 0 unresolved IDs**.
- [x] Added and registered docs/data/special-acquisition-endpoint-audit-2026-09-24.json.
- [x] Validation: **16 forward pairs / 16 reverse pairs / exact parity clean / audit pass**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue the machine-checkable non-PQ reverse-projection audit, prioritizing current-facing stale counts or orphan targets.


### 2026-09-24 cycle completion — mentor skill coverage projection reconciliation
- [x] Audited mentor skill coverage against the canonical mentor record layer and mentor crosslink projection.
- [x] Removed the stale Hit → `skill-time-skip-tremor-pulse` linked ID; retained **Time Skip/Tremor Pulse** as the single explicit unresolved skill lesson.
- [x] Reconciled current coverage to **33 mentors / 133 lesson reward objects / 132 typed skill rewards / 1 typed non-skill reward / 131 mentor→skill edges / 130 unique targets / 1 unresolved skill lesson / 0 broken endpoints**.
- [x] Updated the stale canonical skill census from 420 to the live 469 count.
- [x] Added and registered `docs/data/mentor-skill-coverage-audit-2026-09-24.json`.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue the machine-checkable non-PQ reverse-projection audit against another current-facing consumer or partial research index.


### 2026-09-24 cycle completion — Expert Mission acquisition cross-link completion
- [x] Audited the Expert Mission acquisition index against the canonical Expert Mission endpoint layer.
- [x] Added canonical `skill_id` and `endpoint_id` to all **18/18** maintained EM03–EM20 acquisition records using exact-name matching.
- [x] Added and registered `docs/data/expert-mission-acquisition-index-audit-2026-09-24.json`.
- [x] Validation: **18/18 cross-linked / 0 missing IDs / 0 duplicates / 0 unresolved names / exact parity clean**.
- [x] Preserved partial acquisition evidence boundaries; no drop-rate or guarantee claims were upgraded.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue the remaining non-PQ reverse-projection audit, prioritizing another acquisition/event/identity consumer that can be deterministically reconciled.


### 2026-09-24 cycle completion — live DLC/PQ projection count reconciliation
- [x] Found and repaired stale top-level `current_counts` in `docs/data/pq-reward-relationships.json`: DLC, farming, and character counts were incorrectly zero despite populated live relationship arrays.
- [x] Recomputed and synchronized current counts to **244 skills / 145 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming / 853 total**.
- [x] Refreshed and registered `docs/data/dlc/dlc-presentation-consumer-audit-2026-09-24.json`.
- [x] Validation: **20 canonical DLC targets / 86 forward / 86 reverse / 0 mismatches / 0 orphan targets**; current relationship census matches the live array.
- [x] No gameplay/acquisition evidence was upgraded or inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue the remaining non-PQ reverse-projection audit against another deterministic stale-field or orphan-target consumer.


### 2026-09-24 cycle completion — Time Rift/story/tournament endpoint projection audit
- [x] Audited `docs/data/time-rift-story-tournament-endpoints.json` and confirmed **11 endpoints / 13 forward edges / 13 unique skills**.
- [x] Corrected stale contract wording claiming 14 forward edges; live Match 5 contributes two legitimate edges and the maintained layer totals 13.
- [x] Added and registered `docs/data/time-rift-story-tournament-endpoint-audit-2026-09-24.json`.
- [x] Validation: **0 duplicate pairs / 0 missing pairs / 0 extra pairs / all endpoint IDs resolve / audit clean**.
- [x] No new relationship or gameplay evidence was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue deterministic non-PQ consumer scanning, prioritizing event/raid and character/preset navigation layers.


### 2026-09-24 cycle completion — Conton City Patrol endpoint projection audit
- [x] Audited `docs/data/conton-city-patrol-endpoints.json` against its existing canonical skill identities and exact forward/reverse projection.
- [x] Confirmed **3 endpoints / 3 forward edges / 3 reverse edges / 3 unique skill targets / 0 unresolved skill IDs** for Conton City Patrol 04, 10, and 17.
- [x] Added and registered `docs/data/conton-city-patrol-endpoint-audit-2026-09-24.json`.
- [x] Forward↔reverse parity is exact; no additional patrol reward relationship was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue the deterministic non-PQ reverse-projection audit, prioritizing the next current-facing event/raid or character/preset consumer with machine-checkable orphan/count drift; do not turn partial research absence into negative canonical claims.


### 2026-09-24 cycle completion — character/preset presentation consumer census refresh
- [x] Reconciled the live `docs/data/character-presets-record-layer.json` producer against the character presentation consumer audit and preset↔skill navigation audit.
- [x] Corrected stale presentation counts from **40** to **51 preset records** and from **12** to **17 distinct presentation character IDs**; the live layer contains **46 numbered preset records + 5 separate-character records**.
- [x] Synchronized verified-loadout counts to **25 records / 162 skill-slot entries**.
- [x] Preserved all identity boundaries, including the unresolved Captain Ginyu body-swap presentation labels and the five separate-character records.
- [x] No acquisition, DLC, or character identity relationship was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic non-PQ reverse-projection scanning, prioritizing event/raid acquisition consumers and any remaining stale current-field/count projections.


### 2026-09-24 cycle completion — skill acquisition coverage current-projection hardening
- [x] Preserved the stale nested 465/226-era projection as historical state and explicitly marked it superseded.
- [x] Added live **469 canonical / 239 PQ-linked / 230 unlinked** projection with current endpoint-layer counts.
- [x] Added and registered `docs/data/skill-acquisition-coverage-current-projection-audit-2026-09-24.json`.
- [x] Validation: **469 - 239 = 230**; overlapping endpoint layers are not a disjoint partition.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** scan Tokipedia/starting-move and remaining unregistered non-PQ endpoint audits for stale projections or orphan targets.


### 2026-09-24 cycle completion — Tokipedia and starting-move endpoint reconciliation
- [x] Audited `docs/data/tokipedia-endpoints.json`: **4 endpoints / 4 forward edges / 4 reverse edges / 4 unique skill targets / 0 broken IDs**.
- [x] Found and corrected the remaining deterministic canonical/index mismatch for **Energy Minefield**: index `source_quest_or_shop` was still **60%**, while canonical and endpoint evidence establish **75% Tokipedia completion**.
- [x] Added `docs/data/tokipedia-endpoint-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Audited `docs/data/starting-move-endpoints.json`: **2 endpoints / 2 forward edges / 2 reverse targets / 0 broken IDs / exact parity**.
- [x] Added `docs/data/starting-move-endpoint-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundaries preserved; no additional acquisition route inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** scan remaining non-PQ endpoint layers for unregistered audits or stale cross-domain projections, then reconcile any deterministic count/ID drift found.


### 2026-09-24 cycle completion — character-exclusive endpoint current-baseline audit
- [x] Audited `docs/data/character-exclusive-skill-endpoints.json` against the live **469-record** canonical skill layer.
- [x] Confirmed **10 endpoints / 10 forward edges / 10 unique skill targets / 0 unresolved IDs / 0 duplicate endpoint pairs**.
- [x] Added `docs/data/character-exclusive-skill-endpoint-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] No endpoint changes were inferred; cast/boss exposure remains distinct from CaC acquisition.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** audit the remaining non-PQ endpoint/index consumers for current 469-baseline drift, prioritizing any unregistered Expert Mission/current acquisition projection or event/raid gap that can be machine-checked without inventing relationships.


### 2026-09-24 cycle completion — raid/gift accessory partial-research bridge audit
- [x] Audited `docs/data/accessory-raid-gift-canonical-bridge.json` against `docs/data/accessory-canonical-reconciliation.json`.
- [x] Confirmed **16 bridge records / 10 resolved route records / 6 unresolved candidate records / 6 unique resolved canonical IDs / 0 duplicate source IDs / 0 missing canonical IDs**.
- [x] Confirmed the six unresolved candidate names are exactly mirrored by the bridge's `unmatched_candidates` list; no candidate was silently promoted or discarded.
- [x] Confirmed expected multi-route identity reuse for **accr-001, accr-002, and accr-003** without creating duplicate inventory identities.
- [x] Added and registered `docs/data/accessory-raid-gift-bridge-audit-2026-09-24.json`.
- [x] Preserved the boundary that raid/event history establishes route evidence, not current availability, reward probability, or a new canonical accessory identity.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** audit `docs/data/accessory-raid-identity-reconciliation-2026-09.json` against the live canonical accessory layer; machine-check whether any of its nine unresolved/route-reconciled raid identities now have an exact canonical match, while explicitly preserving unresolved names and never merging near-name variants without evidence.


### 2026-09-24 cycle completion — raid accessory exact-identity reconciliation
- [x] Audited `docs/data/accessory-raid-identity-reconciliation-2026-09.json` against the live canonical accessory layer and maintained equipment-accessory record layer.
- [x] Promoted **6 exact identities** into the canonical accessory layer: **Tapion Wig → accr-106; Tights Hat → accr-107; Universe 6 Supreme Kai's Helper's Hat → accr-108; Lord Zuno's Topknot Wig → accr-109; Android 21 Wig & Glasses → accr-110; Tiencha Wig → accr-111**.
- [x] Updated the raid/gift bridge to use those canonical IDs; bridge now has **14 resolved / 2 unresolved** records.
- [x] Preserved **Cheelai Wig, Cheelai Wig (w/Scouter), and Hercule Wig 2** as unresolved; no near-name merge was made with Hercule Wig, and the Cheelai variants remain distinct.
- [x] Added and registered `docs/data/accessory-raid-identity-reconciliation-audit-2026-09-24.json`.
- [x] Validation: **9 raid identity records / 6 exact canonical matches / 3 unresolved / 111 canonical accessory records / 16 raid-gift bridge records / 14 bridge-resolved / 2 bridge-unresolved / 0 broken canonical IDs / exact unmatched-list parity / no near-name merges**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** reconcile the remaining 3 unresolved raid accessory identities (Cheelai Wig, Cheelai Wig (w/Scouter), Hercule Wig 2) against existing repository research/equipment sources; only promote an exact identity when source evidence establishes it, otherwise preserve the explicit unresolved boundary. Then continue the event/raid non-PQ consumer scan.


### 2026-09-24 cycle completion — unresolved raid accessory boundary + backlog synchronization
- [x] Rechecked the remaining three raid identity candidates (**Cheelai Wig**, **Cheelai Wig (w/Scouter)**, **Hercule Wig 2**) against the repository's canonical accessory and equipment layers and route research.
- [x] No exact canonical records were found for those three; **Hercule Wig 2** was explicitly kept separate from canonical **Hercule Wig**.
- [x] Synchronized `docs/data/accessory-unmatched-route-backlog.json`: removed the six identities already reconciled in the previous batch and retained unresolved route candidates rather than treating absence as proof of nonexistence. Backlog now contains **5** unresolved route identities.
- [x] Existing event/raid evidence was reviewed; the repository currently has route research but no dedicated generic raid skill endpoint layer that can be deterministically projected without inventing relationships. No speculative event/raid endpoint layer was created.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** audit the remaining five accessory unmatched-route candidates (**Cheelai Wig, Cheelai Wig (w/Scouter), Hercule Wig 2, Golden Turtle Hermit's Shell, Turtle Hermit's Beard, plus the SSGSS Goku Wig route if still represented by a separate backlog source**) against the canonical/equipment layers and route-specific records, then continue the event/raid non-PQ consumer scan using only deterministic existing endpoint structures.


### 2026-09-24 cycle completion — Turtle Hermit's Beard exact accessory reconciliation
- [x] Audited the remaining unmatched accessory candidates against the maintained equipment/accessories layer.
- [x] Promoted **Turtle Hermit's Beard** as canonical accessory `accr-112`, backed by the exact existing equipment identity `acc-032`; no name variant was merged.
- [x] Removed Turtle Hermit's Beard from `docs/data/accessory-unmatched-route-backlog.json`; **4 unresolved route candidates remain**.
- [x] Kept **Golden Turtle Hermit's Shell**, **Cheelai Wig**, **Hercule Wig 2**, and **SSGSS Goku's Wig** unresolved because current repository evidence does not establish an exact canonical identity without a near-name or route-only assumption.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** reconcile the remaining four unmatched accessory candidates, beginning with Golden Turtle Hermit's Shell and SSGSS Goku's Wig, then continue deterministic event/raid non-PQ consumer scanning.


### 2026-09-24 cycle completion — Golden Shell + SSGSS Goku raid reconciliation
- [x] Reconciled **SSGSS Goku's Wig** as an alias of existing canonical `accr-096` (**SSGSS Goku Wig**) using independent inventory/model evidence; no duplicate canonical identity created.
- [x] Promoted **Turtle Hermit's Golden Shell** as distinct canonical accessory `accr-113`; independent model evidence distinguishes it from **Turtle Hermit's Shell**, while Online Raid evidence establishes the raid route.
- [x] Kept the reported Crystal Raid attribution for the Golden Shell explicitly unconfirmed rather than treating route-list wording as proof.
- [x] Updated raid identity reconciliation, raid-gift bridge, unmatched backlog, and reconciliation audit.
- [x] Remaining backlog candidates: **Cheelai Wig** and **Hercule Wig 2**. The separate **Cheelai Wig (w/Scouter)** identity record also remains unresolved and must not be merged with Cheelai Wig.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** reconcile Cheelai Wig / Cheelai Wig (w/Scouter) and Hercule Wig 2 against inventory/model evidence, then perform the deterministic event/raid non-PQ consumer scan.


### 2026-09-24 cycle completion — exact Cheelai variants + Hercule Wig 2 accessory reconciliation
- [x] Promoted **Cheelai Wig → accr-114**, **Cheelai Wig (w/Scouter) → accr-115**, and **Hercule Wig 2 → accr-116** using independent inventory/model evidence and route documentation.
- [x] Kept Cheelai's two named variants distinct and kept Hercule Wig 2 distinct from canonical Hercule Wig; no near-name merge was performed.
- [x] Synchronized canonical accessory reconciliation, raid/gift bridge, unmatched-route backlog, raid identity reconciliation, and the 2026-09-24 accessory identity audit.
- [x] Validation: **116 canonical accessories / 9 raid identity records / 9 resolved / 0 unresolved / 18 bridge records / 18 bridge-resolved / 0 bridge-unresolved / 0 broken canonical IDs**.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic post-accessory event/raid non-PQ consumer scanning, prioritizing current-facing stale counts, orphan targets, and reverse-index drift over speculative endpoint creation.


### 2026-09-24 cycle completion — accessory canonical projection count boundary
- [x] Distinguished the legacy 74 acc identities / 32 PQ-edge accessory projection from the current 116 accr canonical reconciliation layer.
- [x] Added and registered docs/data/accessory-canonicalization-current-projection-audit-2026-09-24.json.
- [x] Updated the canonicalization audit with explicit cross-namespace count/projection boundaries.
- [x] Validation: legacy forward/reverse PQ parity clean; current canonical count 116; raid identity count 9 with 0 unresolved; no unsupported PQ edges inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: continue deterministic non-PQ consumer scanning for stale current fields/counts or orphan targets in event/raid or character/preset navigation layers.


### 2026-09-24 cycle completion — Time Rift/story/tournament endpoint contract drift correction
- [x] Corrected `docs/data/CROSS-LINK-CONTRACT.md` from 14 to the live validated **13 forward skill edges** for the 11-endpoint Time Rift/story/tournament layer.
- [x] Confirmed no canonical endpoint relationship required modification; only stale documentation was corrected.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** scan remaining cross-link documentation and machine-readable indexes for deterministic stale endpoint counts/IDs.


### 2026-09-24 cycle completion — current non-PQ skill endpoint consumer census
- [x] Added and registered a current 2026-09-24 non-PQ skill endpoint consumer audit: **469 canonical / 239 PQ-linked / 230 non-PQ / 469 covered / 0 uncovered**.
- [x] Kept the 2026-09-23 audit as historical evidence.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** scan character/preset, event/raid, and equipment navigation indexes for deterministic stale current counts or orphan IDs.


### 2026-09-24 cycle completion — PQ navigation current-layer reconciliation
- [x] Added current PQ navigation consumer audit with **469 skills / 151 characters / 173 equipment-accessory records** and **853 authoritative PQ relationships**.
- [x] Registered the audit and preserved older scalar snapshots as historical evidence.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** scan event/raid and equipment navigation consumers for stale current counts or orphan canonical targets.

### 2026-09-24 cycle completion — current PQ consumer baseline synchronization
- [x] Audited current-facing PQ consumer projections against the authoritative `docs/data/pq-reward-relationships.json` baseline after the Super Soul 158 domain migration.
- [x] Corrected two stale **854-edge** current-facing assertions: `docs/data/pq-non-pq-consumer-census-2026-09-22.json` and `docs/data/pq-direct-template-dlc-consumer-audit-2026-09-22.json` now expose the live **853-edge** baseline.
- [x] Preserved the superseded 854 value as historical context; no historical entry was deleted.
- [x] Added and registered `docs/data/pq-current-consumer-baseline-synchronization-2026-09-24.json` in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **853 total / 244 skill / 145 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**, with **0 stale 854 assertions** in the repaired current-facing consumers.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue deterministic reverse/navigation parity scanning against the **853-edge** baseline, prioritizing remaining current-facing event/raid and equipment/navigation consumers for stale counts, orphan targets, or projection drift.

### 2026-09-24 cycle completion — raid accessory bridge audit current-layer reconciliation
- [x] Audited `docs/data/accessory-raid-gift-canonical-bridge.json` against the current canonical accessory layer.
- [x] Corrected stale audit counts from **16/105/6 unresolved** to the live **18 bridge records / 116 canonical accessories / 0 unmatched candidates**.
- [x] Current bridge integrity: **17 resolved + 1 route-family-only / 14 unique canonical IDs / 0 duplicate source IDs / 0 missing canonical IDs / 0 unresolved candidates**.
- [x] Preserved the superseded counts as explicit stale historical snapshot metadata.
- [x] Confirmed existing cross-domain registration; no new relationship edge or canonical identity was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** continue deterministic non-PQ equipment/accessory navigation scanning for stale record counts, one-way links, and canonical-ID drift.

### 2026-09-24 cycle completion — record reverse-navigation current-baseline refresh
- [x] Refreshed `docs/data/record-reverse-pq-navigation-audit.json` to the current **853-edge / 145 Super Soul / 124 equipment** baseline.
- [x] Equipment exact-pair parity: **124/124**, no missing/extra/duplicate pairs.
- [x] Super Soul exact-pair parity: **145/145**, no missing/extra/duplicate pairs.
- [x] Preserved noncanonical equipment acquisition metadata and documented route conflicts; historical snapshots remain intact.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next priority:** deterministic non-PQ equipment/accessory presentation-consumer scanning for stale counts, one-way navigation, and canonical-ID drift.


### 2026-09-24 cycle completion — non-PQ equipment/accessory presentation consumer audit
- [x] Audited `docs/Equipment-All.html` for canonical data loading, PQ reverse-link derivation, local-search navigation, DLC-provenance navigation, and target resolution.
- [x] Verified **124 canonical equipment edges / 122 unique targets / 0 unresolved / 0 duplicate pairs**.
- [x] Added and registered `docs/data/equipment-accessory-presentation-consumer-audit-2026-09-24.json`.
- [ ] CI/runtime unavailable; browser behavior remains an environment gate.
- **Exact next priority:** scan remaining non-PQ equipment/accessory presentation consumers for one-way links and canonical-ID drift.


### 2026-09-24 cycle completion — special acquisition current skill-baseline reconciliation
- [x] Corrected `docs/data/special-acquisition-endpoint-audit-2026-09-23.json` from stale **465** canonical skills to live **469**.
- [x] Verified special endpoint integrity: **14/14/14**, zero unresolved or duplicate endpoint pairs.
- [x] Registered the refreshed audit in `docs/data/pq-cross-domain-index.json`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic event/raid and acquisition-index consumer scanning for stale 469 counts, orphan IDs, and one-way navigation.


### 2026-09-24 completed current skill-domain consumer drift reconciliation
- [x] Recomputed the live skill/domain baseline at **469 canonical / 469 index / 469 current / 0 stale / 0 duplicate IDs**, with **239 PQ-linked / 230 non-PQ endpoint / 469 full endpoint union**.
- [x] Repaired stale current-facing 465-record assertions in `docs/data/pq-endpoint-navigation-validation.json` and `docs/data/skill-pq-acquisition-presentation-audit.json`.
- [x] Refreshed current PQ endpoint consumer counts to **469 skills / 153 characters / 174 equipment-accessory records** without changing the **853-edge** relationship graph.
- [x] Added and registered `docs/data/current-skill-domain-consumer-scan-2026-09-24.json`.
- [x] Preserved dated 2026-09-23 audits and bounded provenance artifacts as historical evidence; no historical content was deleted.
- [x] No canonical acquisition relationship, probability, Ultimate Finish requirement, or gameplay field was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** continue deterministic current-facing **event/raid/Festival/Chapter 4 and character/preset** consumer scanning for stale counts, one-way navigation, orphan targets, and canonical identity drift; then resume the highest-impact thin-domain source-backed expansion.


### 2026-09-24 cycle correction — post-write parity validation
- [x] Corrected the remaining stale `reverse_navigation.skill_count` value from **465** to **469** in `docs/data/skill-pq-acquisition-presentation-audit.json`.
- [x] Corrected and revalidated the cross-domain index JSON separator after registering the new current skill-domain consumer audit.
- [x] Final checked state: PQ endpoint validation **469/234/174/153/20 with 853 edges**, PQ skill presentation **469/244 with exact reverse parity**, consumer scan **pass**, index JSON **valid**.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** continue deterministic event/raid/Festival/Chapter 4 and character/preset consumer scanning.


### 2026-09-24 completed broader current skill consumer census
- [x] Synchronized five current-facing skill projections from the superseded 465 baseline to the live **469** canonical/index baseline.
- [x] Current non-PQ arithmetic is now **469 - 239 = 230**, with **131** unique mentor-linked targets and **99** non-PQ/non-mentor endpoint targets.
- [x] Confirmed the four recovered Hyper/Ice skills do not introduce character-source or mentor-source identities, so those bridge edge counts remain unchanged.
- [x] Re-fetched edited JSON consumers after writes and confirmed current counts/parity.
- [x] Preserved dated historical audits containing 465/455 counts as historical evidence.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** deterministic census of **event/raid/Festival/Chapter 4 and character/preset presentation consumers**, repairing only current-facing stale counts, one-way navigation, orphan targets, and identity drift supported by repository evidence.


### 2026-09-24 completed — Future Saga Chapter 4 character consumer reconciliation
- [x] Reconciled both Chapter 4 official character records to exact canonical names in the live **153-character** layer.
- [x] Added and registered docs/data/future-saga-chapter-4-character-navigation-audit-2026-09-24.json.
- [x] Confirmed **2/2 exact matches / 0 unresolved identities / 0 unsupported variant collapses / 0 loadout promotions**.
- [x] Preserved Chapter 4 provenance separately from canonical character identity and did not infer preset/loadout/skill/customization data.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** scan remaining Chapter 4/Festival/event and character/preset projections for stale baselines and one-way navigation before further preset research.


### 2026-09-24 completed — character presentation consumer count drift
- [x] Reconciled the current `character-presentation-consumer-audit.json` nested character counts from **151** to the live **153** canonical identity baseline.
- [x] Preserved preset/PQ/loadout counts and all identity boundaries; no unsupported relationships were added.
- [x] Confirmed `Characters.md` already exposes 153 and Chapter 4 identities are exact canonical matches.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** inspect remaining current-facing **event/raid/Festival** projections for stale counts, one-way links, and canonical-ID drift; preserve dated historical snapshots.


### 2026-09-24 completed — Festival skill/source identity navigation
- [x] Audited the explicit Festival of Universes skill/source records in skill research batch 264.
- [x] Added and registered `docs/data/festival-skill-character-navigation-audit-2026-09-24.json`.
- [x] Confirmed **3/3** explicit Festival skill source characters resolve to canonical identities; no unsupported PQ/raid/preset edges were created.
- [ ] CI/runtime unavailable; no CI success claimed.
- **Exact next task:** audit remaining raid/event projections, prioritizing explicit raid/gift accessory and Super Soul consumers for stale current baselines and one-way canonical navigation.


### 2026-09-24 cycle completion — raid/event Super Soul presentation consumer coverage
- [x] Audited `docs/Super-Souls-Database.md` against the canonical `docs/data/super-souls-record-layer.json` raid/event acquisition population.
- [x] Confirmed **230 canonical Super Soul records / 37 raid-or-event-associated records / 0 duplicate canonical IDs**.
- [x] Found the narrative raid sections surfaced only **12/37** canonical raid/event records; **25** existing canonical records were not presented by that consumer.
- [x] Added a complete current raid/event presentation index covering all 37 existing canonical records, preserving each record's existing acquisition type/source and verification status.
- [x] Added and registered `docs/data/super-soul-raid-event-presentation-consumer-audit-2026-09-24.json`.
- [x] Explicitly preserved the boundary that presentation coverage does not establish current availability, recurrence schedules, drop probabilities, guarantees, or new PQ relationships.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic current-facing event/raid and remaining cross-domain consumer scanning for stale counts, orphan targets, one-way navigation, and canonical-ID drift; then resume the highest-impact source-backed thin-domain expansion.


### 2026-09-24 cycle completion — Accessory PQ presentation consumer count reconciliation
- [x] Audited docs/Accessory-PQ-Database.md against the current accessory PQ bridge and canonical reconciliation layer.
- [x] Corrected stale presentation wording/counts: current canonical accessory reconciliation is 116 accr-### identities, while the PQ bridge is 45 research records / 35 resolved / 10 unresolved / 34 unique resolved targets.
- [x] Preserved the two resolved broader-domain accessory endpoints (equip-135, equip-050) rather than creating duplicate acc-### identities.
- [x] Added and registered docs/data/accessory-pq-presentation-consumer-audit-2026-09-24.json.
- [x] No reward relationship, guarantee, drop rate, inventory identity, or acquisition route was inferred or changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: continue deterministic current-facing event/raid/Festival/character/preset consumer scanning, especially remaining equipment/accessory pages and cross-route indexes, for stale counts, orphan targets, one-way navigation, and canonical-ID drift.


### 2026-09-24 cycle completion — Accessory Shop presentation consumer count reconciliation
- [x] Audited docs/Accessory-Shop-Database.md against accessory-shop-research.json and accessory-shop-canonical-bridge.json.
- [x] Corrected stale page wording from 49 to the live **51 populated shop records**.
- [x] Preserved shop-051 and shop-052 as unresolved historical slots rather than reconstructing them by assumption.
- [x] Added and registered docs/data/accessory-shop-presentation-consumer-audit-2026-09-24.json.
- [x] Validation: structured shop layer and bridge both contain 51 populated records; 4 existing canonical identities remain intentionally unmatched to exact shop IDs.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: continue deterministic event/raid/Festival and non-PQ acquisition consumer scanning for stale current counts, orphan targets, one-way navigation, and canonical-ID drift.


### 2026-09-24 cycle completion — raid accessory identity count drift correction
- [x] Reconciled the current raid accessory identity audit: its resolved array contains **11** identities, not 9; corrected `docs/data/accessory-raid-identity-reconciliation-audit-2026-09-24.json` from 9/9 to **11/11**.
- [x] Corrected the dependent current projection and canonical database wording from **9** raid identities to **11**.
- [x] Confirmed all 11 resolved canonical IDs exist and the 18-record raid/gift bridge remains fully resolved.
- [x] No new identity or route was inferred; only deterministic count/projection drift was repaired.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next priority: continue deterministic event/raid/Festival and non-PQ acquisition consumer scanning for stale counts, orphan targets, one-way navigation, and canonical-ID drift.


### 2026-09-24 cycle completion — accessory/equipment current consumer count synchronization
- [x] Live census exposed two stale current-facing counts: `equipment-accessory-presentation-consumer-audit-2026-09-24.json` reported 173 record-layer records while the live layer contains 174; `accessory-presentation-consumer-current-audit-2026-09-24.json` reported 9 raid identities while the reconciled audit contains 11.
- [x] Corrected the two current projections to **174 equipment/accessory records** and **11/11 raid identities resolved**.
- [x] Registered both count-sync audits in `docs/data/pq-cross-domain-index.json`.
- [x] Revalidated all edited JSON documents successfully.
- [x] Preserved dated historical `docs/data/accessory-cross-route-audit.json` values as historical evidence; no historical snapshot was rewritten.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: continue deterministic event/raid/Festival/non-PQ current consumers, focusing on orphan canonical targets and one-way navigation after count drift is exhausted.

### 2026-09-24 completed Festival skill presentation consumer
- [x] Added a dedicated Festival of Universes section to `docs/Skills-Database.md` for Galaxy Breaker (Festival), God Bind (Festival), and Justice Crush (Festival), using the maintained research batch as the evidence boundary.
- [x] Extended `docs/data/festival-skill-character-navigation-audit-2026-09-24.json` with explicit presentation-consumer parity for the three rows.
- [x] Confirmed no PQ/raid/preset relationship was inferred or added.
- [x] Validation and commit state recorded in the append-only handoff.
- [ ] **Next:** continue deterministic non-PQ event/raid/Festival consumer scanning, then resume exhaustive preset/loadout expansion.
### 2026-09-24 completion — high-connectivity character preset presentation consumer audit
- [x] Audited the named high-connectivity preset targets in `docs/Character-Preset-Research.md` against `docs/data/characters-record-layer.json`.
- [x] Added `docs/data/character-preset-research-presentation-consumer-audit-2026-09-24.json` covering 10 target groups with **0 groups lacking an exact canonical identity match**.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json` so preset research is discoverable from the central cross-domain registry.
- [x] Preserved the critical evidence boundary: this audit establishes presentation/identity resolution only; it does **not** infer preset numbering, loadouts, acquisition routes, Festival progression, Partner Customization keys, or variant equivalence.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic character/preset and event/raid/Festival consumer scanning, then begin machine-readable preset/loadout expansion for the highest-connectivity character targets, starting with Goku, without filling unsupported fields by inference.


### 2026-09-24 completed bounded current presentation consumer scan
- [x] Added `docs/data/current-presentation-consumer-scan-2026-09-24.json` covering current character/preset and Chapter 4 presentation surfaces.
- [x] Registered the scan in `docs/data/pq-cross-domain-index.json`.
- [x] Verified the live baseline: **152 canonical characters / 51 preset records / 25 verified preset loadouts / 162 verified loadout skill-slot entries / 2 Chapter 4 PQs**.
- [x] Confirmed the existing character presentation audit remains clean for unresolved preset IDs and orphan reverse character targets.
- [x] Documented the Goku loadout boundary: source-observed named rows cannot safely be mapped to repository numeric preset IDs by row order, so no unsupported Goku loadouts were promoted.
- [ ] **Next:** continue exact source-to-numeric preset mapping only where a source directly binds the mapping; otherwise proceed to the next highest-impact thin-domain research tranche without inference.

### 2026-09-24 completed raid/event Super Soul presentation coverage repair
- [x] Reconciled the current `docs/Super-Souls-Database.md` raid/event presentation table against the canonical raid/event-associated Super Soul producer.
- [x] Added the **25 previously missing canonical raid/event records (052, 054, 057, 058, 063, 074, 082, 083, 092, 094, 095, 096, 097, 103, 104, 111, 112, 115, 116, 117, 127, 128, 129, 135, 136)** to the presentation index.
- [x] Closed `docs/data/super-soul-raid-event-presentation-consumer-audit-2026-09-24.json`: **37/37 surfaced, 0 missing, 0 duplicate canonical IDs, all raid IDs resolve**.
- [x] Preserved acquisition/effect verification states from the canonical producer; no current raid availability, recurrence, probability, or guarantee was inferred.
- [ ] **Next:** continue deterministic event/raid/Festival/Chapter 4 consumer scanning for remaining one-way navigation and stale scalar issues, then resume the highest-impact source-backed preset/loadout tranche.


### 2026-09-24 cycle completion — Future Saga Chapter 4 character audit count synchronization
- [x] Re-fetched the live canonical character producer and found `docs/data/future-saga-chapter-4-character-navigation-audit-2026-09-24.json` still asserted **153** canonical characters.
- [x] Corrected that current-facing audit to the live producer count of **152** from `docs/data/characters-record-layer.json`.
- [x] Preserved the two Chapter 4 character identities and all exact identity-resolution results; no preset, loadout, unlock, skill, or Partner Customization relationship was inferred.
- [x] Added an explicit note that the older 153 value is superseded current-state metadata, preserving historical context rather than rewriting history elsewhere.
- [x] Revalidated the edited JSON by parsing the complete updated document.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic event/raid/Festival/Chapter 4 and remaining character/preset current-consumer scanning for stale scalar counts, orphan targets, one-way navigation, and canonical-ID drift; once that consumer layer is clean, resume the highest-impact source-backed preset/loadout tranche.


### 2026-09-24 cycle completion — preset/loadout audit projection synchronization
- [x] Audited `docs/data/character-preset-skill-navigation-audit-2026-09-23.json` against the canonical `docs/data/character-presets-record-layer.json`.
- [x] Found a deterministic internal projection mismatch: the audit's top-level count correctly reported **25 verified loadouts / 162 verified loadout skill-slot entries**, but its embedded `verified_preset_loadouts` array still contained only **23** rows from an earlier snapshot.
- [x] Regenerated the embedded projection directly from the **25** canonical records marked `loadout_status=verified`.
- [x] Preserved Super Soul labels separately from the 162 skill-slot count; no acquisition, exclusivity, preset-number, or identity inference was introduced.
- [x] Validation: embedded projection now contains 25 rows and exactly 162 skill entries; all IDs match the canonical verified-record set.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic character/preset/event consumer scanning for stale projections and one-way navigation; then resume source-backed preset/loadout expansion for unresolved characters where explicit numeric mapping exists.


### 2026-09-24 cycle completion — Vegeta Preset 10/11 numeric identity evidence refresh
- [x] Rechecked the unresolved Battle Suit 10/11 boundary against the repository's cited community video source.
- [x] Upgraded the evidence from a generic repository search result to explicit video chapter timestamps: **Vegeta Preset 10 at 39:09** and **Vegeta Preset 11 at 42:06**.
- [x] Kept both loadouts unresolved because the chapter metadata does not expose their six skill slots; no skill configuration was inferred.
- [x] Updated `docs/data/preset-battle-suit-reconciliation-2026-09-23.json` with the direct numeric-identity evidence and preserved the unresolved-loadout boundary.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue source-backed preset/loadout expansion where the source directly exposes both numeric identity and skill configuration; otherwise continue deterministic non-PQ event/raid/Festival consumer scanning.


### 2026-09-24 cycle completion — Super Soul guide census synchronization
- [x] Deterministically compared the current-facing docs/Super-Souls.md catalogue census with docs/data/super-souls-record-layer.json.
- [x] Found stale prose claiming the canonical layer contained **42** records while the live canonical producer contains **230** records.
- [x] Updated only that current census statement to **230**, preserving the surrounding historical research-batch narrative and evidence boundaries.
- [x] Validation: canonical producer re-read at 230 records; edited guide re-fetched after commit and target wording was replaced without unrelated normalization.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic non-PQ event/raid/Festival/Chapter 4 consumer scanning for stale scalar counts and one-way navigation; then resume source-backed preset/loadout expansion.

### 2026-09-24 cycle completion — Super Soul database census synchronization
- [x] Found a second current-facing stale Super Soul census in `docs/Super-Souls-Database.md`: **42** populated records versus **230** live canonical records.
- [x] Corrected only the current census statement to **230**; historical research-batch tables and dated history remain unchanged.
- [x] Validation: live canonical layer remains 230 records; edited database fetched after commit and the current census is synchronized.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic non-PQ Event/Raid/Festival/Chapter 4 consumer scanning, including current-facing prose outside dated historical sections, then resume source-backed preset/loadout expansion.


### 2026-09-24 cycle completion — raid/event Super Soul presentation deduplication
- [x] Re-scanned the current `docs/Super-Souls-Database.md` raid/event presentation index against its canonical IDs.
- [x] Found a deterministic presentation-only duplication: **62 table rows / 37 unique canonical IDs**, with **25 canonical IDs duplicated**.
- [x] Removed the duplicate presentation rows, leaving **37 rows / 37 unique IDs / 0 duplicate presentation IDs**. Canonical Super Soul records and provenance were unchanged.
- [x] Updated `docs/data/super-soul-raid-event-presentation-consumer-audit-2026-09-24.json` with before/after row counts and duplicate-row census; canonical audit remains **37/37 surfaced, 0 missing, all raid IDs resolve**.
- [x] Validation: live database section re-fetched after write; 37 rows, 37 unique IDs, 0 duplicates. The historical 12/37 result remains explicitly described as historical rather than current state.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic current-facing **event/raid/Festival/Chapter 4 consumer scanning** for duplicate presentation rows, stale scalar/coverage claims, one-way navigation, orphan targets, and canonical-ID drift; then resume source-backed preset/loadout expansion.


### 2026-09-24 cycle completion — Event/Raid/Festival/Chapter 4 consumer scan
- [x] Added `docs/data/current-event-raid-festival-chapter4-consumer-scan-2026-09-24.json` covering the current presentation surfaces for raid/event Super Souls, Festival skill→character navigation, and Future Saga Chapter 4.
- [x] Raid/event presentation: **37/37 surfaced, 0 missing, 0 duplicate presentation IDs**; the older 12/37 statement is explicitly historical.
- [x] Festival navigation: **3/3 explicit skill rows resolve to exact canonical characters; 0 unresolved identities; 0 unsupported preset/PQ/raid promotions**.
- [x] Chapter 4 presentation: publisher-backed headline counts remain synchronized at **1 Extra Mission / 2 PQs / 4 moves / 1 Awoken Skill / 6 costumes-accessories / 4 Super Souls / 8 loading-screen illustrations**; unresolved item/mission/battle detail remains explicit.
- [x] Character cross-check: live `docs/Characters.md` and the character presentation audit both report **152** canonical identities; no edit was required.
- [x] Registered the new scan in `docs/data/pq-cross-domain-index.json` for central cross-database discoverability.
- [x] Validation: new JSON parses; central index re-read after registration; no current consumer mismatch found in this bounded scope.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** inspect the next uncovered current consumer surface for stale scalar/list assumptions and one-way navigation; if clean, begin the highest-impact source-backed preset/loadout tranche only where numeric preset identity and configuration are directly bound by evidence.


### 2026-09-24 cycle completion — Goku preset numeric identity evidence refresh
- [x] Live census before editing: `character-presets-record-layer.json` = **51 records / 17 presentation character IDs / 25 verified loadouts / 162 verified skill-slot entries / 26 unresolved loadout records**.
- [x] Bounded batch: existing unresolved Goku preset records `goku-preset-2` through `goku-preset-18` (excluding the absent preset 13 record).
- [x] Added explicit timestamped numeric-identity observations from the maintained community video: Goku Presets 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17 and 18.
- [x] Updated `docs/data/character-preset-skill-navigation-audit-2026-09-23.json` so the Goku candidate now records numeric identity as confirmed while keeping loadout promotion blocked.
- [x] Evidence boundary preserved: the video labels the preset numbers but does **not** expose complete six-slot configurations; no skills were inferred from row order, costume order, or proximity.
- [x] Validation: reconciliation JSON and navigation audit both parse/re-fetch successfully; the canonical preset producer remains unchanged at 51 records / 25 verified loadouts / 162 skill entries.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** locate a source exposing both explicit Goku numeric preset labels and complete skill slots. If unavailable, move to the next unresolved preset family rather than guessing Goku loadouts.


### 2026-09-24 cycle completion — Goku preset loadout source-boundary audit
- [x] Live producer census: **51 canonical preset records / 25 verified loadouts / 162 verified skill-slot entries**; 16 existing Goku numeric preset records remain loadout-unresolved.
- [x] Reviewed the current Goku in-game-data source: it exposes **19 named main-slot loadout rows with complete skill configurations**, but those rows use costume/named labels rather than the repository numeric preset IDs.
- [x] Cross-checked the maintained community video: it explicitly labels the existing repository Goku numeric presets **2–12 and 14–18**, but its chapter index does not expose their skill-slot configurations.
- [x] Created and registered `docs/data/goku-preset-loadout-source-boundary-2026-09-24.json` documenting the complementary evidence and the exact unresolved numeric-to-named mapping boundary.
- [x] No row-order, costume-order, or proximity mapping was promoted; canonical Goku loadouts remain unresolved until a source directly binds numeric preset IDs to complete configurations.
- [x] During the current-consumer scan, direct live fetches confirm the canonical character producer and `docs/Characters.md` remain at **152** identities; a repository search result showing 153 was stale search indexing and was not treated as live evidence. No character-count edit was made.
- [x] Validation: new audit parses, central cross-domain index re-fetched with the registration, and canonical preset producer remains unchanged.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** search for an explicit numeric Goku preset table/game-data identifier containing complete skill slots; if unavailable, move to the next unresolved preset family.


### 2026-09-24 cycle completion — source-backed preset identity tranche (Vegeta / Goku GT / Captain Ginyu)
- [x] Live producer baseline remains **51 preset records / 25 verified loadouts / 162 verified skill-slot entries**.
- [x] Added direct numeric-identity observations for **Vegeta Presets 10 and 11, Goku (GT) Preset 2, and Captain Ginyu Presets 5 and 6** to `docs/data/preset-battle-suit-reconciliation-2026-09-23.json`.
- [x] Evidence source: Burcol's 2024-11-22 preset-index video explicitly labels Vegeta 10 at 39:09, Vegeta 11 at 42:06, Captain Ginyu 5 at 31:23, Captain Ginyu 6 at 41:34, and Goku GT 2 at 45:50 (also repeated at 46:56).
- [x] Updated `docs/data/character-preset-skill-navigation-audit-2026-09-23.json` with the five-record evidence boundary.
- [x] Evidence limit preserved: numeric identity is confirmed, but the source does not expose the complete skill-slot configuration for those numeric IDs. No row-order, costume-order, or proximity inference was used; no loadouts were promoted.
- [x] Validation: both JSON files re-serialized successfully through the GitHub write path; canonical preset counts remain unchanged.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** find a source directly binding the numeric IDs for these five records to complete skill configurations; if unavailable, continue to the next unresolved family.


### 2026-09-24 cycle completion — current character-count consumer drift repair
- [x] Re-ran the live current-facing character consumer scan against `docs/data/characters-record-layer.json` rather than relying on stale repository search-index excerpts.
- [x] Confirmed the canonical producer contains **152** character identities.
- [x] Corrected `docs/data/characters/published-character-dlc-navigation-audit.json` from its superseded 153 live-count assertion to **152**, and corrected obsolete 151-name current prose while preserving historical context.
- [x] Corrected `docs/data/current-skill-domain-consumer-scan-2026-09-24.json` from its internal 153-character baseline/repair wording to **152**.
- [x] Re-fetched the related current consumers and confirmed the PQ endpoint validation, character presentation audit, partner-character navigation audit, current character/equipment/raid synchronization audit, DLC character-count reconciliation, and Chapter 4 character audit all use the live **152** count.
- [x] Preserved PQ-number references such as PQ153 and dated historical snapshots; no character identity or relationship was inferred or changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next priority:** continue deterministic current-facing event/raid/Festival/character/preset consumer scanning for stale scalars, duplicate presentation rows, orphan targets, one-way navigation, and canonical-ID drift; then resume the highest-impact source-backed preset/loadout or thin-domain expansion.


### 2026-09-24 cycle completion — exact Goku (GT) Preset 2 loadout
- [x] Completed the current Event/Raid/Festival/Chapter 4 consumer scan at the live baseline without finding deterministic stale current metadata requiring another repair.
- [x] Promoted `goku-gt-preset-2` to `loadout_status=verified` using exact named-loadout evidence plus independent numeric-preset identity evidence.
- [x] Added all 8 skill-slot entries: Power Pole Combo, Kamehameha, Instant Transmission, Charged Ki Wave, Super Spirit Bomb, Super Kamehameha, Spirit Explosion, and Super Saiyan.
- [x] Updated preset/loadout audit census from **25 / 162** to **26 / 170** verified loadouts / skill-slot entries.
- [x] Preserved evidence boundaries: no acquisition, exclusivity, reward, or gameplay claim was inferred.
- [ ] **Next:** continue unresolved preset families only where both numeric identity and complete skill configuration are directly evidenced; otherwise retain unresolved status and move to the next family.


### 2026-09-24 cycle completion — preset promotion evidence gate
- [x] Audited unresolved Goku 2–5, Vegeta 10–11, and Captain Ginyu 5–6 for direct loadout evidence.
- [x] Confirmed the available unlock video establishes preset identities but not complete eight-slot configurations.
- [x] Rejected an SSGSS Goku Preset 4 community loadout as evidence for base Goku Preset 4 because the character identity does not match.
- [x] Added `docs/data/character-preset-loadout-promotion-gates-2026-09-24.json` to preserve the evidence gate and avoid row-order inference.
- [x] Kept all affected records unresolved rather than promoting unsupported skill assignments.
- [ ] **Next:** locate explicit numeric-preset + complete-loadout evidence for the remaining unresolved families.


### 2026-09-24 cycle completion — version-aware preset evidence audit
- [x] Re-searched Goku Presets 2–5 for complete loadout evidence.
- [x] Strengthened numeric identity evidence using the maintained Burcol preset-index source.
- [x] Rejected older-Xenoverse and wrong-form/SSGSS evidence from contaminating Xenoverse 2 base-Goku records.
- [x] Updated `docs/data/character-preset-loadout-promotion-gates-2026-09-24.json` with the version-aware evidence boundary.
- [ ] **Next:** find version-correct numeric-preset + complete-loadout evidence for unresolved records.


### 2026-09-24 cycle completion — fresh preset source verification
- [x] Re-searched unresolved Goku Presets 2–5 with fresh web evidence.
- [x] Confirmed numeric identity without promoting unsupported loadouts.
- [x] Rejected SSGSS Goku Preset 4 evidence as the wrong roster identity for base Goku Preset 4.
- [x] Updated the preset evidence-gate audit.
- [ ] **Next:** locate complete version-correct numeric-preset loadout evidence.


### 2026-09-24 cycle completion — mentor explorer cross-navigation
- [x] Live mentor baseline verified from the canonical layer: **33 mentor identities / 133 lesson reward objects / 132 skill rewards / 1 typed non-skill reward / 131 mentor→skill edge rows / 130 unique canonical skill targets / 0 broken skill endpoints**.
- [x] Added `docs/Mentors-All.html`, a live canonical mentor explorer that reads `docs/data/mentors-record-layer.json` and exposes lesson→skill links into `Skills-All.html`.
- [x] Updated `docs/Skills-All.html` so canonical skill records with mentor provenance link back to the mentor explorer, completing the presentation-level mentor↔skill navigation loop.
- [x] Updated `docs/Mentors.md` and `README.md` to expose the new explorer and replaced the obsolete roadmap claim that the mentor catalog still needed normalization.
- [x] Added and registered `docs/data/mentor-presentation-consumer-audit-2026-09-24.json` in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the evidence boundary: Hit's Time Skip/Tremor Pulse remains the single unresolved skill lesson because no canonical skill ID exists; Zamasu's initiation reward remains typed as a Super Soul rather than a missing skill. No unlock condition, friendship threshold, reward probability, or gameplay mechanic was inferred.
- [x] Validation: audit JSON parses; cross-domain index parses and contains the new registration; explorer and reverse-navigation wiring were re-fetched and checked for the expected canonical data paths. CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next batch:** inspect the next uncovered current non-PQ presentation consumer, prioritizing the Expert Mission endpoint layer and its page/search navigation for stale counts, one-way links, orphan targets, and canonical-ID drift; preserve unresolved evidence boundaries, then resume source-backed preset/loadout expansion where direct numeric identity plus complete configuration can be established.


### 2026-09-24 cycle completion — Expert Mission presentation navigation + residual homepage consumer drift
- [x] Audited the live Expert Mission system index against the canonical `docs/data/expert-mission-endpoints.json` layer.
- [x] Added canonical skill endpoint links to `docs/Expert-Missions.md` for all **18/18** maintained EM→skill endpoint rows; EM01–02 remain intentionally without skill links because the endpoint layer contains 18 non-tutorial skill endpoints.
- [x] Added `docs/data/expert-mission-presentation-consumer-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **20/20** mission index entries remain present; **18/18** canonical EM skill endpoints render as direct `Skills-All.html?q=` links; audit status = pass; 0 broken endpoint links.
- [x] Corrected a residual current-facing homepage drift in `docs/index.md`: Super Soul census changed from the stale **18 populated records** to the live **230 canonical records**. Historical research counts were not rewritten.
- [x] Evidence boundaries preserved: no per-clear skill guarantee, drop rate, prerequisite, or EM17 Spirit Sword/Spirit Bomb conflict resolution was inferred. The Expert Mission endpoint layer remains the identity/navigation source.
- [x] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic current-facing consumer scanning outside the already-covered PQ/mentor/Expert Mission surfaces, prioritizing remaining homepage/reference count drift, one-way links, orphan targets, and canonical-ID namespace confusion; after that, resume the highest-impact source-backed preset/loadout tranche only where numeric preset identity and complete configuration are directly evidenced.


### 2026-09-24 cycle completion — homepage current consumer synchronization
- [x] Re-scanned the current homepage consumer after the mentor and Expert Mission presentation repairs.
- [x] Repointed all homepage mentor destinations from the general mentor page to the canonical `Mentors-All.html` explorer and replaced the loose **33+** label with the exact **33 canonical mentor identities** count.
- [x] Confirmed current homepage scalars/semantics: **672** is explicitly a skill-category-membership metric, **186** numbered PQs, **18** Awoken/Transformation targets, **230** canonical Super Souls, **51** Accessory Shop records, **116** canonical accessory identities, **36** TP/STP equipment-shop records, **45** Accessory→PQ research records, and **20** Expert Missions. These values are not treated as interchangeable canonical-record counts.
- [x] Added `docs/data/homepage-current-consumer-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: homepage mentor navigation now resolves to the canonical explorer; audit status = pass; historical dated audit files were intentionally left unchanged.
- [x] No new acquisition relationships, preset/loadout mappings, unlock conditions, or gameplay facts were inferred. CI/runtime remains unavailable.
- [ ] **Exact next batch:** scan the remaining non-PQ reference/summary consumers for stale scalar metrics and one-way navigation (especially Guides, Skills-Complete-Database, DLC overview, and system landing pages), then move into the highest-impact source-backed preset/loadout tranche with direct numeric identity + complete configuration evidence.


### 2026-09-24 cycle completion — non-PQ skill reference navigation repair
- [x] Audited the next uncovered current non-PQ skill-reference consumers: `docs/Guides.md` and `docs/Skills-Master-Database.md`.
- [x] Found both still linked to the obsolete `skills-database.html` target despite the canonical live explorer being `Skills-All.html`.
- [x] Repaired both links to `Skills-All.html`; no canonical skill data or acquisition relationship was changed.
- [x] Added and registered `docs/data/non-pq-skill-reference-navigation-audit-2026-09-24.json`.
- [x] Validation: obsolete target occurrences = 0 in the two audited consumers; new target occurrences = 2; canonical explorer exists; audit status = pass.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue scanning remaining non-PQ landing/reference consumers for obsolete explorer targets, stale scalar/list assumptions, orphan navigation, and canonical-ID drift; then resume source-backed preset/loadout expansion only where numeric identity + complete configuration are directly evidenced.


### 2026-09-24 cycle completion — global layout canonical explorer navigation
- [x] Audited both global Jekyll layouts: `docs/_layouts/home.html` and `docs/_layouts/wiki.html`.
- [x] Repointed global Skills, Characters, and Mentors navigation to the canonical searchable explorers: `Skills-All.html`, `Characters-All.html`, and `Mentors-All.html`.
- [x] Added `docs/data/global-layout-canonical-explorer-navigation-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: all three canonical routes are present in both layouts and obsolete landing routes were removed from these global navigation surfaces; audit status = pass.
- [x] Navigation-only change; no canonical records, relationships, or research assertions were altered. CI/runtime remains unavailable.
- [ ] **Exact next batch:** continue deterministic scan of remaining reference/landing pages for stale explorer targets, one-way links, and canonical-ID/count drift; prioritize DLC/system landing consumers before evidence-gated preset/loadout expansion.


### 2026-09-24 cycle completion — DLC character explorer navigation repair
- [x] Audited docs/DLC-Overview.md headline-character presentation links against the canonical docs/Characters-All.html explorer.
- [x] Repointed all 15/15 resolved DLC headline-character links from the generic /Search/ target to Characters-All.html?q=..., preserving identity labels and query strings.
- [x] Added docs/data/dlc/dlc-character-explorer-navigation-audit-2026-09-24.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Validation: 15/15 links target the canonical Character Explorer; 0 unresolved; 0 canonical relationship changes; audit status = pass.
- [x] Presentation-only change; no DLC ownership, character identity, preset/loadout, acquisition, or gameplay relationship was inferred.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: continue deterministic current-facing DLC/system landing consumer scanning for stale explorer targets, stale scalar/list assumptions, one-way navigation, orphan targets, and canonical-ID drift; then resume evidence-gated preset/loadout expansion.


### 2026-09-24 cycle completion — canonical Super Soul/equipment explorer self-navigation
- [x] Audited `docs/Super-Souls-All.html` and `docs/Equipment-All.html` self-navigation.
- [x] Repaired Super Soul entity links to `Super-Souls-All.html?q=...` and equipment/accessory entity links to `Equipment-All.html?q=...` instead of generic `/Search/`.
- [x] Added and registered `docs/data/canonical-explorer-self-navigation-audit-2026-09-24.json`.
- [x] Validation: 2/2 self-navigation consumers repaired; 0 relationship changes; audit pass.
- [x] Preserved PQ reverse navigation and all acquisition/data semantics.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic scanning of remaining non-PQ entity/reference explorers and landing pages for generic Search self-links, stale explorer targets, one-way cross-database navigation, stale counts, and canonical-ID drift; then resume evidence-gated preset/loadout research.


### 2026-09-24 cycle completion — remaining canonical cross-database navigation repair
- [x] Audited `Parallel-Quests-All.html`, `Awoken-All.html`, and `Partner-Customization.md` for deterministic cross-database navigation.
- [x] Repaired **24** links: PQ→Equipment (1), PQ→DLC (1), PQ→Characters (1), Awoken→Awoken Explorer (1), Partner Customization→Characters (20).
- [x] Added and registered `docs/data/remaining-canonical-cross-navigation-audit-2026-09-24.json`.
- [x] Validation: 24/24 targeted links repaired; no data/relationship semantics changed; audit pass.
- [x] Evidence boundary preserved: navigation-only changes.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** deterministic non-PQ landing/reference scan for remaining generic Search links, stale explorer targets, stale counts/list assumptions, orphan navigation, and canonical-ID drift; then evidence-gated preset/loadout expansion.


### 2026-09-24 cycle completion — character explorer self-navigation and DLC fallback correction
- [x] Repaired both `Characters-All.html` character self/search links to the canonical Character Explorer.
- [x] Verified DLC landing-page fallback semantics and restored PQ DLC links to generic Search because `DLC-Overview` is not a query explorer.
- [x] Added and registered `canonical-explorer-self-navigation-audit-2026-09-24-b.json`.
- [x] Validation passed with no relationship/data changes.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** finish remaining non-PQ landing/reference scan for stale explorer targets, stale counts/list assumptions, orphan navigation, and canonical-ID drift.


### 2026-09-24 cycle completion — global navigation explorer-target audit
- [x] Repointed wiki sidebar Super Souls → Super-Souls-All.html and Awoken Skills → Awoken-All.html.
- [x] Verified Expert Missions has no Expert-Missions-All.html; retained the existing landing route to avoid a broken link.
- [x] Added and registered global-navigation-canonical-explorer-audit-2026-09-24-c.json.
- [x] Validation passed; no data/relationship semantics changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: deterministic scan for stale counts/list assumptions, orphan navigation, and canonical-ID drift, then evidence-gated preset/loadout expansion.

### 2026-09-24 cycle completion — skill explorer self-navigation repair
- [x] Audited `docs/Skills-All.html` as the remaining canonical entity explorer with a generic `/Search/?q=` self-link.
- [x] Repointed the skill-card entity link to `Skills-All.html?q=...`, keeping skill navigation inside the canonical searchable Skill Explorer.
- [x] Extended `docs/data/canonical-explorer-self-navigation-audit-2026-09-24-b.json` to record the Skill Explorer repair alongside the previously audited Character Explorer/fallback scope.
- [x] Confirmed the central cross-domain index already registers the audit; no index mutation was required.
- [x] Validation: `Skills-All.html` contains **0** generic Search self-link definitions and **1** canonical Skill Explorer self-link definition; audit JSON parses; audit status = pass; central index registration resolves.
- [x] No skill identity, acquisition, provenance, mechanics, PQ relationship, mentor relationship, or gameplay fact was changed.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic non-PQ landing/reference scanning for stale scalar/list assumptions, one-way links, orphan targets, and canonical-ID drift across system pages and reference consumers; then resume evidence-gated preset/loadout expansion only where numeric preset identity and complete configuration are directly evidenced.

### 2026-09-24 cycle completion — current preset/loadout evidence boundary
- [x] Recomputed the live canonical preset layer: 51 canonical preset/character configuration records / 26 verified loadout records / 25 unresolved loadout records.
- [x] Deterministically checked all 26 verified loadout records for required evidence fields; 26/26 have a loadout object, loadout source, and non-empty source list.
- [x] Audited the unresolved numeric core: Goku Presets 2–12 and 14–18, Vegeta Presets 10–11, and Captain Ginyu Presets 5–6 have direct numeric-identity observations from the maintained community video, but not complete numeric-to-loadout bindings.
- [x] Cross-checked current external evidence for the boundary: the current Goku in-game-data table exposes complete named/costume loadouts but does not safely bind them to repository numeric IDs; the Orange Piccolo page exposes a complete one-preset named loadout but no repository numeric preset ID.
- [x] Added and registered docs/data/preset-loadout-current-evidence-audit-2026-09-24.json.
- [x] Preserved the evidence boundary: 0 preset loadout promotions were made; no row-order, costume-order, chapter-order, or visual-proximity mapping was inferred.
- [x] Validation: canonical preset JSON parsed; 26/26 verified records satisfy required evidence fields; audit JSON and central index registration validated.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Exact next batch: locate a source that directly binds numeric Goku Presets 2–18, Vegeta Presets 10–11, or Captain Ginyu Presets 5–6 to complete skill-slot configurations; promote only directly bound configurations, then synchronize the preset navigation audit and canonical projections.

### 2026-09-24 cycle completion — preset evidence corroboration
- [x] Checked current Goku in-game-data evidence and a dated Burcol preset/unlock video against the unresolved numeric preset records.
- [x] Confirmed the video directly labels several unresolved numeric identities (including Goku 8/10/12/14/18, Vegeta 11, and Captain Ginyu 5/6), while the Goku data page supplies complete named loadouts without a safe numeric binding.
- [x] Added this corroboration to `docs/data/preset-loadout-current-evidence-audit-2026-09-24.json`.
- [x] Promotion count remains 0; no numeric-to-named mapping was inferred from ordering or visual proximity.
- [ ] Exact next batch: search for a direct source that exposes both the numeric preset label and its complete skill slots; if none exists, continue other exhaustive repository coverage rather than weakening the evidence boundary.


### 2026-09-24 cycle completion — preset/loadout evidence boundary validator
- [x] Added `scripts/validate_preset_loadout_evidence.py` to enforce the evidence gate for numeric preset/loadout promotion.
- [x] Validator requires every verified loadout to contain a loadout object, explicit loadout_source, and non-empty sources; current live result: **26/26 pass**.
- [x] Validator preserves the unresolved numeric boundary for **20** expected records: Goku Presets 2–12 and 14–18, Vegeta Presets 10–11, Captain Ginyu Presets 5–6.
- [x] Live census: **51** preset records, **26** verified loadouts, **25** unresolved; **0 duplicate IDs**.
- [x] Updated `docs/data/preset-loadout-current-evidence-audit-2026-09-24.json` with validator/parity results.
- [x] No unsupported numeric-to-loadout promotion was made.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** continue deterministic current-facing reference/landing consumer scan for stale counts, orphan targets, and canonical-ID drift; return to preset research only with direct numeric-label + complete skill-slot evidence.


### 2026-09-24 cycle completion — canonical explorer target inventory
- [x] Inspected current landing/navigation surfaces and verified canonical searchable explorer targets: Characters-All.html, Skills-All.html, Parallel-Quests-All.html, Equipment-All.html, Super-Souls-All.html, Awoken-All.html, and Mentors-All.html.
- [x] Confirmed no Expert-Missions-All.html target is emitted; Expert Missions remain on their existing landing/database surfaces.
- [x] Confirmed Parallel-Quests-All.html reward/character navigation uses canonical explorer targets, with DLC retaining generic Search fallback because DLC-Overview is a landing page.
- [x] Extended docs/data/current-presentation-consumer-scan-2026-09-24.json with the explorer target inventory.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** inspect remaining system/reference consumers for canonical-ID drift and one-way navigation, prioritizing any surface not covered by the current presentation scan.


### 2026-09-24 cycle completion — homepage canonical explorer target synchronization
- [x] Re-audited `docs/index.md` against the live canonical explorer inventory.
- [x] Repaired legacy homepage destinations for Characters, Super Souls, and Equipment so they open the canonical searchable explorers where one exists.
- [x] Preserved existing canonical counts and semantics; no data/relationship facts were altered.
- [x] Added `docs/data/homepage-canonical-explorer-navigation-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: targeted obsolete landing links = 0; canonical explorer targets present; audit status = pass.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next batch:** deterministic scan of remaining system/reference landing consumers for stale explorer targets and scalar/count drift, especially DLC, Super Soul/Equipment reference pages, and system landing pages not covered by the current audit registry; then return to direct-evidence preset/loadout expansion.


### 2026-09-24 completed preset projection census synchronization
- [x] Recomputed the live canonical preset producer directly from docs/data/character-presets-record-layer.json: 51 records / 26 verified loadouts / 25 unresolved loadouts / 0 duplicate IDs.
- [x] Revalidated scripts/validate_preset_loadout_evidence.py: all 26 verified records have loadout object + explicit loadout source + non-empty sources; the 20-record numeric unresolved boundary remains intact.
- [x] Corrected three stale current-facing projections from 25 → 26 verified loadouts: docs/data/current-presentation-consumer-scan-2026-09-24.json, docs/data/characters/character-presentation-consumer-audit.json, and docs/data/goku-preset-loadout-source-boundary-2026-09-24.json.
- [x] Direct numeric-to-complete-loadout web research remained insufficient for Goku Presets 2–18, Vegeta Presets 10–11, and Captain Ginyu Presets 5–6; no unsupported promotion was made.
- [x] Restored the unexpectedly empty docs/AI-CONTINUATION-PROMPT.md from the latest non-empty handoff revision and appended the current cycle state.
- [x] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: continue deterministic preset/character consumer scanning for stale projections and one-way navigation, then pursue direct numeric preset-label + complete eight-slot configuration evidence only where explicitly supported.

### 2026-09-24 completed Character Preset Research navigation bridge
- [x] Audited docs/Character-Preset-Research.md as a high-connectivity preset research consumer.
- [x] Added canonical explorer navigation for Characters, Skills, Parallel Quests, Equipment/Accessories, and Super Souls.
- [x] Extended docs/data/character-preset-research-presentation-consumer-audit-2026-09-24.json with the five-target navigation contract.
- [x] Verified the five canonical explorer targets exist in the live repository tree.
- [x] Preserved the evidence boundary: navigation changes do not create preset/loadout/acquisition relationships.
- [ ] Next: continue deterministic preset/character consumer scanning for stale projections and one-way links, then pursue explicit numeric preset + complete configuration evidence.

### 2026-09-24 completed system/reference canonical explorer bridge
- [x] Added canonical explorer navigation to DLC Overview, Super Souls, Equipment, Mentors, Awoken Skills, and Parallel Quests reference pages.
- [x] Kept navigation-only semantics separate from factual relationship/acquisition/mechanics evidence.
- [ ] Next: scan remaining system/reference consumers for stale counts, legacy destinations, and one-way links; then resume direct preset/loadout evidence research.

### 2026-09-24 completed global navigation PQ migration
- [x] Replaced the live wiki-layout Parallel Quests legacy route with `Parallel-Quests-All/`.
- [x] Kept Expert Missions on its existing route because no canonical explorer currently exists.
- [x] Updated the global navigation audit with the repaired target.
- [ ] Next: continue remaining stale-count/legacy-destination/one-way-link scan, then resume direct preset/loadout evidence research.

### 2026-09-24 completed PQ explorer validator contract synchronization
- [x] Audited the live PQ explorer against its consumer validator after canonical cross-database navigation repairs.
- [x] Repaired the stale `scripts/validate_pq_page_consumers.py` skill-navigation assertion so it validates the live `Skills-All.html?q=...` contract instead of the obsolete Search-based `searchUrl(v)` assumption.
- [x] Added and registered `docs/data/pq-explorer-validator-contract-synchronization-2026-09-24.json`.
- [x] Preserved the intentional PQ→DLC Search fallback and all canonical relationship/acquisition semantics.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] Next: continue deterministic Event/Raid/Festival/Chapter 4 consumer scanning, then resume evidence-gated numeric preset/loadout expansion.


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
- [x] Web research also reconfirmed that the strongest readily indexed numeric-preset source still exposes numeric identity/unlock placement rather than complete slot configurations; no unsupported preset promotion was made. cite
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

### 2026-09-24 completed remaining system/reference consumer scan
- [x] Audited the remaining high-connectivity system/reference surfaces: Skills Master/Complete Database, Characters, Mentors, Awoken Skills, DLC Overview, Super Souls, QQ Bangs, QQ Bang Database, and Expert Missions.
- [x] Added `docs/data/system-reference-consumer-scan-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Confirmed dedicated canonical explorer destinations are used where they exist: Characters, Skills, Parallel Quests, Equipment, Super Souls, Awoken, and Mentors. No stale explorer destination or unsupported replacement target was found in this bounded scan.
- [x] Preserved source-category snapshot semantics in Skills Master Database and the separate official mentor-count context; neither was incorrectly converted into a canonical repository total.
- [x] Did not invent Super Soul, QQ Bang, or Expert Mission explorers where the repository has no dedicated canonical explorer.
- [x] No relationship, acquisition, probability, mechanics, or completeness claims were added.
- [x] Commits: `3130d721e5ff6ea2e34f73d7d4fadec27ee3e80f` (audit), `78f37d623e56e75e83a3058783f38a9b1ce69f86` (registry).
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue evidence-gated numeric preset/loadout research for Goku Presets 2–12 and 14–18, Vegeta 10–11, and Captain Ginyu 5–6 only where one source directly binds the numeric preset label to a complete configuration; otherwise expand the next thin structured domain without inference.

### 2026-09-24 completed strict-thin Super Soul 032/034 evidence refresh
- [x] Rechecked the two remaining strict-thin Super Soul records: `super-soul-032` and `super-soul-034`.
- [x] Confirmed PQ 185 and PQ 186 exact-name reward identity from the current 186-PQ guide.
- [x] Confirmed the community-reported second activation/name-state for Super Soul 032: after the relevant activation, its displayed name changes when the user is KO'd. This observation was already preserved in the canonical record and therefore required no speculative field promotion.
- [x] Searched current community discussion for Super Soul 034 mechanics; no sufficiently reliable item-level evidence was found to resolve its effect, Limit Burst, or character source. Explicit null/unresolved fields remain intact.
- [x] Added `docs/data/super-soul-032-034-strict-thin-evidence-refresh-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: 2/2 targets resolved; unsupported promotions 0; explicit unresolved fields preserved.
- [x] Commit: `212637a29f7f991d7e6cbf849594a08a80263b7f`; registry commit `19e22b72755010ae967b5c8c8d601ebdec6b1862`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** resume the highest-impact evidence-gated numeric preset batch, seeking a single artifact that binds a numeric preset identifier to its complete eight-slot configuration; if still unavailable, perform the next bounded provenance pass over the thinnest unresolved skill endpoint records without inference.

### 2026-09-24 completed Goku numeric preset loadout evidence recheck
- [x] Audited all 16 currently indexed unresolved Goku numeric preset records: 2–12 and 14–18.
- [x] Current Fandom search evidence confirms Goku's numeric preset table exists and exposes direct numeric Preset → Skills → Super Soul mapping for rows visible in the indexed search result; the current page reports 19 main-slot presets. cite
- [x] Community unlock-video chapters independently confirm discovery/acquisition events for multiple targeted Goku presets, but do not constitute complete eight-slot loadout evidence. cite
- [x] No loadout was promoted because the directly extractable evidence did not expose complete eight-slot configurations for the targeted records. No inference from neighboring preset order or video timestamps was used.
- [x] Added `docs/data/goku-numeric-preset-loadout-evidence-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: 16 targets checked; 0 loadout promotions; 0 unsupported promotions.
- [x] Commits: `c157430190381c158d742297bf9dc0dca78435a7` (audit), `c7fe5492d96331c211e92bc9ce057eae35831dcc` (registry).
- [ ] **Exact next:** locate a directly extractable complete Goku preset table or equivalent artifact, then promote verified loadouts in a batch. If unavailable, move to Vegeta 10–11 / Captain Ginyu 5–6 using the same evidence gate.

### 2026-09-24 completed Vegeta Presets 10–11 evidence pass
- [x] Rechecked both unresolved numeric preset records against directly extractable current evidence.
- [x] Community unlock evidence explicitly identifies Vegeta Presets 10 and 11, but only as acquisition/discovery events, not complete loadouts. cite
- [x] Current Vegeta in-game-data search evidence exposes the numeric preset table, but directly extractable results did not provide complete Presets 10–11 rows sufficient for eight-slot promotion. cite
- [x] Preserved both records as indexed/unresolved; no inferred skills, awoken, evasive, or Super Soul fields were added.
- [x] Added and registered `docs/data/vegeta-10-11-preset-loadout-evidence-audit-2026-09-24.json`.
- [x] Commits: `c74f76e6a70352f4ef665910e27c4c4511e764bf`, `216775a5189aa8bf504e4625fdeb47a282bc069a`, `1d8b8f083f68104f1aaf92c681e9ac38d307751c`.
- [ ] **Exact next:** audit Captain Ginyu Presets 5–6 with the same complete-loadout evidence gate.

### 2026-09-24 completed Captain Ginyu Presets 5–6 evidence pass
- [x] Audited both unresolved numeric Captain Ginyu presets.
- [x] Community unlock evidence explicitly identifies Preset 5 at 31:23 and Preset 6 at 41:34, but does not expose complete loadouts. cite
- [x] Japanese gameplay reference documents Ginyu configurations, but does not bind its unlabeled configurations to numeric Presets 5–6; no sequence inference was used. cite
- [x] Legacy GameFAQs documentation provides variant skills but does not establish current numeric 5–6 mapping. cite
- [x] No loadout fields were promoted; both records remain indexed/unresolved.
- [x] Added and registered `docs/data/captain-ginyu-5-6-preset-loadout-evidence-audit-2026-09-24.json`.
- [x] Commits: `44d5cfa2921f201e94aad91a91d148cfcf3247c3`, `4af784c97d1c7133e53492485466e7a877865ae8`.
- [ ] **Exact next:** find a source explicitly binding Captain Ginyu Presets 5–6 to complete loadout rows; if unavailable, proceed to the next unresolved numeric preset batch without inference.


### 2026-09-24 completed mentor endpoint producer/consumer synchronization
- [x] Reconciled the current Hit mentor lesson 3 endpoint for **Time Skip/Tremor Pulse** without fabricating a canonical skill ID.
- [x] Cleared the unsupported Hit lesson skill_id from docs/data/mentors-record-layer.json and removed the orphan endpoint from docs/data/mentor-endpoints.json forward/reverse projections.
- [x] Synchronized current mentor presentation and coverage consumers to **33 mentors / 133 lesson reward objects / 131 typed skill rewards / 1 typed non-skill reward / 131 mentor→skill edges / 130 unique skill targets / 1 unresolved skill lesson / 0 broken endpoints**.
- [x] Added and registered docs/data/mentor-endpoint-consumer-synchronization-2026-09-24.json.
- [x] Evidence confirms the exact lesson identity/acquisition route: Hit's fourth mentor reward / Lesson 3 is Time Skip/Tremor Pulse. Canonical skill identity remains unresolved.
- [x] Validation passed for endpoint parity and current consumer agreement; CI/runtime remains unavailable.
- [ ] **Next:** continue the deterministic non-PQ/mentor consumer scan for stale scalars, orphan endpoint IDs, and one-way navigation; only promote Time Skip/Tremor Pulse after a standard canonical skill record exists.


### 2026-09-24 completed mentor-derived acquisition consumer reconciliation
- [x] Reconciled current-facing mentor-derived skill acquisition projections after the Hit → Time Skip/Tremor Pulse endpoint repair.
- [x] Removed the unresolved Hit skill ID from `docs/data/mentors.json` resolved projection.
- [x] Current mentor acquisition projection is now **131 resolved mentor→skill edges / 130 unique resolved skill targets**.
- [x] Preserved the distinction between **132 typed skill reward lessons** and **131 resolved canonical skill endpoints**, with **1 unresolved skill lesson**.
- [x] Corrected current acquisition/presentation audits and `docs/Mentors.md`; historical snapshots remain preserved.
- [x] Added/registered `docs/data/mentor-derived-acquisition-consumer-reconciliation-2026-09-24.json`.
- [x] Validation passed: no unresolved Hit skill ID in resolved projections, 0 broken endpoints, crosslink/current acquisition parity maintained.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** continue the deterministic non-PQ/mentor consumer scan for any remaining current-facing references to `skill-time-skip-tremor-pulse` or stale 132-edge/131-target counts; preserve explicitly historical snapshots.


### 2026-09-24 completed remaining mentor acquisition stale-count sweep
- [x] Found and corrected the final current top-level stale mentor acquisition counts in `docs/data/skill-acquisition-coverage-report.json`: **132/131 → 131/130** resolved edges/targets.
- [x] Confirmed the removed Hit → `skill-time-skip-tremor-pulse` ID has no current canonical/projection occurrence; remaining occurrences are explicitly historical/audit evidence.
- [x] Preserved historical `docs/COVERAGE-AUDIT.md` counts under append-only rules.
- [x] Validation: current mentor projection 131 resolved edges / 130 unique targets; 133 lesson rewards / 132 typed skill rewards / 1 non-skill reward / 1 unresolved skill lesson; 0 broken endpoints.
- [x] Commit: `db9db28c1d35a43babeda0098e8ff79c8871e587`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** bounded current-facing non-PQ acquisition consumer sweep outside the mentor layer, prioritizing stale scalar projections and one-way links.


### 2026-09-24 completed non-PQ endpoint-layer stale mentor count repair
- [x] Found the remaining current stale mentor endpoint-layer scalar in `docs/data/skill-acquisition-cross-domain-endpoint-audit-2026-09-24.json`.
- [x] Corrected mentor endpoint count **132 → 131** and recorded the 130 unique resolved target baseline.
- [x] Preserved historical counts and made no unsupported acquisition inference.
- [x] Commit: `1376634625eecdd45b66db014218231b737d270d`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** bounded non-PQ reverse-projection sweep across Expert Mission, shop, special, and remaining endpoint consumers.

### 2026-09-24 completed stale metadata census validation repair
- [x] Reconciled the current-looking validation block in `docs/data/skill-stale-metadata-census-2026-09-23.json` from 465/465 to the live 469/469 canonical/index baseline.
- [x] Preserved historical 465 context and did not alter canonical skill data.
- [x] Commit: `f295e2ae1c0c2ada350e068aae1550c8ba0d7b52`.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** sweep remaining current-facing acquisition indexes/projections for one-way links and stale scalars.


### 2026-09-24 completed bounded non-PQ acquisition consumer sweep
- [x] Added and registered `docs/data/current-nonpq-acquisition-consumer-sweep-2026-09-24.json`.
- [x] Revalidated current skill acquisition projection and endpoint parity at **469 canonical / 239 PQ-linked / 230 non-PQ / 131 resolved mentor edges / 130 unique mentor targets / 99 non-PQ non-mentor targets / 469 endpoint-covered / 0 uncovered**.
- [x] Confirmed current Time Rift/story/tournament and shop endpoint layers remain 13 and 33 forward skill edges respectively.
- [x] Classified remaining 465/132-style search hits as historical/provenance or already-reconciled audit context; no additional current-facing scalar repair was justified.
- [x] No acquisition, mechanics, probability, availability, or preset/loadout inference was introduced.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** resume P1 source-backed provenance enrichment or direct numeric preset/loadout evidence; only promote a numeric preset when one artifact directly binds its label to the complete configuration.


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

### 2026-09-24 cycle completion — Savage Strike provenance boundary and audit registration
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-163.json` for Savage Strike with current evidence: SSGSS Vegito identity, Strike Super classification, TP Medal Shop acquisition, 100 Ki evidence, and alternate-input/knockback-pursuit mechanics.
- [x] Preserved the TP Medal Shop price conflict: dated sources report 200 TP Medals while a later secondary guide reports 300; no exact current price was promoted.
- [x] Added and registered `docs/data/savage-strike-provenance-audit-2026-09-24.json`.
- [x] Also registered the already-updated 2026-09-24 Present For You→Purification and Quick Sleep→Saiyan Spirit provenance audit artifacts so current research evidence is represented in the cross-domain registry.
- [x] Verified the live canonical/index layers remain **469/469**; Savage Strike is not currently present in either canonical `skills.json` or `skills-index.json`.
- [x] Intentionally did **not** insert an index-only Savage Strike record, because that would break canonical/index parity.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** integrate `skill-savage-strike` into canonical `docs/data/skills.json` and `docs/data/skills-index.json` together through the supported canonical build/update path, then reconcile any acquisition/cross-domain projections that require the new canonical endpoint. Preserve the unresolved TP Medal Shop price conflict and do not infer from legacy TP rotation data.

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
- [x] Refreshed Quick Sleep research provenance to the live 2026-09-24 evidence boundary: Majin-only Other Super, 0 Ki, 0 Stamina, Skill Shop after defeating Mira (Final Form) in the main story.
- [x] Preserved the TP/STP Medal rotation mention as alternate provenance only; no second canonical endpoint or current rotation/price claim was introduced.
- [x] Refreshed the canonical `docs/data/skill-shop-endpoints.json` Quick Sleep edge from `last_verified=2026-09-23` to `2026-09-24`.
- [x] Added and registered `docs/data/quick-sleep-shop-endpoint-provenance-reconciliation-2026-09-24.json`.
- [x] Validation target: 469 canonical skills / 469 index skills / 1 Quick Sleep shop edge / 0 duplicate Quick Sleep edges / 0 unresolved Quick Sleep endpoint.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** reconcile downstream Quick Sleep consumers to the refreshed endpoint date, then continue with the next evidence-backed P1 target only where a bounded canonical/index or endpoint change is directly supported.


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


### 2026-09-24 completed Time Skip/Tremor Pulse research enrichment
- [x] Strengthened the existing Hit mentor research record with current direct evidence: Strike Evasive, 200 Stamina, CaC-usable, Hit Lesson 3/fourth mentor reward, Super Class prerequisite, unblockable directional teleport behavior, and a source-backed 7% damage reference retained as research-only.
- [x] Added and registered `docs/data/skill-time-skip-tremor-pulse-research-enrichment-2026-09-24.json`.
- [x] Preserved the unresolved canonical boundary: no `skill-time-skip-tremor-pulse` record was inserted into `skills.json` or `skills-index.json`, and no mentor endpoint edge was restored by inference.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** losslessly run the standard skill builder when runtime is available; then validate canonical/index parity and reconcile the Hit mentor endpoint. If unavailable, continue the next evidence-backed thin-domain enrichment rather than guessing.


### 2026-09-24 completed Savage Strike P1 provenance enrichment
- [x] Strengthened Savage Strike research provenance without changing canonical identity or inventing a shop price.
- [x] Added and registered `docs/data/skill-savage-strike-p1-provenance-enrichment-2026-09-24.json`.
- [x] Advanced `docs/data/skill-p1-provenance-coverage-gap-2026-09-24.json`; Pressure Sign is now the next bounded P1 target.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** evidence-bound Pressure Sign provenance audit and canonical/index validation.


### 2026-09-24 completed Punisher Shield P1 provenance refresh
- [x] Refreshed Punisher Shield provenance for identity, Counter taxonomy, CaC availability, DLC provenance, Ki cost, and PQ129 acquisition.
- [x] Added and registered `docs/data/skill-punisher-shield-p1-provenance-enrichment-2026-09-24.json`.
- [x] Preserved unresolved Ultimate Finish, reward probability, and detailed combat measurements.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** select the next unresolved P1 research target and perform an evidence-bound provenance refresh.


### 2026-09-24 completed Critical Upper P1 provenance refresh
- [x] Verified Critical Upper identity, classification, 100 Ki cost, and Dodoria Lesson 1 acquisition.
- [x] Added and registered `docs/data/skill-critical-upper-p1-provenance-enrichment-2026-09-24.json`.
- [x] Preserved unsupported stamina, frame, probability, and universal damage claims.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** select the next unresolved P1 provenance target.


### 2026-09-24 completed Dimensional Hole P1 provenance refresh
- [x] Verified Dimensional Hole identity/classification, CaC availability, 0 Ki, and PQ80 Basic Reward route.
- [x] Added and registered `docs/data/skill-dimensional-hole-p1-provenance-enrichment-2026-09-24.json`.
- [x] Preserved unsupported probability, stamina, frame, and universal damage data.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Next:** select the next unresolved P1 provenance target.

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
- [x] Web verification corroborated the repository research: the Xenoverse 2 ID list identifies Acid 140 and Howl 10440 as non-CaC skills, while Xenoverse 2-specific pages document the corresponding Saibaman/Great Ape movesets. cite
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved gap records, prioritizing Boiling Burg / Energy Boil / Baked Sphere / Boulder Toss / Boulder Break with direct Xenoverse 2 evidence; preserve the 469/469 canonical boundary until supported builder execution is available.

### 2026-09-24 continuation — five unresolved skill audits registered
- [x] Refreshed Energy Boil, Baked Sphere, Boulder Toss, and Boulder Break evidence audits; Boiling Burg was refreshed in the preceding cycle.
- [x] Updated the central research-gap ledger and registered all five audits in `docs/data/pq-cross-domain-index.json`.
- [x] JSON validation passed for all affected research-gap records.
- [ ] No canonical skill promotion; 469/469 boundary preserved.
- [ ] CI/runtime unavailable.
- [ ] Exact next: continue unresolved thin-domain research, seeking direct evidence for currently missing fields rather than duplicating identity-only corroboration.


### 2026-09-24 cycle completion — Boulder Toss + Boulder Break subtype reconciliation
- [x] Re-read the live continuation handoff, efficiency addendum, and exhaustive TODO before editing.
- [x] Reconciled **Boulder Toss** (skill ID 441) and **Boulder Break** (skill ID 442) against the existing repository batch-286 taxonomy correction and current Xenoverse 2 Great Ape quest/technique evidence.
- [x] Updated both dedicated evidence audits to record **Strike** as research-supported while retaining unresolved numeric `ki_cost`.
- [x] Updated `docs/data/skill-research-gaps.json`: both records now have only `ki_cost` unresolved.
- [x] Preserved the canonical integration boundary: no manual insertion into the 469/469 oversized canonical catalogs; supported builder/runtime remains unavailable.
- [x] Validation: audit JSON and central gap ledger were updated through the GitHub API; registry already contains both audit paths; no gameplay/acquisition relationship was invented.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next: continue the remaining unresolved gap set, prioritizing **Boiling Burg**, **Energy Boil**, **Baked Sphere**, **Boiling Ball**, and **Tricky Strike** only where direct Xenoverse 2 evidence can resolve a currently missing field; otherwise preserve the evidence boundary.


### 2026-09-24 continuation — Demigra five-skill gap reconciliation
- [x] Followed the recorded next queue: **Boiling Burg, Energy Boil, Baked Sphere, Boiling Ball, Tricky Strike**.
- [x] Reconciled **Baked Sphere** research taxonomy to **Explosive Wave** and reduced its central unresolved field set to `ki_cost` only.
- [x] Audited the other four records against current evidence; no additional canonical subtype or numeric Ki-cost field met the repository evidence boundary.
- [x] Added `docs/data/skill-research-gap-reconciliation-2026-09-24-demigra-five.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved all guardrails: no cross-game cost inference, no enemy-only acquisition routes, and no manual insertion into the oversized canonical skill catalogs.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved skill-gap queue after this five-record pass, prioritizing fields that can be directly resolved from Xenoverse 2-specific evidence rather than repeating identity verification.


### 2026-09-24 continuation — Acid + Howl acquisition-boundary reconciliation
- [x] Audited **Acid** and **Howl** as the next unresolved queue items using current Xenoverse 2-specific references plus the live research audits.
- [x] Acid: preserved distinct normal skill ID **140** and raid-boss ID **143**; classification is Super Skill; CaC acquisition is not documented; only `ki_cost` remains unresolved.
- [x] Howl: classification is Evasive Skill; CaC acquisition is not documented; only `ki_cost` remains unresolved.
- [x] Updated the central gap ledger and both dedicated audits to explicitly record the no-CaC-unlock boundary rather than leaving `unlock_method` ambiguously unresolved.
- [x] Current web verification corroborates Acid's Saibaman usage and Howl's Great Ape/Evasive usage, but did not expose a trustworthy canonical numeric Ki cost.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved skill-gap queue, prioritizing records with fields that can be resolved by direct Xenoverse 2 evidence; do not infer numeric Ki costs from other games or mods.


### 2026-09-24 continuation — Neo Wolf Fang Fist P1 provenance enrichment
- [x] Selected Neo Wolf Fang Fist as the next partially verified P1 target after the current verification-date census was exhausted.
- [x] Added `docs/data/skill-neo-wolf-fang-fist-p1-provenance-enrichment-2026-09-24.json`.
- [x] Reconciled existing research to current Xenoverse 2 evidence: Strike Super, PQ86 acquisition, and variable 100–700 Ki usage.
- [x] Preserved unresolved exact drop probability, frame data, and universal damage fields; no unsupported Ultimate Finish gate was added.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next partially verified P1 research target with direct Xenoverse 2 evidence, while preserving unresolved technical fields.

### 2026-09-24 cycle completion — Boiling Ball + Tricky Strike subtype reconciliation
- [x] Reconciled Boiling Ball (ID 541) and Tricky Strike (ID 542) against repository research batch 289 and current Xenoverse 2-specific evidence.
- [x] Boiling Ball is research-supported as Super / Ki Blast; Tricky Strike is research-supported as Super / Strike.
- [x] Updated docs/data/skill-research-gaps.json so both records now have only ki_cost unresolved; no CaC acquisition route or numeric cost was invented.
- [x] Updated both dedicated evidence audits to preserve the resolved subtype and explicit unresolved Ki-cost boundary.
- [x] Canonical skill catalogs remain untouched at the established 469/469 boundary.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: 97a09fd5653ef8fd497b202e5059f77e86ffdd09, 16b4c1a5c67429e262c5200260ad1fd6f9a417c9, 617559a481b5dc12033dd3b7a6d6d3025ae7f7ad, bd5524d7a7964868074fd7033be420e057ece610.
- [ ] **Exact next:** continue the next unresolved thin-domain candidate after Boiling Ball/Tricky Strike, prioritizing a record whose remaining field can be resolved by direct Xenoverse 2 evidence; preserve the 469/469 canonical boundary until the supported builder/runtime is available.

### 2026-09-24 continuation — Energy Boil evidence-boundary pass
- [x] Followed the post-Boiling Ball/Tricky Strike queue and selected **Energy Boil** as the next unresolved thin-domain record.
- [x] Strengthened the dedicated Energy Boil evidence audit with current reference evidence confirming its Final Form Demigra Evasive identity, ID 10540, and CaC-unavailable boundary.
- [x] Preserved the evidence boundary: `subcategory` and `ki_cost` remain unresolved because no trustworthy canonical XV2 subtype or numeric cost was exposed. No subtype was inferred from animation/function wording.
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
- [x] Added `docs/data/skill-research-gaps-energy-boil-evidence-boundary-refresh-2026-09-24.json` and registered it in the cross-domain index.
- [x] Reconfirmed Xenoverse 2 ID 10540/short ID 540, Final Form Demigra ownership, CaC-unavailable status, and Evasive classification; current accessible evidence still does not expose the repository subcategory or numeric Ki cost.
- [x] Updated the central Energy Boil gap note without promoting unsupported taxonomy, cost, acquisition, or canonical catalog data.
- [x] Validation: canonical/index **469/469**, duplicate IDs **0**; changed JSON artifact parses; no CI success claimed.
- [ ] **Exact next:** continue the remaining unresolved thin-domain queue only where direct Xenoverse 2 evidence can resolve a missing field; otherwise resume source-backed P1 enrichment.


### 2026-09-24 cycle completion — Acid evidence refresh
- [x] Added and registered the Acid evidence refresh audit.
- [x] Reconfirmed normal ID 140 and separate raid ID 143, Super classification, CaC-unavailable boundary, and Saibaman 2 usage.
- [x] Numeric Ki cost remains unresolved; no unsupported canonical promotion was made.
- [x] Canonical skill/index boundary remains 469/469.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the unresolved thin-domain queue where direct Xenoverse 2 evidence can resolve a missing field.


### 2026-09-24 cycle completion — Savage Strike acquisition-terminology consistency correction
- [x] Corrected the Savage Strike research record's generic Skill Shop wording to **TP Medal Shop**, matching its canonical acquisition fields and provenance evidence.
- [x] Updated the dedicated Savage Strike audit; unresolved TP Medal price/rotation conflict remains preserved.
- [x] Canonical/index parity remains **469/469**; no premature promotion was made.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue source-backed P1 enrichment with substantive evidence-field improvements.


### 2026-09-24 cycle completion — Quick Sleep handoff reconciliation
- [x] Recorded Quick Sleep Ki-cost correction from 0 to 300 using Xenoverse 2-specific evidence.
- [x] Preserved unresolved recovery/timing/damage details.
- [x] Canonical/index parity remains 469/469.
- [ ] CI/runtime unavailable; no CI success claimed.
- [ ] **Exact next:** continue substantive P1 evidence enrichment.


### 2026-09-24 cycle completion — bounded skill P1 provenance enrichment, PQ87–PQ91
- [x] Selected the next substantive P1 batch from existing research batch 54 after the verification-date queue was exhausted: **Atomic Blast, Buu Buu Ball, Victory Rush, III Bomber, and Final Kamehameha**.
- [x] Added `docs/data/skill-pq87-pq91-p1-provenance-enrichment-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-54.json` with current Xenoverse 2-specific classification, resource, acquisition, and mechanics evidence.
- [x] Corrected the research-layer **Buu Buu Ball** classification from stale Ultimate/Ki Blast metadata to **Strike Evasive**, **300 Stamina**, **Majin CaC**; the correction is source-backed by the current Xenoverse 2 skill reference.
- [x] Added current mechanics evidence for Atomic Blast, Victory Rush, and III Bomber while preserving unresolved universal damage/probability fields.
- [x] Preserved the **Final Kamehameha** acquisition conflict: current reference lists PQ91 and TP Medal Shop, while historical player reports discuss Ultimate-Finish/RNG behavior and the maintained PQ transcription places it in Basic Rewards. `ultimate_finish_required` remains unresolved; no drop probability was invented.
- [x] Canonical `skills.json` / `skills-index.json` were not manually reconstructed; the established **469/469** boundary is preserved until the supported builder/runtime is available.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: audit `d030db0bf8e89dfff7e793575d7c80c03caeeccc`; research batch `2fd2100ce2544cd4114211dbc7605b64d075a60b2`; registry `1989441c167f340709679293f5fc02283ab4c645`.
- [ ] **Exact next:** continue substantive P1 enrichment from the next existing partially verified research batch after PQ87–PQ91, prioritizing records where current Xenoverse 2 evidence can resolve real classification/resource/acquisition/mechanics fields. Do not manually promote into the 469/469 canonical catalogs without the supported builder.


### 2026-09-24 cycle completion — internal artifact contract cleanup
- [x] Applied the repository's existing `strip_internal_artifacts.py` semantics to this historical handoff/TODO document: only assistant-internal citation/export markers were removed; surrounding historical notes were retained.
- [x] No gameplay data, research evidence, canonical records, or task history was removed.
- [ ] CI remains unverified; no success claimed.
- [ ] **Exact next:** continue the queued substantive P1 research batch; do not weaken the artifact checker.


### 2026-09-24 cycle completion — Wolf Fang Fist P1 provenance verification
- [x] Verified Wolf Fang Fist as a Super / Strike skill with 100 Ki, Yamcha mentor Lesson 1 acquisition, CaC usability, and documented 15-hit rush / knock-away mechanics.
- [x] Preserved unresolved stamina, frame-data, and universal damage values rather than inferring them.
- [x] Added and registered the dedicated provenance audit; canonical/index boundary remains 469/469.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue the next partially verified research batch where direct Xenoverse 2 evidence can resolve substantive missing fields.


### 2026-09-24 cycle completion — Power Pole P1 provenance verification
- [x] Selected existing partially verified **Power Pole** (research batch 165) as the next substantive target after Wolf Fang Fist.
- [x] Confirmed **Super / Strike**, **100 Ki**, CaC usability, **Skill Shop** acquisition, and long-range weapon mechanics from current Xenoverse 2-specific documentation.
- [x] Confirmed the documented straight-line single-hit behavior and increased damage against grounded/pinned opponents.
- [x] Corrected the research-layer DLC provenance to **GT Pack 1**; older Xenoverse evidence is used only for DLC provenance, not to import its shop price into Xenoverse 2.
- [x] Explicitly preserved unresolved stamina, exact frame/hitbox, universal damage, and Xenoverse 2 Skill Shop price fields rather than importing unsupported values.
- [x] Added `docs/data/skill-power-pole-p1-provenance-verification-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Research-layer record is now `verified`; canonical/index catalogs remain **469/469** and were not manually reconstructed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue with the next existing partially verified research batch after Power Pole where current Xenoverse 2 evidence can resolve substantive missing fields; preserve nulls for unsupported numeric/version-sensitive values and do not promote into canonical catalogs without the supported builder.


### 2026-09-24 cycle completion — Justice Rush P1 provenance verification
- [x] Selected existing partially verified **Justice Rush** (research batch 166) as the next substantive target after Power Pole.
- [x] Reconfirmed **Super / Strike**, **100 Ki**, CaC usability, and Gohan (Adult) & Videl Lesson 1 mentor acquisition from Xenoverse 2-specific evidence.
- [x] Confirmed the documented ten-hit short-range barrage, launching final kick, and Ultimate-cancel opportunity before the final kick.
- [x] Preserved unresolved stamina, exact frame/hitbox, and universal numeric damage fields rather than inferring them.
- [x] Added `docs/data/skill-justice-rush-p1-provenance-verification-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Research-layer record is now `verified`; canonical/index catalogs remain **469/469** and were not manually reconstructed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue with the next existing partially verified research batch after Justice Rush where current Xenoverse 2 evidence can resolve substantive missing fields; preserve nulls for unsupported numeric/version-sensitive values and do not promote into canonical catalogs without the supported builder.


### 2026-09-24 cycle completion — Critical Upper P1 provenance verification
- [x] Selected existing partially verified **Critical Upper** (research batch 167) as the next substantive target after Justice Rush.
- [x] Reconfirmed **Super / Strike**, **100 Ki**, CaC usability, and Dodoria mentor acquisition from current Xenoverse 2-specific evidence.
- [x] Confirmed Lesson 1 as the acquisition point and documented short-range uppercut/launch/follow-up mechanics; later Jiren partner customization availability remains secondary context.
- [x] Preserved unresolved stamina, exact frame/hitbox, and universal damage values. The dedicated source's displayed 10% damage is retained only as source context, not universal canonical numeric data.
- [x] Added `docs/data/skill-critical-upper-p1-provenance-verification-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Research-layer record is now `verified`; canonical/index catalogs remain **469/469** and were not manually reconstructed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue with the next existing partially verified research batch after Critical Upper where current Xenoverse 2 evidence can resolve substantive missing fields; preserve nulls for unsupported numeric/version-sensitive values and do not promote into canonical catalogs without the supported builder.


### 2026-09-24 cycle completion — Rebellion Spear P1 provenance verification
- [x] Verified the existing research-layer record for **Rebellion Spear** (batch 168) against current Xenoverse 2-specific evidence.
- [x] Confirmed **Super / Strike**, **100 Ki**, CaC usability, and **Bardock mentor training — Lesson 1** as the documented acquisition endpoint.
- [x] Added direct mechanics evidence for the controllable rush/chase behavior, yellow Ki trail, and approximately 5-second duration.
- [x] Added and registered the dedicated provenance audit; canonical/index parity remains **469/469**.
- [x] Preserved unresolved stamina, exact frame/hitbox, and universal damage values; no unsupported numeric promotion was made.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] **Exact next:** continue batch **169 — Android Kick**, then batch 170 — Dynamite Kick, using direct Xenoverse 2 evidence and preserving unresolved/version-sensitive fields.


### 2026-09-24 cycle update — Android Kick P1 provenance verification
- [x] Live canonical census before editing: **469** skill records; Android Kick is not currently present in `docs/data/skills-index.json`, so no unsupported canonical promotion was attempted.
- [x] Bounded batch: **skill-research-batches/skill-batch-169.json — Android Kick**.
- [x] Revalidated Xenoverse 2 **Super / Strike**, **100 Ki**, CaC usability, **Skill Shop** acquisition, and Mira/custom-partner ownership context using current Xenoverse 2-specific evidence.
- [x] Strengthened mechanics evidence: high somersault, optional second-input diving kick, and back-input backflip behavior.
- [x] Added `docs/data/skill-android-kick-p1-provenance-verification-2026-09-24.json` and updated batch 169.
- [x] Evidence limits preserved: stamina, exact frame/hitbox data, universal damage, and any separate Ki cost for the second input remain unresolved/version-sensitive.
- [x] Validation: JSON records parse; canonical count remains **469**; no canonical promotion was attempted because the supported builder/runtime remains unavailable.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue **skill-research-batches/skill-batch-170.json — Dynamite Kick**, using the same bounded P1 provenance workflow; then proceed to the next deterministic research batch.


### 2026-09-24 cycle update — Dynamite Kick P1 provenance verification
- [x] Live canonical census: **469** skill records; Dynamite Kick was not promoted because the supported builder/runtime remains unavailable.
- [x] Bounded batch: **skill-research-batches/skill-batch-170.json — Dynamite Kick**.
- [x] Revalidated Xenoverse 2 **Super / Strike**, **100 Ki**, CaC usability, and **Training with Hercule** acquisition using current Xenoverse 2-specific evidence plus independent mentor/training corroboration.
- [x] Strengthened mechanics evidence: short-range chargeable kick, increased follow-up sequence while charging, up to 13 hits, and knockback finish.
- [x] Added `docs/data/skill-dynamite-kick-p1-provenance-verification-2026-09-24.json` and updated batch 170.
- [x] Preserved evidence limits: stamina, exact frame/hitbox data, and stable universal numeric damage remain unresolved/version-sensitive.
- [x] Validation: changed JSON parsed successfully; canonical count remains **469**; no unsupported canonical/index mutation made.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue the next highest-priority deterministic research batch after 170, preferring existing partially verified skill records with direct Xenoverse 2 evidence and cross-database value.


### 2026-09-24 cycle update — Super Dragon Fist P1 provenance verification
- [x] Live canonical census remains **469** skill records; no canonical promotion attempted because the supported builder/runtime remains unavailable.
- [x] Bounded batch: **skill-research-batches/skill-batch-171.json — Super Dragon Fist**.
- [x] Revalidated Xenoverse 2 **Super / Strike**, **100 Ki**, CaC usability, and **Skill Shop** acquisition using current Xenoverse 2-specific evidence and independent corroboration.
- [x] Strengthened mechanics evidence: short-distance approach, rapid three-punch rush on contact, multi-hit/rushdown behavior.
- [x] Explicitly excluded historical Xenoverse 1 PQ42 acquisition from the Xenoverse 2 canonical route.
- [x] Added `docs/data/skill-super-dragon-fist-p1-provenance-verification-2026-09-24.json` and updated batch 171.
- [x] Preserved evidence limits: stamina, exact frame/hitbox values, and stable universal numeric damage remain unresolved/version-sensitive.
- [x] Validation: changed JSON parsed successfully; canonical/index parity remains **469/469**.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue the next deterministic research batch after 171, using the existing batch sequence and the same bounded provenance workflow.


### 2026-09-24 cycle update — Shining Slash P1 provenance refresh
- [x] Live canonical census remains **469** skill records; Shining Slash already existed in the canonical/index layer, so no promotion was required.
- [x] Bounded batch: **skill-research-batches/skill-batch-172.json — Shining Slash**.
- [x] Refreshed **Super / Strike**, **100 Ki**, **Earthling or Saiyan** CaC restriction, and **PQ38 — Power Teams** acquisition against live canonical data and current/independent Xenoverse 2 evidence.
- [x] Preserved the canonical reward semantics: PQ38 Basic Reward and **no Ultimate Finish requirement**; no drop probability inferred.
- [x] Strengthened mechanics evidence for the sword-based charged gap-closing/teleport behavior.
- [x] Added `docs/data/skill-shining-slash-p1-provenance-verification-2026-09-24.json` and updated batch 172.
- [x] Preserved evidence limits: exact frame, hitbox, damage, and drop-probability values remain unresolved/version-sensitive.
- [x] Validation: changed JSON parsed successfully; canonical/index parity remains **469/469**.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue **skill-batch-173.json — Cross Arm Dive** using the same bounded provenance workflow, with live canonical evidence checked first.


### 2026-09-24 cycle update — Cross Arm Dive P1 provenance verification
- [x] Live canonical census remains **469** skill records; no canonical promotion was required.
- [x] Bounded batch: **skill-research-batches/skill-batch-173.json — Cross Arm Dive**.
- [x] Revalidated Xenoverse 2 **Super / Strike**, **100 Ki**, CaC/Future Warrior availability, and **Skill Shop** acquisition using current Xenoverse 2-specific evidence plus independent corroboration.
- [x] Strengthened mechanics evidence: rising-then-falling attack, cross-arm downward chop, and knockdown behavior; independent community evidence corroborates use after knockdown setups.
- [x] Added `docs/data/skill-cross-arm-dive-p1-provenance-verification-2026-09-24.json` and updated batch 173.
- [x] Preserved evidence limits: stamina, exact frame/tracking/hitbox values, and stable universal numeric damage remain unresolved/version-sensitive. Historical Xenoverse shop pricing/progression was not imported.
- [x] Validation: changed JSON parsed successfully; canonical/index parity remains **469/469**.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue the next deterministic research batch after 173 using the existing batch sequence and the same bounded provenance workflow.


### 2026-09-24 cycle update — Spirit Stab P1 provenance verification
- [x] Live canonical census remains **469**; Spirit Stab is absent from the current canonical index, so no unsupported promotion was attempted.
- [x] Bounded batch: **skill-research-batches/skill-batch-174.json — Spirit Stab**.
- [x] Revalidated Xenoverse 2 **Super / Strike**, **100 Ki**, CaC usability, SSGSS Vegito association, **Super Pack 4** provenance, and **TP Medal Shop** acquisition using current Xenoverse 2-specific evidence and independent DLC/update records.
- [x] Strengthened mechanics: long-range Ki-blade thrust, single-hit, re-stand behavior, and documented inability to guard the attack.
- [x] Added `docs/data/skill-spirit-stab-p1-provenance-verification-2026-09-24.json` and updated batch 174.
- [x] Preserved evidence limits: stamina, exact frame/hitbox/damage values, and detailed guard-state edge cases remain unresolved/version-sensitive.
- [x] Validation: changed JSON parsed successfully; canonical/index parity remains **469/469**.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue **skill-batch-175.json — Smile Charge** using the same bounded provenance workflow, with live canonical evidence checked first.


### 2026-09-24 — TODO completion update — Smile Charge P1 provenance verification
- [x] Completed **skill-batch-175 — Smile Charge** with Xenoverse 2 identity, 100-Ki Strike classification, CaC-unavailable boundary, Android 17/Android 17 (DB Super) Partner Customization endpoint, and mechanics provenance.
- [x] Added and registered the Smile Charge provenance audit.
- [x] Preserved the 469/469 canonical/index boundary; no unsupported canonical promotion was made.
- [x] Preserved unresolved stamina, exact frame/hitbox/damage, and Ultimate Finish fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** complete **skill-batch-176 — Mach Punch** using direct Xenoverse 2 evidence and the same bounded provenance workflow.


### 2026-09-24 — TODO validation update — Smile Charge CI result
- [x] Post-change Repository quality run **36092956273** and Clean internal artifacts run **36092956276** both failed immediately; Repository quality exposed the artifact-check job with zero steps.
- [x] No repository-content conclusion was drawn from the zero-step failure; Smile Charge canonical promotion remains blocked by the existing builder/runtime boundary.
- [ ] CI success remains unverified.
- [ ] **Exact next:** batch **176 — Mach Punch**.


### 2026-09-24 — TODO completion update — Mach Punch P1 provenance verification
- [x] Completed **skill-batch-176 — Mach Punch**: identity, 100-Ki Strike classification, PQ19 reward route, Future Warrior availability, partner customization endpoints, and mechanics provenance.
- [x] Added and registered the Mach Punch provenance audit.
- [x] Preserved the 469/469 canonical/index boundary; no unsupported promotion was made.
- [x] Preserved unresolved stamina, exact frame/tracking/hitbox/damage, and Ultimate Finish fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect and complete the next deterministic skill research batch after 176.


### 2026-09-24 — TODO completion update — Final Cannon P1 provenance verification
- [x] Completed **skill-batch-177 — Final Cannon** with identity, 100-Ki Strike classification, PQ52 route, Future Warrior boundary, partner customization endpoints, and mechanics provenance.
- [x] Added and registered the Final Cannon provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved numeric evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** complete **skill-batch-178 — Shadow Crusher**.


### 2026-09-24 — TODO completion update — Shadow Crusher P1 provenance refresh
- [x] Completed **skill-batch-178 — Shadow Crusher** with current Xenoverse 2 identity, Ki Blast-counter mechanics, 100-Ki canonical cost, CaC boundary, and Cooler Lesson 1 acquisition provenance.
- [x] Added and registered the Shadow Crusher provenance audit.
- [x] Preserved the verified 469/469 canonical/index boundary and unresolved numeric evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** complete **skill-batch-179 — Fake Death**.


### 2026-09-24 — TODO completion update — Fake Death
- [x] Completed **skill-batch-179 — Fake Death** and resolved the previously blocked repository write.
- [x] Added and registered the Fake Death provenance audit.
- [x] Preserved verified canonical parity at **469/469** and unresolved evidence limits.
- [ ] CI remains unverified.
- [ ] **Exact next:** complete **skill-batch-180 — Phantom Fist**.

### 2026-09-24 — TODO completion update — Phantom Fist P1 provenance verification
- [x] Completed **skill-batch-180 — Phantom Fist** with Xenoverse 2 identity, Super/Other classification, 100 Ki cost, PQ97 acquisition, and defensive stamina-recovery mechanics.
- [x] Added and registered the Phantom Fist provenance audit.
- [x] Preserved the 469/469 canonical/index boundary; no unsupported canonical promotion was made.
- [x] Preserved unresolved stamina cost, exact timing/repeat behavior, drop probability, and Ultimate Finish fields where evidence was insufficient.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect and complete the next deterministic skill research batch after 180 using the same bounded provenance workflow.

### 2026-09-24 — TODO completion update — Evil Ray Strike P1 provenance verification
- [x] Completed **skill-batch-181 — Evil Ray Strike** with Xenoverse 2 identity, Super/Strike classification, 100 Ki cost, Kid Gohan mentor acquisition, and guard-breaking tracking mechanics.
- [x] Added and registered the Evil Ray Strike provenance audit.
- [x] Preserved the 469/469 canonical/index boundary; no unsupported canonical promotion was made.
- [x] Preserved unresolved stamina, exact frame/tracking/hitbox/damage, and Ultimate Finish fields where evidence was insufficient.
- [ ] CI remains unverified.
- [ ] **Exact next:** complete **skill-batch-182** using the same bounded provenance workflow.

### 2026-09-24 — TODO validation update — post-181 Actions rerun
- [x] Repository quality and Clean internal artifacts both failed immediately with zero exposed workflow steps on the latest Evil Ray Strike commit; this does not identify a repository-content failure.
- [x] Reran both failed jobs; reruns were accepted successfully and remain pending/processing at handoff time.
- [ ] CI success remains unverified.
- [ ] **Exact next:** inspect the rerun results, then complete **skill-batch-182 — Gigantic Slam**.

### 2026-09-24 — TODO completion update — Gigantic Slam P1 provenance verification
- [x] Completed skill-batch-182 — Gigantic Slam with Xenoverse 2 identity, Super/Strike classification, 100 Ki, grab/6-hit mechanics, and unavailable-for-CaC classification.
- [x] Added and registered the Gigantic Slam provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved numeric evidence fields.
- [ ] CI remains unverified.
- [ ] Exact next: inspect current Actions reruns, then complete skill-batch-183.

### 2026-09-24 — TODO completion update — Mach Kick P1 provenance verification
- [x] Completed skill-batch-183 — Mach Kick with Xenoverse 2 identity, Super/Strike classification, 100 Ki, PQ17 acquisition, six-kick mechanics, and Space Mach Attack relationship.
- [x] Added and registered the Mach Kick provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] Exact next: inspect current Actions reruns, then complete skill-batch-184.

### 2026-09-24 — TODO completion update — Punisher Drive P1 provenance verification
- [x] Completed skill-batch-184 — Punisher Drive with Xenoverse 2 identity, Super/Strike classification, Skill Shop acquisition, rapid invisible-rush mechanics, and Soul Punisher separation.
- [x] Added and registered the Punisher Drive provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete skill-batch-185.

### 2026-09-24 — TODO completion update — Dragon Thunder P1 provenance refresh
- [x] Completed/refresh-verified **skill-batch-185 — Dragon Thunder** with cast exclusivity, Super/Strike classification, 100 Ki, Omega Shenron user context, and Xenoverse 2-specific anti-air mechanics.
- [x] Added and registered the Dragon Thunder provenance audit, including the source-conflict note.
- [x] Preserved the 469/469 canonical/index boundary and unresolved numeric evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete **skill-batch-186**.

### 2026-09-24 — TODO completion update — Super Afterimage P1 provenance verification
- [x] Completed **skill-batch-186 — Super Afterimage** with Xenoverse 2 identity, Super/Other classification, 100 Ki, Skill Shop acquisition, movement/afterimage mechanics, and Counter Skill cross-taxonomy.
- [x] Added and registered the Super Afterimage provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete **skill-batch-187**.

### 2026-09-24 — TODO completion update — God Breaker P1 provenance verification
- [x] Completed **skill-batch-187 — God Breaker** with PQ44 acquisition, Super/Strike counter taxonomy, 100 Ki, Ki Blast output, and melee/grab counter mechanics.
- [x] Added and registered the God Breaker provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete **skill-batch-188**.

### 2026-09-24 — TODO completion update — Heroic Counter P1 provenance verification
- [x] Completed **skill-batch-188 — Heroic Counter** with Xenoverse 2 identity, Super/Strike classification, 100 Ki, universal counter behavior, PQ155 acquisition, and HERO OF JUSTICE Pack 1 provenance.
- [x] Added and registered the Heroic Counter provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete **skill-batch-189**.

### 2026-09-24 — TODO completion update — Counter Impact P1 provenance verification
- [x] Completed **skill-batch-189 — Counter Impact** with Xenoverse 2 identity, Ki Blast classification, 100 Ki, PQ153 acquisition, Counter Skill taxonomy, and melee-triggered warp/Ki Wave mechanics.
- [x] Added and registered the Counter Impact provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete **skill-batch-190**.

### 2026-09-24 — TODO completion update — Punisher Shield P1 provenance verification
- [x] Completed **skill-batch-190 — Punisher Shield** with Xenoverse 2 identity, Ki Blast classification, 100 Ki, PQ129 acquisition, Extra Pack 4 provenance, Future Warrior usability, and barrier/counter mechanics.
- [x] Added and registered the Punisher Shield provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then complete **skill-batch-191**.

### 2026-09-24 — TODO completion update — Absolute Zero P1 provenance verification
- [x] Completed **skill-batch-197 — Absolute Zero** with current Xenoverse 2 classification, 300 Stamina, Eis Shenron/GT Pack 2 provenance, PQ96 acquisition, and counter/freeze mechanics evidence.
- [x] Preserved the Basic Reward vs historical random-acquisition discrepancy instead of inventing an Ultimate Finish gate or drop probability.
- [x] Added and registered `docs/data/skill-absolute-zero-p1-provenance-verification-2026-09-24.json`.
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-197.json` and preserved canonical/index parity at **469/469** without unsupported promotion.
- [ ] CI success remains unverified because current Actions failures expose zero workflow steps/logs.
- [ ] **Exact next:** complete **skill-batch-198 — Burst Reflection** using direct Xenoverse 2 evidence and the same bounded provenance workflow.


### 2026-09-24 — TODO validation correction — post-write Actions state
- [x] Re-polled current Actions after the Absolute Zero cycle writes: Repository quality run `36094226481` and Clean internal artifacts run `36094226504` failed with zero exposed workflow steps/logs.
- [x] No canonical data was changed in response to the runner/observability failure; append-only historical documentation was preserved.
- [ ] CI success remains unverified.
- [ ] **Exact next:** complete **skill-batch-198 — Burst Reflection** using direct Xenoverse 2 evidence.

### 2026-09-24 — TODO completion update — Burst Reflection P1 provenance verification
- [x] Completed **skill-batch-198 — Burst Reflection** with current Xenoverse 2 classification, 100 Ki, Shenron-wish acquisition, Future Warrior availability, Nuova Shenron context, and barrier/beam mechanics.
- [x] Added and registered the Burst Reflection provenance audit.
- [x] Preserved the GT Pack 2/older-Xenoverse context distinction and did not import a stale PQ acquisition route.
- [x] Preserved the 469/469 canonical/index boundary and unresolved numeric/matchup evidence.
- [ ] CI remains unverified.
- [ ] **Exact next:** complete **skill-batch-199 — Time Skip/Back Breaker** using direct Xenoverse 2 evidence and the same bounded provenance workflow.

### 2026-09-24 — TODO completion update — Time Skip/Back Breaker P1 provenance verification
- [x] Completed **skill-batch-199 — Time Skip/Back Breaker** with current Xenoverse 2 identity, 100 Ki, Hit Lesson 1 acquisition, Future Warrior availability, and rear-counter mechanics.
- [x] Added and registered the Time Skip/Back Breaker provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved evidence fields.
- [ ] CI remains unverified; latest Pages run is in progress while quality/clean runs fail without useful step output.
- [ ] **Exact next:** complete **skill-batch-200 — Time Skip/Flash Skewer**.

### 2026-09-24 — TODO completion update — Time Skip/Flash Skewer P1 provenance verification
- [x] Completed **skill-batch-200 — Time Skip/Flash Skewer** with current Xenoverse 2 identity, 100 Ki, Hit Initiation Test acquisition, Future Warrior availability, and Strike-counter mechanics.
- [x] Corrected DLC context to **Super Pack 1** and documented the conflicting secondary attribution rather than propagating it.
- [x] Added and registered the Time Skip/Flash Skewer provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved/version-sensitive mechanics.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then determine the next live research batch after 200.

### 2026-09-24 — TODO completion update — Time Skip/Jump Spike P1 provenance verification
- [x] Completed **skill-batch-201 — Time Skip/Jump Spike** with current Xenoverse 2 identity, 100 Ki, Hit Lesson 2 acquisition, Future Warrior availability, Super Pack 1 context, and forward-rush mechanics.
- [x] Added and registered the Time Skip/Jump Spike provenance audit.
- [x] Preserved the 469/469 canonical/index boundary and unresolved numeric/frame evidence.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then determine the next live research batch after 201.


### 2026-09-24 TODO completion update — Ultrasonic Blitz P1 provenance verification
- [x] Live census before editing: canonical/index boundary **469/469**; duplicate-ID baseline remains **0**.
- [x] Completed the next live research target after batch 201: **skill-batch-202 — Ultrasonic Blitz**.
- [x] Revalidated Xenoverse 2 **Super / Strike / Counter Skill** identity, **100 Ki**, Goku (Ultra Instinct -Sign-) association, Conton City Vote Pack context, Future Warrior usability, and **PQ151 — Even Further Beyond** acquisition.
- [x] Revalidated the current Counter Skill taxonomy as **Melee Counter** and preserved the repository's Basic Reward interpretation for PQ151 without inventing a probability or Ultimate Finish gate.
- [x] Added and registered `docs/data/skill-ultrasonic-blitz-p1-provenance-verification-2026-09-24.json` and refreshed `docs/data/skill-research-batches/skill-batch-202.json`.
- [x] Preserved unresolved exact counter frames/hitboxes, current damage, stamina cost, and drop probability; no unsupported canonical promotion was made.
- [x] Web evidence checked: current Xenoverse 2 Ultrasonic Blitz reference, Counter Skill taxonomy, Super Attack taxonomy, DLC reference, plus independent community/video corroboration. 
- [x] Current Actions state was inspected and the failed Repository quality / Clean internal artifacts jobs were rerun; no workflow success is claimed because the exposed jobs still provide no usable step/log evidence.
- [ ] CI success remains unverified.
- [ ] **Exact next:** inspect the post-rerun Actions state, then continue with the next live research target after **Ultrasonic Blitz**, preserving the 469/469 boundary and using the same bounded P1 provenance workflow.


### 2026-09-24 validation correction — Ultrasonic Blitz write set
- [x] Post-write JSON validation initially found two serialization mistakes in the newly edited batch/index files; both were corrected immediately without changing research semantics.
- [x] Revalidated `skill-batch-202.json`, `pq-cross-domain-index.json`, and the new Ultrasonic Blitz audit: all three now parse successfully; provenance artifact scan is clean.
- [x] Current Actions rerun inspection: Repository quality and Clean internal artifacts still complete as failures with no exposed workflow steps/logs. No CI success is claimed.
- [x] Corrected live commit sequence: `dc3c8029`, `4a49a1b9`, `cd31986c`, `5e41fd44`, `85126d70`, `d7c72351`, `59436781`, `6a3863ed`.
- [ ] **Exact next:** continue **skill-batch-203 — Demon Flash Strike** after inspecting current Actions state, using the same bounded P1 provenance workflow and preserving the 469/469 canonical boundary.


### 2026-09-24 TODO completion update — Demon Flash Strike P1 provenance verification
- [x] Live provenance census: **465 canonical / 465 index / 0 duplicate IDs**.
- [x] Completed **skill-batch-203 — Demon Flash Strike** with current Super / Strike / Counter Skill classification, 100 Ki, Gohan (Beast), Hero of Justice Pack 2, and PQ160 provenance.
- [x] Preserved Basic Reward semantics and did not invent an Ultimate Finish gate or drop probability.
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-203.json` to 2026-09-24 and preserved unresolved exact frame/hitbox, stamina, probability, and matchup evidence.
- [ ] CI success remains unverified.
- [ ] **Exact next:** inspect current Actions state, then continue **skill-batch-204** using the bounded P1 provenance workflow.


### 2026-09-24 TODO completion — Counter Impact taxonomy reconciliation
- [x] Completed **skill-batch-204**.
- [x] Counter Impact taxonomy correction verified: **Super / Ki Blast / Counter Skill**, subtype unresolved/null.
- [x] Refreshed verification to **2026-09-24** and registered batch 204 in the cross-domain index.
- [ ] **Next:** inspect and process **skill-batch-205**.


### 2026-09-24 TODO completion — Punisher Shield
- [x] Completed **skill-batch-205** and verified Punisher Shield's existing conservative acquisition fields.
- [x] Refreshed verification to **2026-09-24** and registered the batch in the cross-domain index.
- [x] No unsupported Ultimate Finish condition was inferred.
- [ ] **Next:** process **skill-batch-206 — Shadow Crusher**.


### 2026-09-24 TODO completion — Shadow Crusher
- [x] Completed **skill-batch-206** and verified the existing acquisition/taxonomy fields.
- [x] Refreshed verification to **2026-09-24** and registered the audit in the cross-domain index.
- [x] Preserved null Ultimate Finish handling for the non-PQ mentor route.
- [ ] **Next:** process **skill-batch-207 — Reverse Mabakusenko**.


### 2026-09-24 TODO completion — Reverse Mabakusenko
- [x] Completed **skill-batch-207** and verified the existing classification/acquisition fields.
- [x] Refreshed verification to **2026-09-24** and registered the audit in the cross-domain index.
- [x] Preserved null Ultimate Finish handling for the Skill Shop route.
- [ ] **Next:** process **skill-batch-208 — Super Afterimage and God Breaker**.


### 2026-09-24 — TODO completion update — Batch 209 historical reconciliation correction
- [x] Corrected Batch 140's invalid Flash Fist Crush duplicate reference: Batch 127 is Deadly Dance, not Flash Fist Crush.
- [x] Refreshed Batch 209 to 2026-09-24 and registered both the Batch 209 reconciliation and Batch 140 correction in the cross-domain index.
- [x] Preserved current Flash Fist Crush as Super / Strike / Universal Counter with 100 Ki and Shenron-wish acquisition; no duplicate canonical identity was created.
- [x] Revalidated Dragon Thunder and Shadow Crusher without changing their established findings.
- [x] Validation baseline: **469/469** canonical/index, **0 duplicate IDs**; no canonical catalog reconstruction.
- [ ] CI remains unverified because the latest quality/clean runs expose no workflow steps or usable logs.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-210** with direct Xenoverse 2 evidence and the same bounded provenance/correction workflow.


### 2026-09-24 — TODO reconciliation update — Batch 208 finalized
- [x] Refreshed **skill-batch-208 — Super Afterimage and God Breaker reconciliation** to 2026-09-24 using the existing dedicated P1 audits; no duplicate canonical research was created.
- [x] Preserved Super Afterimage's Counter Skills cross-membership without inventing a dedicated subtype and God Breaker's Melee Counter classification/acquisition.
- [x] Validation baseline remains **469/469** canonical/index with **0 duplicate IDs**.
- [x] Commit: `767d1fb9747ab8c3746a4bcf51be3c9fb06fed5c`.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-210**.


### 2026-09-24 — TODO completion update — Batches 210–213 audit-chain refresh
- [x] Finalized **skill-batch-210** historical Flash Fist Crush correction and refreshed its verification metadata.
- [x] Refreshed **skill-batch-211** post-correction audit for Counter Impact, Burst Reflection, and Change The Future.
- [x] Refreshed **skill-batch-212** acquisition/taxonomy audit for Absolute Zero, Dragon Burn, Dimensional Hole, and Counter Burst.
- [x] Refreshed **skill-batch-213** counter-taxonomy audit for Counter Burst, Ultrasonic Blitz, and Demon Flash Strike.
- [x] Validation baseline remains **469/469** canonical/index with **0 duplicate IDs**; no speculative records were created.
- [ ] CI remains unverified because the Actions jobs continue to fail without exposed workflow steps/logs.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-214**.


### 2026-09-24 — TODO completion update — Batch 214 counter-taxonomy refresh
- [x] Refreshed **skill-batch-214** for Burst Rush, Super God Shock Flash, and Heroic Counter.
- [x] Preserved their current counter subtypes and acquisition/Ultimate-Finish semantics without changing canonical identities.
- [x] Validation remains **469/469** canonical/index with **0 duplicate IDs**.
- [x] Commit: `b36c5f284635bb893a13388d6b4b260323804d15`.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-215**.


### 2026-09-24 — TODO completion update — Batches 215–217
- [x] Refreshed **skill-batch-215** counter-taxonomy reconciliation for Pressure Sign, Rough Ranger, Sudden Death Beam, Phantom Fist, Super Afterimage, and Heroic Assault.
- [x] Completed the Heroic Assault follow-up through **skill-batch-216** with current Xenoverse 2 identity, acquisition, DLC/source, mechanics, and availability evidence.
- [x] Refreshed **skill-batch-217** and preserved the 25-item published Counter Skills category while tracking Heroic Assault's taxonomy/category discrepancy separately.
- [x] Validation remains **469/469** canonical/index with **0 duplicate IDs**.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-218**.


### 2026-09-24 — TODO completion update — Batch 218
- [x] Refreshed **skill-batch-218** Fighting Pose K audit with current Xenoverse 2 acquisition and mechanics evidence.
- [x] Preserved current Skill Shop acquisition and avoided substituting historical PQ39/cross-game references.
- [x] Validation remains **469/469** canonical/index with **0 duplicate IDs**.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-219**.


### 2026-09-24 — TODO completion update — Batches 219–220
- [x] Refreshed **skill-batch-219** nine Fighting Pose records and **skill-batch-220** remaining Power Up Super records.
- [x] Preserved evidence-bounded acquisition and Ultimate Finish fields; no historical cross-game source was promoted over current Xenoverse 2 evidence.
- [x] Validation remains **469/469** canonical/index with **0 duplicate IDs**.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-221**.


### 2026-09-24 — TODO completion update — Batches 221–227
- [x] Refreshed Batches **221–227** and completed the Strike Evasive research/reconciliation chain.
- [x] Preserved all documented source conflicts, character-only restrictions, acquisition uncertainty, and canonical-promotion boundaries.
- [x] Validation remains **469/469** canonical/index with **0 duplicate IDs**.
- [ ] CI remains unverified.
- [ ] **Exact next:** begin the Ki Blast Evasive queue from Batch 227, starting with **Special Beam Blast**.


### 2026-09-24 — TODO completion update — Ki Blast Evasive Batches 228–234
- [x] Completed the bounded Ki Blast Evasive intake/reconciliation through **Batch 234**.
- [x] Corrected Special Beam Blast and Dimension Cannon availability; preserved current-source conflicts for Maiden Burst and Victory Cannon.
- [x] Reconciled cast-exclusive/DLC implementations without speculative CaC promotion.
- [x] Validation remains **469/469** canonical/index with **0 duplicate IDs**.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect current Actions state, then process **skill-batch-235** and its Mach Dash/Final Pose category-source reconciliation.


### 2026-09-24 — TODO completion update — Evasive Batches 235–237
- [x] Completed the Power Up transition audit and Other Evasive intake through **Batch 237**.
- [x] Preserved the Final Pose/Mach Dash CaC wording conflict and the Evasive/Super and cast-only distinctions across the Other Evasives.
- [x] Live validation remains **469/469 canonical/index**, **0 duplicate IDs**.
- [ ] CI success remains unverified; latest Pages deployment is in progress.
- [ ] **Exact next:** process **skill-batch-238**.

### 2026-09-24 cycle completion — Batch 238 Evasive CaC-access reconciliation refresh
- [x] Live baseline confirmed at **469 canonical / 469 index / 0 duplicate IDs**; no new canonical skill identity was created.
- [x] Refreshed **skill-batch-238** for **Final Pose**, **Mach Dash**, and **Punisher Guard** using current Xenoverse 2 Evasive references.
- [x] Confirmed Final Pose and Mach Dash as **Power Up Evasives**, 200 Stamina, with Skill Shop and PQ18 acquisition endpoints respectively; the current Evasive reference explicitly places both in its CaC-accessible Power Up table. 
- [x] Confirmed Punisher Guard as an **Other Evasive**, 300 Stamina, Skill Shop after story completion, and CaC-accessible in the current Evasive reference; the current Other Evasives category contains it as well. 
- [x] Preserved the source-count discrepancy instead of forcing category/table counts into one partition: the Other Evasives category has 11 entries, while the current Evasive reference lists 8 CaC-accessible Other Evasives and separately lists cast-exclusive Evasives. 
- [x] Added `docs/data/skill-evasive-cac-access-reconciliation-2026-09-24.json` as the current dated evidence audit and refreshed `skill-batch-238.json`.
- [x] Validation: changed JSON payloads are structurally generated from parsed source data; canonical/index boundary remains **469/469** with no duplicate-ID change.
- [ ] CI success remains unverified; no CI success claimed.
- [ ] **Exact next:** continue the next live unfinished Evasive/research batch after the current 238 refresh, beginning with **skill-batch-239** only if its historical correction remains unreconciled in the live canonical layer; otherwise choose the next deterministic unfinished consumer from the handoff/TODO queue.

### 2026-09-24 cycle completion — Ki Blast Super historical reconciliation Batches 247–248
- [x] Live canonical/index boundary remains **469/469** with **0 duplicate IDs**; no canonical reconstruction or duplicate promotion was performed.
- [x] Reconciled historical **Batches 247–248** against the later live provenance/audit chain rather than treating their 2026-09-17 placeholders as current truth.
- [x] Batch 247: Photon Swipe and Gamma Blaster are already represented in the later canonical layer; later reward-condition audits supersede the original batch's UF placeholders while the historical batch remains preserved.
- [x] Batch 248: later provenance work supersedes historical nulls for records including Divine Spear, Burning Blast, and Force Edge; Steel Mirage's reward-source conflict remains explicitly preserved rather than guessed.
- [x] Added `docs/data/skill-kiblast-super-batches-247-248-reconciliation-2026-09-24.json` and refreshed the two historical batch verification/status records.
- [x] Validation: all changed JSON parsed successfully; no canonical/index reconstruction was attempted.
- [ ] CI success remains unverified; the current Actions API exposes no workflow run for the previous documentation commit.
- [ ] **Exact next:** continue **skill-batch-249**, using the same historical-batch reconciliation approach and only promote/change canonical fields when current evidence is stronger than the historical batch.

### 2026-09-24 cycle completion — Batch 249 Ki Blast Super current reconciliation
- [x] Reconciled all seven Batch 249 candidates against the live PQ/provenance layers instead of carrying forward the original 2026-09-17 acquisition endpoints unchanged.
- [x] Corrected the research-layer PQ endpoints: Gigantic Cluster and Eraser Bomb → **PQ163**; Variable Snipe Shot → **PQ165**; Burning Swan → **PQ167**; Emperor's Cannon → **PQ183** with the existing PQ183-vs-PQ184 conflict preserved.
- [x] Added Gigantic Cross's deterministic **Conton City Patrol 04** endpoint without collapsing it into the historical PQ142 provenance.
- [x] Corrected **Swallow Shot** from CaC-usable/PQ159 to **cast-exclusive Videl (DB Super)** with no player acquisition endpoint; current Super Attack and Videl references support the cast-exclusive classification. 
- [x] Added `docs/data/skill-batch-249-reconciliation-2026-09-24.json`.
- [x] Preserved the **469/469** canonical/index boundary and **0 duplicate IDs**; Swallow Shot is deliberately not manually inserted into generated canonical files because the supported lossless builder path is unavailable.
- [x] JSON validation completed successfully; CI remains unverified.
- [ ] **Exact next:** continue **skill-batch-250**, reconciling its historical Ki Blast Super records against the current canonical/provenance/PQ layers and preserving cast-exclusive/raid-only boundaries.

### 2026-09-24 cycle completion — Batch 250 Ki Blast Super historical reconciliation
- [x] Reconciled all seven Batch 250 records against the current PQ relationship, unavailable-for-CaC, and later catalog/provenance layers.
- [x] Confirmed **Blades of Judgement** and **Lightning of Absolution** through PQ112/PQ111 reward evidence; confirmed **Holy Wrath** through PQ111 while preserving the later Basic-Reward semantics over the historical UF assertion.
- [x] Preserved **Light of Justice**, **Seasoning Arrow**, and **Time Shackles** as unavailable-for-CaC/cast-exclusive boundaries without inventing acquisition routes.
- [x] Preserved **Marbling Drop**'s EM15/raid acquisition uncertainty; later catalog evidence supports EM15/Raid availability, but the repository's Expert Mission documentation still marks the acquisition claim as pending reconciliation. No drop rate or guarantee was inferred.
- [x] Added `docs/data/skill-batch-250-reconciliation-2026-09-24.json` and refreshed the historical batch verification/status metadata.
- [x] Validation: JSON parsed successfully; canonical/index boundary remains **469/469** with **0 duplicate IDs** and no speculative canonical promotion.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue **skill-batch-251**, reconciling Saturday Crash, Consecutive Energy Blast, Super Destructo-Disc, and Earth Splitting Galick Gun against current canonical/PQ/provenance evidence.

### 2026-09-24 cycle completion — Batch 251 Ki Blast Super historical reconciliation
- [x] Reconciled all four Batch 251 records against current mentor/PQ/provenance evidence.
- [x] Verified **Saturday Crash** through the live Raditz mentor endpoint and retained its previously verified 100 Ki cost.
- [x] Preserved **Consecutive Energy Blast**'s Skill Shop acquisition without inventing a shop rotation, price, or probability.
- [x] Confirmed **Super Destructo-Disc** had already been promoted to the canonical/index layer; no duplicate promotion was performed, and its unresolved Expert Mission drop-rate/guarantee semantics remain explicit.
- [x] Confirmed **Earth Splitting Galick Gun → PQ11** through the canonical PQ reward relationship/reverse index while preserving the existing Ultimate-Finish evidence conflict instead of guessing a definitive gate.
- [x] Added `docs/data/skill-batch-251-reconciliation-2026-09-24.json` and refreshed the historical batch verification/status metadata.
- [x] Validation: JSON parsed successfully; canonical/index boundary remains **469/469** with **0 duplicate IDs**.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue **skill-batch-252**, reconciling Death Slicer, Ki Blast Cannon, Dodon Ray, Death Slash, Burst Attack, and Kairos Cannon.
### 2026-09-24 — TODO completion update — Batch 252 Ki Blast Super reconciliation
- [x] Completed **skill-batch-252** for Death Slicer, Ki Blast Cannon, Dodon Ray, Death Slash, Burst Attack, and Kairos Cannon.
- [x] Reconciled current class, subtype, cost, acquisition, and availability evidence; preserved unresolved fields rather than inferring them.
- [x] Corrected Kairos Cannon from character-only to **Future Warrior/CaC-accessible** through **Conton City Tournament Match 2 — "Thinning the Herd"**.
- [x] Added and registered `docs/data/skill-batch-252-reconciliation-2026-09-24.json`.
- [x] Validation remains **469/469 canonical/index**, **0 duplicate IDs**, with no canonical reconstruction.
- [ ] CI remains unverified.
- [ ] **Exact next:** recompute the live unfinished research/catalog census after Batch 252 and select the next deterministic evidence-backed consumer; no unsupported Batch 253 identity should be invented.
### 2026-09-24 — TODO completion update — Frieza Race Skills + Lovely Showtime
- [x] Closed the Frieza Race Skills count discrepancy: current source and repository catalog both contain exactly **Darkness Rush (Melee)** and **Turn Golden**.
- [x] Added the dated Frieza Race reconciliation audit and preserved skill-level verification as a separate task from category membership.
- [x] Reconciled Lovely Showtime's Ki-cost conflict: dedicated skill page = **200 Ki**; aggregate Ultimate Attack table = **300 Ki**. Retained 200 provisionally and documented the source conflict for future direct game-data verification.
- [x] Added the dated Lovely Showtime cost audit.
- [x] Validation remains **469/469 canonical/index**, **0 duplicate IDs**; no canonical reconstruction.
- [ ] CI remains unverified.
- [ ] **Exact next:** select the next deterministic open high-value enrichment/reconciliation target; do not invent Batch 253.
### 2026-09-24 — TODO completion update — PQ86-PQ100 P1 skill enrichment
- [x] Enriched Batch 54: Neo Wolf Fang Fist, Maiden Burst, Absolute Zero, and Dimension Ray with current Xenoverse 2-specific evidence.
- [x] Corrected Absolute Zero to **Ki Blast Evasive / 300 Stamina** and preserved the source-backed counter/freeze behavior.
- [x] Preserved unresolved Drain Field resource/reward-slot semantics rather than guessing.
- [x] Added `docs/data/skill-batch-54-enrichment-audit-2026-09-24.json`.
- [x] Validation remains **469/469 canonical/index**, **0 duplicate IDs**; no canonical reconstruction.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the next partially verified Batch 54 target with direct current evidence.
### 2026-09-24 — TODO completion update — Drain Field reconciliation
- [x] Reconciled Drain Field's PQ95 acquisition and Other/Super identity using current repository reward data and independent community evidence.
- [x] Preserved the zero-cost claim as attributed community evidence rather than unsupported game-data fact; exact drop probability remains unresolved.
- [x] Added `docs/data/drain-field-reconciliation-2026-09-24.json`.
- [x] Validation remains **469/469 canonical/index**, **0 duplicate IDs**; no canonical reconstruction.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the next partially verified Batch 54 target.
### 2026-09-24 — TODO completion update — Batch 54 second enrichment follow-up
- [x] Enriched Charged Ki Wave, Phantom Fist, Bluff Kamehameha, Emperor's Edge, and X100 Big Bang Kamehameha with current source evidence.
- [x] Preserved Emperor's Edge subtype uncertainty after correcting an interim over-specific assertion.
- [x] Added `docs/data/skill-batch-54-enrichment-followup-2026-09-24.json`.
- [x] Validation remains **469/469 canonical/index**, **0 duplicate IDs**; no canonical reconstruction.
- [ ] CI remains unverified.
- [ ] **Exact next:** recompute the live unfinished census and continue the next deterministic enrichment/reconciliation target.


### 2026-09-24 — TODO completion update — Boulder Toss + Boulder Break Expert Mission provenance follow-up
- [x] Added an independent current Xenoverse 2 Expert Mission 3 source to both Boulder Toss and Boulder Break evidence audits.
- [x] Updated the central unresolved-gap ledger with the additional mission-use provenance while retaining the unresolved numeric Ki-cost boundary.
- [x] Preserved the **469/469** canonical/index boundary and did not promote either cast-only skill without the supported builder/runtime.
- [ ] CI remains unverified; the current main commit exposes no workflow runs/status checks through the available GitHub interface.
- [ ] **Exact next:** continue the remaining unresolved skill-gap queue with **Acid** using direct Xenoverse 2 evidence, then proceed through the remaining unresolved records without inventing numeric costs.


### 2026-09-24 — TODO completion update — Acid evidence follow-up
- [x] Added independent Xenoverse 2 evidence for Acid's Super classification and CaC-unavailable boundary.
- [x] Preserved normal Acid ID 140 versus raid-boss Acid ID 143 as separate identities.
- [x] Kept numeric Ki cost unresolved and made no unsupported canonical promotion.
- [x] Canonical/index boundary remains **469/469**.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining unresolved skill-gap queue, beginning with **Boiling Burg / Energy Boil / Baked Sphere** using direct Xenoverse 2 evidence.


### 2026-09-24 — TODO completion update — Boiling Burg evidence follow-up
- [x] Strengthened Boiling Burg with independent Xenoverse 2 ID, ownership, Ultimate, and CaC-unavailable evidence.
- [x] Preserved long ID 5540 versus short ID 540 identity mapping.
- [x] Reduced the tracked gap to numeric Ki cost only.
- [x] Preserved the **469/469** canonical boundary.
- [ ] CI remains unverified.
- [ ] **Exact next:** research **Energy Boil** subtype and Ki cost with direct Xenoverse 2 evidence.


### 2026-09-24 — TODO completion update — Energy Boil evidence follow-up
- [x] Strengthened Energy Boil with independent Xenoverse 2 ID, encounter, Evasive, ownership, and CaC-unavailable evidence.
- [x] Preserved unresolved subcategory and numeric Ki cost rather than guessing.
- [x] Preserved the **469/469** canonical boundary.
- [ ] CI remains unverified.
- [ ] **Exact next:** research **Baked Sphere** and continue the cast-only unresolved queue.


### 2026-09-24 — TODO completion update — Baked Sphere evidence follow-up
- [x] Strengthened Baked Sphere with independent Xenoverse 2 identity and CaC-unavailable evidence.
- [x] Preserved the Explosive Wave research subcategory and unresolved numeric Ki cost.
- [x] Preserved the **469/469** canonical boundary.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining unresolved cast-only skill queue.

### 2026-09-24 cycle completion — Remaining thin-skill datamined cost-boundary census
- [x] Recomputed the remaining unresolved thin-skill set from the live `docs/data/skill-research-gaps.json`: Acid, Howl, Boiling Burg, Energy Boil, Baked Sphere, Boulder Toss, Boulder Break, Boiling Ball, and Tricky Strike.
- [x] Checked the current final-update `Madreag/xenoverse_2_wiki` skill pages derived from the 2026-06-06 Steam depot for all nine records.
- [x] Confirmed that every checked upstream datamined page exposes a **null Ki cost**; no numeric cost was inferred or promoted from class, animation, NPC behavior, or historical/cross-game material.
- [x] Added `docs/data/skill-research-gaps-datamined-cost-boundary-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Updated the central gap ledger to preserve this evidence boundary and distinguish “published datamined corpus does not expose a cost” from the stronger unsupported claim that the game itself has no cost.
- [x] Preserved the **469/469** canonical/index boundary and made no unsupported canonical promotion.
- [x] Inspected the newest Repository quality run `36096707167` on commit `c1870010ab3118650dbc33c30216bb030f1b0f10`: the job `Check for internal artifacts` failed after about two seconds with **zero workflow steps** and no runner ID/log payload. CI success remains unverified.
- [ ] **Exact next:** continue the remaining thin-skill queue by seeking an independent Xenoverse 2-specific numeric Ki-cost source for the highest-impact unresolved record; do not promote any cost until directly supported, and do not invent a new research batch identity.

### 2026-09-24 continuation — Howl recurring Xenoverse 2 provenance refresh
- [x] Continued the unresolved thin-skill queue with **Howl** using independent current Xenoverse 2 encounter evidence.
- [x] Added/updated `docs/data/skill-research-gaps-howl-evidence-audit-2026-09-24.json` with Great Ape Festival, The Return of the Giant Ape-Fest!, Saiyan Survivors, Expert Mission 3, and Legend Patrol/story provenance.
- [x] Reconfirmed **ID 10440 / short ID 440**, **CaC-unavailable**, **Great Ape** source, and **Evasive** classification; Legend Patrol explicitly labels Howl as an Evasive Skill.
- [x] Updated and registered the evidence in `docs/data/skill-research-gaps.json` and `docs/data/pq-cross-domain-index.json`.
- [x] Preserved numeric **Ki cost as unresolved** and made no canonical promotion or invented acquisition route.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the next remaining thin-skill record after Howl, prioritizing **Boiling Ball / Tricky Strike** and seeking direct Xenoverse 2-specific evidence for any still-unresolved fields.

### 2026-09-24 continuation — Boiling Ball + Tricky Strike evidence refresh
- [x] Continued the documented thin-skill queue with **Boiling Ball** and **Tricky Strike**.
- [x] Refreshed both dedicated audits using current indexed Xenoverse 2 evidence: Character ID List, maintained CaC-unobtainable list, and Demigra reference material.
- [x] Reconfirmed **Boiling Ball ID 541 / BBL** and **Tricky Strike ID 542 / TRK**, both CaC-unavailable Final Form Demigra skills.
- [x] Reconfirmed repository research taxonomy: **Boiling Ball = Ki Blast**, **Tricky Strike = Strike**.
- [x] Added the refreshed evidence to `docs/data/skill-research-gaps.json` and registered both audits in `docs/data/pq-cross-domain-index.json`.
- [x] No numeric Ki cost was exposed by the checked sources; both costs remain unresolved and no unsupported canonical promotion was made.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue the remaining unresolved thin-skill queue, prioritizing **Acid**/other records only where a new direct Xenoverse 2 source can resolve a currently missing field; otherwise advance to the next deterministic partially verified PQ/skill enrichment target rather than repeating evidence with no new field coverage.

### 2026-09-24 continuation — Batch 296 Time Control cost resolution
- [x] Advanced the deterministic partially verified skill queue after the thin cast-only pass by auditing **skill-batch-296**.
- [x] Resolved **Time Control**'s previously null numeric Ki cost to **100 Ki** using dedicated Xenoverse 2 skill documentation, which also confirms its Other/Super classification and stun/barrier behavior. citeturn2search0
- [x] Updated `docs/data/skill-research-batches/skill-batch-296.json` and registered the batch in `docs/data/pq-cross-domain-index.json`.
- [x] No cross-game cost inference was used; remaining Batch 296 null costs remain unresolved.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue Batch 296's remaining unresolved records (**Giga Boost, Holstein Shock, Emperor's Sign, Position Shift**) seeking direct Xenoverse 2 numeric-cost evidence, then proceed through the next deterministic partially verified batch.

### 2026-09-24 continuation — Batch 296 provenance refresh
- [x] Continued **skill-batch-296** across Giga Boost, Holstein Shock, Emperor's Sign, and Position Shift.
- [x] Added independent current Xenoverse 2 corroboration for their identities and acquisition/usage boundaries: Giga Boost (Dodoria/Skill Shop), Holstein Shock (Ginyu/PQ15), Emperor's Sign (Frieza/TP Medal Shop), and Position Shift (Towa/Skill Shop after Kid Buu).
- [x] Numeric Ki costs remain unresolved because the retrieved current sources did not expose those values; no costs were inferred from older Xenoverse, gameplay discussion, or mechanics.
- [x] Updated and registered the batch refresh.
- [ ] CI remains unverified.
- [ ] **Exact next:** continue to the next deterministic partially verified skill research batch after 296 and resolve genuinely missing fields with direct Xenoverse 2 evidence.


### 2026-09-24 — TODO completion update — Batch 296 cost evidence boundary
- [x] Rechecked the remaining Batch 296 null Ki-cost fields for **Giga Boost, Holstein Shock, Emperor's Sign, and Position Shift** against current Xenoverse 2-specific references.
- [x] Confirmed their existing Super/Other classifications and acquisition endpoints remain supported: Giga Boost → Conton City Skill Shop; Holstein Shock → PQ15; Emperor's Sign → TP Medal Shop; Position Shift → Skill Shop after defeating Kid Buu.
- [x] Added `docs/data/skill-batch-296-cost-evidence-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved all four numeric Ki costs as unresolved because the checked current references expose no reliable numeric value; no cross-game or analogous-skill inference was used.
- [x] Updated `docs/data/skill-research-batches/skill-batch-296.json` with the evidence boundary.
- [ ] CI success remains unverified; no successful Actions result is claimed.
- [ ] **Exact next:** move to the next deterministic partially verified skill-research batch after 296 and resolve only fields for which direct Xenoverse 2 evidence adds new coverage; do not invent a new batch identity.

### 2026-09-24 — TODO completion update — Batch 301 verification
- [x] Verified Batch 301 cast-exclusive/raid Ultimate records against current Xenoverse 2 Ultimate Attack documentation.
- [x] Confirmed 300-Ki status for Final Galick Rush and Super Dragon Flight (Ultimate); preserved Explosive Scream as unobtainable for CaCs.
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-301.json` with the evidence boundary.
- [x] No unsupported acquisition or canonical promotion was introduced.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue with Batch 302 and resolve only directly supported missing fields.

### 2026-09-24 — TODO completion update — Batch 302 verification
- [x] Verified Batch 302 Energy Cannon and Darkness Mixer against current Xenoverse 2-specific evidence.
- [x] Confirmed Darkness Mixer remains an Other Super, Crystal Raid-capable, and normally unavailable to CaCs; numeric Ki cost remains unresolved.
- [x] Preserved Energy Cannon as a Ki Blast Super for Demon God Demigra; no unsupported cost or acquisition endpoint was added.
- [x] Refreshed skill-batch-302.json with the evidence boundary.
- [x] No unsupported canonical promotion was introduced.
- [ ] CI success remains unverified.
- [ ] Exact next: continue with Batch 303 and resolve only directly supported missing fields.

### 2026-09-24 cycle completion — Batch 302 cost-evidence reconciliation
- [x] Live census before editing: **469 canonical/index records**, **0 duplicate IDs**, and **9 unresolved research-gap records**.
- [x] Bounded batch: **skill-batch-302 — Energy Cannon and Darkness Mixer**.
- [x] Research/evidence: current Xenoverse 2 documentation confirms Darkness Mixer as an **Other Super**, normally unavailable to CaCs; current gameplay documentation states it does not cost anything to use. Energy Cannon remains a **Super / Ki Blast**, CaC-unavailable Demigra skill, but the checked current Xenoverse 2-specific sources expose no reliable numeric in-combat Ki cost.
- [x] Changes: added `docs/data/skill-batch-302-cost-evidence-audit-2026-09-24.json`; updated `docs/data/skill-research-batches/skill-batch-302.json` to record **Darkness Mixer = 0 Ki** in the research layer and preserve Energy Cannon as null; registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence limits preserved: no shop-price-to-Ki inference, no cross-game Energy Cannon/Kiai inference, and no stamina/frame/charge-rate values were invented.
- [x] Validation: changed JSON files were parsed successfully; canonical/index boundary remains **469/469** with **0 duplicate IDs**; no canonical reconstruction or unsupported promotion was performed.
- [ ] CI success remains unverified; no successful Actions result is claimed.
- [x] Commits: audit `797552a796628bfa03c6bee48d4739377bfd7c78`; Batch 302 `cbe3a0f74e728c753ab4adf6f6928822cc4fa7fc`; cross-domain index `83fe67845639662549b40f06429c59a14922c6f7`.
- [x] Live census after editing: **469 canonical/index records**, **0 duplicate IDs**, **9 unresolved research-gap records**.
- [ ] **Exact next:** inspect the current Actions state, then continue **skill-batch-303 — Audacious Laugh** and resolve only fields with direct current Xenoverse 2 evidence; preserve existing acquisition/classification boundaries and do not invent a new batch identity.

### 2026-09-24 cycle completion — Batch 303 Audacious Laugh evidence resolution
- [x] Continued the exact next task from the prior handoff: **skill-batch-303 — Audacious Laugh**.
- [x] Current evidence confirms: **Super / Other**, **100 Ki**, **CaC/Future Warrior usable**, Zarbon as character source, and acquisition through **Zarbon's Initiation Test**.
- [x] Effect refined to a non-damaging taunt that slows the locked-on opponent's movement.
- [x] Existing `dlc_requirement: null` and `ultimate_finish_required: false` were retained; no unsupported dependency was introduced.
- [x] Added `docs/data/skill-batch-303-audacious-laugh-evidence-audit-2026-09-24.json`.
- [x] Updated `docs/data/skill-research-batches/skill-batch-303.json`.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Next: continue the remaining research/cross-domain priorities after rechecking the live TODO and handoff; do not create duplicate batch identities.

### 2026-09-24 cycle completion — Batch 305 Other Ultimate provenance refresh
- [x] Advanced to the next deterministic batch after Batch 303: **skill-batch-305 — Body Change, Energy Zone, The Saviour Has Come**.
- [x] Revalidated all three as **Other Ultimates with 300 Ki** using current Xenoverse 2-specific documentation.
- [x] Strengthened acquisition endpoints: Body Change → **Captain Ginyu Lesson 3**; Energy Zone → **Skill Shop after defeating Mira (Final Form)**; The Saviour Has Come → **Mr. Satan Lesson 3**.
- [x] Preserved `ultimate_finish_required: false`; no drop-rate or Ultimate-Finish semantics were invented.
- [x] Added `docs/data/skill-batch-305-other-ultimate-provenance-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Updated `docs/data/skill-research-batches/skill-batch-305.json`.
- [x] External evidence checked: current Xenoverse 2 Ultimate documentation plus independent Dragon Ball and instructor-guide sources. citeturn0search1turn0search2turn0search3turn0search5turn0search6turn0search8
- [ ] CI success remains unverified; no successful Actions result is claimed.
- [ ] **Exact next:** inspect the live unfinished census and continue the next deterministic partially verified batch after Batch 305, prioritizing missing acquisition/mechanics fields with direct Xenoverse 2 evidence and preserving unresolved values where evidence is insufficient.

### 2026-09-24 cycle completion — Batch 306 Ki Blast Ultimate evidence enrichment
- [x] Continued the next deterministic tranche: **skill-batch-306 — Gigantic Meteor, Gigantic Explosion, Super Electric Strike, Minus Energy Power Ball**.
- [x] Strengthened **Super Electric Strike** with direct current Xenoverse 2 evidence: **300 Ki**, Ki Blast Ultimate, 17-hit long-range tracking wave, and **Expert Mission 11 Basic Reward** acquisition.
- [x] Strengthened **Minus Energy Power Ball** with direct current Xenoverse 2 evidence: **500 Ki**, 39-hit Ki Blast Ultimate properties, and Guru-expanded Shenron wish acquisition.
- [x] Preserved the existing Gigantic Meteor and Gigantic Explosion evidence boundaries; no unsupported damage/frame/drop data was added.
- [x] Updated `docs/data/skill-research-batches/skill-batch-306.json` and promoted the Super Electric Strike record in `docs/data/skills-index.json`.
- [x] Web evidence: dedicated Xenoverse 2 documentation confirms Super Electric Strike's 300 Ki/17-hit properties and Minus Energy Power Ball's 500 Ki/39-hit properties; the maintained Expert Mission guide identifies Super Electric Strike as EM11's Basic Reward. citeturn2search0turn2search6turn3search4turn3search5
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue the next deterministic partially verified tranche after Batch 306, prioritizing records whose acquisition/mechanics fields can gain new direct Xenoverse 2 evidence; do not infer unsupported numeric values.

### 2026-09-24 cycle completion — Batch 307 Ki Blast Ultimate mechanics/provenance enrichment
- [x] Continued **skill-batch-307** across Serious Bomb, Warp Kamehameha, Sphere of Destruction, and Ice Cannon.
- [x] Added/recovered canonical coverage for **Serious Bomb**: Ultimate / Ki Blast, **500 Ki**, TP Medal Shop, CaC availability, and current 19-hit pseudo-strike/projectile behavior.
- [x] Enriched **Warp Kamehameha** with current **400 Ki / 24-hit** teleporting Kamehameha mechanics.
- [x] Enriched **Sphere of Destruction** with current **300 Ki / 13-hit / 35% damage** projectile evidence.
- [x] Enriched **Ice Cannon** with current **300 Ki / 5-hit / 3-second freeze** evidence and preserved its Shenron-wish endpoint.
- [x] Updated `docs/data/skill-research-batches/skill-batch-307.json` and `docs/data/skills-index.json`.
- [x] Validation: live canonical/index census is now **470 records with 0 duplicate IDs**.
- [x] Web evidence: dedicated Xenoverse 2 references directly expose the relevant costs, classifications, acquisition endpoints, and mechanics. citeturn1search0turn1search1turn1search2turn1search3turn1search8
- [ ] CI success remains unverified.
- [ ] **Exact next:** inspect the next deterministic partially verified tranche after Batch 307 and continue promoting/enriching records only where direct Xenoverse 2 evidence adds new coverage; preserve nulls where it does not.


### 2026-09-24 cycle completion — Batch 308 cast-exclusive Ultimate evidence boundary
- [x] Bounded batch: **skill-batch-308 — Lightning Impact, Final Galick Rush, Lovely Showtime, Super Dragon Flight (Ultimate)**.
- [x] Revalidated current Xenoverse 2 cast-exclusive Ultimate taxonomy and 300-Ki costs from the current Ultimate Attack reference.
- [x] Revalidated CaC-unavailable variant identities against the maintained Xenoverse 2 Character ID List: Final Galick Rush short ID 1572, Lovely Showtime short ID 1561, and Super Dragon Flight (Ultimate) short ID 2081 are not CaC-usable; Lightning Impact's cast-exclusive variant is distinct from its CaC-usable short ID 1100 entry.
- [x] Revalidated DLC associations: Lightning Impact → Ultra Pack 2; Final Galick Rush and Lovely Showtime → Ultra Pack 1; Super Dragon Flight (Ultimate) has no explicit DLC requirement asserted.
- [x] Added `docs/data/skill-batch-308-cast-exclusive-ultimate-evidence-audit-2026-09-24.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved unresolved unlock methods and Ultimate Finish semantics where the evidence does not establish a CaC acquisition route; no cast-only variant was converted into a fabricated PQ/shop unlock.
- [x] Validation: audit JSON and cross-domain index re-parsed successfully; registration points to the live audit file; no canonical skill/index reconstruction or unsupported promotion was performed.
- [ ] CI: no workflow runs are exposed yet for the latest commit `0316e35e6a260e32d287bd2d00da6100250744ee`; no CI success claimed.
- [x] Commits: audit `74ed5fce17e54e9077152709160e0ce6f44cfd5c`; cross-domain registration `0316e35e6a260e32d287bd2d00da6100250744ee`.
- [ ] **Exact next:** inspect the next deterministic partially verified/cast-exclusive skill tranche after Batch 308, prioritizing records whose missing fields can be resolved by direct current Xenoverse 2 evidence; preserve the canonical builder boundary until a supported complete-file write path is available.


### 2026-09-24 cycle completion — Batch 56 Appetizing Rush evidence reconciliation
- [x] Bounded batch: **skill-batch-56 — Appetizing Rush**.
- [x] Revalidated current Xenoverse 2 evidence: Strike Ultimate, Android 21, cast-exclusive/CaC-unavailable, and Ultra Pack 2 association.
- [x] Confirmed the current Character ID evidence distinguishes Appetizing Rush as long ID **6111** / short ID **1111**, CaC Skill = No.
- [x] Recorded a live-source **Ki-cost conflict**: the dedicated Appetizing Rush page reports **400 Ki**, while the current Ultimate Attack table reports **300 Ki**. Neither value was promoted because the conflict is unresolved.
- [x] Added and registered `docs/data/skill-batch-56-appetizing-rush-evidence-audit-2026-09-24.json`; updated `docs/data/skill-research-batches/skill-batch-56.json` with the evidence boundary.
- [x] Validation: audit, research batch, and cross-domain registry parsed successfully; canonical skill catalogs were not reconstructed or speculatively modified.
- [ ] CI: no workflow runs exposed for the latest Batch 56 write; no CI success claimed.
- [x] Commits: audit `5deaf1b68318563ba22a7a1c6365949ef3f43c33`; registry `b53f2954635e50c174a98eb81cdddc8b88918223`; batch `8e64ee4394da4c1f8e5253871f6f67f8057ea2c7`.
- [ ] **Exact next:** continue the next existing partially verified skill-research record after Batch 56, using current Xenoverse 2 evidence to resolve classification/acquisition/mechanics where possible and preserving conflicts/nulls where evidence remains insufficient.


### 2026-09-24 cycle completion — Batch 309 Ki Blast Ultimate evidence enrichment
- [x] Continued **skill-batch-309 — Shocking Death Ball, Teleporting Vanishing Ball, Super Vanishing Ball**.
- [x] Strengthened Shocking Death Ball: Ki Blast Ultimate, 300 Ki, EM14 acquisition, 17-hit projectile/paralysis behavior, Super 17/Android 17 Customize Partner provenance.
- [x] Strengthened Teleporting Vanishing Ball: Ki Blast Ultimate, 300 Ki, PQ62 acquisition, 15-hit teleporting projectile behavior, Kid Buu provenance.
- [x] Strengthened Super Vanishing Ball: Ki Blast Ultimate, 300 Ki, Skill Shop acquisition, 18-hit long-range projectile behavior, Kid Buu/Janemba Customize Partner provenance.
- [x] Added and registered `docs/data/skill-batch-309-ki-blast-ultimate-evidence-audit-2026-09-24.json`.
- [x] Preserved unresolved drop probability, Ultimate Finish requirements, and shop-price semantics rather than inferring them.
- [x] Validation: audit and batch JSON parsed successfully; canonical promotion was intentionally not attempted.
- [ ] CI: no workflow runs exposed for the latest Batch 309 writes; no CI success claimed.
- [x] Commits: audit `82d70e6ef72b0a63ec37aba094a394325bb402e5`; batch `0117446e4c776f6bfb44a04adf7c0516377f7222`; registry `2fbc9ba78a634828bb544eaab27984a17b8b3794`.
- [ ] **Exact next:** continue **skill-batch-310**, starting with the next Ki Blast Ultimate whose missing fields can be directly resolved from current Xenoverse 2 evidence.


### 2026-09-24 cycle completion — Batch 310 Ki Blast Ultimate evidence enrichment
- [x] Completed **skill-batch-310** across Super Ghost Kamikaze Attack, Full Power Energy Blast Volley, Neo Tri-Beam, Vacation Delete, Breaker Energy Wave, God of Destruction's Menace, Revenge Death Ball, Gigantic Burst, and Prominence Flash.
- [x] Strengthened current Xenoverse 2 evidence for classification, Ki costs, acquisition endpoints, user provenance, hit counts, and mechanics where directly supported.
- [x] Corrected **Breaker Energy Wave** from unresolved cost to **0 Ki**, supported by its dedicated current page and its once-only low-health condition.
- [x] Preserved unresolved reward-probability and Ultimate-Finish semantics; no unsupported drop logic was introduced.
- [x] Added/registered `docs/data/skill-batch-310-ki-blast-ultimate-evidence-audit-2026-09-24.json` and updated the research batch.
- [x] Validation: changed JSON parsed successfully; canonical reconstruction was not attempted.
- [ ] CI: no workflow runs exposed for the latest writes; no CI success claimed.
- [x] Commits: audit `2d51e88b15617cc2ddcadac16426e96f4e87bd3a`; batch `581deac4d9b668b24a275af143b40d9027a9d695`; registry `31daf8470956f2464ec695b8e1579eeb711a98be`.
- [ ] **Exact next:** continue **skill-batch-311**, beginning with Blue Hurricane and Assault Rain, and resolve only fields directly supported by current Xenoverse 2 evidence.


### 2026-09-24 cycle completion — Batch 311 Blue Hurricane / Assault Rain evidence correction
- [x] Corrected Batch 311 Blue Hurricane identity to Burter; established 300 Ki and EM15 Basic Reward provenance.
- [x] Established Assault Rain at 300 Ki with Super Buu provenance and EM9 Basic Reward provenance.
- [x] Added and registered docs/data/skill-batch-311-blue-hurricane-assault-rain-evidence-audit-2026-09-24.json.
- [x] Changed JSON parsed successfully; no assistant citation/export artifacts detected in the changed files.
- [x] Preserved unresolved CaC, drop-rate, frame-data, and version-sensitive damage boundaries; no unsupported canonical promotion.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue Batch 311 with Spirit Ball, Death Meteor, and Minus Energy Power Ball using direct Xenoverse 2 evidence.


### 2026-09-24 cycle completion — Batch 311 remaining three-skill evidence reconciliation
- [x] Spirit Ball enriched: 300 Ki, Yamcha Lesson 3, controllable/tracking Ki Blast projectile.
- [x] Death Meteor enriched: 300 Ki, EM7 acquisition; corrected to Strike classification rather than forcing Ki Blast taxonomy.
- [x] Minus Energy Power Ball enriched: 500 Ki, Guru-expanded Shenron wish, 39-hit long-range Ki Blast.
- [x] Added and registered the remaining Batch 311 evidence audit.
- [x] JSON validation completed; unsupported drop/CaC/frame/damage claims preserved as unresolved.
- [ ] CI remains unverified.
- [ ] **Exact next:** inspect the remaining unfinished research census and continue the next deterministic partially verified tranche after Batch 311.


### 2026-09-24 cycle completion — Android 13's Hat residual accessory identity evidence
- [x] Strengthened `pqacc-022` / Android 13's Hat with external Xenoverse 2 inventory ID 918, Future Warrior accessory identity, and reported TP Medal Shop / 7 TP provenance.
- [x] Preserved the repository identity boundary: no new `acc-###` ID was invented and PQ105 was not treated as a guaranteed route.
- [x] Added and registered the dedicated residual identity audit; all changed JSON parses successfully.
- [ ] CI/runtime remains unavailable.
- [ ] **Exact next:** continue the residual accessory identity queue with the next unresolved exact-name candidate supported by direct current inventory evidence.


### 2026-09-24 cycle completion — Kale/Caulifla residual accessory domain resolution
- [x] `pqacc-027` Kale's Accessory → `equip-055` Kale Wig; PQ148 crosslink preserved.
- [x] `pqacc-028` Caulifla's Accessory → `equip-053` Caulifla Wig; PQ147 crosslink preserved.
- [x] Added/registered the domain-resolution audit; JSON validation passed.
- [ ] CI/runtime remains unverified.
- [ ] **Exact next:** audit the next unresolved late-DLC accessory identities, starting with Golden Frieza Head, Broly Wig (Black Hair, Normal), Dragon Ball Balloon, and Goku (Ultra Supervillain Quelled) Wig.


### 2026-09-24 cycle completion — four late-DLC accessory domain resolutions
- [x] Golden Frieza Head → `equip-107`; Broly Wig (Black Hair, Normal) → `equip-109`; Dragon Ball Balloon → `equip-110`; Goku (Ultra Supervillain Quelled) Wig → `equip-112`.
- [x] Added/registered audit and validated JSON.
- [x] No duplicate canonical accessory IDs created; unresolved reward-condition details remain separate.
- [ ] CI/runtime remains unverified.
- [ ] **Exact next:** continue the remaining unmatched accessory identities, starting with Android 14's Hat and Bardock (DB Super)'s Scouter.


### 2026-09-24 cycle completion — residual accessory evidence boundary: Android 14 / Bardock (DB Super) Scouter
- [x] Audited Android 14's Hat (PQ104) and Bardock (DB Super)'s Scouter (PQ146) against current Xenoverse 2 equipment/PQ sources.
- [x] Confirmed both PQs document character **clothing** rewards rather than exact character-specific accessory inventory identities.
- [x] Added and registered `docs/data/accessory-android14-bardock-super-scouter-evidence-audit-2026-09-24.json`.
- [x] Linked the audit from the accessory canonical bridge and preserved both records as unresolved; no generic Scouter or clothing-derived accessory was inferred.
- [x] Changed JSON parsed successfully and contains no internal citation/export markers.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue the remaining residual accessory candidates only when exact inventory-level evidence exists; otherwise resume the deterministic non-PQ/mentor consumer scan after Batch 311.


### 2026-09-25 — mentor coverage scalar repair
- [x] Corrected current-facing mentor counts in `skill-acquisition-coverage-report.json` from 132/131 to 131/130.
- [x] Validated against both current acquisition projection audits; status remains clean/pass.
- [ ] Continue the non-PQ consumer scan for remaining stale counts, orphan endpoint IDs, and one-way navigation.


### 2026-09-25 — mentor typed-reward consumer reconciliation
- [x] Corrected `mentor-skill-coverage-audit-2026-09-24.json` `typed_skill_rewards` from 131 to 132.
- [x] Preserved 131 resolved mentor→skill edges, 130 unique canonical targets, 1 unresolved Hit lesson, and 0 broken endpoints.
- [ ] Continue the current-facing non-PQ consumer scan for semantic count drift and one-way navigation.


### 2026-09-25 — mentor endpoint synchronization count repair
- [x] Corrected current typed mentor skill-reward count from 131 to 132 in `mentor-endpoint-consumer-synchronization-2026-09-24.json`.
- [x] Kept resolved endpoint counts at 131 edges / 130 unique targets with 1 unresolved lesson and 0 broken endpoints.
- [ ] Continue semantic count-drift scan across current mentor/non-PQ consumers.


### 2026-09-25 — TODO completion update — mentor typed-reward + PQ navigation consumer reconciliation
- [x] Repaired current mentor typed-skill reward count in docs/data/mentor-skill-coverage-report.json to 132, matching 133 lesson rewards minus the 1 typed non-skill Zamasu reward; resolved mentor skill edges remain 131, unique canonical targets 130, unresolved skill lessons 1, broken endpoints 0.
- [x] Repaired current PQ navigation domain counts in docs/data/pq-endpoint-navigation-current-audit-2026-09-24.json: equipment/accessory records 173 → 174 and character names 151 → 152.
- [x] Preserved the authoritative PQ relationship baseline at 853 total / 244 skill / 145 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming.
- [x] Changed JSON files re-parsed successfully; no canonical relationships or gameplay data were inferred or altered.
- [ ] CI remains unverified; the latest prior runs exposed zero workflow steps/logs. The exact next check is the Actions state for commit b16717265b2b606618ac08b7b6d74427c9aeb558.
- [ ] Exact next: continue exact-pair parity scanning of remaining current reverse/navigation consumers, prioritizing non-PQ equipment/accessory presentation consumers.


### 2026-09-25 — TODO CI status correction after consumer repairs
- [x] Confirmed the consumer-repair push `06b87bb911bebfb083439e2c3ccdc5fac3dbf270` still produces the same zero-step GitHub Actions failure pattern; no repository checker result is observable from those jobs.
- [x] Current main is `1bf72b0cd61d9746f48cc0679ffe7340b67e0525`; its quality/artifact/Pages runs were queued at inspection time.
- [ ] CI success remains unverified.
- [ ] **Exact next:** inspect the queued runs, then continue exact-pair reverse/navigation scanning if the runner failure persists.


### 2026-09-25 — Batch 312 evidence refresh completion
- [x] Confirmed latest Actions failures are runner-level (zero exposed steps/logs), not actionable repository test output.
- [x] Rechecked current non-PQ/Event/Raid/Festival/Chapter 4 consumers: current presentation baselines remain 152 characters / 469 skills / 174 equipment-accessory records / 11 raid accessory identities; checked consumer audits are clean.
- [x] Refreshed all 10 Batch 312 Ki Blast Ultimate records from direct current Xenoverse 2 pages.
- [x] Corrected Break Cannon to 300+ Ki and Perfect Kamehameha to 400 Ki with Cell (Perfect) Lesson 4 acquisition; confirmed Requiem of Destruction's Super Pack 2 association.
- [x] Added/registered `docs/data/skill-batch-312-ki-blast-ultimate-evidence-refresh-2026-09-25.json`; changed JSON re-parsed successfully.
- [ ] CI success remains unverified.
- [ ] **Exact next:** continue the next direct-evidence Batch 312/313 record; preserve unresolved fields and source conflicts.


### 2026-09-25 — Batch 313 evidence refresh completion
- [x] Refreshed all four Batch 313 Ki Blast Ultimate records from direct current Xenoverse 2 pages.
- [x] Added and registered docs/data/skill-batch-313-evidence-refresh-2026-09-25.json.
- [x] Confirmed 300-Ki costs and acquisition endpoints; added direct mechanics for Super Kamehameha, Saiyan Spirit, Explosive Assault, and Special Beam Cannon.
- [x] Preserved unresolved drop/Ultimate Finish/shop/version fields; no speculative canonical promotion.
- [x] Changed JSON re-parsed successfully.
- [ ] CI success remains unverified.
- [ ] Exact next: continue the next existing partially verified tranche after Batch 313 with direct evidence.


### 2026-09-25 — Batch 314 evidence refresh completion
- [x] Refreshed all five Batch 314 Ki Blast Ultimate records with direct current Xenoverse 2 evidence.
- [x] Corrected X4 Kaioken Kamehameha to 300-400 Ki and enriched staged-hit/fatigue mechanics; enriched X20 Kaioken Kamehameha, Dual Destructo-Disc, Innocence Breath, and Maiden Blast.
- [x] Added/registered docs/data/skill-batch-314-evidence-refresh-2026-09-25.json; changed JSON re-parsed successfully.
- [x] Preserved unresolved reward probabilities, Ultimate Finish requirements, shop pricing, version history, and canonical IDs.
- [ ] CI success remains unverified.
- [ ] Exact next: continue Batch 315 direct-evidence research.


### 2026-09-25 — Batch 315 evidence refresh completion
- [x] Refreshed all five Batch 315 Ki Blast Ultimate records with direct current Xenoverse 2 evidence.
- [x] Corrected variable Ki costs: Final Flash (SS3 DAIMA) 400+, Super Kamehameha (SS4 DAIMA) 400-500, Thunder Flash 300-600.
- [x] Added direct hit/mechanics evidence for Prominence Flash and Mystic Flash.
- [x] Added/registered docs/data/skill-batch-315-evidence-refresh-2026-09-25.json; changed JSON re-parsed successfully.
- [x] Preserved unresolved CaC/Ultimate Finish/reward/shop/version/canonical-ID fields.
- [ ] CI success remains unverified.
- [ ] Exact next: continue Batch 316 direct-evidence research.

### 2026-09-25 — TODO completion update — Batch 316 direct-evidence refresh
- [x] Refreshed `docs/data/skill-research-batches/skill-batch-316.json` for **Blaster Stream, Full Power Destruction, Gigantic Burst, Lightning Impact, and Requiem of Destruction** using current Xenoverse 2 evidence.
- [x] Added `docs/data/skill-batch-316-evidence-refresh-2026-09-25.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved unresolved Ultimate-Finish, reward-probability, exact-frame, version-sensitive damage, and unsupported race-restriction fields.
- [x] Validation: **470 canonical/index records, 0 duplicate IDs, 5/5 Batch 316 audit records, JSON parse clean, no internal citation/export markup in changed research/index files**.
- [ ] CI remains unverified; no usable workflow result was exposed for the latest evidence-registration commit.
- [ ] **Next:** direct-evidence refresh for **Angry Explosion, Assault Rain, Brave Heat, Break Cannon, Breaker Energy Wave, Chain Destructo-Disc Barrage, Chaotic Time Impact, and Circle Flash**.

### 2026-09-25 — TODO completion update — Batch 317 evidence reconciliation
- [x] Reconciled **8** handoff-carried Ki Blast Ultimate records and added `docs/data/skill-batch-317-evidence-reconciliation-2026-09-25.json`.
- [x] Registered the audit in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved existing reward conflicts/nulls and did not invent drop rates, frame data, damage, or narrower restrictions.
- [x] No canonical promotion was attempted; the records already exist in the live canonical/index layer.
- [ ] CI remains unverified.
- [ ] **Next:** select the next deterministic partially verified Ki Blast Ultimate tranche, excluding these already-reconciled records.

### 2026-09-25 — TODO completion update — Batch 318 Divine-series evidence refresh
- [x] Refreshed **Divine Lasso, Divine Ray Bomb, Divine Spear, Divine Wrath: Purification** with current direct evidence.
- [x] Added and registered `docs/data/skill-batch-318-divine-series-evidence-refresh-2026-09-25.json`.
- [x] Preserved unresolved reward/FI/frame/restriction fields rather than inferring them.
- [ ] CI remains unverified.
- [ ] **Next:** Divinity Unleashed, Do or Die, Dodon Ray, then adjacent stale records.

### 2026-09-25 — TODO completion update — Batch 319
- [x] Reconciled **Divinity Unleashed, Do or Die, Dodon Ray**.
- [x] Added and registered `docs/data/skill-batch-319-divinity-do-or-die-dodon-ray-evidence-reconciliation-2026-09-25.json`.
- [x] Preserved unresolved reward semantics and evidence boundaries.
- [ ] CI remains unverified.
- [ ] **Next:** recompute the live catalog and continue alphabetically after Dodon Ray, excluding completed evidence tranches.

### 2026-09-25 — TODO completion update — Batch 320
- [x] Reconciled **Atomic Blast, Bending Kamehameha, Big Bang Attack, Big Bang Kamehameha**.
- [x] Added and registered `docs/data/skill-batch-320-atomic-big-bang-evidence-refresh-2026-09-25.json`.
- [x] Preserved evidence conflicts and unsupported-field boundaries.
- [ ] CI remains unverified.
- [ ] **Next:** continue after the Batch 320 boundary with the next unreconciled Ki Blast Super records.


### 2026-09-25 — TODO completion update — Batch 321 Ki Blast Super evidence refresh
- [x] Refreshed **Bloody Sauce, Burst Attack, Confusion Blade, Consecutive Energy Blast, Crazy Finger Shot** using direct current Xenoverse 2 evidence.
- [x] Added `docs/data/skill-research-batches/skill-batch-321.json` and `docs/data/skill-batch-321-ki-blast-super-evidence-refresh-2026-09-25.json`.
- [x] Registered the Batch 316–321 evidence artifacts in `docs/data/pq-cross-domain-index.json`, including the previously omitted 316–320 registrations.
- [x] Validation: **470 skills/index records, 0 duplicate IDs, 5/5 Batch 321 records, JSON parse clean, no canonical reconstruction/promotion**.
- [x] Preserved unresolved reward probabilities, shop pricing/rotation, exact frame data, version-sensitive damage, and unsupported narrower restrictions.
- [ ] CI remains unverified; no successful Actions result is claimed.
- [ ] **Next:** recompute the live Ki Blast Super catalog and select the next 4–12 existing partially verified records after Batch 321, excluding Batches 316–321 and using direct current Xenoverse 2 evidence only where it can materially resolve fields.


### 2026-09-25 — TODO completion update — Batch 322 Death Wave / Murder Grenade
- [x] Recomputed the post-Batch-321 Ki Blast Super scope; only **Death Wave** and **Murder Grenade** remained as existing `partially_verified` records, so the batch intentionally contains 2 rather than inventing additional targets.
- [x] Added `docs/data/skill-research-batches/skill-batch-322.json` and `docs/data/skill-batch-322-death-wave-murder-grenade-evidence-refresh-2026-09-25.json`.
- [x] Registered Batch 322 in `docs/data/pq-cross-domain-index.json`.
- [x] Confirmed EM5/Death Wave and EM3/Murder Grenade current Basic Reward endpoints; preserved unresolved exact drop/guarantee semantics and did not infer first-clear guarantees.
- [x] JSON validation passed for all changed research/audit/index files.
- [ ] CI remains unverified.
- [ ] **Next:** recompute the live Ki Blast Super catalog and continue with the next research-incomplete records after Batch 322, excluding Batches 316–322.


### 2026-09-25 — TODO completion update — Death Meteor taxonomy parity correction
- [x] Corrected the stale `Death Meteor` projection from **Ultimate / Ki Blast** to **Ultimate / Strike** in `docs/data/skills-index.json`.
- [x] Synchronized `docs/data/skill-expert-mission-acquisition-early.json` to `canonical_subcategory: Strike` while preserving EM07 acquisition and unresolved reward semantics.
- [x] Added and registered `docs/data/death-meteor-taxonomy-parity-audit-2026-09-25.json`.
- [x] Validation: **470 index records**, changed JSON parsed cleanly, no internal citation artifacts detected, cross-domain index now **152** keys.
- [ ] CI remains unverified.
- [ ] **Next:** compare remaining partially_verified Ultimate projections — Assault Rain, Blue Hurricane, Dead End Bullet, Hellzone Grenade — against their current catalog/evidence classifications and correct only confirmed mismatches.


### 2026-09-25 — TODO completion update — Batch 311 Ultimate taxonomy parity
- [x] Audited Assault Rain, Blue Hurricane, Dead End Bullet, Hellzone Grenade against live taxonomy projections.
- [x] Corrected stale historical Batch 311 Blue Hurricane classification from Ki Blast to Strike; live canonical/index was already correct.
- [x] Confirmed the other three records require no taxonomy changes.
- [x] Added/registered docs/data/skill-311-ultimate-taxonomy-parity-audit-2026-09-25.json.
- [x] Validation: 470 skills-index records, Batch 311 has 5 records, JSON clean, cross-domain index 153 keys.
- [ ] CI remains unverified.
- [ ] Next: continue deterministic taxonomy parity checks across remaining partially_verified Ultimate records and their historical research batches.


### 2026-09-25 — TODO completion update — Ultimate EM taxonomy parity validator
- [x] Compared all **13** records in `skill-expert-mission-acquisition-early.json` against the live **470-record** skills index.
- [x] Found **0 class/subcategory mismatches**; Death Meteor and Blue Hurricane now agree as Strike across the corrected layers.
- [x] Added and registered `docs/data/ultimate-em-taxonomy-parity-audit-2026-09-25.json`.
- [x] Validation passed; cross-domain index now **154** keys.
- [ ] CI remains unverified.
- [ ] **Next:** inspect remaining historical/catalog parity for Shocking Death Ball and Spirit Sword, then continue to the next deterministic invariant.


### 2026-09-25 cycle completion — Shocking Death Ball / Spirit Sword historical parity audit
- [x] Live baseline remains **470 skills-index records** with the canonical/index taxonomy parity boundary preserved.
- [x] Compared **Shocking Death Ball** across the Batch 309 research layer, early Expert Mission acquisition layer, provenance audit, and Ki Blast Ultimate evidence audit: all agree on **Ultimate / Ki Blast**; no taxonomy mismatch found.
- [x] Compared **Spirit Sword** across the Expert Mission reconciliation, Strike Ultimate catalog, EM16–17 evidence, and canonical promotion manifest: all agree on **Ultimate / Strike**.
- [x] Preserved the historical EM17 **Spirit Sword / Spirit Bomb** naming conflict; no reward-tier, drop-rate, or guarantee claim was introduced or removed.
- [x] Added and registered `docs/data/ultimate-em-shocking-death-ball-spirit-sword-parity-audit-2026-09-25.json`.
- [x] Validation: **2 records checked / 0 class-subcategory mismatches / 0 unsupported taxonomy edits / 0 historical conflicts deleted**.
- [ ] CI remains unverified; no successful workflow result is exposed.
- [ ] **Exact next:** continue the next deterministic cross-database invariant after the EM taxonomy sweep, prioritizing a small current producer/consumer or reverse-navigation parity check rather than repeating already-clean skill taxonomy audits.


### 2026-09-25 cycle completion — Current skill consumer 470-record baseline synchronization
- [x] Found two explicitly current-facing consumers still asserting the superseded **469** skill baseline after the live canonical/index layer advanced to **470**.
- [x] Repaired `docs/data/current-character-equipment-raid-consumer-synchronization-2026-09-24.json` to use **470** canonical skills and renamed its current boolean to `skill_current_pq_consumer_uses_470`.
- [x] Refreshed `docs/data/pq-endpoint-navigation-validation.json` current/live skill-record fields to **470** while preserving the unchanged **244 PQ skill edges / 239 unique targets / 0 unresolved targets**.
- [x] Added and registered `docs/data/skill-current-consumer-470-baseline-synchronization-2026-09-25.json`.
- [x] Validation: **2 stale current count fields repaired / 0 relationship edges changed / 0 skill IDs promoted / 0 acquisition relationships inferred**.
- [x] Historical 469-record research artifacts were intentionally preserved rather than rewritten.
- [ ] CI remains unverified; no successful Actions result is claimed.
- [ ] **Exact next:** continue the remaining current-facing consumer census for stale **469/470** skill counts, then return to the non-PQ reverse/navigation invariant queue.


### 2026-09-25 cycle completion — second-pass current skill consumer census
- [x] Searched current-facing skill-count consumers after the live canonical/index baseline advanced to **470**.
- [x] Repaired five current consumers that still exposed **469**: PQ endpoint current audit, non-PQ acquisition endpoint audit, homepage consumer audit, skill-shop endpoint layer, and mentor skill coverage report.
- [x] Added and registered `docs/data/skill-current-consumer-census-2026-09-25.json`.
- [x] Validation: **470 canonical / 470 index**, **5 current consumer count repairs**, **0 relationship edges changed**, **0 acquisition routes inferred**, **0 historical snapshots rewritten**.
- [x] Historical per-batch artifacts retaining 469 were deliberately preserved as dated evidence.
- [ ] CI remains unverified.
- [ ] **Exact next:** resume the deterministic non-PQ reverse/navigation parity scan now that the explicit 469/470 current-scalar census has been completed.


### 2026-09-25 cycle completion — Non-PQ reverse/navigation parity repair
- [x] Recomputed the live non-PQ endpoint union against the **470-record** skill index and the **239 unique PQ-linked skill targets** using the maintained mentor, Expert Mission, shop, Time Rift/story/tournament, Tokipedia, Patrol, special, character-exclusive, and starting-move endpoint layers.
- [x] Found two uncovered non-PQ canonical skills: **Serious Bomb** and **Time Skip/Tremor Pulse**.
- [x] Repaired **Serious Bomb** by restoring its existing TP Medal Shop forward/reverse endpoint pair from its canonical `shop` acquisition fields; shop coverage is now **34 linked skills / 34 forward edges**.
- [x] Preserved **Time Skip/Tremor Pulse** as the single explicit unresolved endpoint because the current mentor layer intentionally withholds its canonical endpoint ID; no relationship was fabricated.
- [x] Added and registered `docs/data/non-pq-skill-reverse-navigation-parity-2026-09-25.json`.
- [x] Validation: **470 canonical skills / 239 PQ-linked / 231 non-PQ / 230 resolved non-PQ endpoint targets / 1 explicit unresolved target / 0 canonical IDs promoted / 0 acquisition relationships inferred**.
- [ ] CI remains unverified.
- [ ] **Exact next:** reconcile the remaining **Time Skip/Tremor Pulse** mentor-layer endpoint boundary against the canonical skill and current mentor evidence, preserving the unresolved state unless the normal endpoint-reconciliation evidence threshold is met.


### 2026-09-25 cycle completion — Final non-PQ reverse/navigation reconciliation
- [x] Reconciled the last uncovered non-PQ canonical skill: **Time Skip/Tremor Pulse** (`skill-time-skip-tremor-pulse`), whose exact canonical record now exists in the 470-record skill index.
- [x] Restored **Hit Lesson 3 → Time Skip/Tremor Pulse** across `mentor-endpoints.json`, `mentor-skill-crosslink-report.json`, and `mentor-skill-coverage-report.json` using the exact existing canonical ID; no skill identity was inferred or fabricated.
- [x] Synchronized `skill-acquisition-coverage-report.json` to the current 470/239/231 baseline and added a current 2026-09-25 projection.
- [x] Added and registered `docs/data/non-pq-skill-reverse-navigation-final-reconciliation-2026-09-25.json`.
- [x] Final validation: **470 canonical / 239 PQ-linked / 231 non-PQ / 231 resolved non-PQ endpoint targets / 0 unresolved non-PQ skills / 132 mentor skill edges / 131 unique mentor skill targets / 0 broken endpoints**.
- [ ] CI remains unverified; no successful Actions result is claimed.
- [ ] **Exact next:** resume the deterministic producer/consumer parity queue outside the now-clean non-PQ reverse-navigation invariant, prioritizing any remaining current 470-count consumer or cross-domain endpoint mismatch not already audited.
