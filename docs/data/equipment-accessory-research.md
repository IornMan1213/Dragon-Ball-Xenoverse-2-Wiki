# Equipment Accessories — Research Layer

This layer separates **accessories** from stat-bearing clothing. Accessories must be catalogued independently because an accessory can have its own acquisition route, character/theme provenance, gender/race applicability, DLC provenance, and cosmetic behavior.

## Accessory record standard

For every discovered accessory, record where possible:

- Exact displayed name
- Stable research ID
- Accessory category/type
- Character/theme provenance
- Acquisition route
- Quest/shop/event/source
- DLC or free-update provenance
- Race/gender restrictions when documented
- Whether it affects combat statistics
- Whether it is purely cosmetic
- Whether it is a wig, scouter, tail, mask, weapon-like cosmetic, staff, halo, aura, emblem-like item, or other special accessory
- Duplicate/variant relationship
- Version sensitivity
- Collection-inclusion status when known
- Verification state
- Source provenance

A missing field means **not established**, not that the value is zero, unrestricted, or unavailable.

## Expanded accessory population

The research layer currently contains 57 indexed accessory entries. These are deliberately separated from clothing records and are not treated as fully verified merely because an item appears in a historical list.

| ID range | Coverage |
|---|---|
| acc-001–016 | Base headwear, wigs, halos and wings |
| acc-017–028 | Old, standard and New Model Scouter variants |
| acc-029–039 | Swords, staffs, props and specialty headwear |
| acc-040–044 | DLC/gift accessories and Golden-form accessories |
| acc-045–053 | Raid, Crystal Raid and STP-related accessory research |
| acc-054–057 | Newer free-update/special-accessory research leads |

## Acquisition evidence notes

Current equipment indexes separate accessories from upper/lower/hands/feet clothing and identify shop items, PQ rewards, TP Medal Shop items, wishes, raids and DLC-related items. These sources are useful for discovery, but historical entries are not automatically treated as current-version guarantees.

Sources:
- https://www.gameskinny.com/tips/dragon-ball-xenoverse-guide-equipment-and-accessory-list/
- https://dragonballxenoverse2.wiki/unlockables/outfits/

Historical accessory lists provide acquisition leads such as Piccolo's Turban from PQ03, Goku's Wig from PQ10, Goku's Super Saiyan Wig from PQ18, Tapion's Sword from PQ22, Z-Sword from PQ35, and several scouter families from the Accessory Shop. These remain research evidence rather than automatic current-version guarantees.

Source: https://steamcommunity.com/sharedfiles/filedetails/?id=403805311

Raid research documents additional accessories including Golden Scouter, Android 21 Wig & Glasses, Tapion Wig, Frieza's Head (Final Form), Golden Great Ape Hat & Tail, Super Saiyan Rosé Wig, Fused Zamasu Wig, and Tiencha Wig. Raid appearances are stored separately from permanent shop routes because event availability can differ.

Source: https://steamcommunity.com/app/454650/discussions/0/5362100230210878233/

Character Gift research independently reports equipment pools for Goku, Gohan (Kid), Nappa, Vegeta, and other mentors, including SS Rosé Wig, Golden Great Ape Hat and Tail, and Golden Scouter. These remain partially verified until historical gift behavior is reconciled with current-version availability.

Source: https://gamefaqs.gamespot.com/boards/190457-dragon-ball-xenoverse-2/77816881

Official Time Patrol Support Pack documentation confirms Frieza's Head (Final Form) and Korin Wig with Ears & Tail as included accessories and notes that some included content can also be obtained through in-game shops or conditions. DLC ownership is therefore stored separately from the actual acquisition route.

Sources:
- https://www.bandainamcoent.com/games/dragon-ball-xenoverse-2/downloadable-content
- https://www.xbox.com/en-US/games/store/dragon-ball-xenoverse-2-time-patrol-support-pack/9NRRJXR84XT0

## Important distinctions

### Accessory vs clothing

Accessories are their own equipment category. Do not convert an accessory into an upper/lower/hands/feet clothing record merely because it completes a visual costume.

### Raid reward vs permanent acquisition

A raid appearance is not automatically a permanent shop route. Some raid rewards have alternate routes while others may be limited or event-dependent. Preserve each route independently.

### DLC ownership vs unlock method

A DLC store listing proves that the accessory belongs to that content package; it does not by itself prove the player's current in-game acquisition condition. Keep both fields.

### Collection percentage

Collection-completion behavior remains a separate research problem. Do not assume every raid/event/special accessory contributes to the same completion percentage until the game behavior is documented.

## Verification states

- **indexed** — accessory identity discovered.
- **partially_verified** — identity plus some acquisition/provenance evidence established.
- **verified** — identity, current acquisition, restrictions, and relevant behavior reconciled against sufficient evidence.

No accessory should be promoted solely because a DLC store page, historical guide, or community list names it.

## Next population targets

1. Finish the base Accessory Shop catalog.
2. Expand all PQ-specific accessories.
3. Expand TP/STP Medal Shop accessories.
4. Build complete raid/event accessory tables with event provenance.
5. Expand Character Gift reward pools.
6. Add DLC accessories by pack/chapter.
7. Resolve race/gender restrictions per accessory.
8. Reconcile collection-percentage inclusion rules.
9. Add version/discontinued-route history.
10. Cross-link accessories to their associated clothing sets, characters, mentors, PQs, raids, DLC, and shop records.
