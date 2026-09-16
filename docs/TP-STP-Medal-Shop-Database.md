---
layout: wiki
title: TP / STP Medal Shop Database
---

# TP / STP Medal Shop Database

This page tracks **equipment and accessory research** connected to the TP Medal Shop and STP Medal Shop. The shops are rotation-based, so a dated shop schedule is treated as a historical snapshot rather than permanent availability.

## Why the distinction matters

A shop record can contain several different facts:

- the item exists;
- the item can appear in a medal shop;
- the item appeared during a particular dated rotation;
- the item had a particular TP/STP price during that observation;
- the item is currently available;
- the item may have another acquisition route.

Those facts are not interchangeable.

## Structured research layer

`docs/data/tp-stp-medal-shop-research.json`

The initial research layer contains **36 equipment/shop records** covering historical clothing and accessory rotations. It intentionally keeps the records `partially_verified` until current rotation, currency, price, and restrictions are reconciled.

## Currency layers

### TP Medals

TP Medals remain earnable through gameplay and can be spent in-game. Bandai Namco's 2024 currency transition notice states that TP Medal sales through digital stores ended around May 2024 while gameplay-earned TP Medals continued to be usable in-game. urlBandai Namco TP Medal transition noticehttps://en.bandainamcoent.eu/dragon-ball/news/dragon-ball-xenoverse-2-notice-new-paid-currency-sales-may-2024

### STP Medals

STP Medals are a separate in-game currency used at the Medal Shop and other locations. Current platform storefront documentation describes them as exchangeable for various in-game items. urlXbox STP Medal listinghttps://www.xbox.com/en-US/games/store/dragon-ball-xenoverse-2-stp-medal-x500/9NHJ4D0MRVT8

## Rotation evidence

Historical schedules demonstrate that costumes, accessories, gifts, Super Souls, illustrations, and techniques can rotate through the shop. A 2025 schedule, for example, records different weekly costume inventories and explicitly dated windows. urlGameFAQs TP/STP shop schedule archivehttps://gamefaqs.gamespot.com/boards/204216-dragon-ball-xenoverse-2/80987260

Older records likewise document accessories such as Spike the Devil Man's Head, Mr. Popo's Turban, Launch Wig, Power Pole, Saiyuki Hood, and Tapion's Sword as medal-shop inventory. These are retained as historical evidence, not as proof of today's stock. urlHistorical TP Medal Shop inventory recordhttps://steamcommunity.com/app/454650/discussions/0/305509857566034039/

## Research states

- **indexed** — shop relationship discovered.
- **partially_verified** — shop relationship and some historical evidence supported; current rotation or another important field remains unresolved.
- **verified** — item, shop/currency, applicable price or dated rotation, restrictions, and current/historical interpretation are sufficiently reconciled.

## Next population targets

1. Build dated rotation snapshots instead of one giant undated shop list.
2. Split TP and STP appearances into separate acquisition records.
3. Record exact costume component prices when a set is sold piece-by-piece.
4. Map every shop accessory back to its canonical accessory record.
5. Map every shop clothing item back to its individual equipment pieces.
6. Add DLC/free-update provenance.
7. Preserve historical rotations and discontinued content.
8. Record platform/date differences when documented.
9. Cross-link shop records to PQ, raid, mentor, gift, and wish acquisition routes.
10. Promote records only after current-status evidence is available.

## Research principle

**A historical shop schedule is evidence of availability at that time — not a guarantee of current availability.**
