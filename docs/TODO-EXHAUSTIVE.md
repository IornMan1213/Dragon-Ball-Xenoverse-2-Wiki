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
