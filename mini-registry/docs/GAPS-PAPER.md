# The register's open questions — a decision paper for the owner's ruling

**What this is.** The register of requirements (`docs/REQUIREMENTS.md`) closes with fourteen open questions. G-14 is already closed (below). This paper answers the other thirteen, G-01 to G-13, so that you can rule on them in one act and round 2, the groundwork, can be drafted from the brief, the register and your ruling. **Every recommendation here is a proposal for your ruling, not a decision.** Nothing in this paper changes the brief or the register.

**How to read a passage.** A passage is quoted word for word after its file and line, as `` `<path>:<line>` «<words>» ``. Paths are relative to the estate's root: the brief is `../brief/MINI-REGISTRY-BRIEF.md`, the register is `docs/REQUIREMENTS.md`. In the tables, "line N" is the brief's line N and "register line N" is the register's, each quoted above its table.

**How the positions are judged.** Each section quotes every line of the register that names its question, then names the settings, counts and screens open to every position and gives them to all ("Given to every position"). The table then judges the positions on what divides them, and no cell denies a position a fact this paper grants elsewhere.

**The four tests, the same for every question.**

- **(a) For agreement, not the registry.** `../brief/MINI-REGISTRY-BRIEF.md:7` «the planning unit wants to see a small working prototype: a school clerk enrols a child, and the registry does not register the same child twice. The prototype is for agreement. It is not the registry.» A position that adds a goal, a screen, a body to connect to or a field the clerk enters fails this test. Where every position adds the same, the test does not divide them, and the row says so.
- **(b) The "must not" sentences.** `../brief/MINI-REGISTRY-BRIEF.md:33` «Hold any real person's data. Every screen says "Invented data, Progressa is fictional".» · `../brief/MINI-REGISTRY-BRIEF.md:34` «Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.» · `../brief/MINI-REGISTRY-BRIEF.md:35` «Open a window on its own. Every check of the screens runs without one.»
- **(c) Known numbers.** `../brief/MINI-REGISTRY-BRIEF.md:29` «The numbers are fixed so that every later count has a known answer. The data is made the same way every time it is reset.»
- **(d) What the later rounds must do with it.** `../brief/MINI-REGISTRY-BRIEF.md:52` «The scaffold and the made-up data, in the known numbers above» · `../brief/MINI-REGISTRY-BRIEF.md:53` «The goal built» · `../brief/MINI-REGISTRY-BRIEF.md:54` «The duplicates count: how many of the 8 the search catches»

**The search rule is not widened anywhere in this paper.** The only rule that says two entries are the same child is the brief's: `../brief/MINI-REGISTRY-BRIEF.md:13` «if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;» No recommendation below matches on anything else, and none forgives anything but capitals.

## The question already closed

**G-14 — closed, not reopened.** The orchestrator closed it from the brief, which forgives capitals and nothing else: `../brief/MINI-REGISTRY-BRIEF.md:13` «(capitals ignored)» — so a space is part of a name.

## Summary — the thirteen recommendations

| Question | What we recommend, in a few words |
|---|---|
| G-01 | A whole number in sequence, one above the highest held, never given twice |
| G-02 | Never reached under the data's settings; if it is, enter nothing new and refuse the entry |
| G-03 | At reset every list entry is enrolled by the brief's own rule; the search then looks among learners only |
| G-04 | 60 different children; the entries counted apart — 68, with each of the 8 on exactly two lists |
| G-05 | A key table of the made-up data, read by the counts and never by the search; none of the 8 differs in capitals only |
| G-06 | Age in completed years on one fixed date held in the settings; 6 and 12 included |
| G-07 | Date as YYYY-MM-DD; school chosen from the three; all four entered before the search |
| G-08 | Enrolment the only goal; reset is a command, and there is no screen for looking learners up |
| G-09 | Every view the clerk can see is a screen, messages and refusals included |
| G-10 | Evidence by construction: a generator in the source, a fixed seed, and the reset's reads recorded |
| G-11 | None: the three lists are data inside the prototype, not bodies it connects to |
| G-12 | The register's tests R-01 to R-21 as programs, with the cases round 3 adds |
| G-13 | One A4 page, as a PDF, counted by its page count |

The thirteen fit together: G-03, G-04 and G-05 together give round 7 a known answer before it runs — **4 of the 8 caught** — and give round 5 a known number of learners after reset — **64** (60 children, and the 4 the rule does not catch each held twice). Both figures follow from the recommendations and stand or fall with your ruling on them.

---

## G-01 — the learner number

> **G-01** (R-06) What does a learner number look like, and how is a new one made?

