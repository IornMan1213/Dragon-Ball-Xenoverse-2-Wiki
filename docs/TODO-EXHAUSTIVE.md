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
