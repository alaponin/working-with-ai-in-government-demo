# The register's open questions — a decision paper for the owner's ruling

**What this is.** The register of requirements (`docs/REQUIREMENTS.md`) closes with fourteen open questions. G-14 is already closed (below). This paper answers the other thirteen, G-01 to G-13, so that you can rule on them in one act and round 2, the groundwork, can be drafted from the brief, the register and your ruling. **Every recommendation here is a proposal for your ruling, not a decision.** Nothing in this paper changes the brief or the register.

**How to read a passage.** A passage is quoted word for word after its file and line, as `` `<path>:<line>` «<words>» ``. Paths are relative to the estate's root: the brief is `../brief/MINI-REGISTRY-BRIEF.md`, the register is `docs/REQUIREMENTS.md`.

**The four tests, the same for every question.**

- **(a) For agreement, not the registry.** `../brief/MINI-REGISTRY-BRIEF.md:7` «the planning unit wants to see a small working prototype: a school clerk enrols a child, and the registry does not register the same child twice. The prototype is for agreement. It is not the registry.» A position that adds a goal, a screen, a body to connect to or a field the clerk enters fails this test.
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
| G-02 | Kept from arising by the data and the rule; if it arises, enter nothing new and say so |
| G-03 | At reset every list entry is enrolled by the brief's own rule; the search then looks among learners only |
| G-04 | 60 different children; the entries counted apart — 68, if each of the 8 is on exactly two lists |
| G-05 | A key table of the made-up data, read by the counts and never by the search |
| G-06 | Age in completed years on one fixed date held in the settings; 6 and 12 included |
| G-07 | Date as YYYY-MM-DD; school chosen from the three; all four entered before the search |
| G-08 | Enrolment the only goal; reset is a command, and there is no screen for looking learners up |
| G-09 | Every view the clerk can see is a screen, refusals included; no separate dialog boxes |
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
- `docs/REQUIREMENTS.md:93` «each new learner number unlike every number held before it»

The brief says a learner number is given and new; it says nothing of its form.

**Position A — a number in sequence.** The registry gives each new learner the whole number one higher than the highest it holds, and never gives a number twice. It says nothing about the child, and the same data enrolled in the same order always gets the same numbers.

**Position B — a number made from the child's details.** The number carries the date of birth and a running part, so that a clerk can read something from it and a mistyped number is easier to catch.

**Position C — a random number.** An opaque number drawn at random, which can never be guessed and never collides in practice. It stands beside the brief's line 29, «The data is made the same way every time it is reset.»: numbers drawn afresh at each reset differ from one reset to the next.

| Test | A — in sequence | B — from the details | C — random |
|---|---|---|---|
| (a) for agreement, not the registry | the smallest thing that is "new"; settles nothing about the real registry's scheme | designs the real registry's numbering, which is not what the prototype is for | small, but adds a source of chance |
| (b) must not | no bearing | no bearing; the number would repeat the invented date of birth | no bearing |
| (c) known numbers | the same numbers after every reset | the same numbers after every reset | numbers differ after every reset, against line 29 |
| (d) rounds 5 to 7 | round 6 builds it in a line; R-06's "unlike every number held before" is a comparison of whole numbers | round 6 must also design the running part for children born on one day | round 5's data cannot be compared reset to reset (R-15) |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: a whole number given in sequence, one higher than the highest the registry holds, never given twice.
*Ground:* it is the least the brief's "a new learner number" needs, and the only one of the three that is both silent about the child and the same after every reset.

## G-02 — more than one learner found

> **G-02** (R-05) What does the registry do when its search finds more than one learner with the same family name, given names and date of birth, capitals ignored?

