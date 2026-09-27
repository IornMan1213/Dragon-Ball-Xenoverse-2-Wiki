# PQ reward normalization

Typed reward maps convert the mixed reward arrays in PQ batch records into explicit cross-domain relationships: skills, Super Souls, clothing, accessories, and artworks.

`pq-163-186-reward-map.json` is the first populated tranche. Empty arrays are intentionally conservative: they mean the current source-backed reward list did not establish that reward type for that PQ, not that no alternate acquisition route exists.

This layer remains `partially_verified` until every PQ reward is normalized and every collectible resolves to a canonical record in its target domain.
