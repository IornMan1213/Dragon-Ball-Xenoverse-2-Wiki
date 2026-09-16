---
layout: wiki
title: Accessory Acquisition Matrix
permalink: /Accessory-Acquisition-Matrix/
---

# Accessory Acquisition Matrix

This page is the cross-system acquisition layer for **Dragon Ball Xenoverse 2 accessories**. It exists separately from the individual PQ and shop databases so the same accessory can retain multiple legitimate acquisition routes without creating duplicate inventory entries.

## Current reconciliation coverage

The machine-readable acquisition matrix now tracks canonical identities across gifts, Parallel Quests, shops, raids/Crystal Raids, DLC provenance, and version-sensitive events. The current PQ reconciliation pass explicitly checks PQ157-PQ168 and records when a PQ's basic reward list contains clothing rather than an accessory, or no accessory in the checked reward extract.

## Why this exists

Accessory research is unusually prone to duplicate names, historical PQ-number conflicts, alternate reward routes, and confusion between ordinary raids, Crystal Raids, gifts, shops, wishes, and DLC. Current community documentation also reports disagreement about exactly which equipment contributes to the in-game Equipment Collection percentage, so collection status is tracked separately from acquisition.

## Cross-route records

| Accessory | Acquisition systems currently documented | Evidence state | Important caveat |
|---|---|---|---|
| SS Rosé Wig | Character Gift — Goku; Crystal Raid / raid-related reward documentation | Partially verified | Gift reward is one random equipment item from the applicable pool. |
| Golden Scouter | Character Gift — Nappa; Character Gift — Vegeta; Crystal Raid documentation | Partially verified | Gift pools and raid availability should remain separate provenance records. |
| Golden Great Ape Wig & Tail | Character Gift — Gohan; Crystal Raid / raid documentation | Partially verified | Do not merge with similarly named Great Ape accessories. |
| Fused Zamasu Wig | Crystal Raid / Online Raid documentation | Partially verified | Raid availability is event-dependent. |
| Tiencha Wig | Accessory Shop; Online Raid documentation | Partially verified | Historical raid documentation and shop route are separate acquisition paths. |
| Frieza's Head (Final Form) | Crystal Raid; Time Patrol Support Pack / DLC documentation | Partially verified | Current DLC provenance and raid provenance remain separate. |
| Tapion Wig | Ranked/event documentation | Partially verified | Event availability is not treated as a permanent shop route. |
| Janemba's Sword | Crystal Raid documentation | Partially verified | Cosmetic accessory; keep distinct from Tapion's Sword. |
| Lord Zuno's Topknot Wig | Crystal Raid documentation | Partially verified | Historical/event availability requires version-aware research. |
| Universe 6 Supreme Kai's Helper's Hat | Crystal Raid documentation | Partially verified | Historical raid route; availability is event-dependent. |
| Tights Hat | Crystal Raid documentation | Partially verified | Raid provenance must not be inferred as a PQ route. |
| SS4 Wig & Tail (Goku) | PQ110; DLC provenance | Partially verified | PQ110's Ultimate Finish relationship is tracked separately from DLC ownership. |
| Resistance Helmet | PQ111; DLC provenance | Partially verified | DLC provenance does not itself prove a guaranteed PQ reward. |
| Android 13's Hat | PQ105; TP Medal Shop reported | Partially verified | PQ and shop routes remain separate records. |
| Android 17 (DB Super) Wig | PQ152; DLC provenance | Partially verified | Basic reward listing establishes the PQ association; exact reward mechanics remain separate. |
| King Vegeta (DB Super) Wig | PQ154; DLC provenance | Partially verified | Basic reward listing establishes the PQ association; exact reward mechanics remain separate. |
| Gamma 2's Helmet | PQ155; HERO OF JUSTICE Pack 1 | Partially verified | Current DLC documentation and PQ evidence are cross-referenced. |
| Gamma 1's Helmet | PQ156; HERO OF JUSTICE Pack 1 | Partially verified | Current PQ listing identifies it in the basic rewards. |
| Dr. Hedo Hood | PQ159; HERO OF JUSTICE Pack 2 | Partially verified | Current PQ listing identifies it in the basic rewards. |
| Red Ribbon Army Helmet | PQ160; HERO OF JUSTICE Pack 2 | Partially verified | Current PQ listing identifies it in the basic rewards. |
| Gohan (Beast) Wig | PQ162; HERO OF JUSTICE Pack 2 | Partially verified | Current PQ listing identifies it in the basic rewards. |
| Videl (DB Super) Wig | PQ168; Future Saga Chapter 1 | Partially verified | PQ relationship remains subject to reward-condition reconciliation. |
| Goku (Ultra Supervillain Quelled) Wig | PQ185; Future Saga Chapter 4 | Indexed / partially verified | Newest PQ route requires current-version reward reconciliation. |

