

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


### 2026-09-22 cycle update — PQ reference/index consumer reconciliation
- [x] Reconciled the general PQ reference/index consumers against the canonical 860-edge relationship layer and 186-record PQ layer.
- [x] Corrected PQ farming presentation to the canonical route set: PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88.
- [x] Preserved PQ36 numbering conflicts as provenance/history rather than replacing the canonical player-facing record layer.
- [x] No canonical relationship edges were changed.
- [ ] Exact next task: search remaining PQ-facing consumers for stale canonical-count, farming-route, or external-corpus claims and repair deterministic presentation drift.

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
- [x] Completed and registered the deterministic PQ reference/index repair: docs/Parallel-Quests.md now uses the complete canonical farming set **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, PQ88**; validator/audit added and cross-domain index registration completed.
- [x] Current canonical relationship baseline remains **860 edges** (244 skill / 151 Super Soul / 125 equipment / 247 character / 86 DLC / 7 farming) across **186 PQ records**.
- [x] No canonical relationship identities were added, removed, or renamed.
- [ ] Next continuation gate remains the latest acquisition-metadata task: reconcile skill source_quest, source_quest_or_shop, and unlock_method against canonical PQ associations without promoting research-layer reward-trigger assumptions into canonical facts.


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


### 2026-09-22 cycle update — equipment detail enrichment equip-031–040
- [x] Enriched 10 equipment/accessory records with source-backed category and slot coverage while preserving unresolved reward/drop/stat mechanics.
- [x] Added and registered `docs/data/equipment/equipment-031-040-detail-audit.json`.
- [x] Live validation: 139 equipment records, 174 combined equipment/accessory records, 0 duplicate IDs, 125 equipment edges / 123 unique targets / 0 unresolved / 0 broken.
- [ ] Exact next batch: enrich `equip-041`–`equip-050` with independently verified category/slot, restrictions/effects, and DLC provenance.


