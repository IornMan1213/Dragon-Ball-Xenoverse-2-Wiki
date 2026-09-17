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

Structured in `pq-batch-05.json`. Covers Future Androids, Dragon Ball collection, Android 16, Broly/Vegeta protection, the second World Tournament, Namek training, and Majin Buu quests. Skills documented include Burning Attack, Rolling Bullet, Change The Future, God Breaker, Burning Slash, Taunt, Chain Destructo-Disc Barrage, Kamekameha, Do or Die, and Explosive Buu Buu Punch.

### Batch 6 — PQ51–PQ60

Structured in `pq-batch-06.json`. Covers Great Saiyaman, Super Saiyan bargain, Majin Buu, Gotenks, Hercule, Janemba, Potara, and Super Spirit Bomb quests. Skills documented include Burst Rush, Final Cannon, Justice Pose, Victory Cannon, Super Donut Volley, Stone Bullet, Rakshasa's Claw, Vanishing Ball, Force Shield, Dimension Cannon, and Majin Kamehameha.

### Batch 7 — PQ61–PQ70

Structured in `pq-batch-07.json`. Covers continued Cell Games, Frieza rematch, Beerus/Whis, Super Saiyan God, Dragon Ball recovery, God of Destruction, and Golden Frieza/Metal Cooler quests.

- **PQ61 — The Cell Games Continued:** defeat Gohan, Videl, and Piccolo; defeat Videl and Piccolo before Gohan; then defeat Gohan with Cell alive. Recoome Kick and Fighting Pose H are documented.
- **PQ62 — Frieza's Nightmare Returns!:** defeat Vegito and Gotenks, defeat Gotenks before Vegito, then defeat Super Vegito and Super Saiyan 3 Gotenks. Teleporting Vanishing Ball is documented.
- **PQ63 — Appetite for Destruction:** defeat Beerus and Whis, defeat Beerus last, then defeat Beerus again; Kai Kai is documented.
- **PQ64 — Beerus the Impulsive:** defeat all enemies with at least eight minutes remaining, then defeat Beerus; Ill Rain is documented.
- **PQ65 — The New Warriors:** defeat all enemies, clear within eight minutes, then defeat Goku and Vegeta; Scissors Paper Rock is documented.
- **PQ66 — Stop Beerus' Destruction:** defeat Beerus without an ally being defeated, then defeat Whis; Candy Beam is documented.
- **PQ67 — Power of a Super Saiyan God:** defeat Goku, clear under three minutes, then defeat revived Goku; Super God Fist is documented.
- **PQ68 — Old Rivals and Dragon Balls:** recover three Dragon Balls, defeat Frieza/Cell/Kid Buu, then recover all seven; Angry Shout is documented.
- **PQ69 — God of Destruction and His Master:** defeat Beerus and Whis, clear under five minutes, then defeat revived Beerus; Headshot is documented.
- **PQ70 — Things Are Getting Serious!:** defeat all enemies, clear within eight minutes, then defeat Golden Frieza and Metal Cooler; Emperor's Blast is documented.

### Batch 8 — PQ71–PQ80

Structured in `pq-batch-08.json`. Covers Golden Frieza/Frieza Force assaults, Galactic Patrol training, Beerus/Whis training, the Goku/Vegeta rivalry, parent-and-child training, Broly's revival, and Great Ape festival quests.

- **PQ71 — Abominable Saiyans:** keep Trunks above 50%, then defeat Golden Frieza; Last Emperor is documented.
- **PQ72 — First Training:** clear under five minutes and defeat all enemies while Golden Frieza survives; Burst Kamehameha is documented.
- **PQ73 — Frieza's Siege Against Earth!:** defeat all enemies before Golden Frieza appears, then complete the final phase; Psychic Move is documented.
- **PQ74 — Galactic Patrol, Away!:** clear within ten minutes, keep Jaco alive, then defeat Golden Frieza; Final Pose is documented.
- **PQ75 — Room to Spare:** have Beerus enter the next battle with Whis remaining, then defeat Beerus and Whis; Counter Burst is documented.
- **PQ76 — Eternal Rival:** defeat the SSGSS pair, defeat SS4 Goku after SS4 Vegeta appears, then defeat the SSGSS pair again; Warp Kamehameha is documented.
- **PQ77 — Parent and Child:** clear within ten minutes, then defeat all enemies; Ki Explosion is documented.
- **PQ78 — Heated, Furious, Ultimate Battle:** keep revived Goku alive, then defeat revived Broly; Dust Attack is documented.
- **PQ79 — Great Ape Festival:** clear within ten minutes, then defeat the training Time Patroller; Mighty Explosive Wave is documented.
- **PQ80 — The Return of the Giant Ape-Fest!:** keep Jaco and Pan alive, then defeat all enemies; Dimensional Hole is documented.