**Bears on:** R-05. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:13` «if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;»
- `../brief/MINI-REGISTRY-BRIEF.md:14` «if it finds none, it gives the child a new learner number and saves the record;»
- `../brief/MINI-REGISTRY-BRIEF.md:15` «the clerk sees which of the two happened.»
- `../brief/MINI-REGISTRY-BRIEF.md:7` «the registry does not register the same child twice»

The brief names two outcomes, exactly one and none, and line 15 speaks of "the two". Whether more than one can arise depends on where the search looks (G-03).

**Position A — a third outcome on the screen.** When the search finds more than one learner, the registry enters nothing new, shows every learner found, and tells the clerk that more than one was found. It is the honest answer to a case that can happen wherever the search looks across lists.

**Position B — kept from arising, and refused if it does.** The registry holds at most one learner for any family name, given names and date of birth, capitals ignored: a learner is only ever added when the search finds none (line 14), and the made-up data holds no two different children sharing all three. If the case is met all the same, the registry enters nothing new and tells the clerk the entry cannot be completed. A check of the data after reset counts such learners and expects 0.

| Test | A — a third outcome | B — kept from arising |
|---|---|---|
| (a) for agreement, not the registry | adds an outcome and a screen beside the brief's "two" (line 15) | adds no outcome in normal use; one refusal for a state the checks show never happens |
| (b) must not | no bearing | no bearing |
| (c) known numbers | the number of learners found more than once has no known answer unless G-03 and G-05 fix it | learners sharing all three: 0, after every reset |
| (d) rounds 5 to 7 | round 7 must decide whether "more than one" counts as caught | round 5 checks the data holds no shared key; round 7 counts with the brief's two outcomes only |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position B: the registry and the made-up data are kept so that no two learners share family name, given names and date of birth (capitals ignored), and if the case is met the registry enters nothing new and says the entry cannot be completed.
*Ground:* line 7 asks that the registry not register the same child twice, and line 15 knows two outcomes; B keeps to both and enters nothing new in either reading.

## G-03 — where the search looks

> **G-03** (R-04, R-05, R-06) Where does the search look: among the learners the registry has saved, among the children on the three lists, or both — and are the children on the three lists learners with a learner number when the prototype starts?

**Bears on:** R-04, R-05, R-06. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:7` «Progressa's Ministry of Education, Youth and Skills (MoEYS) wants one list of learners instead of three.»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored)»
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.»
- `../brief/MINI-REGISTRY-BRIEF.md:54` «The duplicates count: how many of the 8 the search catches»

**Position A — among saved learners only, starting from none.** The three lists are the made-up data for the counts; the registry starts with no learners, and a learner exists only once a clerk enrols it. Line 13 says "learner", and line 14 gives a learner number only on enrolment, so nothing on the lists is a learner until enrolled.

**Position B — the lists enrolled at reset by the brief's own rule; the search looks among learners.** At each reset the registry enrols every entry of the three lists, in a fixed order (the census, then the candidate list, then the grant list, each in its own order), through the same search: an entry that matches exactly one learner by line 13 joins it and enters nothing new; an entry that matches none becomes a new learner with a number. After reset the lists' children are learners with numbers, and the clerk's search looks among learners only. This is line 7's "one list of learners instead of three", made by line 13's rule and no other.

**Position C — the search looks at learners and at the list entries directly.** The lists stay three lists; a clerk's search reads them and the saved learners; a list child has no learner number until a clerk enrols it. The lists stay as the bodies hold them.

| Test | A — learners only, from none | B — lists enrolled at reset by the rule | C — learners and lists |
|---|---|---|---|
| (a) for agreement, not the registry | a clerk enrolling a child on the census finds nothing: the prototype does not show "one list instead of three" | shows the one list made from three, with no screen, goal or body added; the reset gains one act | shows the three lists, but adds the case of two or three matches (G-02) to ordinary use |
| (b) must not | no bearing | no bearing | no bearing |
| (c) known numbers | learners after reset: 0 | learners after reset: 60 plus the duplicates the rule misses — known once G-05 is ruled (64 under its recommendation) | matches per search vary with how many lists carry the child |
| (d) rounds 5 to 7 | round 7 must enrol every list entry itself to count — Position B done in round 7 instead of at reset | round 7 counts, for each of the 8, how many learners carry it: one learner is caught; the count is the rule's, not 8 by construction | round 7 must decide whether a search finding two entries of one child "catches" it |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position B: at each reset the registry enrols every list entry, in a fixed order, through the brief's own rule, so that the lists' children are learners with numbers, and the clerk's search then looks among learners only.
*Ground:* it makes line 7's one list by line 13's rule alone, gives round 5 a known number of learners and round 7 a count that the rule, not the data, decides.

