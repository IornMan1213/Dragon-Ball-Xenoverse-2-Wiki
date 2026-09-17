---
layout: wiki
title: Parallel Quest Audit
---

# Parallel Quest Audit

> **Browse the live quest catalog:** [Every Parallel Quest](Parallel-Quests-All.html)

This is the exhaustive PQ verification pass that follows the skill catalog. The target is every available Parallel Quest, including DLC quests, with exact unlock path, difficulty, enemies, base rewards, skill rewards, drop conditions, and Ultimate Finish conditions.

## Record standard

Each PQ record should eventually contain:

- PQ number and internal/official name
- Star difficulty
- Unlock condition
- DLC requirement, when applicable
- Time limit
- Enemy waves / special allies
- Base clear rewards
- Skill rewards and exact drop condition
- Super Soul / outfit / accessory / item rewards
- Ultimate Finish trigger
- What the quest unlocks next
- Verification date and source provenance

## Current verified coverage

### Batch 1 — PQ1–PQ10

Structured in `pq-batch-01.json`. Early Saiyan-era quests were cross-checked against the maintained PQ transcription and independent hidden-objective references. Documented skill candidates include Spirit Slash, Solar Flare, Paralyze Beam, Kamehameha, Meteor Strike, Shine Shot, Kaioken, Meteor Blow, Wall of Defense, and Unrelenting Barrage. Exact reward-slot probabilities remain unresolved.

### Batch 2 — PQ11–PQ20

Structured in `pq-batch-02.json`. This block covers Saiyan, Namek, and Ginyu Force quests. PQ11's Earth Splitting Galick Gun UF reward and PQ18's Time Control/Mach Dash reward evidence are preserved; other reward-slot semantics remain unresolved.

### Batch 3 — PQ21–PQ30

Structured in `pq-batch-03.json`. Covers Frieza/Namek, Cooler, Android, and Hercule quests, including Dragon Ball recovery, time-limit, escort, and revived-enemy conditions.

### Batch 4 — PQ31–PQ40

Structured in `pq-batch-04.json`. Covers Cell training through the Future Warriors quest. A historical conflict concerning PQ36 is preserved: maintained game-specific guides document PQ36, while a newer datamined corpus claims it was cut. The contradiction is not silently resolved.

### Batch 5 — PQ41–PQ50

Structured in `pq-batch-05.json`. Covers Future Androids, Dragon Ball collection, Android 16, Broly/Vegeta protection, the second World Tournament, Namek training, and Majin Buu quests.

### Batch 6 — PQ51–PQ60

Structured in `pq-batch-06.json`. Covers Great Saiyaman, Super Saiyan bargain, Majin Buu, Gotenks, Hercule, Janemba, Potara, and Super Spirit Bomb quests.

### Batch 7 — PQ61–PQ70

Structured in `pq-batch-07.json`. Covers continued Cell Games, Frieza rematch, Beerus/Whis, Super Saiyan God, Dragon Ball recovery, God of Destruction, and Golden Frieza/Metal Cooler quests.

### Batch 8 — PQ71–PQ80

Structured in `pq-batch-08.json`. Covers Golden Frieza/Frieza Force assaults, Galactic Patrol training, Beerus/Whis training, the Goku/Vegeta rivalry, parent-and-child training, Broly's revival, and Great Ape festival quests.

### Batch 9 — PQ81–PQ90

Structured in `pq-batch-09.json`. Covers later base-game Gogeta, Golden Frieza/Metal Cooler, Broly/Dragon Ball, Saiyan, Yamcha, Dragon Ball collection, ultimate-series, and great-evil-alliance quests. Exact random reward-slot/drop percentages remain unresolved.

### Batch 10 — PQ91–PQ100

Structured in `pq-batch-10.json`. This completes the **100 base-game PQ audit block**. The quests cover the Saiyan Revolt, Baby/Tuffle conflict, Pan and GT Goku scenario, Shadow Dragons, Super 17, Mira/Towa, villain regrouping, Frieza-race invasion, and the final SSGSS rivalry.

