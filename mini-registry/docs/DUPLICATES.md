# The duplicates count — how many of the 8 the search catches

*Round 7 of the brief (`../brief/MINI-REGISTRY-BRIEF.md:54`), a checking round. Invented data, Progressa is fictional.*

**The search catches 4 of the 8.**

The figure is the counting program's own last line, `_working/round-07-duplicates/_evidence/count.py --stage count`, run over the data as `node reset.js` made it at 2026-10-31 20:21 UTC (log `_working/round-07-duplicates/_evidence/A3_count.log`):

```text
the search catches 4 of the 8
```

**How it was counted.** The 8 are the children the key table (`src/data/key_table.json`) names, by `same_child`, on two list entries (`list_entry`); the set was listed first, 8 children, each on exactly two entries. For each entry, the learner number it made or found was read from the reset's record of what the search did, `src/data/enrolments.json` (ruling Q-12). A child is **caught** where both its entries point to one learner, **missed** where they point to two. The reason is read from the three list files, field by field, on the three fields the search compares — family name, given names, date of birth — capitals ignored. The same table, as data, is `docs/count/duplicates.csv`.

| Child | Its two list entries | Learner number each made or found | Caught | Fields that differ between the entries |
|---|---|---|---|---|
| C19 | school census 10 · social grant list 7 | 10 · 10 | yes | none — "Praquinvel", "Joren Kekesa", 2017-04-19 on both |
| C24 | school census 20 · candidate list 20 | 20 · 42 | **no** | family name: "Prarasel" (census) against "Praresel" (candidate list) |
| C26 | candidate list 22 · social grant list 17 | 44 · 44 | yes | none — "Velnokgal", "Tovsan", 2016-10-11 on both |
| C31 | school census 11 · candidate list 13 | 11 · 11 | yes | none — "Miquin", "Madanta Celcello", 2019-12-11 on both |
| C50 | school census 17 · social grant list 19 | 17 · 61 | **no** | family name: "Temnok" (census) against "Tomnok" (grant list) |
| C53 | school census 13 · candidate list 8 | 13 · 13 | yes | none — "Orobenwes", "Celgrelo Maisa", 2014-12-17 on both |
| C56 | school census 22 · social grant list 9 | 22 · 52 | **no** | family name: "Orowes" (census) against "Orowus" (grant list) |
| C58 | candidate list 14 · social grant list 2 | 36 · 46 | **no** | family name: "Tumitem" (candidate list) against "Tomitem" (grant list) |

Each of the four missed differs in its family name by one letter and in nothing else; each of the four caught matches on all three fields letter for letter, in the same capitals. Each missed child is held twice, under two learner numbers.

**What the figure shows, and what it does not.** It shows that the brief's own rule — the search for "exactly one learner with the same family name, given names and date of birth (capitals ignored)" (brief line 13) — joins the 4 of the 8 whose three fields match and, for each of the 4 "whose family name is spelt differently on one list" (brief line 26, R-12), "a second record for the same child, with a new learner number … so that the registry registers the same child twice", "a limit of the search step, the brief's own rule" (F-5); it does not show how the real registry would fare on real lists, for the data is invented and made so that 4 of the 8 differ by one letter in the family name alone, and "the prototype is for agreement. It is not the registry" (brief line 7).