## G-04 — what "Children 60" counts

> **G-04** (R-09) Is "Children 60" the number of different children, each counted once however many lists carry it, or the number of entries across the three lists?

**Bears on:** R-09. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children spread over three lists»
- `../brief/MINI-REGISTRY-BRIEF.md:23` «| Children | 60 |»
- `../brief/MINI-REGISTRY-BRIEF.md:25` «| Children on more than one list | 8 |»

**Position A — 60 different children.** Each invented child is counted once, however many lists carry it. Line 25 counts "children on more than one list", which only makes sense if a child is one thing and its entries on the lists are another; and line 19 spreads children over lists.

**Position B — 60 entries across the three lists.** The table is a table of the data, and the data is entries; 60 is what a reader counting rows would find.

| Test | A — 60 children | B — 60 entries |
|---|---|---|
| (a) for agreement, not the registry | no bearing | no bearing |
| (b) must not | no bearing | no bearing |
| (c) known numbers | children 60; entries 60 plus the extra appearances of the 8 — 68 if each is on exactly two lists | entries 60; the number of children is then not given (60 less the extra appearances), and the table's "Children" counts no children |
| (d) rounds 5 to 7 | round 5 makes 60 children and lays the 8 over two lists each | round 5 must work out how many children to make |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: 60 is the number of different children, and round 2 also fixes the number of entries, which is 68 if, as we propose, each of the 8 is on exactly two lists.
*Ground:* line 25 counts children across lists, which needs a child to be counted once; two lists each keeps every later count known.

## G-05 — how the data records the same child

> **G-05** (R-11, R-12) How does the made-up data record that entries on two lists are the same child, so that the 8 and the 4 can be counted?

**Bears on:** R-11, R-12. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:25` «| Children on more than one list | 8 |»
- `../brief/MINI-REGISTRY-BRIEF.md:26` «| Of those, children whose family name is spelt differently on one list | 4 |»
- `../brief/MINI-REGISTRY-BRIEF.md:54` «The duplicates count: how many of the 8 the search catches»
- `docs/REQUIREMENTS.md:173` «This test counts the data; how many of these children the registry's search catches is not tested here.»

This is the question the search can be widened through: whatever records sameness must not become a second way of matching.

**Position A — a key table of the made-up data, read by the counts only.** Each list entry carries only what its list would carry. Beside the lists, the made-up data holds one table that names, for every entry, the invented child it stands for (a child key, not a learner number). The counts of R-11, R-12 and round 7 read it; the enrolment, the search and the reset's enrolment of the lists (G-03) never open it.

**Position B — a shared key carried on every list, used to join them.** Every entry carries the child's common key, as a ministry joining its lists by one identifier would, and the registry joins entries with the same key at reset. The 8 are then counted directly from the lists, and the prototype shows a joined list at once.

**Position C — no record; sameness worked out from the fields.** The data holds only the three lists; the counts find the 8 by comparing names and dates. To find the 4 whose family name is spelt differently, the counts would need a rule that forgives spelling, which the brief does not give: line 13 forgives capitals only.

| Test | A — key table, counts only | B — shared key, used to join | C — no record |
|---|---|---|---|
| (a) for agreement, not the registry | one table of the data, no screen or field | joins by a key the brief never mentions: shows a registry other than the one line 13 describes | no table, but a second matching rule |
| (b) must not | no bearing | no bearing | no bearing |
| (c) known numbers | 8 and 4 counted from the table, exactly | 8 counted from the key; 4 counted by letter comparison | the 4 cannot be counted without a rule the brief lacks |
| (d) rounds 5 to 7 | round 7 counts, against the table, how many of the 8 the rule joined: the rule decides the answer | round 7's count is 8 by construction, whatever the rule does — the search widened by the back door | round 7 counts with the same looser rule it is testing |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A, with three settings for round 2: a family name "spelt differently" differs in at least one letter, not in capitals alone; apart from those 4 family names, each of the 8 has the same family name, given names and date of birth on both its lists, capitals ignored (some, we propose, differing in capitals only, so that the rule's "(capitals ignored)" is exercised); and no two different children share family name, given names and date of birth, capitals ignored — which gives round 7 the known answer of 4 of the 8 caught.
*Ground:* only A lets the 8 and the 4 be counted exactly while the search matches by line 13 and nothing else.

## G-06 — the date ages are reckoned on

> **G-06** (R-13) On what date is a child's age reckoned, and are the ages 6 and 12 themselves within "6 to 12"?

**Bears on:** R-13. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:27` «| Ages | 6 to 12 |»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The numbers are fixed so that every later count has a known answer. The data is made the same way every time it is reset.»

