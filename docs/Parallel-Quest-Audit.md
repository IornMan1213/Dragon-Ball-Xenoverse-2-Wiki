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

Structured in `pq-batch-12.json`. Covers the end of Super Pack 4 and the transition through Extra Packs 1 and 2. DLC ownership was cross-checked rather than inferred from numbering.

### Batch 13 — PQ121–PQ130

Structured in `pq-batch-13.json`. This block completes Extra Pack 2, covers Extra Pack 3, and begins Extra Pack 4. The maintained historical PQ transcription provides the objective sequences and documented basic rewards; GameFAQs independently confirms the key UF triggers for PQ121–127. citeturn0search0turn0search2turn0search3

- **PQ121 — Off-The-Charts Energy:** defeat all enemies, clear under eight minutes, then defeat Fu and the others; the Fu Super Soul is documented.
- **PQ122 — The Final Battle Before the Final Battle?!:** defeat enemies while leaving Beerus for last, then defeat Beerus and the others; Meditation and Power Rush are documented.
- **PQ123 — Planetary Possession:** keep Super Baby 2 above 50%, then defeat Omega, Eis, and Nuova Shenron; Reverse Shot and Variant Drive are documented. citeturn0search2
- **PQ124 — Downfall of the Ultimate Saiyan:** allow Super Baby 2 to heal at least three times before the final defeat sequence; Revenge Final Flash is documented. citeturn0search2
- **PQ125 — Proof's in the Potara:** keep Kefla above 50%, then defeat Ultra Instinct Goku, Beerus, and Champa; Blaster Ball and Ray Blast are documented. citeturn0search2
- **PQ126 — Catch Kefla If You Can!:** reach Kami's Lookout, clear in six minutes, then defeat Kefla and the others; Gigantic Breaker is documented. citeturn0search2
- **PQ127 — Multiverse Match of the Century:** defeat all enemies, clear in eight minutes, then defeat Kefla and the others; Gigantic Burst and Revenge Death Ball are documented. citeturn0search2
- **PQ128 — Legendary Super Saiyan Smackdown:** clear under eight minutes, then defeat Broly (Full Power Super Saiyan); Powered Shell and Gigantic Charge are documented.
- **PQ129 — Frieza Force on the Hunt:** keep an NPC above 50%, then defeat Gotenks and SSGSS Gogeta; Spirit Blaster and Punisher Shield are documented.
- **PQ130 — Legendary Starving Saiyan Broly:** keep Broly (Full Power Super Saiyan) above 50%, then defeat him; Gigantic Rage is documented. citeturn0search0

The source corpus also continues beyond this batch through PQ131–133, confirming that the audit should continue sequentially rather than treating PQ130 as the end of the DLC corpus. citeturn0search0

## Early verified examples

### PQ 11 — Burst Open and Mix!

A 2-star Saiyan Saga quest. Clear PQ10 first. The Ultimate Finish requires defeating Great Ape Vegeta within 10 minutes and then defeating the Time Patroller who appears. Earth Splitting Galick Gun is preserved as a documented UF reward in the existing local audit.

### PQ 18 — Force Entrance Exam

A 3-star Ginyu Force quest. Clear PQ17 first. Keep Guldo above 50%, defeat Burter, Jeice and Recoome, then defeat Ginyu and the revived pair for the Ultimate Finish. Time Control and Mach Dash have explicit reward evidence in the existing local audit.

### PQ 110 — Heretics from a Dark World

A 7-star crossover quest. The Ultimate Finish requires keeping Rosé Goku Black above 50% and then defeating Mira. Divinity Unleashed, SS4 Wig & Tail, and Time Patrol Gi are preserved as documented rewards.

## Research target

The wiki distinguishes **indexed PQs** from **fully verified PQs**. A quest is not marked complete merely because its title or number has been indexed: reward tables and Ultimate Finish conditions must be checked before promotion.

Current structured audit coverage: **PQ1–PQ130** plus the previously documented spot-verified examples. Remaining DLC PQs will be processed in numbered batches with the same provenance and conflict-preservation rules.

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- DLC catalog: https://dbxv2.fandom.com/wiki/DLC
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; the live explorer exposes the individual source records while detailed local verification proceeds.
