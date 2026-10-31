# CLAIMS — every claim the note will make, each with its source

Written before the note (the drafting page, item 4). Root of every path: `/Users/arnelaponin/Documents/Dev/wai-demo`. Each row is one claim; `source` is `path:line`; `words` are the words at that line that carry the claim, copied exactly, so that `a1_claims.py` finds each as a substring of that line. A claim resting on two passages has two rows with the same claim number and a letter.

Short names: brief = `brief/MINI-REGISTRY-BRIEF.md`; goal = `mini-registry/docs/GOAL.md`; paper = `mini-registry/docs/GOAL-QUESTIONS-PAPER.md` (ruled whole, D-2026-10-31-07); dup = `mini-registry/docs/DUPLICATES.md`; review = `mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md`; ruling = `_coordination/_ledger/20261031T195657Z_MR_ruled_D-2026-10-31-11.yaml`.

| Claim | What the note says | Source | Words |
|---|---|---|---|
| K01a | The note is addressed to the Permanent Secretary | mini-registry/CONSTANTS.md:29 | the Permanent Secretary receives the note |
| K01b | The note is addressed to the Permanent Secretary | brief/MINI-REGISTRY-BRIEF.md:40 | A one-page note to the Permanent Secretary: what the prototype shows, and what it does not. |
| K02 | The Ministry is the Ministry of Education, Youth and Skills | brief/MINI-REGISTRY-BRIEF.md:7 | Progressa's Ministry of Education, Youth and Skills |
| K03 | A clerk can enrol a child; the registry does not register the same child twice | brief/MINI-REGISTRY-BRIEF.md:7 | a school clerk enrols a child, and the registry does not register the same child twice |
| K04 | Exactly one learner with the same family name, given names and date of birth, capitals aside: shown, nothing new entered | brief/MINI-REGISTRY-BRIEF.md:13 | if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new |
| K05 | Not recognised when the family name is spelt differently; 4 of the 8 caught, the other four held twice | mini-registry/docs/DUPLICATES.md:26 | Each missed child is held twice, under two learner numbers. |
| K06 | The Ministry wants one list of learners instead of three | brief/MINI-REGISTRY-BRIEF.md:7 | wants one list of learners instead of three |
| K07 | A small working prototype, for the planning unit's agreement before the real one is built | brief/MINI-REGISTRY-BRIEF.md:7 | Before anyone builds the real thing, the planning unit wants to see a small working prototype |
| K08 | The clerk enters family name, given names, date of birth and school | brief/MINI-REGISTRY-BRIEF.md:11 | A school clerk enters a child's family name, given names, date of birth and school. |
| K09 | The registry searches for the child first | brief/MINI-REGISTRY-BRIEF.md:11 | The registry searches for the child first |
| K10 | None found: a new learner number, the record saved | brief/MINI-REGISTRY-BRIEF.md:14 | if it finds none, it gives the child a new learner number and saves the record |
| K11 | The clerk sees which of the two happened | brief/MINI-REGISTRY-BRIEF.md:15 | the clerk sees which of the two happened |
| K12a | Refused before the search: a detail missing, a date naming no real day, a school other than the three | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:297 | before the search (Q-7), holds: all four entered, spaces only missing (Q-4, Q-5); the date a day (Q-1); the school one of the 3 (Q-6) |
| K12b | The school other than the three is refused | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:154 | such a school is refused on SC-4 |
| K13a | The clerk is told each fault | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:297 | every fault found (Q-9) |
| K13b | The clerk is told each fault | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:192 | each refusal names its fault |
| K14 | Nothing is saved on a refused entry | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:69 | nothing saved (Q-7) |
| K15 | It runs on one computer | brief/MINI-REGISTRY-BRIEF.md:39 | The working prototype, on your computer, with its checks passing. |
| K16a | It connects to nothing outside the computer | brief/MINI-REGISTRY-BRIEF.md:34 | Connect to anything outside your computer. |
| K16b | It connects to nothing outside the computer (met) | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:28 | A6 — nothing connects, nothing opens | met |
| K17 | All of its checks pass | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:24 | `# fail 0` |
| K18a | None of the checks opens a window | brief/MINI-REGISTRY-BRIEF.md:35 | Open a window on its own. Every check of the screens runs without one. |
| K18b | None of the checks opens a window (met) | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:33 | windows added: 0 |
| K19a | 60 invented children | brief/MINI-REGISTRY-BRIEF.md:23 | Children | 60 |
| K19b | three schools | brief/MINI-REGISTRY-BRIEF.md:24 | Schools | 3 |
| K20 | Three lists: school census, examinations authority's candidate list, social grant programme's list | brief/MINI-REGISTRY-BRIEF.md:19 | The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list. |
| K21a | Eight children on two lists | brief/MINI-REGISTRY-BRIEF.md:25 | Children on more than one list | 8 |
| K21b | Eight children on two lists (each on exactly two) | mini-registry/docs/DUPLICATES.md:13 | 8 children, each on exactly two entries |
| K22 | For four of them the family name on one list differs by a single letter | mini-registry/docs/DUPLICATES.md:26 | Each of the four missed differs in its family name by one letter and in nothing else |
| K23 | The search catches 4 of the 8 | mini-registry/docs/DUPLICATES.md:5 | The search catches 4 of the 8. |
| K24a | The four caught have the same three details on both lists | mini-registry/docs/DUPLICATES.md:26 | each of the four caught matches on all three fields letter for letter |
| K24b | Each caught child is held once | mini-registry/docs/DUPLICATES.md:13 | A child is **caught** where both its entries point to one learner |
| K25 | Each of the other four held twice, under two learner numbers | mini-registry/docs/DUPLICATES.md:26 | Each missed child is held twice, under two learner numbers. |
| K26 | The search treats every difference other than capitals as a different child | mini-registry/docs/GOAL.md:39 | every difference but capitals makes two values differ |
| K27 | A limit of the search step as defined | mini-registry/docs/GOAL.md:105 | This is a limit of the search step, the brief's own rule |
| K28 | The invented data is made so that four of the eight differ; the figure does not show real lists | mini-registry/docs/DUPLICATES.md:28 | it does not show how the real registry would fare on real lists, for the data is invented and made so that 4 of the 8 differ by one letter in the family name alone |
| K29 | It is not the registry; it is for agreement | brief/MINI-REGISTRY-BRIEF.md:7 | The prototype is for agreement. It is not the registry. |
| K30 | Enrolment only; no way to look a learner up | mini-registry/docs/GOAL.md:7 | there is no screen for looking learners up |
| K31a | Only invented data; Progressa is fictional | brief/MINI-REGISTRY-BRIEF.md:3 | Everything in it is invented for Progressa, the fictional country |
| K31b | Every screen says so | brief/MINI-REGISTRY-BRIEF.md:33 | Every screen says "Invented data, Progressa is fictional". |
| K31c | Every screen says so (as built) | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:69 | R-17's line on the screen |
| K32 | Connected to no other body; the three lists are part of the invented data | brief/MINI-REGISTRY-BRIEF.md:34 | Other bodies, if the project needs them, are simulated. |
| K33a | Two different children sharing the three details: the second taken for the first, nothing new saved | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:259 | the child is shown as the learner on SC-2, nothing saved |
| K33b | The paper's proposals are ruled | _coordination/_ledger/20261031T181936Z_MR_ruled_D-2026-10-31-07.yaml:8 | Rule all 13 as recommended |
| K34 | No two children in the invented data share all three | mini-registry/docs/GOAL.md:95 | no two different children share all three fields |
| K35 | Three points kept in their simplest form | _coordination/_ledger/20261031T195657Z_MR_ruled_D-2026-10-31-11.yaml:8 | let's currently go with simplest approaches |
| K36a | An entry of blank characters of any kind, not only spaces, is treated as missing | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:104 | Q-4 (any whitespace read as "spaces") |
| K36b | Spaces only are an entry missing (the ruling) | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:115 | spaces only are an entry missing |
| K37 | A school other than the three, once refused, is not shown again on the way back | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:104 | Q-6 with Q-8 (a fourth school lost on the way back) |
| K38a | More than one matching learner: refused, nothing saved | mini-registry/docs/GOAL-QUESTIONS-PAPER.md:305 | SC-5 also says nothing was saved |
| K38b | Never arises in the invented data | mini-registry/docs/GOAL.md:95 | Under the data's settings it is never reached |
| K38c | Checked only on a record added for the purpose | mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md:82 | F-4's check writes its own record |
