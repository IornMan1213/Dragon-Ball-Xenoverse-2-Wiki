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

The canonical layer currently contains **230 records**. This is an enumerated research population, not a claim that the game's full Super Soul catalogue has been completed.

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
| 046 | Kind of human-like, don't you think? | Super 17 Online Raid | Energy Field: -20% damage taken for wearer/allies for 10 sec | Verified |
| 047 | Kicking a Shadow Dragon in the head is not a wise thing to do! | Shadow Dragon raid family | +5% defense baseline; larger defense boost at ≤10% HP; stamina-damage reduction value unresolved | Partially verified |

Exact raid recurrence schedules and drop probabilities are not inferred from these records.


### Complete current raid/event Super Soul presentation index — 2026-09-24

The canonical research layer currently contains **37 raid/event-associated Super Soul records**. This table is a presentation index of those existing canonical records; it does **not** assert current raid availability, recurrence schedules, drop probabilities, or reward guarantees. The canonical layer remains the source of truth for full mechanics and provenance.

| ID | Super Soul | Acquisition type | Acquisition source | Verification |
|---|---|---|---|---|
| super-soul-036 | Buu's reached full power! | Online Raid Quest | Hit / Hit Lite Raid individual reward | verified_secondary |
| super-soul-037 | I'm over 1,000 years old. | Online Raid Quest | Hit / Hit Lite Raid individual reward; also NPC Gogoh after base-game completion | verified_secondary |
| super-soul-038 | My Ki is building... Overflowing... | Online Raid Quest | Broly / Broly Lite Raid | verified_secondary |
| super-soul-039 | I am going to bathe in your blood! | Online Raid Quest | Broly / Broly Lite Raid | verified_secondary |
| super-soul-040 | You fool! Why are you laughing? | Online Raid Quest | An Invitation from Cell Online Raid | verified_secondary |
| super-soul-041 | Not on my watch! | Online Raid Quest | Hercule Online Raid / individual performance reward | verified_secondary |
| super-soul-042 | Over here, you idiot... | Online Raid Quest | The Power of the Mask / Masked Saiyan Online Raid | verified_secondary |
| super-soul-043 | Bye-bye, universe! | Online Raid Quest | Demented Deity Online Raid / anniversary individual performance reward | verified_secondary |
| super-soul-044 | Let's see you handle THIS kind of power! | Online Raid Quest | Great Ape Baby Online Raid | verified |
| super-soul-045 | Your time in this fight ends now! | Online Raid Quest | Saibaman / Great Ape Baby Lite Online Raids | verified |
| super-soul-046 | Kind of human-like, don't you think? | Online Raid Quest | Super 17 Online Raid | verified |
| super-soul-047 | Kicking a Shadow Dragon in the head is not a wise thing to do! | Online Raid Quest | Shadow Dragon / Heartless Galactic Warrior raid family | partially_verified |
| super-soul-052 | Why are you dodging?! | Raid Quest | Limited-time Raid Quest event reward; community records the Transforming Bardock raid damage-milestone track | partially_verified |
| super-soul-054 | Leave my daddy alone! | Raid Quest | Limited-time Raid Quest event reward; community records the Supervillain Perfect Cell raid | verified_secondary |
| super-soul-057 | Can I attack now? | Raid Quest | Limited-time Raid Quest Event Reward; community records the Majin Buu (Gohan Absorbed) raid | verified_secondary |
| super-soul-058 | Now I'm MAD! | Raid Quest | Limited-time Raid Quest Event Reward; community records the Dabura raid | verified_secondary |
| super-soul-063 | Zudodoeyaahh! | Raid Quest | Limited-time Raid Quest Event Reward; community records the True Terror in Saiyan Form / DBS Broly raid | verified_secondary |
| super-soul-074 | Goku! Time for dinner! | Raid Quest Event | Raid Quest Event Reward — Limited-Time | verified_secondary |
| super-soul-082 | Let's get round two started! | Raid Quest Event | Raid Quest Event Reward — Limited-Time | verified_secondary |
| super-soul-083 | I can finally get my hands dirty again. | Raid Quest Event | Raid Quest Event Reward — Limited-Time | verified_secondary |
| super-soul-092 | I think I'm finally warmed up now! | Raid Quest Event | Raid Quest Event Reward — Limited-Time | verified_secondary |
| super-soul-094 | Your energy is now mine to wield. | Raid Quest Event | Raid Quest Event Reward — Limited-Time | verified_secondary |
| super-soul-095 | I've got something extra special for you! | Raid Quest Event | Raid Quest Event Reward — Limited-Time | verified_secondary |
| super-soul-096 | It must be some kind of trick... | Raid Quest Event | Hercule Online Raid | verified_secondary |
| super-soul-097 | It all comes down to this! | Raid Quest Event | Transforming Goku (GT) Online Raid | verified_secondary |
| super-soul-103 | Emoc htorf! Peas and Carrots! | Raid Quest Event | Dyspo Online Raid | verified_secondary |
| super-soul-104 | Looks like I mixed up the capsules... | Raid Quest Event | Transforming Majin Buu Online Raid | verified_secondary |
| super-soul-111 | I can tell you're an amateur by the way you pose! | Raid Quest Event | Gamma 2 Online Raid | verified_secondary |
| super-soul-112 | That's minus ten points! | Raid Quest Event | Super 17 Online Raid | verified_secondary |
| super-soul-115 | Help me, Daddy! I'm scared! | Raid Quest Event | Transforming Cooler Online Raid | verified_secondary |
| super-soul-116 | Damn... Gonna have to go all out! | Raid Quest Event | Cell Max Online Raid | verified_secondary |
| super-soul-117 | Not a single word! | Raid Quest Event | Android 13 Online Raid | verified_secondary |
| super-soul-127 | That's a dead ball now, right? | Raid Quest Event | Gohan (Future) Online Raid | verified_secondary |
| super-soul-128 | Nothing beats flying! | Raid Quest Event | Transforming Gogeta (DB Super) Online Raid | verified_secondary |
| super-soul-129 | There was actually five of me! | Raid Quest Event | Ginyu Force Online Raid | verified_secondary |
| super-soul-135 | I learned a lot from how you fight. | Limited Time Event | Limited Time Event Reward | verified_secondary |
| super-soul-136 | You intend to defy me?! | Raid Quest Event | Broly (Restrained) Online Raid | verified_secondary |

This index is now complete at **37/37** raid/event canonical names surfaced. The earlier **12/37** result is retained in the dated audit history; this current presentation table does not upgrade evidence status or invent route details.
