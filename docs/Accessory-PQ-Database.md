---
layout: wiki
title: Accessory PQ Database
permalink: /Accessory-PQ-Database/
---

# Accessory PQ Database

The Parallel Quest accessory research layer connects individual accessories to their documented PQ acquisition routes without collapsing different reward mechanics into a single "drop" label.

## What this tracks

- PQ number and identity
- Accessory name and variant
- Normal reward vs Ultimate Finish relationship when documented
- Scripted/guaranteed rewards vs reward-pool entries
- Alternate Shop, Raid, Gift, Wish, and DLC routes
- Historical source conflicts
- Current-version uncertainty
- Verification status and source provenance

## Current research population

The machine-readable layer now contains **32 accessory/PQ research records**. Some records are deliberately `indexed` rather than `partially_verified` where the evidence establishes a research lead but not the exact inventory component.

| Accessory / research item | PQ | State |
|---|---:|---|
| Piccolo's Turban | 3 | Partially verified |
| Four-Star Dragon Ball Hat | 5 | Partially verified |
| Chiaotzu's Hat (With Collar) | 9 | Partially verified |
| Tapion's Sword | 22 | Partially verified |
| Goku's Wig | 25 | Partially verified |
| Dore's Scouter | 27 | Partially verified |
| Android 19's Hat | 28 | Partially verified |
| Yamcha's Sword | 29 | Partially verified; historical PQ conflict retained |
| Great Saiyaman Bandana 1 | 51 | Partially verified |
| Great Saiyaman Helmet | 51 | Partially verified |
| Great Saiyaman Bandana 2 | 53 | Partially verified |
| Goku Wig (Super Saiyan) | 63 | Partially verified |
| Jaco's State-of-the-Art Radio | 72 | Partially verified |
| Tagoma's Scouter | 73 | Partially verified |
| SSGSS Goku Wig | 76 | Partially verified |
| Pan's Bandana | 93 | Partially verified |
| Yamcha Baseball Hat | 97 | Partially verified |
| SSGSS Vegeta Wig | 100 | Partially verified |
| Android 14's Hat | 104 | Partially verified |
| Android 13's Hat | 105 | Partially verified |
| SS4 Wig & Tail (Goku) | 110 | Partially verified |
| Resistance Helmet | 111 | Partially verified |
| Bulma (Kid) Wig | 149 | Partially verified |
| Bardock (DB Super) accessory lead | 146 | Indexed |
| Gine (DB Super) accessory lead | 144 | Indexed |
| Caulifla accessory lead | 147 | Indexed |
| Kale accessory lead | 148 | Indexed |
| Android 17 (DB Super) Ranger accessory/equipment lead | 152 | Indexed |
| Android 15's Sunglasses | — | Indexed; no PQ route established |
| Red Ribbon Army Helmet | 160 | Partially verified |
| Gohan (Beast) Wig | 162 | Partially verified |
| Videl (DB Super) Wig | 168 | Partially verified |

## New DLC-era coverage

The Hero of Justice PQ research provides direct reward listings for several accessories. PQ160, **Pan in Peril**, lists the Red Ribbon Army Helmet; PQ162, **The Man, the Myth, the Yamcha**, lists the Gohan (Beast) Wig; and PQ168, **Videl: Super Mom**, lists the Videl (DB Super) Wig. These are recorded as PQ associations, not assumed guaranteed drops, because a basic reward listing alone does not establish the underlying roll mechanics. citeturn0search1

The broader PQ documentation confirms that equipment can be obtained through different reward mechanisms, including opponent-linked drops and Ultimate Finish rolls. citeturn0search5

## High-confidence example: PQ110

Current research identifies the SS4 Wig & Tail (Goku) as an Ultimate Finish reward on PQ110, while other equipment and rewards on that quest use separate reward mechanisms. This distinction is preserved in the machine-readable record rather than treating every listed reward as an identical drop type.

The current research source is:

https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/parallel-quests/pq-110.md

Historical DLC documentation should be used alongside the quest record when reconciling DLC provenance and accessory availability.

## Reward mechanics matter

A PQ reward list alone does **not** establish whether an accessory is:

- guaranteed on normal completion;
- a random normal-clear reward;
- a first-clear reward;
- an Ultimate Finish reward;
- a random Ultimate Finish reward;
- a scripted reward outside the random pool; or
- part of a version-specific reward table.

The database therefore does **not** invent a drop percentage when the underlying evidence only says that an accessory is associated with a quest.

## Known conflicts and caveats

### Yamcha's Sword

Historical sources disagree on its PQ association. The current record retains PQ29 while documenting the competing PQ36 claim rather than silently selecting one. This needs direct current-version reconciliation.

### Goku's Wig

PQ25 is the current mapping used by the research layer, but older inventories can differ in numbering or presentation. It remains partially verified until that historical discrepancy is resolved.

### TP/STP overlap

Some accessories that appear in PQ research also have shop routes. PQ provenance and shop provenance are therefore stored separately instead of allowing one route to overwrite another.

## Cross-system relationships

Accessory acquisition is not isolated from the rest of the game. The same item can have multiple documented routes, including:

- Parallel Quests
- Ultimate Finishes
- Accessory Shop
- TP/STP Medal Shop
- Raids
- Crystal Raids
- Character Gifts
- Shenron Wishes
- DLC/free updates
- Special events

The broader equipment documentation likewise contains mixed PQ and shop acquisition routes, so each individual item needs its own provenance rather than a single universal acquisition label.

## Data source

Machine-readable records:

`docs/data/accessory-pq-research.json`

Related research:

- `docs/Accessory-Shop-Database.md`
- `docs/TP-STP-Medal-Shop-Database.md`
- `docs/Equipment-Database.md`
- `docs/data/equipment-accessories-record-layer.json`
- `docs/data/equipment-record-layer.json`

## Sources

- https://steamcommunity.com/sharedfiles/filedetails/?id=796204215
- https://steamcommunity.com/sharedfiles/filedetails/?id=808851543
- https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/parallel-quests/pq-110.md
- https://dbxv2.fandom.com/wiki/Equipment
- https://dbxv2.fandom.com/wiki/Parallel_Quests
- https://dbxv2.fandom.com/wiki/DLC
- https://enjoi7.sakura.ne.jp/db_newproject2/ac.html

## Research status

**Partially verified.** The database now covers accessory/PQ relationships from the early base-game quests through selected DLC-era quests, while preserving uncertainty around reward-slot mechanics. Further passes should continue through the remaining PQs and reconcile every relationship against the canonical accessory inventory.
