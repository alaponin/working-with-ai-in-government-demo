# The limits, listed again by the reviewer from the record

Listed by the reviewer from the sources themselves, before the round's LIMITS.md was compared: the brief (whole), the register of requirements, every closing proposal of the gaps paper (its summary rows 26 to 38 and the recommendation closing each section, ruled by D-03; G-14 closed from the brief), of the earlier questions paper (ruled by D-05) and of the goal's questions paper (ruled by D-07), the rulings of 21:56 (D-11) as the build's accepted review names them, the build's accepted review, the count, the duplicates count and the goal. A row is a limit where it says what the prototype does not do or show, or what it accepts or refuses that a reader would not assume. Ruled answers that are settings of the invented data, definitions or the note's own form are listed at the end, not as limits.

Root `/Users/arnelaponin/Documents/Dev/wai-demo`. Short names as the round's: brief, req, gaps, qp, gqp, goal, count, dup, build, D11. `r6_limits.py` checks each row's words at its line, each `note` row's words in `docs/NOTE.md`, and each `left out` row's round row in the report's left-out table.

| Row | The limit | Source | Words at the source | Round's row | Where | Note words, or the round's row in the report's left-out list |
|---|---|---|---|---|---|---|
| M01 | For agreement; not the registry | brief:7 | The prototype is for agreement. It is not the registry. | B01 | note | It is not the registry. |
| M02 | Everything invented; Progressa fictional | brief:3 | Everything in it is invented for Progressa | B02 | note | Progressa is fictional |
| M03 | No real person's data; every screen says so | brief:33 | Hold any real person's data. | B02, R01 | note | it holds only invented data |
| M04 | Connects to nothing outside the computer | brief:34 | Connect to anything outside your computer. | B03, R02 | note | connects to nothing outside it |
| M05 | Other bodies only simulated; none needed, the lists are data | brief:34 | Other bodies, if the project needs them, are simulated. | R03, G11 | note | no system of the census, the examinations authority or the social grant programme is linked to it |
| M06 | Opens no window; checks run without one | brief:35 | Open a window on its own. | B04 | note | none of them opens a window |
| M07 | One goal, enrolment | brief:11 | One goal: **enrol a learner.** | R04 | note | it offers enrolment only |
| M08 | The search forgives capitals and nothing else | brief:13 | (capitals ignored) | G14 | note | the search treats every difference other than capital letters as a different child |
| M09 | The register: no real person's data | req:222 | The prototype holds no real person's data. | R01 | note | it holds only invented data |
| M10 | The register: nothing outside the computer | req:248 | The prototype connects to nothing outside the computer it runs on. | R02 | note | connects to nothing outside it |
| M11 | The register: another body only simulated | req:261 | that body is simulated | R03 | note | is linked to it |
| M12 | The register: one goal | req:36 | The prototype has one goal: to enrol a learner. | R04 | note | it offers enrolment only |
| M13 | The register: no window on its own | req:274 | The prototype opens no window on its own. | B04 | note | none of them opens a window |
| M14 | The register's test on the 4 does not test what the search catches | req:173 | how many of these children the registry's search catches is not tested here | C19 | left out | C19 |
| M15 | More than one learner found: never reached; refused | gaps:27 | Never reached under the data's settings; if it is, enter nothing new and refuse the entry | G02 | note | this never arises in the invented data |
| M16 | None of the 8 differs in capitals only | gaps:30 | none of the 8 differs in capitals only | G05 | note | None of the eight differs in capital letters alone |
| M17 | No two different children share all three fields | gaps:196 | no two different children share all three fields | P14 | note | No two children in the invented data share all three. |
| M18 | Date only as YYYY-MM-DD, refused otherwise | gaps:254 | the date entered as YYYY-MM-DD and refused otherwise | G07, C21 | note | not written as year, month and day |
| M19 | The school not searched on | gaps:254 | the school not searched on | none (P09's reason states it) | note | with the same family name, given names and date of birth |
| M20 | No screen for looking learners up | gaps:33 | there is no screen for looking learners up | G08, C12 | note | with no way to look a learner up |
| M21 | No other body: the lists are data inside | gaps:36 | the three lists are data inside the prototype, not bodies it connects to | G11 | note | The three lists are part of the invented data |
| M22 | Its checks are the register's tests, as programs | gaps:37 | The register's tests R-01 to R-21 as programs | G12 | left out | G12 |
| M23 | A space is part of a name | gaps:20 | so a space is part of a name | G14 | note | the search treats every difference other than capital letters as a different child |
| M24 | The 4 differ in the family name only | qp:168 | so that each of the 4 the rule misses is missed for its spelling alone | P08 | note | for four of them the family name on one list differs by a single letter |
| M25 | Every list carries a school, the same for each of the 8 | qp:187 | We recommend that every list carry a school | P09 | left out | P09 |
| M26 | Every list holds its dates in the one form | qp:206 | We recommend YYYY-MM-DD on every list | P10 | left out | P10 |
| M27 | "Share" ignores capitals | qp:281 | We recommend that "share" ignore capitals, as the search does. | P14 | note | No two children in the invented data share all three. |
| M28 | A date naming no day refused | gqp:57 | a date that names no day is refused on SC-4 | Q01 | note | not naming a real day |
| M29 | No age held on the entry; a date after the reckoning date enrolled too | gqp:77 | the child is enrolled; 6 to 12 holds the data, not the entry | Q02 | left out | Q02 |
| M30 | A record not saved or no number given: F-6 | gqp:96 | F-6 shown on SC-5 | Q03 | left out | Q03 |
| M31 | No length and no character refused in a name | gqp:115 | We recommend no length and no character refused | Q04a | note | A name is not limited in length, and no character in it is refused. |
| M32 | Spaces only are an entry missing | gqp:115 | spaces only are an entry missing | Q04b | note | is treated as missing |
| M33 | An entry missing is refused | gqp:134 | an entry missing is refused on SC-4 | Q05 | note | An entry with a detail missing |
| M34 | A school not among the three refused where it reaches; the clerk's screen offers the three alone | gqp:142 | SC-1 offers the 3 alone under both positions | Q06 | note | a school other than the three is refused before the search |
| M35 | A different school on a learner found: no notice | gqp:249 | We recommend Position A: no notice. | Q11 | left out | Q11 |
| M36 | A different child sharing the three is taken for the learner; nothing for the clerk to do | gqp:268 | F-7, a limit of the rule; nothing for the clerk to do | Q12 | note | The second would be taken for the first, and nothing new saved. |
| M37 | More than one learner found: checked only on a record its check writes | build:82 | F-4's check writes its own record | V08 | note | checked only on a record added for the purpose |
| M38 | Any blank characters taken as missing (kept as built) | build:104 | Q-4 (any whitespace read as "spaces") | V09 | note | An entry of blank characters of any kind, not only spaces, is treated as missing. |
| M39 | A fourth school lost on the way back (kept as built) | build:104 | a fourth school lost on the way back | V10 | note | is not shown again when the clerk returns to correct the entry |
| M40 | The three kept in the simplest form | D11:8 | let's currently go with simplest approaches | V11 | note | Three points are kept in their simplest form. |
| M41 | The window checks read at intervals, by window number, over the whole login session | build:103 | a window opened and closed between two readings is not seen | V16 | left out | V16 |
| M42 | The record's tracer: the build's record check exits 1 | build:100 | resolves names given relative to a directory descriptor against the working directory | V20 | left out | V20 |
| M43 | F-1 to F-7: each one's check its only test | count:37 | its check under the ruling on G-12 is the only test it will have | C17 | left out | C17 |
| M44 | No element of the goal carries the data, the simulation, the windowless checks, the note | count:37 | What no element of the goal carries: | C18 | left out | C18 |
| M45 | The 4 missed differ by one letter in the family name | dup:26 | Each of the four missed differs in its family name by one letter and in nothing else | C04 | note | for four of them the family name on one list differs by a single letter |
| M46 | Not how the real registry would fare on real lists | dup:28 | it does not show how the real registry would fare on real lists | C06 | note | not how many children a registry would hold twice on real lists |
| M47 | A limit of the search step, not of the whole | goal:105 | This is a limit of the search step, the brief's own rule | C05 | note | This is a limit of the search step as it is defined |
| M48 | A date in any other form refused | goal:32 | a date in any other form is refused (F-2) | C21 | note | not written as year, month and day |

**Ruled answers that are not limits** (each of the round's rows, read and agreed as not a limit or as settled by a row above): G01, G03, G04, G06, G09, G10, G13 (the note's form; met at one A4 page, 11-point type); P01–P07, P11–P13 (settings of the invented data); Q05–Q10, Q13 (refusals and screens the note states, or the way back); B04, R05. The other rulings of the record (D-01, D-02, D-04, D-06, D-08, D-09 Node.js, D-10, D-12, D-13, D-14 not sending) carry no limit of what the prototype shows.

**Counts.** Limits listed here: 48 rows. In the note: 37. Left out with the round's reason in the report: 11 (M14, M22, M25, M26, M29, M30, M35, M41, M42, M43, M44). Unaccounted: 0. Rows the round's list lacks: 1, M19 (the school not searched on), which the note carries in its sentence on what the search compares, so not missing. Rows of the round's list not here: 0 among its limits (its 38 limits each map to a row above).
