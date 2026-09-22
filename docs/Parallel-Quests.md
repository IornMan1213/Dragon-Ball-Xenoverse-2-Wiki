# Parallel Quests (PQs)

Parallel Quests are the main side content of *Dragon Ball Xenoverse 2*. They feature alternate timelines and “what-if” scenarios and are a major source of skills, Super Souls, clothing, Zeni, and unlocks.

- Canonical local record layer: **186 numbered PQ records (PQ1–PQ186)**, including preserved historical numbering entries.
- External/datemined research may describe fewer standalone missions because of numbering gaps; those conflicts are preserved in the audit rather than replacing the canonical record layer.
- DLC: numbered PQs 101+ are tied to their canonical DLC identities in the relationship layer.

## Core Mechanics
- **Regular Finish** — basic clear condition
- **Ultimate Finish Activation** — secondary/hidden condition that opens the extended phase
- **Ultimate Finish Completion** — awards the best reward table (blue “Ultimate Finish” text)
- Failure mainly if the player team (you + up to 2 allies) is fully KO’d or the timer expires
- KO’d allies can be revived by staying near their body
- Skills and equipment drop either from specific enemies or randomly on Ultimate Finish
- Multiplayer shares newly obtained skills with the party
- Optional Patrollers in Training can drop materials, medals, clothing, and occasional Dragon Balls

## Practical Index of Notable Parallel Quests
Selected and organized from the full list for usefulness (farming, key skills, progression).

### Fast / High-Utility Routes
| # | Name | Stars | Notes |
|---|------|-------|-------|
| 44 / 45 | Dragon Ball farming routes | — | Canonical farming relationships identify both PQs as Dragon Ball routes; see the live explorer for quest details |
| 83 | Dangerous Duo! Warriors Never Rest | 7 | Canonical farming relationship; also a community route for Dragon Ball collection and Quest Tour rewards |
| 88 | Evil Seeks Dragon Balls Yet Again! | — | Canonical farming relationship for Dragon Ball collection |
| 4 | Prepare for the Attack of Saiyans! | 1 | Early clear |
| 15 / 22 / 44 / 45 / 68 / 83 / 88 | Dragon Ball farming routes | — | Complete current canonical farming relationship set; verify specific route mechanics in the live quest record |

### Notable Skill & Equipment Sources (Base Game Examples)
| # | Name | Examples of Notable Rewards |
|---|------|----------------------------|
| 2 | A Deal?! The Saiyan Brothers | Flying Nimbus!!, Spirit Slash |
| 8 | Invade Earth | Kaioken |
| 14 | Saiyan Pride | Kaioken Kamehameha |
| 24 | Super Saiyan Legend | Double Death Slicer |
| 57 | Hell is a Picture? | Gogeta’s Clothes, Rakshasa’s Claw |
| 59 | Potara Warrior | Vegito’s Clothes, Dimension Cannon |
| 76 | Eternal Rival | Warp Kamehameha |
| 95 | Super 17, the Ultimate Android | Drain Field, Flash Bomber |
| 100 | The Ultimate Rivalry | x100 Big Bang Kamehameha |

### Higher-Difficulty & DLC Highlights
- Many 6-star and 7-star base PQs gate strong skills and clothing behind Ultimate Finish or specific enemy order.
- **Super / Extra / Ultra / Legendary / Hero of Justice packs**: Add large numbers of 7-star PQs tied to new characters (Universe 6, Goku Black/Zamasu, Tournament of Power, Broly Full Power, Gammas, Beast, etc.).
- **Future Saga Chapters 1–4**: Extensive set of high-difficulty PQs (roughly 163+) with new skills (including Dragon Spiral, Indomitable, Venus Fist and others), artwork, and some of the highest Zeni rewards in the game. Chapter 4 contains some of the newest content.

## Canonical Relationship & Navigation Notes
The repository treats `docs/data/pq-reward-relationships.json` as the authoritative relationship layer. The current canonical PQ relationship census is **859 unique edges** across skills, Super Souls, equipment, characters, DLC, and farming. The maintained local explorer is the presentation surface for the 186 canonical PQ records.

- **Skill rewards:** resolve through the canonical PQ → Skill relationship layer and the local Skills explorer.
- **Super Souls:** resolve through the canonical PQ → Super Soul relationship layer; detailed per-record navigation currently uses the local Search surface.
- **Equipment/accessories:** resolve through the canonical equipment/accessory relationship projections; known naming conflicts remain explicit rather than being silently merged.
- **DLC:** PQ requirements resolve through individual canonical DLC identities; broad bundle labels such as `Super Pass` are presentation metadata and do not replace individual pack identities.
- **Characters:** character navigation is derived from explicit canonical `pq_features_character` relationships, not inferred from generic enemy text.
- **Farming:** the canonical farming relationship layer currently contains seven Dragon Ball routes: **PQ15, PQ22, PQ44, PQ45, PQ68, PQ83, and PQ88**.

## Farming Guidance
- Use the canonical farming routes above as the repository's relationship-backed route set.
- Do not treat a community claim that one PQ is “fastest” as canonical acquisition data; route-efficiency claims remain separate from the relationship itself.
- Ultimate Finish requirements must be checked from the individual PQ record when hunting a specific reward; a farming relationship does not imply a particular drop condition.
- Use the live [Parallel Quest Explorer](Parallel-Quests-All.html) for the maintained numbered records and current structured reward/navigation fields.
- Check the in-game second page of each PQ for the exact current reward table when the repository marks a reward condition as unresolved.

**Sources**:  
User-supplied Parallel Quest compilation (mechanics + full numbered list with conditions and rewards), used as the basis for this practical, original index and summary. Cross-referenced with known high-value community routes.

This page continues to grow as a useful local reference. Specific ranges or individual PQs can be detailed further on request without turning the file into a raw encyclopedia dump.
