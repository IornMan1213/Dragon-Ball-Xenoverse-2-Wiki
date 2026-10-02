---
layout: wiki
title: Super Souls Database
---

# Super Souls Database

A structured catalogue of Super Souls, their triggers, effects, Limit Bursts, acquisition routes, and research status.

> **Research standard:** this database distinguishes cataloguing from verification. Unknown drop rates, trigger timing, stacking behavior, shop rotation details, and version-sensitive behavior are left unresolved rather than guessed.

## What a Super Soul is

Super Souls are equippable effects that modify combat behavior or other gameplay systems under defined conditions. The catalogue spans Parallel Quests, Item Shop and TP/STP Medal Shop rotations, NPC rewards, the Mixing Shop, Expert Missions, raids, story content, and other game systems.

Only one Super Soul can be equipped at a time on a preset. Because copies are shared across CaC slots, a soul already equipped on another character or saved preset can affect whether another CaC can equip it.

## Research fields

| Field | Purpose |
|---|---|
| **Name** | Exact in-game Super Soul name |
| **Character source** | Character associated with the soul, when documented |
| **Acquisition** | PQ, shop, NPC, raid, Expert Mission, story, Mix Shop, etc. |
| **Trigger** | Exact activation condition |
| **Effect** | Human-readable effect description |
| **Magnitude** | Numeric value where independently documented |
| **Duration** | Temporary duration, if applicable |
| **Stacking** | Whether and how the effect can stack |
| **Limit Burst** | Burst type and documented effects |
| **CaC availability** | Whether Player Created Characters can equip it |
| **DLC** | Required paid DLC or other content dependency |
| **Version notes** | Changes, exceptions, or unresolved version differences |
| **Verification** | `indexed`, `partially_verified`, or `verified` |

## Current structured catalogue

The machine-readable source of truth is `docs/data/super-souls-record-layer.json`.

The canonical layer currently contains **42 populated records** (18 initial records plus the eight promoted records from research batch 03). This is an enumerated research population, not a claim that the game's full Super Soul catalogue has been completed.

### Canonical records

The initial canonical population covers the first 18 research records, including PQ, Item Shop, TP/STP Shop, and NPC acquisition families. All remain `partially_verified` until acquisition details and important mechanics are sufficiently reconciled.

### Staged research batch 03

The next eight records have now been researched and staged in `docs/data/super-souls-research-batch-03.json`. These eight records were promoted into the canonical layer on 2026-09-19 after duplicate, schema, acquisition, and independent-source reconciliation. Exact current shop rotation timing and unresolved drop-rate behavior remain intentionally unclaimed.

| Staged ID | Super Soul | Source | Acquisition | Status |
|---|---|---|---|---|
| 024 | I'm the fastest in the universe | Burter | Item Shop | Verified |
| 025 | We're the one and only Ginyu Force! | Jeice | Item Shop | Verified |
| 026 | Let me show you how it's done. | Ginyu | Item Shop | Verified |
| 027 | I must protect Grand Elder Guru! | Nail | Item Shop | Verified |
| 028 | Popporunga pupirittparo | Dende | NPC Sasana | Verified |
| 029 | The ultimate power is mine! | Piccolo | Mixing Shop / DLC provenance | Verified |
| 030 | I'll never forgive you, scum! | Frieza (1st Form) | Item Shop | Verified |
| 031 | Drop dead!!! | Gohan (Kid) | PQ28 | Verified |

The staged batch follows the game's catalogue ordering for this research pass; its IDs are research identifiers and do not overwrite the canonical layer's existing IDs.

## Verification policy

A record may be promoted to **verified** only when its core identity, acquisition route, and important mechanics are reconciled against sufficient independent evidence. Verification does not mean every community measurement or historical interaction has been exhaustively reproduced.

`partially_verified` means meaningful information has been checked, but one or more important fields remain source-dependent or unresolved.

`indexed` means the soul has been catalogued or discovered, but substantial research remains.

## Acquisition coverage

The catalogue must eventually account for Parallel Quests, Item Shop purchases, TP/STP Medal Shop rotations, Mixing Shop recipes, Conton City/NPC rewards, Expert Missions, raids/events, story/progression rewards, DLC-specific content, and version-sensitive acquisition paths.

## DLC provenance

DLC ownership and in-game acquisition are stored separately. A DLC can introduce a Super Soul while the soul itself may be obtained through a PQ or another in-game route after the relevant content is available. DLC provenance should never be used as a substitute for an acquisition condition.

## Research priorities