**Bears on:** R-06. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:14` «if it finds none, it gives the child a new learner number and saves the record;»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The data is made the same way every time it is reset.»
- `docs/REQUIREMENTS.md:91` «read the number of learners and every learner number the registry holds (what a learner number looks like: gap G-01; where the search looks: gap G-03)»
- `docs/REQUIREMENTS.md:93` «each new learner number unlike every number held before it»
- `docs/REQUIREMENTS.md:211` «reset the data and keep a copy of it; enrol one child; reset the data again and keep a second copy.»
- `docs/REQUIREMENTS.md:212` «compare the two copies record by record. **Expected:** records that differ: 0.»

The brief says a learner number is given and new; it says nothing of its form.

**Given to every position:** the registry gives the number, never the clerk; at each reset the lists are enrolled in one fixed order (G-03); wherever chance is used, it is drawn from a fixed seed (G-10); a check digit, which any of the three could carry, is left out of all three.

**Position A — a number in sequence.** The registry gives each new learner the whole number one higher than the highest it holds, and never gives a number twice. It says nothing about the child, and the same enrolments after every reset get the same numbers.

**Position B — a number made from the child's details.** The number carries the child's date of birth and a running part for children born on that day, so that a person reading the number can read the date of birth from it.

**Position C — an opaque number from a seeded generator.** The number is drawn from a generator seeded with the same fixed seed at every reset, so the same enrolments after every reset get the same numbers, as line 29 asks; a number already held is drawn again, so none is given twice. It tells nothing about the child, nor the order in which children were enrolled.

| Test | A — in sequence | B — from the details | C — opaque, seeded |
|---|---|---|---|
| (a) for agreement, not the registry | the least that is "new"; says nothing about the child, and settles nothing about the real registry's scheme | designs a numbering that carries the child's date of birth: a choice for the real registry, not the prototype | says nothing about the child, and settles nothing about the real registry's scheme; adds a seeded generator and a redraw |
| (b) must not | no bearing | no bearing; the number repeats the invented date of birth | no bearing |
| (c) known numbers | the same numbers after every reset | the same numbers after every reset | the same numbers after every reset, from the fixed seed |
| (d) rounds 5 to 7 | round 6 builds one more than the highest held; register line 93 holds by construction; register line 212 finds 0 records that differ | round 6 must also design the running part; register line 93 holds only if the running part never repeats within one day | round 6 builds the generator and its redraw; register line 93 holds by the redraw; register line 212 finds 0 records that differ, as under A |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: a whole number given in sequence, one higher than the highest the registry holds, never given twice.
*Ground:* A and C are alike silent about the child and the same after every reset; A meets register line 93 by construction where C needs a generator and a redraw, so A is the smaller of the two, and B designs the real registry's numbering.

## G-02 — more than one learner found

> **G-02** (R-05) What does the registry do when its search finds more than one learner with the same family name, given names and date of birth, capitals ignored?

**Bears on:** R-05. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:13` «if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;»
- `../brief/MINI-REGISTRY-BRIEF.md:14` «if it finds none, it gives the child a new learner number and saves the record;»
- `../brief/MINI-REGISTRY-BRIEF.md:15` «the clerk sees which of the two happened.»
- `../brief/MINI-REGISTRY-BRIEF.md:7` «the registry does not register the same child twice»
- `docs/REQUIREMENTS.md:80` «(What the registry does when the search finds more than one: gap G-02.)»

The brief names two outcomes, exactly one and none, and line 15 speaks of "the two"; line 13's "exactly one" shows that it foresees more.

**Given to every position:** a learner is added only when the search finds none (line 14); the made-up data holds no two different children sharing family name, given names and date of birth, capitals ignored (G-05, setting 3); so, where the search looks among learners only (G-03, A or B), the registry never holds two learners sharing all three, and the case is met 0 times after every reset. If it is met all the same, the registry enters nothing new and shows the clerk one view of its own, which carries the words of line 33 and is a screen (G-09). **What divides the positions:** what that view says — a refusal, or every learner found.

**Position A — show every learner found.** The registry enters nothing new, shows every learner found with its learner number, and says that more than one was found. It is the nearest thing to line 13's "shows that learner", and tells the clerk what there is to resolve.

**Position B — refuse the entry.** The registry enters nothing new, shows no learner, and says the entry cannot be completed because the registry holds more than one learner with these details. Line 13 shows a learner only when it finds exactly one; with more than one the registry cannot say which child this is, and says only that.