### Batch 9 — PQ81–PQ90

Structured in `pq-batch-09.json`. This block covers the later base-game Gogeta, Golden Frieza/Metal Cooler, Broly/Dragon Ball, Saiyan, Yamcha, Dragon Ball collection, ultimate-series, and great-evil-alliance quests. Objective sequences and documented basic rewards were cross-checked against the maintained PQ transcription and independent hidden-objective references. Exact random reward-slot/drop percentages remain unresolved.

- **PQ81 — Wake UP!:** defeat all enemies, clear within eight minutes, then defeat Gogeta; Afterimage Strike is documented.
- **PQ82 — Ultimate Brotherly Battle:** defeat all enemies, clear within eight minutes, then defeat Golden Frieza and Metal Cooler; Dragon Burn is documented.
- **PQ83 — Dangerous Duo! Warriors Never Rest:** recover three Dragon Balls, defeat Broly while Gohan survives, then recover all seven; Charge is documented.
- **PQ84 — Saiyan Warriors:** defeat Broly, clear within ten minutes, then defeat Broly, Vegito, and Gotenks; Saiyan Spirit is documented.
- **PQ85 — Power Berserkers:** defeat Gohan, Piccolo, and Vegeta, clear within ten minutes, then defeat Gohan, Broly, and Bardock; Zigzag Express is documented.
- **PQ86 — Yamcha is Number One:** clear in under five minutes, then defeat Yamcha again; Neo Wolf Fang Fist is documented.
- **PQ87 — Saiyan Battle:** defeat Gotenks, Gohan, and Vegeta, clear in under five minutes, then defeat Goku and the revived warriors; Atomic Blast is documented.
- **PQ88 — Evil Seeks Dragon Balls Yet Again!:** recover six Dragon Balls, defeat all enemies, then recover the seventh; Buu Buu Ball is documented.
- **PQ89 — Super-Super Ultimate Series of Battles!:** defeat Goku, Gohan, and Goten, clear within ten minutes, then defeat Vegito and Gotenks; Victory Rush is documented.
- **PQ90 — Gathering of the Great Evil Alliance:** defeat all enemies, clear within ten minutes, then defeat revived Frieza, Cell, and Majin Buu; III Bomber is documented.

## Early verified examples

### PQ 11 — Burst Open and Mix!

A 2-star Saiyan Saga quest. Clear PQ10 first. The Ultimate Finish requires defeating Great Ape Vegeta within 10 minutes and then defeating the Time Patroller who appears. Earth Splitting Galick Gun is preserved as a documented UF reward in the existing local audit.

### PQ 18 — Force Entrance Exam

A 3-star Ginyu Force quest. Clear PQ17 first. Keep Guldo above 50%, defeat Burter, Jeice and Recoome, then defeat Ginyu and the revived pair for the Ultimate Finish. Time Control and Mach Dash have explicit reward evidence in the existing local audit.

### PQ 110 — Heretics from a Dark World

A 7-star crossover quest. The Ultimate Finish requires keeping Rosé Goku Black above 50% and then defeating Mira. Divinity Unleashed, SS4 Wig & Tail, and Time Patrol Gi are preserved as documented rewards.

## Research target

The wiki distinguishes **indexed PQs** from **fully verified PQs**. A quest is not marked complete merely because its title or number has been indexed: reward tables and Ultimate Finish conditions must be checked before promotion.

Current structured audit coverage: **PQ1–PQ90** plus the previously documented spot-verified PQ examples. The remaining PQs will be processed in numbered batches so contradictions and historical research remain auditable.

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; the live explorer exposes the individual source records while detailed local verification proceeds.
