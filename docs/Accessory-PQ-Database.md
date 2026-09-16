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

## Initial research population

The first pass contains **20 accessory-to-PQ relationships**. These are research records, not a claim that every listed accessory is currently obtainable in exactly the same way on every version.

| Accessory | PQ | Current research state |
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
| Great Saiyaman Bandana 2 | 53 | Partially verified |
| Goku Wig (Super Saiyan) | 63 | Partially verified |
| Jaco's State-of-the-Art Radio | 72 | Partially verified |
| Tagoma's Scouter | 73 | Partially verified |
| SSGSS Goku Wig | 76 | Partially verified |
| Pan's Bandana | 93 | Partially verified |
| Yamcha Baseball Hat | 97 | Partially verified |
| SSGSS Vegeta Wig | 100 | Partially verified |
| SS4 Wig & Tail (Goku) | 110 | Partially verified |
| Great Saiyaman Helmet | 51 | Partially verified |
| Bulma (Kid) Wig | 149 | Partially verified |

## Important reward distinction

A reward list alone does **not** establish whether an accessory is guaranteed, random, first-clear, normal-clear, Ultimate Finish, or bonus-slot content. Those mechanisms are being tracked separately.

Current structured research for PQ110 identifies the SS4 Wig & Tail (Goku) as an Ultimate Finish reward, while the same quest has separate scripted clothing and reward-pool entries. See the PQ110 research source listed below.

The older searchable PQ reward guides also demonstrate why the database needs explicit acquisition-condition fields: they list accessories alongside ordinary quest rewards without necessarily exposing the underlying drop-table mechanics.

## Known conflicts

### Yamcha's Sword

Historical sources disagree on the PQ association. One searchable equipment guide associates it with PQ29, while another historical equipment list associates it with PQ36. The wiki deliberately retains this conflict instead of silently choosing one source.

### Goku's Wig

The searchable PQ reward guide identifies Goku's Wig under PQ25. Older accessory inventories can contain different numbering or acquisition notes, so the record remains partially verified until the discrepancy is reconciled against stronger current evidence.

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

A PQ record should therefore point toward the accessory record rather than duplicating its complete acquisition history.

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
- https://www.gameskinny.com/tips/dragon-ball-xenoverse-guide-equipment-and-accessory-list/

## Research status

**Partially verified.** The purpose of this layer is to establish the accessory→PQ relationship first, then deepen each record with exact reward-slot mechanics, Ultimate Finish conditions, alternate routes, DLC provenance, and current-version behavior.