### Batch 11 — PQ101–PQ110

Structured in `pq-batch-11.json`. Covers Super Packs 1–4. Historical guides and independent sources agree on the major Ultimate Finish triggers and documented basic rewards; exact random reward-slot percentages remain unresolved except where a current maintained source explicitly establishes one.

### Batch 12 — PQ111–PQ120

Structured in `pq-batch-12.json`. This block continues from Super Pack 4 into Extra Packs 1 and 2. DLC ownership was cross-checked rather than inferred from numbering: PQ111–112 belong to Super Pack 4; PQ113–117 belong to Extra Pack 1; PQ118–122 belong to Extra Pack 2. citeturn1search2turn1search10

- **PQ111 — The Zero Mortal Plan:** defeat all enemies, clear under five minutes, then defeat Rosé Goku Black and Super 17; Lightning of Absolution and Holy Wrath are documented.
- **PQ112 — Advent of the Mighty God Zamasu!:** defeat all enemies while keeping allies alive, then defeat Android 17 and the other enemies; Blades of Judgment and Divine Wrath: Purification are documented.
- **PQ113 — Birth of the Ultimate Majin!:** keep Majin Buu (Gohan Abs.) above 50%, then defeat all Majin Buus; Super Ghost Buu Attack and the Super variant of Candy Beam are documented.
- **PQ114 — The Majin Revival Plan:** clear under ten minutes, then defeat Dabura and Kid Buu; Petrifying Spit and Evil Blast are documented.
- **PQ115 — Extreme Battle with Android 13!:** defeat all enemies without losing allies, then defeat Android 13 and Android 17; Handy Canon and S.S. Deadly Bomber are documented. citeturn1search0turn1search1
- **PQ116 — A Hero's Duty:** clear under nine minutes, then defeat Dabura and Omega Shenron; Brave Sword Slash and Hero's Flute are documented. citeturn1search3
- **PQ117 — A Dance of Swords:** clear under ten minutes, then defeat Future Trunks and Tapion; Evil Flame and Brave Sword Attack are documented. citeturn2search0
- **PQ118 — Beerus's Tournament Troubles:** keep Beerus above 50%, then defeat Golden Frieza and the other enemies; no skill is documented in the basic reward list. citeturn2youtube8turn2search1
- **PQ119 — A Ranger's Duty:** clear under nine minutes, then defeat Great Ape Nappa; Rough Ranger is documented. citeturn2search1
- **PQ120 — Whis's Special Training:** defeat all Jirens before one leaves, then defeat Beerus, Whis, and Jiren; Power Impact is documented. citeturn2search1

## Early verified examples

### PQ 11 — Burst Open and Mix!

A 2-star Saiyan Saga quest. Clear PQ10 first. The Ultimate Finish requires defeating Great Ape Vegeta within 10 minutes and then defeating the Time Patroller who appears. Earth Splitting Galick Gun is preserved as a documented UF reward in the existing local audit.

### PQ 18 — Force Entrance Exam

A 3-star Ginyu Force quest. Clear PQ17 first. Keep Guldo above 50%, defeat Burter, Jeice and Recoome, then defeat Ginyu and the revived pair for the Ultimate Finish. Time Control and Mach Dash have explicit reward evidence in the existing local audit.

### PQ 110 — Heretics from a Dark World

A 7-star crossover quest. The Ultimate Finish requires keeping Rosé Goku Black above 50% and then defeating Mira. Divinity Unleashed, SS4 Wig & Tail, and Time Patrol Gi are preserved as documented rewards.

## Research target

The wiki distinguishes **indexed PQs** from **fully verified PQs**. A quest is not marked complete merely because its title or number has been indexed: reward tables and Ultimate Finish conditions must be checked before promotion.

Current structured audit coverage: **PQ1–PQ120** plus the previously documented spot-verified examples. Remaining DLC PQs will be processed in numbered batches with the same provenance and conflict-preservation rules.

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- DLC catalog: https://dbxv2.fandom.com/wiki/DLC
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; the live explorer exposes the individual source records while detailed local verification proceeds.
