# Exhaustive TODO — Live Status Snapshot

**Last updated:** 2026-09-16

This is the live progress companion to [`TODO-EXHAUSTIVE.md`](./TODO-EXHAUSTIVE.md). It records the work completed in the current exhaustive research pass so the master TODO never loses the distinction between indexed, researched, partially verified, and fully verified.

## Current campaign

### Skills

- **Master source index:** present at `docs/data/skills.json`; it is still a seeded/indexed layer, not a verified encyclopedia. Its source category counts include 183 Ki Blast Supers, 130 Strike Supers, 110 Ki Blast Ultimates, 30 Strike Ultimates, 32 Other Supers, 20 Power-Up Supers, 23 Ki Blast Evasives, 16 Strike Evasives, 11 Other Evasives, 2 Power-Up Evasives, 10 Saiyan, 10 Majin, 4 Namekian, 4 Frieza Race, 4 Human, 37 unavailable-for-CaC, 25 Counter, and 18 Transformations. These are overlapping category counts and must **not** be summed as a unique skill total. fileciteturn88file0
- **Research batches:** 01, 02, 03, 04 and 05 exist. Batch 01 contains five records; Batch 02 contains six records that largely duplicate Batch 01; Batch 03 contains six; Batch 04 contains six; Batch 05 contains five. fileciteturn91file0 fileciteturn92file0 fileciteturn93file0 fileciteturn94file0 fileciteturn89file0
- **Field-level verification pass:** completed for all five Batch 05 records, but none is promoted to fully `verified` yet because important fields still require reconciliation.
- **New verification log:** `docs/data/skill-verification/skill-verification-01.json`.

### Batch 05 verification status

| Skill | Status | What was independently supported | Still needs verification |
|---|---|---|---|
| Divinity Unleashed | `partially_verified` | PQ 110, quest name, skill reward, 25% first-clear slot in the consulted research source | full mechanics/cost/CaC/shop audit |
| Super Dragon Fist | `partially_verified` | Strike Super, 100 Ki, Skill Shop, three-hit rush, notable users | current prerequisite, full CaC availability, patch audit |
| God Splitter | `partially_verified` | Ki Blast Super, 100 Ki, Zamasu training, guard cancel, projectile behavior | exact current lesson numbering, full CaC availability, patch audit |
| Kaioken Assault | `partially_verified` | Strike Super, 100 Ki base activation, multi-hit rush, health drain, historical 200-Ki patch change | current unlock, follow-up cost, current damage/vanish behavior, CaC audit |
| Burst Rush | `partially_verified` | Strike Super, 100 Ki, counter stance, four-hit rush, PQ 51, variant behavior | exact drop probability, current UF wording, CaC audit, patch audit |

Evidence used in this pass includes the PQ 110 research record, skill reference pages, the Zamasu instructor guide, and official Steam patch notes where applicable. citeturn2search0turn1search1turn1search6turn1search4turn2search2

### Batch 01 verification progress

A first source-check pass also covered the five Batch 01 records:

- **Quick Sleep:** source confirms Skill Shop, Majin-only CaC use, healing behavior, vulnerability, and Purification interaction. The repository's original `0 Ki` field conflicts with the consulted page's displayed `300 Ki`; this conflict must be resolved before promotion. citeturn4search0
- **Saiyan Blaster:** source confirms Conton City Patrol 10 / “Teach Me, Broly! (Part 2)”, Evasive classification, Ki Blast classification, 400 Stamina, and Awoken activation interaction. citeturn4search1
- **Gigantic Cluster:** existing research identifies PQ 163; an independent guide confirms the skill is one of the PQ 163 rewards, but exact drop mechanics still need stronger reconciliation. citeturn4youtube49
- **Remote Serious Bomb:** source confirms 300 Ki, two-stage operation, Awoken sealing effect, and 80% Tokipedia completion. citeturn4search4turn4search6
- **Impulse Slash:** source confirms TP Medal Shop, Strike Ultimate classification, 300 Ki, 32-hit rush and Awoken/guard interaction. citeturn4search3turn4search2

These five remain `partially_verified` until every required field in the master skill verification checklist is reconciled.

## Important discrepancies discovered

1. **Quick Sleep Ki cost:** repository research says `0`; consulted current reference shows `300`. Do not silently choose one. This is now an explicit verification conflict.
2. **Kaioken Assault acquisition:** repository research claimed Skill Shop/story progression, while the consulted current reference marks acquisition `TBA`. The claim is therefore not promoted.
3. **Burst Rush probability:** repository research says `30%`; consulted sources establish PQ 51 and the counter behavior but do not establish that exact probability. Keep the percentage unverified.
4. **God Splitter lesson number:** sources establish Zamasu training and the move's behavior, but the exact current lesson numbering needs reconciliation.
5. **Remote Serious Bomb:** the consulted sources support 80% Tokipedia completion rather than a generic “Extra Story completion” description; the canonical wording should be normalized to the more precise route once reconciled.

## Next research actions

- [ ] Resolve the five discrepancies above.
- [ ] Finish Batch 01 field-by-field.
- [ ] Deduplicate Batch 01/02.
- [ ] Finish Batch 03 field-by-field.
- [ ] Finish Batch 04 field-by-field.
- [ ] Finish Batch 05 field-by-field.
- [ ] Create Batch 06 from the next untouched canonical skills.
- [ ] Continue category-by-category until the entire canonical skill manifest has been audited.
- [ ] Only then promote individual records/fields to `verified`.
- [ ] Generate dedicated hard-written pages from verified/partially verified records.

## Exhaustive definition of done

A skill is **not** done when its name exists, when a wiki page exists, or when an unlock source is known. It is done only when the wiki has enough evidence to document identity, type, restrictions, costs, inputs, mechanics, acquisition, conditions, source provenance, version changes, related content, and unresolved uncertainty—and the page is discoverable by blanket search.

The same rule applies to every character, mission, item, Super Soul, QQ Bang, DLC, mechanic, mentor, shop, event, story chapter, build and guide in the project.