### 2026-09-22 cycle update — equipment detail enrichment equip-041–050
- [x] Enriched equip-041–050 across both equipment layers with source-backed category, slot coverage, restrictions, and existing DLC/PQ provenance.
- [x] Added `docs/data/equipment/equipment-041-050-detail-audit.json` and registered it in the cross-domain index.
- [x] Validation: 139 equipment records / 174 combined records / 0 duplicate IDs; canonical equipment graph remains 125 edges / 123 targets; all 10 batch relationships are source-backed with 0 unresolved/broken endpoints.
- [ ] Exact next batch: enrich equip-051–060 with the same evidence and parity workflow.


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
- [x] Reference-page consumer is aligned: **186** canonical PQ records, **860** relationship edges, farming set **PQ15/PQ22/PQ44/PQ45/PQ68/PQ83/PQ88**, and a live explorer link; no stale PQ13 farming shorthand remains.
- [x] Reward explorer consumer is aligned: **244 skills / 151 Super Souls / 125 equipment / 86 DLC edges**, zero unresolved canonical reward/DLC targets, and structured reward parity **244/244, 151/151, 125/125**.
- [x] Character explorer consumer is aligned: **247 character edges**, **75 unique canonical character targets**, **143 source PQs**, zero missing targets, and zero invalid PQ IDs.
- [x] Refreshed the three presentation audit files with current validator references/date and live counts; strengthened `scripts/validate_pq_reference_pages.py` with an explicit live-explorer-link contract.
- [x] No relationship identities or target aliases were added/removed; historical/evidence boundaries remain preserved.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `433d37d44c34cbe4128cbb93f298fd33cdb1070e`, `346b275ac4d5fc792ab127daea3ec6b68cf095e8`, `9ebd2c4aa34ad981e0259ba21dd5be6201d76647`, `08f0c633c7f65203c6d1178a9432480f52647097`.
- [ ] Exact next task: audit `scripts/validate_skills_pq_reverse_navigation.py` / `docs/data/skill-pq-acquisition-presentation-audit.json` and `scripts/validate_record_reverse_pq_navigation.py` / `docs/data/record-reverse-pq-navigation-audit.json` against canonical PQ relationships and live target records; repair deterministic reverse-link drift only.


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
\n### 2026-09-22 cycle update — general PQ reference identity-contract hardening
- [x] Hardened `scripts/validate_pq_reference_pages.py` to enforce exact PQ numbers **1–186**, unique PQ IDs, known relationship types, and unique canonical `(relationship,PQ,target)` keys.
- [x] Refreshed `docs/data/pq-reference-page-audit.json` to schema 1.1.0; current validation remains clean.
- [x] No canonical relationship or identity data changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `8a256fb4e2998c12a0f29b42a637acbdc93ff5c4`, `8bf3f109e1ec3249f43f6daf9978d58d2198a4db`.
- [ ] Exact next batch: inspect remaining PQ-facing search/landing consumers and cross-domain index registry for deterministic duplicated counts or one-way navigation gaps.


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
- [x] Hardened `scripts/validate_pq_reverse_indexes.py` with explicit duplicate-pair detection for standalone normalized maps/reverse projections.
- [x] Added exact canonical reward-domain parity for the unified projection: **520/520 pairs** across Skills, Super Souls, and Equipment, with **0 missing / 0 extra / 0 duplicate pairs**.
- [x] Refreshed `docs/data/pq-reward-normalization/pq-unified-reverse-index-audit.json` to schema **1.1.0**.
- [x] Preserved source-layer drift as informational; no canonical relationships or source rewards were changed.
- [ ] CI: no successful GitHub Actions status exposed; CI success not claimed.
- [x] Commits: `46f7dcdc4a87e5997d02b817d6f4d20046f285df`, `5cd22060600e245262eb87ee993c1d34bc7ee009`, `c9cf3614b86fc306ab24628d2e42e85deb0a2b5b`.
- [ ] Exact next batch: inspect the next registered cross-domain presentation consumer for stale scalar/list assumptions or one-way canonical navigation.


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
- [x] Live validation: **149/149 canonical character names unique; 15/15 DLC-character bridge records; 0 resolved bridge targets missing; 0 unresolved bridge records with a target; 0 duplicate bridge source labels**.
- [x] DLC identity validation: **86 canonical PQ→DLC edges / 20 unique targets / 20 identity records / 0 missing targets / 0 orphan identities / 0 duplicate IDs / 0 duplicate names**.
- [x] Published Character/DLC local navigation remains clean; all checked links resolve to repository-local artifacts.
- [x] Refreshed docs/data/characters/published-character-dlc-navigation-audit.json to schema **1.1.0**.
- [x] No canonical character, DLC, PQ relationship, or provenance identity was changed. The two explicitly unresolved Chapter 4 character source labels remain unresolved.
- [ ] CI: no successful GitHub Actions workflow run exposed for commit 120cc346f9b7e049d2785e25eed9d1e5b1bd27cf; CI success not claimed.
- [x] Commits: ec4782b3ad6610f6fc681b492a73f138d208e725, 120cc346f9b7e049d2785e25eed9d1e5b1bd27cf.
- [x] Live census after editing: **860 canonical PQ relationship edges = 244 skills / 151 Super Souls / 125 equipment / 247 characters / 86 DLC / 7 farming**.
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
- [x] Audited the published Search surface: `docs/Search.md`, `docs/assets/search.js`, and `docs/search-data.html`.
- [x] Added `scripts/validate_search_consumer.py` enforcing the Search permalink/hooks, `?q=` navigation contract, local generated search-index fetch, live input listener, and zero external fetch endpoints.
- [x] Added `docs/data/search-consumer-audit.json` and registered it plus the validator in `docs/data/pq-cross-domain-index.json`.
- [x] Static live-source result: required Search hooks and query/navigation contracts are present; the search-data producer uses the local `site.pages` corpus and excludes itself; Search JS contains **0 external fetch endpoints**.
- [x] Evidence boundary: presentation wiring only; no claim of exhaustive search ranking/content materialization.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: validator `d0b319c5974c9a6861bff364136f6b2deaad0a0b`; audit `99474ac1c291d4c49b85cd6ce2d1c853f9d63440`; registry `c041e968d72fe23d54c778d42e73b0d40bf9b21d`; TODO `634c62bb8c90358f9026fc55b2fb6a99ca10074d`; handoff `8189b490cf28d3b149971d48fb7c74fc94c610f3`.
- [ ] Exact next task: inspect the next registered Search/landing consumer or unvalidated cross-domain producer for deterministic one-way navigation, stale scalar/list assumptions, or canonical endpoint drift; prefer exact local consumer parity and do not infer new relationships.

### 2026-09-22 cycle update — Equipment provenance batch `equip-081`–`equip-090`
- [x] Live equipment/accessory endpoint census: **174 canonical identities / 0 duplicate IDs / 125 PQ→equipment edges / 123 unique targets / 0 broken endpoints**.
- [x] Enriched `equip-081`, `082`, `083`, `084`, `086`, `087`, `089`, and `090` with maintained catalog provenance and slot coverage.
- [x] Preserved `equip-088` as a normalized historical alias to `acc-012`; `equip-085` remains absent and was not fabricated.
- [x] Added `docs/data/equipment/equipment-081-090-detail-audit.json`.
- [x] Validation: **174/174 endpoints resolved; 0 duplicate IDs; 125 forward; 123 reverse; 0 broken**.
- [ ] CI: no successful workflow/check exposed; CI success not claimed.
- [x] Commits: canonical `1b2f96e444c1f0ce17174cba4d4d95841ae671cd`; audit `007c9a768edd1483583cec7336b2f7537366922a`; TODO `93e4ff79cc11b260fbe039ad355eef9adee89a86`; handoff `abb34842d07901192c89c1e47017feb52c54f469`.
- [ ] Exact next task: fresh census, then enrich **`equip-091`–`equip-100`**, preserving canonical accessory bridges and normalized aliases.