| Test | A — show every learner found | B — refuse the entry |
|---|---|---|
| (a) for agreement, not the registry | one view for a case the brief does not name, as B adds one: on that count the test does not divide them; this view lists several learners, a view used nowhere else | one view for a case the brief does not name, as A adds one: on that count the test does not divide them; this view is a refusal, of the kind G-07 already needs, and shows no learner |
| (b) must not | the view carries the words (G-09): no bearing | the view carries the words (G-09): no bearing |
| (c) known numbers | learners sharing all three after every reset: 0; times the view is reached by the counts of rounds 5 and 7: 0 | learners sharing all three after every reset: 0; times the view is reached by the counts of rounds 5 and 7: 0 |
| (d) rounds 5 to 7 | round 6 builds a list of learners reached by no count; round 7 counts with line 15's two outcomes | round 6 reuses the refusal view; round 7 counts with line 15's two outcomes |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position B: under the settings given to both the case is never met, and if it is met the registry enters nothing new and says the entry cannot be completed.
*Ground:* neither view is ever reached under the shared settings; B says only what line 13 allows when it cannot show "that learner", and reuses a refusal the prototype needs anyway, where A adds a list of learners line 13 never shows.

## G-03 — where the search looks

> **G-03** (R-04, R-05, R-06) Where does the search look: among the learners the registry has saved, among the children on the three lists, or both — and are the children on the three lists learners with a learner number when the prototype starts?

**Bears on:** R-04, R-05, R-06. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:7` «Progressa's Ministry of Education, Youth and Skills (MoEYS) wants one list of learners instead of three.»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored)»
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.»
- `../brief/MINI-REGISTRY-BRIEF.md:54` «The duplicates count: how many of the 8 the search catches»
- `docs/REQUIREMENTS.md:91` «read the number of learners and every learner number the registry holds (what a learner number looks like: gap G-01; where the search looks: gap G-03)»
- `docs/REQUIREMENTS.md:67` «in each enrolment the search is the first act on the data, before any write»
- `docs/REQUIREMENTS.md:92` «match none of the records the search looks in»

**Given to every position:** line 13's rule as the only rule of matching; G-04's and G-05's settings — 60 children, each of the 8 on exactly two lists, 68 list entries, the key table read by the counts only, the 4 differing by at least one letter; the clerk's enrolment the one goal.

**Position A — among saved learners only, starting from none.** The three lists are the made-up data for the counts; the registry starts with no learners, and a learner exists only once a clerk enrols it. Line 13 says "learner", and line 14 gives a learner number only on enrolment, so nothing on the lists is a learner until enrolled.

**Position B — the lists enrolled at reset by the brief's own rule; the search looks among learners.** At each reset the registry enrols every entry of the three lists, in a fixed order (the census, then the candidate list, then the grant list, each in its own order), through the same search: an entry that matches exactly one learner by line 13 joins it and enters nothing new; an entry that matches none becomes a new learner with a number. After reset the lists' children are learners with numbers, and the clerk's search looks among learners only. This is line 7's "one list of learners instead of three", made by line 13's rule and no other.

**Position C — the search looks at learners and at the list entries directly.** The lists stay three lists; a clerk's search reads them and the saved learners; a list child has no learner number until a clerk enrols it. The lists stay as the bodies hold them.

| Test | A — learners only, from none | B — lists enrolled at reset by the rule | C — learners and lists |
|---|---|---|---|
| (a) for agreement, not the registry | no screen, goal, field or body added; but a clerk enrolling a child on the census finds nothing, so the prototype does not show line 7's one list instead of three | no screen, goal, field or body added; the reset gains one act; shows the one list made from three, and holds twice each the 4 the rule misses, which is what line 54 counts | no screen, goal, field or body added; shows the three lists as three, and a search can find two entries of one child in ordinary use (G-02) |
| (b) must not | no bearing | no bearing | no bearing |
| (c) known numbers | learners after reset: 0; list entries: 68 | learners after reset: 64 — 60 children, and the 4 the rule does not join each held twice; list entries: 68 | learners after reset: 0; list entries: 68; a search for one of the 4 the rule joins finds 2 entries |
| (d) rounds 5 to 7 | round 7 must itself enrol every list entry to count: Position B done in round 7 instead of at reset | round 7 counts, against G-05's key table, how many of the 8 one learner carries: 4, decided by the rule, not 8 by construction | round 7 must decide whether a search finding two entries of one child "catches" it |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position B: at each reset the registry enrols every list entry, in a fixed order, through the brief's own rule, so that the lists' children are learners with numbers, and the clerk's search then looks among learners only.
*Ground:* it makes line 7's one list by line 13's rule alone, gives round 5 a known number of learners and round 7 a count that the rule, not the data, decides.

## G-04 — what "Children 60" counts

> **G-04** (R-09) Is "Children 60" the number of different children, each counted once however many lists carry it, or the number of entries across the three lists?

**Bears on:** R-09. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children spread over three lists»
- `../brief/MINI-REGISTRY-BRIEF.md:23` «| Children | 60 |»
- `../brief/MINI-REGISTRY-BRIEF.md:25` «| Children on more than one list | 8 |»
- `docs/REQUIREMENTS.md:133` «count the children in the data, by the unit of counting that gap G-04 asks after.»
- `docs/REQUIREMENTS.md:121` «and every child on at least one of them»

**Given to every position:** each of the 8 on exactly two lists (G-05, setting 4); the counts read G-05's key table; the 8 and the 4 unchanged.

**Position A — 60 different children.** Each invented child is counted once, however many lists carry it. Line 25 counts "children on more than one list", which only makes sense if a child is one thing and its entries on the lists are another; and line 19 spreads children over lists.

**Position B — 60 entries across the three lists.** The table is a table of the data, and the data is entries; 60 is what a reader counting rows would find.

| Test | A — 60 children | B — 60 entries |
|---|---|---|
| (a) for agreement, not the registry | no bearing | no bearing |
| (b) must not | no bearing | no bearing |
| (c) known numbers | children 60, entries 68: both known | entries 60, children 52: both known; but the table's "Children" then counts entries on line 23 and children on line 25 |
| (d) rounds 5 to 7 | round 5 makes 60 children and lays the 8 over two lists each: 68 entries; round 7's 8 unchanged | round 5 makes 52 children and lays the 8 over two lists each: 60 entries; round 7's 8 unchanged |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: 60 is the number of different children, and round 2 also fixes the number of entries, which is 68 with each of the 8 on exactly two lists.
*Ground:* line 25 and register line 121 count children apart from the entries that carry them; only A gives the word "Children" one meaning in the brief's table.

## G-05 — how the data records the same child

> **G-05** (R-11, R-12) How does the made-up data record that entries on two lists are the same child, so that the 8 and the 4 can be counted?

**Bears on:** R-11, R-12. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:25` «| Children on more than one list | 8 |»
- `../brief/MINI-REGISTRY-BRIEF.md:26` «| Of those, children whose family name is spelt differently on one list | 4 |»
- `../brief/MINI-REGISTRY-BRIEF.md:54` «The duplicates count: how many of the 8 the search catches»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «(capitals ignored)»
- `docs/REQUIREMENTS.md:159` «by what the data records of which entries are the same child (gap G-05)»
- `docs/REQUIREMENTS.md:172` «for each of them, compare the family name each list gives it, letter for letter;»
- `docs/REQUIREMENTS.md:173` «This test counts the data; how many of these children the registry's search catches is not tested here.»
- `docs/REQUIREMENTS.md:79` «(b) enrol a child with F and G written in other capitals — for example every letter a capital — and the same D.»