- Continue expanding the canonical layer after schema, duplicate, acquisition, and source reconciliation passes. Batch 03 (IDs 024–031) has completed this promotion gate.
- Populate the remaining base-game catalogue.
- Reconcile acquisition and effects against independent references.
- Inventory DLC-specific Super Souls by DLC family.
- Track TP/STP Shop rotation requirements separately from ownership requirements.
- Add Expert Mission, raid, event, NPC, and Mixing Shop sources.
- Record exact Limit Burst behavior where evidence supports it.
- Preserve historical/version differences instead of silently overwriting them.
- Cross-link souls to skills, Awoken Skills, characters, PQs, DLC, and build-relevant mechanics.

## Source policy

External references are evidence, not text to copy blindly. The current research layer uses the Xenoverse 2 Wiki Super Soul index, independent Super Soul guides, the Madreag research corpus, historical GameFAQs research, and official Bandai Namco DLC documentation.

**Repository rule:** internal web-tool citation markers must never be committed to wiki files. Repository pages use ordinary source URLs or repository references instead.


### FUTURE SAGA Chapter 4 additions — 2026-09-19

Four Chapter 4 Super Souls are now indexed in the canonical layer (records 032–035). Official DLC material establishes that Chapter 4 adds four new Super Souls, while PQ 185/186 reward inventories provide the acquisition leads. Community testing supplies secondary effect evidence for three; those mechanics remain explicitly marked as partially verified rather than presented as official item-level values.

| ID | Super Soul | Acquisition lead | Verification |
|---|---|---|---|
| 032 | This power... It's different from any I've ever had. | PQ 185 | Partially verified |
| 033 | Malice... Existence... Cruelty... | PQ 185 | Partially verified |
| 034 | The final battle begins now. | PQ 186 | Partially verified |
| 035 | I'll use this power to protect everyone! | PQ 186 | Partially verified |


### Raid / event additions — 2026-09-19

Four raid-associated Super Souls are now represented in the canonical layer (036–039). Their acquisition families and secondary effect evidence have been reconciled without inventing drop rates or recurrence schedules.

| ID | Super Soul | Acquisition family | Verification |
|---|---|---|---|
| 036 | Buu's reached full power! | Hit / Hit Lite Raid | Verified secondary |
| 037 | I'm over 1,000 years old. | Hit / Hit Lite Raid; NPC Gogoh | Verified secondary |
| 038 | My Ki is building... Overflowing... | Broly / Broly Lite Raid | Verified secondary |
| 039 | I am going to bathe in your blood! | Broly / Broly Lite Raid | Verified secondary |

The Hit raid evidence also preserves a documented discrepancy for record 036 rather than silently choosing between conflicting percentage values.

### Additional raid/event additions — 2026-09-19

Four more raid-associated records have been reconciled into the canonical layer (040–043):

| ID | Super Soul | Raid family | Verification |
|---|---|---|---|
| 040 | You fool! Why are you laughing? | Cell / An Invitation from Cell | Verified secondary |
| 041 | Not on my watch! | Hercule / Humanity's Greatest Threat | Verified secondary |
| 042 | Over here, you idiot... | Masked Saiyan / The Power of the Mask | Verified secondary |
| 043 | Bye-bye, universe! | Fused Zamasu / Demented Deity | Verified secondary |

The canonical layer retains unresolved numerical damage details for 043 instead of converting community testing into a false exact value.

### Raid-exclusive candidates indexed — 2026-09-19

Records 044–047 have now undergone item-level reconciliation. Three have verified core effects; 047 remains partially verified because its stamina-damage reduction value and historical raid mapping are not sufficiently established.

| ID | Super Soul | Acquisition | Core effect | Status |
|---|---|---|---|---|
| 044 | Let's see you handle THIS kind of power! | Great Ape Baby Online Raid | Giant Form: +15% all attacks and passive stamina auto-recovery | Verified |
| 045 | Your time in this fight ends now! | Saibaman / Great Ape Baby Lite raids | Instant Transmission restores Ki; catalog lists +100 Ki | Verified |
| 046 | Kind of human-like, don't you think? | Super 17 Online Raid — official 15,000-damage individual target tier | Energy Field: -20% damage taken for wearer/allies for 10 sec; Limit Burst: Revive Gauge Auto-Recovery! | Verified |
| 047 | Kicking a Shadow Dragon in the head is not a wise thing to do! | Shadow Dragon raid family | +5% defense baseline; larger defense boost at ≤10% HP; stamina-damage reduction value unresolved | Partially verified |
| 049 | Getting beat up makes me cranky... | Parallel Quest 44 | +5% Ki auto-recovery; +15% Ki Blast-based attacks at max Stamina; Rush Limit Burst | Verified |
| 050 | I'll use all my strength to kill you... | Parallel Quest 29 — The Androids Attack | +5% Ki auto-recovery; +10% normal attacks at max Ki; Power Limit Burst | Verified |
| 051 | Before creation comes ruin... | Parallel Quest 63 — Appetite for Destruction | +20% Ki Blast Skills after about 30 seconds; Rush Limit Burst | Verified |
| 052 | Janemba! Janemba! | Parallel Quest 64 — Beerus the Impulsive | +60 Ki on successful Just Guard; +10% Ki Blast Skills for 10 seconds; Auto Just Guard | Verified |
| 048 | Set your rage free... | Parallel Quest 42 — Artificial Warriors | -5% ally revival time; +100% Ki on KO; Limit Burst: Auto Health and Stamina Recovery!; DEF Down. | Verified |

