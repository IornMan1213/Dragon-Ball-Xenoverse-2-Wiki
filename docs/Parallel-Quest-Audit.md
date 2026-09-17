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

The first structured audit batch now covers PQ1–PQ10. Quest names, star bands, objective sequences, lose conditions, and the historically documented basic reward lists were cross-checked against the maintained 186-PQ transcription and an independent 100-PQ hidden-objective reference.

The batch deliberately does **not** convert a skill appearing in a historical basic-reward list into a guaranteed or Ultimate-Finish-only reward. Exact reward-slot probabilities remain unresolved until the underlying reward tables or sufficiently explicit current evidence establish them.

- **PQ1 — Being a Time Patroller:** finish Elder Kai's trial, defeat the Saibamen, then Yamcha and Tien; 120 Zeni and Energy Capsule S are documented basic rewards.
- **PQ2 — A Deal?! The Saiyan Brothers:** defeat all enemies, defeat Raditz last, then Kid Gohan; the historical reward list includes Spirit Slash.
- **PQ3 — World Tournament Tag Team:** defeat Yamcha/Krillin/Tien, clear under five minutes, then defeat Piccolo/Gohan; Solar Flare is listed among the rewards.
- **PQ4 — Prepare for the Attack of Saiyans!:** defeat Gohan/Piccolo, clear under five minutes, then defeat Goku and revived Piccolo; Paralyze Beam is listed among the rewards.
- **PQ5 — Saiyan Blood:** defeat Piccolo/Goku, keep Raditz above 50%, then defeat Gohan and revived Goku; Kamehameha is listed among the rewards.
- **PQ6 — Saibamen's Revenge:** defeat all enemies, clear under five minutes, then defeat Nappa and the Saibamen; Meteor Strike is listed among the rewards.
- **PQ7 — Attack of the Saiyans:** defeat Raditz/Nappa/Vegeta, all Saibamen, and all revived Saiyans; Shine Shot is listed among the rewards.
- **PQ8 — Invade Earth:** defeat Goku, keep Nappa alive, then defeat revived Goku; Kaioken is listed among the rewards.
- **PQ9 — The Saiyan King is...Who?:** defeat Nappa, keep Vegeta above 50%, then defeat Great Ape Nappa; Meteor Blow is listed among the rewards.
- **PQ10 — Saiyan Survivors:** defeat all enemies, clear under five minutes, then defeat Piccolo and Gohan; Wall of Defense and Unrelenting Barrage are listed among the rewards.

The structured source is `docs/data/parallel-quest-research-batches/pq-batch-01.json`.

### Batch 2 — PQ11–PQ20

PQ11–PQ20 are now structured in `pq-batch-02.json`, with objective sequences, lose conditions, documented basic rewards, and skill-reward candidates cross-checked against the maintained 186-PQ transcription and independent hidden-objective references. PQ11's Earth Splitting Galick Gun Ultimate Finish condition is preserved as an explicitly documented UF reward; other reward-slot semantics remain unresolved where the evidence is insufficient.

### Batch 3 — PQ21–PQ30

PQ21–PQ30 are now structured in `pq-batch-03.json`. The audit captures the five-minute, three-minute, Dragon Ball recovery, escort/health-threshold, and revived-enemy Ultimate Finish sequences across this block, along with documented basic rewards and associated skill candidates. Exact reward-slot/drop percentages remain unresolved unless directly established.

### Batch 4 — PQ31–PQ40

PQ31–PQ40 are now structured in `pq-batch-04.json`. This block covers the Cell-training and Cell Games sequence through the Future Warriors quest, including the eight-warrior training condition at PQ31, Cell Jr. requirements at PQ32/PQ37, the Ginyu return at PQ34, Cell health protection at PQ35, the three-minute Cell condition at PQ37, the ten-minute Power Teams condition at PQ38, the Vegeta/Piccolo survival requirement at PQ39, and the eight-minute Future Gohan/Trunks condition at PQ40.

