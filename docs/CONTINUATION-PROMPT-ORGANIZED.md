

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