Exact raid recurrence schedules and drop probabilities are not inferred from these records.


### Super Souls 110–114 — 2026-10-02 verification

The canonical records for Super Souls 110–114 were rechecked against the current Super Soul catalogue plus independent guide/DLC evidence. The canonical acquisition routes remain PQ132 for 110–112 and PQ133 for 113–114.

| ID | Super Soul | Character | Acquisition | Core verified mechanics | Status |
|---|---|---|---|---|---|
| 110 | Whoa, it's freezing here! | Goku | PQ132 | Battle start: self-inflicted freeze/ice status; +15% all attacks for 30 seconds | Verified |
| 111 | This is no time to mess around... | Vegeta | PQ132 | 30 seconds after battle start: prevents Ki depletion for 15 seconds and cures status ailments | Verified |
| 112 | I can't have you dying on me! | Chirai | PQ132 | Ally KO: +15% movement speed and -50% revive time for 10 seconds | Verified |
| 113 | Here it comes! | Rozie | PQ133 | Charged Ki Blast hit: +10% normal attacks and +10% normal Ki Blasts; both stack up to 3 times | Verified |
| 114 | I got my claws in you, and fangs too! | Kakunsa | PQ133 | Charged attack hit: +15% Strike Skills and +10% movement speed; both stack up to 2 times | Verified |

The pass does not infer exact reward probabilities, hidden frame/tick behavior, or undocumented stacking interactions beyond the documented stack limits.


### Super Souls 115–120 — 2026-10-02 verification

Records 115–120 were rechecked against the current Super Soul catalogue and independent Parallel Quest/stat-sheet evidence. Their canonical acquisition routes remain PQ134–137.

| ID | Super Soul | Character | Acquisition | Verified mechanics |
|---|---|---|---|---|
| 115 | Power! A lotta power! It's great! | Whis | PQ134 | +50% maximum Ki and +50% maximum Stamina; Power Limit Burst |
| 116 | That won't work on me! | Ribrianne | PQ135 | Once after Ultimate Attack hit: -50% damage taken for 10 sec; Hearts Ki Blast type |
| 117 | Pathetic | Vegeta (Super Saiyan God) | PQ136 | Blazing Attack trigger; +10% Strike, +10% Ki Blast-based skills, +10% Ki restored; 3-stack cap |
| 118 | Justice is nothing to me now. | Toppo | PQ136 | Below 50% HP: +20% all attacks, -15% damage taken, +10% Stamina recovery; guard sealed |
| 119 | This is everything I've got! | SSGSS Vegeta (Evolved) | PQ137 | Once on SSGSS (Evolved): +60% Ki auto-recovery for 30 sec |
| 120 | That heat... I'll have to match it. | Jiren | PQ137 | Once after Ultimate Attack hit: +15% all attacks, -10% damage taken, +10% movement, +10% Ki restored, +10% Stamina recovery |

No unsupported drop probabilities or hidden frame/tick behavior were added.


### Super Souls 121–126 — 2026-10-02 verification

Records 121–126 were rechecked against the current Super Soul catalogue and independent PQ reward/stat-sheet evidence. PQ reward evidence confirms 121/122 in PQ138, 123/124 in PQ140, and 125/126 in PQ141. 

| ID | Super Soul | Character | Acquisition | Verified mechanics |
|---|---|---|---|---|
| 121 | I'm not gonna die until I defeat you! | Majuub | PQ138 / PQ151 | KO: revive at 1 HP, nullify damage 10 sec, +15% normal attacks |
| 122 | I just flew around the whole world! | Pan (Kid) | PQ138 | Always +10% movement speed and +5% Stamina recovery |
| 123 | This thing carries hopes of everyone on Earth! | Goku (GT) | PQ140 | Super Spirit Bomb: +15% Ki Blast attacks for 15 sec; +1.2% HP/sec during the attack |
| 124 | Now then, time for another delightful hunt! | Android 21 | PQ140 | Start: -15% enemy Stamina/-10% enemy attacks; after 30 sec: -50% enemy Ki/+10% damage taken by enemies |
| 125 | D-Don't talk bad about my family! | Uub (Kid) | PQ141 | Below 50% HP: +10% normal melee/Strike; below 25%: +15% to both |
| 126 | This oughta make things interesting. | Broly | PQ141 | Opponent Reinforcement Skill: +10% all attacks, stacking to 10 times |

