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

## Early verified examples

### PQ 11 — Burst Open and Mix!

A 2-star Saiyan Saga quest. Clear PQ 10 first. The Ultimate Finish requires defeating Great Ape Vegeta within 10 minutes and then defeating the Time Patroller who appears. **Earth Splitting Galick Gun** is a 50% Ultimate Finish reward in the current datamined reference.

### PQ 18 — Force Entrance Exam

A 3-star Ginyu Force quest. Clear PQ 17 first. Keep Guldo above 50%, defeat Burter, Jeice and Recoome, then defeat Ginyu and the revived pair for the Ultimate Finish. **Time Control** is a 40% Ultimate Finish reward and **Mach Dash** is a 40% first-clear bonus reward in the existing local audit.

### PQ 110 — Heretics from a Dark World

A 7-star crossover quest. The Ultimate Finish requires keeping Rosé Goku Black above 50% and then defeating Mira. **Divinity Unleashed** is a 25% first-clear skill reward; the quest also has the SS4 Wig & Tail and Time Patrol Gi reward pool.

## Research target

The wiki distinguishes **indexed PQs** from **fully verified PQs**. A quest is not marked complete merely because its title or number has been indexed: reward tables and Ultimate Finish conditions must be checked before promotion.

Current structured audit coverage: **PQ1–PQ10** plus the previously documented spot-verified PQ examples. The remaining PQs will be processed in numbered batches so contradictions and historical research remain auditable.

## Primary research corpus

- Structured public PQ records: https://github.com/Madreag/xenoverse_2_wiki/tree/main/content/parallel-quests
- Game/wiki Parallel Quest reference: https://dbxv2.fandom.com/wiki/Parallel_Quests
- Independent hidden-objective reference: https://twinfinite.net/guides/dragon-ball-xenoverse-2-parallel-quests/
- Maintained historical PQ transcription: https://steamcommunity.com/sharedfiles/filedetails/?id=808851543

> This page is the audit control sheet; the live explorer exposes the individual source records while detailed local verification proceeds.
