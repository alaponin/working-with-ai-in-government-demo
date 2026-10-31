# PAIRS — each sentence of the note, with the claim rows of CLAIMS.md it rests on

Headings that state no fact are paired with `none`. Checked by `a1_claims.py`, which cuts the note's sentences from `docs/NOTE.md` and compares them to this table, in order.

| # | Sentence of the note | Claims |
|---|---|---|
| 1 | One list of learners: what the prototype shows, and what it does not | K01b |
| 2 | To the Permanent Secretary, Ministry of Education, Youth and Skills | K01a, K01b, K02 |
| 3 | The prototype shows that a school clerk can enrol a child in a single list of learners, and that the registry does not register the same child twice when the child's names and date of birth are entered as the registry already holds them. | K03, K04, K06 |
| 4 | It does not show that the registry recognises the same child when the family name is spelt differently: of the eight invented children who appear on two lists, the search catches 4 of the 8 as one child, and holds each of the other four twice. | K05, K21a, K21b, K22, K23, K25 |
| 5 | What the prototype shows | none |
| 6 | The Ministry wants one list of learners instead of three. | K06 |
| 7 | The prototype is a small working model of that list, made so that the planning unit can agree what the registry is to do before the real one is built. | K07, K29 |
| 8 | A clerk enters a child's family name, given names, date of birth and school, and the registry searches for the child first. | K08, K09 |
| 9 | If it finds exactly one learner with the same family name, given names and date of birth, capital letters aside, it shows that learner and enters nothing new. | K04 |
| 10 | If it finds none, it gives the child a new learner number and saves the record. | K10 |
| 11 | The clerk sees which of the two happened. | K11 |
| 12 | An entry with a detail missing, a date of birth that does not name a real day, or a school other than the three is refused before the search; the clerk is told each fault, and nothing is saved. | K12a, K12b, K13a, K13b, K14 |
| 13 | The prototype runs on one computer and connects to nothing outside it. | K15, K16a, K16b |
| 14 | All of its checks pass, and none of them opens a window. | K17, K18a, K18b |
| 15 | The children on more than one list | none |
| 16 | The prototype holds 60 invented children in three schools, spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list. | K19a, K19b, K20 |
| 17 | Eight children are on two lists, and for four of them the family name on one list differs by a single letter. | K21a, K21b, K22 |
| 18 | The search catches 4 of the 8. | K23 |
| 19 | Those four have the same family name, given names and date of birth on both lists, and each is held once. | K24a, K24b |
| 20 | Each of the other four is held twice, under two learner numbers, because the search treats every difference other than capital letters as a different child. | K25, K26 |
| 21 | This is a limit of the search step as it is defined. | K27 |
| 22 | The invented data is made so that exactly four of the eight differ in this way: the figure shows how the rule behaves, not how many children a registry would hold twice on real lists. | K28 |
| 23 | What the prototype does not show | none |
| 24 | It is not the registry. | K29 |
| 25 | It is for agreement, it offers enrolment only, with no way to look a learner up, and it holds only invented data: Progressa is fictional, and every screen says so. | K29, K30, K31a, K31b, K31c |
| 26 | It is connected to no other body. | K16a, K32 |
| 27 | The three lists are part of the invented data; no system of the census, the examinations authority or the social grant programme is linked to it. | K20, K32 |
| 28 | It cannot tell apart two different children who share a family name, given names and date of birth. | K33a, K33b |
| 29 | The second would be taken for the first, and nothing new saved. | K33a, K33b |
| 30 | No two children in the invented data share all three. | K34 |
| 31 | Three points are kept in their simplest form. | K35 |
| 32 | An entry of blank characters of any kind, not only spaces, is treated as missing. | K36a, K36b |
| 33 | A school other than the three, once refused, is not shown again when the clerk returns to correct the entry. | K12b, K37 |
| 34 | Where the search finds more than one matching learner, the entry is refused and nothing is saved; this never arises in the invented data, and is checked only on a record added for the purpose. | K38a, K38b, K38c |