Documented catalogue/data discrepancies remain preserved; no unsupported drop probabilities were added.


### Super Souls 127-132 — 2026-10-02 verification

Records 127-132 were rechecked against the Super Soul catalogue and independent Parallel Quest reward evidence.

| ID | Super Soul | Character | Acquisition | Verified mechanics |
|---|---|---|---|---|
| 127 | I don't want them to get hurt! | Gine (DB Super) | PQ142 | Ally KO: +50% Ki/Stamina Auto-Recovery for 20 sec |
| 128 | This is as far as you go. | Pikkon | PQ143 | Full Ki: force enemies to target you for 3 sec; Just Guard restores 50 Ki |
| 129 | You've awakened my true power... | Zarbon | PQ144 | Always +20% recovery effect; Awoken Skill: +5% all abilities while active |
| 130 | I won't forgive those who best my comrades! | Kahseral | PQ144 | Ally KO: +50% Stamina/Ki Auto-Recovery for 20 sec |
| 131 | I've cast aside everything for this! | Toppo (God of Destruction) | PQ145 | Always +35% all attacks, with documented +10% damage taken and recovery/mobility penalties |
| 132 | There's no way you can hit me! | Dyspo | PQ146 | Evasive Skill: +25% movement speed and +30% Stamina Auto-Recovery for 15 sec |

Canonical acquisition remains authoritative; no unsupported reward probabilities were added. Documented wording/data nuances are retained rather than silently normalized.


### Super Souls 133-136 — 2026-10-02 verification

Records 133-136 were rechecked against current catalogue/character evidence and independent Parallel Quest evidence. The broader DLC/PQ documentation confirms the surrounding Legendary Pack quest sequence and its Super Soul rewards. 

| ID | Super Soul | Character | Acquisition | Verified mechanics |
|---|---|---|---|---|
| 133 | It's just me and you now! | Caulifla (Super Saiyan 2) | PQ147 | Once on locking onto an enemy: +15% listed abilities and +20% Ki recovery; lock-on state is temporarily affected |
| 134 | My back's getting tingly...! | Kale (Super Saiyan 2) | PQ148 | Charge skill: +5% all attacks and +120% Ki Auto-Recovery for 5 sec |
| 135 | Our two strengths aren't just added together. | Gogeta (DB Super) | PQ149 | Always activates Ki Auto-Recovery and boosts Stamina recovery speed by 5% |
| 136 | I will prevail, no matter the cost! | Jiren (Full Power) | PQ150 | More Ki than opponent: +15% all attacks; less Ki: +10% Ki Auto-Recovery |

No unsupported drop probabilities were added. Super Soul 137 was deliberately left partially verified because its canonical identity has a documented naming discrepancy against current external catalogue evidence.


### Super Soul 137 — 2026-10-02 identity resolution

Super Soul 137 is now verified. The canonical repository label is **"I'll never forgive you!"**; current external item-level catalogue evidence identifies the same Frieza (1st Form) Soul as **"I'll never forgive you, scum!"**. The identity, Item Shop acquisition, guard-break trigger, and Limit Burst align. The external naming suffix is retained as a documented variant rather than replacing the canonical label. Current catalogue evidence gives **-20% damage received from all attacks for 4 seconds** after guard break. 


### Super Souls 185–186 — 2026-10-02 verification

Records 185–186 were promoted into the canonical record layer after direct reconciliation against current Super Soul catalogue evidence and independent player-facing references. Both are TP Medal Shop/STP Medal Shop endpoints rather than Parallel Quest rewards.

| ID | Super Soul | Character | Acquisition | Verified mechanics |
|---|---|---|---|---|
| 185 | I said don't go easy on me! | Super Saiyan 2 Gohan (Teen) | TP Medal Shop / STP Medal Shop | Ultimate Attack: +25% Ultimate Attack damage; -40% Ki recovery penalty; Power Limit Burst |
| 186 | You irritating little pests! | Frieza (1st Form) | TP Medal Shop / STP Medal Shop | Super Attack: +20% Super Attack damage; Race Default Ki Blast type; standard ATK Up/Ki Auto-Recovery/Stamina Recovery Speed Down Limit Burst |

No shop rotation schedule, hidden frame/tick behavior, or undocumented probability was inferred.
