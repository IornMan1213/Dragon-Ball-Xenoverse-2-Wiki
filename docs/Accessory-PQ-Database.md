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

The machine-readable layer now contains **45 accessory/PQ research records**. Some records are deliberately `indexed` rather than `partially_verified` where the evidence establishes a research lead but not the exact inventory component.

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
| Bardock (DB Super)'s Scouter | 146 | Partially verified |
| Gine (DB Super)'s Accessory | 144 | Indexed |
| Caulifla's Accessory | 147 | Indexed |
| Kale's Accessory | 148 | Indexed |
| Android 17 (DB Super)'s Ranger Accessory | 152 | Indexed |
| Android 15's Sunglasses | — | Indexed; no PQ route established |
| Android 17 (DB Super) Wig | 152 | Partially verified |
| King Vegeta (DB Super) Wig | 154 | Partially verified |
| Dr. Hedo Hood | 159 | Partially verified |
| Red Ribbon Army Helmet | 160 | Partially verified |
| Gohan (Beast) Wig | 162 | Partially verified |
| Videl (DB Super) Wig | 168 | Partially verified |
| Gamma 2's Helmet | 155 | Partially verified |
| Gamma 1's Helmet | 156 | Partially verified |
| SS4 Goku (DAIMA) Wig & Tail | 179 | Indexed |
| SS3 Vegeta (DAIMA) Wig | 180 | Indexed |
| Glorio Wig | 181 | Indexed |
| Panzy Wig | 181 | Indexed |
| Golden Frieza Head | 182 | Indexed |
| Broly Wig (Black Hair, Normal) | 183 | Indexed |
| Dragon Ball Balloon | 184 | Partially verified |
| Goku (Ultra Supervillain Quelled) Wig | 185 | Indexed |

## Conton City Vote and Hero of Justice coverage

PQ152, **Dyspo's Wanted Man**, lists Android 17 (DB Super)'s Wig; PQ154, **Dabura the Loyal? Servant**, lists King Vegeta (DB Super) Wig; PQ155, **I Need a Hero... Pose!**, lists Gamma 2's Helmet; and PQ156, **Hunting Down Dr. Hedo**, lists Gamma 1's Helmet. The DLC documentation independently associates these items with their respective DLC packs. citeturn0search1turn0search2

The Hero of Justice PQ layer also identifies later accessories including Red Ribbon Army Helmet, Gohan (Beast) Wig, and Videl (DB Super) Wig. These remain tied to individual quests rather than being flattened into a generic DLC acquisition label. citeturn0search1

## DAIMA and later DLC coverage

The later PQ guide provides accessory/equipment research leads for PQ179–185, including SS4 Goku (DAIMA) Wig & Tail, SS3 Vegeta (DAIMA) Wig, Glorio Wig, Panzy Wig, Golden Frieza Head, Broly Wig (Black Hair, Normal), Dragon Ball Balloon, and Goku (Ultra Supervillain Quelled) Wig. The Dragon Ball Balloon has stronger evidence: current Madreag quest data records it as a **50% Ultimate Finish reward**, while the other late-DLC records remain indexed until their exact reward mechanics are reconciled. citeturn0search8turn0search9

This is intentional: a research lead is useful, but it is not the same thing as a verified acquisition condition.

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
- https://github.com/Madreag/xenoverse_2_wiki/blob/main/content/parallel-quests/pq-184.md
- https://dbxv2.fandom.com/wiki/Equipment
- https://dbxv2.fandom.com/wiki/Parallel_Quests
- https://dbxv2.fandom.com/wiki/DLC
- https://enjoi7.sakura.ne.jp/db_newproject2/ac.html

## Research status

**Partially verified.** The database now spans early base-game accessory relationships through Conton City Vote, Hero of Justice, Future Saga, and DAIMA-era PQ research leads. The next pass should reconcile indexed late-DLC records against the canonical accessory inventory and continue filling the remaining PQ range without inventing reward rates.