- **PQ31 — Let's Train:** defeat eight warriors, have Vegeta and Gohan transformed, then defeat revived Gohan; Super Dragon Flight is documented in the reward list.
- **PQ32 — Multiple Cell Jr. Hunt:** defeat seven Cell Jr., clear under five minutes, then defeat Cell and every Cell Jr.; Energy Barrier is documented.
- **PQ33 — Earth in Danger!:** defeat Cell, all enemies, and all revived enemies; Death Psycho Bomb is documented.
- **PQ34 — Return of Ginyu Force!:** defeat all Ginyu Force members, clear under five minutes, then defeat Frieza and revived Ginyu; Paralysis is documented.
- **PQ35 — Miscalculations in Time:** defeat the training Time Patroller, keep Cell above 50%, then defeat Gohan; the documented basic reward list contains the Super Soul "I wanted to kill you with my own hands.".
- **PQ36 — The Cell Games Begin:** defeat Piccolo and Goku before Gohan, then defeat Gohan with Cell surviving; Evil Whirlwind is documented. A newer datamined corpus claims PQ36 was cut, while the maintained game-specific reward transcription and independent guides document PQ36 directly, so this contradiction remains explicitly flagged for later reconciliation.
- **PQ37 — Clash! Perfect Cell!:** defeat Cell and each Cell Jr., clear under three minutes, then defeat both Cells; Instant Rise is documented.
- **PQ38 — Power Teams:** defeat Goku and Cell, clear within ten minutes, then defeat revived Gohan and Cell; Shining Slash is documented.
- **PQ39 — 17 and 18 of the Official History:** defeat Android 17 and 18, keep Vegeta and Piccolo alive, then defeat Android 16 and the revived Androids 17 and 18; Side Bridge is documented.
- **PQ40 — The Future Warriors!:** defeat all enemies, clear within eight minutes, then defeat Future Gohan and Trunks; Heat Dome Attack is documented.

### Batch 5 — PQ41–PQ50

PQ41–PQ50 are now structured in `pq-batch-05.json`. This block covers the Future Androids, future Dragon Ball collection quests, Android 16's history, the Broly/Vegeta protection quest, the second World Tournament, Namek training, and the first large Majin Buu cleanup quest. Core Ultimate Finish triggers and documented reward lists were independently cross-checked; exact random reward-slot/drop percentages remain unresolved.

- **PQ41 — Warriors' Annihilation - Future Chapters:** defeat Gohan, keep Android 17 and 18 alive, then defeat Trunks; Burning Attack is documented.
- **PQ42 — Artificial Warriors:** defeat Android 16, 17, and 18, defeat all Cell Jr., then defeat Cell and the revived Androids; Rolling Bullet is documented. The skill's exact reward slot remains unresolved here because historical basic-reward listings do not by themselves establish the acquisition roll.
- **PQ43 — Change the Future:** defeat all enemies, keep Future Gohan above 50%, then defeat Cell; Change The Future is documented.
- **PQ44 — Dragon Balls of the Future:** recover six Dragon Balls, defeat all enemies, then recover the seventh; God Breaker and Burning Slash are documented.
- **PQ45 — Take Back the Dragon Balls!:** recover six Dragon Balls, defeat all Cell Jr., then recover the seventh; Taunt is documented.
- **PQ46 — 16 of the Official History:** defeat all enemies while keeping Android 16 alive, then defeat Cell; Chain Destructo-Disc Barrage is documented.
- **PQ47 — Daddy! Don't Die!:** defeat Broly and Majin Buu, keep Vegeta above 50%, then defeat Broly; the documented basic rewards include Broly's Clothes and the Super Soul "A monster? No, I'm a devil!".
- **PQ48 — 2nd World Tournament Tag Team:** defeat Android 18, Goten, and Trunks, clear under five minutes, then defeat all appearing enemies; Kamekameha is documented.
- **PQ49 — Namek Berserker:** defeat Goten, Gohan, and Piccolo, clear under five minutes, then defeat Nail and revived Piccolo; Do or Die is documented.
- **PQ50 — Majin Chaos:** defeat 30 small Majin Buu, clear within ten minutes, then defeat Majin Buu and Super Buu; Explosive Buu Buu Punch is documented.

## Early verified examples

### PQ 11 — Burst Open and Mix!

A 2-star Saiyan Saga quest. Clear PQ 10 first. The Ultimate Finish requires defeating Great Ape Vegeta within 10 minutes and then defeating the Time Patroller who appears. **Earth Splitting Galick Gun** is a 50% Ultimate Finish reward in the current datamined reference.

### PQ 18 — Force Entrance Exam

A 3-star Ginyu Force quest. Clear PQ 17 first. Keep Guldo above 50%, defeat Burter, Jeice and Recoome, then defeat Ginyu and the revived pair for the Ultimate Finish. **Time Control** is a 40% Ultimate Finish reward and **Mach Dash** is a 40% first-clear bonus reward in the existing local audit.

### PQ 110 — Heretics from a Dark World

A 7-star crossover quest. The Ultimate Finish requires keeping Rosé Goku Black above 50% and then defeating Mira. **Divinity Unleashed** is a 25% first-clear skill reward; the quest also has the SS4 Wig & Tail and Time Patrol Gi reward pool.

## Research target

The wiki distinguishes **indexed PQs** from **fully verified PQs**. A quest is not marked complete merely because its title or number has been indexed: reward tables and Ultimate Finish conditions must be checked before promotion.

Current structured audit coverage: **PQ1–PQ50** plus the previously documented spot-verified PQ examples. The remaining PQs will be processed in numbered batches so contradictions and historical research remain auditable.

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; the live explorer exposes the individual source records while detailed local verification proceeds.