### 2026-09-22 cycle update — Equipment detail enrichment `equip-091`–`equip-100`
- [x] Fresh census: **174 combined equipment/accessory records / 139 legacy equipment records / 0 duplicate IDs / 125 forward PQ→equipment edges / 123 unique targets / 0 broken endpoints**.
- [x] Enriched legacy `equip-091`–`equip-100`; preserved canonical bridges `equip-091→acc-058` and `equip-093→acc-070`.
- [x] Added category/slot/DLC provenance for the eight non-aliased endpoints and recorded the evidence boundary.
- [x] Added `docs/data/equipment/equipment-091-100-detail-audit.json` and registered it.
- [x] Validation clean; CI status unavailable/no success claimed.
- [x] Commits: `267cb0dcd98b9c5b8307e0d0f1ca5ac4b3da65cb`, `af70f83339d32794fa6c577ebfadc97850bd0f62`, `87b75353add617b60607c476dacb3442dc95ba3b`, `bb005ca06da404f9027bf18148e6204f4b72cfe3`, TODO `660fb46d05ba6192d315cf1755e2b12ae4dad661`, handoff `f97fbca4878cd220633d2964b3799ed8330bb87e`.
- [ ] Exact next task: fresh census, then **`equip-101`–`equip-110`**.

### 2026-09-22 cycle update — Equipment detail enrichment `equip-101`–`equip-110`
- [x] Enriched `equip-101`–`equip-110` with source-backed category/slot/DLC metadata.
- [x] Reconciled DAIMA Pack provenance for `101–105` and Future Saga Chapter 3 for `106–110`.
- [x] Added/registered `docs/data/equipment/equipment-101-110-detail-audit.json`.
- [x] Validation clean: **174 combined records / 0 duplicate IDs / 125 forward / 123 reverse / 0 broken endpoints**; all 10 batch records classified with slot coverage.
- [x] CI unavailable; no success claimed.
- [x] Commits: canonical `34ffe98a4702514806dbe425aba3f38f18804e6d`, combined `9bcf4242481a7d2283e7fe4db7894e923be2c13a`, audit `8bcbb0f4bf6d846b2557c84631851f07599e4af1`, registry `b51aa73512fb62822681a83b8a80af358142f5d2`, TODO `eced4791690df05feae417c6bd1683f062fef101`, handoff `86e808dcbe2713956f5d6f2bed73f6fc7ac36490`.
- [ ] Exact next task: fresh census, then **`equip-111`–`equip-120`**.

### 2026-09-22 cycle update — Equipment detail enrichment `equip-111`–`equip-120`
- [x] Enriched `equip-111`–`equip-120` with source-backed category/slot/DLC metadata.
- [x] Reconciled Future Saga Chapter 4 provenance for `111–115`; retained base-game PQ-era provenance for `116–120`.
- [x] Added/registered `docs/data/equipment/equipment-111-120-detail-audit.json`.
- [x] Validation clean: **174 combined records / 0 duplicate IDs / 125 forward / 123 reverse / 0 broken endpoints**; 10/10 batch records have slot coverage and explicit classification.
- [x] CI unavailable; no success claimed.
- [x] Commits: canonical `55f163ba865fecb908a2f1dc259ea455aafb17cf`, combined `bf0f9087f5ac0d56fc34fa69860717bb3817d3a9`, audit `a8e2b5c6029f45e4f0b9bf0e61d58d21b80b19b8`, registry `0a0194f191171bfff92e201de90a08cfeb6f4500`, TODO `853eeb1f4fb1e91c478a91d67bb53080e3e1f102`, handoff `c9743f7f9465aebd38a50bf8085bf0ebfe906a1b`.
- [ ] Exact next task: fresh census, then **`equip-121`–`equip-130`**.