This is the question the search can be widened through: whatever records sameness must not become a second way of matching.

**A conflict, and how this paper resolves it.** The first edition proposed that some of the 8 differ in capitals only, so that line 13's «(capitals ignored)» is exercised by the data. Register line 172 compares family names «letter for letter»: if that comparison heeds capitals, a child whose family name differs in capitals only is counted as spelt differently, and R-12 counts more than 4. This paper drops the capitals-only children: under setting 2 below, R-12 counts 4 whether its comparison heeds capitals or not, and «(capitals ignored)» is still exercised, by R-05's test (b) at register line 79. The other way out — keeping capitals-only children and having round 2 read register line 172 as capitals ignored — would read into an accepted test and is not recommended.

**Given to every position** — four settings of the data, open to all three: (1) a family name "spelt differently" differs from the other list's in at least one letter, not in capitals alone; (2) apart from those 4 family names, each of the 8 has, on both its lists, the same family name, given names and date of birth, letter for letter and in the same capitals; (3) no two different children share family name, given names and date of birth, capitals ignored; (4) each of the 8 is on exactly two lists (G-04). **What divides the positions:** where, if anywhere, the data records that two entries are one child.

**Position A — a key table of the made-up data, read by the counts only.** Each list entry carries only what its list would carry. Beside the lists, the made-up data holds one table that names, for every entry, the invented child it stands for (a child key, not a learner number). The counts of R-11, R-12 and round 7 read it; the enrolment, the search and the reset's enrolment of the lists (G-03) never open it.

**Position B — a shared key carried on every list entry.** Every entry carries the child's key as one more field of its list, as lists joined by one identifier would; the counts read the key from the lists themselves. It counts the 8 and the 4 as exactly as A does, and needs no table beside the lists.

**Position C — no record; sameness worked out from the fields.** The data holds only the three lists, and nothing the brief does not name; the counts find the 8 by comparing names and dates.