On the bounds, the brief leaves one reading open: "6 to 12" in a table of settings reads as both ends included, and no passage reads otherwise. The two positions differ on the date.

**Position A — one fixed date, held in the settings.** Ages are reckoned in completed years on one date written in round 2's settings; every child is aged 6 to 12 on that date, both ends included.

**Position B — the day the check runs.** Ages are reckoned on the day of the check, as a clerk would reckon them; the data reads as current whenever it is looked at.

| Test | A — a fixed date | B — the day of the check |
|---|---|---|
| (a) for agreement, not the registry | one setting | no setting |
| (b) must not | no bearing | no bearing |
| (c) known numbers | ages the same at every reset and every check | the same data gives other ages as the calendar moves, so R-13 can fail on data that has not changed, against line 29 |
| (d) rounds 5 to 7 | round 5 makes dates of birth that fit the date | round 5 must remake dates of birth each run, which line 29 forbids |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: ages in completed years on one fixed date held in round 2's settings, with 6 and 12 both included.
*Ground:* line 29 asks for counts with a known answer every time; only a fixed date gives one.

## G-07 — the form of the entries

> **G-07** (R-03) In what form does the clerk enter a date of birth; is the school chosen from the data's three schools or written in; and must all four entries be made before the search runs?

**Bears on:** R-03. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:11` «A school clerk enters a child's family name, given names, date of birth and school. The registry searches for the child first:»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «with the same family name, given names and date of birth (capitals ignored)»
- `../brief/MINI-REGISTRY-BRIEF.md:24` «| Schools | 3 |»

**Position A — fixed forms.** The date of birth is entered in one form, YYYY-MM-DD, and any other is refused with a message; the school is chosen from the data's three; all four are entered before the search runs, as line 11 orders them. The school is stored, not searched on: line 13 names three fields.

**Position B — free forms.** The date is accepted in the forms a clerk writes and converted; the school is written in; the search runs as soon as the three searched fields are entered, and the school is asked after. Fewer refusals, and closer to a clerk's habits.

| Test | A — fixed forms | B — free forms |
|---|---|---|
| (a) for agreement, not the registry | no field added; one refusal message | no field added, but a conversion of dates and a second step |
| (b) must not | no bearing | no bearing |
| (c) known numbers | schools stay 3 | a school written in can make a fourth, against line 24's 3; a date like 03/04 read two ways can join two children or split one |
| (d) rounds 5 to 7 | round 6 builds a check of one form and a choice of three | round 6 builds a converter whose readings round 7's count then depends on |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the date entered as YYYY-MM-DD and refused otherwise, the school chosen from the data's three, and all four entered before the search runs, the school not searched on.
*Ground:* line 11 puts the four entries before the search, and fixed forms keep the dates exact and the schools at 3, so the rule forgives nothing but capitals.

## G-08 — what counts as a goal

> **G-08** (R-02) Does anything else the prototype offers — resetting the data, looking at a learner — count as a goal under "One goal"?

**Bears on:** R-02. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:11` «One goal: **enrol a learner.**»
- `../brief/MINI-REGISTRY-BRIEF.md:13` «it shows that learner and enters nothing new;»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The data is made the same way every time it is reset.»

**Position A — enrolment is the only thing on the clerk's screens.** Reset is a command run outside the screens, by the checks and by whoever shows the prototype; a learner is shown only as enrolment's outcome (line 13); there is no screen for looking learners up. Nothing else exists to be counted as a goal.

