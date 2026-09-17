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

- **PQ91 — Saiyan Revolt:** defeat Goku while keeping Raditz and Nappa alive, then defeat Vegito; Final Kamehameha is documented.
- **PQ92 — Revenge of the Tuffle:** defeat Great Ape Baby, clear under five minutes, then defeat Goku; Maiden Burst is documented.
- **PQ93 — Small but Strong!:** defeat Goku, defeat GT Goku and Trunks before Pan, then defeat Goku and Vegeta; documented rewards are equipment/Super Souls rather than a documented skill reward.
- **PQ94 — Ultimate Power, Ultimate Saiyan:** defeat Gogeta, clear under five minutes, then defeat Gogeta, Eis, Nuova, and Omega Shenron; Bluff Kamehameha is documented.
- **PQ95 — Super 17, the Ultimate Android:** defeat Super 17 while keeping Goku alive, then defeat revived Super 17; Spirit Explosion is documented.
- **PQ96 — The Shadow Dragons:** defeat Omega Shenron while keeping all allies alive, then defeat all enemies; Crazy Finger Shot is documented.
- **PQ97 — Insidious Plot:** defeat Mira and Towa, clear under three minutes, then defeat all enemies; Sauzer Blade is documented.
- **PQ98 — Villains Regroup!:** defeat all enemies, clear under five minutes, then defeat Janemba and Turles; Dimension Ray is documented.
- **PQ99 — Frieza Race Revivified:** defeat all enemies, clear under five minutes, then defeat Frieza and the avatar; Emperor's Edge is documented.
- **PQ100 — The Ultimate Rivalry:** defeat all enemies, clear within eight minutes, then defeat SSGSS Goku and SSGSS Vegeta; X100 Big Bang Kamehameha is documented.

### Batch 11 — PQ101–PQ110

Structured in `pq-batch-11.json`. This block begins the DLC audit, covering Super Packs 1–4. Historical guides and independent sources agree on the major Ultimate Finish triggers and documented basic rewards; exact random reward-slot percentages remain unresolved except where a current maintained source explicitly establishes one.

- **PQ101 — Seeking Fighters for Tournament!:** keep Goku and Vegeta above 50%, then defeat SSGSS Goku and SSGSS Vegeta; Breaker Energy Wave is documented.
- **PQ102 — Universe 6 in a Fix!:** keep all allies alive, then defeat Omega Shenron and Super 17; no skill is documented in the basic reward list.
- **PQ103 — Warriors of Universes 6 & 7!:** finish with at least ten minutes remaining, then defeat Hit; the documented basic rewards are Super Souls/items.
- **PQ104 — Vados the Talent Scout:** keep Vados above 80%, then fight Vados and revived enemies; Destruction's Concerto: Comet and Starfall are documented.
- **PQ105 — Champa's Hellish Holiday:** clear under five minutes, then fight Champa; Sonic Bomb, God of Destruction's Menace, and God of Destruction's Roar are documented.
- **PQ106 — A Destructive Showdown!:** fight Champa/Vados, keep Beerus and Whis above 50%, then fight Beerus/Whis; Destruction's Concerto: Meteor, Requiem of Destruction, and Destruction's Conductor are documented.
- **PQ107 — The Future's Greatest Hope!:** keep Future Trunks above 50%, then defeat SSGSS Goku and SSGSS Vegeta; no skill is documented in the basic reward list.
- **PQ108 — Doppleganger Dispute!:** clear under ten minutes, then defeat SSGSS Goku and Future Trunks; no skill is documented in the basic reward list.
- **PQ109 — A Fateful Fight With Deity!:** keep all allies alive, then defeat Zamasu and Rosé Goku Black; Super Black Kamehameha Rosé is documented.
- **PQ110 — Heretics from a Dark World:** keep Rosé Goku Black above 50%, then defeat Mira; Divinity Unleashed is documented. Current maintained data additionally identifies PQ110 as a 7-star quest and explicitly documents its reward-slot semantics.

## Early verified examples

### PQ 11 — Burst Open and Mix!

A 2-star Saiyan Saga quest. Clear PQ10 first. The Ultimate Finish requires defeating Great Ape Vegeta within 10 minutes and then defeating the Time Patroller who appears. Earth Splitting Galick Gun is preserved as a documented UF reward in the existing local audit.

### PQ 18 — Force Entrance Exam

A 3-star Ginyu Force quest. Clear PQ17 first. Keep Guldo above 50%, defeat Burter, Jeice and Recoome, then defeat Ginyu and the revived pair for the Ultimate Finish. Time Control and Mach Dash have explicit reward evidence in the existing local audit.

### PQ 110 — Heretics from a Dark World

A 7-star crossover quest. The Ultimate Finish requires keeping Rosé Goku Black above 50% and then defeating Mira. Divinity Unleashed, SS4 Wig & Tail, and Time Patrol Gi are preserved as documented rewards.

## Research target

The wiki distinguishes **indexed PQs** from **fully verified PQs**. A quest is not marked complete merely because its title or number has been indexed: reward tables and Ultimate Finish conditions must be checked before promotion.

Current structured audit coverage: **PQ1–PQ110** plus the previously documented spot-verified examples. The first DLC block is now structurally covered; remaining DLC PQs will be processed in numbered batches with the same provenance and conflict-preservation rules.

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; the live explorer exposes the individual source records while detailed local verification proceeds.