| Test | A — key table, counts only | B — shared key on every entry | C — no record |
|---|---|---|---|
| (a) for agreement, not the registry | one table of the data; no screen, field or body | one field more on every list entry, which the lists of line 19 do not name; no screen or body | nothing added to the data |
| (b) must not | no bearing | no bearing | no bearing |
| (c) known numbers | 8 and 4 counted exactly from the table, under settings 1 to 4 | 8 and 4 counted exactly from the key, under settings 1 to 4 | under settings 2 and 3 the 4 the rule joins are found by line 13's rule; the 4 spelt differently cannot be told from two different children without a rule that forgives spelling, which line 13 does not give |
| (d) rounds 5 to 7 | the key sits where the enrolment and the search never read; round 7 counts, against the table, how many of the 8 one learner carries: the rule decides, 4 | the key sits in the entries the reset's enrolment reads (G-03); keeping it out of the match needs a rule that the search ignore a field it holds, and if round 6 matches on it, round 7's count is 8 by construction — the search widened by the back door | round 7 would count with a looser rule than the one it tests |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A, with settings 1 to 4 for round 2 — the 4 differ in at least one letter, the other 4 match letter for letter and in the same capitals, so none of the 8 differs in capitals only, and no two different children share all three fields — which gives round 7 the known answer of 4 of the 8 caught and R-12 a count of 4 whether or not its comparison heeds capitals.
*Ground:* A and B count the 8 and the 4 equally exactly; only A keeps the record of sameness out of everything the search reads, so the search matches by line 13 alone.

## G-06 — the date ages are reckoned on

> **G-06** (R-13) On what date is a child's age reckoned, and are the ages 6 and 12 themselves within "6 to 12"?

**Bears on:** R-13. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:27` «| Ages | 6 to 12 |»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The numbers are fixed so that every later count has a known answer. The data is made the same way every time it is reset.»
- `docs/REQUIREMENTS.md:185` «reckon each child's age from its date of birth (on what date, and whether 6 and 12 are included: gap G-06)»
- `docs/REQUIREMENTS.md:186` «**Expected:** every age within 6 to 12; children outside: 0.»

On the bounds, the brief leaves one reading open: "6 to 12" in a table of settings reads as both ends included, and no passage reads otherwise. The two positions differ on the date.

**Given to every position:** ages in completed years; 6 and 12 both included; the dates of birth fixed by the data and the same after every reset (line 29).

**Position A — one fixed date, held in the settings.** Ages are reckoned on one date written in round 2's settings; every child is aged 6 to 12 on that date.

**Position B — the day the check runs.** Ages are reckoned on the day of the check, as a clerk would reckon them, and the data reads as current whenever it is looked at; the dates of birth are made so that every child is aged 6 to 12 on any day of a set span.

| Test | A — a fixed date | B — the day of the check |
|---|---|---|
| (a) for agreement, not the registry | one setting | no date in the settings; a span the dates are made for |
| (b) must not | no bearing | no bearing |
| (c) known numbers | children outside 6 to 12: 0 at every reset and every check | children outside: 0 within the span; after it, register line 186 fails on data that has not changed, so the count's answer depends on the day |
| (d) rounds 5 to 7 | round 5 makes dates of birth that fit the date, with ages anywhere from 6 to 12 | round 5 fits the dates to the span; the longer the span, the narrower the spread of ages within 6 to 12 the data can hold |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: ages in completed years on one fixed date held in round 2's settings, with 6 and 12 both included.
*Ground:* line 29 asks that every later count have a known answer; only a fixed date gives one with no end.

## G-07 — the form of the entries

> **G-07** (R-03) In what form does the clerk enter a date of birth; is the school chosen from the data's three schools or written in; and must all four entries be made before the search runs?

**Bears on:** R-03. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:11` «A school clerk enters a child's family name, given names, date of birth and school. The registry searches for the child first:»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «with the same family name, given names and date of birth (capitals ignored)»
- `../brief/MINI-REGISTRY-BRIEF.md:24` «| Schools | 3 |»
- `docs/REQUIREMENTS.md:53` «enter F, G, D and S for a child the registry does not yet hold (the form of a date and of a school: gap G-07); submit.»
- `docs/REQUIREMENTS.md:54` «the screen offers an entry for each of the four — family name, given names, date of birth, school — and the record saved holds F, G, D and S as entered.»
- `docs/REQUIREMENTS.md:146` «count the different schools the data names.»

The question has three parts, and each can be ruled apart; every cell below names the part it judges, so a mixed ruling reads off the same cells.

**Given to every position:** the school stored, not searched on (line 13 names three fields); a message for an entry left empty, which either needs (line 11 names four entries); every message a screen (G-09); every date read one way only.

**Position A — fixed forms.** The date of birth is entered in one form, YYYY-MM-DD, and any other is refused with a message; the school is chosen from the data's three; all four are entered before the search runs, as line 11 orders them.

