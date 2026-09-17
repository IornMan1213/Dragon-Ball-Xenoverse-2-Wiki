---
layout: wiki
title: Parallel Quest Audit
---

# Parallel Quest Audit

> **Browse the live quest catalog:** [Every Parallel Quest](Parallel-Quests-All.html)

This is the exhaustive Parallel Quest verification pass. The audit covers the numbered PQ range through PQ186, while distinguishing **quest-number coverage** from the number of currently available quests. Current maintained datamined research reports **183 standalone PQs**, with **PQ36 absent/cut**, so the catalog must not imply that all numbers 1–186 correspond to live quests. citeturn0search0

## Record standard

Each structured PQ record should contain:

- PQ number and official name
- Star difficulty
- Unlock condition
- DLC requirement, when applicable
- Win and lose conditions
- Base clear rewards
- Skill rewards and exact drop condition where established
- Super Soul / outfit / accessory / item rewards
- Ultimate Finish trigger
- Verification date and source provenance

## Current verified coverage

### Batch 1 — PQ1–PQ10
Structured in `pq-batch-01.json`. Early Saiyan-era quests were cross-checked against the maintained PQ transcription and independent hidden-objective references. Exact reward-slot probabilities remain unresolved where sources do not establish them.

### Batch 2 — PQ11–PQ20
Structured in `pq-batch-02.json`. Covers Saiyan, Namek, and Ginyu Force quests, preserving explicit evidence such as PQ11's Earth Splitting Galick Gun UF reward and PQ18's Time Control/Mach Dash rewards.

### Batch 3 — PQ21–PQ30
Structured in `pq-batch-03.json`. Covers Frieza/Namek, Cooler, Android, and Hercule quests, including Dragon Ball recovery, time-limit, escort, and revived-enemy conditions.

### Batch 4 — PQ31–PQ40
Structured in `pq-batch-04.json`. Covers Cell training through Future Warriors. **PQ36 is a preserved historical conflict:** the historical maintained Steam/game-specific transcription lists a PQ36, while current maintained datamined research identifies PQ36 as cut and the live numbering as skipping 36. The audit preserves the evidence rather than silently deleting the historical record. citeturn0search0turn0search1

### Batch 5 — PQ41–PQ50
Structured in `pq-batch-05.json`. Covers Future Androids, Dragon Ball collection, Android 16, Broly/Vegeta protection, World Tournament, Namek training, and Majin Buu quests.

### Batch 6 — PQ51–PQ60
Structured in `pq-batch-06.json`. Covers Great Saiyaman, Super Saiyan bargain, Majin Buu, Gotenks, Hercule, Janemba, Potara, and Super Spirit Bomb quests.

### Batch 7 — PQ61–PQ70
Structured in `pq-batch-07.json`. Covers Cell Games continuation, Frieza rematch, Beerus/Whis, Super Saiyan God, Dragon Ball recovery, God of Destruction, and Golden Frieza/Metal Cooler quests.

### Batch 8 — PQ71–PQ80
Structured in `pq-batch-08.json`. Covers Golden Frieza/Frieza Force assaults, Galactic Patrol training, Beerus/Whis training, Goku/Vegeta rivalry, parent-and-child training, Broly revival, and Great Ape festival quests.

### Batch 9 — PQ81–PQ90
Structured in `pq-batch-09.json`. Covers later Gogeta, Golden Frieza/Metal Cooler, Broly/Dragon Ball, Saiyan, Yamcha, Dragon Ball collection, ultimate-series, and great-evil-alliance quests. Exact random reward-slot percentages remain unresolved where unsupported.

### Batch 10 — PQ91–PQ100
Structured in `pq-batch-10.json`. Completes the 100-quest base-game audit block, covering the Saiyan Revolt, Baby/Tuffle conflict, GT scenarios, Shadow Dragons, Super 17, Mira/Towa, villain regrouping, Frieza-race invasion, and final SSGSS rivalry.

### Batch 11 — PQ101–PQ110
Structured in `pq-batch-11.json`. Covers Super Packs 1–4. Major Ultimate Finish triggers and documented basic rewards were cross-checked; exact random reward-slot percentages remain unresolved except where current maintained data establishes them.

### Batch 12 — PQ111–PQ120
Structured in `pq-batch-12.json`. Covers the end of Super Pack 4 and transition through Extra Packs 1–2. DLC ownership was cross-checked rather than inferred from numbering.

### Batch 13 — PQ121–PQ130
Structured in `pq-batch-13.json`. Completes Extra Pack 2, covers Extra Pack 3, and begins Extra Pack 4. Historical objective/reward transcription and current maintained records were cross-checked.