**Position B — reset and look-up on screens, as tools, not goals.** For a meeting held to reach agreement, the planning unit will want to restart the demonstration and to see what the registry holds; offer both on screens and say they are not goals.

| Test | A — enrolment only | B — reset and look-up on screens |
|---|---|---|
| (a) for agreement, not the registry | the smallest prototype that shows the goal | adds two screens and two things to do, beside "One goal" (line 11) |
| (b) must not | no bearing | two more screens to carry the banner |
| (c) known numbers | no bearing | no bearing |
| (d) rounds 5 to 7 | round 6 builds one screen flow; the checks reset by command | round 6 builds three flows; R-02's test must then rule each one in or out |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: enrolment is the only thing the clerk's screens offer, reset is a command outside them, and there is no screen for looking learners up.
*Ground:* line 11 says one goal, and A leaves nothing that could be read as a second.

## G-09 — what counts as a screen

> **G-09** (R-17) What counts as a screen: does a message the prototype shows, such as a refusal of an entry, count?

**Bears on:** R-17. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:33` «Every screen says "Invented data, Progressa is fictional".»
- `../brief/MINI-REGISTRY-BRIEF.md:35` «Every check of the screens runs without one.»

**Position A — every view the clerk can see.** The entry form, the result after a new learner, the result after a found learner and every refusal or message are screens. Each is shown as a whole page carrying the words, never in a separate dialog box.

**Position B — the pages only.** The entry form and the two results are the screens; a message shown in a box of its own is part of the page beneath it, not a screen.

| Test | A — every view | B — the pages only |
|---|---|---|
| (a) for agreement, not the registry | no screen added: refusals become pages | no screen added |
| (b) must not | every view a person sees says the words (line 33) | a refusal box can show without the words |
| (c) known numbers | screens without the words: 0, over a list the checks can enumerate | the same count over a shorter list |
| (d) rounds 5 to 7 | round 6 puts the words in one frame every view shares; the windowless checks read each view | a dialog box is the hardest thing for a windowless check to read |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: every view the clerk can see, refusals and messages included, is a screen and carries the words, and none is shown in a separate dialog box.
*Ground:* line 33 says every screen; the stricter reading costs nothing and leaves no view a person sees without the words.

## G-10 — the evidence that no real person's data is held

> **G-10** (R-16) What evidence does the brief accept that no real person's data is held?

**Bears on:** R-16. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:3` «Everything in it is invented for Progressa, the fictional country every course here uses.»
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children»
- `../brief/MINI-REGISTRY-BRIEF.md:33` «Hold any real person's data.»
- `../brief/MINI-REGISTRY-BRIEF.md:29` «The data is made the same way every time it is reset.»

The brief names no evidence. A third position — comparing the invented records with a list of real persons — would need that list on the computer, which is the one thing line 33 forbids; it is set aside for that reason and not judged below.

**Position A — evidence by construction, recorded.** The data is made only by a generator in the prototype's source, from name parts written in that source and a fixed seed; the reset reads no file of persons, and a record of every file the reset reads, taken by program, shows it. That is R-16's test as written.

**Position B — a statement by whoever made the data.** The person who wrote the generator and its name parts states that they are invented. It covers what a program cannot see: where the name parts came from.

| Test | A — by construction, recorded | B — a statement |
|---|---|---|
| (a) for agreement, not the registry | no screen or field; one record the checks already take | one sentence in the note or the source |
| (b) must not | shows line 33 is kept by a program's reading | asserts line 33 is kept; no program reads it |
| (c) known numbers | files of persons read at reset: 0 | no count |
| (d) rounds 5 to 7 | round 5 writes the generator and its seed; the same seed gives line 29's same data | round 5 adds the statement |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the data is made only by a generator in the prototype's source from invented name parts and a fixed seed, and the record of the files the reset reads is the evidence, with the screens' words beside it.
*Ground:* it is the only position that R-16's test can pass or fail by a program, and its fixed seed is what line 29 asks anyway.

## G-11 — other bodies

> **G-11** (R-19) Which other bodies, if any, does the project need — and are the census, the examinations authority and the social grant programme, whose lists the data holds, among them?