**Position B — free forms.** The date is accepted in the several forms a clerk writes, each read one way and converted, and a form that reads two ways (03/04) is refused; the school is written in; the search runs as soon as the three searched fields are entered, and the school is asked only when the child is new. Fewer refusals, closer to a clerk's habits, and no school asked for a child already held.

| Test | A — fixed forms | B — free forms |
|---|---|---|
| (a) for agreement, not the registry | date: one refusal for any other form; school: a choice of three; order: one step. A refusal of dates, as B has: on that count the test does not divide them; no field added | date: a converter, and a refusal for forms that read two ways; school: a free field; order: two steps. A refusal of dates, as A has: on that count the test does not divide them; no field added |
| (b) must not | no bearing | no bearing |
| (c) known numbers | date: exact; school: register line 146 counts 3 after reset, and the learners' records name only those 3 | date: exact, ambiguous forms refused; school: register line 146 counts 3 after reset, but a school written in by a clerk can add a fourth name to the learners' records, so a count of schools after enrolment has no known answer |
| (d) rounds 5 to 7 | round 6 builds one date form, a choice of three and one step; register line 54 passes on one screen | round 6 builds a converter whose forms round 3 must list, a free school field and a second step; register line 54 passes once the school is asked |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the date entered as YYYY-MM-DD and refused otherwise, the school chosen from the data's three, and all four entered before the search runs, the school not searched on.
*Ground:* line 11 has the clerk enter all four and then the registry search; fixed forms keep the schools at the data's 3 and build the least.

## G-08 — what counts as a goal

> **G-08** (R-02) Does anything else the prototype offers — resetting the data, looking at a learner — count as a goal under "One goal"?

**Bears on:** R-02. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:11` «One goal: **enrol a learner.**»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «it shows that learner and enters nothing new;»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The data is made the same way every time it is reset.»
- `docs/REQUIREMENTS.md:40` «list every goal the prototype offers the clerk on its screens (what counts as a goal: gap G-08).»
- `docs/REQUIREMENTS.md:41` «**Expected:** one goal, enrolling a learner. Pass if the list holds that goal and no other.»

**Given to every position:** reset available to the checks by a command; a learner shown as enrolment's outcome (line 13).

**Position A — enrolment is the only thing on the clerk's screens.** Reset is a command run outside the screens, by the checks and by whoever shows the prototype; a learner is shown only as enrolment's outcome; there is no screen for looking learners up. Nothing else exists to be counted as a goal.

**Position B — reset and look-up on screens, as tools, not goals.** For a meeting held to reach agreement, the planning unit will want to restart the demonstration and to see what the registry holds; offer both on screens, the look-up reusing the view of a found learner, and say they are not goals.

| Test | A — enrolment only | B — reset and look-up on screens |
|---|---|---|
| (a) for agreement, not the registry | the smallest prototype that shows the goal | adds two things to do on the screens beside "One goal" (line 11): fails the test on that count |
| (b) must not | no bearing | two more screens to carry the words of line 33 |
| (c) known numbers | no bearing | no bearing |
| (d) rounds 5 to 7 | round 6 builds one flow; register line 41 lists one goal | round 6 builds three flows; register line 40 lists every goal the screens offer, and must then rule reset and look-up out |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: enrolment is the only thing the clerk's screens offer, reset is a command outside them, and there is no screen for looking learners up.
*Ground:* line 11 says one goal, and A leaves nothing that could be read as a second.

## G-09 — what counts as a screen

> **G-09** (R-17) What counts as a screen: does a message the prototype shows, such as a refusal of an entry, count?

**Bears on:** R-17. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:33` «Every screen says "Invented data, Progressa is fictional".»
- `../brief/MINI-REGISTRY-BRIEF.md:35` «Every check of the screens runs without one.»
- `docs/REQUIREMENTS.md:238` «the list of its screens (what counts as a screen: gap G-09).»
- `docs/REQUIREMENTS.md:239` «show each screen in turn, among them the screen after a new learner is saved and the screen after an existing learner is found, and read its text.»
- `docs/REQUIREMENTS.md:240` «**Expected:** screens without them: 0.»

**Given to every position:** every message is shown on a page that carries the words, never in a dialog box apart from the page; the pages are read by the windowless checks (line 35); the same messages exist under both (G-02's refusal, G-07's refusals). **What divides the positions:** whether a message is on the list of screens register line 238 sets up.

**Position A — every view the clerk can see.** The entry form, the result after a new learner, the result after a found learner and every message are each a screen, and each is on the list of register line 238.

**Position B — the pages only.** The entry form and the two results are the screens; a message shown on a page is part of that page, not a screen of its own, and the list of register line 238 is the three pages. Each message already sits on a page that carries the words.

