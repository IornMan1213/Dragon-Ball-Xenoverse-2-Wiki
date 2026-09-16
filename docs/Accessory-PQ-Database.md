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

The machine-readable layer now contains **29 accessory/PQ research records**. Some records are deliberately `indexed` rather than `partially_verified` where the evidence establishes a research lead but not the exact inventory component.

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

## High-confidence example: PQ110

Current research for **PQ110, "Heretics from a Dark World,"** identifies the SS4 Wig & Tail (Goku) as an Ultimate Finish reward. The same research separates the Super Saiyan 4 Suit as a scripted reward, the Time Patrol Gi as a separate reward pool, and other rewards such as Super Souls, skills, and Super Mix Capsules. citeturn0search0

This is exactly the distinction the database is designed to preserve: **the accessory's PQ association does not mean every reward on that quest uses the same acquisition mechanism.**

Historical DLC documentation independently places the SS4 Wig & Tail and Super Saiyan 4 Suit in DLC Pack 4/PQ110, while Resistance Helmet is associated with PQ111. citeturn0search2turn0search1

## Reward mechanics matter

A PQ reward list alone does **not** establish whether an accessory is:

- guaranteed on normal completion;
- a random normal-clear reward;
- a first-clear reward;
- an Ultimate Finish reward;
- a random Ultimate Finish reward;
- a scripted reward outside the random pool; or
- part of a version-specific reward table.

The game's PQ documentation distinguishes ordinary completion from Ultimate Finish and notes that equipment and other rewards can be tied to specific defeated opponents or to Ultimate Finish reward rolls. citeturn0search9

Accordingly, the database does **not** invent a drop percentage when the underlying evidence only says that an accessory is associated with a quest.

## Known conflicts and caveats

### Yamcha's Sword

Historical sources disagree on its PQ association. The current record retains PQ29 while documenting the competing PQ36 claim rather than silently selecting one. This needs a direct current-version reconciliation.

### Goku's Wig

PQ25 is the current mapping used by the research layer, but older inventories can differ in numbering or presentation. It remains partially verified until that historical discrepancy is resolved.

### TP/STP overlap

Some accessories that appear in PQ research also have shop routes. The Saiyan Tail and Great Ape-related accessories are a useful example of why the database keeps PQ and shop provenance separate: community documentation describes rotating TP Medal Shop availability alongside PQ/DLC acquisition. citeturn0search4

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

The broader equipment documentation also shows that later content contains a mixture of TP/STP Shop and PQ acquisition routes, so the equipment database must preserve the acquisition source per individual item rather than assuming a single universal route. citeturn0search8

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

**Partially verified.** The database has moved from a simple accessory/PQ list toward an acquisition graph. The next verification pass should reconcile individual PQ reward slots and conditions, then continue populating PQs beyond the currently documented accessory set.