### Batch 14 — PQ131–PQ140
Structured in `pq-batch-14.json`. Covers the remainder of Extra Pack 4 and Ultra Packs 1–2. Current maintained quest records provide 7-star classification and, where established, datamined reward-slot percentages; the maintained Steam transcription independently confirms the objective/reward lists.

### Numbering gap — PQ141–PQ150
The audit intentionally records the numbering gap rather than fabricating ten quests. The next populated block begins at PQ151.

### Batch 15 — PQ151–PQ160
Structured in `pq-batch-15.json`. Covers the Conton City Vote Pack and Hero of Justice Packs 1–2. The historical Steam transcription confirms the quest names, DLC labels, win/lose conditions, and basic reward lists, while the maintained corpus supplies 7-star classification and exact reward-slot percentages where established.

### Batch 16 — PQ161–PQ170
Structured in `pq-batch-16.json`. Covers the final Hero of Justice Pack 2 quests and Future Saga Chapter 1. Steam's maintained 186-PQ transcription independently confirms the quest names, DLC labels, objective sequences, lose conditions, and documented reward lists; GameFAQs independently corroborates the Ultimate Finish objective sequences for the later quests.

### Batch 17 — PQ171–PQ180
Structured in `pq-batch-17.json`. Covers Future Saga Chapters 1–2 and the Dragon Ball DAIMA Pack. The maintained Steam transcription independently confirms the quest names, DLC labels, objective sequences, lose conditions, and documented reward lists; GameFAQs corroborates the Ultimate Finish objective sequences for PQ171–178.

### Batch 18 — PQ181–PQ186
Structured in `pq-batch-18.json`. This is the final numbered block. The maintained Steam 186-PQ transcription confirms the six quest names, DLC assignments, objective sequences, lose conditions, and documented rewards; GameFAQs independently corroborates the Ultimate Finish sequences. The structured records explicitly leave exact reward-slot/drop percentages unresolved where they are not established. fileciteturn848file0L2-L10

- **PQ181 — The Greatest Training Ever:** clear under 15 minutes, then defeat Beerus and the others; Super Kamehameha (SS4 DAIMA) and Final Flash (SS3 DAIMA) are documented.
- **PQ182 — Frieza's Fervent Wish:** clear under 10 minutes, then defeat SSGSS Gogeta; Dark Inscription is documented.
- **PQ183 — Broly vs. Broly:** clear under 10 minutes, then defeat Broly; Emperor's Cannon is documented.
- **PQ184 — The Invincible Duo:** clear under 9 minutes, then defeat SS4 Goku (DAIMA) and the others; Chaotic Time Impact is documented.
- **PQ185 — A God's Amusement:** clear under 10 minutes, then defeat Fused Zamasu (Half-Corrupted); Dragon Spiral and Indomitable are documented.
- **PQ186 — Frieza's Right-Hand Man:** clear under 14 minutes, then defeat Golden Frieza and the others; Venus Fist is documented.

## Early verified examples

### PQ 11 — Burst Open and Mix!
A 2-star Saiyan Saga quest. Clear PQ10 first. The Ultimate Finish requires defeating Great Ape Vegeta within the documented time condition and then defeating the appearing Time Patroller. Earth Splitting Galick Gun remains preserved as a documented UF reward.

### PQ 18 — Force Entrance Exam
A 3-star Ginyu Force quest. Clear PQ17 first. The existing audit preserves the explicit Time Control and Mach Dash reward evidence.

### PQ 110 — Heretics from a Dark World
A 7-star crossover quest. The existing audit preserves the Rosé Goku Black health condition, Mira Ultimate Finish, Divinity Unleashed, and associated documented rewards.

## Research target

The wiki distinguishes **numbered audit coverage** from **currently available PQs**. A quest is not marked complete merely because its title or number has been indexed: objectives, rewards, and Ultimate Finish conditions must be checked before promotion.

**Current structured audit coverage: numbered PQ1–PQ186, with known numbering gaps preserved.** The audit is structurally complete, but a final cross-link consistency pass remains: every documented skill reward should resolve to exactly one canonical skill key, and every skill record claiming a PQ source should resolve back to a numbered PQ audit record. Current research supports 183 standalone PQs because PQ36 is cut; the historical PQ36 evidence remains preserved for auditability. citeturn0search0

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- DLC catalog: https://dbxv2.fandom.com/wiki/DLC
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; detailed structured records remain in `docs/data/parallel-quest-research-batches/` while the live explorer exposes the public catalog.
