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

## Effect notation

Community references commonly use letter tiers for effect magnitude. The current catalogue describes S/M/L/XL as generally corresponding to 5/10/15/20 percent, while XXL can vary. These tiers are treated as reference notation, not a substitute for an exact numeric value when one is documented.

## Trigger categories

The structured catalogue separates triggers instead of reducing every soul to a generic damage bonus.

- **Always** — active while equipped.
- **Battle start** — activates when the battle begins.
- **HP threshold** — activates at a specified HP condition.
- **Ki threshold** — activates at a specified Ki condition.
- **Stamina threshold** — activates at a specified stamina condition.
- **Awoken activation** — reacts to a particular transformation.
- **Skill activation** — reacts to using a defined skill category or skill.
- **KO / revive** — reacts to the user or another combatant being KO'd or revived.
- **Just Guard** — reacts to a successful Just Guard.
- **Charged Ki Blast** — reacts to a charged Ki Blast connecting.
- **Reinforcement activation** — reacts to an active reinforcement skill.

## Acquisition coverage

The catalogue must eventually account for every documented acquisition route, including:

1. Parallel Quest reward tables.
2. Item Shop purchases.
3. TP Medal Shop and STP Medal Shop rotations.
4. Mixing Shop recipes.
5. Conton City and NPC rewards.
6. Expert Mission rewards.
7. Raid and event rewards.
8. Story and progression rewards.
9. DLC-specific PQ and system rewards.
10. Special or version-sensitive acquisition paths.

Current references confirm that Super Souls span multiple acquisition systems rather than being limited to PQs.

## Current structured catalogue

The machine-readable source of truth is `docs/data/super-souls-record-layer.json`.

The first research batch contains 10 canonical records. The project intentionally does **not** treat those 10 records as the complete Super Soul catalogue.

### Initial records

| ID | Super Soul | Source | Acquisition | Status |
|---|---|---|---|---|
| 001 | Hee Hee Sunglasses | Kid Goku | Item Shop | Partially verified |
| 002 | Flying Nimbus!! | Goku | PQ02 | Partially verified |
| 003 | Haaaaaaaaaaaah!! | Tien | TP/STP Medal Shop | Partially verified |
| 004 | Your death is imminent! | Piccolo | PQ05 | Partially verified |
| 005 | Your power is 5? ...Scum. | Raditz | Item Shop | Partially verified |
| 006 | Get lost before I send you flying. | Yamcha | Item Shop | Partially verified |
| 007 | Gyau!!!! | Saibaman | PQ07 | Partially verified |
| 008 | Tien, please don't die | Chiaotzu | Item Shop | Partially verified |
| 009 | You cocky little...! | Nappa | Acquisition unresolved | Partially verified |
| 010 | I'll kill all of you!! | Dodoria | PQ22 | Partially verified |

## Next research targets

The next catalogue pass is targeting the following documented records after the initial batch:

| Target | Character | Acquisition currently indexed | Important mechanics to reconcile |
|---|---|---|---|
| H-How could he?! | Zarbon | PQ12 | Always; stamina recovery +5% |
| Saiyans are a warrior race!! | Vegeta | Item Shop | Enemy KO; Strike damage; stacking behavior |
| Kieeeee!! | Guldo | Item Shop | Charged Ki Blast hit; Slow status |
| Your life is mine! Toh! | Recoome | Item Shop | Reinforcement activation; all Attack +10%; duration |
| I must tell Lord Frieza... | Appule | Item Shop | Passive-effect state and Limit Burst |
| Tch... Guess I have no choice. | Raspberry | Item Shop | Passive-effect state and Limit Burst |
| Unleash your power!! | Krillin | Item Shop | Battle-start effect and duration |
| Stop trampling on Namek's peace! | Young Namekian | NPC Moraska | Ally-race scaling and mobility effect |

These entries remain research targets until their structured records are added and independently reconciled.

## Verification policy

A record may be promoted to **verified** only when its core identity, acquisition route, and important mechanics are reconciled against sufficient independent evidence. Verification does not mean every community measurement or historical interaction has been exhaustively reproduced.

`partially_verified` means meaningful information has been checked, but one or more important fields remain source-dependent or unresolved.

`indexed` means the soul has been catalogued or discovered, but substantial research remains.

## DLC provenance

DLC ownership and in-game acquisition are stored separately. A DLC can introduce a Super Soul while the soul itself may be obtained through a PQ or another in-game route after the relevant content is available. Official Bandai Namco DLC descriptions confirm that DLC packs can contain dedicated Super Souls alongside characters, PQs, skills, and other content.

## Research priorities

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