## PQ157-PQ168 checked range

The dedicated reconciliation layer records each PQ in this range rather than only recording positive accessory matches:

- **PQ157:** no accessory in the checked basic-reward extract.
- **PQ158:** Gamma 2's Clothes is clothing, not an accessory.
- **PQ159:** Dr. Hedo Hood.
- **PQ160:** Red Ribbon Army Helmet.
- **PQ161:** Red Ribbon Soldier 94 Clothes is clothing, not an accessory.
- **PQ162:** Gohan (Beast) Wig.
- **PQ163-PQ167:** no accessory in the checked basic-reward extracts.
- **PQ168:** Videl (DB Super) Wig remains a cross-reference requiring reward-condition reconciliation.

The current PQ guide directly identifies Gamma 1's Helmet in PQ156, Gamma 2's Clothes in PQ158, Dr. Hedo Hood in PQ159, Red Ribbon Army Helmet in PQ160, Red Ribbon Soldier 94 Clothes in PQ161, and Gohan (Beast) Wig in PQ162. The DLC catalogue separately groups these items with the corresponding HERO OF JUSTICE content. citeturn0search2turn0search5

## Character Gift equipment pools

Current/historical gift documentation reports accessory routes including:

- **Goku:** SS Rosé Wig.
- **Gohan:** Golden Great Ape Wig and Tail.
- **Nappa:** Golden Scouter.
- **Vegeta:** Golden Scouter.

Gift equipment is modeled as pool-based unless evidence establishes a deterministic reward. The wiki therefore does not turn a character gift into a guaranteed one-item drop.

## Raid and Crystal Raid separation

Raid documentation contains accessories such as Tights Hat, Universe 6 Supreme Kai's Helper's Hat, Lord Zuno's Topknot Wig, Janemba's Sword, Frieza's Head (Final Form), Golden Great Ape Hat & Tail, Golden Scouter, Super Saiyan Rosé Wig, Fused Zamasu Wig, Tapion Wig, and Tiencha Wig.

These are stored as **event/raid provenance**, not silently converted into PQ or shop records.

## DLC provenance

DLC ownership and in-game acquisition are separate facts. A DLC pack can contain a PQ, costume/accessory, skill, or other content without that purchase itself being the item's immediate unlock condition.

Therefore:

- **DLC ownership** is not the same thing as an **unlock condition**.
- A PQ belonging to a DLC pack does not automatically mean its accessory is guaranteed.
- Shop availability can coexist with DLC provenance.
- Event/raid availability is retained even when an item later receives another route.

## Collection percentage is a separate research problem

Community reports show unresolved disagreement about which base-game, DLC, raid, tournament, and special items contribute to the in-game Equipment Collection percentage. This wiki therefore does **not** claim that every accessory in this database necessarily counts toward the same percentage.

The collection-status research target is:

1. identify the game's actual collection denominator;
2. separate clothing, accessories, Super Souls, and other equipment classes;
3. determine whether DLC and event equipment are included;
4. test special items and discontinued/event-only equipment;
5. document version differences.

## Research rules

- One accessory identity gets one canonical record even when it has multiple acquisition routes.
- Each acquisition route keeps its own provenance and verification state.
- Historical route conflicts are preserved until independently reconciled.
- A reward listing does not become a guaranteed-drop claim without evidence.
- Raid availability is event/version sensitive.
- Character Gift equipment can be random from a defined pool and should not be represented as a deterministic one-gift/one-item guarantee.
- DLC purchase status, PQ ownership, and actual unlock conditions are separate fields.
- Clothing is never duplicated into the accessory catalogue merely because it appears beside accessories in a PQ reward table.
- Absence from a checked basic-reward extract is recorded as an evidence state, not proof that no alternate route exists.
- Collection percentage is never inferred from an acquisition list.

## Related databases

- `docs/data/equipment-accessories-record-layer.json`
- `docs/data/accessory-acquisition-matrix.json`
- `docs/data/accessory-pq-research.json`
- `docs/data/accessory-pq-reconciliation-157-168.json`
- `docs/data/accessory-shop-research.json`
- `docs/Accessory-PQ-Database.md`
- `docs/Accessory-Shop-Database.md`
- `docs/TP-STP-Medal-Shop-Database.md`
- `docs/Equipment-Database.md`

## Sources

- https://dbxv2.fandom.com/wiki/Equipment
- https://dbxv2.fandom.com/wiki/Online_Raid_Quest
- https://steamcommunity.com/sharedfiles/filedetails/?id=808851543
- https://gamefaqs.gamespot.com/boards/190458-dragon-ball-xenoverse-2/74485071?page=15
- https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/77816881
- https://www.bandainamcoent.com/games/dragon-ball-xenoverse-2/downloadable-content
- https://en.bandainamcoent.eu/dragon-ball/dragon-ball-xenoverse-2/dlc
