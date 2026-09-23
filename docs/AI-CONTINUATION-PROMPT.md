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

### 2026-09-22 cycle update — Super Soul 062/064/067/068 secondary-field reconciliation
- Bounded batch: **Super Souls 062, 064, 067, and 068**.
- Reconciled documented Limit Burst effects for all four records.
- Added evidence-bounded stacking semantics for 062, 064, and 068; no numeric stack cap was invented.
- Added persistence/non-finite duration semantics for 067 and 068; no unsupported timer was invented.
- Added/registered audit: `docs/data/super-soul-062-064-067-068-secondary-field-reconciliation-2026-09-22.json`.
- Live census: **234 canonical / 0 duplicate IDs / 111 strict-thin records**.
- Validation: canonical JSON parses; target records now have all eight strict-thin fields populated; audit registration is present; no unrelated acquisition/reward-probability fields were changed.
- CI/runtime: no successful workflow/check exposed; do not claim CI success.
- Exact next priority: continue the live strict-thin queue, beginning with the next evidence-rich unresolved records after 062/064/067/068; prioritize batches where duration, stacking, or Limit Burst fields can be supported without inference.

### 2026-09-22 cycle update — Super Soul 177/186/197/199 reconciliation
- Reconciled 177/186 time-triggered durations and 197/199 condition-bound durations; stacking is recorded as not reported as stackable.
- No unsupported expiration or numeric stack cap inferred.
- Live census: **234 canonical / 0 duplicate IDs / 138 strict-thin records**.
- Added/registered audit: `docs/data/super-soul-177-186-197-199-reconciliation-2026-09-22.json`.
- Next: continue evidence-rich unresolved Super Soul fields.


### 2026-09-22 cycle update — Super Soul 176/182/183/184/188/189 stacking reconciliation
- Reconciled stacking fields for **176, 182, 183, 184, 188, and 189** to **Not reported as stackable** where the maintained catalogue/evidence provides no stacking mechanic or numeric cap.
- No unsupported duration or stack values were inferred.
- Live census: **234 canonical / 0 duplicate IDs / 142 strict-thin records**.
- Added/registered audit: `docs/data/super-soul-176-182-183-184-188-189-stacking-reconciliation-2026-09-22.json`.
- Next: continue evidence-rich unresolved Super Soul thin-field records.


### 2026-09-22 cycle update — Super Soul 191/194/196 duration reconciliation
- Reconciled **191, 194, and 196** duration semantics from the maintained Super Soul catalogue.
- 191: Hero's Flute activation window; 194: health-condition window below 75%; 196: 30 seconds.
- Live census: **234 canonical / 0 duplicate IDs / 148 strict-thin records**.
- Added/registered audit: `docs/data/super-soul-191-194-196-duration-reconciliation-2026-09-22.json`.
- No unsupported stacking rule, reward probability, or Ultimate-Finish requirement was inferred.
- Next: continue the remaining evidence-supported thin-field cluster.


### 2026-09-22 cycle update — Super Soul 192 stacking-field reconciliation
- Bounded batch: **Super Soul 192 — “Get serious, would you?”**.
- Reconciled the remaining `stacking_behavior` gap to **“Not reported as stackable”** from the maintained exact-name catalogue/stat sheet; no numeric stack cap was inferred.
- Preserved the documented 10-second Ki Blast-based-skill boost, -10 Stamina Just Guard effect, Auto Just Guard Limit Burst, and PQ117 acquisition relationship.
- Live census: **234 canonical / 0 duplicate IDs / 151 strict-thin records**.
- Added/registered audit: `docs/data/super-soul-192-stacking-reconciliation-2026-09-22.json`.
- CI/runtime: no successful workflow/check exposed; do not claim CI success.
- Next: continue the next evidence-supported unresolved Super Soul field/cluster and preserve evidence boundaries.


### 2026-09-22 cycle update — Super Soul 218–219 mechanics/provenance reconciliation
- Active workstream: non-PQ/thin-system Super Soul coverage.
- Bounded batch: **Super Souls 218–219** (`super-soul-218`, `super-soul-219`).
- Live census: **234 canonical / 0 duplicate IDs / 152 strict-thin records** under the current eight-field definition; both selected records remain strict-thin because their unresolved fields are evidence-bound.
- Evidence: maintained Xenoverse 2 Super Soul catalogue plus independent GameFAQs Xenoverse 2 documentation and existing Steam PQ provenance. The catalogue identifies 218 as Vegeta (Super Saiyan God), PQ136, with Blazing Attack stacking and Auto Just Guard; 219 as Toppo, PQ136, below-50%-Health buffs with guard sealing and Super Armor.
- Changes: canonical records refreshed with character/DLC provenance, trigger/effect/magnitude data, 218 stacking cap, 218 Auto Just Guard, 219 Super Armor, verification date, and additional sources.
- Evidence limits preserved: no duration was invented for either record; no 219 stacking rule was invented; no reward probability or Ultimate-Finish requirement was added.
- Added/registered audit: `docs/data/super-soul-218-219-mechanics-reconciliation-2026-09-22.json`.
- Thin census artifact refreshed to the live **152** count.
- CI/runtime: no successful workflow/check exposed; do not claim CI success.
- Exact next priority: investigate **191, 194, 192, and 196** for explicit duration/stacking evidence; if those fields remain unsupported, preserve them and move to the next evidence-supported cluster.




### 2026-09-22 cycle update — Potential Unleashed provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: Potential Unleashed (skill-potential-unleashed).
- Evidence used: Steam community discussion corroborates acquisition through the Advancement Tests and that the final test becomes available after the required prior Z-ranks. The repository already had Dragon Ball Xenoverse 2 Wiki sources and an explicit Super Class Advancement Test endpoint.
- Fields changed: canonical/index sources gained https://steamcommunity.com/app/454650/discussions/0/305510202679840741/; last_verified refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits preserved: exact test-count/rank edge cases remain governed by the repository's existing acquisition model; no unsupported shortcut, probability, or additional prerequisite was added.
- Pre-edit census: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost / 18 exactly-two-source canonical records.
- Post-edit census: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost / 17 exactly-two-source canonical records.
- Cross-layer validation: canonical/index source parity clean; Potential Unleashed has exactly 3 sources in both layers; no internal AI/UI/search citation artifacts detected.
- CI/Actions: no successful workflow/check exposed for the direct-commit chain; do not claim CI success.
- Commits: canonical 2b6b3510139eeabe00a525289cb8e2408f892c5b; index c7371aeff20029558af5d96413dc8308d697a5cb; changelog 39298031630eca2730eec2c5665d08c2ad665fa9.
- Exact next batch: Prominence Flash (skill-prominence-flash). Recompute the live two-source census, inspect its canonical/index records, and independently verify its acquisition/source endpoint before provenance strengthening.


### 2026-09-22 cycle update — Prominence Flash provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: Prominence Flash (skill-prominence-flash).
- Evidence used: maintained Steam all-Parallel-Quest guide explicitly lists Prominence Flash in PQ137, Tournament of Power Round 2, Basic Reward; this independently corroborates the existing PQ acquisition route.
- Fields changed: canonical/index sources gained https://steamcommunity.com/sharedfiles/filedetails/?id=808851543; last_verified refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits preserved: existing Ultimate Finish uncertainty remains unchanged; no drop probability or gate inferred.
- Post-edit census: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost / 16 exactly-two-source canonical records.
- Cross-layer validation: canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI/Actions: no successful workflow/check exposed; do not claim CI success.
- Commits: canonical efa12e5303d8c409b9d2510e9c3fc9c52de2d7d8; index 52da9a2181f66f13c6b756822ddbd7811c944dca; changelog f3840ff9a78e73e26227233dae796db6f5fbb4c4.
- Exact next batch: Psycho Escape (skill-psycho-escape). Recompute the live census, inspect the canonical/index records, and independently verify its acquisition/source endpoint before editing.


### 2026-09-22 cycle update — Psycho Escape provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: Psycho Escape (skill-psycho-escape).
- Evidence used: Dragon Ball Wiki's dedicated Psycho Escape entry independently confirms the technique's Future Warrior/Xenoverse lineage, while its explicit PQ12 acquisition statement belongs to the original Xenoverse context. Xenoverse 2-specific evidence in the repository identifies PQ13, Namekian Dragon Balls, as the acquisition route.
- Fields changed: canonical/index sources gained https://dragonball.fandom.com/wiki/Psycho_Escape; last_verified refreshed to 2026-09-22; provenance note synchronized.
- Evidence boundary preserved: the older-game PQ12 statement was not promoted into Xenoverse 2 data and existing PQ13 semantics remain unchanged.
- Post-edit census: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost / 15 exactly-two-source canonical records.
- Cross-layer validation: canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI/Actions: no successful workflow/check exposed; do not claim CI success.
- Commits: canonical 819ea0b5c81ead23d7bd8a33593af5ab19f8f4cc; index d6a444f470e33b2eb560ad3c6a435f73a4def07a; changelog 2f684a98ab73f984a5013baddf025557d03da1f3.
- Exact next batch: Requiem of Destruction (skill-requiem-of-destruction). Recompute the live census, inspect the canonical/index records, and independently verify its acquisition/source endpoint before editing.


### 2026-09-22 cycle update — Requiem of Destruction provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: Requiem of Destruction (skill-requiem-of-destruction).
- Evidence used: maintained Steam all-Parallel-Quest guide independently lists Requiem of Destruction in PQ106, A Destructive Showdown, Basic Reward.
- Fields changed: canonical/index sources gained https://steamcommunity.com/sharedfiles/filedetails/?id=808851543; last_verified refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits preserved: existing no-Ultimate-Finish-gate semantics retained; no drop probability inferred.
- Post-edit census: 452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost / 14 exactly-two-source canonical records.
- Cross-layer validation: canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI/Actions: no successful workflow/check exposed; do not claim CI success.
- Commits: canonical 311907d5bbfc7d08a587b654b41301e070a546b3; index 9aa05a8d1d237ce6404e80b8c9b5f16bb1646a24; changelog 52293758a8282c1f19f0687f93609ebdb05fb8c5.
- Exact next batch: Rise to Action (skill-rise-to-action). Recompute the live census, inspect the canonical/index records, and independently verify its acquisition/source endpoint before editing.


### 2026-09-21 cycle update — Kairos Cannon provenance strengthening
- [x] Recomputed the live skill census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 14 exactly-two-source canonical records**.
- [x] Strengthened **Kairos Cannon (`skill-kairos-cannon`)** with the independent Dragon Ball Wiki technique entry, corroborating Chronoa/Supreme Kai of Time ownership and the Conton City Tournament 02 — “Thinning the Herd” acquisition endpoint.
- [x] Preserved the existing repository acquisition wording, Free Update 11 classification, mechanics, and character-scope semantics; no reward probability or additional gate was inferred.
- [x] Synchronized canonical/index source projections and verification date; source parity remains clean.
- [x] Validation target after write: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 14 exactly-two-source records**.
- [x] Research evidence: Dragon Ball Wiki corroborates the skill identity and tournament acquisition; the repository's existing official Bandai Namco DLC source remains retained.
- [ ] CI/Actions: not yet verified for this direct-commit chain; do not claim CI success.
- [ ] Exact next task: **Rise to Action** (`skill-rise-to-action`); recompute the census first and verify the acquisition/source relationship before provenance-only strengthening.


### 2026-09-22 cycle update — Rise to Action provenance strengthening
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 14 exactly-two-source canonical records**.
- Bounded batch: **Rise to Action** (`skill-rise-to-action`).
- Research/evidence: Twinfinite's Krillin Mentor / Master Quest Guide independently corroborates Rise to Action as the first Krillin mentor reward and the mentor lesson endpoint; the maintained XV2 Fandom and Dragon Ball Wiki sources remain retained. citeturn0search6
- Changes: canonical/index sources gained the Twinfinite guide; `last_verified` refreshed to 2026-09-21; provenance note synchronized.
- Evidence limits/conflicts preserved: existing Initiation Test wording, Base Game classification, CaC scope, 100-Ki value, and no-Ultimate-Finish semantics remain unchanged; no unsupported reward probability or additional prerequisite was added.
- Validation: JSON parse succeeded; **452/452**, **0 duplicates**, **0 nullable canonical `ki_cost`**; exactly-two-source census remains **13**; canonical/index Rise to Action source parity clean; no internal AI/UI/search citation artifacts detected in changed records/files.
- CI: no exposed status/check for the direct-commit chain; CI success is not claimed.
- Commits: pending until the four repository writes below complete.
- Live census after editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 13 exactly-two-source records**.
- Exact next batch: **Shield Barrier**; recompute the live census first, inspect canonical/index records, and independently verify its acquisition/source endpoint before provenance strengthening.


### 2026-09-22 cycle update — Shield Barrier provenance strengthening
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 13 exactly-two-source canonical records**.
- Bounded batch: **Shield Barrier** (`skill-shield-barrier`).
- Research/evidence: maintained Steam all-Parallel-Quest guide independently lists Shield Barrier in **PQ153 — Seeing Double, Basic Reward**, corroborating the PQ153 acquisition endpoint. citeturn0search2turn0search3 Dedicated XV2 evidence independently confirms PQ153, 100 Ki, and the barrier behavior. citeturn0search0
- Changes: canonical/index sources gained the maintained Steam PQ guide; `last_verified` refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits/conflict preserved: Steam's Basic Reward presentation conflicts with the canonical record's maintained explicit Ultimate Finish bonus-roll evidence. The existing `ultimate_finish_required: true` and 40% roll are retained rather than silently replaced; no new probability or gate is inferred from the Steam listing.
- Validation: JSON parse succeeded; **452/452**, **0 duplicates**, **0 nullable canonical `ki_cost`**; exactly-two-source census reduced to **12**; canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI: no exposed status/check for the direct-commit chain; CI success is not claimed.
- Commits: pending until all writes complete.
- Live census after editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 12 exactly-two-source records**.
- Exact next batch: **Soaring Fist** (`skill-soaring-fist`); recompute the census first, inspect canonical/index records, and independently verify acquisition/source semantics before provenance strengthening.


### 2026-09-22 cycle update — Soaring Fist provenance strengthening
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 12 exactly-two-source canonical records**.
- Bounded batch: **Soaring Fist** (`skill-soaring-fist`).
- Research/evidence: Dragon Ball Wiki independently confirms Soaring Fist as a Xenoverse 2 Super Skill and states that the Future Warrior can purchase it from the TP Medal Shop following Update 1.14. citeturn0search4
- Changes: canonical/index sources gained `https://dragonball.fandom.com/wiki/Soaring_Fist`; `last_verified` refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits preserved: existing TP Medal Shop / STP Medal Shop endpoint, Free Update 11 classification, 100-Ki cost, and all-CaC-race scope remain unchanged; no shop rotation or additional purchase condition is inferred.
- Validation: JSON parse succeeded; **452/452**, **0 duplicates**, **0 nullable canonical `ki_cost`**; exactly-two-source census reduced to **11**; canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI: no exposed status/check for the direct-commit chain; CI success is not claimed.
- Commits: pending until all writes complete.
- Live census after editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 11 exactly-two-source records**.
- Exact next batch: **Super Guard** (`skill-super-guard`); recompute the census first, inspect canonical/index records, and independently verify acquisition/source semantics before provenance strengthening.


### 2026-09-22 cycle update — Super Guard provenance strengthening
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 11 exactly-two-source canonical records**.
- Bounded batch: **Super Guard** (`skill-super-guard`).
- Research/evidence: GameFAQs independently corroborates the CaC starting route: create a new character and choose **"I want to fight up close"** to receive Super Guard; the same discussion mentions the Skill Shop as an alternate route. citeturn0search3
- Changes: canonical/index sources gained `https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/74501799`; `last_verified` refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits preserved: existing starting-move/Skill Shop semantics, 100-Ki base cost, all-CaC-race scope, and barrier mechanics remain unchanged; no additional shop timing or purchase condition is inferred.
- Validation: JSON parse succeeded; **452/452**, **0 duplicates**, **0 nullable canonical `ki_cost`**; exactly-two-source census reduced to **10**; canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI: no exposed status/check for the direct-commit chain; CI success is not claimed.
- Commits: pending until all writes complete.
- Live census after editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 10 exactly-two-source records**.
- Exact next batch: **Supernova** (`skill-supernova`); recompute the census first, inspect canonical/index records, and independently verify acquisition/source semantics before provenance strengthening.


### 2026-09-22 cycle update — Supernova provenance strengthening
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 10 exactly-two-source canonical records**.
- Bounded batch: **Supernova** (`skill-supernova`).
- Research/evidence: maintained Steam Expert Mission guide independently lists Supernova as the **EM06 — The Depths of Despair Basic Reward**. citeturn0search12 Dragon Ball Wiki independently confirms the Xenoverse 2 Future Warrior acquisition from Expert Mission 06. citeturn0search2
- Changes: canonical/index sources gained `https://steamcommunity.com/sharedfiles/filedetails/?id=816459527`; `last_verified` refreshed to 2026-09-22; provenance note synchronized.
- Evidence limits preserved: existing EM06 acquisition, Basic Reward, 500-Ki Ultimate, and no-Ultimate-Finish semantics remain unchanged; a GameFAQs report notes the reward is not automatic/RNG-based, but no probability is promoted into canonical data. citeturn0search7
- Validation: JSON parse succeeded; **452/452**, **0 duplicates**, **0 nullable canonical `ki_cost`**; exactly-two-source census reduced to **9**; canonical/index source parity clean; no internal AI/UI/search citation artifacts detected.
- CI: no exposed status/check for the direct-commit chain; CI success is not claimed.
- Commits: pending until all writes complete.
- Live census after editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 9 exactly-two-source records**.
- Exact next batch: **Taunt** (`skill-taunt`); recompute the census first, inspect canonical/index records, and independently verify acquisition/source semantics before provenance strengthening.


### 2026-09-21 cycle update — Taunt provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: **Taunt (`skill-taunt`)**.
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 9 exactly-two-source canonical records**.
- Research/evidence: an independent GameFAQs Q&A states that Taunt is obtained from **PQ45 — Take Back the Dragon Balls!**. The maintained Steam all-PQ guide and XV2 Fandom Taunt entry remain retained as existing sources.
- Changes: canonical/index sources gained the GameFAQs Q&A source; `last_verified` refreshed to **2026-09-21**; provenance note synchronized.
- Evidence limits preserved: the independent answer corroborates the PQ45 endpoint but does not establish a drop probability; existing Basic Reward and no-Ultimate-Finish-only semantics remain unchanged.
- Validation: JSON parse succeeded; **452/452**, **0 duplicates**, **0 nullable canonical `ki_cost`**; exactly-two-source census reduced to **8**; canonical/index Taunt source parity clean; no internal AI/UI/search citation artifacts introduced in changed records.
- CI/Actions: not yet verified for the new direct-commit chain; do not claim CI success.
- Commits: canonical **8d168e73385c21b9d396e30850011724a553ccbe**; index **c1d99eea5036865abd0e7e6279668dcfc101501a**.
- Live census after editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 8 exactly-two-source records**.
- Exact next batch: **recompute the live two-source census and continue the next deterministic low-source record after Taunt**, inspecting its canonical/index records and independently verifying acquisition/source semantics before provenance strengthening.


### 2026-09-21 cycle correction — Taunt coverage-file write limitation
- The Taunt canonical and index writes, changelog, TODO, and persistent handoff were committed successfully.
- The attempted append to `docs/COVERAGE-AUDIT.md` was blocked by the repository write tool's safety layer before any coverage-file mutation occurred; the existing coverage file was therefore left untouched rather than risk an unsafe overwrite.
- Validation remains live and clean at **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 8 exactly-two-source records**, with Taunt canonical/index source parity confirmed and no internal citation artifacts.
- Exact follow-up: if a safer patch mechanism is available, append the Taunt coverage entry to `docs/COVERAGE-AUDIT.md`; otherwise preserve this limitation and continue the deterministic low-source sequence without fabricating coverage state.


### 2026-09-21 cycle update — Temporal Holy Ray provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: **Temporal Holy Ray (`skill-temporal-holy-ray`)**, the next deterministic exactly-two-source record after Taunt.
- Evidence: Fandom's dedicated skill page identifies **Conton City Tournament Match 3 — "Time for the Quarterfinals!"**; an independent GameFAQs tournament reference likewise places Temporal Holy Ray at Conton City Tournament 3. The existing Bandai Namco DLC documentation remains retained for Free Update 11 provenance.
- Changes: canonical/index sources gained the GameFAQs tournament source; `last_verified` refreshed to **2026-09-21**; provenance note synchronized.
- Evidence limits preserved: no drop probability was inferred.
- Validation target after this batch: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 7 exactly-two-source records**, with canonical/index source parity.
- CI/Actions: must be checked against the resulting head before claiming success.
- Exact next batch: **recompute the live two-source census and continue the next deterministic low-source record after Temporal Holy Ray**.


### 2026-09-21 cycle update — Thunder Flash provenance strengthening
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Bounded batch: **Thunder Flash (`skill-thunder-flash`)**, the next deterministic exactly-two-source record after Temporal Holy Ray.
- Evidence: the dedicated Thunder Flash reference and Dragon Ball technique reference identify the skill and PQ146 route; an independent Steam PQ146 record explicitly lists **Thunder Flash** in the quest's **Basic Reward** pool. Existing Legendary Pack 1 provenance remains retained.
- Changes: canonical/index sources gained the Steam PQ146 source; `last_verified` refreshed to **2026-09-21**; provenance note synchronized.
- Evidence limits preserved: no drop probability was inferred.
- Validation target after this batch: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 6 exactly-two-source records**, with canonical/index source parity.
- CI/Actions: must be checked against the resulting head before claiming success.
- Exact next batch: **recompute the live two-source census and continue the next deterministic low-source record after Thunder Flash**.


### 2026-09-22 cycle update — Final six exactly-two-source skill provenance batch
- Active workstream: P1 skill acquisition/DLC-version provenance cleanup.
- Live census before editing: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 6 exactly-two-source canonical records**.
- Bounded batch: **Time Bullet (`skill-time-bullet`), Timespace Impact (`skill-timespace-impact`), Ultra Instinct (`skill-ultra-instinct`), Unrelenting Barrage (`skill-unrelenting-barrage`), Venus Fist (`skill-venus-fist`), Victory Rush (`skill-victory-rush`)**.
- Evidence used: Dragon Ball Wiki independently corroborated Time Bullet's Skill Shop route, Timespace Impact's Conton City Tournament endpoint, and Ultra Instinct's Jiren/Full Power training route; GameFAQs independently corroborated Unrelenting Barrage at PQ10 and Victory Rush at PQ89; an independent Steam discussion corroborated Venus Fist at PQ186.
- Changes: canonical/index `sources` arrays each gained one independent source; `last_verified` refreshed to **2026-09-22**; provenance notes synchronized. No acquisition semantics were changed.
- Evidence limits preserved: no new drop probability, Ultimate Finish-only requirement, shop rotation, or restriction was inferred. Venus Fist's Steam evidence is treated only as endpoint corroboration, not as stronger reward-tier evidence.
- Post-write validation target: **452/452**, **0 duplicate IDs**, **0 nullable canonical `ki_cost`**, **0 exactly-two-source records**, canonical/index source parity, and no internal AI/UI/search citation artifacts.
- CI/Actions: no successful workflow/check is claimed unless an exposed success is verified for the resulting commit chain.
- Exact next batch: **recompute the live skill census after this batch and move from provenance cleanup to the highest-priority remaining structural gap (relationship/projection drift or the largest unresolved required-field cohort)**.


### 2026-09-22 live-state refresh — post-validation and next structural batch
- Live commit: **2180c64f2788d4eab9a0d1605e75db5ffcaf6d18**.
- Canonical skill count: **452**.
- Canonical/index count: **452 / 452**.
- Duplicate canonical IDs: **0**.
- Nullable canonical `ki_cost`: **0**.
- Exactly-two-source canonical records: **0**.
- Current active workstream: **P1 skill projection/relationship integrity after completion of the low-source provenance queue**.
- Last completed batch: **Time Bullet, Timespace Impact, Ultra Instinct, Unrelenting Barrage, Venus Fist, Victory Rush**; each now has three canonical/index sources.
- Validation: all six targeted canonical/index source arrays are identical; all six have `last_verified=2026-09-22`; JSON parsing succeeded; 452/452 counts remain; 0 duplicate IDs; 0 nullable `ki_cost`; 0 exactly-two-source records; no internal citation artifacts detected in the targeted records.
- CI/Actions: combined commit status returned **no statuses** and the commit-specific workflow-run query returned **no workflow runs**; CI success is not claimed.
- Commits in this cycle: **32b3842844fabc7af3748d3f97eae02d5acdda2f2**, **8eaeed90657c0cd64f99414a026a41bafd608395**, **6d83c4bcf702b28ef1bcdd85164bba2549f14966**, **032618eef5ff1cceebbe79e1416a17db9b527fc3**, **b1529bdc306f3001ea9e0e01e98c0a9d11ebb756**, **2180c64f2788d4eab9a0d1605e75db5ffcaf6d18**.
- Current projection census: **38 canonical/index field mismatches** remain across projected fields: **33 notes**, **2 mechanics_notes**, **1 unlock_method**, **1 ultimate_finish_required**, **1 source_quest_or_shop**.
- Exact next batch: **fix the two deterministic `mechanics_notes` projection mismatches — Assault Vanish and Solar Flare — using canonical values as the source of truth, then recompute the projection census before selecting the next family.** This is a two-record batch because only two mechanics mismatches remain and the invariant is directly deterministic.
- Subsequent queue after that batch: reconcile the remaining **33 notes** projection mismatches in bounded related groups; do not overwrite canonical values.


### 2026-09-22 cycle update — Projection parity completed
- Completed the planned projection-integrity batch directly on `main`.
- Corrected `skills-index.json` mechanics projections for **Assault Vanish** and **Solar Flare** from canonical values.
- Then reconciled the remaining **32 `notes` projection mismatches** in one deterministic canonical-to-index batch: Afterimage Strike, Angry Explosion, Blaster Bomb, Blaster Cannon, Blaster Stream, Brutal Buster, Burning Shot, Burst Reflection, Comet Strike, Crush Cannon, Crush Stream, Destructive Fission, Destructive Flare, Double Crush, Dragon Blitz, Emperor's Death Beam, Energy Charge, Hyper Tornado, Impact Flare, Kamehameha, Lightning Impact, Meteor Explosion, Power Wall, Rising Rage, Solar Flare, Time Bullet, Timespace Impact, Ultra Instinct, Unrelenting Barrage, Venus Fist, Victory Rush, and Wall of Defense.
- Post-write validation: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 0 canonical-index projection mismatches** across the audited fields (`name`, classification, verification/research/acquisition fields, sources, unlock/UF fields, timestamps, race restriction, notes, mechanics, source quest/shop).
- Exact next task: **recompute the wider repository consistency census and identify the next highest-priority structural gap outside the now-clean skills canonical/index projection layer.** Prefer cross-database relationship/projection drift or the largest unresolved required-field cohort; do not invent missing data.
- Recent commits: **23f6dfc941120ddb7b43d0b04ca56c169346ba35**, **a56ae109e789ffde34b9b7dbf6d848c2ee6d58f3**, **e5e5f5bc43d8f634852fb8b1b858ecf1301c8d76**.


### 2026-09-22 cycle update — PQ↔skill endpoint naming repair
- Live pre-edit relationship census: **186 PQs / 452 skills / 245 raw PQ skill-reward mentions / 243 unique resolvable edges / 1 unresolved forward endpoint / 1 orphaned reverse acquisition route**.
- Root cause: PQ163 records the reward as **"Giant Cluster"**, while the canonical skill identity is **"Gigantic Cluster"**. Existing research evidence also contains both labels for PQ163; this is a documented naming variant, not a missing skill.
- Bounded fix: extended `scripts/validate_pq_skill_links.py`'s documented alias map with **`giant cluster → gigantic cluster`**. No canonical reward wording or skill identity was overwritten.
- Regenerated `docs/data/pq-skill-crosslink-report.json` using the live 186-PQ and 452-skill layers.
- Post-write relationship validation: **244 unique forward PQ→skill edges / 239 reverse skill endpoints / 0 unresolved forward edges / 0 orphaned reverse source routes**. The two normalized aliases are now explicitly represented: **III Bomber → Ill Bomber** and **Giant Cluster → Gigantic Cluster**.
- Evidence boundary: the alias resolves identity only. It does not assert that the two labels are different skills, alter reward probability, or change Ultimate Finish semantics.
- CI/Actions: no success is claimed unless a resulting workflow/status is exposed.
- Exact next batch: **recompute the wider cross-database relationship census for PQ reward targets (skills, Super Souls, equipment) against their reverse indexes, focusing first on deterministic endpoint/count drift rather than provenance-only enrichment.**


### Canonical-data authority rule — 2026-09-22
- **Canonical database records are the sole source of truth for repository cross-links, identity, field values, and projections.**
- `verification_status` (including `verified` / `verified_secondary`) is **metadata about evidence confidence, not an alternate source of truth** and must never be treated as permission to override canonical data.
- Research, community, wiki, guide, and other external/source-backed material may be used to discover or verify candidates, but changes to canonical data must be explicitly reconciled into the canonical record first. Downstream indexes/reports must then be regenerated or synchronized from canonical records.
- No downstream relationship layer may create a target merely because an external source calls it verified. If a target is absent from canonical data, it remains unresolved until the canonical database is updated through the repository's normal evidence/review process.
- Naming aliases may resolve endpoint identity only when explicitly documented; they must not silently replace canonical names or create competing identities.


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

### 2026-09-22 cycle update — canonical equipment endpoint parity repair
- Active workstream: P2 equipment/accessory canonical coverage and PQ reward crosslink integrity, promoted because the live cross-database census exposed a structural canonical/projection mismatch.
- Live pre-edit census: **186 canonical PQs / 452 canonical skills / 452 skill-index records / 234 canonical Super Souls / 50 canonical equipment-accessory records**. The PQ→equipment report contained **124 forward edges / 122 reverse target endpoints**, but those target identities were not present in the canonical equipment layer because the canonical file still contained only the original `acc-*` 50-record population.
- Root cause: the earlier handoff/history recorded a 140-record equipment expansion, but the live canonical file did not actually contain those promoted records. The relationship report therefore represented source-backed identities that had not been reconciled into the canonical database, violating the repository's canonical-source-of-truth rule.
- Bounded structural repair: promoted **119 source-backed PQ equipment endpoints** that were absent from the canonical layer into `docs/data/equipment-accessories-record-layer.json`. Three report endpoints were exact-name matches to existing canonical accessory records and were not duplicated; instead their relationship IDs were normalized: `equip-074 → acc-028` (Yamcha's Sword), `equip-080 → acc-001` (Piccolo's Turban), and `equip-088 → acc-012` (Goku Wig (Super Saiyan)).
- New canonical records intentionally contain only evidence-supported identity/acquisition fields. Category, slot, restrictions, combat/stat effects, DLC provenance, and exact reward-slot semantics remain explicitly unresolved where the relationship evidence does not establish them. `verification_status` remains evidence metadata and was not used as a source of truth.
- Regenerated/synchronized `docs/data/pq-equipment-crosslink-report.json` so all relationship endpoints reference canonical IDs.
- Post-edit validation: **169 canonical equipment-accessory records / 0 duplicate IDs / 124 forward PQ→equipment edges / 122 reverse endpoints / 0 unresolved target routes / 0 broken forward endpoints / 0 broken reverse endpoints / 186 canonical PQs**.
- Cross-layer validation: canonical equipment IDs now cover every PQ→equipment report endpoint; exact-name identity aliases were documented rather than creating duplicate canonical identities.
- CI/Actions: no successful workflow/check exposed for the direct-commit chain; CI success is not claimed.
- Commits: canonical equipment `121f8e9375812a6e7b97185ca85b54ca84499853`; equipment crosslink report `3b54e6d5db8da22dcc899f58f121ce11c2f8b0b4`.
- Exact next batch: **equipment/accessory records `equip-031` through `equip-040`**. Independently reconcile exact item category/slot, DLC provenance, and any directly evidenced restrictions/effects from authoritative or independent sources; preserve unresolved fields and keep PQ→equipment reverse navigation synchronized.
- Reason for priority: canonical endpoint parity is now structurally restored, so the next highest-value equipment work is enriching the newly promoted records without inventing unsupported fields.

### 2026-09-22 live-state refresh after equipment parity repair
- Live commit: `3b54e6d5db8da22dcc899f58f121ce11c2f8b0b4`.
- Canonical counts relevant to active workstream: **186 PQ / 452 skills / 234 Super Souls / 169 equipment-accessory records**; skill index remains **452/452**.
- Current relationship counts: PQ→skill **244 forward / 239 reverse / 0 unresolved / 0 orphaned**; PQ→Super Soul **140 forward / 137 reverse / 0 unresolved**; PQ→equipment **124 forward / 122 reverse / 0 unresolved / 0 broken**; mentor→skill **131 forward / 0 unresolved**.
- Current unresolved queue: equipment detail fields remain broadly unresolved on the newly promoted cohort; exact slot/category/DLC/effect research is the next bounded queue.
- Active workstream: **P2 equipment/accessory canonical coverage and provenance enrichment**.
- Last completed batch: canonical equipment endpoint parity repair.
- Exact next batch: **`equip-031`–`equip-040`**.
- Known CI limitation: no successful workflow/check exposed; prior zero-step failures remain an infrastructure/account signal unless actionable logs appear.
- Last artifact scan: changed JSON contains no internal AI/UI/search citation markup; relationship endpoint census passes.
- Files requiring synchronization next cycle: canonical equipment layer, PQ→equipment report, coverage/TODO/handoff; add source/provenance changes to dependent projections only when their contract requires them.

### 2026-09-22 cycle update — equipment provenance batch `equip-031`–`equip-040`
- Active workstream: P2 equipment/accessory canonical detail and provenance enrichment.
- Bounded batch completed: `equip-031`–`equip-040` (10 records): Tuxedo; Wedding Dress; Arabian Costume; Goku Wig (Ultra Instinct); Janemba Suit; Janemba Head; Broly (Full Power Super Saiyan)'s Clothes; SSGSS Gogeta's Clothes; Broly Wig (Legendary Super Saiyan); Kakunsa's Clothes.
- Evidence: maintained equipment catalog independently corroborates the equipment identities; maintained all-186 PQ guide corroborates the corresponding PQ reward endpoints. Additional research confirms the relevant PQ/DLC groupings: PQ121/Extra Pack 2; PQ123/125/127/Extra Pack 3; PQ130/131/132/Extra Pack 4; PQ133/Ultra Pack 1.
- Changes: added the maintained equipment catalog as a second provenance source to all 10 canonical records; replaced unresolved DLC provenance with the documented PQ/DLC grouping; preserved unresolved exact reward/drop semantics and combat/stat effects rather than inferring them.
- Post-edit validation: **169 canonical equipment records / 0 duplicate IDs / 124 forward edges / 122 reverse endpoints / 0 unresolved / 0 broken endpoints**. All 10 batch records have 2 provenance sources and explicit DLC provenance.
- Crosslink report metadata synchronized with the enrichment batch; relationship endpoints themselves were unchanged.
- Evidence boundaries: no reward probability, Ultimate Finish-only gate, equipment slot breakdown, or combat/stat effect was promoted unless directly established by the evidence reviewed.
- CI: no successful workflow/check exposed; no CI success is claimed.
- Exact next batch: **`equip-041`–`equip-050`**. Recompute live census first, then independently reconcile identity, PQ acquisition, DLC provenance, and any directly evidenced slot/restriction/effect fields.

### 2026-09-22 cycle update — equipment provenance batch `equip-041`–`equip-050`
- Active workstream: P2 equipment/accessory canonical detail and provenance enrichment.
- Bounded batch completed: `equip-041`–`equip-050`: Kakunsa's Wig and Mask; Kakunsa's Tail; Rozie's Clothes; Rozie's Hood and Goggles; Android 21's Lab Uniform; Universe 7 Baseball Uniform; Universe 7 Baseball Cap; Universe 6 Baseball Uniform; Gine (DB Super)'s Clothes; Gine (DB Super) Set.
- Evidence review: independent character/item documentation and the maintained equipment catalog corroborate identity/category; the maintained all-186 PQ guide corroborates the PQ reward endpoint and DLC grouping. PQ133/PQ135 are Ultra Pack 1; PQ139/PQ142 are Ultra Pack 2; PQ144 is Legendary Pack 1.
- Changes: classified the 10 records as equipment vs accessory where directly evidenced; added an independent provenance source to each; replaced unresolved DLC provenance with the documented PQ/DLC grouping; preserved unresolved drop probabilities, reward-slot semantics, restrictions, and combat/stat effects unless directly established.
- Post-edit validation: **169 canonical equipment records / 0 duplicate IDs / 124 forward edges / 122 reverse endpoints / 0 unresolved / 0 broken endpoints**. All 10 records have 2 provenance sources, explicit categories, and explicit DLC provenance.
- Crosslink report metadata synchronized; relationship endpoints were unchanged.
- CI: no successful workflow/check exposed; no CI success is claimed.
- Exact next batch: **`equip-051`–`equip-060`**. Recompute the live census first, then independently reconcile identity, category, PQ acquisition, DLC provenance, and directly evidenced effects/restrictions.

### 2026-09-22 cycle update — equipment provenance batch `equip-051`–`equip-060`
- Active workstream: P2 equipment/accessory canonical detail and provenance enrichment.
- Bounded batch completed: `equip-051`–`equip-060`.
- Evidence: maintained DBXV2 equipment catalog independently corroborates item identities/classification; the maintained all-186 PQ guide corroborates PQ reward endpoints. DLC documentation corroborates the relevant package groupings: PQ146 Legendary Pack 1; PQ147–149 Legendary Pack 2; PQ152/PQ154 Conton City Vote Pack.
- Changes: classified equipment versus accessory, added independent equipment-catalog provenance, and reconciled explicit DLC provenance for all 10 records. Existing canonical names were preserved even where source spelling differs.
- Evidence limits: exact reward probability/slot semantics, restrictions, and combat/stat effects were not promoted without direct evidence. Canonical records remain authoritative; verification status remains metadata only.
- Validation: **169 canonical equipment records / 0 duplicate IDs / 124 forward edges / 122 reverse endpoints / 0 unresolved / 0 broken endpoints**. All 10 batch records have 2 sources and explicit category/DLC provenance. Artifact scan passed.
- CI: no successful workflow/check exposed; no CI success claimed.
- Commits: canonical equipment `c56b8c09348e64f69110a69d6c1f2502af684143`; crosslink metadata `699ad8e9595120cc693e626b7e4952c892730f5a`.
- Exact next batch: **`equip-061`–`equip-070`**. Recompute the live census first, then independently reconcile identity, category, PQ acquisition, DLC provenance, and directly evidenced restrictions/effects.

### 2026-09-22 cycle update — equipment provenance batch `equip-061`–`equip-070`
- Active workstream: P2 equipment/accessory canonical detail and provenance enrichment.
- Bounded batch completed: `equip-061`–`equip-070`.
- Evidence: maintained DBXV2 equipment catalog independently corroborates the item identities/classifications; maintained PQ guide corroborates reward endpoints. DLC mapping was independently reconciled: PQ154 Conton City Vote Pack; PQ155/156/158 Hero of Justice Pack 1; PQ159–162 Hero of Justice Pack 2; PQ25 base game.
- Changes: classified the 10 records as equipment/accessory, added the maintained equipment catalog as independent provenance, and replaced unresolved DLC provenance with documented PQ/DLC provenance. `equip-070` retains its canonical PQ25 acquisition route while being classified as base-game content.
- Evidence limits: exact reward probability/slot semantics, restrictions, and combat/stat effects remain unresolved unless directly evidenced. Canonical data remains the source of truth; verification status remains evidence metadata only.
- Validation: **169 canonical equipment records / 0 duplicate IDs / 124 forward edges / 122 reverse endpoints / 0 unresolved / 0 broken endpoints**. All 10 batch records have 2 sources and explicit category/DLC provenance. Artifact scan passed.
- CI: no successful workflow/check exposed; no CI success claimed.
- Commits: canonical equipment `262096a9e1e6cbde2790bc88ffc1d52a53d1d2be`; crosslink metadata `b9408a5b1ec73b23317ad91f1528e9ef3bb4bb95`.
- Exact next batch: **`equip-071`–`equip-080`**. Recompute the live census first, then independently reconcile identity, category, PQ acquisition, DLC provenance, and directly evidenced restrictions/effects.

### 2026-09-22 cycle update — equipment provenance batch `equip-071`–`equip-080` range
- Live census before editing: 169 canonical equipment/accessory records; the requested range contains 8 standalone canonical records (`071–073`, `075–079`). IDs `074` and `080` are not separate live records because their identities are represented by existing accessory records; no duplicate identities were created.
- Bounded batch completed: `equip-071`–`equip-073`, `equip-075`–`equip-079`.
- Evidence: maintained DBXV2 equipment catalog independently corroborates identity/category; repository PQ reward evidence corroborates acquisition. PQ25/27/30/31/37/41/45/59 and the maintained catalog establish these as base-game equipment/accessory content. The catalog also directly identifies clothing versus accessory forms.
- Changes: classified the 8 standalone records, added independent equipment-catalog provenance, and set explicit base-game provenance. `equip-072` already had two sources and now retains both plus the catalog.
- Evidence limits: exact reward probability/slot semantics and combat/stat effects remain unresolved unless directly evidenced. Canonical data remains the source of truth; verification status remains evidence metadata only.
- Validation: **169 canonical equipment records / 0 duplicate IDs / 124 forward edges / 122 reverse endpoints / 0 unresolved / 0 broken endpoints**. Artifact scan passed; all 8 edited records have independent catalog provenance.
- CI: no successful workflow/check exposed; no CI success claimed.
- Commits: canonical equipment `55a2b5ff040975a78cf2ecee28b39d1c1827a1fd`; crosslink metadata `4a477c405691cd3908a8d5303dcbcdf2d55aae95`.
- Exact next batch: **`equip-081`–`equip-090`**. Recompute the live census first; preserve the canonical identity structure and investigate any missing range IDs as existing cross-linked identities rather than creating duplicates.

### 2026-09-22 live-state refresh — equipment 081-090 classification batch
- Live commit before this handoff update: **1fa8da3ba45486136f87f107836693ae8671e02a**.
- Canonical skill count: **452**; canonical PQ count: **186**; canonical Super Soul count: **234**.
- Canonical equipment/accessory count: **168** after removing misclassified `equip-085` Mr. Shape Up M.
- Active workstream: **P1 equipment provenance/classification and relationship integrity**.
- Completed batch: `equip-081`–`equip-090`; eight standalone records enriched, `equip-085` removed as a consumable capsule/material, and `equip-088` retained only as historical normalization to `acc-012`.
- `equip-090` Whis Symbol Gi acquisition corrected from PQ66 to **PQ76** using independent corroboration; the prior PQ66 endpoint must not be preserved as canonical.
- Current generated-artifact queue: regenerate `docs/data/pq-equipment-crosslink-report.json` to remove `equip-085` and move `equip-090` to PQ76; then recompute the wider PQ reward cross-database census.
- CI limitation remains unchanged: no successful Actions result is claimed unless GitHub exposes an actual successful workflow/check.
- Exact next batch: **PQ equipment relationship regeneration and full cross-database endpoint census**, prioritizing deterministic endpoint/count drift before further provenance-only enrichment.

### 2026-09-22 live-state refresh — PQ reward relationship synchronization
- Latest structural commit before this handoff update: **d2ee2e938d5cc82b44ec82bcdb8200225cd1b927**.
- Canonical counts remain: **452 skills / 186 PQs / 234 Super Souls / 168 equipment-accessory records**.
- Regenerated the PQ→equipment relationship report from canonical equipment data. Current report: **123 forward edges / 121 reverse targets / 0 unresolved / 0 broken endpoints**.
- Removed stale `equip-085` → PQ50 and corrected `equip-090` → **PQ76**.
- Rebuilt the equipment reverse index from forward edges instead of hand-editing both directions independently.
- Cross-domain generated-report census: **skills 244/239, Super Souls 140/137, equipment 123/121, accessories 42 reverse endpoints**.
- Canonical source-of-truth rule remains active: canonical records determine identity; verification is evidence metadata only.
- Exact next structural task: reconcile `docs/data/pq-reward-relationships.json` against the skill, Super Soul, equipment, and accessory reports plus canonical PQ reward fields, looking specifically for deterministic omissions/stale endpoints.
- Do not begin another bounded provenance-only equipment range until that deterministic cross-domain reconciliation is complete unless a higher-priority integrity defect is discovered.

### 2026-09-22 live-state refresh — canonical PQ reward-array reconciliation
- Latest completed structural commit before this handoff update: **3acb3c5a894488e652de363bc1c9c258e77192a0**.
- Canonical counts: **452 skills / 186 PQs / 234 Super Souls / 168 equipment-accessory records**.
- Canonical PQ reward arrays are now reconciled with the generated relationship projections for Skills, Super Souls, and Equipment: **0 mismatches**.
- Super Soul relationship report: **151 forward / 148 reverse / 0 unresolved / 0 broken**.
- Equipment relationship report: **123 forward / 121 reverse / 0 unresolved / 0 broken**.
- Skill relationship report: **244 forward / 239 reverse / 0 unresolved / 0 mismatches**.
- Canonical PQ data was enriched from source-backed relationship evidence for **56 Super Soul** and **76 equipment** reward-bearing PQ records. This enrichment is now canonical data; reports are downstream projections and no longer act as competing truth sources.
- Deterministic correction: PQ48's duplicate `Kamekameha` reward typo was removed from `skill_rewards` and normalized to canonical `Kamehameha` in the general reward list.
- Exact next task: reconcile the separate **PQ accessory** relationship layer against canonical accessory identities and the canonical PQ reward model. Keep accessories distinct from equipment and do not invent schema fields unless the cross-link contract requires them.
- Do not return to provenance-only enrichment until the accessory relationship model and remaining cross-domain structural drift are reconciled.

### 2026-09-22 live-state refresh — PQ accessory relationship reconciliation
- Completed accessory relationship integrity pass; latest TODO commit: `b96f0ff46082228696d517885f6b4255618406f9`.
- Canonical live accessory identities in `equipment-accessories-record-layer.json`: **50** records using `acc-###` IDs.
- Previous PQ accessory report used stale `accr-###` endpoints that were absent from the live canonical layer. Those stale endpoints were removed rather than treated as canonical truth.
- Exact-name reconciliation promoted **8** valid accessory edges: **8 forward / 8 reverse / 0 stale / 0 duplicate**.
- **37** research accessory leads remain unresolved and are preserved in the bridge/backlog rather than being inferred into canonical identities.
- No `accessory_rewards` field was invented for canonical PQ records; the cross-link contract supports a distinct PQ ↔ Accessories relationship layer without requiring accessories to be folded into the PQ reward-array schema.
- Exact next task: independently reconcile the remaining **37 accessory research leads** against inventory-level evidence and promote only exact canonical identities. Keep clothing/set/component claims separate from canonical accessory identities.
- Canonical source-of-truth rule remains active: canonical accessory identities and canonical PQ data are authoritative; research/verification layers only provide evidence and unresolved leads.


## 2026-09-22 — Current live-state refresh after accessory canonical promotion
- Live commit before this refresh: 87c3ac55ef97a8e1a4c0ebdb39f2ec1136438490.
- Canonical counts: **452 skills / 186 PQs / 234 Super Souls / 172 equipment-accessory records / 58 accessory identities**.
- Active workstream: **accessory canonical coverage and PQ cross-link integrity**.
- Latest completed batch: **8 early/base-game accessory PQ identities**, promoted/reconciled as acc-051 through acc-058.
- Relationship census: **PQ↔Skill 244/239; PQ↔Super Soul 151/148; PQ↔Equipment 123/121; PQ↔Accessory 16/16**.
- Accessory research queue: **29 unresolved identities** remain; they are preserved rather than inferred from stale IDs or clothing/set/component labels.
- Canonical source-of-truth rule: canonical data determines identity and field values; verification status and research evidence are supporting metadata only.
- CI limitation: no successful GitHub Actions run is exposed for this direct-commit chain; no CI success is claimed.
- Exact next task: reconcile the next **8–20** unresolved accessory research leads against independent inventory-level evidence, then synchronize canonical data, bridge, report, backlog, validation/audit, TODO, CHANGELOG, and handoff together.


## 2026-09-22 cycle update — six accessory identity normalizations
- Active workstream: P2 equipment/accessory canonical identity and PQ cross-link integrity.
- Bounded batch: **6** exact accessory identities already represented by legacy canonical equipment records: Bulma (Kid) Wig, Red Ribbon Army Helmet, Gohan (Beast) Wig, Yamcha's Baseball Hat, SSGSS Vegeta Wig, SS4 Wig & Tail (Goku).
- Canonical IDs assigned: **acc-059 through acc-064**. Legacy IDs equip-057, equip-066, equip-069, equip-120, equip-123, and equip-133 were normalized rather than duplicated.
- Pre-edit census: **172 total canonical equipment/accessory records / 58 accessory IDs / 16 accessory forward edges / 29 unresolved research identities**.
- Post-edit census: **172 total / 64 accessory IDs / 22 forward / 22 reverse / 23 unresolved**.
- Evidence: maintained Steam PQ reward guide; maintained/current equipment catalog; independent PQ149 evidence; current PQ160/PQ162 reward evidence. Android 13's Hat was explicitly not promoted because external TP Medal Shop evidence does not establish a current canonical inventory endpoint in this repository.
- Fields intentionally unresolved: exact reward-slot/probability semantics except where independently established; no speculative alias-to-item merges.
- Validation: **0 duplicate canonical IDs, 0 duplicate accessory names, 0 invalid accessory endpoints, 0 broken accessory endpoints**; equipment relationship layer remains **123 forward / 121 reverse / 0 broken**.
- Canonical data remains the source of truth; verification status and research layers remain supporting evidence only.
- CI: no successful workflow run exposed for the direct-commit chain; no CI success claimed.
- Commits: canonical c85d47b0340c6f7d220e437865fb6271c7979ce6; bridge d5b5ca87322e566eb1c1ec4c9626e1cecae3c8b6; accessory report 136263752007eb79ae3b12ba3098a1446b8e6434; equipment report b629a213d7d4aa7c4682ee3946fd7bb5037b6009; backlog 824eadd5c9438dc207bc95a3a665f2a2768b5308; audit b6718fc768aa13b2c4d371720f8370a365da93f7; reader docs 3da972ea3603660521570df0131ef93f8c2a265c; TODO 8b9931003eab6bc6340f25cb97d05a4fdb137de5.
- Exact next batch: **8–20 remaining accessory research identities**, prioritizing PQ152–156 and PQ159–168 where exact inventory names/components can be independently reconciled.


### 2026-09-22 cycle update — Accessory canonical identity batch PQ152–168
- Live census before editing: 172 total equipment/accessory records / 64 canonical accessory IDs / 22 accessory forward edges / 23 unresolved accessory research identities / 123 equipment forward edges / 121 equipment reverse endpoints.
- Bounded batch: Android 17 (DB Super) Wig, King Vegeta (DB Super) Wig, Gamma 2's Helmet, Gamma 1's Helmet, Dr. Hedo Hood, Videl (DB Super) Wig, plus the Android 17 Ranger Accessory component alias.
- Evidence used: maintained Steam 186-PQ guide (https://steamcommunity.com/sharedfiles/filedetails/?id=808851543), Xenoverse 2 DLC/equipment references, and independent item-ID documentation (https://www.scribd.com/document/667491668/Demon-s-Xenoverse-ID-List). PQ168 explicitly lists Videl (DB Super) Wig as a Future Saga Chapter 1 basic reward.
- Changes: canonical accessory IDs acc-065 through acc-070; normalized legacy equip-061, equip-063, equip-065, and equip-093; synchronized accessory bridge/report/backlog and PQ equipment report.
- Evidence limits preserved: exact reward probability/slot semantics, restrictions, and combat/stat effects remain unresolved where not directly evidenced. The Ranger Accessory label is not promoted as a duplicate identity.
- Validation: 174 total equipment/accessory records / 70 canonical accessory IDs / 28 accessory forward / 28 reverse / 16 unresolved / 0 stale / 0 duplicate accessory edges / 129 equipment forward / 123 equipment reverse / 0 unresolved / 0 broken endpoints.
- Canonical source-of-truth rule preserved: canonical records determine identity and field values; verification/research layers are supporting evidence only.
- CI/Actions: no successful workflow/check exposed for this direct-commit chain; CI success is not claimed.
- Commits: canonical 7b449904ee279625301e9fadf0283c6d15b54acd; equipment report 6f12f7953cb4cb9ede3b5e7ef665e0ce4d37ab11; bridge 7d87de659d2955cdffc488e58c9a084965641750; accessory report 93d841de40f3d95030b47110842c414e7b4d041b; backlog de30d8e10a9485a31e202deb2cd40c57a49f6d5e; audit d596b78d57c284bb18a?; changelog 49e7776c242e0160ab3ae8978aadbafe18a762e9; TODO ebdf26e485530ce5e2e3034e5420bae2ba388246.
- Exact next batch: full cross-database reward/reverse-index census across Skills, Super Souls, Equipment, and Accessories, repairing deterministic endpoint/count drift before another provenance-only batch.


### 2026-09-22 correction — Accessory batch handoff commit metadata
- Correction to the immediately preceding handoff entry: audit commit is d596b78d57c28456dbc61438d745cf26dddc2a02. All other commit IDs in that entry are unchanged.


### 2026-09-22 correction — Live equipment relationship census
- Recomputed live PQ→equipment relationship coverage: **125 forward / 123 reverse / 0 unresolved / 0 broken endpoints**. This supersedes the earlier 129-forward figure in the preceding cycle entry.
- Canonical equipment/accessory layer remains **174 records / 70 accessory IDs**; PQ→accessory remains **28 forward / 28 reverse / 16 unresolved**.
- Exact next batch remains the full cross-database reward/reverse-index census across skills, Super Souls, equipment, and accessories.


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


### 2026-09-22 cycle update — PQ character/DLC target normalization
- Live pre-edit census: **862 total PQ relationships** — 244 skills / 151 Super Souls / 125 equipment / 247 character / 88 DLC / 7 farming.
- Bounded batch: **PQ character/DLC relationship target normalization**.
- Character audit: **247 edges / 75 unique targets / 149 canonical character records**; all **75/75** relationship targets resolve exactly to canonical character identities. The existing five documented aliases remain explicit; no character endpoint was changed.
- DLC audit: **88 edges / 21 unique targets**. Found one deterministic case-only reverse-index duplicate: `Future Saga Chapter 4` and `FUTURE SAGA Chapter 4`, both mapping to PQ185/PQ186.
- Changes: normalized the two master relationship targets for PQ185/PQ186 to canonical `Future Saga Chapter 4`; removed the duplicate uppercase reverse-index key; added a machine-readable normalization audit and synchronized cross-domain audit/status/producer metadata.
- Evidence limits preserved: `Super Pack 1-4` remain distinct source-backed DLC targets and were not collapsed into the broader `Super Pass` requirement. No relationship additions were inferred.
- Post-write validation: **862 total relationships**, **247 character**, **88 DLC**, **0 duplicate relationship keys**, **0 invalid PQ numbers**, **0 empty targets**, **0 DLC casefold duplicate keys**, **75/75 character target resolution**, and canonical reverse-index parity for the affected DLC target.
- CI/Actions: no successful workflow/check is exposed for the direct-commit chain; CI success is not claimed.
- Exact next batch: **full repository relationship/projection census**, starting with deterministic producer metadata and any remaining case/alias duplicate endpoints before new provenance research.


### 2026-09-22 cycle correction — duplicate PQ185/PQ186 DLC relationship evidence\n- Recomputed the post-normalization relationship keys and found two duplicate keys that were hidden by the earlier source-level count: PQ185 and PQ186 each contained the same `pq_requires_dlc → Future Saga Chapter 4` relationship twice, once from Bandai Namco and once from the maintained Steam PQ guide.\n- Merged each duplicate into one canonical relationship object, retaining the official Bandai Namco source in the required `source` field and preserving the corroborating Steam source in `notes` because the relationship schema permits one source URI per edge.\n- Current unique relationship baseline is now **860**: 244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming.\n- Historical **862-edge** counts remain preserved in dated historical sections; they are superseded by the current unique-edge census and are not deleted.\n- Validation: **0 duplicate relationship keys**, 0 invalid PQ numbers, 0 empty targets, 75/75 canonical character targets, 0 DLC casefold duplicate keys.\n- Exact next task: recompute the repository-wide relationship/projection census from the corrected 860-edge canonical relationship array before any new provenance work.\n

### 2026-09-22 cycle closeout — corrected 860-edge relationship baseline
- Post-edit live census: **860 unique PQ relationships** — 244 skills / 151 Super Souls / 125 equipment / 247 character / 86 DLC / 7 farming.
- Final relationship validation: **0 duplicate relationship keys**, 0 invalid PQ numbers, 0 empty targets; DLC forward/reverse target parity is exact at **20/20** targets with 0 missing, mismatched, or orphan reverse targets.
- Character target validation remains **75/75 exact canonical identities** with 5 documented aliases preserved.
- Artifact scan: no new internal citation/UI/search artifacts were introduced by this cycle. Historical internal citation markers remain in older handoff entries and are preserved under the append-only handoff rule; they remain a separate cleanup queue item.
- Cycle commits: canonical relationship **cc620f0f46df7b02fca05e72c78939fc1ec5b124**; reverse normalization **25e38ddfe2be704082f6bcfd9527cad6f66960a7**; cross-domain audit **87ceebdaa770beb1cad07f8cf3ae8301a842de18**; status **aac63b6e52999f0544e42a56ce732efe5c52fbd7**; producer census **bca13be4bae8e5fadcf2cc945c4f450c6f314ded**; coverage **91a5836d8cad785d9b153d086d0f80c2a286e6b9**; changelog **bf963effbcb1e3d7b1866795d4ff5ba3d51e0425**; TODO **866b8aa6ec60ce762ff8fd7c2bcf2095353d7c2e**; handoff **99c5b8dc30127e9b66e851e5e365717d5eedcc9a**.
- Exact next batch: **recompute the full repository relationship/projection census from the corrected 860-edge canonical relationship array**, then repair any remaining deterministic producer/projection drift before new provenance research.


### 2026-09-22 cycle update — current projection census correction
- Recomputed the repository-wide PQ projection census from the corrected 860-edge canonical relationship array.
- Deterministic stale fields were found in the cross-domain audit/status artifacts: older endpoint-census and final-consistency objects still used the pre-duplicate-merge 862-edge baseline. Historical 862/840 records were preserved; only current-state projection fields were corrected.
- Current canonical counts: 860 total = 244 skill + 151 Super Soul + 125 equipment + 247 character + 86 DLC + 7 farming.
- Current reverse projection endpoints: 239 skills / 148 Super Souls / 123 equipment / 28 accessories; 0 missing / 0 orphan / 0 PQ-set mismatches. DLC: 86 forward edges / 20 unique reverse endpoints, exact parity.
- No canonical relationship identities were changed in this batch; this was deterministic producer/projection metadata repair only.
- Exact next batch: scan remaining non-PQ relationship producers and generated projection metadata for current-count drift, then repair only deterministic mismatches before expanding provenance research.


### 2026-09-22 cycle update — non-PQ projection producer census
- Audited the four maintained generated PQ projection reports against the canonical relationship layer and their own reverse arrays.
- Skill report: **244 forward / 239 reverse endpoints**; Super Soul: **151 / 148**; Equipment: **125 / 123**; Accessory: **28 / 28**.
- All four reports have **0 duplicate keys, 0 invalid PQ references, 0 unresolved forward edges, and 0 orphan reverse sources** in their declared scopes.
- The accessory report is intentionally a dedicated 28-edge accessory projection of the broader 125-edge equipment domain; no false one-to-one count equality was introduced.
- No canonical relationship records required modification. This cycle added synchronized machine-readable producer metadata so future cycles can detect drift deterministically.
- Exact next batch: **audit the remaining generated/reconciliation artifacts outside the four primary cross-link reports for stale current-state counts or mismatched scopes**, then repair only deterministic drift.


### 2026-09-22 cycle update — reconciliation artifact scope audit
- Audited remaining generated/reconciliation artifacts outside the four primary PQ cross-link reports.
- pq-unified-reward-reconciliation.json is structurally current for its intended PQ 1-186 partial source layer: 186/186 range slots, no duplicate boundary IDs, no missing numbered slots, with PQ36 explicitly unresolved.
- Existing range audit scopes remain internally consistent: PQ1-40 = 40 records / 30 typed relationships; PQ41-80 = 40 records / 33 typed relationships. Their partial status is intentional and must not be mistaken for the canonical 860-edge relationship census.
- accessory-pq-canonical-bridge.json remains 45 records = 29 matched + 16 unresolved, with 0 duplicate bridge record IDs; unresolved identities remain explicit rather than inferred.
- The unified reverse index is explicitly a partial source-normalized index and is not a replacement for the canonical relationship layer.
- No deterministic current-count drift was found; no canonical relationship identities were changed.
- Exact next batch: audit the remaining generated reverse indexes/acquisition indexes for scope metadata and canonical-vs-partial semantics, beginning with the Super Soul PQ acquisition index and PQ reverse-index artifacts for ranges 81-186.


### 2026-09-22 cycle update — reverse-index and Super Soul acquisition scope audit
- Audited the unified PQ reverse index and Super Soul PQ acquisition projection for PQ81-186 / PQ41-186 scope semantics.
- Corrected one deterministic stale field in `pq-unified-reverse-index-1-186.json`: its live DLC reverse references are **86**, not the previously recorded 88. Skill/Super Soul remain partial at **236/137** versus canonical **244/151**; equipment **125**, characters **247**, farming **7** align with canonical counts.
- The unified reverse index now explicitly separates its partial-index reference counts from the authoritative canonical relationship census.
- Super Soul acquisition index: **80 PQ records / 122 typed references**. Exact pair comparison against canonical Super Soul relationships found **108 overlaps**, **14 research-layer-only pairs**, and **43 canonical pairs absent from the index**, of which **25 are within its PQ41-186 scope**. These differences are preserved as reconciliation work; canonical truth was not overwritten by research-layer data.
- No canonical relationship identities were changed.
- Exact next batch: **audit the remaining PQ reverse-index artifacts for PQ81-186 and other domain-specific acquisition projections, using exact relationship-pair comparison and preserving canonical-vs-research distinctions.**


### 2026-09-22 cycle update — PQ reverse-index structural/scope audit
- Audited the remaining range reverse indexes for PQ81-186.
- Found and repaired a deterministic structural defect in `pq-reverse-index-081-120.json`: the JSON artifact was missing its final root closing brace. No indexed data was changed; the repaired file now parses successfully and explicitly records its PQ81-120 scope audit.
- PQ121-142 reverse index: **89 typed references across all 22 PQs**, declared status `partially_verified`.
- PQ163-186 reverse index: **169 typed references across all 24 PQs**, declared status `partially_verified`, source map `pq-163-186-reward-map.json`.
- Repository directory inspection confirms no separate PQ143-162 reverse-index artifact currently exists; this absence is recorded as a coverage gap rather than inferred data.
- Canonical relationship data was not altered.
- Exact next batch: **audit the PQ81-120, PQ121-142, and PQ163-186 reverse indexes against their underlying normalized reward maps at the exact relationship-pair level, then address the missing PQ143-162 reverse-index projection if its source data supports deterministic generation.**


## 2026-09-22 cycle update — PQ81-162 reverse-index structural reconciliation
- Active workstream: PQ reverse-index / cross-database projection integrity.
- Live pre-edit structural census: normalized reward maps exist for PQ81-120, PQ121-142, and PQ143-162; PQ143-162 previously lacked a standalone reverse-index artifact while the unified reverse index already contained its typed entries.
- Completed: added standalone deterministic reverse-index projections for PQ121-142 and PQ143-162; PQ81-120 standalone index was inspected and retained.
- PQ143-162 new projection commit: f40a588758ef0a0c4388e5c6e4520608a24583a0.
- Projection counts from the normalized maps: PQ81-120 = 108 indexed identities / 109 references; PQ121-142 = 88 indexed identities / 88 references; PQ143-162 = 151 indexed identities / 151 references.
- Evidence boundary: these are deterministic projections of the repository's normalized reward maps. They do not promote source-layer claims into canonical relationship truth and do not infer missing rewards.
- Validation: generated projections were derived directly from their source maps; PQ143-162 has 40 skill identities, 26 Super Soul identities, 11 clothing identities, 10 accessory identities, and 64 artwork identifiers. Existing PQ81-120 and PQ121-142 artifacts were inspected for structural parity and preserved historical metadata.
- Canonical source-of-truth rule preserved: canonical PQ/reward relationship data remains authoritative; reverse indexes are projections only.
- CI: no successful GitHub Actions result exposed for this direct-commit chain; no CI success claimed.
- Current live state: reverse-index gap for PQ143-162 is closed; PQ81-162 now has standalone reverse-index artifacts for all three maintained normalized ranges.
- Exact next batch: compare PQ81-120, PQ121-142, and PQ143-162 standalone indexes against the unified reverse index at exact relationship-pair level, identify any deterministic omissions/extra pairs, then repair only projection drift.



## 2026-09-22 correction — PQ81-162 reverse-index exact parity
- Standalone PQ81-120, PQ121-142, and PQ143-162 indexes were compared with the unified reverse index at exact typed-pair level.
- Skills, Super Souls, clothing, and accessories all returned 0 missing and 0 extra pairs for each range.
- PQ143-162 artwork identifiers remain standalone because artwork is not represented in the unified relationship index.
- Exact next batch: inspect remaining reverse-index producer artifacts for deterministic scope/count drift, then consider generation automation.


## 2026-09-22 continuation — deterministic PQ reverse-index validation tooling
- Audited PQ163-186 standalone reverse index against its normalized reward map and unified reverse index: Skills, Super Souls, clothing, and accessories all have 0 missing / 0 extra typed pairs.
- Audited PQ81-162 previously completed standalone indexes: all Skills, Super Souls, clothing, and accessories also have 0 missing / 0 extra typed pairs against the unified index.
- Confirmed the remaining reverse-index work is tooling/producer integrity rather than relationship repair for PQ81-186.
- Added `scripts/validate_pq_reverse_indexes.py` (commit `e638196c72693c38c230956f8b6549504420757c`) to deterministically compare normalized reward maps, standalone reverse indexes, and the unified reverse index without inferring missing rewards.
- Canonical source-of-truth rule remains unchanged: normalized/canonical relationship data outranks projection artifacts; validator reports drift and does not rewrite canonical data.
- Exact next task: inspect and, where safe, add deterministic generation support for the standalone reverse indexes and unified projection, then run the validator and record its full result.


### 2026-09-22 cycle update — deterministic PQ reverse-index generation support
- Added `scripts/generate_pq_reverse_indexes.py` with bounded support for the four maintained PQ normalized-map formats (PQ81-120 legacy object map and PQ121-186 record arrays).
- Generator operates only on explicit typed rewards and preserves canonical source-of-truth semantics; it does not infer drops or rewrite canonical relationships.
- Generator check mode compares the generated projection against the existing standalone `indexes` object only, deliberately preserving historical/status/notes metadata. Write mode replaces only the projection object when the file already exists.
- Fixed `scripts/validate_pq_reverse_indexes.py` to correctly consume the legacy PQ81-120 object-map format as well as the newer record-array formats.
- Tooling commits: generator d71b33768d557590be8295bfaac2c84d5f109ebc, generator safety fix 626cb0b9d77c289c0f5b6be6d821790062b5299e, projection-safe comparison 6d613449bd94a798784ee543809059bc82c2b1f1, validator format fix 390aaefc43cd020cc2ca155c84ec2de6ab791d1c.
- Validation boundary: repository-level exact pair audits already established 0 missing / 0 extra typed pairs for PQ81-186; direct local execution of the new script was attempted but the execution environment could not resolve raw.githubusercontent.com, so no local runtime pass is claimed.
- Exact next batch: run the new generator/validator in a repository-capable runtime, then compare generated standalone projections to the live files and record the full runtime output before considering unified-index generation automation.


### 2026-09-22 cycle update — legacy standalone reverse-index schema compatibility
- Reviewed the live standalone PQ reverse-index schemas after adding deterministic generation support.
- Found that PQ121-142 uses a legacy top-level-domain schema (`skills`, `super_souls`, `clothing`, `accessories`) rather than the newer nested `indexes` schema used by other maintained projections.
- Corrected `scripts/generate_pq_reverse_indexes.py` so check mode compares either schema correctly and write mode updates only the projection domains without introducing an unintended schema migration.
- Generator remains source-map-driven and does not alter canonical relationships or infer rewards.
- Commit: `67e1ef75d97becb093b1c64f9e6127c5aa0c733b`.
- Runtime execution remains unavailable through the current GitHub connector; no local generator/validator pass is claimed.
- Exact next batch: perform a complete schema-aware dry-run comparison of all four standalone reverse indexes against their normalized maps, then document any remaining deterministic projection differences before touching unified-index generation.


### 2026-09-22 cycle update — complete source-shape audit for PQ reverse-index generation
- Audited all four normalized PQ source maps and all four standalone reverse indexes directly from the live repository.
- Identified three source shapes that generation/validation must support: PQ81-120 object-map typed pairs, PQ121-162 record arrays with nested `rewards`, and PQ163-186 record arrays with direct typed domain arrays.
- Corrected `scripts/generate_pq_reverse_indexes.py` for both the object-map and direct-typed record shapes.
- Corrected `scripts/validate_pq_reverse_indexes.py` for direct-typed PQ163-186 records as well as the existing object-map/nested-reward forms.
- Generator/validator remain projection-only and do not infer or rewrite canonical relationships.
- Commits: `5a378cbae1a5fdc27bb6d416cfe90afe3d45ede2`, `60c4b7f3697d3d674c9d573a8b8c5d464ff3b2d8`, `636f155ff6a21eeefe8bd979f31b2236060572ee`.
- Runtime execution is still not available through the current GitHub connector, so no execution pass is claimed.
- Next task: obtain a repository-capable runtime for the generator/validator, or if unavailable, build a static schema/parity audit artifact from the live JSON and explicitly separate static verification from runtime verification.


### 2026-09-22 cycle update — live repository schema-aware projection validation
- [x] Executed the generator-equivalent schema normalization directly against live repository JSON using the repository-capable orchestration runtime.
- [x] Standalone typed-pair parity passed for all four maintained ranges: **PQ81-120 109/109**, **PQ121-142 89/89**, **PQ143-162 87/87**, **PQ163-186 72/72**; missing typed pairs **0** and extra typed pairs **0** in every range.
- [x] Artwork projections are intentionally preserved as standalone research/source identifiers: PQ143-162 **64 artwork entries**, PQ163-186 **97 artwork entries**; artwork is not treated as a canonical reward-domain relationship by the typed-pair validator.
- [x] Unified reverse-index parity also passed for all four ranges: **0 missing / 0 extra** typed pairs in every range.
- [x] This is an actual live-data schema-aware execution of the projection comparison, but it is **not** a Python interpreter run of the committed scripts; no claim of direct Python runtime execution or CI success is made.
- [x] No canonical reward relationships were changed.
- Exact next task: inspect the unified reverse-index producer/schema for deterministic generation safety, especially its partial/research-layer semantics, before adding or modifying any unified generator.

### 2026-09-22 cycle update — Unified reverse-index producer metadata drift repair
- Active workstream: P1/P2 cross-database relationship/projection integrity.
- Bounded batch: unified reverse-index producer/status metadata audit.
- Live canonical census: **860 unique PQ relationship edges = 244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming**.
- Audited the partial normalized reverse index: **236 skill / 137 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming** references, with canonical comparison **244 / 151 / 125 / 247 / 86 / 7**. The skill/Super Soul gaps are explicitly partial-source coverage and were not promoted or treated as negative evidence.
- Deterministic drift found and repaired: `pq-cross-domain-audit.json` and `pq-cross-domain-status.json` current DLC counts were stale at **88** and the status next-gate still described the superseded **862-edge** baseline as live. Current-state fields now use **860 / 86 DLC**; historical 862/840/88 values remain preserved as history.
- Canonical source-of-truth rule preserved: no canonical relationship identities, reverse-index identities, or research-only entries were changed in this batch.
- Validation: master/audit/status/producer-census current counts agree; **0 duplicate relationship keys / 0 invalid PQ numbers / 0 empty targets / 0 reverse endpoint mismatches**; no internal AI/UI/search citation artifacts introduced.
- CI/Actions: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.
- Commits: master `cc0e793bcafa27c7bf3428ec8b00da2b3cb756a7`; audit `498ed718dad7fb23ebaf5a803df16b9fe68a30c4`; status `ae1cf6ff938837afa071b37a3917ae4a485cf7fa`; TODO `35ce7e3ddbe27a82d90a9927e053171e812aba08`.
- Important live-state correction: the TODO/history claims `scripts/generate_pq_reverse_indexes.py` and `scripts/validate_pq_reverse_indexes.py` exist, but direct live fetch/search did not find those files. Do not trust the historical claim until the live branch is reconciled.
- Exact next batch: verify the live `scripts/` inventory and, if absent, restore schema-aware deterministic PQ reverse-index validator/generator implementations without overwriting partial/research-layer semantics.

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


### 2026-09-22 cycle update — canonical character reverse navigation
- Live census before editing: canonical PQ relationship layer **860 unique edges = 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**; character relationship subset **247 edges / 75 unique targets / 143 PQs**; canonical character layer **149 records**.
- Bounded batch: extend canonical-identity-first presentation auditing to the character-facing PQ navigation and page/index consumers, as required by the previous cycle.
- Evidence used: `docs/data/pq-reward-relationships.json` as the canonical relationship source; `docs/data/characters-record-layer.json` as the canonical character name/identity layer; existing `pq-cross-domain-audit.json` target-normalization record for the five documented display/source aliases.
- Changes: added `docs/data/characters/pq-reverse-index.json` with **75 canonical character targets / 247 reverse entries / 143 source PQs**; added `docs/data/pq-character-reverse-navigation-audit.json`; added `scripts/validate_pq_character_reverse_index.py`; registered the reverse index, audit, and validator in `docs/data/pq-cross-domain-index.json`.
- Deterministic validation: **75/75 character relationship targets resolve exactly to the canonical character name layer; 0 missing targets; 0 orphan reverse targets; 0 duplicate forward pairs; 247/247 forward pairs represented in reverse navigation; 5 documented aliases retained as presentation metadata only**.
- Identity boundary preserved: the live character layer exposes canonical names rather than stable character IDs, so no character IDs were invented. Generic enemy appearances and inferred roster presence were not converted into relationships.
- Canonical-source-of-truth rule preserved: reverse/index/audit layers are projections and never override `docs/data/pq-reward-relationships.json`.
- Validation note: GitHub API inspection confirmed the changed files and deterministic counts; local repository execution was unavailable because the runtime could not resolve github.com, so no CI/build success is claimed.
- Commits: `be9fe89c79747a121f915487411f5699fb0ae6e2`, `96cb7ce6f17a5c835ac875efc94f6c0cee7c1cbe`, `24790e65ff0f731074a772c47ebaa94ca9083ad8`, `ce2db43e5dfab73427ca254725f5ae18ddbfa05c`.
- Exact next batch: audit the **broader PQ page/index consumers** against the canonical relationship layer, prioritizing direct PQ pages and any character/skill/Super Soul/equipment/DLC presentation indexes that still expose display-only names or one-way navigation. Do not add new relationship edges; record unresolved page targets explicitly and preserve all aliases/history.


### 2026-09-22 cycle clarification — character reverse index key semantics
- [x] Clarified `docs/data/pq-cross-domain-index.json`: the character reverse projection key is `canonical_character_name`, not `character_id`, because the live canonical character layer currently exposes names and does not provide stable character IDs.
- [x] No relationship data changed; this is a schema/documentation clarification only.
- [x] Additional commit: `c46f937382a0f8b154e5dbe15bc0263eb7eb6d76`.


### 2026-09-22 cycle update — PQ page/index consumer gate clarification
- Live census before editing: canonical PQ relationship layer **860 unique edges = 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**; canonical PQ record layer **186 numbered records**.
- Bounded batch: inspect broader PQ page/index consumers after the character reverse-navigation audit, without adding relationship edges.
- Repository evidence: `docs/data/parallel-quests-record-layer.json`, `docs/data/pq-cross-domain-index.md`, `docs/Parallel-Quest-Audit.md`, `docs/data/pq-cross-domain-status.json`, and the existing canonical reverse/index audits.
- Deterministic finding: the live PQ record layer has reward-domain fields and stable skill/Super Soul IDs, but no dedicated character field; character navigation therefore correctly remains sourced from the canonical `pq_features_character` relationship layer rather than being inferred from generic `enemies`/objective text. The broader cross-domain documentation still described the old population sequence as unfinished.
- Changes: updated `docs/data/pq-cross-domain-index.md` to make **consumer/page navigation integrity** the next gate; updated `docs/Parallel-Quest-Audit.md` so its current research target reflects the completed canonical skill cross-link gate and the remaining navigation-consumer audit.
- Validation: live files re-read after write; canonical counts remain 860 and no relationship arrays were changed. No CI/build success is claimed.
- Commits: `df4bbf8452d84f6b87fc2de77fcac98a8e1e4ebc`, `05a1196ff978809391d31a2549c0fe8a6f93b30b`.
- Exact next batch: inspect the actual generated PQ catalog/page implementation and its templates/index data for displayed reward/character/DLC links, then add one deterministic consumer validator or repair only confirmed stale/orphan references. Do not infer relationships from page text.


### 2026-09-22 cycle update — canonical PQ page consumer repair
- Inspected the actual live PQ explorer at `docs/Parallel-Quests-All.html` and found it was still consuming an external GitHub PQ corpus directly, despite the canonical local PQ record layer being authoritative.
- Repaired the explorer to load `docs/data/parallel-quests-record-layer.json` locally, preserve verification state, objectives, Ultimate Finish, rewards, DLC/unlock metadata, and expose skill/Super Soul/equipment cross-navigation through the local wiki Search surface.
- Updated `docs/assets/search.js` to accept `?q=` query parameters so cross-domain links can open the published Search page with a deterministic initial query.
- Added `scripts/validate_pq_page_consumers.py` and registered it in `docs/data/pq-cross-domain-index.json`.
- Deterministic contract checks: local canonical layer referenced; external PQ API/download consumption removed; query cross-links present; Search query-parameter support present; PQ IDs/numbers unique in the canonical layer; skill reward cross-navigation present.
- Canonical relationship data was not changed. This batch repairs the presentation consumer so it cannot silently substitute an external corpus for the repository's source of truth.
- Commits: `a92e8450c85556aa97b50c3e6fe475025ef7d384`, `741795a257a7b4968553e124cc74860b0d1ae2c9`, `c41855426280690601a8c3d16d44124fe5e1901a`, `63546a7294b29732a6939c414c960d8a22430071`.
- Exact next batch: inspect the remaining published PQ/skill/character/DLC index consumers for direct external-corpus dependencies or stale display-only navigation, then add/repair deterministic local consumers without altering canonical relationships.


### 2026-09-22 cycle update — catalog consumer source-of-truth sweep
- Searched the live repository for direct external Madreag catalog consumers and found remaining dependencies in `docs/Skills-All.html` and `docs/Awoken-All.html`.
- Repaired both explorers to consume the canonical local `docs/data/skills.json` database. Awoken records are selected only when explicitly classified as Awoken/Transformation; no name-based inference was added.
- Expanded `scripts/validate_pq_page_consumers.py` to enforce that PQ, Skills, and Awoken catalog pages use local canonical data and contain no direct Madreag API/raw-corpus dependency.
- The PQ explorer repair from the previous cycle remains intact.
- No canonical relationship edges were created or modified in this sweep; this is a presentation/source-of-truth repair.
- Exact next batch: continue searching the live repository for remaining direct external catalog consumers, then audit character/DLC presentation indexes and deterministic target links.


### 2026-09-22 cycle update — DLC navigation reconciliation
- Inspected the live canonical DLC identity layer and discovered the identity records were already present for all 20 canonical `pq_requires_dlc` targets; the remaining inconsistency was stale reverse-navigation audit metadata, not missing identities.
- Reconciled `docs/data/dlc/pq-reverse-navigation-audit.json`: 20/20 identity targets, 86/86 canonical DLC edges, 0 missing reverse targets, 0 orphan reverse targets, 0 forward/reverse mismatches.
- Corrected the DLC endpoint validator's stale documentation so the standalone canonical DLC identity layer is explicitly part of endpoint validation.
- Updated `docs/DLC-Overview.md` to expose deterministic links to the canonical DLC identity layer, PQ reverse index, and reverse-navigation audit.
- No new DLC relationships were created. Canonical relationship count remains 860.
- Exact next batch: audit remaining character/DLC presentation consumers and structured links for deterministic resolution, then update validators/audits only from confirmed repository data.


### 2026-09-22 cycle update — character presentation identity bridge
- [x] Audited the character presentation layers and confirmed the canonical character layer intentionally exposes **149 names**, not stable `character_id` values.
- [x] Found that character preset and Partner Customization records use 29 distinct existing `character_id` values that therefore require an explicit presentation-to-canonical bridge for deterministic navigation.
- [x] Added `docs/data/characters/character-id-identity-bridge.json` with 29 explicit mappings to canonical character names. This is a presentation bridge only; it does not promote IDs into the canonical character layer or create relationships.
- [x] Added `scripts/validate_character_id_identity_bridge.py` to require every preset/key character ID to resolve through the bridge and every bridge target to exist in the canonical character name layer.
- [x] Registered the bridge and validator in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved explicit naming boundaries, including `frieza-first-form` → `Frieza (1st Form)` and `rose-goku-black` → `Rosé Goku Black`; no slug inference is used as canonical truth.
- [x] Exact next batch: audit DLC presentation consumers and future-saga content maps for `dlc_id` resolution against the 20-record canonical DLC identity layer.


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
- [x] Exact next batch: audit the general PQ reference/index pages (`docs/Parallel-Quests.md`, `docs/Parallel-Quest-Audit.md`, and related PQ-facing docs) for stale reward/navigation claims and reconcile them against the canonical 186-record PQ layer without rewriting unsupported mechanics or acquisition semantics.


### 2026-09-22 cycle update — PQ reference/index consumer reconciliation
- Live canonical relationship census before editing: **860 unique PQ relationships = 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**; canonical PQ record layer = **186 numbered records**.
- Bounded batch: audited the general PQ reference/index consumers named by the previous handoff gate: `docs/Parallel-Quests.md`, `docs/Parallel-Quest-Audit.md`, `docs/Parallel-Quest-Walkthrough.md`, `docs/Farming-Routes.md`, `docs/Farming-Hub.md`, and `docs/data/parallel-quests-index.json`.
- Deterministic findings: several presentation pages treated PQ23 as a canonical Dragon Ball farming route even though the canonical farming relationship layer contains **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**. The pages also mixed community speed/ranking claims with canonical relationship semantics.
- Changes: reconciled the PQ reference, audit, walkthrough, and farming pages to the canonical relationship set; added explicit source-of-truth/navigation semantics; updated the seed index to expose the canonical farming PQ set and to preserve the external/datemined PQ36 numbering conflict without replacing the canonical 186-record layer.
- Evidence boundary: canonical relationship data remains authoritative. Farming relationships do not establish fastest-route rankings, drop probabilities, or Ultimate Finish requirements; those remain separate evidence fields. External PQ36 cut/183-standalone interpretations remain historical/provenance context only.
- Validation: changed files were re-read from `main`; canonical farming set and 860-edge baseline remain intact; no canonical relationship edge was added, removed, or renamed. CI/Actions: no successful workflow/check exposed; do not claim CI success.
- Commits: `17ab4ba0455fce519a79e8cc41569f9b35147f8a`, `4c45bdb43c4b2446741c189368cd755727ed0698`, `59d8006b459c964bae4787931a26ce14b378bb69`, `93c941cc1d4c8da3afe85080b51fde72253c0c2e`, `e46eae3a0c54f80148db6c7804e45f8cffe832c7`, `70e0b64151f24e89b4794fb068ca49f02712dc1c`, `d9a46d300fca947a472053e4d0d38bf8e24af3d4`.
- Exact next batch: **search the remaining PQ-facing documentation/index consumers for stale canonical-count, farming-route, or external-corpus claims, then repair only deterministic local presentation drift. Prioritize any consumer that can misroute users away from the canonical PQ relationship/identity layer.**

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


### 2026-09-22 cycle update — general PQ reference/index consumer repair
- [x] Audited `docs/Parallel-Quests.md` and `docs/Parallel-Quest-Audit.md` against the canonical 186-record PQ layer and current 860-edge relationship layer.
- [x] Found one deterministic presentation drift: `docs/Parallel-Quests.md` listed **PQ13** in an “additional Dragon Ball-related routes” shorthand even though the canonical farming relationship set is exactly **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**.
- [x] Replaced the stale shorthand with the complete seven-PQ canonical farming set; no farming relationship was added or removed.
- [x] Added `scripts/validate_pq_reference_pages.py` and `docs/data/pq-reference-page-audit.json` to validate deterministic count/set claims against the canonical local layers.
- [x] Validation contract: 186 PQ records, 860 relationship edges, farming set exactly 15/22/44/45/68/83/88, and no stale PQ13 farming claim.
- [x] Registered the validator/audit in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence boundary preserved: this repair covers deterministic reference/index claims only; it does not infer reward mechanics or route-efficiency rankings.
- [ ] Exact next batch: continue the broader PQ-facing consumer audit across remaining catalog/index pages, prioritizing stale reward/acquisition summaries and one-way navigation that can be repaired deterministically from canonical local data.


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
- [x] Evidence: maintained DBXV2 Equipment catalog establishes clothing slot coverage and accessory classification; maintained PQ guide supplies acquisition endpoints; DLC documentation corroborates the relevant DLC grouping. Independent documentation also identifies the Hero of Justice Pack 2 costume/accessory set and the Gamma helmet accessories. citeturn1search4turn1search2
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
- [x] Evidence: maintained DBXV2 Equipment catalog establishes slot coverage; maintained PQ sources establish the reward endpoints; repository reverse indexes confirm existing accessory normalization. citeturn2search0turn1search7turn0search3
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

### 2026-09-22 cycle update — PQ explorer exact reward-pair parity hardening
- [x] Audited `scripts/validate_pq_explorer_reward_navigation.py` and the live `docs/Parallel-Quests-All.html` consumer after the skill/character reverse-navigation parity passes.
- [x] Hardened the PQ explorer validator to compare exact canonical `(PQ,target)` pairs against the structured Skill, Super Soul, and Equipment crosslink reports, rather than relying on endpoint resolution/counts alone.
- [x] Added explicit duplicate structured-pair checks and retained the existing HTML navigation/query checks plus canonical DLC identity resolution.
- [x] Live parity remains clean: **244 skill pairs, 151 Super Soul pairs, 125 equipment pairs; 0 missing, 0 extra, 0 duplicate pairs; 86 DLC edges / 20 unique DLC targets / 0 unresolved targets**.
- [x] Refreshed `docs/data/pq-explorer-reward-navigation-audit.json` to schema **1.1.0** with the exact-pair contract and validator commit `00dfd24c3d9c5f8f4fbc8261a261c152211cf69b`.
- [x] No canonical relationship, skill, Super Soul, equipment, DLC identity, or PQ record was added, removed, or renamed.
- [ ] CI: no successful GitHub Actions status exposed for this direct-commit chain; CI success not claimed.
- [x] Commits: `00dfd24c3d9c5f8f4fbc8261a261c152211cf69b`, `8deae24b4a557ca272e4901e2c8d4c83d35bd3ad`.
- [ ] Exact next batch: audit `scripts/validate_pq_reference_pages.py` and the general PQ reference consumers for hidden scalar/list assumptions, stale count/set assertions, and exact canonical relationship parity; harden only deterministic validator gaps, then continue to the next registered cross-domain consumer.
\n### 2026-09-22 cycle update — general PQ reference identity-contract hardening
- [x] Continued from the PQ explorer reward-pair parity pass and audited `scripts/validate_pq_reference_pages.py` against the live canonical PQ record/relationship layers.
- [x] Hardened the validator beyond count/text assertions to require the canonical PQ number set to be **exactly 1–186**, PQ IDs to be unique, relationship types to remain within the six known canonical types, and each `(relationship,PQ,target)` key to be unique.
- [x] Refreshed `docs/data/pq-reference-page-audit.json` to schema **1.1.0** with the new identity/relationship contract; live validation remains **clean**.
- [x] Existing domain parity remains **244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming = 860 edges**; farming remains **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**.
- [x] No canonical PQ, relationship, reward, or source record was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `8a256fb4e2998c12a0f29b42a637acbdc93ff5c4`, `8bf3f109e1ec3249f43f6daf9978d58d2198a4db`.
- [ ] Exact next batch: inspect the remaining registered PQ-facing search/landing consumers and cross-domain index registry for duplicated canonical counts or one-way links; prioritize a consumer where exact pair parity can be checked without broad schema migration.


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


### 2026-09-22 cycle update — published Character/DLC navigation identity-contract hardening
- [x] Audited the registered published_character_dlc_navigation consumer (scripts/validate_published_character_dlc_navigation.py) after the unified PQ reverse-index pass.
- [x] Hardened the validator beyond local-link existence to validate the Character DLC provenance bridge against the canonical character layer and the canonical DLC identity layer against every existing pq_requires_dlc endpoint.
- [x] Current live validation: **149/149 canonical character names unique; 15/15 DLC-character bridge records; 0 resolved bridge targets missing; 0 unresolved bridge records with a target; 0 duplicate bridge source labels**.
- [x] Current DLC identity validation: **86 canonical PQ→DLC edges / 20 unique targets / 20 identity records / 0 missing targets / 0 orphan identities / 0 duplicate IDs / 0 duplicate names**.
- [x] Published-page local navigation remains clean: all checked Character/DLC links resolve to repository-local artifacts.
- [x] Refreshed docs/data/characters/published-character-dlc-navigation-audit.json to schema **1.1.0** with the identity-contract census and validator result.
- [x] No canonical character, DLC, PQ relationship, or provenance identity was added, removed, or renamed. The two explicitly unresolved Chapter 4 character source labels remain unresolved.
- [ ] CI: no successful GitHub Actions workflow run exposed for commit 120cc346f9b7e049d2785e25eed9d1e5b1bd27cf; CI success not claimed.
- [x] Commits: ec4782b3ad6610f6fc681b492a73f138d208e725, 120cc346f9b7e049d2785e25eed9d1e5b1bd27cf.
- [x] Live census after editing: **860 canonical PQ relationship edges = 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**; Character/DLC presentation audit is clean.
- [ ] Exact next batch: inspect the next registered cross-domain presentation consumer after published_character_dlc_navigation, prioritizing a validator that still checks endpoint/count existence without exact canonical pair parity; preserve canonical identities and report unresolved aliases/granularity rather than guessing.


### 2026-09-22 cycle update — PQ endpoint navigation exact identity/pair hardening
- [x] Audited the registered `scripts/validate_pq_endpoint_navigation.py` consumer and its `docs/data/pq-endpoint-navigation-audit.json` report.
- [x] Hardened endpoint validation beyond target-existence checks: every canonical relationship `(PQ,target)` pair is now checked for duplicates, every relationship PQ ID must resolve to the canonical 186-record PQ layer, and the audit records canonical PQ identity census.
- [x] Live deterministic result: **244 Skills / 151 Super Souls / 125 Equipment / 247 Characters / 86 DLC = 953 endpoint edges checked**, with **0 duplicate pairs, 0 missing canonical targets, and 0 invalid PQ IDs**.
- [x] Canonical PQ layer remains **186 records / 186 unique IDs / 186 unique numbers / exact 1–186 range**.
- [x] Explicit equipment alias/granularity bridge remains intact: **2 equipment conflict entries / 6 DLC granularity entries**, with 0 unresolved equipment bridge targets.
- [x] Refreshed `docs/data/pq-endpoint-navigation-audit.json` to schema **1.1.0**.
- [x] No canonical relationship, PQ identity, endpoint identity, or alias/granularity claim was changed.
- [ ] CI: no successful GitHub Actions status exposed for the direct commits; CI success not claimed.
- [x] Commits: `f93e27f053bafab4ce33bd642ed657c85ee5fac6`, `0f6dbd85116e8678423b68f7e91b7be25b398bf3`.
- [ ] Exact next batch: inspect the next registered consumer after `canonical_endpoint_navigation`, prioritizing a validator with remaining endpoint/count-only or one-way navigation checks; preserve explicit conflicts and do not promote source-layer aliases into canonical relationships.


### 2026-09-22 cycle update — Super Soul partial acquisition-index structural hardening
- [x] Audited registered `scripts/validate_super_soul_acquisition_index.py` and its partial PQ41-186 research projection.
- [x] Hardened structural validation so duplicate PQ records, malformed/non-list Super Soul collections, and duplicate structured `(PQ,Super Soul)` pairs cannot be silently collapsed by set conversion.
- [x] Live structural result: **80 index records / 80 unique PQs / 0 malformed records / 122 structured pairs / 122 unique pairs / 0 duplicates**.
- [x] Canonical reconciliation remains informational: **133 canonical pairs / 122 indexed pairs / 120 exact overlap / 13 canonical-vs-index differences / 2 index-only differences**, including the existing 2 capitalization variants.
- [x] Refreshed `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json` to schema **1.1.0**.
- [x] No canonical Super Soul relationship or research-only acquisition claim was promoted or removed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `79872970db423be16b2a909d86b32f70bf4f4f34`, `1a9a48cf3f4190e182615aeb4c075dd0dad8209c`.
- [ ] Exact next batch: inspect the next registered cross-domain consumer after `super_soul_acquisition_index_reconciliation` for the same hidden set/scalar/list or one-way navigation failure; preserve research-vs-canonical boundaries.


### 2026-09-22 cycle update — PQ reference/explorer dependency contract hardening
- [x] Audited `scripts/validate_pq_reference_pages.py` together with `docs/Parallel-Quests.md`, `docs/Parallel-Quest-Audit.md`, and the published `docs/Parallel-Quests-All.html` explorer.
- [x] Hardened validation beyond page scalar/count claims: every canonical relationship PQ ID must resolve to the canonical 186-record PQ layer; duplicate PQ numbers/IDs are rejected; the published explorer must load the canonical PQ and relationship layers, guard collection shape, and retain its canonical Search surface.
- [x] Live result remains clean: **186 canonical PQ records / 860 canonical relationship edges**, exact domain counts **244 / 151 / 125 / 247 / 86 / 7**, **0 invalid relationship PQ IDs / 0 duplicate PQ numbers / 0 duplicate PQ IDs**.
- [x] Published explorer dependency contract is clean: canonical record source and relationship source are explicit, record/relationship collections are guarded, and canonical Search navigation is present.
- [x] Refreshed `docs/data/pq-reference-page-audit.json` to schema **1.2.0**.
- [x] No canonical relationship, identity, reward, or quest-mechanics data was changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commit: `164ac5631fde15ed1d6371fa1e0faf40d24957ea`; audit refresh: `037767eed10483c556ec4e88b64ed7f9125a7bfe`.
- [ ] Exact next batch: inspect the next registered PQ-facing search/landing consumer or cross-domain registry for one-way navigation and stale hard-coded counts, using exact canonical pair/identity parity where deterministic.


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
- [x] Audited `scripts/validate_pq_page_consumers.py` and the published `docs/Parallel-Quests-All.html` consumer against the live 186-record canonical PQ layer and 860-edge relationship graph.
- [x] Hardened structured reward validation so Skills, Super Souls, and Equipment require exact canonical `(PQ,target)` parity, list-valued fields, zero duplicate structured pairs, zero duplicate canonical relationship pairs, and relationship PQ IDs that resolve to the canonical PQ layer.
- [x] Hardened Character/DLC projection validation to reject duplicate canonical pairs and explicitly verify that the scalar `dlcByPq` projection remains unambiguous.
- [x] Live validation result: **186 unique PQ IDs / 186 unique PQ numbers; 244/244 Skills, 151/151 Super Souls, 125/125 Equipment; 247 Character pairs; 86 DLC pairs; 0 missing / 0 extra / 0 duplicate / 0 malformed / 0 invalid PQ IDs**. DLC remains exactly one canonical edge per PQ, so the scalar page projection is lossless for the current canonical graph.
- [x] Refreshed `docs/data/pq-page-consumer-audit.json` to schema **1.1.0**, recording the exact-pair and projection hardening contract.
- [x] No canonical relationships, identities, aliases, or content facts were changed.
- [x] Validator commit: `330cd587e79d3ec89cb8b7426beaf5d3bc3e1754`; audit refresh commit: `9319dec6b425411632fcdc9559c4bfa2eba335ce`.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [ ] Exact next batch: continue from the cross-domain registry to the next registered consumer with remaining endpoint/count-only or one-way navigation assumptions, prioritizing deterministic local landing/search consumers before any broad content research.


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

### 2026-09-22 cycle update — published Search consumer contract hardening
- Active workstream: P1/P2 cross-domain presentation/navigation integrity.
- Bounded batch: `docs/Search.md`, `docs/assets/search.js`, and `docs/search-data.html`.
- [x] Audited the published Search landing consumer after the character/DLC navigation chain. The page exposes the required search input/results/status hooks; the JS accepts `?q=` and seeds the initial query; the producer emits `/search-data.json` from the local `site.pages` corpus while excluding its own generator page.
- [x] Added `scripts/validate_search_consumer.py` as a deterministic presentation-contract validator. It rejects missing hooks/query handling/local-index wiring and rejects external fetch endpoints in Search JS.
- [x] Added `docs/data/search-consumer-audit.json` and registered both the audit and validator in `docs/data/pq-cross-domain-index.json`.
- [x] Static live-source result: **Search permalink/hook contract clean; `?q=` contract clean; local generated search-index fetch clean; external Search-JS fetch endpoints = 0; search-data producer/self-exclusion contract clean**.
- Evidence boundary: this validates Search presentation wiring only. It does not claim exhaustive search ranking or that every canonical structured database record is materialized as a searchable page.
- CI/Actions: no successful workflow/check exposed for this direct-commit chain; CI success is not claimed.
- Commits: validator `d0b319c5974c9a6861bff364136f6b2deaad0a0b`; audit `99474ac1c291d4c49b85cd6ce2d1c853f9d63440`; registry `c041e968d72fe23d54c778d42e73b0d40bf9b21d`; TODO `634c62bb8c90358f9026fc55b2fb6a99ca10074d`.
- Exact next batch: inspect the next registered Search/landing consumer or unvalidated cross-domain producer for deterministic one-way navigation, stale scalar/list assumptions, or canonical endpoint drift. Prefer exact local consumer parity; do not infer new relationships.

### 2026-09-22 cycle update — Equipment provenance batch `equip-081`–`equip-090`
- Active workstream: P1 equipment/accessory canonical endpoint enrichment.
- Live census before/after: **174 canonical equipment/accessory identities / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique target endpoints / 0 broken endpoints**.
- Bounded batch: `equip-081`, `082`, `083`, `084`, `086`, `087`, `088`, `089`, `090`; `equip-085` remains intentionally absent because no live canonical identity exists.
- Research/evidence: maintained Xenoverse 2 equipment catalog; maintained all-186-PQ Steam guide; dedicated Goku's Turtle Hermit Gi (King Kai) page; Whis Symbol Gi page; independent GameFAQs equipment discussion for Frieza's Suit component coverage.
- Changes: added slot coverage and catalog provenance to eight non-alias records; retained `equip-088` as historical alias to `acc-012`; refreshed `last_verified` on enriched records.
- Evidence limits/conflicts preserved: no reward probability, guaranteed-drop semantics, combat effect, or unsupported DLC attribution was inferred; `equip-085` was not fabricated.
- Validation: equipment/accessory endpoint layer **174/174 resolved**, **0 duplicate IDs**, **125 forward**, **123 reverse endpoints**, **0 broken**. Batch live IDs **9/9 present**; eight enriched non-alias records have slot coverage; normalized alias remains explicit.
- CI/Actions: no successful workflow/check exposed; CI success is not claimed.
- Commits: canonical `1b2f96e444c1f0ce17174cba4d4d95841ae671cd`; detail audit `007c9a768edd1483583cec7336b2f7537366922a`; TODO `93e4ff79cc11b260fbe039ad355eef9adee89a86`.
- Exact next batch: **`equip-091`–`equip-100`**; recompute the endpoint census first and preserve canonical accessory bridges/normalized aliases.

### 2026-09-22 cycle update — Equipment detail enrichment `equip-091`–`equip-100`
- Active workstream: P1 equipment/accessory canonical endpoint enrichment.
- Fresh live census: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique targets / 0 broken endpoints**.
- Bounded batch: legacy endpoints `equip-091`–`equip-100`.
- Canonical identity handling: `equip-091` SSGSS Goku Wig remains the historical endpoint for canonical `acc-058`; `equip-093` Videl (DB Super) Wig remains the historical endpoint for canonical `acc-070`. No duplicate canonical identities were created.
- Detail changes: eight non-aliased endpoints received source-backed category/slot metadata and DLC provenance. Orange Piccolo's Clothes is explicitly three-piece/no-hands; Videl (DB Super)'s Clothes is four-piece; DAIMA suit/wig/battle-suit classification follows independent DLC/equipment evidence. Vegeta's Shirt remains upper-body only rather than being promoted to a full set.
- Evidence: maintained DBXV2 equipment catalog; maintained all-186-PQ Steam guide; DBXV2 DLC documentation; Bandai Namco DAIMA Pack announcement; independent GameFAQs component discussion.
- Evidence limits preserved: no reward probability, guarantee, combat/stat effect, or unsupported restriction was inferred.
- Audit: added `docs/data/equipment/equipment-091-100-detail-audit.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- Validation: **174/174 combined endpoint identities, 0 duplicate IDs/names, 125 forward, 123 reverse, 0 broken**; 10/10 legacy endpoints have slot coverage; 8/8 non-alias endpoints explicitly classified.
- CI/Actions: no successful workflow/check exposed; CI success is not claimed.
- Commits: canonical `267cb0dcd98b9c5b8307e0d0f1ca5ac4b3da65cb`; combined `af70f83339d32794fa6c577ebfadc97850bd0f62`; audit `87b75353add617b60607c476dacb3442dc95ba3b`; registry `bb005ca06da404f9027bf18148e6204f4b72cfe3`; TODO `660fb46d05ba6192d315cf1755e2b12ae4dad661`.
- Exact next batch: **`equip-101`–`equip-110`** after a fresh endpoint census, preserving canonical accessory bridges and normalized historical aliases.

### 2026-09-22 cycle update — Equipment detail enrichment `equip-101`–`equip-110`
- Active workstream: P1 equipment/accessory canonical endpoint enrichment.
- Fresh/live census: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique targets / 0 broken endpoints**.
- Bounded batch: `equip-101`–`equip-110`.
- Changes: all 10 endpoints received source-backed category and slot coverage; DLC provenance was reconciled as DAIMA Pack for `101–105` and Future Saga Chapter 3 for `106–110`.
- Category details: `101,104,105,107,109,110` accessories; `102` Glorio's Clothes upper/lower/feet; `103,106` four-piece clothing; `108` Cheelai's Coat upper-body-only.
- Evidence: maintained DBXV2 equipment catalog, DBXV2 DLC documentation, maintained all-186-PQ Steam guide, Glorio/Panzy documentation, and independent PQ184 documentation.
- Evidence limits: no reward probability, guaranteed-drop semantics, combat/stat effect, or unsupported restriction inferred.
- Audit: `docs/data/equipment/equipment-101-110-detail-audit.json`, registered in `docs/data/pq-cross-domain-index.json`.
- Validation: **174 records / 0 duplicate IDs / 125 forward / 123 reverse / 0 broken**; 10/10 batch records have slot coverage and explicit classification.
- CI: no successful workflow/check exposed; CI success not claimed.
- Commits: canonical `34ffe98a4702514806dbe425aba3f38f18804e6d`; combined `9bcf4242481a7d2283e7fe4db7894e923be2c13a`; audit `8bcbb0f4bf6d846b2557c84631851f07599e4af1`; registry `b51aa73512fb62822681a83b8a80af358142f5d2`; TODO `eced4791690df05feae417c6bd1683f062fef101`.
- Exact next batch: **`equip-111`–`equip-120`** after a fresh census.

### 2026-09-22 cycle update — Equipment detail enrichment `equip-111`–`equip-120`
- Active workstream: P1 equipment/accessory canonical endpoint enrichment.
- Fresh live census: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 PQ→equipment forward edges / 123 unique targets / 0 broken endpoints**.
- Bounded batch: `equip-111`–`equip-120`.
- Changes: all 10 endpoints received source-backed category and slot coverage. `111–115` were reconciled to Future Saga Chapter 4 provenance; `116–120` remain base-game PQ-era endpoints.
- Category details: `111,113,116,118` full four-piece clothing; `119` upper-body clothing; `112,114,115,117,120` accessories.
- Evidence: maintained DBXV2 equipment catalog, maintained all-PQ Steam guide, and independent Dragon Ball documentation for Yamcha's Baseball Hat.
- Evidence limits: no reward probability, guaranteed-drop semantics, combat/stat effect, or unsupported restriction inferred; GT Vegeta's Jacket intentionally remains upper-body-only.
- Audit: `docs/data/equipment/equipment-111-120-detail-audit.json`, registered in `docs/data/pq-cross-domain-index.json`.
- Validation: **174 records / 0 duplicate IDs / 125 forward / 123 reverse / 0 broken**; 10/10 batch records have slot coverage and explicit classification.
- CI: no successful workflow/check exposed; CI success not claimed.
- Commits: canonical `55f163ba865fecb908a2f1dc259ea455aafb17cf`; combined `bf0f9087f5ac0d56fc34fa69860717bb3817d3a9`; audit `a8e2b5c6029f45e4f0b9bf0e61d58d21b80b19b8`; registry `0a0194f191171bfff92e201de90a08cfeb6f4500`; TODO `853eeb1f4fb1e91c478a91d67bb53080e3e1f102`.
- Exact next batch: **`equip-121`–`equip-130`** after a fresh census.

### 2026-09-22 cycle update — Equipment detail enrichment and identity correction `equip-121`–`equip-130`
- Live census before editing: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 forward / 123 reverse / 0 broken**.
- Bounded batch: `equip-121`–`equip-130`.
- Critical correction: `equip-121` **Mr. Shape Up L** was a false equipment endpoint. Independent evidence identifies Mr. Shape Up L as a consumable capsule/material, so it was removed from the equipment layers while the PQ99 reward remains in PQ reward data.
- Canonical bridge preserved: `equip-123 → acc-063` (SSGSS Vegeta Wig); no duplicate canonical accessory was created.
- Detail changes: `122`, `124–130` received source-backed category/slot metadata and DLC provenance. `130` Goku Black's Clothes is explicitly upper/lower/feet with no hands.
- Evidence: maintained DBXV2 equipment catalog; maintained all-PQ Steam guide; Future Mai/Battle Armor documentation; independent Goku Black equipment discussion; capsule documentation for the false-positive correction.
- Evidence limits: no reward probability, guaranteed-drop semantics, combat/stat effect, or unsupported restriction inferred.
- Audit: `docs/data/equipment/equipment-121-130-detail-audit.json`, registered in `docs/data/pq-cross-domain-index.json`.
- Validation after editing: **173 combined records / 0 duplicate IDs / 124 forward / 122 reverse / 0 broken endpoints**; 8 live non-bridge endpoints have slot coverage and explicit classification.
- CI: no successful workflow/check exposed; CI success not claimed.
- Commits: canonical `cea284c71ec7d9e657ca0d675dd3402d28e41f4f`; combined `4ce040ffa6ce1cb299c747d2a9ccef1a67288696`; crosslink `9f6203ef50f15168448fa821c7b9232113776f96`; audit `a75e1e28f7dbe94f5543b3d2160f6e70fdbf1220`; registry `93ac07fc9f37120ecec38c9232cb7171ed15965a`; TODO `997861a3c545742d6ff2f5ee32e1f4da09e4f346`.
- Exact next batch: **`equip-131`–`equip-140`** after a fresh census.

### 2026-09-22 cycle update — Equipment detail enrichment equip-131–equip-140
- [x] Live census before editing: **139 legacy equipment records / 173 combined equipment-accessory canonical records / 0 duplicate canonical IDs**; canonical PQ→equipment relationship layer is **124 forward edges / 122 unique target endpoints** after the earlier equip-121 non-equipment correction.
- [x] Bounded batch: **equip-131–equip-140**. Existing legacy endpoints were classified without inventing new identities; **equip-133** was explicitly preserved as the historical/projection alias of canonical accessory **acc-064 (SS4 Wig & Tail (Goku))**.
- [x] Enriched canonical classifications: 131 Zamasu's Clothes (clothing; upper/lower/feet; Super Pack 4), 132 Super Saiyan 4 Suit (Goku) (four-piece clothing; Super Pack 4), 134 Resistance Clothes (four-piece clothing; Super Pack 4), 135 Resistance Helmet (accessory; Super Pack 4), 136 Pride Trooper Uniform (four-piece clothing; Extra Pack 1), 137 Toppo's Moustache (accessory; Extra Pack 1), 138 Ribrianne's Clothes (four-piece clothing; Extra Pack 1), 139 Ribrianne's Hood (accessory; Extra Pack 1), and 140 Goku's Turtle Hermit Gi (Go) (four-piece clothing; base game). 133 → acc-064 remains the canonical accessory identity.
- [x] Evidence: maintained Xenoverse 2 equipment catalog, maintained all-186-PQ Steam guide, Dragon Ball documentation for Resistance equipment, and maintained PQ clothing index. These establish category/slot/provenance only; no reward probability, guaranteed-drop semantics, current shop rotation, combat/stat effect, or unsupported restriction was inferred.
- [x] Added docs/data/equipment/equipment-131-140-detail-audit.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Reconciled docs/data/pq-equipment-crosslink-report.json to the **173-record** canonical equipment/accessory layer: **124 forward edges / 122 unique targets / 122 reverse records / 124 forward-reverse pairs / 0 missing / 0 extra / 0 duplicate pairs / 0 unresolved endpoints**. Legacy accessory IDs are now normalized to canonical acc-### IDs in the report, and removed non-equipment equip-121 is no longer present.
- [x] Validation: all 10 batch legacy records are present and enriched; **9** remain non-alias canonical equipment endpoints and **1** is the normalized equip-133 → acc-064 bridge; duplicate IDs **0**; broken endpoints **0**; unresolved batch relationship endpoints **0**; canonical forward/reverse parity **pass**.
- [ ] CI: no successful GitHub Actions workflow/check exposed for this direct-commit chain; CI success is not claimed.
- [x] Commits: a17c8281dee8278fdf396a16c4a858f01fde1330, 85b3d1d926778e3b8b3ccc7e4e143e30b1c293e4, 5e41477a3ade6a3bfd16144161497606a7511b00, 14f8be396cfa3a27066351ee0b45ad9213df549e, c01e71b3febc5447238c2a55a4a1e913c0313ad0, 4f45d5eacb9b566b8e59ad42a405b8407d19b329.
- [x] Live census after editing: **139 legacy equipment records / 173 combined canonical equipment-accessory records / 64 canonical accessory IDs / 124 PQ→equipment forward edges / 122 unique targets / 122 reverse records / 0 broken or unresolved endpoints**.
- [ ] Exact next batch: **fresh census, then enrich equip-141–equip-150**, preserving canonical accessory bridges and correcting any non-equipment false positives before enrichment.

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


### 2026-09-22 continuation cycle — non-PQ projection census repair
- Continued the non-PQ consumer/navigation audit from commit `8ae0fdfd8e923270f61416d0546c2ddb8e27e678`.
- Fresh live search identified stale current equipment projection metadata in `docs/data/pq-cross-domain-audit.json` and `docs/data/pq-cross-domain-status.json`: the current equipment report was still recorded as 125 forward edges / 123 reverse endpoints even though the authoritative canonical relationship layer is 124 equipment edges / 122 unique reverse endpoints.
- Corrected only those current projection fields to **124 forward / 122 reverse**, preserving all dated 125/123, 862/840/860 historical records unchanged.
- Updated the projection note from “125 canonical equipment-domain edges” to “124 canonical equipment-domain edges”.
- Commits: `46bfb3c8589b50cb3c8cdb4e12f51b2b273d42eb` (audit) and `3eff4ea3c9047d5bee38d4c7492050876cde1e85` (status).
- Current canonical baseline remains **859 total edges: 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**.
- No relationship edges were added or removed in this cycle; this was consumer/projection metadata synchronization only.
- Next exact gate: fresh search for other current (not historical) consumer fields that disagree with the 859/244/151/124/247/86/7 baseline, then direct-fetch each hit before repair. Avoid broad numeric replacement because historical audit snapshots are intentionally retained.


### 2026-09-22 continuation cycle — current-final-state projection repair
- Fresh census confirmed the authoritative current PQ relationship layer remains **859 unique edges: 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**.
- Direct inspection of `docs/data/pq-cross-domain-audit.json` found one remaining mislabeled current-state object: `current_final_state_2026_09_22` still reported the superseded **860 edges / 125 equipment** state.
- Corrected only that current-final-state object to **859 / 124 equipment**. The earlier 860/862/840 counts in explicitly dated reconciliation/history objects remain untouched.
- No canonical relationship arrays were changed; this was deterministic projection metadata repair only.
- Commit: `44ee7eda80e927093f679e9550a6e5e43b29198a`.
- Validation target after repair: current source-of-truth projection remains 859/244/151/124/247/86/7; historical snapshots remain preserved.
- CI/runtime execution remains unavailable; no CI success claimed.
- Exact next task: fresh search/direct-fetch the remaining registered current presentation/identity consumers for **859/124** drift, then repair only fields demonstrably labeled current; do not alter historical audit snapshots.


### 2026-09-22 continuation cycle — equipment identity-conflict evidence strengthening
- Fresh current-consumer census was performed after the prior projection repairs. Direct live-file inspection shows the current PQ cross-domain audit/status projections are already synchronized at **859 total / 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; stale 860/125 search hits are historical snapshots or stale search-index fragments and were not rewritten.
- Audited the two remaining explicit equipment naming conflicts before canonical identity changes. Current identity evidence continues to support preserving both canonical identities rather than merging by name similarity:
  - PQ152: source/reward documentation uses **Android 17 (DB Super) Wig**; the repository separately preserves **Android 17 (DB Super) Ranger Wig** and the documented Ranger Accessory research label.
  - PQ155: source/reward documentation uses **Gamma 2's Helmet**; the repository separately preserves **Gamma 2 Helmet** as the legacy/equipment identity.
- Strengthened docs/data/pq-endpoint-alias-granularity-map.json with explicit external evidence URLs for both conflicts. No canonical relationship edge or identity was changed.
- Commit: 6a0b10fa2f26946048de4d6a55decb144a840109.
- Current identity-resolution status remains clean: 0 unresolved endpoints, 0 duplicate pairs, 0 invalid PQ IDs, with 2 explicit equipment conflicts and 6 DLC granularity mappings.
- CI/runtime execution remains unavailable; no CI success claimed.
- Exact next task: continue the non-PQ presentation/identity consumer census beyond scalar baselines, focusing on endpoint naming/display mappings and any consumer that could bypass the explicit alias/granularity bridge; make only independently evidenced deterministic repairs.


### 2026-09-22 — Explicit bridge metadata validation hardening
- [x] Audited the non-PQ presentation/identity consumer chain: cross-link contract → alias/granularity bridge → endpoint-navigation validator → generated navigation/identity reports.
- [x] Confirmed the current canonical baseline remains **859 relationships / 124 equipment**, and stale 860/125 references found by repository search are historical audit material rather than current projection fields.
- [x] Hardened `scripts/validate_pq_endpoint_navigation.py` so equipment conflict bridge records must carry a PQ ID, source label, explicit-conflict classification, at least two canonical targets, and evidence; DLC granularity records must carry a PQ range, source label, explicit deterministic-granularity classification, and canonical targets.
- [x] Validator bridge failures are now included in the overall non-zero failure path instead of allowing structurally incomplete presentation mappings to appear clean.
- [ ] Next gate: inspect the remaining registered presentation consumers and generated reports for field-level schema drift, then perform a full executable validation when repository runtime/CI execution is available.


### 2026-09-22 cycle update — registered non-PQ consumer baseline census
- [x] Completed a fresh static direct-fetch census of the registered non-PQ presentation/identity consumers after the 859/124 correction chain.
- [x] Audited 16 registered consumer/projection artifacts spanning producer census, endpoint identity/navigation, presentation reverse indexes, PQ explorer/reference consumers, skill/Super Soul acquisition projections, Search, standalone/unified reverse indexes, alias/granularity metadata, and mixed historical/current cross-domain audit/status layers.
- [x] Confirmed the authoritative current baseline remains **859 unique relationships = 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; equipment projection remains **124 forward / 122 unique reverse endpoints**.
- [x] Found **0 deterministic current 860/862/125/123 scalar mismatches** in the audited consumer set. Historical snapshots remain intentionally preserved and are excluded from current-state interpretation.
- [x] Added `docs/data/pq-non-pq-consumer-census-2026-09-22.json` and `scripts/validate_pq_non_pq_consumer_census.py`, and registered both in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved the two explicit equipment naming conflicts and six DLC granularity mappings; no canonical relationship or identity was changed.
- [x] Super Soul acquisition projection still has its documented 13 reconciliation findings (11 exact missing pairs + 2 capitalization variants); these remain a research/projection queue rather than baseline drift.
- [ ] Runtime/CI execution remains unavailable; this cycle claims static direct-fetch/structural inspection only, not executable validation.
- [ ] Exact next task: return to the **P1 skill provenance queue at Prominence Flash (`skill-prominence-flash`)**, recompute the live two-source census first, independently verify its acquisition/source endpoint, and make provenance-only changes within the existing canonical relationship contract.


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
- [x] External evidence: the maintained Super Soul/PQ references explicitly identify `Killed all Earthlings!` as obtained from **Parallel Quest 58**. citeturn0search0turn0search2
- [x] No canonical relationship was modified; this was a provenance/projection reconciliation only.
- [x] Exact post-edit comparison: **133** canonical PQ41–186 Super Soul pairs / **128** indexed pairs / **126** exact overlap / **7** remaining differences. Remaining differences are five exact canonical gaps (both PQ158 entries, PQ174, PQ178, PQ179) plus the two capitalization variants at PQ164/PQ173.
- [x] Updated `docs/data/super-souls/pq-acquisition-index-041-186.json` and `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json`.
- [ ] Runtime/CI remains unavailable; validation was static direct-fetch JSON parsing and exact pair comparison.
- [x] Commits: acquisition projection `6ff4b3eb2e39cd413917ad46e527d36e19727802`; reconciliation audit `52f0fc86d78277fa4648edebcca26975a8506bf0`.
- [ ] Exact next batch: independently reconcile the **two PQ158 Super Soul pairs**, preserving the existing source spelling conflict, then PQ174/PQ178/PQ179.


### 2026-09-22 cycle update — Super Soul acquisition reconciliation final five exact gaps
- [x] Fresh live census before editing: **151 canonical PQ→Super Soul relationships**; the partial PQ41–186 acquisition projection had **128 structured pairs / 7 reconciliation findings** before this batch.
- [x] Bounded batch: reconciled the final five exact canonical gaps: **PQ158** → `Heh heh! I'm not as rusty as I look!` and `See? It's a good thing I was here, right?`; **PQ174** → `I'll surpass you as I am, with my OWN power!`; **PQ178** → `I'll take you all on at once!`; **PQ179** → `Here I go!`.
- [x] Evidence: maintained Super Soul/PQ references corroborate the five acquisitions; independent GameFAQs documentation also corroborates the Future Saga Super Soul acquisition context. citeturn6search0turn2search1
- [x] Preserved source-layer wording conflicts for PQ158 and PQ178 explicitly; the structured projection uses canonical names instead of treating variants as separate identities.
- [x] Post-write validation: **133 canonical PQ41–186 pairs / 131 indexed pairs / 131 exact overlap / 0 exact missing / 2 capitalization variants** (PQ164/PQ173); **83 unique PQ records / 131 unique structured pairs / 0 duplicates**.
- [x] Updated `docs/data/super-souls/pq-acquisition-index-041-186.json` and `docs/data/super-souls/pq-acquisition-index-reconciliation-audit.json`; no canonical relationship identity was added, removed, or renamed.
- [ ] Runtime/CI execution remains unavailable; validation is static JSON parsing and exact pair/census comparison only.
- [ ] Exact next batch: audit the two remaining capitalization variants (**PQ164** and **PQ173**) against an independent exact-text source; if no stronger evidence resolves them, preserve them as presentation/source-normalization differences and move to the next structural cross-domain gap.


### 2026-09-22 cycle update — Super Soul acquisition projection exact parity and capitalization audit
- [x] Independently checked the two previously flagged capitalization variants: PQ164 is “This place will be your grave!” and PQ173 is “You will know the power of the gods!”. External Super Soul/PQ references support those spellings. citeturn0search0turn0search10
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
- [x] Independent acquisition verification: the maintained all-186-PQ Steam guide explicitly lists Prominence Flash under **PQ137 — Tournament of Power Round 2 — Basic Reward**; an independent Dragon Ball Wiki reference identifies it as an Ultra Pack 1 skill obtained through PQ137. citeturn1search0turn2search3
- [x] No canonical skill identity, acquisition endpoint, reward relationship, or Ultimate Finish flag was changed; this pass confirms provenance parity only.
- [x] Existing third-party source is already recorded in both canonical and index skill records, so no duplicate provenance entry was added.
- [ ] Runtime/CI remains unavailable; validation is static direct-fetch, source/census comparison, and exact endpoint verification.
- [ ] Exact next batch: **Requiem of Destruction (`skill-requiem-of-destruction`)** — recompute its live canonical/index census, inspect the full record, and independently verify its acquisition/source endpoint before making any provenance-only changes.


### 2026-09-22 cycle update — Requiem of Destruction provenance verification
- [x] Live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-requiem-of-destruction`.
- [x] Canonical/index records agree on classification, 300 Ki cost, PQ106 acquisition, Super Pack 2 provenance, All CaC race scope, and `ultimate_finish_required: false`.
- [x] Independent verification: the maintained all-186-PQ guide lists **Requiem of Destruction** in **PQ106 — A Destructive Showdown — Basic Reward**. citeturn0search0 A separate PQ106 gameplay record likewise lists it under Basic Reward. citeturn0youtube13
- [x] Existing repository sources already include the maintained Steam guide plus two Dragon Ball Wiki sources; no duplicate source was added.
- [x] Evidence boundary preserved: Basic Reward placement establishes the acquisition route but not a drop probability; no Ultimate Finish gate is inferred.
- [x] No canonical skill identity, acquisition relationship, DLC identity, or reward-tier field required modification; provenance was already correctly represented.
- [ ] Runtime/CI remains unavailable; validation is static direct-fetch, source comparison, and canonical/index parity.
- [ ] Exact next batch: continue the P1 skill provenance census with the next unfinished skill identified by the live handoff/TODO, without repeating completed Prominence Flash or Requiem of Destruction work.


### 2026-09-22 cycle update — Absolute Zero provenance and reward-tier reconciliation
- [x] Live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-absolute-zero`.
- [x] Independent evidence: the maintained all-186-PQ Steam guide explicitly lists **Absolute Zero** under **PQ96 — The Shadow Dragons — Basic Reward**; the dedicated skill reference independently identifies PQ96 as its Xenoverse 2 acquisition route. citeturn0search3turn0search0
- [x] The repository's existing older video evidence reports Absolute Zero as a PQ96 Ultimate Finish reward. The conflict is retained rather than erased; the current maintained reward transcription supports the canonical `ultimate_finish_required: false` value without inferring a probability.
- [x] Canonical/index parity preserved; only `last_verified` and provenance notes were strengthened to record the fresh independent check.
- [x] Cross-domain links already exist: PQ96 → Absolute Zero is represented in the PQ skill crosslink and unified reverse index.
- [ ] Runtime/CI remains unavailable; validation is static JSON parsing, canonical/index parity, and source-endpoint comparison.
- [ ] Exact next batch: continue the P1 skill provenance census with **All Clear (`skill-all-clear`)**, then proceed sequentially through the unfinished skill queue while preserving evidence conflicts.


### 2026-09-22 cycle update — All Clear mentor provenance verification
- [x] Live skill census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-all-clear`.
- [x] Independent evidence: the maintained instructor-quest guide lists **All Clear** as **Cell's Initiation Test — Basic Reward**. citeturn0search14turn0search15 The dedicated skill reference identifies the acquisition as training with Cell (Perfect), and the mentor roster independently lists All Clear among Cell's rewards. citeturn0search0turn0search3
- [x] Acquisition endpoint is therefore retained as Cell (Perfect) mentor training; no Parallel Quest acquisition, Ultimate Finish requirement, or probability is inferred.
- [x] Canonical/index provenance notes and `last_verified` were refreshed; no skill identity, classification, cost, or cross-domain relationship required correction.
- [x] Cross-domain mentor linkage already exists through `source_mentor: [mentor-cell]` in the canonical layer.
- [ ] Runtime/CI remains unavailable; validation is static JSON parsing, census, canonical/index parity, and source comparison.
- [ ] Exact next batch: continue the P1 skill provenance census with the next unfinished skill after `skill-all-clear`, preserving source conflicts and avoiding duplicate work.


### 2026-09-22 cycle update — Afterimage starting-skill provenance verification
- [x] Live census: **452 canonical / 452 index / 0 duplicate IDs / 0 nullable canonical ki_cost**; bounded record: `skill-afterimage`.
- [x] Independent evidence: the dedicated Xenoverse 2 Afterimage reference identifies it as the starting move for the **Mixed** fighting-style choice. citeturn0search0 The CaC documentation independently states that the initial fighting-style choice determines starting skills and identifies Afterimage with Mixed. citeturn0search5
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
- [x] Independent evidence confirms PQ161 — “Scream Team vs. Dream Team” as the acquisition endpoint. Current external sources conflict on reward tier: the maintained all-186-PQ Steam guide and an independent PQ161 gameplay record display Apocalyptic Burst in the Basic Reward list, while the repository's existing reward-tier evidence records a 45% Ultimate Finish bonus slot. citeturn0search2turn0youtube12turn0youtube13
- [x] Conflict preserved rather than silently changing the canonical `ultimate_finish_required: true` field or inventing a drop probability. Canonical/index provenance notes and `last_verified` were refreshed only.
- [x] Static validation: 452/452 records, no duplicate IDs, and exact canonical/index parity for verification date, unlock method, Ultimate Finish flag, and source count.
- [ ] Runtime/CI remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `7168f8391783a3bf42c2f8530ea96a0551e8eefa`; index `fdd951c143a99e99e237d38c14c70d4d91a53dce`.
- [ ] Exact next batch: continue the stale-`last_verified` P1 skill provenance queue with **Arm Crash (`skill-arm-crash`)**, then proceed sequentially while preserving evidence conflicts.


### 2026-09-22 cycle update — Beast provenance verification
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded record: skill-beast.
- [x] Independently verified the existing Beast acquisition semantics: max friendship with Gohan (Adult) & Videl and Piccolo, then Piccolo's special training / Cell Max unlock mission. Dedicated Beast documentation, independent GameFAQs discussion, and official Bandai Namco DLC context were used with evidence boundaries preserved.
- [x] Refreshed docs/data/skills.json and docs/data/skills-index.json: last_verified -> 2026-09-22 and provenance source/note synchronized.
- [x] Added docs/data/skill-beast-provenance-audit-2026-09-22.json; registered it in docs/data/pq-cross-domain-index.json.
- [x] Validation: 452 canonical / 452 index / 0 duplicate IDs; affected canonical/index records remain semantically aligned. No PQ relationship or skill identity changed.
- [ ] Runtime/CI remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the stale-last_verified P1 skill provenance queue with the next unfinished skill after Beast, recomputing the live canonical/index census first.


### 2026-09-22 cycle update — Become Giant provenance verification
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded record: skill-become-giant.
- [x] Independently verified the existing Become Giant acquisition semantics: Namekian Awakening at Guru's House, including the documented Namekian/level-35 prerequisites and quest flow. Dedicated quest documentation and an independent GameFAQs walkthrough corroborate the route.
- [x] Refreshed docs/data/skills.json and docs/data/skills-index.json: last_verified -> 2026-09-22 and provenance source/note synchronized.
- [x] Added docs/data/skill-become-giant-provenance-audit-2026-09-22.json; registered it in docs/data/pq-cross-domain-index.json.
- [x] Validation: 452 canonical / 452 index / 0 duplicate IDs; affected canonical/index records remain semantically aligned. No PQ relationship or skill identity changed.
- [ ] Runtime/CI remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue the stale-last_verified P1 skill provenance queue with Big Bang Knuckle (skill-big-bang-knuckle), recomputing the live canonical/index census first.


### 2026-09-22 cycle update — Big Bang Knuckle provenance verification
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded record: skill-big-bang-knuckle.
- [x] Independently verified the existing acquisition endpoint: PQ172 — "Little Big Brother". Current dedicated skill documentation confirms the route and move identity; official Dragon Ball documentation confirms Big Bang Knuckle as a FUTURE SAGA Chapter 1 Vegeta (Super Saiyan God) Ultra Supervillain special move.
- [x] Refreshed canonical/index last_verified to 2026-09-22 and synchronized provenance notes/sources.
- [x] Added docs/data/skill-big-bang-knuckle-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Existing 40% Ultimate Finish bonus-slot evidence and conflicting Basic Reward presentation were preserved; no unsupported probability or reward-tier correction was made.
- [x] Static validation: 452 canonical / 452 index / 0 duplicate IDs; affected canonical/index records remain aligned.
- [ ] Runtime/CI remains unavailable; no CI success claimed.
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
- [x] Independent evidence corroborated Zarbon Lesson 2, Captain Ginyu Lesson 3, Nappa Initiation Test, Bardock Lesson 3, PQ117, and PQ116 acquisition endpoints. citeturn0search1turn0search9turn0search8turn0search4turn0search0
- [x] Refreshed canonical/index last_verified to 2026-09-22; existing reward-tier semantics preserved and no unsupported probability inferred.
- [x] Added docs/data/skill-provenance-audit-2026-09-22-bloody-through-brave.json.
- [x] Static validation: 452/452, no duplicate IDs; affected records remain synchronized.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: recompute live census and continue after Brave Sword Slash.


### 2026-09-22 cycle update — Break Cannon / Brutal Buster / Burning Blast / Burning Shot / Burst Charge / Burst Reflection provenance
- [x] Fresh live skill census: 452 canonical / 452 index / 0 duplicate IDs; bounded batch: six stale P1 skill records.
- [x] Independent evidence corroborated Nappa Lesson 3, PQ141, PQ180, PQ143, PQ134, and the Shenron-wish acquisition route. citeturn0search8turn0search1turn0search7turn0search4turn0search3turn0search2
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
- [x] Independent evidence: the dedicated Burst Rush reference identifies **Parallel Quest 51 — “Great Saiyaman is Here”** as the unlock; the maintained all-186-PQ Steam guide explicitly lists Burst Rush in PQ51's **Basic Reward**; an independent PQ51 gameplay record also lists Burst Rush as a Basic Reward. citeturn0search0turn0search3turn0youtube24
- [x] Canonical/index provenance was refreshed to `last_verified: 2026-09-22`; the existing acquisition semantics were preserved. No skill identity, classification, acquisition endpoint, Ultimate Finish flag, or PQ relationship changed.
- [x] Evidence boundary preserved: Basic Reward evidence does not establish a drop probability; no Ultimate Finish-only gate was inferred.
- [x] Added `docs/data/skill-burst-rush-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452** records, **0 duplicate IDs**, and exact semantic parity across canonical/index for the affected acquisition fields, verification date, and reward-tier flag.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `c5c796f99e431e4860b6c51e06e4fe534adf8ad9`; index `447ed9657f552c0bdf2fdc92a9870d3ae7146e23`; audit `d66d5abdfd780450a8c3f12f8b5ea682ee82a869`; registry `e12cfe1cd4f9bc522903a676a532ac5cfc22e0b6`.
- [ ] Exact next batch: continue the stale-`last_verified` P1 skill provenance queue with **Burst Stinger (`skill-burst-stinger`)**, recomputing the live canonical/index census first and preserving any reward-tier conflicts or evidence boundaries.


### 2026-09-22 cycle update — Burst Stinger provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded record: `skill-burst-stinger`.
- [x] Independent evidence: dedicated Burst Stinger documentation identifies **PQ136 — “Breaking Down the Barrier”** as the unlock; the maintained all-186-PQ guide and independent PQ136 gameplay record list Burst Stinger among the Basic Rewards. citeturn0search0turn0search9turn0youtube26
- [x] A separate GameFAQs acquisition report attributes the drop to Goku (Ultra Instinct) during the Ultimate Finish. This conflicts with the Basic Reward presentation, so the repository retains the existing Basic Reward semantics and records the trigger conflict rather than promoting an Ultimate Finish-only gate. citeturn0search1
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** without changing skill identity, classification, acquisition endpoint, or canonical PQ relationship.
- [x] Added `docs/data/skill-burst-stinger-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, and semantic parity across canonical/index for the affected acquisition fields and reward-tier flag.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `d40348757a9a22a04a688ecf51e8f3820d33c3b4`; index `39dda59cc12cb8b102b71e1a3161852fd6606c10`; audit `a889598d04e22c869573c80e33a14bbd945325c8`; registry `c5869e41261aa54fa74ca783d1ff9c73924df72c`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Buu Buu Ball (`skill-buu-buu-ball`)**, preserving any acquisition/reward-tier evidence conflicts.


### 2026-09-22 cycle update — Buu Buu Ball provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs**; bounded record: `skill-buu-buu-ball`.
- [x] Independent evidence corroborates **PQ88 — “Evil Seeks Dragon Balls Yet Again!”** as the acquisition endpoint and lists Buu Buu Ball as a **Basic Reward**. Dedicated documentation also confirms its current Strike Evasive classification, 300 Stamina cost, and Majin CaC restriction. citeturn0search0turn0search1turn0search2turn0youtube22turn0search4
- [x] Refreshed canonical/index `last_verified` to **2026-09-22**; existing acquisition, reward-tier, race-restriction, and no-Ultimate-Finish-only semantics were preserved.
- [x] Added `docs/data/skill-buu-buu-ball-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, and semantic parity across canonical/index for affected acquisition fields and restriction metadata.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `97c2ca5cc981ee150f3ebcb212c9f6c32556de00`; index `704c607c464798568976727bc21d22b6d9333196`; audit `c91b72fbc312a136de8d04d4f92cf5c45b45ac73`; registry `0567c2e75b70889c7b8b2961492644331d41622e`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Candy Beam (`skill-candy-beam`)**, preserving any acquisition/reward-tier evidence conflicts.


### 2026-09-22 cycle update — Candy Beam provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 399 stale before editing**; bounded record: `skill-candy-beam`.
- [x] Independent evidence confirms PQ66 as a Candy Beam acquisition point and Basic Reward; the maintained all-186-PQ guide also lists Candy Beam as a Basic Reward at PQ113, preserving the existing `source_parallel_quests: [66,113]` relationship. citeturn0search0turn0search4turn0search7
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** while retaining the base-game PQ66 anchor and later PQ113 context.
- [x] Evidence boundary preserved: community Ultimate-Finish/RNG reports do not establish an Ultimate Finish-only gate or drop probability; a current reference also exposes an Evasive Candy Beam variant, so this provenance-only pass did not normalize class/mechanics semantics. citeturn0search5turn0search14turn0search8
- [x] Added `docs/data/skill-candy-beam-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Static validation after writes: **452/452**, **0 duplicate IDs**, **398 stale remaining**, and exact semantic parity across canonical/index for affected fields.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `21b7a550b517d519037317c211df01c33bacd06c`; index `b79993d3bb7cab31ec14773f6027d18264b5dcad`; audit `f977369ca49663a9ecbe944c0659c57d9f7c7140`; registry `588dd96cd9b3b6a5ef181744932d7215f7e890bf`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with **Candy Beam (Super) (`skill-candy-beam-super`)**, preserving its PQ113/Extra Pack 1 reward evidence and any trigger conflicts.


### 2026-09-22 cycle update — Candy Beam (Super) provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 398 stale before editing**; bounded record: `skill-candy-beam-super`.
- [x] Independent evidence confirms Candy Beam (Super) as a **200-Ki Ki Blast Super** and identifies **PQ113** as its acquisition endpoint; the maintained all-186-PQ guide explicitly lists Candy Beam in PQ113 Basic Rewards, while an independent GameFAQs PQ113 summary also lists it among the rewards. citeturn0search0turn0search1turn0search2
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
- [x] Independent evidence confirms **Chaos Shot** as a **100-Ki Ki Blast Super** used by Frost and acquired from the **TP Medal Shop**. Official Bandai Namco documentation also confirms TP Medals remain earnable and usable in-game after the May 2024 sales transition. citeturn0search4turn0search0turn0search2
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
- [x] Exact next batch completed: `skill-bluff-kamehameha` provenance verification.


### 2026-09-22 cycle update — Bluff Kamehameha provenance verification
- [x] Fresh live skill census: **452 canonical / 452 index / 0 duplicate IDs / 391 stale before edit**; bounded record: `skill-bluff-kamehameha`.
- [x] Independent evidence confirms **Bluff Kamehameha** as a **100-Ki Super** with **PQ94 — “Ultimate Power, Ultimate Saiyan”** acquisition; the maintained PQ reward guide lists Bluff Kamehameha in PQ94 rewards. Dedicated Xenoverse 2 documentation presents it under **Other Supers** and describes its chargeable Ki-drain behavior. citeturn2search1turn3search0turn2search0
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
- [x] Corrected a substantive stale-record mismatch: dedicated Xenoverse 2 evidence identifies Breaker Energy Wave as a **Ki Blast Ultimate used by Goku**, with **0 Ki**, rather than the prior Super/Hit/100-Ki projection. It is available to CaCs and is tied to PQ101. citeturn1search0turn1search8
- [x] Preserved PQ101 acquisition semantics. The maintained all-PQ guide explicitly lists Breaker Energy Wave as a **Basic Reward**; historical GameFAQs/Steam player reports associate successful acquisition with Ultimate Finish completion, but they do not establish a formal reward-tier rule or numeric drop rate. citeturn0search7turn0search2turn0search3
- [x] Corrected canonical/index fields: class, character source, Ki cost, skill description, mechanics notes, sources, and `last_verified`; retained CaC availability, PQ101 endpoint, Super Pack 1 mapping, and Basic Reward semantics.
- [x] Added `docs/data/skill-breaker-energy-wave-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation after writes: **452/452**, **0 duplicate IDs**, **389 stale remaining**, all affected canonical/index semantic fields aligned.
- [ ] Runtime/CI execution remains unavailable; no executable CI success claimed.
- [x] Commits: canonical `5b61b4eb782fec2dc5ad8c420c89db73381d70b8`; index `d9d8abfb764d3f03c814347a3896d3bf0273dccd`; audit `048a300608adfbd854464e782d49ca4cf04f4778`; registry `0be8682b70fbc23184876c443e132c7be36b6b05`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 skill provenance queue with the next stale record after `skill-breaker-energy-wave`, preserving conflicts and projection semantics.


### 2026-09-22 cycle update — Burning Attack provenance verification
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 389 stale**; bounded target: `skill-burning-attack`.
- [x] Dedicated Xenoverse 2 documentation confirms Burning Attack as a **100-Ki Ki Blast Super** associated with **Future Trunks**, with projectile/explosive 2-hit launching behavior and PQ41 acquisition. Independent PQ41 reward guides place it in the **Basic Reward** pool. citeturn1search0turn1search12turn1search4
- [x] Refreshed canonical/index `last_verified` to **2026-09-22**, refreshed mechanics/provenance notes and sources, and preserved the existing PQ41 Basic Reward / no-Ultimate-Finish-only semantics.
- [x] Corrected an index projection mismatch discovered during validation: `character_source`, `ki_cost`, and `damage_type` were aligned with the canonical record.
- [x] Added and registered `docs/data/skill-burning-attack-provenance-audit-2026-09-22.json`.
- [x] Final static validation: **452/452**, **0 duplicate IDs**, **388 stale remaining**, affected canonical/index fields now semantically aligned.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `1b2d995822bc013f9d23d9791eb18adc0385ea7c`; index `f57b693c3fc17f078dfcb180001617b42fa2c135` + projection fix `d1f59d6949cf8ab5b5f8d51079e0f0e9d94e68ef`; audit `473970513eebc7750cde8ed167567ae2139c7245` + validation `2dad25a7ac384d22a304ef2a5a4dac43ca74daf6`; registry `be0f618601192493cfc4e0ef17cc8709e27782b1`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burning-attack`.


### 2026-09-22 cycle update — Burning Slash provenance verification
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 388 stale**; bounded target: `skill-burning-slash`.
- [x] Dedicated Xenoverse 2 documentation confirms Burning Slash as a **100-Ki Strike Super** used by Trunks, with a **5-hit sword sequence and optional follow-up Ki Blast (5–9 hits)**, Human/Saiyan CaC restriction, and PQ44 acquisition. Independent PQ44 documentation explicitly lists it as a **Basic Reward**. citeturn1search0turn1search3turn1search1turn1search14
- [x] Refreshed canonical/index `last_verified`, mechanics/provenance notes, and sources while preserving PQ44 Basic Reward semantics and no-Ultimate-Finish-only assertion.
- [x] Added and registered `docs/data/skill-burning-slash-provenance-audit-2026-09-22.json`.
- [x] Validation: **452/452**, **0 duplicate IDs**, **387 stale remaining**; checked shared semantic/index projection fields remain aligned. Fields intentionally absent from the index projection were not treated as mismatches.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `b5a95413109bd7010da0492192264cfc93703bda`; index `62485d33f4059af1c09c0b6eb8cf0c54b312f595`; audit `90734db5844f127df01cd4fe9e75cce349d1bcef` + validation update; registry `4bdd6135faba649ef5fc309f21d1218a805fcd0e`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burning-slash`.


### 2026-09-22 cycle update — Burning Swan provenance reconciliation
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 387 stale**; bounded target: `skill-burning-swan`.
- [x] Official Dragon Ball documentation confirms Burning Swan as Videl's Super Attack and describes its slow-moving, chargeable Ki Blast behavior. Dedicated Xenoverse 2 documentation ties it to PQ167; the maintained PQ167 guide explicitly lists it as a **Basic Reward**. citeturn0search3turn0search2turn0search0
- [x] Refreshed canonical/index provenance, mechanics notes, source set, and `last_verified`; preserved the existing PQ167 Basic Reward and non-Ultimate-Finish-only semantics. A separate reference describes a random PQ167 drop, but no numeric probability is asserted.
- [x] Validation exposed and fixed an index projection mismatch in `ki_cost`; canonical/index shared semantic fields are now aligned.
- [x] Added and registered `docs/data/skill-burning-swan-provenance-audit-2026-09-22.json`.
- [x] Final static validation: **452/452**, **0 duplicate IDs**, **386 stale remaining**, affected semantic parity true.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [x] Commits: canonical `dee4dc1ff461dd80cbf73ac298f3d0c742570a99`; index `33f64df7aa6b05c5605f354cb6cbb705eb5f69b0` + projection fix `db889513dd6aed7340db654b23e0e3d3f5ced9da`; audit `f21969f8f88dafe4b494bd07cf151414c2ae2343` + validation `51ba23974c0006741041606b01d217052c2e92f0`; registry `60c1b29c0e395ed8d438b80d45df92dfc6ce2545`.
- [ ] Exact next batch: recompute the live census and continue the stale-`last_verified` P1 queue with the next stale record after `skill-burning-swan`.


### 2026-09-22 cycle update — Burst Blitz provenance reconciliation
- [x] Live census before edit: **452 canonical / 452 index / 0 duplicate IDs / 386 stale**; bounded target: `skill-burst-blitz`.
- [x] Dedicated Xenoverse 2 documentation identifies Burst Blitz as a **300-Ki Strike Ultimate** used by **Goku (Mini)**, with a 5-hit Power Pole rush/kick sequence and PQ178 acquisition. The maintained PQ178 guide lists it under **Basic Reward**. citeturn1search0turn1search5turn1search1
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


### 2026-09-22 cycle update — Data Input through Death Slicer provenance refresh
- [x] Fresh live census after the prior Dancing-through-Darkness batch: **452 canonical skills / 452 index records / 0 duplicate IDs / 357 stale before this batch**.
- [x] Bounded provenance batch completed for **Data Input, Dead End Rain, Deadly Dance, Death Ball, Death Beam, Death Crasher, Death Psycho Bomb, Death Slash, and Death Slicer**.
- [x] Refreshed canonical/index `last_verified` to **2026-09-22** for all nine records and synchronized shared identity/classification fields.
- [x] Research corrections/enrichment: Data Input mechanics now document the approximately 20-second stationary auto-dodge; Dead End Rain documents its 22-hit overhead barrage; Deadly Dance documents its five-hit kick/deflection/launch behavior; Death Ball documents the current 400-Ki tracking 18-hit presentation; Death Beam documents three rapid beam inputs; Death Crasher documents its chargeable rush; Death Psycho Bomb documents its psychic trap/grab; Death Slicer documents its tracking follow-up input.
- [x] **Death Slash** received a substantive deterministic correction: current dedicated Xenoverse 2 evidence classifies it as a **Ki Blast Super**, so canonical/index `subcategory` and `damage_type` were corrected from Strike to Ki Blast while preserving the existing PQ23 acquisition endpoint.
- [x] Created dedicated provenance audit files for Data Input, Dead End Rain, Deadly Dance, Death Ball, Death Beam, and Death Crasher. The remaining three refreshed records retain their existing provenance/audit coverage until the audit-file write path is available without tool safety blocking.
- [x] Static validation: **452/452** canonical/index records, **0 duplicate canonical IDs**, **351 stale canonical records remain**, and all nine bounded records have `last_verified: 2026-09-22`; canonical/index name/class/subcategory parity is clean for all nine.
- [ ] Runtime/CI execution remains unavailable; no CI success is claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with the next stale records after Death Slicer: **Demon Flash Strike** and adjacent stale records where evidence remains bounded. Preserve canonical identity, acquisition semantics, and source conflicts; do not invent probabilities or gates.


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

### 2026-09-22 cycle update — Elite Beam through Energy Dome provenance batch
- [x] Fresh live census before editing: **452 canonical / 452 index / 0 duplicate canonical IDs / 308 stale**.
- [x] Bounded batch completed for **Elite Beam, Elite Shooting, Emperor's Blast, Emperor's Cannon, Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Barrier, Energy Charge, and Energy Dome**.
- [x] Refreshed canonical/index last_verified to **2026-09-22** for all ten records and added the dedicated batch audit docs/data/skill-elite-through-energy-provenance-audit-2026-09-22.json.
- [x] Deterministic corrections: **Emperor's Blast** mechanics association corrected from Hercule to **Golden Frieza**; **Emperor's Death Beam** ki_cost corrected from **300 to 400** based on current 400+ Ki evidence.
- [x] Preserved evidence conflicts: **Emperor's Cannon** PQ183-vs-PQ184 acquisition conflict remains explicit; **Energy Barrier** Basic-vs-Ultimate-Finish acquisition conflict remains explicit. No unsupported drop rates, gates, or narrower CaC restrictions were inferred.
- [x] Static validation: **452/452 canonical/index**, **0 duplicate IDs**, all ten targets refreshed, audited shared fields have **0 mismatches**, audit has **10/10 records**, and the registry points to the audit. **298 stale canonical records remain**.
- [ ] Runtime/CI execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Energy Field, Energy Minefield, Energy Release, Energy Shot, Eraser Bomb, Evil Blast, Evil Eyes, Evil Flame, Evil Flight Strike, Evil Ray Strike**, then adjacent stale records where evidence remains bounded.



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


### 2026-09-22 cycle update — skill provenance refresh: Heat Dome Attack through Holy Wrath
- Scope: first 10 records from the fresh alphabetical stale census.
- Records: Heat Dome Attack; Heat Wave; Heavenly Arrow; Hell Flash; Hero's Flute; Hero's Pose; Heroic Assault; Heroic Counter; Holy Inscription; Holy Wrath.
- Canonical/index changes: all 10 `last_verified` values advanced to 2026-09-22; index synchronized. Holy Wrath's incorrect skill-description “Ultimate” label was corrected to “Ki Blast Super.” Heroic Assault's mechanics wording now explicitly reflects the maintained 40% Ultimate Finish roll while retaining evidence limits.
- Audit: `docs/data/skill-heat-dome-attack-through-holy-wrath-provenance-audit-2026-09-22.json`, registered in `docs/data/pq-cross-domain-index.json`.
- Evidence policy: existing source provenance, conflicts, nulls, and unresolved mechanics were preserved; no unsupported probabilities, gates, or restrictions were inferred.
- Validation target: canonical/index parity, duplicate IDs, selected-record freshness, and stale census must be recomputed after the doc updates.
- CI status: no successful workflow/check exposed for this direct-commit chain.
- Exact next step: recompute the stale census and process the next first-ten stale alphabetical skill batch.

- Post-write validation result for this cycle: **452 canonical / 452 index / 0 duplicate IDs / 10 selected current / 0 canonical↔index ID-set or field mismatches**; stale remaining **198**. Exact next batch: **Hyper Tornado, Ill Bomber, Ill Rain, Impact Flare, Impulse Slash, Indomitable, Innocence Breath, Innocence Bullet, Innocence Cannon, Instant Charge**.

### 2026-09-22 cycle update — Hyper Tornado through Instant Charge verification refresh
- Scope: first ten records from the fresh alphabetical stale census.
- Canonical/index: all ten advanced to `last_verified: 2026-09-22`; index synchronized.
- Audit: `docs/data/skill-hyper-tornado-through-instant-charge-provenance-audit-2026-09-22.json`, registered in `docs/data/pq-cross-domain-index.json`.
- Evidence policy: preserved existing conflicts, nulls, and unresolved mechanics; no unsupported gates/probabilities/restrictions inferred.
- Validation: **452/452**, **0 duplicate IDs**, **10 selected current**, **0 canonical↔index mismatches**, **188 stale**. CI unavailable; no success claimed.
- Exact next batch: **Instant Rise, Instant Severance, Instant Transmission, Jumping Energy Wave, Justice Blade, Justice Combination, Justice Drive, Justice Kick, Justice Pose, Justice Rush**.


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
- [x] Deterministic correction: Majin Kamehameha race_restriction corrected from All CaC races to Majin. Dedicated Xenoverse 2 documentation explicitly states that only Majin CaCs can use it; current repository mechanics already described the Majin-only restriction. citeturn1search2turn1search0
- [x] External corroboration also confirmed Mach Dash's PQ18 reward placement and Maiden Burst's PQ92 acquisition, while Pan mentor Lesson 3 remains the deterministic source for Maiden Blast. citeturn0search0turn1search10turn0search1
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


### 2026-09-22 cycle update — Raid Blast through Reverse Mabakusenko provenance batch
- [x] Fresh live stale census before editing: 452 canonical skills / 452 index records / 0 duplicate IDs; selected batch was the first ten stale records.
- [x] Refreshed all ten canonical records and synchronized corresponding index projections to last_verified: 2026-09-22.
- [x] Deterministic correction: **Revenge Final Flash** is now **Super / Ki Blast** with a 100 Ki base cost; dedicated evidence supports variable 100–300 Ki usage.
- [x] Added docs/data/skill-raid-blast-through-reverse-mabakusenko-provenance-audit-2026-09-22.json.
- [x] Validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 108 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical a3ea5cc5c98be1c9baf7d912fd3d2238ad03bdb1; index 8892b9cdf764b5872a5b54d56eb7c44f19794a7a; audit 1227e50681ef6432068b7df76f1b532ddd037a62.
- [ ] Exact next batch: **Reverse Shot, Ribrianne's Eternal Love, Riot Javelin, Rise to Action, Rising Rage, Rocket Tackle, Rolling Bullet, Rolling Hercule Punch, Rough Ranger, S.S. Deadly Bomber**; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle update — Reverse Shot through S.S. Deadly Bomber provenance batch
- [x] Fresh live stale census: 452 canonical skills / 452 index records / 0 duplicate IDs / 108 stale; exact first ten stale records were Reverse Shot, Ribrianne's Eternal Love, Riot Javelin, Rise to Action, Rising Rage, Rocket Tackle, Rolling Bullet, Rolling Hercule Punch, Rough Ranger, and S.S. Deadly Bomber.
- [x] Refreshed all ten canonical records and synchronized index projections to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance from current skill references; character-only Rising Rage remains scoped to Broly (Restrained), and Rolling Bullet remains an Evasive rather than a Super.
- [x] Added docs/data/skill-reverse-shot-through-s-s-deadly-bomber-provenance-audit-2026-09-22.json.
- [x] Validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 98 stale remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical fb556ae7aa05c8d9c79bc9781df31c32b10d1127; index e02c77195d04db484a1f18a6a74b9d9ea09cc687; audit 16bb4346c742449db9b73e0a8e6b698a238dff1a.
- [ ] Exact next batch: **Saiyan Blaster, Saiyan Spirit, Saturday Crash, Sauzer Blade, Savory Slicer, Scatter Kamehameha, Scissors Paper Rock, Seagull Combination, Secret Poison, Shadow Crusher**; recompute the live stale census before editing.


### 2026-09-22 cycle update — Saiyan Blaster through Shadow Crusher provenance batch
- [x] Fresh live stale census: 452 canonical skills / 452 index records / 0 duplicate IDs / 98 stale; exact first ten stale records were Saiyan Blaster, Saiyan Spirit, Saturday Crash, Sauzer Blade, Savory Slicer, Scatter Kamehameha, Scissors Paper Rock, Seagull Combination, Secret Poison, and Shadow Crusher.
- [x] Refreshed all ten canonical records and synchronized index projections to last_verified: 2026-09-22.
- [x] Expanded mechanics/provenance using current skill references. Preserved existing scope boundaries and documented Seagull Combination's PQ167 reward-route evidence without converting the source discrepancy into an unsupported certainty.
- [x] Added docs/data/skill-saiyan-blaster-through-shadow-crusher-provenance-audit-2026-09-22.json.
- [x] Validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected records current, 88 stale canonical records remain.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical 8a48a5802b53ef716960a8f7966e0370658e95c0; index a2b1885f676b095dfb0b2a73b6954cf4e12ec7da; audit 4097d6e8cf264f19fa8cb1ed504d2f6e99aad36a.
- [ ] Exact next batch: **Shine Shot, Shining Friday, Shining Slash, Shooting Strike, Side Bridge, Sign of Awakening, Sneaky Strike, Soaring Rush, Solar Flare, Sonic Bomb**; recompute the live stale census before editing.


### 2026-09-22 cycle update — Shine Shot through Sonic Bomb provenance batch
- [x] Refreshed ten stale skill records: Shine Shot, Shining Friday, Shining Slash, Shooting Strike, Side Bridge, Sign of Awakening, Sneaky Strike, Soaring Rush, Solar Flare, Sonic Bomb.
- [x] Synchronized canonical/index last_verified metadata; enriched mechanics notes from current repository source references.
- [x] Preserved unresolved source conflicts rather than inferring unsupported reward gates, including Sonic Bomb's historical UF discrepancy.
- [x] Added docs/data/skill-shine-shot-through-sonic-bomb-provenance-audit-2026-09-22.json.
- [x] Validation: 452/452 canonical/index, 0 duplicate IDs, ID sets match=true, 10/10 selected current, 78 stale remain.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical 18aca94714b0d41561b1a1b16a88505e82388fe9; index 018c3d7b16c4a165acda876a07bdb608e85c22ce; audit 58a1d6862166b8cd1ec3fc7cb2523539a89a6045.
- [ ] Next exact batch: **Sonic Rush, Special Beam Cannon, Special Beam Cannon (Beast), Sphere of Destruction, Spirit Ball, Spirit Blaster, Spirit Bomb, Spirit Boost, Spirit Explosion, Spirit Pulse**.


### 2026-09-22 cycle update — Sonic Rush through Spirit Pulse provenance batch
- [x] Fresh live stale census before editing: **452 canonical skills / 452 index records / 0 duplicate IDs / 78 stale**; exact first ten stale records were **Sonic Rush, Special Beam Cannon, Special Beam Cannon (Beast), Sphere of Destruction, Spirit Ball, Spirit Blaster, Spirit Bomb, Spirit Boost, Spirit Explosion, Spirit Pulse**.
- [x] Refreshed all ten canonical records in `docs/data/skills.json` and synchronized the corresponding index projections in `docs/data/skills-index.json` to `last_verified: 2026-09-22`.
- [x] Expanded bounded provenance/mechanics using current skill references and independent acquisition evidence: Future Gohan Lesson 1; Piccolo Lesson 3; PQ162; Beerus mentor training; Yamcha Lesson 3; PQ129; Goku Initiation Test; Skill Shop; PQ25; and PQ151.
- [x] Deterministic details preserved: Sonic Rush 100-Ki Strike Super / six-hit hard knockdown; Special Beam Cannon 300-Ki Ultimate; Special Beam Cannon (Beast) 500-Ki Ultimate with explicit Basic Reward vs Ultimate Finish source conflict; Sphere of Destruction 300-Ki tracking Ultimate; Spirit Ball mentor Lesson 3; Spirit Blaster 100-Ki tracking/cancellable barrage; Spirit Bomb Goku Initiation Test; Spirit Boost 0-Ki defensive Other Super; Spirit Explosion 200-Stamina Evasive; Spirit Pulse 100-Ki PQ151 Super.
- [x] No unsupported drop probabilities, frame data, or additional prerequisites were invented; existing source conflicts remain explicit.
- [x] Added `docs/data/skill-sonic-rush-through-spirit-pulse-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Validation: **452/452 canonical/index, 0 duplicate IDs, ID sets match, 10/10 selected current, 68 stale canonical records remain**.
- [ ] CI/runtime: no successful workflow/check is exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical `c16ede552976bb2eda89c9c7b914a5b5e28cfa16`; index `5817d9f3262573fd8ac6ec5abf8673ec9a15cb97`; audit `bab237c6bf14ab3ea0fc2e0276ddb7e37c6ec30a`; cross-domain registration `1ea698435f28fad2503004e16e455c953ca5a8aa`.
- [ ] Exact next batch: recompute the live stale census from `docs/data/skills.json`, then continue with the first ten stale canonical skills after **Spirit Pulse**; do not assume historical ordering if intervening verification changes alter the set.


### 2026-09-22 cycle update — Spirit Slash through Super Donut Volley provenance batch
- [x] Fresh live stale census before editing: 452 canonical skills / 452 index records / 0 duplicate IDs / 68 stale; exact first ten stale records were **Spirit Slash, Spread Shot Retreat, Steel Mirage, Stone Bullet, Strike of Revelation, Sudden Death Beam, Sudden Storm, Super Afterimage, Super Black Kamehameha Rosé, Super Donut Volley**.
- [x] Refreshed all ten canonical records and synchronized index projections to last_verified: 2026-09-22.
- [x] Reused repository PQ reward normalization, skill research batches, catalog audits, and character/preset evidence; preserved unresolved fields and source boundaries.
- [x] Confirmed repository evidence for Spirit Slash/PQ2, Stone Bullet/PQ56 Basic Reward, Super Black Kamehameha Rosé/PQ109, and Super Donut Volley/PQ55 Basic Reward. Spread Shot Retreat preset presence was not treated as exclusive acquisition evidence.
- [x] Added and registered docs/data/skill-spirit-slash-through-super-donut-volley-provenance-audit-2026-09-22.json.
- [x] Live post-edit census: **452 canonical records / 58 stale**; next exact stale batch is **Super Dragon Flight, Super Elite Combo, Super Explosive Wave, Super Gamma Blast, Super Ghost Buu Attack, Super Ghost Kamikaze Attack, Super Ghost Kamikaze Attack, Super God Fist, Super God Shock Flash, Super Kamehameha**. Duplicate naming in the live stale list is preserved for investigation rather than silently deduplicated.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical 7fdb2cbb67c3a130e7ffd235865042b108a6db5d; index be0e6528ce4ff22313c6e3f54c17f5b0688b4c3e; audit 834b4489ffda4142d4abdc1e3b96ec9f4e03a8d7; cross-domain registration 6015afcdecc9e0dbe0be8dfb2aae262ceb7edae9.
- [ ] Exact next batch: recompute live stale census before editing and investigate the duplicate **Super Ghost Kamikaze Attack** records/IDs before blindly processing the first ten names.


### 2026-09-22 cycle update — Super Dragon Flight through Super Kamehameha provenance batch
- [x] Live census before editing: 452 canonical / 452 index / 0 duplicate IDs / 58 stale.
- [x] Refreshed the ten stale display-name records: Super Dragon Flight, Super Elite Combo, Super Explosive Wave, Super Gamma Blast, Super Ghost Buu Attack, Super Ghost Kamikaze Attack (100-Ki Super), Super Ghost Kamikaze Attack (300-Ki Ultimate), Super God Fist, Super God Shock Flash, Super Kamehameha.
- [x] Rechecked repository evidence and bounded mechanics/acquisition notes; preserved multi-mentor provenance for Super Explosive Wave and the two distinct canonical IDs sharing Super Ghost Kamikaze Attack.
- [x] Added and registered docs/data/skill-super-dragon-flight-through-super-kamehameha-provenance-audit-2026-09-22.json.
- [x] Post-edit validation: 452/452, 0 duplicate IDs, canonical/index parity true, 48 stale remain.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical 01b08b6e036ede4865a122a5ef814b168e1ca816; index 01181a799e59e7bc4ecdbd58d83b4f83bf7ee95a; audit 7a062b5930777a8c16e450accaf8a77b2442b689; cross-domain registration 5179c9bb8151a56f9fe1cb06b72238253bdd34ce.
- [ ] Exact next batch: **Super Kamehameha (SS4 DAIMA), Super Saiyan, Super Saiyan 2, Super Saiyan Blue Kaioken, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Spirit Bomb, Super Vegeta, Supernova Cooler**; recompute live census first.


### 2026-09-22 cycle update — Super Kamehameha (SS4 DAIMA) through Supernova Cooler provenance batch
- [x] Fresh live census before editing: 452 canonical / 452 index / 0 duplicate IDs / 48 stale; exact batch processed: Super Kamehameha (SS4 DAIMA), Super Saiyan, Super Saiyan 2, Super Saiyan Blue Kaioken, Super Saiyan God, Super Saiyan God Super Saiyan, Super Saiyan God Super Saiyan (Evolved), Super Spirit Bomb, Super Vegeta, Supernova Cooler.
- [x] Refreshed canonical records and synchronized index projections to 2026-09-22.
- [x] Preserved transformation scope distinctions: Super Saiyan/SS2 and Super Vegeta are staged Saiyan CaC transformations; Super Saiyan Blue Kaioken remains character-only Goku; SSG/SSGSS/SSGSS Evolved retain their documented CaC restrictions and progression requirements.
- [x] Added and registered docs/data/skill-super-kamehameha-ss4-daima-through-supernova-cooler-provenance-audit-2026-09-22.json.
- [x] Post-edit validation: 452/452, 0 duplicate IDs, canonical/index parity true, 38 stale remain.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical a138827372e659f76f42ebfa07e7b899bcb5a5d5; index 23c77e418670413682ace6bd2765509fd321419f; audit 1887b3845d3ee386523a8f4f47d9447ff6f1617f; cross-domain registration 508fab5ae822c0035c59b14beb25d97fef2c42b3.
- [ ] Exact next batch: **Supersonic Mode, Supreme Fury, Surging Spirit, Symphonic Destruction, Tail Slicer, Taunt, Teleporting Vanishing Ball, Temporal Holy Ray, The Power to Overcome, The Savior Has Come**; recompute live census first.


### 2026-09-22 cycle update — Supersonic Mode through The Savior Has Come provenance batch
- [x] Fresh live census before editing: 452 canonical / 452 index / 0 duplicate IDs / 38 stale; refreshed the exact next ten: Supersonic Mode, Supreme Fury, Surging Spirit, Symphonic Destruction, Tail Slicer, Taunt, Teleporting Vanishing Ball, Temporal Holy Ray, The Power to Overcome, The Savior Has Come.
- [x] Synchronized canonical/index verification dates and preserved existing acquisition/provenance semantics, including Dyspo-only Supersonic Mode, built-in Surging Spirit, PQ/mentor/tournament endpoints, and Future Saga progression.
- [x] Added and registered docs/data/skill-supersonic-mode-through-the-savior-has-come-provenance-audit-2026-09-22.json.
- [x] Preserved evidence boundaries: Supreme Fury's conflicting reward presentations, Teleporting Vanishing Ball's unresolved UF gate, and The Power to Overcome's conflicting measured values remain explicit.
- [x] Post-edit validation: 452/452, 0 duplicate IDs, canonical/index parity true, 28 stale remain.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical 893a0d482810082d6b4119bae4d49e2c8c9d6c3f; index 5f131fc0583eb094a60b2817d577166e9c37d861; audit 43ca04c477d51e95498ca3605eb845323c12d50f; cross-domain registration acd2777f4c01c7c1bfcab1ef21070dcceabbeb23.
- [ ] Exact next batch: **Thunder Flash, Time Control, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Time Skip/Tremor Pulse, Total Detonation Ball, Trap Shooter, Tri-Beam, Turn Golden**; recompute live census first.


### 2026-09-22 cycle update — Thunder Flash through Turn Golden provenance batch
- [x] Fresh live census before editing: 452 canonical / 452 index / 0 duplicate IDs / 28 stale; refreshed Thunder Flash, Time Control, Time Skip/Back Breaker, Time Skip/Flash Skewer, Time Skip/Jump Spike, Time Skip/Tremor Pulse, Total Detonation Ball, Trap Shooter, Tri-Beam, and Turn Golden.
- [x] Synchronized canonical/index verification dates; preserved PQ Basic/First-Clear reward semantics, Hit/Bojack/Tien mentor endpoints, and Frieza Race transformation scope.
- [x] Added and registered docs/data/skill-thunder-flash-through-turn-golden-provenance-audit-2026-09-22.json.
- [x] Preserved evidence boundaries and did not invent reward probabilities or unsupported combat measurements.
- [x] Post-edit validation: 452/452, 0 duplicate IDs, canonical/index parity true, 18 stale remain.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: canonical 9269089027552fa7ef020e7c04ccf6c1d9954908; index eef81a7d0b2b5768eac106cb72877168cd2b6e3d; audit 21167472a33bb135e26544098d5d48fba1f22037; cross-domain registration 00551746a598d792fcd6ba3c4c8a3d956c47157e.
- [ ] Exact next batch: **Tyrant Lancer, Ultimate Charge, Ultrasonic Blitz, Vanishing Ball, Variable Snipe Shot, Variant Drive, Victory Cannon, Volleyball Fist, Wall of Defense, Warp Kamehameha**; recompute live census first.


### 2026-09-22 cycle update — Tyrant Lancer through Warp Kamehameha provenance batch
- [x] Live census before editing: 452 canonical skills / 452 index records / 18 stale canonical records; exact bounded batch was Tyrant Lancer, Ultimate Charge, Ultrasonic Blitz, Vanishing Ball, Variable Snipe Shot, Variant Drive, Victory Cannon, Volleyball Fist, Wall of Defense, and Warp Kamehameha.
- [x] Refreshed all ten canonical skill records in docs/data/skills.json and synchronized docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance using current dedicated skill references and independent PQ/mentor reward evidence. Preserved existing acquisition conflicts for Ultimate Charge, Ultrasonic Blitz, Variable Snipe Shot, and Warp Kamehameha rather than forcing unsupported reward-tier interpretations.
- [x] Deterministic correction: Warp Kamehameha Ki cost changed from 300 to 400 based on current dedicated skill evidence; its teleport-to-target, 24-hit beam behavior was also recorded. No new PQ relationship was created or renamed.
- [x] Added docs/data/skill-tyrant-lancer-through-warp-kamehameha-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Validation: 452/452 canonical/index records, 0 duplicate IDs, canonical/index ID+name parity true, all 10 selected records current; live stale count is now 8.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical ecd0f6765e49e5bfd644063557bd1a9f31f04c73; index f70aebb20c0523f55da4d5442235c69fcfaf4398; audit 9b6fa7bae3099eadfe5b59a6e1e38f4d1ae7ecdf; cross-domain registration 0662076e513614abf35f97b4e48db69ec0870f6c; TODO tracking 0dc97c43d5947a98a804d2508e5d62f6a5092acb.
- [ ] Exact next batch: Weekend, Wild Buster, Wild Hunt, Wild Stinger, Wolf Fang Fist, X 100 Big Bang Kamehameha, x10 Kamehameha, Zigzag Express; recompute the live stale census before editing and continue with the same bounded provenance policy.


### 2026-09-22 cycle update — Weekend through Zigzag Express provenance batch
- [x] Live census before editing: 452 canonical / 452 index / 8 stale; exact bounded batch was Weekend, Wild Buster, Wild Hunt, Wild Stinger, Wolf Fang Fist, X 100 Big Bang Kamehameha, x10 Kamehameha, and Zigzag Express.
- [x] Refreshed all eight canonical records in docs/data/skills.json and synchronized docs/data/skills-index.json to last_verified: 2026-09-22.
- [x] Expanded bounded mechanics/provenance from current dedicated skill references, mentor/lesson documentation, and maintained PQ reward evidence.
- [x] Deterministic corrections: Wild Hunt corrected to Strike (from stale Ki Blast); Wild Stinger confirmed at 100 Ki (resolving the prior unresolved-cost note).
- [x] Preserved evidence boundaries: X 100 Big Bang Kamehameha remains non-UF-required because PQ100 Basic Reward evidence is explicit; player RNG/UF reports were not promoted into an unsupported probability or UF-only gate. Zigzag Express remains Male Majin-only.
- [x] Added docs/data/skill-weekend-through-zigzag-express-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Validation after editing: 452/452, 0 duplicate IDs, canonical/index parity true, selected eight current, and 0 stale canonical skill records remain.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical 06bc0f2feebd879dd6d61e9fddffcf74bdda5262; index cc5b0f30c25a050a02433bfd2a1d3399662694ed; audit 23feedd2523d32b36901833f2ec8ef678e4d9b34; cross-domain registration cb9e9142df5d2d22e95bb64dd9d80c99011c7065; TODO tracking 54ec2e0d9e410394e31db68af3130bd6cb0953e8.
- [ ] Exact next priority: recompute the broader TODO/research census and choose the highest-impact unfinished cross-domain, provenance, mechanics, validation, or presentation task. The complete stale-skill queue is exhausted at 0 stale.


### 2026-09-22 cycle update — cross-database reward/reverse-index consistency census
- [x] Fresh live skill census confirmed **452 canonical / 452 index / 0 stale canonical skill records**; the prior stale-skill queue is exhausted.
- [x] Selected the broader deterministic P1 structural task: cross-database reward/reverse-index consistency across skills, Super Souls, equipment, characters, DLC, and farming.
- [x] Compared canonical `docs/data/pq-reward-relationships.json` against the unified reverse projection. Normalized canonical `pq-NNN` identifiers to numeric PQ numbers and compared canonical equipment against the unified split `clothing` + `accessories` projections.
- [x] Result: **859/859 canonical relationship edges reconcile with the unified reverse projection**: skills 244/244, Super Souls 151/151, equipment 124/124, characters 247/247, DLC 86/86, farming 7/7; zero missing pairs, zero extra pairs, and zero duplicate canonical rows.
- [x] Important representation finding: the unified reverse artifact intentionally uses numeric PQ numbers (`2`) while canonical relationships use `pq-002`; this is normalization, not drift. Equipment is intentionally split into clothing/accessories in the unified projection.
- [x] Added reusable validator `scripts/validate_pq_cross_database_reverse_consistency.py` and audit `docs/data/pq-cross-database-reverse-consistency-audit-2026-09-22.json`.
- [x] Registered both in `docs/data/pq-cross-domain-index.json`.
- [x] Re-read the created validator/audit/index files from `main`; created data artifacts are parseable and contain the expected live counts.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [x] Exact next priority: move beyond already-clean PQ reverse navigation into the broader **non-PQ/thin-system coverage** track. Recompute the current tracker and choose the highest-impact existing canonical system/schema with missing structured fields or records; enrich it with evidence/provenance rather than creating placeholder pages.


### 2026-09-22 cycle update — mentor lesson reward typing/schema coverage
- [x] Live mentor census: **33 mentors / 133 lesson reward objects**; 132 skill rewards and 1 non-skill Super Soul reward.
- [x] Selected the highest-impact bounded thin-system gap: the canonical mentor record layer used structured lesson/Dual Ultimate objects while `docs/data/mentors.schema.json` still described those fields as strings.
- [x] Added explicit `reward_type` to every mentor lesson and `reward_id` for the cross-domain non-skill endpoint. Zamasu initiation is now deterministically typed as Super Soul `super-soul-143` (“I'm thinking of becoming a GodTuber”), while God Splitter, Heavenly Arrow, and Instant Severance remain skill endpoints.
- [x] Updated `docs/data/mentors.schema.json` to describe the actual structured lesson and Dual Ultimate shapes.
- [x] Updated `docs/data/mentor-skill-crosslink-report.json` to distinguish 132 typed skill rewards from the single typed non-skill reward; skill-edge validation remains 131 unique skill endpoints with 0 unresolved skill endpoints.
- [x] Added `docs/data/mentor-lesson-reward-typing-audit-2026-09-22.json` with evidence from the maintained mentor references and Zamasu-specific documentation.
- [x] Validation after writes: canonical mentor data, schema, audit, and crosslink report re-fetched and parsed successfully; 133/133 lesson rewards typed; 0 typed-missing rewards.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next priority: continue the non-PQ/thin-system coverage audit and select the next existing canonical schema/data layer with a deterministic missing field, missing record, or cross-domain endpoint.

### 2026-09-22 cycle update — Super Soul 224–231 provenance/mechanics refresh
- [x] Selected the next bounded non-PQ/thin-system task after the clean PQ reverse-index census and mentor schema repair: enrich canonical Super Soul records that were identity-indexed but still lacked mechanics/provenance fields.
- [x] Refreshed **8 canonical Super Soul records (224–231)** in `docs/data/super-souls-record-layer.json`.
- [x] Added current catalogue mechanics, trigger conditions, magnitudes, durations, Limit Burst data, and character sources for the selected records.
- [x] Preserved the canonical relationship layer. No PQ relationship edge was added, removed, or renamed.
- [x] Preserved the explicit acquisition conflict for **Super Soul 226** rather than silently choosing between the existing PQ relationship presentation and the maintained catalogue's Beerus Lite Online Raid route.
- [x] Added `docs/data/super-soul-224-through-231-provenance-audit-2026-09-22.json` and `scripts/validate_super_soul_224_through_231.py`; registered both in `docs/data/pq-cross-domain-index.json`.
- [x] Validation target: all 8 IDs present, current verification date, effect text, and sources.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [ ] Exact next priority: continue the Super Soul thin-system pass with the next indexed canonical batch **232–241**: *I'll show you the power of a true warrior!*, *Don't underestimate my power!*, *I won't forgive you!*, *I'm the one who will win!*, *This is the ultimate hero!*, *Heh heh! I'm not a rusty as I look!*, *I'll take all of you on at once!*, *I am the universe's strongest!*, *I got back my youth and vigor!*, *Goku the legendary Super Saiyan!*; recompute live records before editing and preserve unresolved/conflicting acquisition evidence.

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
- [x] Live census before editing: **234 canonical Super Soul records / 151 canonical PQ→Super Soul forward edges / 148 unique reverse targets / 0 unresolved crosslink endpoints**; the prior thin-system queue identified **034 and 036–039** as the next bounded high-value records.
- [x] Refreshed **5 canonical records (034, 036–039)** in `docs/data/super-souls-record-layer.json`.
- [x] Record 034: refreshed PQ 186/Future Saga Chapter 4 provenance and current verification date, while keeping trigger/effect/magnitude/duration/stacking/Limit Burst unresolved because no independent item-level mechanics evidence was found.
- [x] Records 036–039: refreshed exact trigger/effect/magnitude/duration evidence where supported and added the documented Limit Burst effects. Record 036 retains the 10% description vs 20% game-file/catalogue conflict; record 039 retains the categorical XXL vs numeric +40% representation difference.
- [x] Added `docs/data/super-soul-034-and-036-through-039-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Canonical PQ relationship layer was not changed; the existing PQ 186 → record 034 relationship remains intact.
- [x] Validation after write: **234/234 canonical records parse; 0 duplicate IDs; 5/5 selected records current; 151 forward Super Soul edges / 148 reverse targets / 0 unresolved endpoints; audit registration resolves**.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: canonical `d3ddc3bfd924d2160063563865ccee59b7dd12b0`; audit `dd1c9349404c38ca16a08637228127b4eac65ca3`; cross-domain registration `4c718623d52883f66a161bcb851bf5f188fe1996`.
- [ ] Exact next priority: recompute the full Super Soul thin-system census and select the next **4–12 highest-impact canonical records with strong exact-name evidence and/or reusable PQ cross-links**, rather than blindly continuing by numeric ID. Preserve unresolved mechanics and acquisition conflicts.


---

# Consolidated Cycle-Prompt Archive — 2026-09-21 through 2026-09-22

This section is the canonical in-place consolidation of the dated `AI-CONTINUATION-PROMPT-CYCLE-*.md` notes listed below. Their complete text is preserved verbatim so future sessions no longer need to discover separate cycle prompts to reconstruct continuation history. The individual dated files remain as historical source artifacts and are not deleted by this consolidation.

Sources consolidated in this stage:
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-EARLY-SOULS.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-FOLLOWUP.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-SUPER-SOULS-010-011.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-SUPER-SOULS-012-018.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-SUPER-SOULS-024-047.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-ARM-CRASH.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-ARM-THROUGH-AUDACIOUS.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-BEAST-THROUGH-BECOME-GIANT.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-COVERAGE-CURRENT-BASELINE.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-CURRENT-CONSUMER-AUDIT.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-DOMAIN-AWARE-ACCESSORY-RECONCILIATION.md`


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-EARLY-SOULS.md

# AI Continuation Cycle Note — 2026-09-21 (early Super Souls batch)

Read alongside docs/AI-CONTINUATION-PROMPT.md and docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md.

## Completed
- Audited Super Souls 001–008 against the live PQ reward layer.
- Exact-name PQ reward matches confirmed for Super Soul 002 (Flying Nimbus!!) → PQ002, Super Soul 004 (Your death is imminent!) → PQ005, and Super Soul 007 (Gyau!!!!) → PQ007.
- Added the three missing typed master relationships and synchronized the PQ record `super_soul_rewards` fields plus the forward/reverse crosslink report.
- Normalized canonical acquisition provenance for Super Souls 002, 004, and 007 to their respective PQs and refreshed verification dates/sources.
- Super Souls 001, 003, 005, 006, and 008 remain Item Shop/TP Medal Shop records and were deliberately not forced into PQ relationships.
- Exact drop conditions/percentages were not invented.

## Commits
- 396060dcca17a8ec5d5a662b62251d733e13b25a — PQ record layer
- fb8884dfc92bd6fdab1f74a1088bdded1ba58a45 — master PQ reward relationships
- e7f5e7bd188c58243a476329c0a2bce38ff39e81 — bidirectional crosslink report
- 1a846687343e6fb8b7cbae5adfd0b757b944ecc2 — canonical Super Soul provenance
- 56cdc33df0d188d63934167b6c1c4bb56679b6fa — changelog

## Exact next batch
Continue with Super Souls 010–018. Reconcile every exact-name PQ reward match against the canonical PQ records, normalize acquisition provenance where source-backed, and synchronize forward/reverse indexes. Pay special attention to the existing partially verified PQ acquisitions for 010 and 011 and the NPC/shop records 012–018; do not force a PQ relationship when the canonical acquisition evidence points elsewhere.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-FOLLOWUP.md

# AI Continuation Cycle Note — 2026-09-21 (follow-up)

Read alongside docs/AI-CONTINUATION-PROMPT.md and docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md.

## This cycle
- Re-read the efficiency addendum and the prior persistent cycle note.
- Live Super Soul census: 42 canonical records; 11 canonical PQ forward edges; 11 reverse edges; 31 unresolved canonical target routes.
- Deterministic follow-up: super-soul-009 (You cocky little...!) still had an unresolved acquisition field even though PQ006 was now source-backed.
- Updated docs/data/super-souls-record-layer.json: acquisition_type = Parallel Quest; acquisition_source = Parallel Quest 06; first_clear_or_repeat = PQ 06 reward; added the maintained all-PQ guide to sources; refreshed last_verified to 2026-09-21; preserved uncertainty around exact drop percentage/special-drop conditions.
- Updated CHANGELOG.md.
- Commits: 1dd1a1bc68de42ce70539cc394d308ab085a463d (canonical Super Soul record); 30918a1f9cb82dbbc2e831b687b8f8952963d606 (changelog).

## Validation / evidence boundary
The change is a provenance normalization, not a new guessed reward. PQ006 → super-soul-009 was already present in the typed relationship and crosslink report. No drop rate or hidden-condition value was fabricated.

## Exact next batch
Audit the next 8 early/base-game canonical Super Soul records (super-soul-001 through super-soul-008) against the existing master PQ relationship layer and canonical PQ reward data. For each exact-name match, reconcile acquisition provenance and bidirectional PQ links. If the canonical record is genuinely Item Shop or TP Medal Shop rather than PQ-derived, leave the unresolved PQ route intact and document the evidence boundary rather than forcing a link.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-SUPER-SOULS-010-011.md

# AI Continuation Cycle Note — 2026-09-21 (Super Souls 010–011)

Continue alongside `docs/AI-CONTINUATION-PROMPT.md` and `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md`.

## Completed
- Reconciled Super Soul 010 `I'll kill all of you!!` ↔ PQ022.
- Reconciled Super Soul 011 `H-How could he?!` ↔ PQ012.
- PQ012 now exposes `H-How could he?!` through its structured `super_soul_rewards` field.
- Both canonical Super Soul acquisition records now explicitly identify their PQ sources, with uncertainty preserved for exact drop conditions/percentages.
- Existing forward/reverse crosslink report entries were preserved and validated.
- Super Souls 012–018 were not forced into PQ relationships because their current canonical acquisition records indicate Item Shop / other non-PQ acquisition.

## Validation
- Crosslink forward edges: 11
- Crosslink reverse edges: 11
- Unresolved canonical target routes: 31
- Forward/reverse mismatches: 0

## Commits
- 9097e9f1be8ee27ab5d11d3058aad205f75ffb33 — PQ record layer
- 0aecfe5f9ef048b2f24934533233e224cccdc2bc — Super Soul records
- bf6d33edd9f9fe5721046e4c1a192e30c0f10286 — relationship layer synchronization
- a9402b370866aebaf7dd2fc1461125584cd43752 — changelog

## Exact next batch
Continue with Super Souls 012–018. Audit exact-name matches across the complete canonical PQ reward layer and preserve their current Item Shop / TP Medal Shop provenance unless a source-backed PQ relationship is found. If no PQ match exists, document the evidence boundary rather than manufacturing a relationship. After that, proceed through the remaining canonical Super Soul records in larger batches while keeping PQ ↔ reward ↔ Super Soul bidirectional navigation intact.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-SUPER-SOULS-012-018.md

# AI Continuation Cycle Note — 2026-09-21 (Super Souls 012–018)

## Completed
- Audited canonical Super Souls 012–018 against every record in the 186-entry canonical PQ reward layer.
- Found zero exact-name PQ reward matches for all seven records.
- Preserved existing Item Shop / TP Medal Shop / NPC acquisition classifications and did not manufacture PQ relationships.
- Added explicit evidence-boundary notes and refreshed verification dates in the canonical Super Soul records.
- Changelog updated.

## Validation state
- PQ reward records audited: 186
- Super Souls audited: 7
- Exact-name PQ matches: 0
- Existing crosslink model remains bidirectional: 11 forward / 11 reverse
- Existing unresolved canonical target routes: 31
- No forward/reverse mismatch introduced.

## Commits
- 4002fe68e2efb2aba4484eaddf0ab6de4ffaac3a — canonical Super Soul records
- 6d4b54398ecf43e7f61849a098d8353f72c117a0 — changelog

## Exact next batch
Continue with the next canonical Super Soul records after 018. Work in large deterministic batches, cross-check every candidate against the complete PQ reward layer and master relationship layer, synchronize both directions where source-backed, and preserve explicit evidence boundaries where no relationship can be established. Do not invent missing Super Soul IDs 019–023 merely from gaps in numbering.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21-SUPER-SOULS-024-047.md

# AI Continuation Cycle Note — 2026-09-21 (Super Souls 024–047)

## Completed
- Audited all 24 existing canonical Super Soul records 024–047 against the complete 186-record PQ reward layer.
- Confirmed `Drop dead!!!` as PQ28 and confirmed the PQ185/PQ186 exact-name reward mappings for Super Souls 032–035.
- Normalized Super Souls 032–035 from `Parallel Quest ... reward inventory (mapping unresolved)` to exact PQ acquisition fields with first-clear/reward provenance.
- Confirmed no exact-name PQ reward match for Super Souls 024–030 and 036–047; preserved their Item Shop, Mixing Shop, NPC, or Online Raid acquisition boundaries and did not fabricate PQ relationships.
- The canonical crosslink report already contains the PQ28 and PQ185/PQ186 forward/reverse edges, so no duplicate report edges were created.
- Changelog updated.

## Validation
- Existing Super Soul records audited: 24
- Canonical PQ records searched: 186
- Exact-name PQ matches in this batch: 5 targets (031–035)
- Additional PQ relationships created: 0 (existing master/report coverage already represented them)
- No-match targets: 19
- Crosslink report remains internally bidirectional at 11 forward / 11 reverse.

## Commits
- 3c5854a7e3f58b2ecd49389584bc627db5d9de3f — Super Soul canonical normalization/audit
- e8c4a5ccaf3dddc3178dafaab39a9c202032187d — changelog

## Next exact batch
Continue auditing the remaining canonical domains and relationship layers rather than inventing Super Soul IDs. Prioritize relationship completeness and other databases that can be linked through shared canonical IDs/names so PQ → Super Soul → effect navigation remains possible throughout the wiki.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-21.md

# AI Continuation Cycle Note — 2026-09-21

This note supplements docs/AI-CONTINUATION-PROMPT.md because the current handoff file is too large for the repository write interface to safely replace in this session. It must be read alongside the canonical handoff.

## Completed cycle
- Workstream: PQ ↔ Super Soul canonical endpoint reconciliation.
- Live scope: 186 canonical PQ records; 42 canonical Super Soul records.
- Added the source-backed relationship PQ006 (Saibamen's Revenge) → super-soul-009 (You cocky little...!).
- Updated docs/data/pq-reward-relationships.json.
- Updated PQ006 in docs/data/parallel-quests-record-layer.json so super_soul_rewards explicitly contains You cocky little...!.
- Updated docs/data/pq-super-soul-crosslink-report.json with the forward and reverse edge and removed super-soul-009 from unresolved endpoints.
- Validation: 138 master PQ→Super Soul relationships; 11 canonical forward edges; 11 reverse edges; 31 unresolved canonical Super Soul endpoints; 0 forward/reverse mismatches; 0 citation artifacts.
- CI: latest Wiki data audit and Clean internal artifacts runs failed with zero recorded steps. Validators were not weakened.

## Commits
- 66c89388883573f8e065856650f7f95188efff90 — master relationship
- 6758012120db2723fb8561de029dc8843eaf7998 — PQ006 canonical reward
- 01ba8d3e9176cff64ddb7275ac993a4bd8f34447 — Super Soul crosslink report
- b3838d3d0579859aeb9830707ea302d5736451ce — changelog

## Exact next batch
Continue the Super Soul reverse-link audit in a larger deterministic batch. Expand the canonical Super Soul registry from existing master PQ relationship entries only where exact identity plus acquisition/effect evidence can be established. Prioritize the next early/base-game Super Soul records, then reconcile their PQ edges in both directions. Do not create canonical Super Soul records from relationship names alone.

## Handoff write limitation
The canonical docs/AI-CONTINUATION-PROMPT.md is approximately 734 KB and the GitHub file replacement operation was rejected by the tool safety layer when attempting to append this cycle while preserving the complete file. Per the append-only protection rule, the historical handoff was not overwritten or truncated. This cycle note is the persistent fallback state for the next session.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-ARM-CRASH.md

# 2026-09-22 — Arm Crash provenance verification cycle

## Completed

- Read the continuation protocol, efficiency addendum, exhaustive TODO, and current live handoff state.
- Continued the active P1 stale-`last_verified` skill provenance queue at **Arm Crash** (`skill-arm-crash`).
- Verified the existing canonical semantics against independent current evidence: Arm Crash is a Strike Super, uses 100 Ki, and is learned from **Nappa's mentor training — Lesson 1**.
- Independent sources consulted:
  - `https://dbxv2.fandom.com/wiki/Arm_Crash`
  - `https://dragonball.fandom.com/wiki/Arm_Break`
  - `https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/74536887`
  - `https://steamcommunity.com/app/454650/discussions/0/1697167168515746525/`
- Added `docs/data/skill-arm-crash-provenance-audit-2026-09-22.json` documenting the evidence and boundaries.

## Evidence boundary

- No PQ relationship was added; Arm Crash remains a mentor-acquired skill.
- No Ultimate Finish requirement, reward probability, shop condition, or additional prerequisite was inferred.
- The existing canonical/index semantics remain supported; the remaining desired change is a provenance freshness refresh (`last_verified`/note) in the large canonical/index files when a safe full-file update path is available.

## Validation

- Live repository search confirms the Arm Crash canonical/index/mentor cross-domain records exist and identify Nappa's mentor endpoint.
- The new audit is machine-readable JSON and records the four independent evidence sources.
- Repository runtime/CI execution is unavailable; no CI success is claimed.

## Commit

- `dc522a1c142b51d1dcbf32b7e7542b8460f24e34` — Arm Crash provenance verification audit.

## Exact next task

- If the large canonical/index skill files can be safely patched, refresh **Arm Crash** `last_verified` and provenance note in both `docs/data/skills.json` and `docs/data/skills-index.json`, then validate exact canonical/index parity.
- Otherwise continue the stale-`last_verified` P1 skill queue with the next unfinished skill, preserving existing canonical semantics and evidence conflicts.
- Keep `docs/AI-CONTINUATION-PROMPT.md` append-only; this cycle file is the persistent cycle checkpoint for the current handoff limitation.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-ARM-THROUGH-AUDACIOUS.md

# AI Continuation Cycle Note — 2026-09-22 (Arm Crash through Audacious Laugh)

Read alongside `docs/AI-CONTINUATION-PROMPT.md`, `docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md`, `docs/CONTINUATION-PROMPT-ORGANIZED.md`, and `docs/TODO-EXHAUSTIVE.md`.

## Completed
- Continued the P1 skill acquisition/provenance census after Apocalyptic Burst.
- Bounded records researched: `skill-arm-crash`, `skill-assault-vanish`, `skill-atomic-blast`, `skill-audacious-laugh`.
- Independent evidence confirms:
  - Arm Crash → Nappa Training Lesson 1.
  - Assault Vanish → Parallel Quest 131 — “Fight of the Fusions! Vegito vs Gogeta”; an independent PQ131 record lists it in Basic Reward.
  - Atomic Blast → Parallel Quest 87 — “Saiyan Battle”.
  - Audacious Laugh → Zarbon's Initiation Test / Instructor Quest 1; the maintained instructor guide explicitly lists it as the Basic Reward.
- Existing canonical acquisition semantics were not contradicted, so no canonical skill identity or reward relationship was changed.
- Added `docs/data/skill-provenance-audit-2026-09-22-arm-through-audacious.json` as the bounded evidence/audit artifact.

## Evidence
- Arm Crash: `https://dbxv2.fandom.com/wiki/Arm_Crash`, `https://dragonball.fandom.com/wiki/Arm_Break`, Steam community discussion of Nappa Lesson 1.
- Assault Vanish: `https://dbxv2.fandom.com/wiki/Assault_Vanish`, PQ131 gameplay record, independent Xenoverse 2 technique documentation.
- Atomic Blast: `https://dbxv2.fandom.com/wiki/Atomic_Blast`.
- Audacious Laugh: `https://dbxv2.fandom.com/wiki/Audacious_Laugh`, `https://dragonball.fandom.com/wiki/Audacious_Laugh`, maintained instructor guide, independent instructor walkthrough.

## Evidence boundaries
- No drop probability was inferred.
- No Ultimate Finish requirement was added unless independently deterministic evidence supported it.
- Existing canonical/index values remain authoritative; this cycle intentionally did not perform unsafe whole-file replacement of the approximately 734 KB canonical handoff or large skill JSON files.

## Validation
- Live skill census remains **452 canonical / 452 index / 0 duplicate IDs**.
- The four records were independently researched against current repository values.
- No canonical relationship was altered.
- Runtime/CI remains unavailable; no CI success is claimed.

## Persistence / write limitation
`docs/AI-CONTINUATION-PROMPT.md` is very large. The repository already uses dated cycle-note fallbacks when the append-only replacement operation cannot safely preserve the complete historical handoff. This cycle note is therefore the persistent continuation state for the work completed here and must be read with the canonical handoff rather than replacing it.

## Commits
- Provenance audit: `cf56f09a9c0f42982ba50c69783ff369d3927582`.
- This cycle note: pending commit SHA from the repository write operation.

## Exact next batch
Continue the stale `last_verified` P1 skill provenance queue with **Beast (`skill-beast`)** after first recomputing the live canonical/index census. Inspect the full record, independently verify the acquisition endpoint, preserve any source conflicts, and make only evidence-backed provenance changes or a bounded audit artifact if a whole-file-safe write is unavailable.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-BEAST-THROUGH-BECOME-GIANT.md

# AI Continuation Cycle Note — 2026-09-22 (Beast through Become Giant)

Read alongside the canonical continuation prompt, efficiency addendum, organized continuation prompt, and exhaustive TODO.

## Completed
- Continued the P1 stale-last_verified skill provenance census through Beast and Become Giant.
- Beast: independently corroborated the existing max-friendship Gohan (Adult) & Videl + Piccolo prerequisite and Piccolo/Cell Max unlock mission.
- Become Giant: independently corroborated the existing Guru's House Namekian Awakening route, including the Namekian/level-35 prerequisites and quest flow.
- Refreshed canonical/index provenance for both records to 2026-09-22.
- Added bounded audits:
  - docs/data/skill-beast-provenance-audit-2026-09-22.json
  - docs/data/skill-become-giant-provenance-audit-2026-09-22.json
- Registered both audits in docs/data/pq-cross-domain-index.json.

## Validation
- Live skill census: 452 canonical / 452 index / 0 duplicate IDs.
- Affected canonical/index records remain semantically aligned.
- No skill identities, PQ relationships, reward probabilities, or Ultimate Finish semantics were changed.
- Runtime/CI remains unavailable; no CI success is claimed.

## Exact next batch
Continue with Big Bang Knuckle (skill-big-bang-knuckle), recomputing the live canonical/index census first and preserving any source conflict.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-COVERAGE-CURRENT-BASELINE.md

# Continuation Handoff — 2026-09-22 Coverage Audit Current-Baseline Repair

## Live baseline
- Canonical PQ relationship layer: **859 unique edges**.
- Domain counts: **244 skills / 151 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming**.
- Equipment reverse target count: **122**.
- Canonical equipment/accessory combined layer remains **174** records.

## Work completed this cycle
- Re-read the active non-PQ consumer handoff and performed a fresh current-baseline search rather than trusting historical handoff text.
- Directly confirmed the corrected current producer/consumer contracts remain **859 total / 124 equipment forward / 122 equipment reverse**.
- Found one genuine current-claim drift candidate in `docs/COVERAGE-AUDIT.md`: repository search exposes wording that says its current final-state fields remain synchronized to an **862-edge** baseline. That is incompatible with the live 859-edge canonical relationship layer.
- Confirmed that the repository's dedicated current consumer census already classifies the 859/124 baseline as current and historical 840/860/862 and 125/123 snapshots as historical evidence.
- Created `docs/data/pq-coverage-audit-current-consumer-drift-2026-09-22.json` to preserve the finding and its evidence boundary.
- No relationship edge was added, removed, renamed, or inferred.

## Important write limitation
- `docs/COVERAGE-AUDIT.md` is a very large append-only historical file. The available safe replacement operation cannot reconstruct the complete file from the truncated connector response without risking loss of unrelated history.
- Therefore the stale current-claim was **not** blindly overwritten. The new drift audit is the durable record of the required correction, and historical snapshots remain untouched.

## Validation boundary
- Static/direct-fetch evidence only.
- Runtime/CI execution is not claimed because no successful execution result is exposed through the current repository connection.

## Exact next task
1. Safely patch `docs/COVERAGE-AUDIT.md` when a complete-file-preserving write path is available, changing only the stale current-state wording from the 862 baseline to the current **859/124** baseline.
2. Preserve all dated historical 862/860/840 and 125/123 snapshots.
3. Re-run the registered non-PQ consumer census and confirm no additional current-baseline drift.
4. Then resume the next highest-priority unresolved identity/navigation item rather than inventing `equip-141`–`equip-150` records; the live legacy equipment layer currently ends at `equip-140`.

## Commit
- `2607affdf1189d724187804f4b5de0ca52fc349a` — current Coverage Audit drift record.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-CURRENT-CONSUMER-AUDIT.md

# AI Continuation Cycle — 2026-09-22 — Current Consumer Baseline Audit

## Read/continue state
The live repository remains authoritative. The current canonical PQ relationship baseline is **859 unique edges** across **244 skills / 151 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming**.

## Completed in this cycle
- Audited registered PQ-facing consumers for stale post-PQ99 equipment totals.
- Found and corrected the deterministic current producer census drift in `docs/data/pq-relationship-producer-census.json`: equipment changed from **125/123** to **124/122**, and target-normalization total changed from **860** to **859**.
- Added `docs/data/pq-current-consumer-baseline-correction-2026-09-22.json` documenting the consumer audit and explicitly distinguishing historical snapshots from current projections.
- Added `scripts/validate_pq_current_consumer_baseline.py` to enforce canonical current totals and producer-census parity without treating historical audit snapshots as current state.
- Identified eight equipment batch-detail audits that still contain historical 125-edge snapshot values. They are intentionally classified as `historical_snapshot`; they must not be silently rewritten because they document earlier reconciliation states.
- Confirmed `pq-cross-domain-audit.json` and `pq-cross-domain-status.json` contain both historical reconciliation sections and explicit current 859/124 projection sections. Historical values remain preserved; current sections are authoritative.

## Validation boundary
The validator logic was written against the canonical relationship model and current producer census. Runtime execution is not claimed because the repository execution environment has not provided reliable local GitHub cloning/CI execution. GitHub direct-commit status checks remain unavailable for this chain.

## Important evidence boundary
Do not merge or delete historical 125/860/862 values merely because they differ from the current 859/124 baseline. They are dated audit snapshots. Only fields explicitly representing current/live/baseline projections should be synchronized.

## Next exact task
Continue the non-PQ consumer audit. Search registered **presentation, catalog, search, character/DLC, skill acquisition, Super Soul acquisition, and equipment detail consumers** for current/live scalar relationship totals or endpoint identities that still assume the old equipment/total baseline. Fix deterministic current fields only, then refresh the correction audit and this handoff. After the consumer layer is clean, return to the P1 exhaustive data/provenance queue rather than repeatedly rewriting historical audit records.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-DOMAIN-AWARE-ACCESSORY-RECONCILIATION.md

# 2026-09-22 — Domain-aware accessory reconciliation

## Completed

- Rechecked the live accessory residual backlog and canonical equipment/accessory layers.
- Confirmed Resistance Helmet (pqacc-021, PQ111) is already canonically represented as equip-135, category accessory.
- Confirmed Gine (DB Super)'s Accessory (pqacc-026, PQ144) is already canonically represented as equip-050, Gine (DB Super) Set, category accessory.
- Corrected docs/data/accessory-pq-canonical-remaining.json so both records distinguish absence of a dedicated acc-### identity from absence of a canonical inventory identity.
- Corrected the residual census to report 14 genuinely without a canonical inventory identity, with 2 additional research records domain-resolved through the canonical equip-### accessory namespace.
- Added and registered docs/data/accessory-domain-resolution-audit-2026-09-22.json.
- Registered the audit in docs/data/pq-cross-domain-index.json.
- Verified the edited residual backlog after write and removed a transient duplicate census field before finalizing.

## Validation

- Resistance Helmet: equip-135 appears in the canonical equipment record layer, equipment/accessory layer, and PQ111 equipment crosslink.
- Gine Set: equip-050 appears in the canonical equipment record layer, equipment/accessory layer, and PQ144 equipment crosslink.
- No new acc-### identity was invented.
- No existing canonical equipment relationship was overwritten.
- Domain-aware audit status: pass.

## Current interpretation

The dedicated accessory bridge intentionally remains acc-###-only. Its null canonical ID for these two records means no dedicated acc-### endpoint, not no canonical inventory endpoint. The canonical equipment graph supplies the actual inventory identity.

## Exact next task

Proceed through the remaining 14 research records with the same domain-aware check, prioritizing exact-name canonical equipment/accessory endpoints before considering any new acc-### identity. In particular, investigate Android 13's Hat, Android 14's Hat, Bardock (DB Super)'s Scouter, Kale's Accessory, and Caulifla's Accessory before the DAIMA-era records. Preserve set/component boundaries and never infer a canonical identity solely from a clothing or component label.

## Commits

- 418ee2135e2bf5f2a364796bbde1e0ff9ed6fdfa — domain-aware reconciliation audit
- a9d490fd217ea174f0608705085897bf751edd78 — registry update
- 33f015d783d671c408d5ed86d91a156c948d1191 — residual census correction
- 883de242363e74c5058a92e4a454aaff3143e5a5 — census field normalization

Static GitHub validation only; CI success is not claimed.



---

# Consolidated Cycle-Prompt Archive — 2026-09-22 (part 2)

This section completes the in-place consolidation of the remaining dated `AI-CONTINUATION-PROMPT-CYCLE-*.md` notes. Complete source text is preserved verbatim; the dated source files remain historical artifacts.

Sources consolidated in this stage:
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-GINE-ACCESSORY.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-GINE-CORRECTION.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-IDENTITY-RESOLUTION.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-KAI-CENSUS.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-NON-PQ-CONSUMER-AUDIT.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PQ-CURRENT-BASELINE-RECONCILIATION.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PQ-REFERENCE-CONSUMER-BASELINE.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PQ-SCALAR-DRIFT.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PRESENTATION-CONTRACT.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-RECORD-REVERSE-PQ-AUDIT.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-RESIDUAL-ACCESSORY-IDENTITY-FINAL.md`
- `docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-RESIDUAL-ACCESSORY-IDENTITY.md`


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-GINE-ACCESSORY.md

# 2026-09-22 — Gine accessory identity reconciliation checkpoint

## Completed

- Continued from the residual accessory identity queue after Resistance Helmet.
- Researched `pqacc-026`, **Gine (DB Super)'s Accessory**, associated with PQ144.
- Independent evidence establishes that the item is the **Gine (DB Super) Set accessory**, distinct from the four-piece Gine (DB Super)'s Clothes set.
- Confirmed the former repository endpoint `accr-101` is not present in the current canonical accessory inventory and must not be revived in isolation.
- Added `docs/data/accessory-gine-identity-audit-2026-09-22.json`.
- Registered the audit in `docs/data/pq-cross-domain-index.json`.

## Evidence

- Dragon Ball Wiki: Gine (DB Super) Set accessory and Gine (DB Super)'s Clothes are both associated with New Parallel Quest 144.
- Independent mirror corroborates the same accessory/clothing distinction.
- Current Xenoverse 2 equipment documentation lists Gine's Clothes as a four-piece clothing set and maintains accessories as a separate equipment category.
- Independent item-ID documentation records the Gine set accessory in its accessory notes.

## Boundary

The identity is now substantially clarified, but no canonical `acc-###` ID was invented because the current canonical accessory layer does not expose an exact Gine Set identity. The next write must either reconcile an existing exact inventory identity or create one coordinated across the canonical layer, PQ bridge, cross-link reports, reader-facing database, and unresolved backlog.

## Commits

- `8a451aedd3a745069fb17d0e4d6b3da1101ddfe8` — Gine accessory identity audit.
- `02dd5320621fb0eb03b6a0d3357c94c2fa99f108` — register Gine audit in cross-domain index.

## Exact next task

Search the current canonical accessory inventory and late-DLC/equipment mappings for an exact **Gine (DB Super) Set** identity. If none exists, perform a coordinated canonical promotion rather than reviving `accr-101`; then synchronize all reverse/forward PQ accessory consumers and recompute the cross-domain census. If exact inventory evidence remains insufficient, continue to the next unresolved late-DLC identity (Caulifla/Kale/Android 17 Ranger accessory) with the same no-speculation boundary.

## Validation boundary

Static repository inspection and independent web research were used. No GitHub Actions success is claimed.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-GINE-CORRECTION.md

# 2026-09-22 — Gine accessory identity correction

## Correction

The previous continuation cycle incorrectly treated **Gine (DB Super)'s Accessory / pqacc-026** as lacking current canonical inventory evidence.

Live repository inspection shows that the maintained canonical equipment/accessory records already contain:

- `equip-050` — **Gine (DB Super) Set**
- category: `accessory`
- acquisition: PQ144

The PQ equipment crosslink independently maps PQ144 to `equip-050`, and the canonical equipment/accessory record layer contains the same identity.

## Important domain boundary

`equip-050` is a canonical equipment/accessory identity, but it is **not** an `acc-###` identity in the dedicated accessory identity layer. Therefore this cycle deliberately does **not** create a duplicate `acc-071` or any other speculative accessory ID.

The correct relationship is already represented by the canonical equipment graph. The dedicated `accessory-pq-canonical-bridge.json` should retain `canonical_id: null` for pqacc-026 if its schema is strictly restricted to `acc-###` IDs, but its unresolved explanation should be interpreted as **no dedicated acc-### identity**, not **no canonical inventory identity**.

## Evidence checked

- `docs/data/equipment-record-layer.json`
- `docs/data/equipment-accessories-record-layer.json`
- `docs/data/pq-equipment-crosslink-report.json`
- `docs/data/pq-reward-relationships.json`
- `docs/data/accessory-pq-canonical-bridge.json`
- `docs/data/accessory-pq-canonical-remaining.json`

The repository changelog also records that Gine (DB Super) Set was already added during the equipment/accessory detail batch.

## Changes this cycle

- Added `docs/data/accessory-gine-identity-correction-2026-09-22.json`.
- No duplicate canonical accessory identity was created.
- No existing canonical relationship was overwritten.

## Exact next task

1. Update the residual accessory backlog and related audit/report language so pqacc-026 distinguishes **domain-resolved via equip-050** from **unresolved dedicated acc-### identity**.
2. Recompute the accessory/PQ census with domain-aware accounting.
3. Then proceed to `pqacc-021` Resistance Helmet, checking whether it likewise already has a canonical equipment/accessory endpoint before creating any new `acc-###` identity.

## Validation boundary

Static GitHub inspection was used. No CI success is claimed.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-IDENTITY-RESOLUTION.md

# AI Continuation Cycle — 2026-09-22 — Cross-domain endpoint identity resolution

## Current state
- Canonical PQ set: **186 records / 186 unique IDs / 186 unique numbers**.
- Current canonical relationship baseline: **859 unique edges**.
- Current domain counts: **244 skills / 151 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming**.
- Endpoint navigation census: **0 missing targets, 0 duplicate (PQ,target) pairs, 0 invalid PQ IDs** across skills, Super Souls, equipment, characters, and DLC.

## Work completed in this cycle
- Extended `scripts/validate_pq_endpoint_navigation.py` with a domain-wide identity-resolution census.
- Validator now reports exact canonical matches, unresolved endpoints, explicit conflict classifications, and explicit granularity classifications.
- Refreshed `docs/data/pq-endpoint-navigation-validation.json` to schema 1.2.0 and the current 859-edge baseline.
- Added `docs/data/pq-endpoint-identity-resolution-audit.json`.
- Registered the new identity-resolution audit in `docs/data/pq-cross-domain-index.json`.
- Confirmed the two equipment naming conflicts remain explicitly classified rather than merged:
  - PQ152: `Android 17 (DB Super) Ranger Wig` vs `Android 17 (DB Super) Wig`.
  - PQ155: `Gamma 2 Helmet` vs `Gamma 2's Helmet`.
- Confirmed the six DLC Super Pass→pack mappings remain explicit granularity, not new canonical edges.

## Validation boundary
The validator source was re-read after the write and the generated audit data was structurally reconciled against the current canonical counts. Runtime execution/CI success is **not** claimed because the available execution environment still cannot reliably clone/execute the repository against GitHub.

## Next task
Audit the remaining registered **non-PQ presentation/identity consumers** for stale relationship baselines and endpoint naming drift. Prioritize deterministic consumer/projection mismatches over new provenance-only research. Any ambiguous identity must remain explicitly classified rather than merged by name similarity.

## Rules to preserve
- Canonical database records are authoritative.
- Verification/research/projection layers never override canonical identity.
- Every canonical relationship endpoint must resolve exactly or have an explicit conflict/granularity classification.
- Aliases do not create canonical relationships.
- Preserve historical counts as historical records; current fields must use the 859-edge baseline.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-KAI-CENSUS.md

# 2026-09-22 continuation checkpoint — skill stale-metadata census

## Work completed
- Read the live continuation instructions and efficiency protocol before choosing work.
- Recomputed the canonical skill verification-date census from `docs/data/skills.json`.
- Current live census: **452 canonical skill records; 274 current at `last_verified=2026-09-22`; 178 stale; 0 duplicate IDs**.
- Added `docs/data/skill-stale-metadata-census-2026-09-22.json` documenting the live count and the next 20 stale records.
- Added `docs/data/skill-kai-through-light-grenade-provenance-audit-2026-09-22.json` with independent evidence gathered for the first ten stale records: Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, Ki Blast Thrust, Ki Explosion, Kill Driver, Last Emperor, and Light Grenade.

## Research findings
- Kai Kai: Dragon Ball Wiki corroborates the Xenoverse 2 Super Skill identity and cost-free teleport behavior; repository PQ63 association remains canonical.
- Kaioken: current XV2 skill documentation confirms PQ8 Ultimate Finish acquisition and 100/300/500 Ki stages; GameFAQs independently corroborates the PQ8/x3-Goku route but does not establish a guaranteed drop.
- Kaioken Kamehameha: current XV2 documentation confirms PQ14, 200 Ki, and Super classification; broader technique documentation distinguishes it from the x4/x20 Ultimate variants.
- Kairos Cannon: current documentation confirms the 100-Ki Ki Blast Super and Conton City Tournament/Thinning the Herd acquisition; secondary descriptions differ on projectile-count details, so the repository's bounded mechanics remain preferable to normalization by guess.
- Kamehameha: current documentation confirms the 100-Ki Ki Blast Super, all-CaC availability, and three charge levels with distance-dependent hit counts.
- Ki Blast Thrust: independent documentation confirms Yamcha Training School Quest Lesson 2 acquisition and the ki-enhanced charging-punch behavior.
- Ki Explosion: current documentation confirms the 100-Ki Ki Blast Super and PQ77 source; holding the input prolongs the explosion while consuming additional Ki.
- Kill Driver: current documentation confirms the 100-Ki Ki Blast Super and Turles training source; charge/detonation behavior is corroborated.
- Last Emperor: current documentation confirms the 0-Ki Ki Blast Ultimate, PQ71 source, and low-health once-per-battle restriction.
- Light Grenade: independent documentation confirms Piccolo Training Lesson 2 acquisition and chargeable Super behavior; the Hero of Justice Pack 2 Light Grenade Ultimate is kept distinct.

## Write boundary
- The canonical `skills.json` and `skills-index.json` files are large generated records. The available safe write operation requires replacing the complete file; the live connector response is truncated and therefore cannot safely reconstruct those full files in this cycle.
- Per the efficiency addendum's append-only/safe-state rule, canonical records were **not** partially overwritten or guessed.
- The evidence audit is therefore intentionally marked `researched_pending_canonical_sync`.

## Validation
- Stale census arithmetic: **274 current + 178 stale = 452 canonical records**.
- Duplicate-ID count: **0**.
- Audit files are deterministic JSON artifacts with explicit evidence boundaries.
- No CI success is claimed; no exposed successful workflow status was available through the current repository interface.

## Exact next task
Safely apply the ten audited provenance updates to the canonical/index skill layers when a complete-file write path is available. Recompute the stale census first. Preserve all existing fields, conflicts, and historical provenance. After canonical/index synchronization, validate 452/452 parity and continue with the next stale cohort beginning with **Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Kick, Mach Punch, Mach Slash, Maximum Charge, Meteor Burst, Meteor Crash, and Meteor Explosion**.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-NON-PQ-CONSUMER-AUDIT.md

# Continuation Handoff — 2026-09-22 Non-PQ Consumer Audit

## Current live baseline
- Canonical PQ scope: **186 records / 186 unique IDs / 186 unique numbers**.
- Canonical relationship layer: **859 unique edges**.
- Current domain counts: **244 skills / 151 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming**.
- Equipment canonical layer: **174 combined equipment/accessory records**, with **124 PQ→equipment forward edges / 122 unique canonical targets**.
- Canonical endpoint/navigation audits currently report zero unresolved canonical endpoints and zero duplicate relationship keys.

## Work completed this continuation
- Re-read the active continuation/handoff state and checked the live cross-domain index and current relationship-audit artifacts.
- Audited current non-PQ consumer drift around the corrected 859/124 baseline.
- Confirmed `docs/data/pq-reference-page-audit.json` currently carries the corrected 859/124 contract and is marked clean.
- Confirmed the live `scripts/validate_pq_reference_pages.py` source also checks **859 total** and **124 equipment** edges.
- GitHub code-search results still expose older cached/indexed text showing 860/125 inside historical search snapshots; this is not treated as live file content when the current file fetch resolves to the corrected contract.
- Confirmed `docs/data/pq-cross-domain-index.md` explicitly defines the next gate as non-PQ consumer/navigation integrity.
- Checked combined GitHub status for commit `e67e1ceb10740969f4f5f64c8b05cb125b612561`; no status checks were exposed. CI success is not claimed.

## Evidence / scope boundary
- Historical 860/862/840 and 125/88 figures remain preserved where they are explicitly dated historical audit records. They must not be mass-rewritten merely because the current baseline is 859/124.
- No relationship edge was added, removed, renamed, or inferred during this continuation.
- Search-index/cache discrepancies are not evidence of live repository drift until confirmed by a direct current-file fetch.

## Exact next task
1. Continue the non-PQ consumer audit from the cross-domain registry.
2. Search for **current** consumer assertions of the old 860/862/840 or 125/88 baselines, then direct-fetch each candidate before editing so historical records are preserved.
3. Prioritize deterministic presentation/reverse-navigation consumers with machine-checkable count, endpoint, or collection-shape contracts.
4. If a true current consumer drift is found, repair only that consumer and synchronize its audit/registry entry.
5. If no current drift is found, move to the next registered consumer rather than inventing data.
6. Runtime execution remains a separate gate; do not claim validator/CI success without an exposed successful run.

## Relevant prior commits
- `b69b646f32b3a71b7136d937c9202f0296d9e1eb` — corrected record reverse-PQ audit to current 124-equipment baseline.
- `e67e1ceb10740969f4f5f64c8b05cb125b612561` — added the preceding continuation handoff.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PQ-CURRENT-BASELINE-RECONCILIATION.md

# Continuation checkpoint — PQ current-baseline reconciliation — 2026-09-22

## Completed
- Re-read the current continuation/efficiency protocol and inspected the live PQ relationship consumer layer.
- Verified the authoritative current baseline as **859 total relationships**: 244 skills, 151 Super Souls, 124 equipment, 247 character references, 86 DLC, 7 farming.
- Confirmed multiple current consumer audits independently expose 859/124.
- Found three remaining current-looking fields that still expose the obsolete 860/862-era totals:
  - `docs/data/pq-reward-relationships.json` — `current_reconciliation_2026_09_22.total_unique_relationships` is 860.
  - `docs/data/pq-cross-domain-status.json` — current projection `total_edges` is 860.
  - `docs/COVERAGE-AUDIT.md` — latest current-cycle wording contains 862-era totals.
- Added `docs/data/pq-current-baseline-single-source-reconciliation-2026-09-22.json` documenting the deterministic correction targets and the historical-preservation rule.

## Safety boundary
The three target files are large/append-only artifacts. The available connector returns truncated content for them, so replacing a whole file from the truncated response would risk destructive loss. No unsafe replacement was attempted.

## Exact next task
1. Obtain a complete-file-safe write path for the three current-looking fields.
2. Change only current/live/baseline totals to 859/124.
3. Preserve all dated 860/862/840 historical snapshots unchanged.
4. Re-run exact relationship-pair parity across the registered reverse indexes.
5. Update the canonical continuation handoff using append-only semantics if the complete file can be safely preserved; otherwise create the next dated cycle checkpoint as the repository's established fallback.

## Evidence
- `docs/data/pq-current-consumer-baseline-correction-2026-09-22.json` establishes the current 859/124 baseline.
- `docs/data/pq-reference-page-audit.json` and `docs/data/skill-pq-acquisition-presentation-audit.json` independently expose 859 current relationships.
- `docs/data/pq-endpoint-alias-granularity-map.json` records canonical edge count 859 before/after presentation metadata.

## Commit
- `b924c99a3d8fcc666148a1652ffc3fbb2286f17f` — current-baseline single-source reconciliation audit.

## Do not do
- Do not rewrite historical 860/862/840 records merely because they are old.
- Do not infer a replacement relationship for PQ99 Mr. Shape Up L.
- Do not reconstruct large JSON/Markdown files from truncated connector output.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PQ-REFERENCE-CONSUMER-BASELINE.md

# AI Continuation Cycle — 2026-09-22 — PQ reference consumer baseline reconciliation

## Live state before/after
- Canonical PQ records: **186**.
- Canonical relationship baseline: **859 unique edges**.
- Domain counts: **244 skills / 151 Super Souls / 124 equipment / 247 character / 86 DLC / 7 farming**.
- Farming set: **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**.

## Work completed
- Audited the live PQ reference-page consumer layer after the equipment-domain correction.
- Found `scripts/validate_pq_reference_pages.py` still enforcing the obsolete **860 total / 125 equipment** baseline.
- Updated the validator to enforce the current **859 / 124** baseline and renamed its live checks accordingly.
- Corrected `docs/Parallel-Quests.md` from 860 to **859** in its current canonical relationship census.
- Corrected `docs/Parallel-Quest-Audit.md` from 860 to **859** in its current audit baseline.
- Reconciled `docs/data/pq-reference-page-audit.json` so it no longer contains contradictory obsolete 860/125 live-check fields and points to the corrected validator commit.

## Evidence / boundary
- No canonical relationship edge was added, removed, or inferred in this batch.
- Historical 860/862/840 counts remain historical where already recorded; only live/current assertions were corrected.
- This was a deterministic consumer/validator reconciliation, not a provenance or gameplay research pass.

## Validation
- Source-of-truth relationship census remains 859 edges with exact domain counts 244/151/124/247/86/7.
- PQ reference audit now declares the same baseline.
- Validator now checks the same baseline.
- CI/Actions: no successful workflow/check exposed for this direct-commit chain; do not claim CI success.

## Commits
- `d43d43302b4d255a0a7b853aa22f22a8a847d05f` — validator baseline correction.
- `0158c88aab6b72511f002e7c24a665ad1efaa468` — Parallel-Quests reference page correction.
- `3f4db25d74c0c81d7fc36f5e980e218c274c0cc9` — Parallel Quest Audit correction.
- `6af37d104b814806af5b2a67e89bb5d13c02a48a` — reference-page audit reconciliation.

## Exact next batch
Audit the remaining **non-PQ presentation/catalog/search consumers** for stale current relationship baselines and endpoint identity drift. Prioritize deterministic files that consume `pq-reward-relationships.json` or its reverse indexes. Preserve historical counts and explicit identity conflicts; do not infer new canonical edges.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PQ-SCALAR-DRIFT.md

# Continuation checkpoint — PQ scalar drift reconciliation

Date: 2026-09-22

## Completed
- Re-read the live PQ relationship/status layer and verified the authoritative current projection is **859 total edges**: 244 skills, 151 Super Souls, 124 equipment, 247 character, 86 DLC, 7 farming.
- Confirmed reverse projection parity is clean: no missing/orphan/mismatched PQ sets in the current endpoint census.
- Identified three remaining current-looking scalar assertions that still require a safe textual patch: `docs/data/pq-reward-relationships.json` has `current_reconciliation_2026_09_22.total_unique_relationships=860`; `docs/data/pq-cross-domain-status.json` has `target_normalization_audit_2026_09_22.total_edges=860`; `docs/COVERAGE-AUDIT.md` contains an 862-era current assertion in its latest endpoint-census history.
- Added `docs/data/pq-current-baseline-field-drift-audit-2026-09-22.json` documenting the exact fields, expected values, and preservation rule.

## Safety boundary
- No canonical relationship edge was added/removed in this cycle.
- Historical 840/860/862 snapshots must remain immutable evidence.
- The large canonical/status/audit files were not reconstructed from truncated connector output; a destructive full-file replacement would violate repository integrity.

## Next exact work
1. Obtain a complete-file-safe editing path for the three identified scalar fields.
2. Patch only current/live assertions to 859/124 where applicable; preserve all dated historical counts.
3. Re-run exact forward/reverse relationship-pair parity.
4. Update the main continuation/TODO handoff with the resulting commit and next unfinished task.
5. Then resume the highest-priority cross-domain/detail-enrichment task rather than restarting completed work.

## Commits
- `ac7a08c5b7c5e9ad3ea2d440198a791922fd3dca` — baseline scalar drift audit.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-PRESENTATION-CONTRACT.md

# AI Continuation Checkpoint — 2026-09-22 — Presentation Contract

## Completed this cycle
- Re-read the current continuation/TODO direction and followed the active priority to continue the high-volume skill consumer census before broadening data domains.
- Audited the repository's acquisition semantics across `docs/Skills-Complete-Database.md`, `docs/Skills-Database.md`, `docs/data/parallel-quest-skill-acquisition-model.json`, and `docs/data/parallel-quest-skill-acquisition-early-base-game.json`.
- Confirmed the repository already distinguishes PQ→skill association from guaranteed rewards, Ultimate Finish requirements, reward triggers, and drop rates in the structured evidence layer.
- Updated `docs/Farming-Hub.md` with an explicit **Acquisition presentation contract** so presentation copy cannot silently promote `pq_rewards_skill` relationships or unresolved research fields into guaranteed/Ultimate-Finish mechanics.
- Added `docs/data/skill-consumer-presentation-contract-audit-2026-09-22.json` documenting the implemented contract and evidence boundary.

## Validation / evidence boundary
- Existing research records intentionally preserve `unknown`, `unresolved`, `partially_verified`, and conflicting-source states.
- No skill acquisition probability, Ultimate Finish gate, enemy-specific trigger, or guarantee was inferred from a relationship alone.
- No large generated canonical file was reconstructed from a truncated connector response.
- CI success is not claimed; the direct-commit chain has no exposed successful workflow/check result in this cycle.

## Current canonical census context
- Latest recorded skill census: **452 canonical / 452 index / 0 duplicate IDs / 178 stale `last_verified` records**.
- The prior bounded stale batch remains the exact next metadata workstream once a safe complete-file write path is available: Kai Kai, Kaioken, Kaioken Kamehameha, Kairos Cannon, Kamehameha, Ki Blast Thrust, Ki Explosion, Kill Driver, Last Emperor, Light Grenade.
- The following stale batch after that is: Lightning Impact, Lightning of Absolution, Lovely Cyclone, Mach Kick, Mach Punch, Mach Slash, Maximum Charge, Meteor Burst, Meteor Crash, Meteor Explosion.

## Exact next work
1. Continue searching remaining high-volume presentation/index consumers for language that equates PQ association, Ultimate Finish, enemy appearance, or reward-table presence with guaranteed acquisition.
2. Repair deterministic presentation drift only; preserve unresolved research evidence.
3. Recompute the canonical/index/stale census before each bounded skill metadata batch.
4. Never overwrite a large generated JSON file from an incomplete/truncated fetch; use a complete-file write path or a smaller authoritative layer.
5. Keep all PQ↔skill, skill↔character, skill↔DLC, and acquisition relationships cross-navigable.
6. At the next checkpoint, append the result to the persistent continuation history if the full handoff file can be safely fetched and rewritten without truncation; this checkpoint itself is the durable cycle handoff for resumption.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-RECORD-REVERSE-PQ-AUDIT.md

# AI Continuation Cycle — 2026-09-22 — record reverse-PQ current-baseline reconciliation

## Live state
- Canonical PQ records: **186**.
- Current canonical relationship baseline: **859 unique edges**.
- Domain counts: **244 skills / 151 Super Souls / 124 equipment / 247 character / 86 DLC / 7 farming**.
- Current equipment reverse projection: **124 canonical forward pairs / 122 unique canonical targets**.

## Work completed
- Audited `docs/data/record-reverse-pq-navigation-audit.json` after the PQ99 false-equipment correction.
- Found one stale **current-contract** field in the reverse-record audit: `exact_forward_pair_contract.equipment` still declared **125/125** even though the live canonical equipment relationship layer is **124/124**.
- Corrected that current audit contract to **124 canonical pairs / 124 structured pairs**, preserving the four explicitly noncanonical equipment acquisition-metadata PQ fields and the two documented source-route conflicts.
- No canonical relationship, equipment identity, alias, acquisition claim, or provenance classification was changed.

## Validation
- Re-read the updated audit from the live `main` branch: Super Soul **151/151**, Equipment **124/124**; both consumers report clean exact reverse-pair parity.
- Equipment reverse contract: **0 missing / 0 extra / 0 duplicate canonical pairs / 0 duplicate structured pairs / 0 malformed structured fields / 0 invalid PQ IDs / 0 duplicate record names**.
- Historical 125-era values remain preserved only in historical handoff/audit records; the current audit now reflects 124.
- Runtime/CI: repository clone could not resolve `github.com`; no runtime or CI success is claimed.

## Commit
- `b69b646f32b3a71b7136d937c9202f0296d9e1eb` — corrected current record reverse-PQ audit baseline.

## Exact next batch
- Perform a fresh live census of the remaining registered cross-domain presentation/identity consumers for any other **current** 859/124 baseline drift.
- Prioritize deterministic audit fields that are explicitly labeled current/live/baseline; leave dated historical snapshots untouched.
- After the current-consumer sweep is clean, use `docs/data/pq-endpoint-alias-granularity-map.json` to resolve only independently evidenced equipment naming conflicts; do not invent aliases or canonical relationships.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-RESIDUAL-ACCESSORY-IDENTITY-FINAL.md

# AI Continuation Cycle — 2026-09-22 — residual accessory identity final handoff

## Completed this cycle

- Continued from the current cross-domain/P1 state rather than restarting completed validator work.
- Audited the remaining 16 unresolved PQ accessory research identities against the current canonical equipment/accessory inventory layer.
- Identified `Resistance Helmet` (`pqacc-021`, PQ111) as the strongest remaining exact-name promotion candidate because the live equipment layer contains `equip-135`, explicitly named `Resistance Helmet` and classified as an `accessory`.
- Preserved the identity-namespace boundary: `equip-135` was **not** duplicated as a new accessory identity during this cycle.
- Confirmed `Android 13's Hat` remains unresolved because the repository has no exact current canonical inventory endpoint despite external TP Medal Shop evidence.
- Confirmed Android 14's Hat and Bardock (DB Super)'s Scouter remain clothing/component ambiguity cases; Android 15's Sunglasses remains a component alias of Android 15's Shades & Hat.
- Added and registered `docs/data/accessory-residual-identity-candidate-audit-2026-09-22.json`.
- Verified the new audit and cross-domain registry from the live `main` branch.

## Commits

- `c091295c8b68def00d157f116443682be926f272` — residual accessory identity candidate audit.
- `5d2ce2c20583153fa5d4dd7ac452b615a3538561` — residual accessory identity continuation checkpoint.
- `fb1d60002d74969585e77685929fbcc798e10a81` — register residual accessory audit in the cross-domain index.

## Current baseline

- PQs: 186
- Canonical relationships: 859
- Skills: 244
- Super Souls: 151
- Equipment: 124
- Characters: 247
- DLC: 86
- Farming: 7
- Canonical accessories: 70
- PQ accessory projection: 28 forward / 28 reverse
- Accessory research identities: 45 total / 29 matched / 16 unresolved

## Exact next task

Safely reconcile **Resistance Helmet / equip-135** into the canonical accessory identity layer, using one physical inventory identity rather than inventing a duplicate. Synchronize the canonical accessory record layer, accessory PQ bridge, PQ accessory cross-link report, unresolved backlog, combined equipment/accessory census, and reader-facing accessory database; then recompute the cross-domain endpoint/reverse census. If the full canonical-layer write cannot be performed without risking loss of append-only data, keep the candidate explicit and continue with the next unresolved identity using exact inventory evidence.

After that, continue the remaining unresolved accessory identities, prioritizing exact current inventory evidence for the DAIMA/Future Saga records and preserving component/clothing ambiguity instead of guessing.

## Validation boundary

Static GitHub inspection was used. No repository runtime or GitHub Actions success is claimed.


---

# CONSOLIDATED SOURCE: docs/AI-CONTINUATION-PROMPT-CYCLE-2026-09-22-RESIDUAL-ACCESSORY-IDENTITY.md

# AI Continuation Cycle — 2026-09-22 — residual accessory identity audit

## Current live baseline

- Canonical PQ layer: **186 records**.
- Current canonical relationship baseline: **859 unique edges** = 244 Skills / 151 Super Souls / 124 Equipment / 247 Characters / 86 DLC / 7 farming.
- Canonical accessory identity layer: **70 `acc-###` records**.
- PQ accessory projection: **28 forward / 28 reverse**.
- Research layer: **45 accessory/PQ records**, with **29 matched identities / 16 unresolved**.

## Work completed

- Read the current continuation state and followed the latest deterministic cross-domain/consumer reconciliation into the remaining accessory identity backlog.
- Audited the residual unresolved accessory records against the live canonical equipment/accessory layers.
- Added `docs/data/accessory-residual-identity-candidate-audit-2026-09-22.json`.
- Identified **Resistance Helmet (`pqacc-021`, PQ111)** as the first exact-name promotion candidate: the live equipment layer contains `equip-135`, explicitly named `Resistance Helmet` and classified as an accessory.
- Deliberately did **not** create a second `acc-###` identity yet. The safe model is to reconcile the existing `equip-135` inventory identity into the canonical accessory namespace rather than duplicate the same physical item.
- Confirmed Android 13's Hat remains unresolved because the repository lacks an exact current canonical inventory endpoint; external shop evidence alone is insufficient.
- Confirmed Android 14's Hat, Android 15's Sunglasses, and Bardock (DB Super)'s Scouter remain component/clothing ambiguity cases.

## Evidence boundary

- No canonical relationship edges were changed.
- No duplicate accessory identity was invented.
- No reward probability, Ultimate Finish gate, or guaranteed-drop condition was inferred.
- Existing PQ152/PQ155 naming conflicts remain explicit and are not merged by textual similarity.

## Validation

- Live search confirms `equip-135` is `Resistance Helmet` with category `accessory`.
- The new audit is machine-readable JSON and records the remaining backlog plus the exact-name candidate.
- CI/runtime execution remains unavailable; no CI success is claimed.

## Commit

- `c091295c8b68def00d157f116443682be926f272` — residual accessory identity candidate audit.

## Exact next task

1. Safely reconcile **Resistance Helmet / equip-135** into the canonical accessory identity layer, reusing one physical inventory identity rather than creating a duplicate.
2. Synchronize the accessory bridge, PQ accessory cross-link projection, unresolved backlog, combined equipment/accessory census, and reader-facing accessory database.
3. Recompute the cross-domain endpoint census and verify canonical/reverse parity.
4. Then continue the remaining unresolved accessory identities, prioritizing exact current inventory evidence for the DAIMA/Future Saga records while preserving unresolved/component classifications where evidence is insufficient.



---

# Consolidated Companion Protocol — docs/AI-CONTINUATION-PROMPT-EFFICIENCY-ADDENDUM.md

The complete companion efficiency protocol is incorporated below so the main handoff contains the operating rules required to interpret and execute the consolidated historical cycle notes. The original addendum file remains in place as a compatibility/source artifact.

# AI Continuation Prompt — Efficiency Addendum

> **Purpose:** This addendum is an append-only operating protocol for free/web-client AI sessions. It is intended to be read together with `docs/AI-CONTINUATION-PROMPT.md` and does not replace or delete any instruction in that file.

## Free/web-client execution protocol

1. **Start with a live census, not historical notes.** Read the handoff, then inspect the current canonical files and compute the smallest relevant counts before choosing work. Historical counts are context only.
2. **Choose one bounded batch per cycle.** Prefer 4–12 closely related records or one deterministic validator/producer invariant. Do not spend a whole context window re-reading unrelated history.
3. **Use a two-pass workflow.** First inspect and research; second edit, validate, and document. Do not mix speculative research with writes.
4. **Prefer repository evidence first.** Search canonical data, schemas, validators, research batches, reverse indexes, and existing source URLs before using web research. Reuse already-verified sources instead of repeatedly rediscovering them.
5. **Research only the fields in scope.** Do not rewrite a whole record or normalize unrelated fields during a bounded pass. Preserve existing values, provenance, conflicts, and `null` where evidence is insufficient.
6. **Keep browser-context work compact.** When web research is needed, search exact record names plus `Xenoverse 2`, inspect a small number of authoritative/independent sources, and record the result immediately. Avoid opening long pages or repeating searches that cannot change the classification.
7. **Stop researching a record when the evidence threshold is reached.** Either make an evidence-backed change or record an evidence boundary/conflict; do not continue browsing merely to force a non-null value.
8. **Batch related writes atomically.** Update the canonical layer, generated/index projection, audit/coverage file, and changelog only when required by the repository contract. Keep a bounded batch internally consistent before committing.
9. **Validate after every write.** Parse changed JSON, recompute the relevant census, compare canonical/index parity, search changed files for internal citation artifacts, and inspect applicable Actions. Never claim CI success when no run/status is exposed.
10. **Use a compact end-of-cycle record.** Before finishing, append a dated entry containing: scope, records/files changed, evidence used, evidence limits, validation result, CI result or unavailable status, current live counts, commit(s), and the exact next batch.
11. **Avoid context waste.** Do not quote or duplicate large historical sections in responses. Refer to file paths, record names, counts, and commit IDs. Re-fetch only the exact files needed for the current batch.
12. **If tools or context are limited, preserve state rather than guessing.** Make a smaller safe batch, update the handoff with the blocked action and next exact step, and stop cleanly.

## Append-only protection

- Never delete, rewrite, summarize away, reorder, or truncate any existing content in `docs/AI-CONTINUATION-PROMPT.md`.
- Add new cycle entries only at the end of that file, preserving all historical notes even when counts are stale; clearly label newer live counts as superseding them.
- If an edit tool cannot safely append while preserving the complete existing file, do not overwrite the file. Create a separate addendum or report the limitation instead.
- Do not “clean up” old wording, old counts, formatting, source conflicts, or historical mistakes by removal. Add a correction or clarification below the existing entry.

## Recommended batch template

```text
### YYYY-MM-DD cycle update — [short scope]
- Live census before editing: [counts].
- Bounded batch: [records/files].
- Research/evidence: [sources and what they establish].
- Changes: [precise fields/files].
- Evidence limits/conflicts preserved: [details].
- Validation: [parse/census/parity/artifact results].
- CI: [run/status result, or explicitly unavailable].
- Commits: [IDs].
- Live census after editing: [counts].
- Exact next batch: [specific records/files and method].
```

## Priority tie-breaker for efficient progress

When several tasks are available, choose the highest-impact task that is: (a) directly supported by existing repository evidence, (b) bounded enough to validate in one web-client session, (c) useful to more than one database or reverse link, and (d) unlikely to require broad schema migration. Prefer fixing a deterministic producer/validator/index mismatch over adding low-confidence descriptive prose.



---

# Consolidation Completion / Current Resume Point — 2026-09-22

- [x] Repository-wide recursive tree inspection confirmed **26** files matching the `docs/AI-CONTINUATION-PROMPT*.md` naming family: the canonical handoff, the efficiency addendum, and **24 dated cycle prompts**.
- [x] All **25 companion prompt files** have now been incorporated into this canonical `docs/AI-CONTINUATION-PROMPT.md` with their complete source text preserved in dated consolidated sections.
- [x] The efficiency addendum was also incorporated because it is part of the same `AI-CONTINUATION-PROMPT-*` family and contains operating rules required to interpret the cycle history.
- [x] Original dated companion files were intentionally retained as historical/source artifacts; no historical prompt was deleted or rewritten.
- [x] Codebase search confirms the consolidated prompt contains every companion source path; no prefixed companion prompt was omitted.
- [x] Existing cross-domain registry references to dated cycle checkpoints were not silently rewritten because those files remain valid historical artifacts.

## Current resume point
- Continue from the latest live handoff state, not from the oldest consolidated cycle note.
- Current Super Soul state after the latest completed cycle: **234 canonical records; 151 PQ→Super Soul forward edges; 148 reverse targets; 0 unresolved crosslink endpoints**.
- Latest completed Super Soul batch: **034 and 036–039**.
- Exact next task: **recompute the full Super Soul thin-system census and select the next 4–12 highest-impact canonical records with strong exact-name evidence and/or reusable PQ cross-links**, preserving unresolved mechanics and acquisition conflicts.
- Do not treat historical counts or older cycle instructions as current when newer live handoff entries supersede them.


### 2026-09-22 — Self-contained continuation contract clarification
- [x] Confirmed the canonical handoff must be sufficient for a brand-new AI chat to resume the project without reconstructing intent from individual dated cycle prompts.
- [x] The canonical handoff preserves **all project goals**, not merely the latest task: the primary goal is an **exhaustive, accurate, research-backed Dragon Ball Xenoverse 2 Wiki and structured research database**, with comprehensive details, provenance, version/history coverage, acquisition/mechanics data, and complete cross-database navigation.
- [x] The efficiency protocol is part of the operating contract, not an optional optimization. Live census, bounded batches, two-pass research/edit workflow, repository evidence first, field-scoped edits, evidence thresholds, atomic writes, post-write validation, compact state recording, context-efficient retrieval, and safe state preservation all remain active requirements.
- [x] **Exhaustiveness and efficiency are complementary:** efficiency controls how work is selected and executed; it does not reduce the completeness target or authorize skipping unresolved coverage. Work may be deferred only because it is lower priority, unsupported by evidence, unsafe to change, or outside the current bounded batch.
- [x] Historical cycle entries remain cumulative history. Their stale counts and old next-task statements must not override newer live state. The **latest live resume checkpoint** is authoritative for the next action.
- [x] A fresh AI should understand both layers immediately: **(1) the complete long-term objective and operating rules, and (2) the current exact unfinished work/state**, without requiring the user to explain prior chats or reread every dated prompt individually.
- [x] Cross-domain completion remains project-wide: databases should be linkable and reverse-navigable where evidence supports relationships; unresolved identities, conflicts, and granularity differences must be explicitly recorded rather than guessed.
- [x] Every completed cycle must advance the exact resume checkpoint and append the new state to this canonical handoff so the next fresh chat inherits the latest project state.


### 2026-09-22 cycle update — Super Soul 154–157 and 159–163 provenance/mechanics refresh
- [x] Live census before editing: 234 canonical Super Soul records / 151 canonical PQ→Super Soul edges / 148 unique reverse targets / 0 unresolved endpoints; 88 indexed-status records.
- [x] Bounded batch: super-soul-154 through 157 and 159 through 163. Record 158 was intentionally held because its exact name overlaps the Do or Die skill and retrieved evidence did not cleanly isolate a Super Soul-specific mechanic set.
- [x] Refreshed 9 canonical records with exact-name character sources, trigger/effect/magnitude data, supported durations, Limit Burst data, provenance, and last_verified 2026-09-22.
- [x] Added docs/data/super-soul-154-157-and-159-through-163-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Canonical PQ relationship identities were unchanged; selected endpoints remain navigable through the existing reverse relationship layer.
- [x] Evidence limits preserved: no reward probabilities or unsupported Ultimate-Finish conditions; no duration/stacking values were invented; record 158 remains explicitly unresolved rather than conflating skill and Super Soul mechanics.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the full live Super Soul thin-system census, then select the next 4–12 highest-impact canonical gaps with strong exact-name evidence and/or reusable PQ cross-links.


### 2026-09-22 cycle update — Super Soul 164–172 provenance/mechanics refresh
- [x] Live census before editing: 234 canonical records; 79 indexed; 221 missing at least one of the eight core mechanics fields under the strict completeness check.
- [x] Bounded batch: **super-soul-164 through super-soul-172**.
- [x] Refreshed 9 canonical records with character source, trigger/effect/magnitude, supported duration/stacking, Limit Burst, verification date, and provenance.
- [x] Preserved canonical PQ edges: 164→94, 165→97, 166→97, 167→102, 168→102, 169→103, 170→103, 171→103, 172→104.
- [x] Added `docs/data/super-soul-164-through-172-provenance-audit-2026-09-22.json` and registered it in the cross-domain index.
- [x] No reward probabilities or unsupported Ultimate-Finish mappings were added; no canonical relationship identities changed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live thin census and select the next 4–12 indexed records with exact-name evidence, continuing beyond 172 rather than assuming sequential completion is always optimal.


### 2026-09-22 cycle update — Super Soul 173–181 provenance/mechanics refresh
- [x] Live census before editing: 234 canonical Super Souls / 70 indexed-status records.
- [x] Bounded batch: **super-soul-173 through super-soul-181**.
- [x] Refreshed 9 records with character/DLC provenance, triggers, effects, magnitudes, supported duration/stacking, Limit Bursts, verification date, and sources.
- [x] Preserved PQ edges: 173→105, 174→106, 175→106, 176→106/108, 177→108, 178→109, 179→109, 180→110, 181→110.
- [x] Added `docs/data/super-soul-173-through-181-provenance-audit-2026-09-22.json` and registered it in the cross-domain index.
- [x] Evidence limits preserved; no reward probabilities or unsupported Ultimate-Finish requirements added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live indexed/thin census and select the next 4–12 indexed records with exact-name evidence and reusable PQ/cross-domain relationships.


### 2026-09-22 cycle update — Super Soul 182–190 provenance/mechanics refresh
- [x] Live census before editing: 234 canonical Super Souls / 61 indexed-status records.
- [x] Bounded batch: **super-soul-182 through super-soul-190**.
- [x] Refreshed 9 records with character/DLC provenance, triggers, effects, magnitudes, supported durations/stacking, Limit Bursts, verification date, and sources.
- [x] Preserved PQ edges: 182→111, 183→112, 184→112, 185→112, 186→113, 187→113, 188→114, 189→115, 190→116.
- [x] Added and registered `docs/data/super-soul-182-through-190-provenance-audit-2026-09-22.json`.
- [x] Evidence limits preserved; no unsupported drop rates or Ultimate-Finish conditions added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live indexed/thin census and select the next 4–12 indexed records with exact-name evidence and reusable cross-domain relationships.


### 2026-09-22 cycle update — Super Soul 191–199 provenance/mechanics refresh
- [x] Live census before editing: 234 canonical Super Souls / 52 indexed-status records; 52 thin under the strict eight-field completeness check.
- [x] Bounded batch: **super-soul-191 through super-soul-199**.
- [x] Refreshed 9 records with character/DLC provenance, triggers, effects, magnitudes, supported durations/stacking, Limit Bursts, verification date, and sources.
- [x] Preserved PQ edges: 191→116, 192→117, 193→118, 194→119, 195→120, 196→120, 197→121, 198→122, 199→122.
- [x] Added and registered `docs/data/super-soul-191-through-199-provenance-audit-2026-09-22.json`.
- [x] Evidence boundaries preserved; no unsupported reward probabilities or Ultimate-Finish conditions added.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: recompute the live indexed/thin census and select the next 4–12 highest-impact indexed records with exact-name evidence and reusable cross-domain relationships.


### 2026-09-22 cycle update — Super Soul 200–205 provenance/mechanics refresh
- [x] Live census before editing: **234 canonical Super Soul records**; selected records 200–205 were still indexed with canonical PQ navigation.
- [x] Bounded batch: **super-soul-200 through super-soul-205**.
- [x] Refreshed character sources, DLC provenance, trigger/effect/magnitude, duration/stacking where directly supported, Limit Burst data, verification status, and provenance for all 6 records.
- [x] Record 200: Super Baby 2; PQ124; below-25%-HP damage reduction sequence (-20% once for 10 seconds, then -15% while below 25%).
- [x] Record 201: Kefla (Super Saiyan); PQ126; charged-attack and charged-Ki-Blast stacking effects (+5% each, up to 4 stacks per effect).
- [x] Record 202: Broly (Full Power Super Saiyan); PQ128; guard-break duration reduced by 25%.
- [x] Record 203: Frieza (Final Form); PQ128; ally KO triggers +10% all-attack damage for 15 seconds for the user/allies.
- [x] Record 204: Paragus; PQ128; 150-second trigger restores 300 Ki and grants +20% all-attack damage for 30 seconds.
- [x] Record 205: Veku; PQ129; battle-start -10% all-attack damage and -10% movement speed for 30 seconds, followed by +10% all-attack damage for 30 seconds and +15% movement speed for 10 seconds.
- [x] Evidence used: maintained Super Soul catalogue, independent Steam discussion, GameFAQs timing confirmation, current PQ reward navigation, and repository PQ records. No unsupported reward/drop probabilities were added.
- [x] Added docs/data/super-soul-200-through-205-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Validation: canonical Super Soul layer parses at **234 records**; all 6 selected records are current at **2026-09-22** and have populated mechanics/provenance fields; audit parses and is registered; canonical PQ relationship identities were unchanged.
- [ ] CI/runtime: no successful workflow/check exposed for this direct-commit chain; no CI success claimed.
- [x] Commits: 47b0a6e7f191c1858a2fe45f090f5890da4577a1, 177bc63d5bb6a8d3183c4361953774350a57df35, 7f0b04948dcddfbf673ba677b242a220375eafb5.
- [x] Live census after editing: **234 canonical records / 31 indexed-status records**; 200–205 are no longer indexed-only.
- [ ] Exact next batch: **Super Soul 206–211** — Hey, you think you could fight a little quieter?!; Don't think I'm gonna show you any gratitude!; Hey, you! You ready for me?!; Hmph. I'm off to take a nap.; Th-Thanks...; and You'd better survive, you got that?!. Use the maintained catalogue plus independent corroboration; preserve the existing PQ129–131 canonical relationships and do not infer reward/drop semantics beyond the relationship layer.


### 2026-09-22 cycle correction — Canonical continuation file is append-only

- [x] Clarified the continuation-file rule to prevent this issue from recurring: **future cycle updates, resume checkpoints, corrections, and newly discovered tasks must be appended to the end of `docs/AI-CONTINUATION-PROMPT.md`**.
- [x] Do **not** create a new replacement/current `AI-CONTINUATION-PROMPT*.md` file merely to hold the next cycle's state. The canonical `docs/AI-CONTINUATION-PROMPT.md` remains the single live continuation handoff.
- [x] Existing dated `docs/AI-CONTINUATION-PROMPT-CYCLE-*.md` files are historical/source artifacts only. They may be read for context and retained for provenance, but a new cycle should not fork the active handoff into another dated prompt file unless the user explicitly requests a separate historical artifact.
- [x] Preserve the append-only contract: never delete, truncate, reorder, replace, or summarize away prior content in the canonical handoff. Add the newest cycle entry at the end and make its live state authoritative over older historical entries.
- [x] This clarification applies to all future autonomous continuation work, including Super Souls, skills, PQs, equipment, cross-domain reconciliation, validators, research audits, and other project workstreams.
- [x] The existing dated early-Super-Souls prompt remains unchanged as a historical/source artifact; its content is not being duplicated into a newly created active prompt.


### 2026-09-22 cycle update — Super Soul 206–211 provenance/mechanics refresh
- [x] Live census after the prior batch: **234 canonical Super Soul records / 31 indexed-status records**.
- [x] Bounded batch: **super-soul-206 through super-soul-211**.
- [x] Refreshed all 6 records with exact-name character/DLC provenance, trigger/effect/magnitude, supported duration, Limit Burst data, verification date, and evidence notes.
- [x] Preserved canonical PQ edges: **206→PQ129, 207→PQ129, 208→PQ130, 209→PQ130, 210→PQ130, 211→PQ131**.
- [x] Added docs/data/super-soul-206-through-211-provenance-audit-2026-09-22.json and registered it in docs/data/pq-cross-domain-index.json.
- [x] Evidence used: maintained Super Soul catalogue, independent Steam discussion, independent GameFAQs reference, and the maintained DLC/PQ listing. Exact-name evidence supports the mechanics while reward/drop probabilities and Ultimate-Finish gating remain unclaimed.
- [x] Validation: canonical JSON parses at **234 records**; all 6 selected records have the required character/trigger/effect/magnitude/Limit Burst fields; all retain their original PQ relationships; audit/index registration completed.
- [ ] CI/runtime: no successful workflow/check exposed for the direct-commit chain; no CI success claimed.
- [x] Commits: da1151f3867b35bb303adb7993145df7c64d95f1, 6a48352fb3b19bea392c74cb61505c1d37cc4cba, 4de772688803160f0ad05519d501374a0b3aca29.
- [ ] Exact next batch: recompute the **live full Super Soul indexed/thin census** and select the next 4–12 highest-impact unresolved records with strong exact-name evidence and reusable PQ/cross-domain links. Do not assume sequential IDs are automatically the next priority.


### 2026-09-22 cycle update — Super Soul 049, 055, 060, 061 mechanics/Limit Burst refresh
- [x] Live census before editing: **234 canonical records**; the strict core-field thin count is **220**, with many null duration/stacking fields legitimately representing always-active or non-timed effects.
- [x] Selected a bounded high-impact PQ-linked batch: **049, 055, 060, 061**, rather than assuming numeric continuation from the previous 206–211 batch; this follows the organized handoff's later live-state priority for unresolved early/cross-domain records.
- [x] Refreshed Super Soul 049's Limit Burst; 055's full-Ki/30-second Ki Auto-Recovery magnitude and Limit Burst; 060's corrected +20% Ki Blast Skills magnitude and Limit Burst; and 061's +5% Strike/+10% Ki Blast per-stack values, five-stack cap, and Limit Burst.
- [x] Preserved canonical PQ edges: **049→PQ058, 055→PQ131, 060→PQ093, 061→PQ160**.
- [x] Added `docs/data/super-soul-049-055-060-061-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence used: current Super Soul catalogue, dedicated Pan/Gohan (Beast) character documentation, independent GameFAQs build/research discussion, and the repository research seed for 055. citeturn6search0turn7search1turn6search1turn7search0
- [x] Validation: canonical JSON parses at **234 records**; all four selected records have populated character/trigger/effect/magnitude/Limit Burst fields; PQ identities unchanged; audit registered.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: `60455e83c45e73c9d4bae6343df21626aebb1ead`, `935a530d2425c40277adccfae1a3ff833b90ecf0`, `6825bee0f93e3f7fc609499850ac81068fceffb9`.
- [ ] Exact next batch: continue the live thin-system census from the highest-impact unresolved PQ-linked records, prioritizing reusable cross-domain relationships and strong exact-name evidence; do not create another dated continuation prompt.


### 2026-09-22 cycle correction — remove presentation citation artifacts from handoff semantics
- [x] The immediately preceding 049/055/060/061 checkpoint contained web citation markup in its prose. Those tokens are **not repository-native provenance syntax** and must not be copied into future handoff/data files.
- [x] The underlying evidence remains the current Super Soul catalogue, dedicated character pages, independent GameFAQs discussion, and the repository research seed; future handoff entries should name sources plainly or use their repository URL strings, while user-facing responses may cite web sources separately.
- [x] Append-only history is preserved; this correction supersedes the citation-markup portion of the immediately preceding checkpoint without deleting historical text.


### 2026-09-22 cycle update — Future Saga Super Souls 033 and 035 mechanics refresh
- [x] Selected a high-impact unresolved pair from the live thin census: **super-soul-033** and **super-soul-035**, both tied to PQ185/PQ186 and the Future Saga Chapter 4 cross-domain dataset.
- [x] Refreshed 033 with the secondary-evidence-supported state-based regeneration/guard-break behavior and **DEF Up! You've Got Super Armor! Ki Rec. SPD Down.** Limit Burst.
- [x] Refreshed 035 with the secondary-evidence-supported battle-start health-drain/subsequent broad-stat-boost description and **Auto Just Guard** Limit Burst.
- [x] Preserved canonical PQ edges: **033→PQ185, 035→PQ186**; Super Soul 034 remains intentionally unresolved rather than being populated from speculation.
- [x] Added `docs/data/super-soul-033-035-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence includes the maintained Super Soul catalogue plus recent community testing/discussion. Numerical values remain explicitly secondary where item-level confirmation is unavailable.
- [x] Validation: canonical Super Soul layer remains **234 records**; selected records parse with populated Limit Burst fields; canonical PQ relationships unchanged; audit registration completed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Commits: `5ba2dfc2c7e096d996a91920b195b285329a2db7`, `a1ee80508c04e6a8a9068670314f96fc0cdc6ca3`, `da5df6b2e5b23d57ae3067f696f96bae05f2717b`.
- [ ] Exact next priority: continue the live thin census with the next highest-impact unresolved records, prioritizing exact-name evidence and PQ/cross-domain reuse; append only to this canonical handoff.

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
- [x] Recomputed the live canonical Super Soul layer before editing: 234 records / 0 duplicate IDs.
- [x] Bounded batch expanded to the next exact-name PQ-linked cluster: 220–223, then 224–228, for 9 records total.
- [x] Refreshed character/DLC provenance, trigger/effect/magnitude, supported duration/stacking, Limit Burst, verification date, and source provenance for all 9 selected records.
- [x] Preserved canonical PQ navigation: 220→PQ137, 221→PQ137, 222→PQ138/PQ151, 223→PQ138, 224→PQ140, 225→PQ140, 226→PQ141, 227→PQ141, 228→PQ142.
- [x] Added and registered docs/data/super-soul-220-223-mechanics-audit-2026-09-22.json and docs/data/super-soul-224-228-mechanics-audit-2026-09-22.json.
- [x] Evidence used: maintained Xenoverse 2 Super Soul catalogue, maintained all-PQ guide, and independent GameFAQs/community references. No reward probability or unsupported Ultimate-Finish gate was inferred.
- [x] Validation after writes: canonical layer remains 234 records / 0 duplicate IDs; all 9 selected records are researched; all have populated character, trigger, effect, magnitude, and Limit Burst fields; canonical PQ relationships remain unchanged.
- [ ] CI/runtime: no successful workflow/check exposed for the direct-commit chain; no CI success claimed.
- [x] Commits: canonical 220–223 74291bd44003e9e1850a456792f9bb416e26d4aa; audit bf4ce64334ea14855867ac262ff008ed7903b041; index c8940618b9cbd14e4399a2fd9b60a7f1f07e1f41; canonical 224–228 f9f05b2e40925011a43ac05033e43d22e05803b6; audit b7774c960d5397923cd5890627e0c2f4143fff17; index 5fc50ebf3dbabfbd8707d55273667120f9c7578f.
- [ ] Exact next priority: recompute the live indexed/thin census again and select the next 4–12 highest-impact unresolved PQ-linked records with strong exact-name evidence and reusable cross-domain relationships; preserve unresolved identity conflicts and do not guess unsupported mechanics. Do not create another dated continuation prompt.

### 2026-09-22 cycle update — Super Soul 229–231 and 237–239 mechanics/status refresh
- [x] Recomputed the live canonical layer and selected six exact-name PQ-linked records with strong existing mechanics evidence: 229, 230, 231, 237, 238, 239.
- [x] Upgraded all six from indexed to researched and completed the remaining core completeness/status work without changing their canonical PQ relationships.
- [x] Preserved canonical PQ navigation: 229→PQ143, 230→PQ145, 231→PQ151, 237→PQ158, 238→PQ178, 239→PQ021.
- [x] Added and registered docs/data/super-soul-229-231-237-239-mechanics-audit-2026-09-22.json.
- [x] Evidence used: maintained Xenoverse 2 Super Soul catalogue plus the repository's existing PQ provenance sources. No unsupported drop probability or Ultimate-Finish condition was introduced.
- [x] Validation: canonical layer remains 234 records / 0 duplicate IDs; all six selected records are researched; all have populated character, trigger, effect, magnitude, and Limit Burst fields; PQ edges remain unchanged.
- [ ] CI/runtime: no successful workflow/check exposed for the direct-commit chain; no CI success claimed.
- [x] Commits: canonical 90f98624fa06d4c8851b9d853061561838660b6a; audit e95ca9de3f089355df5f289ce016427604754129; cross-domain index 8b1007fb668a16abd1c05a9757b070719ed22659.
- [ ] Exact next priority: recompute the live thin/indexed census and select the next 4–12 unresolved PQ-linked records with strong exact-name evidence; records 232–236 remain a high-value unresolved cluster and should be researched only when exact-name evidence is sufficient. Do not create another dated continuation prompt.

### 2026-09-22 cycle update — Super Soul 240–244 provenance/mechanics refresh
- [x] Researched the next evidence-supported early-PQ cluster: Super Souls 240–244.
- [x] Upgraded 240–244 from indexed/partially verified to researched while preserving their existing canonical PQ relationships: 240→PQ026, 241→PQ028, 242→PQ029, 243→PQ035, 244→PQ036.
- [x] Added maintained Super Soul catalogue provenance to each selected record and retained independent early-PQ references already present where applicable.
- [x] Added and registered docs/data/super-soul-240-244-provenance-mechanics-audit-2026-09-22.json.
- [x] Validation: 234 canonical records / 0 duplicate IDs; all five selected records are researched and have populated core mechanics fields; no canonical PQ edge changed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: return to the unresolved Conton City Vote Pack/Hero of Justice cluster 232–236 only when exact-name mechanics evidence is strong enough; otherwise continue the live census for another evidence-supported 4–12 record batch. Do not guess unsupported mechanics.
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


### 2026-09-22 cycle update — early Super Soul secondary-field reconciliation (001 / 003 / 006 / 012)
- [x] Live census before editing: **234 canonical Super Soul records / 0 duplicate IDs / 188 records missing at least one of the current eight strict core fields**.
- [x] Bounded batch: **super-soul-001, 003, 006, and 012**, selected from the deterministic early/base-game thin queue because their remaining gaps were secondary fields resolvable as genuinely non-applicable from exact-name evidence.
- [x] Reconciled **001** effect magnitude and stacking as **N/A**; **003** stacking as **N/A**; **006** stacking as **N/A**; and **012** duration as **N/A**.
- [x] Refreshed source provenance and `last_verified` to **2026-09-22** while preserving acquisition, Limit Burst, and canonical identity semantics.
- [x] Added `docs/data/super-soul-secondary-field-reconciliation-001-003-006-012-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Evidence limits preserved: no unsupported numeric mechanics, timed windows, or stack behavior were inferred. **Super Soul 013** remains unresolved where available evidence does not establish duration/magnitude.
- [x] Validation: canonical layer remains **234 records / 0 duplicate IDs**; strict eight-field thin count decreases from **188 to 184**.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [x] Repository writes: canonical, audit, cross-domain index, changelog, and handoff are the bounded outputs for this cycle.
- [ ] Exact next priority: continue the deterministic early/base-game thin census from the lowest-source/highest-confidence remaining records, beginning with **Super Soul 013** only if exact-name evidence can resolve an applicable field; otherwise skip it and advance. Do not force N/A merely to reduce the thin count.


### 2026-09-22 cycle update — early Super Soul secondary-field reconciliation (013 / 014 / 017 / 026)
- [x] Live batch selected from the current early/base-game thin census after the previous 001/003/006/012 pass.
- [x] Reconciled **013 Kieeeee!!**, **014 Your life is mine! Toh!**, **017 Unleash your power!!**, and **026 Let me show you how it's done.** using exact-name catalogue and independent guide evidence.
- [x] 013: set effect magnitude, duration, and stacking to **N/A** because only the Slow-status effect is documented and no numeric magnitude/duration/stacking mechanic is established.
- [x] 014, 017, 026: set stacking to **N/A**; existing trigger/effect/duration and Limit Burst fields were preserved.
- [x] Added `docs/data/super-soul-secondary-field-reconciliation-013-014-017-026-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved evidence boundary: **024** and **025** remain unresolved for duration rather than being forced to N/A.
- [x] Canonical PQ relationships and acquisition identities were unchanged.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Exact next batch: continue the early/base-game thin census, prioritizing records whose remaining missing fields are directly resolvable from exact-name evidence; revisit 024/025 only if stronger duration evidence appears.


### 2026-09-22 cycle update — Super Soul secondary-field reconciliation (002 / 004 / 008 / 010 / 011 / 028–031)
- [x] Reconciled **9** early/base-game thin records: 002 Flying Nimbus!!, 004 Your death is imminent!, 008 Tien, please don't die, 010 I'll kill all of you!!, 011 H-How could he?!, 028 Popporunga pupirittparo, 029 The ultimate power is mine!, 030 I'll never forgive you, scum!, and 031 Drop dead!!!.
- [x] Added trigger-bound duration semantics where directly supported: 002 **Until taking damage**, 004 **While Turn Giant is active**, 010 **While Ki is at 100%**.
- [x] Marked 008 duration **N/A** because the KO-triggered Ki restoration is instantaneous.
- [x] Marked stacking **N/A** for all nine because the available exact-name evidence documents no stacking mechanic.
- [x] Added `docs/data/super-soul-secondary-field-reconciliation-002-004-008-010-011-028-031-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Preserved acquisition, PQ cross-links, effect magnitudes, and Limit Burst semantics.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue deterministic early/base-game thin census, prioritizing records whose remaining fields can be directly established without speculative values.


### 2026-09-22 cycle update — Super Soul secondary-field reconciliation (024 / 025)
- [x] Reconciled the previously unresolved **024** and **025** duration gaps using stronger exact-name catalogue evidence.
- [x] 024 duration = **N/A** and stacking = **N/A**; 025 duration = **N/A** while its once-only behavior remains documented in stacking_behavior.
- [x] Added `docs/data/super-soul-secondary-field-reconciliation-024-025-2026-09-22.json` and registered it in the cross-domain index.
- [x] No acquisition, PQ relationship, effect magnitude, or Limit Burst semantics changed.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue the deterministic thin census with the next genuinely unresolved applicable fields; do not force unresolved mechanics without direct evidence.


### 2026-09-22 cycle update — Super Soul secondary-field reconciliation (007 / 047)
- [x] Reconciled **007 Gyau!!!!** as a no-special-effect Super Soul: trigger, magnitude, duration, and stacking are **N/A**; its Revive Gauge Auto-Recovery Limit Burst remains preserved.
- [x] Reconciled **047** Limit Burst to **Auto Health and Stamina Recovery!; DEF Down.** from independent raid documentation.
- [x] Added `docs/data/super-soul-secondary-field-reconciliation-007-047-2026-09-22.json` and registered it in the cross-domain index.
- [ ] CI/runtime: no successful workflow/check exposed; no CI success claimed.
- [ ] Next priority: continue the thin census; 032 and 034 remain unresolved where direct item-level mechanics are still insufficiently evidenced.

### 2026-09-22 cycle update — Super Soul 245–246 research promotion
- [x] Bounded batch: **Super Soul 245** ("This fight...is truly pointless...") and **Super Soul 246** ("I actually felt that one...").
- [x] Reconfirmed exact-name character identity, mechanics, Limit Burst, and PQ provenance using the maintained Super Soul catalogue plus independent historical/character/PQ evidence. 245 remains tied to **PQ38**; 246 remains tied to **PQ12**.
- [x] Promoted both records from `partially_verified` to `researched`; refreshed `last_verified` to **2026-09-22**.
- [x] Preserved evidence boundaries: no unsupported reward probabilities, Ultimate-Finish requirements, engine-level timing, or internal rate values were added.
- [x] Added the promotion note to the canonical Super Soul research notes.
- [x] Updated `docs/data/super-soul-242-through-246-provenance-audit-2026-09-22.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- [x] Live canonical validation after write: **234 records / 0 duplicate IDs**; 245 and 246 are both `researched`, each with 3 sources and a canonical PQ edge.
- [x] Commits: canonical `8ab4dc33f3461fc597e95e8a9099e2f8c5ee1620`; audit `65c7afd2d65c0d3d48cf8ce72fc1f2b686f02229`; cross-domain index `b71d470f8449e24847f5b84573755c08e1aa5b86`.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next priority: recompute the live Super Soul thin-system census using the repository's established census definition, then select the next **4–12 highest-impact unresolved records**. The **232–236** cluster remains explicitly evidence-bound and should only be promoted if exact-name item-level mechanics evidence is found; otherwise skip it and continue to another evidence-supported cluster. Do not create another dated continuation prompt.

### 2026-09-22 cycle update — Raid Super Souls 054/057/058/063 evidence strengthening
- [x] Recomputed the live Super Soul corpus and selected the next high-impact partially verified raid cluster: **054, 057, 058, 063**.
- [x] Added independent raid/effect evidence to all four records.
- [x] **057 — Can I attack now?** now has corroborated Limit Burst (**ATK Up! / Ki Auto-Recovery! / Stamina Rec. SPD Down.**) and is promoted to `verified_secondary`.
- [x] **058 — Now I'm MAD!** now has corroborated Limit Burst (**DEF Up! / You've Got Super Armor! / Ki Rec. SPD Down.**) and is promoted to `verified_secondary`.
- [x] **063 — Zudodoeyaahh!** now has corroborated **+100% / XXL throw boost** and **Auto Just Guard** Limit Burst and is promoted to `verified_secondary`.
- [x] **054 — Leave my daddy alone!** gained independent raid-reward evidence, but remains `partially_verified` because its Limit Burst is still unresolved.
- [x] Refreshed `docs/data/super-soul-thin-census-2026-09-22.json`.
- [x] Post-edit live validation: **234 canonical / 0 duplicate IDs**; statuses **86 partially_verified / 11 verified / 97 verified_secondary / 27 researched / 13 indexed**.
- [x] Live strict-thin count is **182** under the current eight-field census definition. This differs from the older checkpoint's 139 and should be treated as the freshly recomputed live value, not as a regression claim.
- [x] Evidence boundaries preserved: no unsupported exact timing, reward probability, or internal engine-rate values were promoted.
- [x] Commit: canonical Super Soul data **55fbdb048c4e63eb019c52986e81ebf12b805697**; refreshed census **507ea19864a4c5c78a5a17629c71b86feb6e7278**.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next priority: continue the deterministic partially-verified Super Soul census, preferring records with multiple unresolved core fields and at least two independent exact-name sources. Recheck **054** only if stronger Limit Burst evidence appears; otherwise move to the next evidence-supported cluster. Do not create a new continuation prompt.

### 2026-09-22 cycle update — Super Souls 049/060 evidence strengthening
- [x] Continued the deterministic partially-verified Super Soul census after the raid batch.
- [x] Selected **049 — "Killed all Earthlings!"** and **060 — "I...hate you!!!"** because both had complete meaningful mechanics already populated but lacked an independent historical source beyond the maintained catalogue/research corpus.
- [x] Added the independent GameFAQs Super Soul guide to both records.
- [x] Promoted **049** and **060** to `verified_secondary`.
- [x] Preserved evidence boundaries: 049 remains an always-active effect with no invented timed duration/stacking; 060 retains the known Charged Ki Blast vs Ki Blast Skill wording discrepancy rather than silently normalizing it.
- [x] Refreshed live thin census: **234 records / 0 duplicate IDs / 182 strict-thin records** under the current eight-field definition.
- [x] Commits: canonical **fb2dd563cfeeb5c4ef6dc127523e7943fc5fb2f**; census **7dda4fe942b4503a7f99134ea55a61019c41c6b9**.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next priority: continue the deterministic partially-verified census. **034** remains an evidence-boundary record because item-level mechanics are still unresolved; next eligible records are the high-source-count partially verified records such as **032, 191, 194, 196, 197, 199, 155, 173–175, 177, 179, 186, 187**. Promote only fields independently supported by exact-name evidence. Do not create another continuation prompt.

### 2026-09-22 cycle update — Super Souls 191/194/196 evidence strengthening
- [x] Continued the deterministic partially-verified Super Soul census.
- [x] Strengthened **191 — "Earth is in your hands now!"**, **194 — "Time to get serious, I guess."**, and **196 — "This heat...will be your downfall!"** with exact-name/historical evidence.
- [x] Promoted all three to `verified_secondary`.
- [x] Recorded non-stacking behavior as **N/A** where direct evidence supports that no stacking mechanic applies.
- [x] Preserved **194's current +25% all-attacks value**; older community reports of a historical +35% state were documented as historical context rather than promoted as current canonical mechanics.
- [x] Refreshed strict-thin census: **234 canonical / 0 duplicate IDs / 182 strict-thin** under the current eight-field definition.
- [x] Canonical commit: **d08438c050a5033519eb6e80fe768aaa80a7d4b7**; census commit: **fcc0cbe409c92b1676fcabcad758d3b0fd2ef4ab**.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next priority: continue the partially-verified Super Soul census with **032, 155, 173–175, 177, 179, 186, 187, 197, 199** and other records whose remaining fields can be independently resolved. Keep **034** evidence-bound unless exact-name item-level mechanics are found. Do not create another continuation prompt.

### 2026-09-22 cycle update — Super Souls 174/177/186/199 evidence strengthening
- [x] Bounded batch: **174, 177, 186, and 199**.
- [x] Added independent historical/community evidence confirming named trigger/effect behavior and promoted all four to `verified_secondary`.
- [x] Preserved unresolved duration/stacking fields rather than inferring values from absence of a timer in secondary sources.
- [x] Live census after editing: **234 canonical / 0 duplicate IDs / 182 strict-thin**.
- [x] Canonical commit: **46e6deb1efd6a62c5e6fd4f9277d1b892d66cbd9**; census commit: **c69890aae01b0677bacd450554cd424e3c924c64**.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next batch: continue deterministic partially-verified Super Soul reconciliation, prioritizing **155, 173, 175, 179, 187, 197, 032**, while keeping **034** evidence-bound unless exact-name item-level mechanics become independently established.


### 2026-09-22 cycle update — Super Souls 155/173/175/179/187/197 evidence reconciliation + 032 boundary review
- [x] Recomputed the live canonical Super Soul layer before editing: **234 records / 0 duplicate IDs**.
- [x] Bounded batch: **155, 173, 175, 179, 187, 197**, the next deterministic high-source partially-verified records from the prior queue.
- [x] Promoted all six to `verified_secondary` after independent exact-name mechanics/acquisition corroboration.
- [x] Preserved 179's documented **-20% guard-break recovery** value; historical ~29–30% community testing was not promoted over the maintained canonical/stat-sheet value.
- [x] Added independent character/DLC/reference evidence where useful, including the Majin Buu page for 187 and current GameFAQs evidence for 197.
- [x] Re-audited **032** and retained `partially_verified`: PQ185 acquisition is corroborated, but item-level mechanics remain secondary/community-tested and its Limit Burst remains unresolved.
- [x] Added and registered `docs/data/super-soul-155-173-175-179-187-197-032-evidence-reconciliation-2026-09-22.json`.
- [x] No canonical PQ relationship identities changed; no reward probabilities, unsupported Ultimate-Finish requirements, or engine-level mechanics were invented.
- [x] Live status counts after the batch: **71 partially_verified / 11 verified / 112 verified_secondary / 27 researched / 13 indexed**; strict-thin census remains a field-completeness metric and was not artificially reduced by status changes.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next priority: recompute the live strict-thin Super Soul census and select the next **4–12 evidence-supported partially-verified records** with multiple unresolved applicable fields. Preserve **034** as an evidence boundary and do not force unresolved mechanics.

### 2026-09-22 cycle close — live thin-census recomputation and next queue
- [x] Recomputed the live canonical Super Soul layer after the 155/173/175/179/187/197 batch: **234 records / 0 duplicate IDs / 182 strict-thin records** under the established eight-field definition.
- [x] Current high-value partially-verified queue from the live layer: **054** (4 missing core fields), **034** (3; retain evidence boundary), then **157, 159, 163, 164** (2 each).
- [x] The queue is based on actual missing core fields and source counts, not numeric order alone.
- [ ] The existing docs/data/super-soul-thin-census-2026-09-22.json remains the prior checkpoint artifact; an attempted direct refresh was blocked by the repository write safety layer, so its older notes were not overwritten.
- [ ] CI/runtime: no successful workflow/check exposed; do not claim CI success.
- [ ] Exact next batch: **Super Soul 054** if stronger Limit Burst evidence can be independently established; otherwise skip without fabrication and move to **157/159/163/164**. Keep **034** evidence-bound unless exact-name item-level mechanics evidence improves.

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
- Exact next task: recompute the live strict-thin queue and select the next **4–12 evidence-supported partially-verified records**; keep **034** evidence-bound unless exact-name item-level mechanics evidence improves.


### 2026-09-22 — Super Soul Limit Burst reconciliation (053 / 056 / 059 / 065)
- Reconciled **053, 056, 059, and 065** with exact-name Fandom and independent GameFAQs evidence.
- Populated their documented Limit Burst type/effect fields; duration and stacking remain unresolved where the evidence does not establish them.
- Added and registered `docs/data/super-soul-053-056-059-065-limit-burst-reconciliation-2026-09-22.json`.
- No canonical PQ relationship, acquisition identity, reward probability, or Ultimate-Finish requirement changed.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next task: continue the live strict-thin queue with the next evidence-supported partially verified records; preserve unresolved fields rather than guessing.


### 2026-09-22 cycle correction — live Super Soul queue after 053/056/059/065
- Live canonical Super Soul layer: **234 records / 0 duplicate IDs / 174 strict-thin records** under the established eight-field definition.
- Completed secondary-field workstreams in this cycle: **024–031** Limit Burst effects and **053/056/059/065** Limit Burst type/effect fields.
- Current partially-verified queue from the live canonical layer, ordered by unresolved core-field count/source support: **034** (3 missing; explicit evidence boundary), **202** (2 missing; 1 source), **032** (2 missing; 5 sources), followed by **200, 201, 203–209** (1 unresolved field each, currently single-source records).
- **034 must remain a skip/boundary unless exact-name item-level mechanics evidence independently resolves its missing fields.** Do not manufacture values from acquisition-only evidence.
- Exact next task: investigate **032** only if exact-name Limit Burst evidence can be independently established; otherwise move to the next evidence-supported partially-verified cluster and preserve unresolved fields.
- CI/runtime: no successful workflow/check exposed; do not claim CI success.


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


### 2026-09-22 cycle update — Super Soul 049/053/056/058/059/060/063/065 secondary-field reconciliation
- Live census before editing: **234 canonical / 0 duplicate IDs / 138 strict-thin records**.
- Bounded batch: **Super Souls 049, 053, 056, 058, 059, 060, 063, and 065**.
- Research/evidence: maintained exact-name Super Soul catalogue plus the independent historical GameFAQs Super Soul guide already attached to the canonical records; repository research-corpus entries were retained where applicable.
- Changes: explicit duration semantics added for always-active, condition-bound, one-time, and trigger-bound effects; `stacking_behavior` set to **Not reported as stackable** where no documented stacking rule/cap exists.
- Evidence limits preserved: no numeric timer, stack cap, acquisition probability, Ultimate-Finish condition, or unrelated mechanic was inferred.
- Added/registered audit: `docs/data/super-soul-049-053-056-058-059-060-063-065-secondary-field-reconciliation-2026-09-22.json`.
- Validation: **234 canonical / 0 duplicate IDs / 130 strict-thin records**; JSON parse succeeded; audit registration parity clean; no internal AI/UI/search citation artifacts detected.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next batch: recompute the live strict-thin queue and select the next evidence-supported early/base-game/high-impact cluster; keep **032/034** as explicit evidence boundaries unless independent exact-name mechanics evidence resolves them.


### 2026-09-22 cycle update — Super Soul 044/045/046/054/055/178/185 secondary-field reconciliation
- Live census before editing: **234 canonical / 0 duplicate IDs / 130 strict-thin records**.
- Bounded batch: **044, 045, 046, 054, 055, 178, 185**.
- Research/evidence: exact-name Super Soul catalogue plus independent GameFAQs raid/DLC documentation and existing repository research-corpus evidence.
- Changes: populated Limit Burst effects for **044/045/046**; set **054/055** stacking to **Not reported as stackable**; made **178/185** non-timed duration semantics explicit.
- Evidence limits preserved: **044** has a documented Ki-vs-Stamina wording discrepancy in its main effect, so that unrelated field was not rewritten; stacking for **044–046** remains unresolved because this pass did not establish a rule/cap.
- Added/registered audit: `docs/data/super-soul-044-045-046-054-055-178-185-secondary-field-reconciliation-2026-09-22.json`.
- Validation: **234 canonical / 0 duplicate IDs / 123 strict-thin records**; changed JSON parsed successfully; audit registration confirmed; no unsupported values were inferred.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next batch: recompute the live strict-thin queue and continue the next evidence-supported one-field cluster, prioritizing exact-name evidence and cross-database usefulness while preserving real evidence boundaries.


### 2026-09-22 cycle continuation — Super Soul 070/071/078/080 duration reconciliation
- Live census before editing: **234 canonical / 0 duplicate IDs / 123 strict-thin records**.
- Bounded batch: **070, 071, 078, 080**.
- Research/evidence: exact-name Super Soul catalogue/stat-sheet evidence and existing repository research-corpus records.
- Changes: explicit non-timed duration semantics added for always-active, condition-bound, and trigger-bound effects; no numeric timers inferred.
- Added/registered audit: `docs/data/super-soul-070-071-078-080-duration-reconciliation-2026-09-22.json`.
- Validation: **234 canonical / 0 duplicate IDs / 119 strict-thin records**; audit registration confirmed; changed JSON parsed successfully.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `57bd6587cba9e578be16ce36fb6e983c3dc0b6b1`, `5355b18b589161e35e29edc1aa904aeef0be5eff`, `bae2496a52f503c90f635076c3c74c7f5cfabea2`, `b903a68215da89cb78731405ea4c263699c1f52c`, `8a381bb8f2576d1914e3a0d9cd1dde315586ca6c`.
- Exact next batch: recompute the live strict-thin queue and continue the next evidence-supported one-field cluster; current top candidates begin with **201, 154, 156, 160, 161, 162, 165, 166, 172**, while preserving genuine evidence boundaries.


### 2026-09-22 cycle continuation — Super Soul 154/160/162/165 stacking reconciliation
- Live census before editing: **234 canonical / 0 duplicate IDs / 119 strict-thin records**.
- Bounded batch: **154, 160, 162, 165**.
- Research/evidence: maintained exact-name Super Soul catalogue, independent historical Super Soul guide, and player-facing stat-sheet evidence.
- Changes: `stacking_behavior` set to **Not reported as stackable** for all four; evidence establishes their triggers/effects/durations but does not document stacking or a numeric cap.
- Added/registered audit: `docs/data/super-soul-154-160-162-165-stacking-reconciliation-2026-09-22.json`.
- Validation: **234 canonical / 0 duplicate IDs / 115 strict-thin records**; JSON parse succeeded; audit registration confirmed; no unrelated fields changed.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `c26fe9a931a9e560db5661882f0fe9da3fdd5438`, `2f43493b85398c865841a2dca1fcee1cd373b171`, `86114d202a0acbd6daa098b8128d6cd473d393b7`, `76c7cb7275f5dbc2f922a28f347aff83e8eed608`, `35f8d11f8cf1b51a825e22fd30a3d3949db4b7e8`.
- Exact next batch: recompute the live strict-thin queue and continue the next evidence-supported duration cluster, beginning with **156, 161, 166, 172**; preserve genuine evidence boundaries rather than forcing nulls into guessed timers.
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



### 2026-09-23 cycle update — unified PQ reverse-index exact-pair census
- Inspected the live canonical PQ relationship layer and the unified reverse-index projection after the prior standalone reverse-index repairs.
- Compared every canonical typed PQ relationship against the unified reverse index at exact target/PQ pair level, treating equipment as the union of the clothing and accessory projection domains.
- Live parity: **859 canonical pairs / 859 unified projection pairs / 0 missing / 0 extra / 0 duplicate projection pairs / 0 invalid PQ numbers / 0 invalid list fields**.
- Current domain counts: **244 skills / 151 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming**.
- Corrected deterministic audit metadata drift in `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json`: the live equipment projection split is **84 clothing / 40 accessories = 124**, replacing its stale historical 83/41 split while preserving the historical audit record.
- No canonical relationship identities were changed and no partial-source omission was promoted into canonical data.
- CI/runtime: the connector environment did not execute the repository Python validator; do not claim runtime validation or CI success. The exact live pair census is recorded as structural/connector validation.
- Audit commit: `254e25870c0f933bf5821136b5374df14f5aff8d`.
- Exact next task: inspect the remaining generated/reconciliation artifacts for stale **current-state** producer metadata/counts outside the already audited PQ relationship reports, repair only deterministic drift, and preserve all historical counts/scopes. Do not begin new provenance enrichment until this structural scan is clean.

### 2026-09-23 cycle update — deterministic current PQ metadata drift repair
- Completed the next handoff priority: scanned generated/reconciliation artifacts for stale current-state PQ relationship metadata.
- Found three deterministic current-looking fields: `docs/data/pq-cross-domain-status.json` had `target_normalization_audit_2026_09_22.total_edges=860`; `docs/data/pq-reward-relationships.json` had `current_counts.equipment=125` and `current_reconciliation_2026_09_22` at 860 total / 125 equipment.
- Repaired those fields to the live canonical baseline: **859 total / 244 skill / 151 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**.
- Preserved explicitly historical 840/860/862-era snapshots and dated provenance unchanged.
- Updated `docs/data/pq-current-baseline-field-drift-audit-2026-09-22.json` with the 2026-09-23 resolution record.
- Validation: re-read all three edited JSON files; current fields now match the 859-edge canonical baseline. No canonical relationship edge was added, removed, or inferred.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `aaa0ae605eb60b5b37f8959fd4b950142dcfa75f`, `0b656b6a3ac9461c9b5c483966981d31301cf4f7`, `2f5cbf7da971a9a6a314770ba764c1cd9ed21ee3`.
- Exact next task: recompute the live strict-thin Super Soul census and continue the next evidence-supported high-impact cluster, beginning with the remaining one-field records identified by the latest live queue; preserve **032/034** as evidence boundaries.

### 2026-09-23 cycle update — Super Soul 087–095 canonical secondary-field synchronization
- Live census before editing: **234 canonical / 0 duplicate IDs / 93 strict-thin records**.
- Bounded batch: **Super Souls 087–095**.
- Research/evidence: existing exact-name duration reconciliation plus current exact-name catalogue and independent GameFAQs evidence; the evidence documents condition-bound, permanent-while-equipped, trigger-bound, timed, instantaneous, and end-of-battle semantics, while providing no numeric stacking caps for this batch. citeturn1search1turn0search0turn0search5
- Changes: synchronized canonical `duration` fields for **087–090 and 092–095**; **091** already had its duration synchronized. Set `stacking_behavior` to **Not reported as stackable** for all nine because no documented stacking mechanic/cap was established.
- Evidence limits preserved: **089** retains an unresolved finite timer; no stack cap or unsupported timer was invented.
- Added canonical-sync metadata to `docs/data/super-soul-087-095-duration-reconciliation-2026-09-22.json` and refreshed `docs/data/super-soul-thin-census-2026-09-22.json`.
- Validation: **234 canonical / 0 duplicate IDs / 85 strict-thin records**; all nine batch records now have all eight strict-core fields populated. JSON re-read/parse succeeded.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `79ced2a6564e3d898d6faf3c235a30efe2cc2bfb`, `489ddac383a18f03723470beac739d8d562363f5`, `b2072ddb25ae4660768f763d70d6be315dc072b1`, `94450bfa343e41652e5cbe318ac0ca739b447ca5`.
- Exact next batch: recompute the live strict-thin queue and continue the next evidence-supported early/base-game/high-impact cluster; prioritize records with multiple unresolved core fields and at least two independent exact-name sources, while preserving **032/034** as evidence boundaries.

### 2026-09-23 cycle update — Super Soul 051, 096–099 secondary-field reconciliation
- Continued from the live strict-thin queue after the 087–095 batch.
- Bounded batch: **Super Souls 051, 096, 097, 098, 099**.
- Evidence was checked against the maintained exact-name corpus in the external research repository plus the local canonical source list. The exact-name corpus explicitly documents the trigger/effect semantics and, where available, measured durations/stacking.
- Changes to canonical `docs/data/super-souls-record-layer.json`:
  - **051 “Can I attack now?”** — ~2-second Super Attack Ki-recovery pulse; stacking explicitly not reported.
  - **096 “Heh heh! I'm not as rusty as I look!”** — explicit 3-stack ceiling; no finite timer reported, so duration is represented as non-timed/ongoing rather than inventing one.
  - **097 “See? It's a good thing I was here, right?”** — ~10-second recovery mode; no stacking rule reported.
  - **098 “I can tell you're an amateur by the way you pose!”** — ~30-second debuff; no stacking rule reported.
  - **099 “That's minus ten points!”** — instantaneous once-only Heavy Smash-triggered Ki reduction; no timed duration or stacking rule.
- Strict-thin census reduced **85 → 80**. All five now have populated duration and stacking fields.
- No unsupported numeric stack cap was introduced; the only explicit cap promoted was the source-documented **3 stacks** for 096.
- Validation: canonical JSON re-read successfully and live strict-core census recalculated to **80 strict-thin / 234 records / 0 duplicate IDs**.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `10d87c2d84e57b47809549a7ecb11d195972ec4c`, `7e162c426e44348ae4252d92fd1a8826981947e8`.
- Exact next task: recompute the strict-thin queue and continue the next evidence-supported early/base-game cluster; prioritize records with multiple unresolved core fields and exact-name evidence, preserving **032/034** as evidence boundaries.

### 2026-09-23 cycle update — Super Soul 100–107 duration/stacking reconciliation
- Recomputed the live strict-thin queue: **234 canonical / 0 duplicate IDs / 64 records with ≥2 missing strict-core fields** before this batch.
- Bounded batch: **100–107** — I'm a super hero!; Just figured out who the real villain is!; Help me, Daddy! I'm scared!; Damn... Gonna have to go all out!; Not a single word!; I'm a whole new me.; Shenron really went the extra mile.; Enter the hero!.
- Exact-name research corpus supplied explicit temporary/persistent semantics for the previously missing duration fields and stacking behavior.
- Canonical changes:
  - 100: ~10-second temporary Ki-restoration boost; no stacking reported.
  - 101: ~30-second one-time lock-on/off restriction; always-on buffs remain persistent; no stacking reported.
  - 102: ~20-second team attack boost; Ki restoration instantaneous; no stacking reported.
  - 103: ~60-second delayed activation, then remainder-of-battle persistence; no stacking reported.
  - 104: instantaneous revival-triggered Ki restoration; no stacking rule reported.
  - 105: remainder-of-battle persistence after the below-50%-Health trigger; no stacking reported.
  - 106: instantaneous end-of-battle item-drop-rate effect; no stacking reported.
  - 107: persistent stacked pose buff; explicit **5-stack cap** retained.
- Strict-thin queue reduced **64 → 56**.
- No unsupported stack cap, reward probability, or Ultimate-Finish condition was introduced.
- Validation: canonical JSON reread/parsed successfully; 234 records remain with 0 duplicate IDs.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `d6705ccee706f74045754c1b6b5b374216cac337`, `370bed450667ddd4c9cde4695e3c4cd17892603a`.
- Exact next task: recompute the strict-thin queue and continue the next evidence-supported cluster, prioritizing early/base-game/high-impact records and preserving **032/034** evidence boundaries.

### 2026-09-23 cycle update — Super Soul 121–128 duration/stacking reconciliation
- Live multi-missing queue before editing: **64** records; after the previous 100–107 pass, the next evidence-rich cluster was **121–128**.
- Reconciled duration semantics for **121–128** from the maintained exact-name research corpus.
- Added explicit ~20-second opening duration for 121; condition-bound semantics for 122 and 126; temporary-but-unresolved exact duration for 123 and 127; permanent while equipped for 124 and 128; ~5-second duration for 125.
- Set stacking to **Not reported as stackable** for all eight because no documented numeric stacking mechanic was established in the evidence used.
- Evidence limits preserved: no unsupported timer or stack cap was invented.
- Strict-thin count reduced **56 → 48**.
- Validation: canonical JSON reread/parsed; 234 records / 0 duplicate IDs.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Commits: `314b4679b622f1fa66968c5522589fa493b278ca`, `5ba1cdaf7d392d01fe9a8fbab9302ed0831845ae`.
- Exact next task: recompute the live strict-thin queue and continue the next evidence-supported early/base-game/high-impact cluster, preserving **032/034** as evidence boundaries.


### 2026-09-23 cycle update — Super Soul 129–143 secondary-field reconciliation
- [x] Recomputed the live canonical Super Soul layer after the prior 121–128 pass: **234 canonical records / 0 duplicate IDs / 60 strict-thin records** under the eight-field census definition.
- [x] Bounded batch: **Super Souls 129–143**.
- [x] Evidence: maintained exact-name Super Soul catalogue plus the independent Madreag Xenoverse 2 research corpus; current web corroboration also confirms the relevant exact-name mechanics, including the explicit stack cap for 133 and explicit timed effects for 134, 136, 140, and 142. citeturn1search0turn2search1turn2search14turn3search0turn4search0
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
- [x] Evidence: maintained exact-name Super Soul catalogue plus independent research/guide sources; exact-name current catalogue confirms **148 = 3s/5s**, **150 = 5s**, while the other selected records lack documented stack caps in the consulted evidence. citeturn6search1turn6search0turn5search1
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
- [x] Research/evidence: maintained exact-name Super Soul catalogue and corroborating character/form pages; the catalogue exposes the documented timed effects, while trigger/condition text was not converted into invented timers. citeturn0search4turn0search5turn0search17
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
- [x] Research/evidence: repository source URLs plus current maintained Super Soul references were checked. Evidence supports distinguishing permanent, condition-bound, and instantaneous effects from finite timed buffs. citeturn3search0turn3search2turn3search8turn3search27
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


### 2026-09-23 cycle update — Super Soul 211–223 secondary-field reconciliation
- Recomputed the live canonical layer before editing: **234 canonical / 0 duplicate IDs / 23 strict-thin records**.
- Bounded batch: **211–223**, excluding the already evidence-bound indexed-only 232–236 cluster from mechanics inference.
- Reconciled evidence-backed secondary fields: 211 no-stacking; 212 Limit Burst effect; 213–215 no-stacking plus Limit Burst effects; 216 Limit Burst effect; 217 no-stacking; 218 Limit Burst effect; 219 no-stacking plus Limit Burst effect; 220–223 Limit Burst effects.
- Preserved evidence boundaries: **217 remains unresolved for Limit Burst fields**; no unsupported timer or numeric stack cap was invented; 032/034 and indexed-only 158/232–236 remain separate evidence boundaries.
- Added audit: `docs/data/super-soul-211-223-secondary-field-reconciliation-2026-09-23.json`.
- Refreshed `docs/data/super-soul-thin-census-2026-09-22.json`: **23 → 11 strict-thin records**.
- Validation: canonical record layer reread; 234 records and 0 duplicate IDs; stored thin census matches the recomputed 11-record queue.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next priority: recompute the live 11-record queue, then resolve the strongest evidence-supported remaining field(s), beginning with **174/187 duration** or **217 Limit Burst** if exact-name evidence is available. Keep **032/034**, **158**, and **232–236** as explicit evidence boundaries unless stronger item-level evidence appears.


### 2026-09-23 cycle update — Super Soul 174/187 duration reconciliation
- [x] Recomputed live state before editing: **234 canonical / 0 duplicate IDs / 11 strict-thin records**.
- [x] Bounded batch: **174 and 187**, targeting the remaining duration-only gaps with evidence-backed semantic states.
- [x] **174**: recorded the documented 30-second post-battle-start activation delay separately from duration; no documented expiration was found, so the record now states post-delay/no documented expiration rather than inventing a timer.
- [x] **187**: recorded condition-bound Stamina-recovery semantics while Ki is maxed and explicitly noted that the temporary Ki Auto-Recovery component has no documented finite duration in the consulted evidence.
- [x] Added audit: `docs/data/super-soul-174-187-duration-reconciliation-2026-09-23.json`.
- [x] Refreshed live thin census: **11 → 9 strict-thin records**.
- [x] Validation: canonical JSON reread/parsed; **234 records / 0 duplicate IDs**; stored census matches the independently recomputed 9-record queue.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining queue: **032, 034, 158, 217, 232–236**. Keep 032/034 and indexed-only 158/232–236 as explicit evidence boundaries. **217 Limit Burst** remains the focused unresolved item-level gap; do not infer a burst from absence of evidence.


### 2026-09-23 cycle update — Do or Die same-name collision boundary
- [x] Recomputed live canonical state: **234 records / 0 duplicate IDs / 9 strict-thin records**.
- [x] Investigated **Super Soul 158 — “Do or Die”** against the repository's PQ, skill, and Super Soul crosslink layers plus external PQ evidence.
- [x] Confirmed an important data-quality boundary: **PQ 49 is also the canonical source for the Super Skill “Do or Die.”** The Super Soul record must not inherit the skill's mechanics merely because the names and PQ endpoint collide.
- [x] Preserved the PQ↔Super Soul relationship for navigation, but added an explicit evidence note preventing mechanics/character-source promotion until item-level evidence distinguishes the records.
- [x] Added audit: `docs/data/super-soul-158-do-or-die-name-collision-audit-2026-09-23.json`.
- [x] Updated `docs/data/pq-super-soul-crosslink-report.json` with the evidence-boundary metadata and refreshed its recomputation date.
- [x] No unsupported mechanics were added to Super Soul 158.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining strict-thin queue: **032, 034, 158, 217, 232–236**. Continue with evidence-backed item-level Limit Burst research for **217** before revisiting unresolved indexed records.


### 2026-09-23 cycle update — Super Soul 032 activation-state evidence refresh
- [x] Added current evidence showing **Super Soul 032** has a second activation/name-state after the user is KO'd: the displayed name changes to “Using this power should be no sweat for you guys.”
- [x] Preserved the evidence boundary: the source establishes the additional activation/name-state but does **not** establish its mechanical effect, so no Limit Burst or second-state effect was inferred.
- [x] Updated the canonical record's source list, version notes, and `last_verified` date.
- [x] Added audit: `docs/data/super-soul-032-activation-state-audit-2026-09-23.json`.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining strict-thin queue remains **032, 034, 158, 217, 232–236**. Next priority remains evidence-backed item-level research for **217 Limit Burst**; do not infer unresolved fields from absence of evidence.


### 2026-09-23 cycle update — Super Soul 217 Limit Burst evidence boundary
- [x] Performed a focused web evidence pass for **Super Soul 217 — “Power! A lotta power! It's great!”**.
- [x] Added independent community evidence corroborating its +12 Ki/+12 Stamina utility and PQ 134 association.
- [x] No consulted source identified the Soul's **Limit Burst** effect or trigger.
- [x] Preserved the unresolved Limit Burst fields; no effect was inferred from absence of evidence.
- [x] Added audit: `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json`.
- [x] Updated `last_verified` and canonical source provenance.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Remaining strict-thin queue remains **032, 034, 158, 217, 232–236**. 217 is now an explicit evidence-boundary result; next work should move to 034 or the indexed 232–236 records only when item-level evidence can be obtained.


### 2026-09-23 cycle update — Super Soul 232–236 indexed identity-conflict audit
- [x] Live state at cycle start: **234 canonical / 0 duplicate IDs / 9 strict-thin records**; remaining queue is **032, 034, 158, 217, 232–236**.
- [x] Investigated the indexed-only **Super Soul 232–236** cluster as the next evidence-boundary workstream.
- [x] Research/evidence: the current Steam all-PQ guide explicitly lists PQ152's Super Soul reward as **"I will put a stop to you, fiend!"** and PQ153's listed Souls as **"You're not much of a fun fight!"** and **"There's more where that came from!"**; it does not corroborate the repository's indexed-only exact-name 232–236 PQ152–155 edges. The maintained Xenoverse 2 Super Soul catalogue independently uses numeric list positions **232–236** for different raid/online-event Souls: **"You fool! Why are you laughing?", "Buu's reached full power!", "Not on my watch!", "Over here, you idiot...", and "Bye-bye, universe!"**. This establishes an identity conflict rather than mechanics evidence.
- [x] Preserved the repository relationships rather than deleting or silently remapping them; added an explicit evidence-conflict boundary to `docs/data/pq-super-soul-crosslink-report.json`.
- [x] Updated `docs/data/super-soul-232-through-236-provenance-audit-2026-09-22.json` with the conflict, current evidence, and the rule that mechanics/character provenance must not be promoted across the unresolved identity boundary.
- [x] No mechanics, duration, stacking, Limit Burst, character source, drop probability, or canonical relationship was invented or changed.
- [x] Validation: both changed JSON artifacts were parsed before write; the crosslink report retains all existing 232–236 edges and records the new evidence-boundary metadata; no strict-thin count reduction is claimed because the conflict does not establish item-level mechanics.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: audit `5d7edf87c502a94dac7b535530d508036e21ba57`; crosslink report `6ac41e7716acf3050df63509a58cace50ccf3be5`.
- [ ] Exact next batch: continue the remaining strict-thin queue with **Super Soul 034** only if stronger item-level evidence can distinguish it from title-only/PQ provenance; otherwise move to **Super Souls 232–236 identity resolution** using item-level identifiers/game-data evidence rather than numeric list position, while keeping **032, 158, and 217** as explicit evidence boundaries. Do not infer mechanics from name/PQ collisions.


### 2026-09-23 cycle update — Super Soul 034 provenance boundary refresh
- [x] Recomputed/inspected the remaining strict-thin boundary: **032, 034, 158, 217, 232–236**.
- [x] Bounded batch: **Super Soul 034 — “The final battle begins now.”**
- [x] Research/evidence: current Steam PQ186 evidence confirms the exact-name reward entry; official Nintendo FUTURE SAGA Chapter 4 documentation confirms the DLC contains **4 Super Souls** and **2 Parallel Quests**. citeturn5search0turn2search0
- [x] Strengthened canonical provenance and verification date without promoting mechanics or character-source claims that the evidence does not establish.
- [x] Updated the 034/036–039 provenance audit with the four-Super-Soul DLC inventory as corroborating context and the remaining item-identity boundary.
- [x] Evidence limits preserved: trigger, effect, magnitude, duration, stacking, Limit Burst, exact reward tier, drop probability, and independently established character source remain unresolved for 034.
- [x] Validation: canonical JSON reread/parsed; record 034 remains present and partially_verified; no strict-thin reduction claimed.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [x] Commits: canonical 0c98d6f4734865455ead5a7ed07ba7af6e164a24; audit 89adf93a6ded0e838565bb92c1f86dd40808a6da; TODO dc64ce56a24b3528af429d8433a31d25b5e97c3e.
- [ ] Exact next priority: resolve **034 item identity/mechanics** only with item-level evidence (game-data identifier, exact-name mechanics source, or equivalent). Otherwise move to **232–236 identity resolution** and keep all unresolved boundaries explicit.


### 2026-09-23 cycle update — Super Soul 232-236 identity correction
- [x] Inspected the live canonical Super Soul, PQ reward, reverse-index, acquisition, and crosslink layers for queued **232-236**.
- [x] Resolved 232-236 as a **duplicate/misattributed identity problem**, not five missing mechanics records: current catalogue positions 232-236 correspond to raid Souls already represented canonically as 040/036/041/042/043.
- [x] Removed canonical placeholder records **super-soul-232 through super-soul-236** and their five erroneous PQ152-PQ155 edges; preserved the earlier audit as historical research history.
- [x] Corrected PQ151-155: PQ151 → “I think I'm getting the hang of this.” + “I'll keep adding a bit of power to my attacks!”; PQ152 → “I will put a stop to you, fiend!”; PQ153 → “There's more where that came from!” + “You're not much of a fun fight!”; PQ154/PQ155 → no Super Soul in the maintained Basic Reward list.
- [x] Updated the canonical PQ layer, normalized reward map, reverse indexes, acquisition projection, relationship layer, cross-domain reconciliation, and Super Soul crosslink report.
- [x] Added `docs/data/super-soul-232-through-236-identity-correction-2026-09-23.json` and `docs/data/super-soul-thin-census-2026-09-23.json`.
- [x] Live result: **229 canonical Super Souls / 146 canonical PQ→Super Soul edges / 4 strict-thin records** (032, 034, 158, 217).
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next priority: continue the remaining strict-thin queue **032/034/158/217** using exact-name/item-level evidence only; do not recreate 232-236 without a distinct game-data identity key.


### 2026-09-23 cycle update — strict-thin evidence checkpoint after 232-236 correction
- [x] Live census after bounded pass: **229 canonical / 0 duplicate IDs / 4 strict-thin**; queue **032, 034, 158, 217**.
- [x] Fresh exact-name evidence pass covered **032, 034, 158, 217**. 032's existing +20% all-abilities evidence and second KO name-state remain bounded; 034's exact PQ186 reward identity is corroborated but item-level mechanics remain unresolved; 158 remains protected by the PQ49 same-name Super Skill collision boundary; 217's +12 Ki/+12 Stamina remains corroborated while Limit Burst remains unresolved.
- [x] Added docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json documenting the evidence and limits.
- [x] No unsupported mechanics, Limit Burst effects, reward probabilities, or item identifiers were promoted.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: **034 item-level mechanics/Limit Burst**, then **217 Limit Burst**, using exact-name/item-level evidence only.

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
- [x] Fresh results continue to corroborate the Soul's +12 Ki/+12 Stamina/XXL utility and PQ134 association, but did **not** establish an exact Limit Burst effect or trigger. citeturn1reddit2turn1search0
- [x] Updated `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json` with the fresh evidence boundary.
- [x] No generic/same-name Limit Burst was substituted; canonical 217 Limit Burst fields remain unresolved.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next batch: continue **217** only with item-level/game-data or exact-name Limit Burst evidence; otherwise move to another high-impact deterministic Super Soul/index reconciliation rather than guessing.

### 2026-09-23 cycle update — Super Soul 217 fresh item-level Limit Burst boundary
- Live census before editing: **229 canonical / 0 duplicate IDs / 228 strict-thin**; remaining queue: **001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 067, 068, 069, 070, 071, 074, 075, 076, 078, 080, 082, 083, 085, 086, 087, 088, 089, 090, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246**.
- Bounded batch: **Super Soul 217 — “Power! A lotta power! It's great!”**.
- Research/evidence: fresh exact-name/item-level web searches again failed to identify authoritative evidence for the Soul's Limit Burst type, trigger, or effect. Generic discussion corroborates the Soul's utility but does not safely establish the unresolved Limit Burst fields.
- Changes: appended the fresh evidence-boundary result to `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json`; canonical mechanics were intentionally not changed.
- Evidence limits preserved: no generic/same-name Limit Burst was substituted and no mechanics were inferred from absence of evidence.
- Validation: canonical JSON parsed; **229 records / 0 duplicate IDs**; strict-thin recomputation remains **228** with queue **001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 055, 056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 067, 068, 069, 070, 071, 074, 075, 076, 078, 080, 082, 083, 085, 086, 087, 088, 089, 090, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246**.
- CI: runtime/Actions success remains unavailable; no CI success claimed.
- Commit: pending until this cycle's audit/handoff/changelog writes complete.
- Exact next batch: move from blocked **217** to the next deterministic high-impact reconciliation already identified in the handoff, while keeping **032/034/158/217** explicit evidence boundaries unless new item-level evidence appears.

### 2026-09-23 correction — strict-thin census definition
- Correction to the immediately preceding 217 evidence-boundary entry: the quick raw-null scan used there was **not** the repository's strict-thin census definition and must not be treated as the live strict-thin count.
- The authoritative stored census at `docs/data/super-soul-thin-census-2026-09-23.json` remains the controlling queue: **229 canonical / 0 duplicate IDs / 4 strict-thin records**, specifically **super-soul-032, super-soul-034, super-soul-158, super-soul-217**.
- No canonical Super Soul mechanics were changed by the erroneous raw-null scan; it is superseded by this correction.

### 2026-09-23 cycle update — current PQ relationship producer-field drift repair
- [x] Audited the remaining current-looking PQ relationship producer/status fields after the prior non-PQ consumer pass.
- [x] Corrected `docs/data/pq-reward-relationships.json` `current_reconciliation_2026_09_22` from the stale **854 / 146 Super Soul** projection to the live **859 / 151 Super Soul** projection; all other current domain counts remain **244 / 151 / 124 / 247 / 86 / 7**.
- [x] Corrected `docs/data/pq-cross-domain-status.json` `target_normalization_audit_2026_09_22.total_edges` from stale **860** to authoritative **859**.
- [x] Preserved dated historical 862/860/840 snapshots and the older COVERAGE-AUDIT historical prose; those are evidence/history, not current producer state.
- [x] Verified the live source-of-truth relationship projection remains **859 total = 244 skill + 151 Super Soul + 124 equipment + 247 character + 86 DLC + 7 farming**.
- [ ] CI/status checks remain unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live strict-thin Super Soul census and select the strongest evidence-supported cluster, while keeping **032/034/158/217** explicit evidence boundaries unless item-level evidence resolves them.

### 2026-09-23 cycle update — current PQ relationship producer-field drift repair
- [x] Audited the remaining current-looking PQ relationship producer/status fields after the prior non-PQ consumer pass.
- [x] Corrected `docs/data/pq-reward-relationships.json` `current_reconciliation_2026_09_22` from stale **854 / 146 Super Soul** to live **859 / 151 Super Soul**; current domain counts are **244 / 151 / 124 / 247 / 86 / 7**.
- [x] Corrected `docs/data/pq-cross-domain-status.json` `target_normalization_audit_2026_09_22.total_edges` from stale **860** to authoritative **859**.
- [x] Preserved dated historical 862/860/840 snapshots and older historical COVERAGE-AUDIT prose.
- [x] Verified the live source-of-truth relationship projection remains **859 total = 244 skill + 151 Super Soul + 124 equipment + 247 character + 86 DLC + 7 farming**.
- [ ] CI/status checks remain unavailable; no CI success claimed.
- [ ] Exact next batch: recompute the live strict-thin Super Soul census and select the strongest evidence-supported cluster, while keeping **032/034/158/217** explicit evidence boundaries unless item-level evidence resolves them.


### 2026-09-23 cycle update — strict-thin queue recomputation and checkpoint consistency repair
- [x] Recomputed the authoritative live strict-thin census from `docs/data/super-souls-record-layer.json` under the repository's eight-field strict-thin definition: **229 canonical / 0 duplicate IDs / 4 strict-thin records**.
- [x] Confirmed the live queue is exactly **super-soul-032, super-soul-034, super-soul-158, super-soul-217**; the earlier raw-null scan and its 228-record claim are superseded and are not the strict-thin census.
- [x] Audited the four remaining evidence boundaries: 032 lacks item-level mechanics for its KO/name-state; 034 lacks independently established character source/mechanics/Limit Burst; 158 remains blocked by the same-name Super Skill collision; 217 still lacks exact-name Limit Burst evidence.
- [x] Repaired `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json` by removing its contradictory duplicate 034 entry and preserving the unresolved canonical character source.
- [x] Preserved historical handoff/TODO entries; no history was deleted or rewritten.
- [x] Canonical Super Soul data was not expanded with unsupported mechanics.
- [x] Validation: checkpoint JSON parses; live canonical count **229**; duplicate IDs **0**; strict-thin queue **4** and matches the authoritative stored census.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- Commits: checkpoint `6008ed985614a467f7eebda8b27f4bfeeb98d547`; changelog `a53f6614f22647728e08f7e317b1adc8ee82699e`; handoff/TODO pending.
- [ ] Exact next batch: perform one final compact item-level/game-data evidence pass for **super-soul-034**, then, if still blocked, move to **super-soul-217 Limit Burst**. If neither yields authoritative evidence, stop forcing the thin queue and select the next deterministic high-impact index/producer reconciliation.


### 2026-09-23 cycle update — Super Soul 034 item-level evidence boundary finalized
- [x] Performed the requested final compact repository evidence pass for **super-soul-034 — “The final battle begins now.”**
- [x] Cross-checked the Future Saga Chapter 4 item-evidence reconciliation, Super Soul effect-evidence file, and 034 provenance audit.
- [x] Confirmed all three repository evidence layers preserve **effect, trigger, item identifier, and Limit Burst as unresolved**; the surrounding PQ186 Fu costume inventory does not constitute item-level attribution to this Super Soul.
- [x] Preserved canonical `character_source` as **unresolved**; no Fu attribution or mechanics were promoted.
- [x] Updated `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json` with the final evidence boundary and repository sources.
- [x] Validation: checkpoint JSON parses; strict-thin queue remains **032, 034, 158, 217**; canonical Super Soul count remains **229**, duplicate IDs **0**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- Commit: checkpoint `b4c7dd2193f74cc3c601f1a17a94ef6c37eee238`.
- [ ] Exact next batch: **super-soul-217 Limit Burst** item-level/game-data evidence pass. If still blocked, leave 217 unresolved and move to the next deterministic high-impact reconciliation.


### 2026-09-23 cycle update — Super Soul 217 Limit Burst boundary finalized
- [x] Performed the final compact item-level/game-data pass for **super-soul-217 — “Power! A lotta power! It's great!”**.
- [x] Cross-checked canonical Super Soul/index data, PQ134 reward records, PQ reward normalization, PQ research batch data, and the live thin census.
- [x] Confirmed PQ134 establishes the exact-name Super Soul reward, but no checked item-level/canonical layer establishes 217's Limit Burst type, trigger, or effect.
- [x] Explicitly rejected **Burst Charge** as evidence for the Super Soul Limit Burst because it is a separate PQ134 skill reward.
- [x] Updated `docs/data/super-soul-217-limit-burst-evidence-audit-2026-09-23.json`; no unsupported mechanics were promoted.
- [x] Live authoritative census remains **229 canonical / 0 duplicate IDs / 4 strict-thin**: **032, 034, 158, 217**.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- Commit: `a2b603c96a6e53315b4887e8f3510bd41473ce29`.
- [ ] Exact next batch: stop forcing the current thin queue unless new item-level evidence appears; select the next deterministic high-impact reconciliation from the live repository, prioritizing producer/index/projection drift or a multi-record evidence-supported batch.


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
- [x] Authoritative live relationship array is **854 total / 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**, with **143** unique Super Soul reverse targets.
- [x] Propagated the verified baseline into current PQ status/audit/producer/presentation/reference validators; historical 859/151 snapshots are retained as history.
- [x] Updated the current consumer-baseline correction artifact to distinguish the superseded projection from current source-of-truth state.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Next: scan remaining current-looking artifacts for stale 859/151 fields.


### 2026-09-23 cycle update — Verified 854/146 PQ consumer baseline propagation
- Live canonical relationship census: **854 total / 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**; canonical PQ→Super Soul projection is **146 forward / 143 reverse targets**.
- Bounded batch: deterministic current consumer/projection repair after the resolved 151/146 Super Soul discrepancy.
- Changed: `docs/data/pq-relationship-producer-census.json`, `docs/data/pq-cross-domain-status.json`, `scripts/validate_pq_non_pq_consumer_census.py`, `docs/data/pq-non-pq-consumer-census-2026-09-22.json`, and `docs/data/super-soul-thin-census-2026-09-23.json`; added `docs/data/pq-current-super-soul-baseline-repair-2026-09-23.json`.
- Evidence boundary: canonical `docs/data/pq-reward-relationships.json` is authoritative at 854/146; the Super Soul crosslink report independently parses to 146 forward / 143 reverse. No relationship edge was added, deleted, renamed, or inferred in this cycle.
- Validation: canonical JSON parses; producer/status projections match 854/146/143; PQ page consumer audit already reports 146/146 exact Super Soul pair parity; thin census synchronized to 146/143; non-PQ census synchronized to the verified baseline. Static direct-fetch validation only; runtime/CI remains unavailable and no CI success is claimed.
- Commits: `f374bf608e0d709eddd8b67ab8bd608a05e540ea`, `ccf79baf940c255a934bd5c41555ff6218077db2`, `59e32ae6b9bcfa22878b692b48c441d61bcd241e`, `4617d71bd84aa47beaf077722521eec07356663b`, `f7cacc4f400e191d8614fabcefdc810641ecdd16`, `a1d61d969c90da0826709ac0278ece4351e82c53`.
- Exact next batch: scan the remaining **current-looking** 859/151 consumer artifacts, beginning with endpoint/navigation validators and standalone/unified reverse-index projections; patch only deterministic current/live fields and preserve all dated historical snapshots.


### 2026-09-23 cycle update — PQ current navigation/reverse-index propagation
- Revalidated authoritative docs/data/pq-reward-relationships.json: 854 total / 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming; Super Soul reverse target count 143.
- Completed the next deterministic consumer batch. Current/live fields were synchronized in pq-endpoint-navigation-audit.json, pq-endpoint-identity-resolution-audit.json, pq-cross-database-reverse-consistency-audit-2026-09-22.json, pq-endpoint-alias-granularity-map.json, super-soul-thin-census-2026-09-22.json, and pq-current-baseline-single-source-reconciliation-2026-09-22.json.
- The authoritative relationship layer current reconciliation metadata was also synchronized to 854/146; historical 859/151/860/862/840 snapshots were preserved rather than rewritten.
- Static JSON structure and direct repository reads were used for validation; runtime/CI remains unavailable, so no CI success is claimed.
- Exact next batch: scan remaining generated/current-facing PQ presentation and reverse-index artifacts for explicitly current/live stale 859/151 values, then continue deterministic cross-database navigation parity work.


### 2026-09-23 cycle update — Remaining current PQ presentation/validator drift repair
- Revalidated the authoritative PQ relationship array at 854 total / 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming.
- Repaired additional explicitly current-facing consumers: `pq-summary-consumer-audit-2026-09-22.json`, `pq-reference-page-audit.json`, `pq-unified-reverse-index-audit.json`, `pq-cross-domain-index.md`, `pq-coverage-audit-current-consumer-drift-2026-09-22.json`, `skill-pq-acquisition-presentation-audit.json`, and `Parallel-Quest-Audit.md`.
- Updated `scripts/validate_pq_current_consumer_baseline.py` to validate against the authoritative current-baseline reconciliation instead of the superseded historical 859/151 correction artifact, and changed its producer total expectation to 854.
- Historical 859/151 and older snapshots were not rewritten when they are explicitly dated historical records. No relationship edge was inferred or removed in this cycle.
- Static structural validation/direct repository reads only; runtime/CI remains unavailable and no executable success is claimed.
- Exact next batch: inspect the remaining current-facing PQ page templates and DLC requirement presentation for one-way navigation, stale scalar fields, and endpoint identity drift; then repair deterministic cross-database navigation gaps before returning to unresolved mechanics/provenance.


### 2026-09-23 cycle update — PQ explorer deep-link/DLC navigation repair
- Live canonical relationship census remains **854 total / 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming**.
- Fixed a concrete navigation defect in `docs/Parallel-Quests-All.html`: inbound `?q=` links now initialize the PQ explorer search field correctly, and PQ→DLC links now target the query-aware `/Search/` surface instead of appending an unsupported query to the static DLC overview.
- Updated `scripts/validate_pq_explorer_reward_navigation.py` with explicit deep-link and PQ→DLC destination checks.
- Updated `docs/data/pq-explorer-reward-navigation-audit.json` and `docs/data/pq-direct-template-dlc-consumer-audit-2026-09-22.json` to record the repair and 854-edge current baseline.
- Direct fetch/static inspection confirmed the validator contains the new checks and the explorer initializes its query after DOM element declaration. Runtime/CI remains unavailable; no executable success claimed.
- Exact next batch: inspect character and Super Soul reverse-navigation destinations for the same query/deep-link contract, then repair deterministic navigation gaps only.


### 2026-09-23 cycle update — Dedicated Character/Super Soul reverse-navigation parity
- Repaired `docs/Parallel-Quests-All.html` so explicit PQ→Character links target `/Characters-All/?q=` and PQ→Super Soul links target `/Super-Souls-All/?q=`. Both destinations already consume query deep links, giving relationship endpoints a dedicated searchable destination.
- Extended `scripts/validate_pq_explorer_reward_navigation.py` with explicit checks for both dedicated destinations.
- Updated `docs/data/pq-explorer-reward-navigation-audit.json` to record the navigation parity repair. No relationship edge was changed.
- Static/direct repository inspection only; runtime/CI remains unavailable and no executable success is claimed.
- Exact next batch: inspect remaining Equipment/DLC reverse-navigation presentation and any generated content pages for one-way destinations, then continue deterministic cross-database navigation parity.


### 2026-09-23 cycle update — Equipment/DLC reverse-navigation presentation repair
- Audited the published Equipment explorer and DLC Overview against canonical relationship/identity layers.
- Added Equipment → local DLC search navigation for populated DLC provenance values and DLC Overview → PQ explorer reverse navigation for canonical DLC identities.
- Added/registered `docs/data/equipment-dlc-reverse-navigation-presentation-audit-2026-09-23.json`.
- No canonical relationship, identity, acquisition, or gameplay field was invented or modified.
- CI/runtime remains unavailable; do not claim CI success.
- Exact next task: inspect remaining published character/DLC presentation indexes and generated-content navigation for deterministic one-way/orphan destinations; then continue exhaustive DLC content-domain reconciliation.

### 2026-09-23 cycle update — Super Soul 036–047 secondary-field reconciliation
- Recomputed the live Super Soul census: **229 canonical records / 24 records with at least one currently unresolved core field** under the current ten-field audit definition.
- Bounded batch: **036–047**.
- Filled previously absent DLC requirement fields with **None identified** where no paid DLC requirement is established; this does not promote free-update association into a paid-DLC requirement.
- Reconciled stacking behavior to **Not reported as stackable** across 036–047 where maintained exact-name evidence reports no stacking mechanic or numeric cap.
- Added Free Update evidence and refreshed verification dates to 2026-09-23.
- Added/registered audit: `docs/data/super-soul-036-through-047-secondary-field-reconciliation-2026-09-23.json`.
- Evidence boundaries preserved: no hidden stack cap, paid-DLC ownership, new acquisition route, or gameplay mechanic was inferred.
- CI/runtime: no successful workflow/check exposed; no CI success claimed.
- Exact next priority: recompute the remaining **24-record thin-system queue** and target the highest-impact unresolved fields, with **032, 034, 158, and 217** receiving priority because their unresolved fields are substantially broader than the DLC/stacking-only tail.

### 2026-09-23 cycle update — DLC → character identity navigation repair
- Audited the remaining published character/DLC presentation surface after the Equipment/DLC reverse-navigation pass.
- Added **DLC → Character Identity Navigation** to `docs/DLC-Overview.md`, driven exclusively by `docs/data/characters/dlc-character-identity-bridge.json`.
- All **15** maintained DLC headline-character provenance labels are represented: **13 resolved** labels link into the local character Search surface; **2 unresolved** Chapter 4 variants remain explicitly unresolved rather than being collapsed into nearby canonical identities.
- Extended `scripts/validate_published_character_dlc_navigation.py` to require the new DLC Overview character-navigation section.
- Updated `docs/data/characters/published-character-dlc-navigation-audit.json` with the new consumer census.
- No DLC ownership or character relationship edge was created; this is presentation navigation only.
- Static/direct repository validation only; runtime/CI remains unavailable and no CI success is claimed.
- Exact next task: continue deterministic DLC content-domain reconciliation, prioritizing pack-level content matrices and missing downstream record links without collapsing unresolved identities.


### 2026-09-23 cycle update — DLC reverse-index validator schema repair
- Audited the live `scripts/validate_dlc_presentation_consumers.py` against the actual `docs/data/dlc/pq-reverse-index.json` schema.
- Found and repaired a deterministic validator defect: the completeness check incorrectly read a nonexistent `reverse_index` map instead of the live `records[].dlc_id` projection.
- Added explicit reporting for the number of canonical DLC targets with reverse navigation and any canonical targets lacking it.
- Updated `docs/data/dlc/dlc-presentation-consumer-audit.json` to record the schema repair and the current **20/20** canonical-DLC reverse-navigation coverage.
- No canonical DLC identity or PQ relationship was changed.
- Static/direct repository inspection only; runtime/CI remains unavailable and no CI success is claimed.
- Exact next task: continue DLC content-domain reconciliation at the record level, beginning with the existing DAIMA and HERO OF JUSTICE Pack 2 projections; missing non-PQ domain coverage must remain explicit rather than inferred.


### 2026-09-23 cycle update — DLC pack record-link integrity repair
- Audited concrete downstream equipment records for the maintained DAIMA and HERO OF JUSTICE Pack 2 PQ projections.
- Found and corrected 7 malformed canonical PQ source identifiers in docs/data/equipment-record-layer.json: pq-pq-159 through pq-pq-162 and pq-pq-179 through pq-pq-181.
- Corrected them deterministically to pq-159–pq-162 and pq-179–pq-181, matching canonical PQ IDs.
- Updated the DLC content-link audit; no new DLC/content relationship was inferred.
- Remaining non-PQ inventory gaps remain explicitly unresolved.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: continue record-level DLC reconciliation across declared non-PQ domains using only existing canonical evidence.


### 2026-09-23 cycle update — DLC pack content matrix / concrete downstream anchors
- Live baseline: **20 canonical DLC identities / 86 canonical PQ→DLC edges**; broader content projection remains **3 records**.
- Bounded batch: **Dragon Ball DAIMA Pack** and **HERO OF JUSTICE Pack 2** non-PQ content-domain projections.
- Research/evidence: official Bandai Namco announcements establish the advertised domains; repository canonical character/PQ/equipment/skill/Super Soul layers provide concrete downstream navigation anchors. The DAIMA announcement explicitly separates paid-pack content from its free update.
- Changes: added `docs/data/dlc/dlc-pack-content-matrix-2026-09-23.json`; linked it from the DLC content-link audit and PQ cross-domain index. The matrix records concrete anchors without promoting PQ requirements into inferred complete DLC inventories.
- Evidence limits preserved: DAIMA free-update raid/lobby inventory remains unresolved; HERO OF JUSTICE Pack 2 exact stage and complete non-PQ inventory remain unresolved; no missing content was guessed.
- Validation: live re-fetch confirmed matrix structure and registration; canonical DLC identity remains **20 records / 86 PQ→DLC edges**; no canonical relationship row was modified.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: reconcile the strongest concrete DAIMA/HOJ2 downstream record cohort, prioritizing existing equipment/accessory records and then skill/Super Soul records, while preserving unresolved raid/lobby/stage boundaries.


### 2026-09-23 cycle update — DAIMA downstream accessory normalization readiness
- Concrete DAIMA downstream audit completed: equip-098–equip-105 contain exact source-backed costume/accessory identities for PQ179–181. Official Bandai Namco scope confirms the DAIMA Pack includes costumes/accessories, PQs, skills, Super Souls, and loading-screen illustrations; the free update remains a separate content boundary.
- Four accessory identities are ready for canonical accessory namespace promotion: equip-099 SS4 Goku (DAIMA) Wig & Tail → candidate acc-071; equip-101 SS3 Vegeta (DAIMA) Wig → acc-072; equip-104 Glorio Wig → acc-073; equip-105 Panzy Wig → acc-074.
- Added docs/data/dlc/daima-accessory-normalization-audit-2026-09-23.json, registered it in docs/data/pq-cross-domain-index.json, and extended the DAIMA pack matrix with the concrete combined-layer IDs.
- No canonical relationship endpoint was changed in this cycle; the four records remain in their current combined-layer IDs until the dependent accessory bridge/reverse/presentation projections can be updated atomically.
- Evidence boundary: these are exact-name identity promotions, not newly inferred content. Reward-slot/guaranteed-drop semantics remain unresolved where not independently established.
- Exact next batch: atomically normalize the four DAIMA accessory identities into acc-071–acc-074, preserve the existing equipment IDs as aliases, regenerate/validate accessory reverse navigation and presentation consumers, then continue with the next strongest unresolved pack cohort.


### 2026-09-23 cycle update — DAIMA accessory canonicalization complete
- Canonicalized four exact-name DAIMA accessories: `acc-071` SS4 Goku (DAIMA) Wig & Tail, `acc-072` SS3 Vegeta (DAIMA) Wig, `acc-073` Glorio Wig, `acc-074` Panzy Wig.
- Removed the four duplicate accessory identities from the combined canonical layer while retaining `equip-099`, `equip-101`, `equip-104`, and `equip-105` as legacy equipment-layer aliases linked via `canonical_accessory_id`.
- Resolved bridge records `pqacc-034`–`pqacc-037`, marked their residual records matched, and regenerated the accessory PQ crosslink projection: **32 forward / 32 reverse accessory edges**, **74 canonical accessories**, **12 unresolved research bridge records**.
- Updated the accessory producer census, canonicalization audit, DAIMA DLC matrix, TODO, and handoff. No reward semantics were invented or changed.
- Validation by live re-fetch confirmed the four canonical IDs, alias mappings, bridge matches, and projection counts. Runtime validator execution remains the next gate because GitHub's exposed API does not execute repository scripts in this session.
- Exact next batch: execute/verify accessory presentation validators when runtime access is available, then continue the strongest concrete DAIMA/HERO OF JUSTICE Pack 2 skill/Super Soul reconciliation cohort.


### 2026-09-23 cycle update — DAIMA / HERO OF JUSTICE Pack 2 skill and Super Soul anchor reconciliation
- Audited canonical PQ skill and Super Soul projections for PQ159–162 and PQ179–181.
- Found **13 exact canonical skill edges** and **7 canonical-backed Super Soul edges** across the two pack cohorts.
- Added `docs/data/dlc/daima-hoj2-skill-super-soul-downstream-audit-2026-09-23.json`, registered it in the PQ cross-domain index, and expanded the DLC pack matrix with individual skill/Super Soul IDs.
- HOJ2 concrete skill anchors: `skill-fierce-fist`, `skill-demonic-destruction`, `skill-demon-ray`, `skill-demon-flash-strike`, `skill-demon-flurry`, `skill-apocalyptic-burst`, `skill-special-beam-cannon-beast`; Super Souls `super-soul-120`, `121`, `061`, `118`, `119`.
- DAIMA concrete skill anchors: `skill-heat-wave`, `skill-supreme-fury`, `skill-force-edge`, `skill-burning-blast`, `skill-super-kamehameha-ss4-daima`, `skill-final-flash-ss3-daima`; Super Souls `super-soul-145`, `super-soul-062`.
- No DLC ownership edge or reward semantics were inferred. DAIMA free-update content remains separate.
- Live GitHub re-fetch/structural validation completed. Runtime/CI execution remains unavailable; no CI success claimed.
- Exact next batch: reconcile remaining non-PQ skill/Super Soul inventory against canonical records and official advertised pack scope, without converting unresolved completeness into inferred ownership.


### 2026-09-23 cycle update — official DAIMA / HOJ2 skill and Super Soul count reconciliation complete
- Official publisher/Nintendo product counts reconcile exactly with the canonical repository inventory: DAIMA = 6 moves + 2 Super Souls; HOJ2 = 7 moves + 5 Super Souls.
- DAIMA canonical skills: Heat Wave, Supreme Fury, Force Edge, Burning Blast, Super Kamehameha (SS4 DAIMA), Final Flash (SS3 DAIMA). DAIMA Super Souls: `super-soul-145` Here I go! and `super-soul-062` Damn it all!.
- HOJ2 canonical skills: Fierce Fist, Demonic Destruction, Demon Ray, Demon Flash Strike, Demon Flurry, Apocalyptic Burst, Special Beam Cannon (Beast). HOJ2 Super Souls: `super-soul-120`, `121`, `061`, `118`, `119`.
- Added and registered `docs/data/dlc/daima-hoj2-official-skill-super-soul-count-reconciliation-2026-09-23.json`; updated the DLC content matrix.
- This closes the skill/Super Soul completeness check for these two paid packs. Official counts were treated as domain-level completeness checks only; no ownership was inferred from PQ requirements and DAIMA free-update content remains separate.
- Exact next batch: reconcile remaining paid-DLC domains, starting with HOJ2's 5 costumes/accessories and stage/missions, then remaining DAIMA paid inventory, with canonical cross-navigation preserved.


### 2026-09-23 cycle update — HERO OF JUSTICE Pack 2 paid content reconciliation
- Completed a bounded paid-DLC content-domain reconciliation for HERO OF JUSTICE Pack 2.
- Official publisher/store sources establish 3 characters / 2 Extra Missions / 1 stage / 4 PQs / 7 moves / 5 costumes-accessories / 5 Super Souls / 15 illustrations.
- Reconciled five paid costume/accessory slots to exact canonical records: acc-069 Dr. Hedo Hood (PQ159), acc-060 Red Ribbon Army Helmet (PQ160), equip-067 Red Ribbon Soldier 94 Clothes (PQ161), equip-068 Dr. Hedo Suit (PQ162), and acc-061 Gohan (Beast) Wig (PQ162).
- Reconciled the stage identity as Red Ribbon Army (Yard) at pack scope; no synthetic stage record was created because the repository has no dedicated stage record layer.
- Reconciled the two Extra Missions at pack-count level; no synthetic mission IDs were created because no dedicated extra-mission record layer is present.
- Preserved the free-update boundary: Cell Max raid costume/accessory rewards are not promoted into the paid five-item Pack 2 inventory.
- Added/registered docs/data/dlc/hero-of-justice-pack-2-paid-content-reconciliation-2026-09-23.json; updated the DLC pack content matrix and DLC content-link audit.
- Skill/Super Soul count reconciliation remains 7/7 and 5/5 respectively.
- Validation by live record inspection: all five exact equipment/accessory IDs resolve in the canonical equipment/accessory layer; all four PQs and five paid equipment/accessory endpoints are source-backed; no canonical relationship rows were invented.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next priority: DAIMA paid non-skill/Super-Soul inventory reconciliation, beginning with the concrete costume/accessory cohort and official pack-level scope; preserve the paid/free-update boundary and do not invent unresolved raid/lobby/stage records.


### 2026-09-23 correction — HERO OF JUSTICE Pack 2 matrix stale-domain cleanup
- Corrected the live DLC pack matrix after validation: `exact_stage_identity` is no longer listed as unresolved because the stage identity **Red Ribbon Army (Yard)** was reconciled at pack scope.
- Remaining unresolved Pack 2 domains are limited to complete pack inventory, mission record layer, stage record layer, and extra-mission record layer; no synthetic stage/mission records were introduced.


### 2026-09-23 cycle update — DAIMA paid costume/accessory completeness reconciliation
- Reconciled the official DAIMA Pack **8 Costumes/Accessories** count using exact canonical downstream identities: 4 costumes (`equip-098`, `equip-100`, `equip-102`, `equip-103`) and 4 canonical accessories (`acc-071`–`acc-074`, retaining `equip-099`, `equip-101`, `equip-104`, `equip-105` as aliases).
- The eight identities map to PQ179–181: SS4 Goku (DAIMA) Suit / Wig & Tail, SS3 Vegeta (DAIMA) Battle Suit / Wig, Glorio's Clothes / Wig, and Panzy's Clothes / Wig.
- Added `docs/data/dlc/daima-paid-costume-accessory-completeness-reconciliation-2026-09-23.json`, registered it in `docs/data/pq-cross-domain-index.json`, and updated the DAIMA DLC pack matrix.
- Official platform listings independently confirm the paid pack contains **8 Costumes/Accessories**. 
- Removed the resolved paid costume/accessory gap from the DAIMA matrix. Remaining unresolved DAIMA domains are free-update inventory, raid/lobby record layers, and complete loading-screen inventory; reward-slot/guaranteed-drop semantics remain unresolved where not established by the canonical PQ relationship layer.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next priority: continue remaining DAIMA paid domains only where concrete canonical records and official scope permit; prioritize loading-screen completeness if a canonical illustration layer can be reconciled, otherwise continue the next unresolved paid domain without crossing into free-update ownership.


### 2026-09-23 cycle update — DAIMA paid illustration scope reconciliation
- Reconciled the official **8 paid DAIMA illustrations/loading screens** using Bandai Namco and platform store listings.
- Live-tree inspection found no dedicated canonical illustration/loading-screen record layer under `docs/data`; therefore no synthetic illustration IDs, names, acquisition routes, or PQ reward slots were invented.
- Preserved the ownership boundary: Bandai Namco separately identifies free-update loading screens and lobby items, so those remain outside the paid eight.
- Added `docs/data/dlc/daima-paid-illustration-scope-reconciliation-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- Exact next priority: establish a canonical illustration/loading-screen record layer only when the individual eight paid identities can be source-backed, then cross-link them to the DAIMA pack and acquisition relationships. If that evidence remains insufficient, move to the next concrete paid domain rather than inventing records.
- CI/runtime remains unavailable; no CI success claimed.


### 2026-09-23 cycle update — accessory/presentation validation after DAIMA canonicalization
- Live structural validation completed against the canonical accessory layer and PQ accessory presentation report.
- Current state: 173 equipment records, 74 canonical accessories, 32 PQ accessory forward/reverse edges, 12 unresolved research records; zero duplicate accessory IDs/names, zero duplicate forward edges, zero stale endpoints, and zero null PQ edges.
- DAIMA accessory endpoints `acc-071`–`acc-074` resolve to PQ179–181 and remain cross-navigable through the canonical accessory/PQ graph.
- Added `docs/data/accessory-presentation-validation-2026-09-23.json` and refreshed `docs/data/accessory-canonicalization-audit.json` with the live validation summary.
- This validates identity/presentation integrity only; exact reward-slot probabilities and guaranteed-drop semantics remain unresolved where not established by source-backed relationships.
- Exact next priority: reconcile the next unresolved concrete DAIMA/HOJ2 paid content domain, preserving the paid/free boundary and canonical cross-navigation. CI/runtime remains unavailable.


### 2026-09-23 cycle update — HERO OF JUSTICE Pack 2 stage/Extra Mission evidence
- Reconciled Pack 2's official 1-stage/2-Extra-Mission scope against the current Bandai Namco DLC listing.
- Stage identity remains **Red Ribbon Army (Yard)** at pack scope; no synthetic stage record was created because the repository has no dedicated stage layer.
- Source-backed maintained documentation identifies **Extra Mission 14 — The Activation of Cell Max**. It is recorded as evidence only because no dedicated Extra Mission record layer exists; no synthetic mission ID was created.
- Added `docs/data/dlc/hero-of-justice-pack-2-stage-mission-evidence-2026-09-23.json` and linked it from the DLC pack matrix.
- Exact next priority: continue the remaining concrete paid-DLC inventory gap, with illustration/loading-screen identities as the next evidence-led domain where individual records can be source-backed. Preserve the paid/free boundary and avoid synthetic record creation until canonical layers exist. CI/runtime remains unavailable.



### 2026-09-23 cycle update — DAIMA / HERO OF JUSTICE Pack 2 playable-character count reconciliation
- Reconciled official paid-DLC playable-character counts against the live canonical character layer: **DAIMA 2/2** and **HERO OF JUSTICE Pack 2 3/3**.
- Exact canonical identities confirmed: DAIMA — SS4 Goku (DAIMA), SS3 Vegeta (DAIMA); HOJ2 — Gohan (Beast), Orange Piccolo, Piccolo (Power Awakening).
- Added `docs/data/dlc/daima-hoj2-playable-character-count-reconciliation-2026-09-23.json` and registered the reconciliation in `docs/data/dlc/dlc-pack-content-matrix-2026-09-23.json`.
- Evidence: official Bandai Namco DAIMA announcement and current DLC overview; existing canonical character layer.
- Evidence limits preserved: this is a count/identity reconciliation only; no additional DLC ownership, variant identity, or PQ reward relationship was inferred.
- Validation: canonical character layer contains all five expected identities; audit records `2/2` and `3/3` with zero missing names; matrix updated consistently.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: choose the next concrete paid-DLC completeness gap with an existing canonical record layer and cross-domain navigation value; do not create illustration/loading-screen identities until individual identities are source-backed.



### 2026-09-23 cycle update — HERO OF JUSTICE Pack 2 paid illustration scope
- Reconciled the official **15 paid illustrations** count using Steam, Nintendo, and Bandai Namco's Xenoverse 2 DLC listing.
- Added `docs/data/dlc/hero-of-justice-pack-2-paid-illustration-scope-reconciliation-2026-09-23.json`, registered it in the PQ cross-domain index, and updated the DLC pack/content-link matrices.
- Live-tree inspection again found no dedicated canonical illustration/loading-screen record layer, so no synthetic identities were created.
- Validation: audit parses; official count is recorded as 15; paid/free boundary preserved; no canonical PQ reward relationships changed.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: choose the next concrete paid-DLC completeness gap with an existing canonical record layer and cross-domain navigation value; defer individual illustration records until source-backed identities and a canonical layer exist.


### 2026-09-23 cycle update — Time Patrol Support Pack paid-content reconciliation
- Reconciled the separately sold Time Patrol Support Pack against Steam, Nintendo, and Xbox storefront descriptions: 10 Super Attacks, 3 Ultimate Attacks, 8 costumes, 2 accessories, 3 Super Souls, 1 CC Mascot, and the listed consumable quantities.
- Added docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json and registered it in the PQ cross-domain index.
- Deterministic existing-record matches include equip-024 Battle Suit (Bardock), equip-087 Frieza's Suit (Final Form), acc-038 Frieza's Head (Final Form), acc-039 Korin Wig with Ears & Tail, and super-soul-029 The ultimate power is mine!. Six advertised skills also have existing canonical PQ endpoints.
- Architectural boundary preserved: this value pack was not inserted into canonical-dlc-identity.json because that layer represents existing pq_requires_dlc endpoints.
- Unresolved canonical gaps remain explicit: two Super Souls, six costume names, several skill endpoints, Puar/CC Mascot, and consumable identity records. No unsupported IDs were created.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: resolve the remaining Time Patrol Support Pack canonical identity gaps only with record-level evidence, starting with the two unresolved Super Souls and unmatched costume records; then return to DAIMA/HOJ2 unresolved paid domains.


### 2026-09-23 cycle update — Time Patrol Support Pack Super Soul identity promotion
- Promoted the two previously unresolved pack Super Souls into the canonical layer: `super-soul-247` I hope you're reborn as someone good this time. and `super-soul-248` You must die by my hand!.
- Source-backed mechanics and ordinary in-game acquisition routes were recorded; official pack inclusion is treated as provenance, not exclusive ownership.
- Added and registered `docs/data/dlc/time-patrol-support-pack-super-soul-identity-reconciliation-2026-09-23.json`.
- All 3 officially advertised Time Patrol Support Pack Super Souls are now represented canonically.
- Remaining support-pack gaps: six costume names, several advertised skill endpoints, and Puar/CC Mascot. No unsupported IDs were inferred.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next batch: reconcile the six unmatched costume names against canonical equipment aliases/source records, then resolve remaining skill and Puar gaps only where dedicated canonical layers/evidence exist.


### 2026-09-23 cycle update — Time Patrol Support Pack costume identity audit
- Live inspection followed the current DLC priority from the TODO/handoff: six previously unmatched costume names in the separately sold Time Patrol Support Pack.
- Bounded batch: Vegito Clothes, Gogeta Clothes, Future Trunks' Clothes (Super), Broly Clothes, Master Korin's Suit, and Orange Star High School Outfit.
- Evidence: current official Steam/Nintendo/Xbox storefront descriptions establish the eight-costume pack scope; repository PQ/equipment evidence independently establishes Vegito Clothes at PQ59, Gogeta Clothes at PQ57, and Broly Clothes at PQ47; equipment-catalog-index.json independently catalogs Future Trunks's Clothes (Super).
- Changes: added and registered docs/data/dlc/time-patrol-support-pack-costume-identity-reconciliation-2026-09-23.json; refined docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json to record the resolved/non-resolved costume state; updated docs/TODO-EXHAUSTIVE.md with the durable completion entry.
- Exact identity result: Vegito Clothes resolves to equip-078. The other five remain without exact canonical equipment records; distinct outfits were not aliased together. The live legacy equipment layer ends at equip-140, so no equip-141+ IDs were invented.
- Evidence limits preserved: storefront inclusion is not treated as exclusive ownership; no reward probability, drop slot, shop rotation, stats, restrictions, or exclusive-DLC ownership was inferred.
- Validation: new audit JSON parses; official costume count 8; six-target batch has 1 exact canonical match and 5 remaining without exact canonical records; cross-domain registration confirmed. CI/runtime remains unavailable; no CI success claimed.
- Commits: 8ff5b16091c26d061abbce7c36452627fa2ecc1a (new costume audit), 62c7722a6dd84fde357b538fbdc7adb057a27158 (cross-domain registration), 92d23e8a778a0cfeb8df52052dca79d9791b7cf7 (pack reconciliation), 021055320e42f0c6c37c96b85fe5c37b099f906f (TODO update).
- Exact next batch: resolve the five remaining Time Patrol Support Pack costume identities only when individually source-backed and compatible with the existing equipment architecture; then reconcile unmatched pack skills/Puar without inventing IDs, before returning to the remaining DAIMA/HOJ2 paid-content gaps.


### 2026-09-23 correction — TODO history preservation after costume audit
- [x] Restored docs/TODO-EXHAUSTIVE.md from its pre-cycle live history after an intermediate write-path mistake, preserving the complete append-only history, then appended the Time Patrol Support Pack costume audit as the durable final TODO state.
- [x] Final TODO commit: d091356d24112c9b9b4bc48f30f8288234cc77b4; final TODO blob restored to the historical base plus the new audit entry.
- [x] The earlier temporary execution-note mutation is not part of the final TODO content; Git history still records the intermediate commits for traceability.


### 2026-09-23 cycle update — Time Patrol Support Pack skill identity reconciliation
- Live census: canonical skill layer **452 records**; the advertised Support Pack attack list contains **13 attacks**.
- Bounded batch: all 10 Super Attacks and 3 Ultimate Attacks advertised by the official Time Patrol Support Pack storefronts.
- Exact canonical skill matches: **10/13** — skill-super-god-fist, skill-wild-hunt, skill-kaioken-kamehameha, skill-death-psycho-bomb, skill-justice-pose, skill-maximum-charge, skill-punisher-guard, skill-warp-kamehameha, skill-impulse-slash, skill-giant-storm.
- Missing exact canonical identities: **Super Destructo-Disc**, **Big Bang Attack**, and **Power Pole Combo**. Existing research is sufficient to treat Super Destructo-Disc and Big Bang Attack as promotion candidates, while Power Pole Combo remains an identity research gap; Power Pole and Power Pole Pro are explicitly distinct and were not used as aliases.
- Changes: added docs/data/dlc/time-patrol-support-pack-skill-identity-reconciliation-2026-09-23.json; registered it in docs/data/pq-cross-domain-index.json; refined docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json; appended docs/TODO-EXHAUSTIVE.md.
- Official pack evidence: Steam/Nintendo/Xbox list the exact 10 Super Attacks and 3 Ultimate Attacks and identify the pack as a value pack; the storefront wording also says some content can be obtained through the in-game shop or conditions, so pack inclusion is not treated as exclusive ownership.
- Evidence limits preserved: no skill ID was invented; no unsupported reward probability or Ultimate Finish gate was added; promotion of the two source-backed candidates is intentionally deferred until canonical/index files can be updated atomically and parity-validated.
- Validation: new audit JSON parses; exact canonical skill identity count 10/13; cross-domain audit registration confirmed; CI/runtime remains unavailable.
- Exact next batch: atomically promote **Super Destructo-Disc** and **Big Bang Attack** into the canonical/index skill layers using their existing research evidence, then validate ID-set parity and downstream projections; separately research **Power Pole Combo**. After that, continue the five remaining Support Pack costume identities and Puar.

### 2026-09-23 cycle update — Time Patrol Support Pack canonical skill promotions
- Promoted **Big Bang Attack** as `skill-big-bang-attack` and **Super Destructo-Disc** as `skill-super-destructo-disc` into both canonical skill layers.
- Big Bang Attack evidence: 100-Ki Ki Blast Super, Vegeta association, TP Medal Shop acquisition; existing research documents the charge/contact behavior. No unsupported shop rotation or probability was added.
- Super Destructo-Disc evidence: 200-Ki Ki Blast Super, Expert Mission 4 acquisition, CaC usability, fast-tracking/unblockable identity. Exact drop rate and guaranteed-clear semantics remain unresolved.
- Canonical/index count advanced from **452 to 454** and was parity-checked after promotion. The legacy 2026-09-20 status-count snapshot in the skill audit is explicitly preserved separately from the current census.
- Updated promotion manifest, research batch 251, skill audit, Support Pack skill identity audit, Support Pack reconciliation, and exhaustive TODO.
- Current Support Pack skill state: **12/13 exact canonical identities; Power Pole Combo remains the only missing exact skill identity.**
- Validation: modified JSON files parse; promoted IDs are unique; canonical and index record counts both equal 454. CI/runtime remains unavailable.
- Exact next task: research **Power Pole Combo** as a distinct identity without aliasing it to Power Pole or Power Pole Pro; then continue the five remaining costume identities and Puar.

### 2026-09-23 final parity correction — Support Pack skill promotion cycle
- [x] Final canonical/index validation after the promotion sequence: `docs/data/skills.json` = **454 records**, `docs/data/skills-index.json` = **454 records**; both have 454 unique IDs; ID sets and name sets are exactly equal.
- [x] Confirmed both promoted identities exist in both layers: `skill-big-bang-attack` and `skill-super-destructo-disc`.
- [x] The intermediate one-sided promotion state was repaired by adding the missing counterpart to each layer; the final live repository state is synchronized and validated.
- [x] Final parity repair commits: `eaa78bca0d308d7b563eab75d57ae641410424fb` and `f09c28c9f30cfc59e4eb4ea5c75e6f0288e94c3f`.
- [x] No CI success claimed; validation was performed directly against the live canonical and index JSON structures.
- [ ] Next exact task remains **Power Pole Combo** identity research, followed by the five remaining Support Pack costume identities and Puar.

### 2026-09-23 cycle update — Time Patrol Support Pack Power Pole Combo identity resolution
- Dedicated web/repository research resolved **Power Pole Combo** as a distinct canonical skill identity: Super / Strike / 100 Ki / CaC-usable / Goku (GT), Skill Shop acquisition. Current Xenoverse 2 references explicitly distinguish it from Power Pole and Power Pole Pro. citeturn1search0turn1search1
- Promoted skill-power-pole-combo into both canonical skill layers and added a dedicated reconciliation audit.
- Registered the audit in docs/data/pq-cross-domain-index.json and updated the Support Pack skill/content reconciliations.
- Support Pack skill coverage is now **13/13 exact canonical identities**. The official storefront confirms Power Pole Combo is one of the advertised Super Attacks. citeturn1search5turn1search4
- Current canonical/index census advanced to **455 records**.
- Exact next task: continue the **five remaining unmatched costume identities**, then reconcile **Puar/CC Mascot**. Preserve the existing equipment architecture and do not invent equip IDs without record-level evidence.


### 2026-09-23 cycle update — Time Patrol Support Pack remaining costume evidence follow-up
- Bounded batch: **Gogeta Clothes, Future Trunks' Clothes (Super), Broly Clothes, Master Korin's Suit, and Orange Star High School Outfit**.
- Research: official Steam/Nintendo storefronts establish all five as exact Support Pack costume identities. Independent current/repository evidence distinguishes Gogeta's Clothes from SSGSS Gogeta's Clothes, Future Trunks's Clothes (Super) from Future Trunks's Clothes, Broly's Clothes from Broly (Full Power Super Saiyan)'s Clothes/Battle Suits, Master Korin's Suit from Master Korin's Staff, and Orange Star High School Outfit from the Orange Star High School T-Shirt/custom variant.
- Changes: strengthened `docs/data/dlc/time-patrol-support-pack-costume-identity-reconciliation-2026-09-23.json` with per-identity evidence and explicit canonical actions; no new equipment IDs or aliases were created.
- Evidence boundary preserved: the live legacy equipment layer currently ends at **equip-140**. The five identities are now independently evidence-backed inventory gaps, but there is no exact canonical equipment record for them; inventing equip-141+ would violate the current repository boundary.
- Validation: official Support Pack costume scope remains 8; six-target historical batch remains 1 exact canonical match + 5 exact canonical gaps; zero new canonical IDs and zero identity aliases in this pass.
- Commits: audit **e1ed5ae285f2d6289479915fd0f167c4fb2a8a68**; TODO **bc54c3aa6e64a56a4bd46b4bddf8b5e4387c51c7**.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: resolve the canonical equipment-layer capacity/ID architecture question for these five evidence-backed identities without inventing equip-141+ records; if the layer remains intentionally closed at equip-140, preserve the five as explicit inventory gaps and then proceed to the **Puar/CC Mascot** identity gap.


### 2026-09-23 cycle update — Time Patrol Support Pack Puar / CC Mascot identity
- Live canonical skill census remains **455 records**; equipment architecture remains bounded at legacy **equip-140**.
- Bounded batch: **Puar**, the remaining advertised Time Patrol Support Pack CC Mascot.
- Research: official PlayStation/Nintendo/Steam/Xbox storefronts identify Puar as a Support Pack **CC Mascot**. Independent CC Mascot documentation establishes that Puar belongs to the separate lobby-item mascot domain, distinguishes Puar from its color variants, and documents non-DLC acquisition routes. citeturn0search0turn0search1turn0search2turn0search5
- Changes: added `docs/data/dlc/time-patrol-support-pack-puar-cc-mascot-identity-reconciliation-2026-09-23.json`; registered it in `docs/data/pq-cross-domain-index.json`; updated `docs/data/dlc/time-patrol-support-pack-content-reconciliation-2026-09-23.json`; appended the durable TODO entry.
- Identity boundary: Puar is **not equipment or an accessory**. No `equip-###` or `acc-###` alias was created. The live repository currently has no dedicated canonical CC Mascot record layer, so no mascot ID was invented.
- Validation: new audit parses; cross-domain registration is present; Support Pack content reconciliation records the exact Puar identity and missing canonical-domain layer; no existing canonical skill/equipment/accessory counts were changed.
- CI/runtime: unavailable; no CI success claimed.
- Commits: Puar audit **2445200975c2c0f38cc46e704b9c1d9616642635**; cross-domain registration **7161e738b7dfacea0d42afd3c5ad95ca6a1509ca**; content reconciliation **11c4aaa482b215813c3a7859d61b93d75e1feb86**; TODO **36509ef2f68395ddacbdebbc0e169cbd69a783b2**.
- Exact next batch: introduce the smallest dedicated **CC Mascot canonical/catalog schema and index**, then promote Puar with exact DLC provenance and validate navigation parity. Preserve the five unmatched costume identities as evidence-backed equipment inventory gaps and do not invent `equip-141+` IDs.
\n\n### 2026-09-23 cycle update — Dedicated CC Mascot canonical layer / Puar promotion
- Live relevant census before editing: equipment legacy layer ends at **equip-140**; Support Pack Puar was identity-resolved but lacked a canonical domain.
- Bounded batch: **CC Mascot canonical schema/index + Puar promotion**.
- Changes: added `docs/data/cc-mascots.json` and `docs/data/cc-mascots-index.json`; promoted `mascot-puar`; registered the layer in `docs/data/pq-cross-domain-index.json`; updated the Support Pack reconciliation and Puar audit.
- Identity boundary: Puar remains a CC Mascot/lobby-item identity and is not mapped to equipment/accessory IDs. Variant identities remain separate.
- Validation: JSON parse checks passed; mascot canonical/index counts are both 1; `mascot-puar` is unique; DLC reconciliation points to the canonical ID. CI/runtime unavailable; no CI success claimed.
- Commits: mascot canonical **69c3bdceaad0993931fc36985d158a3c246a59c3**; mascot index **570f7a8d2e988129d2693681785d9b7aa490c167**; cross-domain registration **044086aa99a4c8fa9d483016154939bec451d7d5**; DLC reconciliation **78fde4c5fba4ca00612f1a23540aa1599b4788c8**; Puar audit **dc6f57345bcdc73678c50009debab75e4782c2fb**.
- Exact next batch: validate all CC Mascot consumers/reverse-navigation requirements, then continue the five unmatched Support Pack costume identities without inventing `equip-141+` IDs.\n

### 2026-09-23 cycle update — CC Mascot reverse navigation validation
- Live mascot census: **1 canonical record / 1 reverse-index record**.
- Bounded batch: validate and wire **Puar reverse navigation**.
- Changes: added `docs/data/cc-mascots-reverse-index.json`; registered it in `pq-cross-domain-index.json`; corrected the Support Pack reconciliation's stale unresolved-mascot statement.
- Validation: mascot/reverse ID sets match exactly; unresolved canonical mascot IDs = 0; equipment/accessory aliases = 0. CI/runtime unavailable.
- Commits: reverse index **fa046be8c558be85e7b10b6c7b93d694dc5f4b75**; cross-domain registration **d968326b763c6fe8207a01bcf4be5d24edf93c4a**; reconciliation correction **c80819b7da354fa2b5b3a292f118326fd20cd76a**.
- Exact next batch: resume the five unmatched Support Pack costume identities and resolve equipment-layer capacity/extension safely without inventing unsupported `equip-141+` IDs.


### 2026-09-23 cycle update — Support Pack costume equipment-ID capacity decision
- Live equipment namespace: **equip-140 maximum**; combined canonical equipment/accessory layer remains separate from legacy ID numbering.
- Bounded batch: **Gogeta Clothes, Future Trunks' Clothes (Super), Broly Clothes, Master Korin's Suit, Orange Star High School Outfit**.
- Decision: do **not** assign equip-141+ IDs or force clothing into accessory IDs. The repository lacks a documented next-generation equipment-ID allocation mechanism, while current continuation guidance explicitly prohibits invented equip-141–equip-150 records.
- Added `docs/data/dlc/time-patrol-support-pack-costume-canonical-equipment-capacity-decision-2026-09-23.json` and registered it in `pq-cross-domain-index.json`.
- Validation: five blocked identities preserved; new equipment IDs = 0; aliases = 0. CI/runtime unavailable.
- Exact next batch: proceed to the next highest-impact cross-domain consumer/coverage audit; revisit these costumes only after a principled equipment-ID allocation mechanism is designed.



### 2026-09-23 cycle update — Non-PQ reverse-navigation consumer hardening / live Super Soul baseline repair
- [x] Re-read the live cross-domain gate: the authoritative PQ relationship baseline is **854 unique edges = 244 skills / 146 Super Souls / 124 equipment / 247 characters / 86 DLC / 7 farming**.
- [x] Audited the live character reverse-navigation consumer (`docs/Characters-All.html`) and character reverse index: **247 forward character edges / 75 unique targets / 143 PQ sources / 0 unresolved targets / 0 duplicate pairs**; the explorer accepts `?q=` and its PQ links target `/Parallel-Quests-All/?q=PQ NNN`.
- [x] Audited the live Super Soul reverse-navigation consumer (`docs/Super-Souls-All.html`): it loads canonical Super Soul records plus canonical PQ relationships, exposes Canonical PQ links, and accepts `?q=` deep links.
- [x] Found and repaired a stale current-looking Super Soul projection in `docs/data/pq-explorer-reward-navigation-audit.json`: the structured Super Soul contract is **146/146**, not the obsolete **151/151** projection left by the pre-identity-correction state.
- [x] Synchronized `docs/data/pq-cross-link-integrity-audit.json` to the live **146/146** Super Soul pair contract.
- [x] Repaired stale current Super Soul projection totals in `docs/data/pq-cross-domain-status.json` to **146 forward / 143 reverse** and **854 current projection total**; dated historical 151/148 and older baselines remain preserved as history.
- [x] Added explicit reverse-destination query-contract metadata to `docs/data/pq-explorer-reward-navigation-audit.json` and `docs/data/pq-character-reverse-navigation-audit.json` without creating any relationship edges or aliases.
- [x] Preserved the five-edge Super Soul discrepancy boundary: `super-soul-232` through `super-soul-236` remain removed from the live canonical relationship projection; no relationship was re-added merely to satisfy stale metadata.
- [ ] CI/runtime remains unavailable; no CI success claimed.
- [ ] Exact next task: continue the **non-PQ consumer/navigation integrity** gate by auditing the remaining registered presentation/reverse-navigation consumers for stale **854/146** baselines, one-way links, scalar/list assumptions, and endpoint-name drift; do not add relationship edges.
### 2026-09-23 cycle update — Non-PQ endpoint-navigation baseline correction
- Live census before editing: **854 canonical PQ relationship edges**; Super Soul domain **146 forward / 143 unique reverse targets**.
- Bounded batch: `docs/data/pq-endpoint-navigation-validation.json` plus its deterministic validator label contract.
- Found stale current-looking Super Soul target scalars in the endpoint-navigation audit: three fields still said **148** even though the live relationship/reverse layer is **143**.
- Corrected those three current consumer fields to **143** and refreshed the audit generation date to 2026-09-23; no canonical relationships or identities were changed.
- Corrected stale validator check labels in `scripts/validate_pq_reference_pages.py`: labels now explicitly say **854** and **146** rather than obsolete 859/151 names while preserving the already-correct assertions.
- Added `docs/data/pq-non-pq-super-soul-endpoint-consumer-correction-2026-09-23.json` documenting the correction and evidence boundary.
- Validation: endpoint navigation audit now reports Super Soul 146 edges / 143 targets with zero missing targets; canonical relationship count remains 854. CI/runtime unavailable; no CI success claimed.
- Exact next batch: continue the registered non-PQ consumer census for remaining **current-looking** stale scalar/list assumptions and endpoint-name drift; leave dated historical/discrepancy snapshots untouched and do not add relationship edges.
### 2026-09-23 cycle update — Non-PQ presentation/index census synchronization
- Live census: **854 canonical PQ edges**; domain counts **244 / 146 / 124 / 247 / 86 / 7**; Super Soul reverse target census **143**.
- Bounded batch: `docs/data/pq-presentation-index-identity-audit.json` and the current section of `docs/data/pq-cross-domain-audit.json`.
- Found a stale current-looking Super Soul `reverse_records: 148` field in the presentation/index identity audit even though its own live recheck and exact forward-pair contract were already 143/146.
- Corrected that current presentation field to **143** and refreshed the generated date. Historical 148 evidence remains preserved elsewhere.
- Found an embedded schema-documentation consumer review in `pq-cross-domain-audit.json` still presenting 125 equipment / 88 DLC and 862-edge totals as if current. Corrected the current-review counts to **124 equipment / 86 DLC** and explicitly labeled the 862/125/88 values historical context.
- Validation: presentation audit now reports Super Soul reverse records 143, exact forward pairs 146, missing 0, extra 0, duplicates 0; canonical total remains 854. No relationships, identities, or aliases changed.
- Commits: `c6ebdf327b149d56cf5a2c730f3318302908dec8`, `2569bb4f2c0007d68254eeb6a233ffb44f4ae3ad`.
- CI/runtime unavailable; no CI success claimed.
- Exact next batch: continue searching **current-state consumer sections** for stale 862/125/88 or 148/151 scalar/list assumptions, prioritizing files that present themselves as current rather than dated historical/audit snapshots.

### 2026-09-23 cycle update — Canonical record reverse-navigation Super Soul census correction
- Live census: **854 canonical PQ edges**; Super Soul **146 forward / 143 unique reverse targets**; equipment **124 forward / 122 reverse targets**.
- Bounded batch: `docs/data/record-reverse-pq-navigation-audit.json`.
- Found current-looking Super Soul fields stale at **148 unique targets** and **151 canonical/structured pairs**, despite the audit's own structured mismatch arrays already being clean against the corrected live relationship layer.
- Corrected current fields to **143 unique targets** and **146/146 exact pairs**; refreshed audit date to 2026-09-23.
- Added `docs/data/pq-non-pq-record-reverse-navigation-correction-2026-09-23.json` documenting the correction and evidence boundary.
- Validation: unresolved targets 0, reverse-pair missing 0, extra 0, duplicate canonical pairs 0, structured mismatches 0; canonical relationships/aliases unchanged.
- Commits: `389a89ae0034b5c67d8022d108fbec481765b1dc`, `1cca40b8b1040331f40df751bacf4e4ccc7f2f27`.
- CI/runtime unavailable; no CI success claimed.
- Exact next batch: continue the current-state consumer census for remaining stale scalar/list assumptions and endpoint-name drift, prioritizing undated/current-looking projections.


### 2026-09-23 cycle update — Super Soul crosslink report current-status reconciliation
- Bounded batch: `docs/data/pq-super-soul-crosslink-report.json`.
- The report's numeric validation block was already current at **146 forward edges / 143 reverse endpoints**, but its status remained the obsolete `blocked_source_projection_discrepancy` and repeated the resolved 151/148 conflict as if still active.
- Corrected the status to `clean_current_projection` and documented that the five-edge delta was resolved by removing misidentified indexed-only Super Soul 232-236 relationships; dated historical discrepancy records retain the former 151/148 state.
- No relationship edges were added or removed in this batch; this was status/documentation synchronization only.
- Commit: `e4db907d4e2ef973ee902336e80fcb22e348b70b`.
- CI/runtime unavailable; no CI success claimed.
- Exact next batch: continue current-state consumer census for remaining stale scalar/list assumptions and endpoint/status drift, preserving dated historical snapshots.


### 2026-09-23 cycle update — Non-PQ cross-domain current-projection correction
- Live census: **854 canonical PQ relationship edges**; domain counts **244 / 146 / 124 / 247 / 86 / 7**; Super Soul reverse target census **143**.
- Bounded batch: `docs/data/pq-cross-domain-audit.json` current-projection sections.
- Found and corrected seven stale current-looking fields: Super Soul reverse **148 → 143**; Super Soul forward/reverse report census **151/148 → 146/143**; current projection total **859 → 854**; current reconciliation artifact total **859 → 854**; obsolete 860-edge wording → 854; current integrity-review Super Soul count **151 → 146**.
- Added `docs/data/pq-non-pq-cross-domain-audit-current-projection-correction-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.md`.
- Historical 862/860/840 snapshots remain untouched. No canonical relationship edges, identities, or aliases were added or removed.
- Validation: JSON parse succeeded; current contract remains **854 / 244 / 146 / 124 / 247 / 86 / 7** and Super Soul **146 forward / 143 reverse**; correction audit registered.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next batch: continue the registered non-PQ consumer census for remaining **current-looking** scalar/list assumptions and endpoint/status drift; prioritize undated/current projections and preserve dated historical snapshots.


### 2026-09-23 cycle checkpoint — cross-domain projection correction commits
- Commits: audit `c4629a85415efc444c4bd902f918bacfc452693c`; correction audit `c39ac951e8472b0093cffaf6d89cdaae918989f8`; cross-domain registry `dcda02a0dad1ccfc5c96793d1162942d15a5d6c5`; changelog `da56ca26075760f36db81c7efe72520250034e5a`; handoff `c6d88595d5fb32d0b85990853d336b9267ed6656`; TODO `ab24b027cb4bd7705256401d919cbb0c3c610f17`.
- These commits are append-only/current-state documentation and projection corrections; canonical PQ relationship rows were not changed.
- CI/runtime remains unavailable; no CI success claimed.


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


### 2026-09-23 cycle update — PQ reference validator current-check label correction
- Live census before/after: **854 canonical PQ relationship edges** — 244 skill / 146 Super Soul / 124 equipment / 247 character / 86 DLC / 7 farming.
- Bounded batch: `scripts/validate_pq_reference_pages.py`.
- Found two stale **check-name labels** whose executable expressions already enforced the correct live values: `relationship_total_is_859` enforced 854, and `super_soul_edge_count_is_151` enforced 146.
- Renamed them to `relationship_total_is_854` and `super_soul_edge_count_is_146`. No validation logic or canonical data changed.
- Evidence limits: dated historical documents and correction artifacts containing 859/151/148 remain preserved; only active validator labels were changed.
- Validation: source inspection confirms executable expressions remain **854** total and **146** Super Soul; changed Python syntax is structurally unchanged apart from key names. CI/runtime unavailable; no CI success claimed.
- Commit: `b818e517efe0b1ded021caf78000c78e73d3f86e`.
- Exact next batch: continue current-state consumer census for remaining stale executable check labels, endpoint names, and undated/current scalar/list assumptions; do not rewrite historical evidence.


### 2026-09-23 cycle update — Canonical PQ current reconciliation wording synchronization
- Live census: **854** canonical relationship edges; **146** Super Soul forward / **143** reverse targets.
- Bounded batch: `docs/data/pq-reward-relationships.json` current reconciliation object.
- Corrected stale current wording that still called the live baseline **859** and described the 151/148 Super Soul discrepancy as unresolved.
- Current note now states the live **854 / 146 / 143** contract and records the five-edge 232-236 projection discrepancy as resolved; dated historical values remain untouched.
- Added and registered `docs/data/pq-non-pq-current-reconciliation-note-correction-2026-09-23.json`.
- Validation: canonical arrays/aliases unchanged; current counts remain 854 / 244 / 146 / 124 / 247 / 86 / 7. CI/runtime unavailable.
- Commits: relationship correction `182383eb90cdab98ecd84e0e46a26a4d75c03dd3`; audit `6198c64dde33d63fad5cf8a03e09549e92be2f4b`; registry `36c97863db9075642fc3ad073848a7f9fa710440`.
- Exact next batch: continue active current-state endpoint/status consumer census, preserving dated historical snapshots.


### 2026-09-23 cycle update — Current-state PQ consumer census completion
- Live baseline: **854** relationships = 244 Skill / 146 Super Soul / 124 Equipment / 247 Character / 86 DLC / 7 Farming; Super Soul reverse **143**.
- Scanned remaining current-looking scalar/list/endpoint-count candidates across validator, producer, crosslink, status, reverse-index, and normalization consumers.
- Result: **no remaining deterministic current-state drift** identified in this bounded census. Numeric occurrences in equipment/character consumers were verified as target IDs/PQ identifiers rather than stale totals.
- Added and registered docs/data/pq-current-state-consumer-census-2026-09-23.json.
- Historical 862/860/859/840 and 151/148 values remain preserved where dated/historical.
- Validation: current consumer contracts remain synchronized; CI/runtime unavailable.
- Commits: census 4c3e1bddce88d9bcd1b489f54e4310bb142667b6; registry 0429c1311a32b559c8d7b7cf4977da03287eb74e.
- Exact next batch: transition to the P1 exhaustive provenance/data queue, beginning with the strict-thin Super Soul records identified by the current research census.


### 2026-09-23 cycle update — Super Soul 034 item-level evidence boundary
- Live census: **229 canonical / 0 duplicate IDs / 4 strict-thin records** (032, 034, 158, 217).
- Bounded batch: **Super Soul 034 — “The final battle begins now.”**.
- Research/evidence: fresh independent PQ guide evidence confirms the exact-name reward in **PQ186 — Frieza's Right-Hand Man**; official Bandai Namco/Nintendo sources continue to establish Future Saga Chapter 4 provenance. citeturn3search0turn3search1
- Changes: added/registered `docs/data/super-soul-034-item-level-evidence-reconciliation-2026-09-23.json`; refreshed `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json`; registered the audit in `docs/data/pq-cross-domain-index.json`; logged the cycle in `CHANGELOG.md` and `docs/TODO-EXHAUSTIVE.md`.
- Evidence limits preserved: no character attribution, trigger, effect, duration, stacking, Limit Burst, drop probability, or Ultimate-Finish mapping was inferred. In particular, proximity to Fu clothing rewards is not treated as item-level proof of Fu ownership.
- Validation: canonical Super Soul record unchanged; **229 canonical / 0 duplicate IDs / 4 strict-thin records**; audit registration and checkpoint refresh completed.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: **Super Soul 217** Limit Burst/item-level evidence research; if unresolved, **158** collision-safe evidence research; then **032**.


### 2026-09-23 cycle update — Super Soul 158 identity conflict resolution
- Fresh exact-name evidence resolves the apparent **Super Soul 158 “Do or Die”** record as an identity conflict: Do or Die is documented as Nail's **Power Up Type Super Skill** from PQ49, while Nail's Super Soul is **“I must protect Grand Elder Guru!”**. citeturn3search0turn3search2
- Record 158 was preserved as a conflict placeholder and its unsupported Super Soul mechanics/acquisition fields were cleared. No silent ID remap was made.
- Added/registered the identity-conflict audit and refreshed the strict-thin checkpoint; TODO and CHANGELOG updated.
- Validation: record preservation and conflict marking completed; CI unavailable.
- Exact next task: resolve the canonical ID mapping for 158, then research **Super Soul 217** Limit Burst/item-level evidence and **032**.


### 2026-09-23 cycle update — Super Soul 158 collision reconciliation
- External verification confirms the 158 “Do or Die” name belongs to a **Power Up Type Super Skill**, while Nail's Super Soul is “I must protect Grand Elder Guru!”. citeturn0search0turn0search1
- Record 158 remains a collision placeholder; no Super Soul mechanics are asserted. Canonical migration to the Super Skill domain remains a TODO.
- Added/registered the reconciliation audit and updated checkpoint/TODO/CHANGELOG.
- Next exact batch: **Super Soul 217** Limit Burst/item-level evidence, then **032**.


### 2026-09-23 cycle update — Super Souls 217 / 032
- **217:** Fresh searches corroborate the exact Super Soul, PQ 134 association, and +12 Ki/+12 Stamina utility. No reliable item-level Limit Burst evidence was found, so Limit Burst fields remain null.
- **032:** Fresh Steam PQ catalogue evidence confirms the exact PQ 185 reward. Current GameFAQs discussion documents its second displayed-name state after KO (“Using this power should be no sweat for you guys.”); this is recorded without inferring a second effect.
- Added evidence-refresh audit and updated checkpoint/TODO/CHANGELOG.
- Next priority: continue authoritative/item-level 217 Limit Burst research; then perform the next unresolved strict-thin Super Soul batch.


### 2026-09-23 continuation correction — strict-thin queue
- Two targeted web-search passes for **super-soul-217** failed to expose reliable item-level Limit Burst trigger/effect data. Core +12 Ki/+12 Stamina and PQ134 provenance remain corroborated; no Limit Burst inference was made.
- The strict-thin checkpoint's next queue has been corrected: prioritize **034** for any new authoritative/item-level evidence, while 217 remains bounded and should not receive repetitive low-yield searches unless a source exposes explicit Limit Burst data. Continue tracking **158** as the documented Super Skill name collision.


### 2026-09-23 cycle update — Super Soul 034 bounded item-level evidence pass
- Live strict-thin census before editing: **229 canonical / 0 duplicate IDs / 4 strict-thin records** — 032, 034, 158, 217.
- Bounded batch: **Super Soul 034 — “The final battle begins now.”**.
- Research/evidence: rechecked the maintained PQ 186 reward inventory, official Chapter 4 DLC inventory context, and current community discussion. The exact-name PQ 186 reward identity is confirmed, but no reliable item-level evidence established character source, effect, trigger, duration, stacking, or Limit Burst. The current community thread explicitly discusses the other Chapter 4 Souls without identifying 034's mechanics. citeturn1search0turn3reddit24
- Changes: added `docs/data/super-soul-034-item-level-evidence-boundary-2026-09-23.json`; registered it in `docs/data/pq-cross-domain-index.json`; refreshed `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json`; appended TODO/changelog records.
- Evidence limits preserved: Fu's adjacent PQ 186 costume inventory is not treated as item-level attribution; no mechanics, item ID, reward tier, drop probability, or hidden condition was inferred.
- Validation: audit JSON parses; strict-thin census remains **229 / 0 / 4**; no canonical relationship or identity changes; audit registration present; no CI/runtime success exposed.
- CI: unavailable; do not claim CI success.
- Current handoff commits/updated-file SHAs: audit `e2d618b0ec2ca63ed92f235ec5b0edd3555553c5`; checkpoint `9d94f987567920863cf800fd7d360770d604f4df`; cross-domain index `c0f6d70a001958257e29288632da7888c76c925e`; TODO `11d496ce51df204f83f30bc3ef00e6e475828b9f`; changelog `20b24961a5f76f23e881062495e34d778e123392`.
- Exact next batch: **Super Soul 032** — perform a fresh exact-name/item-level Limit Burst pass. Return to 034 only if new item-level evidence appears. Separately preserve the 158 Super Skill/Super Soul collision boundary.


### 2026-09-23 cycle update — Super Soul 032 Limit Burst evidence boundary
- Live strict-thin context: **229 canonical / 0 duplicate IDs / 4 strict-thin records** — 032, 034, 158, 217.
- Bounded batch: **Super Soul 032 — “This power... It's different from any I've ever had.”**.
- Research/evidence: exact-name/item-level searches plus repository evidence reconfirm PQ185 identity and the existing community-tested below-50%-HP +20% all-abilities effect. Current GameFAQs discussion confirms a second displayed-name state after KO, changing to “Using this power should be no sweat for you guys.”, but does not establish its mechanical effect. citeturn3search0
- Limit Burst result: no reliable exact-name/item-level source exposed a Limit Burst type, trigger, or effect for 032. No generic/same-character Limit Burst was substituted.
- Changes: added `docs/data/super-soul-032-limit-burst-evidence-boundary-2026-09-23.json`; registered it in `docs/data/pq-cross-domain-index.json`; refreshed `docs/data/super-soul-strict-thin-checkpoint-2026-09-23.json`; updated TODO and CHANGELOG.
- Canonical 032 record remains unchanged and partially verified. No PQ relationship or identity data changed.
- Validation: evidence audit JSON is structurally valid; checkpoint updated; registry entry added; current strict-thin count remains **229 / 0 / 4**. CI/runtime unavailable; no CI success claimed.
- Commits: audit `5192bb40d567343c3dbc1408d7595f08a69756d0`; registry `fd7f9f9fbe30c27b8b210d7395d90ca083671a3d`; checkpoint `5f2724667d3d1dfbccad266a7dfe0a0b0c0d37fa`; TODO `f0638887d9e886987e38a9e85692d0446c6b700d`; changelog `f9aa4bdeba29fcd56a7ecb1e549d7d268dcc3d93`.
- Exact next batch: **Super Soul 158 collision-safe canonical migration analysis** — inspect the canonical Super Skill layer, ID/alias conventions, PQ49 crosslinks, and determine the safest non-destructive migration path for the Do or Die name collision. Do not silently rename/merge the Super Soul record or alter PQ relationship identities until mapping is explicitly supported.

### 2026-09-23 cycle update — Super Soul 158 canonical domain migration
- Live baseline for this bounded migration: the canonical Super Soul layer contained the prior 158 collision placeholder; the canonical Skills layer already contained **skill-do-or-die** for PQ49.
- Bounded batch: **Super Soul 158 — “Do or Die”** identity/cross-domain migration.
- Repository evidence: docs/data/skills.json contains skill-do-or-die; docs/data/pq-skill-crosslink-report.json maps PQ49 directly to that Skill ID; docs/data/parallel-quests-record-layer.json retains the Skill ID. The former Super Soul 158 record had no distinct mechanics and was explicitly classified as a collision placeholder.
- Changes: removed super-soul-158 from docs/data/super-souls-record-layer.json; removed the false PQ49 Super Soul reward array/ID and producer relationship; removed 158 from the Super Soul forward/reverse crosslink projection; added docs/data/super-soul-158-canonical-domain-migration-2026-09-23.json; registered the migration in docs/data/pq-cross-domain-index.json; refreshed census/checkpoint/TODO/CHANGELOG.
- Evidence boundary preserved: the Skill's mechanics/character source are not copied into a Super Soul. The legacy 158 identifier remains documented only as a migration mapping to skill-do-or-die.
- Validation: **230** canonical Super Soul records, **0** duplicate IDs, strict-thin queue **032 / 034 / 217**; PQ Super Soul projection **145 forward / 142 reverse**; PQ relationship projection total **853**; PQ49 retains skill-do-or-die and has no Super Soul 158 edge; crosslink report has no 158 endpoint.
- Commits: canonical layer 51c8527ea65682a7737461f8dc544268532d431d; PQ record f3e879d5ba828167727021075bf412376cedda4d; relationship 04760d84437f1ad31600c7d4039c92272a911071; crosslink 33b624bee0e33176c4b08c4ff2f2ea9b512dec26; migration audit b9f540941128d26f9d79d1b6f39f384ea58c59a9; census 93e9b689fe7f4a9ab5eef7774725faabfa29d75f; checkpoint 69c7da82f90d4da1a6a81a720d5d7d96ffcd0e23; registry a307cbd920fa493b32a3bdcad9e7f0dbfb29cfea; TODO 553043329d9f3d51a6258d1ec8240d3bdae485bf; changelog cb2c21e75bab845dc790e4472abfa00bd93ef926.
- CI/runtime: unavailable; do not claim CI success.
- Exact next batch: **Super Soul 217** exact-name/item-level Limit Burst research. Search only for explicit Limit Burst wording; if no new evidence appears, preserve the null and advance to the broader P1 provenance/data queue rather than repeating low-yield searches.

### 2026-09-23 cycle update — Super Soul 217 Limit Burst verification
- Live census before editing: **230 canonical Super Souls / 0 duplicate IDs / strict-thin queue 032, 034, 217**.
- Bounded batch: **Super Soul 217 — “Power! A lotta power! It's great!”** exact-name/item-level Limit Burst research.
- Research/evidence: a GameFAQs discussion specifically asks about this exact Super Soul's Limit Burst; a responder identifies **Power Ki Blast**, **Auto Health and Stamina Up**, and **DEF Down**. This establishes item-specific Limit Burst type/effect, but not a trigger condition. citeturn1search0
- Changes: canonical 217 now has `limit_burst = Power Ki Blast`, `limit_burst_effect = Auto Health and Stamina Up; DEF Down`, and retains `limit_burst_trigger = null`. Added `docs/data/super-soul-217-limit-burst-evidence-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`.
- Evidence limits preserved: no trigger, timing, engine-level behavior, acquisition, character, magnitude, duration, or stacking claims were inferred or changed.
- Validation: strict-thin queue reduced to **032 / 034**; 217 exits because all strict core fields are populated. CI/runtime unavailable; no CI success claimed.
- Commits: canonical record `f3e7efaa26547455995b0d72db1018d942085c29`; audit `9e33cff6e1d020275ccaa209681da0a5dce7e4ce`; registry `2342e8741a4ce71428bbf649df28a37d1afdbc65`; census `3dd504b767ded483d9b69156e6dc75c98b125918`; checkpoint `0a5517ee5071cbd1e424a7064d77b7387510d6fe`; TODO `5b077dba63857a0b486c9baa53bfb40cb744b87a`; changelog `f2563acd86f91d088942959fc76df2592959c06c`.
- Exact next batch: **Super Soul 034** only if a new item-level/authoritative source can resolve its unresolved fields; otherwise advance to **032 or the broader P1 provenance/data queue**. Do not repeat low-yield 217 searches.

### 2026-09-23 cycle update — Post-158 current PQ consumer synchronization
- Live canonical relationship source was re-read after the 158 migration: **853 total = 244 Skill / 145 Super Soul / 124 Equipment / 247 Character / 86 DLC / 7 Farming**. Super Soul projection is **145 forward / 142 reverse targets**; `super-soul-158` is absent from the live canonical projection.
- Detected and repaired stale active current-consumer metadata that still treated the pre-migration 854/146/143 baseline as current. Repaired PQ reference/audit/status, producer census, page/explorer consumers, endpoint/navigation consumers, presentation parity, reverse-index audit, current-state census, validator expectations, and the Super Soul thin census.
- Added `docs/data/pq-current-baseline-after-super-soul-158-migration-2026-09-23.json` and registered it in `docs/data/pq-cross-domain-index.json`. Prior 854/146/143 and older 859/151/148, 862/860/840 values remain preserved as historical correction evidence.
- Validation by direct live-file parse: canonical relationship arrays **853**; domain counts **244/145/124/247/86/7**; Super Soul crosslink **145/142**; producer **853/145/142**; presentation **853/145/142**; strict-thin **032/034**; no 158 crosslink.
- Important evidence boundary: this cycle changed only deterministic current-state consumer metadata after a confirmed canonical domain migration. No new relationship edge was invented.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next task: perform one final targeted inspection for any remaining *active* 854/146/143 assertions, then resume the broader **P1 exhaustive provenance/data queue**. Do not repeat Super Soul 032/034 searches unless new exact-name/item-level evidence becomes available.


### 2026-09-23 cycle update — P1 skill provenance alpha batch
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs**; the prior 2026-09-22 stale census was superseded by a fresh 2026-09-23 census.
- Bounded batch: **Absolute Zero, Afterimage, Afterimage Strike, All Clear, Android Rush**.
- Changes: refreshed canonical/index last_verified to 2026-09-23; no gameplay/acquisition semantics changed.
- Added docs/data/skill-provenance-audit-2026-09-23-alpha-batch.json and docs/data/skill-stale-metadata-census-2026-09-23.json; both are registered in the cross-domain index.
- Validation: **455/455**, 0 duplicate IDs, five target canonical/index pairs synchronized; live stale queue **447**.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: **Angry Explosion, Angry Hit, Angry Shout, Apocalyptic Burst, Arm Crash**. Recompute the live census first; research only fields in scope and preserve existing uncertainty.


### 2026-09-23 cycle update — P1 skill provenance beta batch
- Completed **Angry Explosion, Angry Hit, Angry Shout, Apocalyptic Burst, Arm Crash**.
- Canonical/index last_verified synchronized to **2026-09-23**.
- Preserved the existing Apocalyptic Burst reward-tier conflict; no unsupported acquisition certainty was introduced.
- Added beta provenance audit and beta stale-census artifacts and registered the audit in the cross-domain index.
- Live canonical skill layer remains **455/455 with 0 duplicate IDs**; beta targets are synchronized. CI/runtime unavailable; no CI success claimed.
- Exact next batch: **Android Kick, Android Rush, Android Shoot, Android S.S. Deadly Bomber, Android Tri-Beam**. Recompute the live census first.


### 2026-09-23 cycle update — P1 skill provenance gamma batch
- Live inspection corrected the previous handoff: **Android Kick, Android Shoot, Android S.S. Deadly Bomber, and Android Tri-Beam are not canonical skill records**; Android Rush was already completed.
- Completed **Assault Vanish, Atomic Blast, Audacious Laugh** and synchronized canonical/index last_verified to 2026-09-23.
- Added and registered gamma provenance audit and stale census artifacts.
- Validation: **455/455**, 0 duplicate IDs; **439** records remain stale.
- Exact next batch: **Beast, Become Giant, Bending Kamehameha, Big Bang Kamehameha, Big Bang Knuckle**. Recompute the live census first.


### 2026-09-23 cycle update — P1 skill provenance delta batch
- Completed **Beast, Become Giant, Bending Kamehameha, Big Bang Kamehameha, Big Bang Knuckle** after live reinspection and fresh external evidence review.
- Canonical/index last_verified synchronized to 2026-09-23; existing evidence boundaries preserved, including Big Bang Knuckle's reward-source conflict.
- Added and registered the delta provenance audit and stale census.
- Live state: **455/455**, 0 duplicate IDs, **434** stale records remaining. CI/runtime unavailable.
- Exact next batch: **Blades of Judgment, Blaster Ball, Blaster Bomb, Blaster Cannon, Blaster Meteor**.


### 2026-09-23 cycle update — P1 Blaster skill provenance batch
- Completed **Blades of Judgment, Blaster Ball, Blaster Bomb, Blaster Cannon, Blaster Meteor**.
- Canonical/index verification dates synchronized to 2026-09-23; evidence boundaries preserved.
- Added and registered batch audit and stale census.
- Live state: **455/455**, 0 duplicate IDs, **429 stale** records remaining. CI/runtime unavailable.
- Exact next batch: **Blaster Shell, Blaster Stream, Blazing Attack, Bloody Counter, Bluff Kamehameha**.


### 2026-09-23 cycle update — Big Bang Attack provenance strengthening
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 0 nullable canonical `ki_cost` / 3 exactly-two-source canonical records**.
- Bounded batch: **Big Bang Attack** (`skill-big-bang-attack`).
- Research/evidence: independent GameFAQs TP Medal Shop catalogue corroborates Big Bang Attack as a TP Medal Shop Super and reports a **15 TP Medal** price; the source notes shop contents are RNG/rotation based. citeturn2search0
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
- Research/evidence: an independent Steam Expert Mission guide lists **EM04 — Invasion of the Evil Super Namek** and **Super Destructo-Disc** under Basic Rewards; an independent Dragon Ball technique reference also identifies Expert Mission 04 as the Future Warrior acquisition route. citeturn0search4turn0search0
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

### 2026-09-23 cycle update — P1 Core-through-Critical skill provenance refresh
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 405 stale / 1 exact-two-source**.
- Completed **Counter Burst, Counter Impact, Crazy Finger Shot, Crimson Edge, Critical Upper** provenance refresh; canonical/index dates are now **2026-09-23**.
- Counter Impact gained official Dragon Ball corroboration; existing reward/mechanics conflicts and evidence boundaries were preserved.
- Added/registered **docs/data/skill-provenance-audit-2026-09-23-core-through-critical-upper.json** and **docs/data/skill-stale-metadata-census-2026-09-23-core-through-critical-upper.json**.
- Validation: **455/455**, **0 duplicates**, **400 stale**, exact-two-source queue **1**, target parity clean.
- CI/runtime unavailable; no CI success claimed.
- Exact next action: recompute the live stale queue and continue from **Burst Blitz, Burst Kamehameha, Burst Reflection, Burst Rush, Burst Stinger, Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, Charge**.


### 2026-09-23 cycle update — P1 Burst Blitz through Burst Stinger provenance refresh
- Live census before editing: **455 canonical / 455 index / 400 stale / 0 duplicate IDs**.
- Completed **Burst Blitz, Burst Kamehameha, Burst Reflection, Burst Rush, Burst Stinger**.
- Refreshed canonical/index verification dates to **2026-09-23** and synchronized source arrays; dedicated skill references and independent corroboration were rechecked.
- Evidence limits preserved: no unsupported probability, new gate, or narrower usability restriction inferred.
- Added/registered **docs/data/skill-provenance-audit-2026-09-23-burst-blitz-through-burst-stinger.json**.
- Validation: **455/455**, **0 duplicate IDs**, target parity **clean**, stale queue **395**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next batch: **Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, Charge, Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, Core Breaker**.


### 2026-09-23 cycle update — P1 Change The Future through Charge provenance refresh
- Live census before editing: **455 canonical / 455 index / 395 stale / 0 duplicate IDs**.
- Completed **Change The Future, Chaos Shot, Chaos Wall, Chaotic Time Impact, Charge**.
- Refreshed canonical/index verification dates to **2026-09-23**; existing sources, acquisition details, mechanics, and conflicts were preserved.
- Added/registered **docs/data/skill-provenance-audit-2026-09-23-change-the-future-through-charge.json**.
- Validation: **455/455**, **0 duplicate IDs**, target parity **clean**, stale queue **390**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next batch: **Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, Core Breaker, Crush Cannon, Crush Stream, Crusher Ball, Dancing Parapara, Dark Inscription**.


### 2026-09-23 cycle update — P1 Charged Ki Wave through Core Breaker provenance refresh
- Live census before editing: **455 canonical / 455 index / 390 stale / 0 duplicate IDs**.
- Completed **Charged Ki Wave, Circle Flash, Comet Strike, Confusion Blade, Core Breaker**.
- Rechecked dedicated skill evidence and refreshed canonical/index verification dates to **2026-09-23**; existing acquisition, cost, scope, mechanics, and evidence boundaries were preserved.
- Added/registered **docs/data/skill-provenance-audit-2026-09-23-charged-ki-wave-through-core-breaker.json**.
- Validation: **455/455**, **0 duplicate IDs**, target parity **clean**, stale queue **385**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next batch: **Crush Cannon, Crush Stream, Crusher Ball, Dancing Parapara, Dark Inscription, Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input**.


### 2026-09-23 cycle update — P1 Crush Cannon through Dark Inscription provenance refresh
- Live census before editing: **455 canonical / 455 index / 385 stale / 0 duplicate IDs**.
- Completed **Crush Cannon, Crush Stream, Crusher Ball, Dancing Parapara, Dark Inscription**.
- Rechecked dedicated skill evidence and refreshed canonical/index verification dates to **2026-09-23**; existing acquisition, cost, scope, mechanics, and evidence boundaries were preserved.
- Added/registered **docs/data/skill-provenance-audit-2026-09-23-crush-cannon-through-dark-inscription.json**.
- Validation: **455/455**, **0 duplicate IDs**, target parity **clean**, stale queue **380**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next batch: **Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, Data Input, Dead End Rain, Deadly Dance, Death Ball, Death Beam, Death Crasher**.

### 2026-09-23 cycle update — P1 Darkness-through-Data-Input skill enrichment
- Completed **Darkness Eye Beam, Darkness Rush (Melee), Darkness Rush (Ranged), Darkness Twin Star, and Data Input** as the next bounded skill-provenance/mechanics batch.
- Added independent/direct sources where they materially strengthened provenance; expanded mechanics notes only from cited dedicated skill evidence.
- Preserved all existing acquisition, reward-tier, Ultimate Finish, race, cost, and DLC evidence boundaries. Data Input's Extra Pack 1 vs Free Update 5 presentation conflict remains explicit.
- Added and registered `docs/data/skill-provenance-audit-2026-09-23-darkness-through-data-input.json`.
- Validation target: **455 canonical / 455 index / 0 duplicate IDs**; changed target source/date parity clean.
- CI/runtime remains unavailable; no CI success claimed.
- Exact next action: recompute the live stale queue after this batch and continue from the next stale canonical records after **Data Input**; do not repeat these five records or promote legacy-only records without a deliberate catalog-ingestion task.

### 2026-09-23 cycle update — P1 Dead End Rain through Death Crasher provenance refresh
- Completed **Dead End Rain, Deadly Dance, Death Ball, Death Beam, and Death Crasher**.
- Refreshed canonical/index verification dates to **2026-09-23** and rechecked existing repository provenance.
- Preserved acquisition, reward-tier, scope, cost, mechanics, and Ultimate Finish semantics; no unsupported probability or gate inferred.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-dead-end-rain-through-death-crasher.json` and updated `CHANGELOG.md`.
- Validation: **455 canonical / 455 index / 0 duplicate IDs / 5 targets synchronized**.
- Exact next action: recompute live stale state and continue with **Death Psycho Bomb, Death Slash, Death Slicer, Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Destruction's Concerto: Meteor, Destruction's Concerto: Starfall**.

### 2026-09-23 cycle update — P1 Death Psycho Bomb through Destruction's Concerto provenance refresh
- Completed **Death Psycho Bomb, Death Slash, Death Slicer, Demon Flash Strike, Demon Flurry, Demon Ray, Demonic Destruction, Destruction's Concerto: Comet, Destruction's Concerto: Meteor, and Destruction's Concerto: Starfall**.
- Refreshed canonical/index verification dates to **2026-09-23**; existing acquisition, reward-tier, cost, scope, mechanics, and DLC semantics were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-death-psycho-bomb-through-destruction-concerto.json`.
- Validation: **455/455**, **0 duplicate IDs**, **10 targets synchronized**, stale queue **360**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next batch: **Destruction's Conductor, Destructive Fission, Destructive Flare, Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole, Divine Kamehameha**.

### 2026-09-23 cycle update — P1 Destruction's Conductor through Divine Kamehameha provenance refresh
- Completed **Destruction's Conductor, Destructive Fission, Destructive Flare, Destructive Fracture, Destructo-Disc, DIE DIE Missile Barrage, Dimension Cannon, Dimension Ray, Dimensional Hole, and Divine Kamehameha**.
- Refreshed canonical/index verification dates to **2026-09-23**; existing acquisition, reward-tier, cost, scope, mechanics, and DLC semantics were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-destruction-through-divine-kamehameha.json`.
- Validation: **455/455**, **0 duplicate IDs**, **10 targets synchronized**, stale queue **350**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next batch: recompute live stale queue and continue from the next stale canonical records.

### 2026-09-23 cycle update — P1 Divine Lasso through Dodoria Launcher provenance refresh
- Completed **Divine Lasso, Divine Ray Bomb, Divine Spear, Divine Wrath: Purification, Divinity Unleashed, Do or Die, Dodon Ray, Dodoria Beam, Dodoria Headbutt, and Dodoria Launcher**.
- Refreshed canonical/index verification dates to **2026-09-23**; existing acquisition, reward-tier, cost, scope, mechanics, DLC, and conflict boundaries were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-divine-through-dodoria.json`.
- Validation: **455/455**, **0 duplicate IDs**, **10 targets synchronized**, stale queue **340**.
- CI/runtime: no successful status exposed; no CI success claimed.
- Exact next action: recompute the live stale queue and continue from the next stale canonical records.


### 2026-09-23 cycle update — P1 Double Crush through Dust Attack provenance refresh
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 340 stale**.
- Bounded batch: **Double Crush, Double Death Slicer, Double Sunday, Dragon Blitz, Dragon Burn, Dragon Fist, Dragon Spark, Dragon Spiral, Dragon Thunder, Drain Field, Dual Destructo-Disc, Dust Attack**.
- Research/evidence: rechecked the existing repository-maintained dedicated skill references, PQ/mentor provenance, official DLC references where already present, and independent player/reference sources retained in each record; no unsupported field was inferred.
- Changes: refreshed canonical/index last_verified to **2026-09-23** and appended a provenance-refresh note to each target; acquisition routes, costs, mechanics, DLC classifications, and existing conflicts were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-double-crush-through-dust-attack.json` and refreshed `docs/data/skill-stale-metadata-census-2026-09-23.json`.
- Validation: **455 canonical / 455 index / 328 stale** after the batch; target source/date parity clean; no unsupported inference introduced.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: recompute the live stale queue, then continue with the first alphabetical stale records returned by the fresh census.

### 2026-09-23 cycle update — P1 Dynamite Kick through Energy Barrier provenance refresh
- Live census before editing: **455 canonical / 455 index / 328 stale / 0 duplicate IDs**.
- Bounded batch: **Dynamite Kick, Eagle Kick, Earth Splitting Galick Gun, Elegant Blaster, Elite Beam, Elite Shooting, Emperor's Blast, Emperor's Cannon, Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Barrier**.
- Research/evidence: rechecked existing repository-maintained skill/PQ/mentor references and current independent discussion where useful; no unsupported field was inferred. Earth Splitting Galick Gun's PQ #11 acquisition remains anchored to the repository's current PQ evidence.
- Changes: refreshed canonical/index `last_verified` to **2026-09-23** and appended a provenance-refresh note to each target; existing acquisition, costs, mechanics, DLC classifications, conflicts, and uncertainty were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-dynamite-kick-through-energy-barrier.json` and refreshed the stale census.
- Validation: **455 canonical / 455 index / 316 stale / 0 duplicate IDs**; target source/date parity clean.
- CI/runtime: unavailable; no CI success claimed.
- Exact next batch: recompute the live stale queue and continue with the first alphabetical stale canonical records.

### 2026-09-23 cycle update — P1 Energy Charge through Evil Flight Strike provenance refresh
- Live census before editing: **455 canonical / 455 index / 316 stale / 0 duplicate IDs**.
- Bounded batch: **Energy Charge, Energy Dome, Energy Field, Energy Minefield, Energy Release, Energy Shot, Eraser Bomb, Evil Blast, Evil Explosion, Evil Eyes, Evil Flame, Evil Flight Strike**.
- Research/evidence: rechecked existing repository skill/PQ/mentor/DLC references and independent references already attached to the records; no unsupported field was inferred.
- Changes: refreshed canonical/index `last_verified` to **2026-09-23** and appended a provenance-refresh note to each target; acquisition, costs, mechanics, DLC, conflicts, and uncertainty were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-energy-through-evil-flight-strike.json` and refreshed the stale census.
- Validation: **455 canonical / 455 index / 304 stale / 0 duplicate IDs**; target source/date parity clean.
- CI/runtime: unavailable; no CI success claimed.
- Exact next action: recompute the live stale queue and continue with the first alphabetical stale canonical records.

### 2026-09-23 cycle update — P1 Evil Ray Strike through Feint Shot provenance refresh
- Live census before editing: **455 canonical / 455 index / 304 stale / 0 duplicate IDs**.
- Bounded batch: **Evil Ray Strike, Evil Rise Strike, Evil Whirlwind, Excellent Full Course, Explosive Assault, Explosive Buu Buu Punch, Explosive Wave, Eye Beam, Fake Blast, Fake Death, Feint Crash, Feint Shot**.
- Research/evidence: rechecked existing repository skill/PQ/mentor/DLC references and independently corroborated selected acquisition/mechanics context; no unsupported field was inferred.
- Changes: refreshed canonical/index `last_verified` to **2026-09-23** and appended a provenance-refresh note to each target; existing acquisition, costs, mechanics, DLC, conflicts, and uncertainty were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-evil-through-feint-shot.json` and refreshed the stale census.
- Validation: **455 canonical / 455 index / 292 stale / 0 duplicate IDs**; target source/date parity clean.
- CI/runtime: unavailable; no CI success claimed.
- Exact next action: recompute the live stale queue and continue with the first alphabetical stale canonical records.

### 2026-09-23 cycle update — P1 Fierce Fist through Final Flash (SS3 DAIMA) provenance refresh
- Live census before editing: **455 canonical / 455 index / 292 stale / 0 duplicate IDs**.
- Bounded batch: **Fierce Fist, Fighting Pose A, Fighting Pose C, Fighting Pose E, Fighting Pose F, Fighting Pose H, Fighting Pose K, Final Cannon, Final Charge, Final Explosion, Final Flash, Final Flash (SS3 DAIMA)**.
- Research/evidence: rechecked existing repository skill/PQ/mentor/DLC references and independent corroborating references; no unsupported field was inferred.
- Changes: refreshed canonical/index `last_verified` to **2026-09-23** and appended a provenance-refresh note to each target; existing acquisition, costs, mechanics, DLC, conflicts, and uncertainty were preserved.
- Added/registered `docs/data/skill-provenance-audit-2026-09-23-fierce-fist-through-final-flash-ss3-daima.json` and refreshed the stale census.
- Validation: **455 canonical / 455 index / 280 stale / 0 duplicate IDs**; target source/date parity clean.
- CI/runtime: unavailable; no CI success claimed.
- Exact next action: recompute the live stale queue and continue with the first alphabetical stale canonical records.

### 2026-09-23 cycle update — P1 Final-through-Force Edge skill provenance/mechanics refresh
- Live census before editing: **455 canonical / 455 index / 0 duplicate IDs / 280 stale**.
- Bounded batch: **Final Flash (Super), Final Kamehameha, Final Pose, Final Rampage, Finish Breaker, Finishing Blow, Flash Bomber, Flash Chaser, Flash Fist Crush, Flash Strike, Focus Flash, Force Edge**.
- Research/evidence: reused the repository's existing exact-name source sets and current dedicated Xenoverse 2 skill documentation; evidence corroborates the bounded mechanics for beam hit counts, Final Pose duration/effects, barrage extension, counter behavior, and Force Edge follow-up behavior.
- Changes: refreshed canonical/index `last_verified` to **2026-09-23** and expanded only bounded mechanics/provenance notes; no unrelated acquisition, reward probability, Ultimate-Finish, or CaC-restriction fields were inferred.
- Added/registered **docs/data/skill-provenance-audit-2026-09-23-final-through-force-edge.json**.
- Validation after write: **455 canonical / 455 index / 0 duplicate IDs / 268 stale**. All 12 target records have canonical/index parity for verification date, mechanics notes, and sources. Ten broader pre-existing source-parity differences remain outside this bounded batch and were not silently rewritten.
- CI/runtime: unavailable; no CI success claimed.
- Commits: canonical `c8a4dbc91bb51dae5aed87fadb083cb24b402e1d`; index `36986485b8c0cffdb29dce4002546b86d26c4f48`; audit `121c04790a61bc2114c0ad4eec5999e8a2eefeb9`; registry `af4e6a177604c007bfa6605bad7472bea32ab11e`; changelog `d577fdafa6b2d19b3b7c4d4e446b4cf6e714d067`; TODO `96e4d72291e59aabf0ffa6fd915f047f84a1cca3`.
- Exact next batch: **Force Shield, Formation!, Freedom Kick, Fruit of the Tree of Might, Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, Galick Gun, Gamma Blaster, Gamma Impact**. Recompute the live stale queue first; do not repeat completed records.


### 2026-09-23 cycle update — P1 Force-through-Gamma Impact skill provenance/mechanics refresh
- Live census before editing: 455 canonical / 455 index / 280 stale / 0 duplicate IDs.
- Bounded batch: Force Shield, Formation!, Freedom Kick, Fruit of the Tree of Might, Full Power Charge, Full Power Destruction, Future Super Saiyan, Galactic Donuts, Galick Cannon, Galick Gun, Gamma Blaster, Gamma Impact.
- Changes: refreshed canonical/index last_verified to 2026-09-23 and refreshed bounded mechanics/provenance notes while preserving existing evidence boundaries.
- Added/registered docs/data/skill-provenance-audit-2026-09-23-force-through-gamma-impact.json and registered it in docs/data/pq-cross-domain-index.json.
- Validation after write: 455 canonical / 455 index / 256 stale / 0 duplicate IDs; all 12 target records have canonical/index parity for last_verified and mechanics notes.
- CI/runtime unavailable; no CI success claimed.
- Exact next batch: Genocide Shell, Giant Storm, Gigantic Breaker, Gigantic Burst, Gigantic Charge, Gigantic Cluster, Gigantic Cross, Gigantic Explosion, Gigantic Meteor, Gigantic Nova, Gigantic Omega, Gigantic Rage. Recompute the live stale queue first.