| Test | A — every view | B — the pages only |
|---|---|---|
| (a) for agreement, not the registry | no view added: only what the list holds | no view added: only what the list holds |
| (b) must not | register line 239 reads every view a person sees, so a message shown without the words fails it | the words show wherever a message sits on a page, but register line 239 reads no message, so a message shown otherwise passes unseen |
| (c) known numbers | screens without the words: 0, over a list of the three pages and each message | screens without the words: 0, over the three pages |
| (d) rounds 5 to 7 | round 6 puts the words in one frame every view shares; the list grows by each message round 3 names | round 6 puts the words in the same frame; the list stays at three, and round 3's messages are not read by the check of register line 239 |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: every view the clerk can see, messages and refusals included, is a screen on the list of register line 238 and carries the words.
*Ground:* line 33 says every screen; A costs one entry in the list per message and leaves no view a person sees unread.

## G-10 — the evidence that no real person's data is held

> **G-10** (R-16) What evidence does the brief accept that no real person's data is held?

**Bears on:** R-16. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:3` «Everything in it is invented for Progressa, the fictional country every course here uses.»
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children»
- `../brief/MINI-REGISTRY-BRIEF.md:33` «Hold any real person's data.»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The data is made the same way every time it is reset.»
- `docs/REQUIREMENTS.md:226` «list every source from which the data is made: every file and program the reset reads.»
- `docs/REQUIREMENTS.md:227` «each source is part of the prototype and makes invented records; none is a record of persons brought in from elsewhere. Pass if no source carries a real person's data (what evidence shows this: gap G-10).»

The brief names no evidence. A third position — comparing the invented records with a list of real persons — would need that list on the computer, which is the one thing line 33 forbids; it is set aside for that reason and not judged below.

**Given to every position:** a statement, by whoever made the name parts, that they are invented — which either position can carry, in the note or the source; the screens' words (line 33).

**Position A — evidence by construction, recorded.** The data is made only by a generator in the prototype's source, from name parts written in that source and a fixed seed; the reset reads no file of persons, and a record of every file the reset reads, taken by program, is the list register line 226 asks for.

**Position B — the statement alone.** The person who wrote the generator and its name parts states that they are invented; it covers what a program cannot see, where the name parts came from. No record of the reset's reads is taken.

| Test | A — by construction, recorded | B — the statement alone |
|---|---|---|
| (a) for agreement, not the registry | no screen or field; one record of the reset's reads | no screen or field; one sentence in the note or the source |
| (b) must not | line 33's first sentence shown kept: register line 226's list read from the record, and register line 227's test passed on it | line 33's first sentence asserted kept; register line 226's list is not made |
| (c) known numbers | files of persons read at reset: 0, counted | no count |
| (d) rounds 5 to 7 | round 5 writes the generator and its fixed seed, the seed G-01's Position C also draws on; the same seed gives line 29's same data | round 5 adds the statement; the data may come from any file |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the data is made only by a generator in the prototype's source from invented name parts and a fixed seed, and the record of the files the reset reads is the evidence, with the maker's statement and the screens' words beside it.
*Ground:* register line 226 asks for a list of every file and program the reset reads; A makes that list by a record, and B makes none.

## G-11 — other bodies

> **G-11** (R-19) Which other bodies, if any, does the project need — and are the census, the examinations authority and the social grant programme, whose lists the data holds, among them?

**Bears on:** R-19. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.»
- `../brief/MINI-REGISTRY-BRIEF.md:34` «Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.»
- `docs/REQUIREMENTS.md:264` «the list of other bodies the prototype draws on (which they are: gap G-11).»
- `docs/REQUIREMENTS.md:266` «each body is answered by a simulation on the computer, and the part that uses it works.»
- `docs/REQUIREMENTS.md:253` «every recorded connection has both its ends on the computer itself.»

**Given to every position:** the same three lists with the same entries; anything simulated runs on the computer.

**Position A — none.** The three lists are made-up data the prototype starts with (line 19), held inside it; the enrolment consults no body. The list of register line 264 is empty, so the test of register line 266 has no body to run.

**Position B — the three bodies, simulated.** The census, the examinations authority and the grant programme are each simulated on the computer as a small service that hands over its list, and the registry reads from them at reset. This shows the agreement the real registry will need: three sources, three owners.

| Test | A — none | B — three simulated bodies |
|---|---|---|
| (a) for agreement, not the registry | nothing added | adds three bodies to connect to and the code to reach them: fails the test on that count |
| (b) must not | nothing to connect to; register line 253 sees the prototype's own connections only | kept by simulation, as line 34 allows; register line 253 must also find the connections to three simulations ending on the computer |
| (c) known numbers | no bearing | no bearing: the simulations serve the same lists |
| (d) rounds 5 to 7 | round 5 writes the lists as data; register line 266 has no body to run | round 5 also builds three simulations; round 6 reads through them; register line 266 runs on three |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the project needs no other body; the three lists are made-up data inside the prototype, and the list of register line 264 is empty.
*Ground:* line 19 calls them lists the prototype starts with, and nothing in "What it must do" asks the registry to reach another body.

## G-12 — which checks are "its checks"

> **G-12** (R-22) Which checks are "its checks": the tests of this register, or a set a later round names?

**Bears on:** R-22. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:39` «The working prototype, on your computer, with its checks passing.»
- `../brief/MINI-REGISTRY-BRIEF.md:50` «The goal written in full: every step of enrolling a learner, and every way it can go wrong»
- `../brief/MINI-REGISTRY-BRIEF.md:51` «The count: every requirement against the goal, both ways»
- `docs/REQUIREMENTS.md:305` «the owner's computer, with the prototype as delivered (which checks are its checks: gap G-12).»
- `docs/REQUIREMENTS.md:307` «**Expected:** checks failing: 0; the enrolment completes on that computer.»
- `docs/REQUIREMENTS.md:214` «## What it must not do»
- `docs/REQUIREMENTS.md:294` «## What it delivers»
- `docs/REQUIREMENTS.md:108` «## The made-up data, in known numbers»
- `docs/REQUIREMENTS.md:199` «**Expected**, after each reset: children 60, schools 3, children on more than one list 8»