**Bears on:** R-19. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:19` «The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.»
- `../brief/MINI-REGISTRY-BRIEF.md:34` «Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.»

**Position A — none.** The three lists are made-up data the prototype starts with (line 19), held inside it; the enrolment consults no body. R-19's list of bodies is empty, and its test says so.

**Position B — the three bodies, simulated.** The census, the examinations authority and the grant programme are each simulated on the computer as a small service that hands over its list, and the registry reads from them at reset. This shows the agreement the real registry will need: three sources, three owners.

| Test | A — none | B — three simulated bodies |
|---|---|---|
| (a) for agreement, not the registry | nothing added | adds three bodies to connect to and the code to reach them |
| (b) must not | nothing to connect to | kept by simulation, as line 34 allows; three more things for R-18 to watch |
| (c) known numbers | no bearing | no bearing, if the simulations serve the same lists |
| (d) rounds 5 to 7 | round 5 writes the lists as data | round 5 also builds three simulations; round 6 reads through them |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the project needs no other body; the three lists are made-up data inside the prototype, and R-19's list of bodies is empty.
*Ground:* line 19 calls them lists the prototype starts with, and nothing in "What it must do" asks the registry to reach another body.

## G-12 — which checks are "its checks"

> **G-12** (R-22) Which checks are "its checks": the tests of this register, or a set a later round names?

**Bears on:** R-22. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:39` «The working prototype, on your computer, with its checks passing.»
- `../brief/MINI-REGISTRY-BRIEF.md:50` «The goal written in full: every step of enrolling a learner, and every way it can go wrong»
- `../brief/MINI-REGISTRY-BRIEF.md:51` «The count: every requirement against the goal, both ways»

**Position A — the register's tests, with round 3's cases.** Its checks are the tests of R-01 to R-21, written as programs (R-22 is the running of them, and R-23 is the note), together with a check for each way the goal can go wrong that round 3 writes down; round 6 names them in one list.

**Position B — whatever round 6 names.** The build knows best what can be checked; round 6 names its checks, and R-22 asks only that they pass.

| Test | A — register and round 3 | B — round 6's own list |
|---|---|---|
| (a) for agreement, not the registry | no bearing on the prototype's size | no bearing on the prototype's size |
| (b) must not | R-17, R-18, R-20 and R-21 carry the "must not" sentences into the checks | the "must not" sentences are checked only if round 6 chooses to |
| (c) known numbers | R-09 to R-15 carry the known numbers into the checks | the known numbers are checked only if round 6 chooses to |
| (d) rounds 5 to 7 | round 6 knows its checks before it builds; round 4's count, both ways, already ties them to the goal | the round that builds also chooses what proves it built |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: its checks are the tests of R-01 to R-21 written as programs, with a check for each way the goal can go wrong that round 3 names, listed together by round 6.
*Ground:* the register is accepted and each test already says pass or fail; under B the round that builds would also choose what proves it.

## G-13 — the note's one page

> **G-13** (R-23) On what size of page, and in what form, is the note's one page counted?

**Bears on:** R-23. **Passages:**
- `../brief/MINI-REGISTRY-BRIEF.md:40` «A one-page note to the Permanent Secretary: what the prototype shows, and what it does not.»
- `../brief/MINI-REGISTRY-BRIEF.md:55` «The note to the Permanent Secretary»

**Position A — one A4 page, as a PDF.** The note is made as a PDF of one A4 page, portrait, with body type no smaller than 11 point; a program reads its page count.

**Position B — one page by length.** The note is plain text of no more than a set number of words, counted by a program; no page size is fixed.

| Test | A — one A4 page, PDF | B — a word limit |
|---|---|---|
| (a) for agreement, not the registry | no bearing on the prototype | no bearing on the prototype |
| (b) must not | no bearing | no bearing |
| (c) known numbers | pages: 1, read by a command | words at most the limit, read by a command; "one page" is then a proxy |
| (d) rounds 5 to 7 | no bearing; round 8 makes the PDF | no bearing; round 8 counts words |

**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A: the note is one A4 page, portrait, as a PDF with body type no smaller than 11 point, counted by its page count.
*Ground:* the brief says one page, and only A counts a page rather than a stand-in for one.