### 2026-09-22 cycle update — Equipment detail enrichment and identity correction `equip-121`–`equip-130`
- [x] Corrected false equipment endpoint `equip-121` (Mr. Shape Up L): independent evidence identifies it as a consumable capsule/material, so it was removed from the equipment layers while the PQ99 reward remains source-backed in PQ reward data.
- [x] Preserved canonical bridge `equip-123 → acc-063` for SSGSS Vegeta Wig.
- [x] Enriched `equip-122`, `124`–`130` with category/slot/DLC metadata.
- [x] Added/registered `docs/data/equipment/equipment-121-130-detail-audit.json`.
- [x] Validation clean: **173 combined records / 0 duplicates / 124 forward / 122 reverse / 0 broken**.
- [x] CI unavailable; no success claimed.
- [x] Commits: `cea284c71ec7d9e657ca0d675dd3402d28e41f4f`, `4ce040ffa6ce1cb299c747d2a9ccef1a67288696`, `9f6203ef50f15168448fa821c7b9232113776f96`, `a75e1e28f7dbe94f5543b3d2160f6e70fdbf1220`, `93ac07fc9f37120ecec38c9232cb7171ed15965a`, TODO `997861a3c545742d6ff2f5ee32e1f4da09e4f346`, handoff `483fef03e27af4085032aef9ef9cbf851810d127`.
- [ ] Exact next task: fresh census, then **`equip-131`–`equip-140`**.

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
- [x] Completed the next P1 stale-last_verified skill provenance batch: skill-beast.
- [x] Confirmed the existing acquisition route with independent evidence: max friendship with Gohan (Adult) & Videl and Piccolo, followed by Piccolo's special training / Cell Max unlock mission.
- [x] Refreshed canonical/index provenance, added docs/data/skill-beast-provenance-audit-2026-09-22.json, and registered the audit in docs/data/pq-cross-domain-index.json.
- [x] Static validation: 452/452 canonical/index records, 0 duplicate IDs; no semantic skill or PQ relationship changes.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: continue the stale-last_verified P1 skill provenance queue with the next unfinished skill after Beast.


### 2026-09-22 cycle update — Big Bang Knuckle provenance verification
- [x] Completed the next P1 stale-last_verified skill provenance batch: skill-big-bang-knuckle.
- [x] Confirmed PQ172 — "Little Big Brother" as the acquisition endpoint using current dedicated documentation; official Dragon Ball documentation confirms the move/character/DLC context.
- [x] Refreshed canonical/index provenance, added docs/data/skill-big-bang-knuckle-provenance-audit-2026-09-22.json, and registered the audit in docs/data/pq-cross-domain-index.json.
- [x] Preserved existing reward-tier evidence conflict; no canonical reward-tier or probability change.
- [x] Static validation: 452/452 canonical/index records, 0 duplicate IDs.
- [ ] Runtime/CI unavailable; no CI success claimed.
- [ ] Exact next batch: continue with the next unfinished stale-last_verified skill after Big Bang Knuckle.


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
- [x] Independent evidence confirms **Chaos Shot** as a **100-Ki Ki Blast Super** used by Frost and acquired from the **TP Medal Shop**. Official Bandai Namco documentation confirms TP Medals remain earnable and usable in-game after the May 2024 sales transition. citeturn0search4turn0search0turn0search2
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
\n### 2026-09-22 cycle update — Data Input through Death Slicer provenance refresh
- [x] Fresh live census: **452 canonical skills / 452 index records / 0 duplicate IDs / 357 stale before this batch**.
- [x] Refreshed **9** adjacent stale skill records: Data Input, Dead End Rain, Deadly Dance, Death Ball, Death Beam, Death Crasher, Death Psycho Bomb, Death Slash, Death Slicer.
- [x] Synchronized canonical/index `last_verified` and shared identity/classification fields for all 9.
- [x] Added current evidence-backed mechanics/provenance details; preserved acquisition semantics and uncertainty boundaries.
- [x] Corrected **Death Slash** from Strike to **Ki Blast Super** in canonical/index `subcategory` and `damage_type`, based on current dedicated Xenoverse 2 evidence.
- [x] Static validation: **452/452**, **0 duplicate IDs**, **351 stale remaining**, all 9 targets refreshed and canonical/index parity clean.
- [ ] CI/runtime execution remains unavailable; no CI success claimed.
- [ ] Exact next batch: recompute census and continue alphabetically with **Demon Flash Strike** and adjacent stale records.\n

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
- [x] Refreshed canonical/index last_verified to **2026-09-22** and registered docs/data/skill-elite-through-energy-provenance-audit-2026-09-22.json.
- [x] Corrected **Emperor's Blast** mechanics association to Golden Frieza and **Emperor's Death Beam** ki_cost from 300 to 400; preserved documented acquisition conflicts for Emperor's Cannon and Energy Barrier.
- [x] Static validation passed: **452/452**, **0 duplicate IDs**, **10/10** audit records, **0 audited canonical/index mismatches**, **298 stale** remaining. Runtime/CI success is not claimed.
- [ ] Exact next batch: recompute the live stale census and continue alphabetically with **Emperor's Death Beam, Emperor's Edge, Endless Shoot, Energy Barrier, Energy Charge, Energy Dome, Energy Field, Energy Minefield**, then adjacent stale records where evidence remains bounded.



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