The register's section "What it must not do" runs from register line 214 to the next section, at register line 294, and holds R-16 to R-21; its section "The made-up data, in known numbers" from register line 108 holds R-08 to R-15, of which R-09 to R-15 hold the table's numbers and line 29's sameness.

**Given to every position:** the checks written as programs by round 6; round 3's list of the ways enrolment can go wrong (line 50); under either, round 6 may name the register's tests.

**Position A — the register's tests, with round 3's cases.** Its checks are the tests of R-01 to R-21, written as programs (R-22 is the running of them, and R-23 is the note), together with a check for each way the goal can go wrong that round 3 writes down; round 6 names them in one list.

**Position B — whatever round 6 names.** The build knows best what can be checked; round 6 names its checks, and R-22 asks only that they pass.

| Test | A — register and round 3 | B — round 6's own list |
|---|---|---|
| (a) for agreement, not the registry | no bearing on the prototype's size | no bearing on the prototype's size |
| (b) must not | R-16 to R-21, the section from register line 214, carry all three "must not" sentences into the checks | the "must not" sentences are checked where round 6 names them |
| (c) known numbers | R-09 to R-15, of the section from register line 108, carry the known numbers into the checks, register line 199 among them | the known numbers are checked where round 6 names them |
| (d) rounds 5 to 7 | round 6 knows its checks before it builds; round 4's count, both ways, already ties them to the goal | the round that builds also chooses what proves it built |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: its checks are the tests of R-01 to R-21 written as programs, with a check for each way the goal can go wrong that round 3 names, listed together by round 6.
*Ground:* the register is accepted and each test already says pass or fail; under B the round that builds would also choose what proves it.

## G-13 — the note's one page

> **G-13** (R-23) On what size of page, and in what form, is the note's one page counted?

**Bears on:** R-23. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:40` «A one-page note to the Permanent Secretary: what the prototype shows, and what it does not.»
- `../brief/MINI-REGISTRY-BRIEF.md:55` «The note to the Permanent Secretary»
- `docs/REQUIREMENTS.md:319` «count its pages (on what page: gap G-13); read it.»
- `docs/REQUIREMENTS.md:320` «**Expected:** 1 page, addressed to the Permanent Secretary, saying what the prototype shows and saying what it does not.»

**Given to every position:** a program reads the count; the note addressed and written as line 40 says.

**Position A — one A4 page, as a PDF.** The note is made as a PDF of one A4 page, portrait, with body type no smaller than 11 point; a program reads its page count.

**Position B — one page by length.** The note is plain text of no more than a set number of words, counted by a program; no page size is fixed, so it reads anywhere and fits one page of any common size.

| Test | A — one A4 page, PDF | B — a word limit |
|---|---|---|
| (a) for agreement, not the registry | no bearing on the prototype | no bearing on the prototype |
| (b) must not | no bearing | no bearing |
| (c) known numbers | pages: 1, read by a command, as register line 319 counts pages | words at most the limit, read by a command; register line 319 counts pages, so this is a stand-in |
| (d) rounds 5 to 7 | no bearing; round 8 makes the PDF | no bearing; round 8 counts words |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the note is one A4 page, portrait, as a PDF with body type no smaller than 11 point, counted by its page count.
*Ground:* the brief says one page, and register line 319 counts pages; only A counts a page rather than a stand-in for one.
