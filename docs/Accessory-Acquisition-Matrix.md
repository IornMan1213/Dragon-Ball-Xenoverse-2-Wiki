---
layout: wiki
title: Accessory Acquisition Matrix
permalink: /Accessory-Acquisition-Matrix/
---

# Accessory Acquisition Matrix

This page is the cross-system acquisition layer for **Dragon Ball Xenoverse 2 accessories**. It exists separately from the individual PQ and shop databases so the same accessory can retain multiple legitimate acquisition routes without creating duplicate inventory entries.

## Why this exists

Accessory research is unusually prone to duplicate names, historical PQ-number conflicts, alternate reward routes, and confusion between ordinary raids, Crystal Raids, gifts, shops, wishes, and DLC. Current community documentation also reports disagreement about exactly which equipment contributes to the in-game Equipment Collection percentage, so collection status is tracked separately from acquisition. citeturn0search0turn0reddit23

## Cross-route records

| Accessory | Acquisition systems currently documented | Evidence state | Important caveat |
|---|---|---|---|
| SS Rosé Wig | Character Gift — Goku; Crystal Raid / raid-related reward documentation | Partially verified | Gift reward is one random equipment item from the applicable pool. |
| Golden Scouter | Character Gift — Nappa; Character Gift — Vegeta; Crystal Raid documentation | Partially verified | Gift pools and raid availability should remain separate provenance records. |
| Golden Great Ape Wig & Tail | Character Gift — Gohan (Kid); Crystal Raid / raid documentation | Partially verified | Do not merge with similarly named Great Ape accessories. |
| Fused Zamasu Wig | Crystal Raid / Online Raid documentation | Partially verified | Raid availability is event-dependent. |
| Tiencha Wig | Accessory Shop; Online Raid documentation | Partially verified | Historical raid documentation describes it as a rare raid reward; shop route is a separate acquisition path. |
| Frieza's Head (Final Form) | Crystal Raid; Time Patrol Support Pack / DLC documentation | Partially verified | Current DLC provenance and raid provenance are intentionally separate. |
| Tapion Wig | Ranked-event documentation | Partially verified | Event availability is not treated as a permanent shop route. |
| Janemba's Sword | Crystal Raid documentation | Partially verified | Cosmetic accessory; keep distinct from Tapion's Sword. |
| Lord Zuno's Topknot Wig | Crystal Raid documentation | Partially verified | Historical/event availability requires version-aware research. |
| Universe 6 Supreme Kai's Helper's Hat | Crystal Raid documentation | Partially verified | Historical raid route; availability is event-dependent. |
| Tights Hat | Crystal Raid documentation | Partially verified | Raid-only/Crystal Raid provenance must not be inferred from ordinary PQ listings. |
| SS4 Wig & Tail (Goku) | PQ110; DLC provenance | Partially verified | PQ110 record tracks the Ultimate Finish relationship separately from DLC ownership. |
| Resistance Helmet | PQ111; DLC Pack 4 | Partially verified | Paid-DLC provenance does not itself prove a guaranteed PQ reward. |
| Android 13's Hat | PQ105; TP Medal Shop reported | Partially verified | Keep PQ and shop routes as separate records. |
| Pan's Bandana | PQ93; other accessory inventory documentation | Partially verified | Exact current reward mechanism remains under reconciliation. |
| Yamcha's Sword | PQ29 reported; PQ36 reported by historical sources; shop route reported | Partially verified | The conflicting PQ numbers are deliberately preserved. |

## Character Gift equipment pools

Current/historical gift documentation reports the following accessory routes:

- **Goku:** SS Rosé Wig.
- **Gohan:** Golden Great Ape Wig and Tail.
- **Nappa:** Golden Scouter.
- **Vegeta:** Golden Scouter.

The same gift documentation lists clothing pieces alongside these accessories. The wiki keeps those equipment types separate instead of treating the entire gift pool as an accessory collection. citeturn0search9

## Raid and Crystal Raid separation

Raid documentation contains accessories such as Tights Hat, Universe 6 Supreme Kai's Helper's Hat, Lord Zuno's Topknot Wig, Janemba's Sword, Frieza's Head (Final Form), Golden Great Ape Hat & Tail, Golden Scouter, Super Saiyan Rosé Wig, Fused Zamasu Wig, Tapion Wig, and Tiencha Wig. citeturn0search2turn0search5

These are stored as **event/raid provenance**, not silently converted into PQ or shop records.

## DLC provenance

The official Bandai Namco DLC catalog confirms that Xenoverse 2's DLC includes Parallel Quests, costumes/accessories, and other content across multiple DLC families, including Future Saga, HERO OF JUSTICE, Conton City Vote Pack, Legendary Pack, Ultra Pack, Extra Pass, and Super Pass. Some DLC content is obtained by clearing in-game conditions rather than directly from the purchase itself. citeturn0search4turn0search8

Therefore:

- **DLC ownership** is not the same thing as an **unlock condition**.
- A PQ belonging to a DLC pack does not automatically mean its accessory is a guaranteed reward.
- Shop availability can coexist with DLC provenance.
- Event/raid availability is retained even when an item later receives another route.

## Collection percentage is a separate research problem

Community reports show unresolved disagreement about which base-game, DLC, raid, tournament, and special items contribute to the in-game Equipment Collection percentage. This wiki therefore does **not** claim that every accessory in this database necessarily counts toward the same percentage. citeturn0reddit23

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
- Collection percentage is never inferred from an acquisition list.

## Related databases

- `docs/data/equipment-accessories-record-layer.json`
- `docs/data/accessory-pq-research.json`
- `docs/data/accessory-shop-research.json`
- `docs/Accessory-PQ-Database.md`
- `docs/Accessory-Shop-Database.md`
- `docs/TP-STP-Medal-Shop-Database.md`
- `docs/Equipment-Database.md`

## Sources

- https://dbxv2.fandom.com/wiki/Equipment
- https://dbxv2.fandom.com/wiki/Online_Raid_Quest
- https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/79523787
- https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/77816881
- https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/74977946
- https://www.bandainamcoent.com/games/dragon-ball-xenoverse-2/downloadable-content
- https://en.bandainamcoent.eu/dragon-ball/dragon-ball-xenoverse-2/dlc
