# The count — every requirement against the goal, both ways

Round 4 of the brief. The requirements are R-01 to R-23 of `docs/REQUIREMENTS.md`; the goal is S-1 to S-7, F-1 to F-7 and SC-1 to SC-5 of `docs/GOAL.md` as the owner ruled it on `docs/GOAL-QUESTIONS-PAPER.md` (D-2026-10-31-07). Each pair is read from the requirement's test and is one row of `docs/count/count.csv`, with the words of the test that ground it.

| Way | Reached | Not reached | Of |
|---|---|---|---|
| requirements → goal | 13 | 10 | 23 |
| goal → requirements | 12 | 7 | 19 |

## Requirements whose test reaches no element of the goal

| Requirement | Ground: the words of its test |
|---|---|
| R-08 | the made-up data: "the prototype's data reset, before any enrolment" |
| R-09 | the made-up data: "the prototype's data reset, before any enrolment" |
| R-10 | the made-up data: "the prototype's data reset, before any enrolment" |
| R-11 | the made-up data: "the prototype's data reset, before any enrolment" |
| R-12 | the made-up data: "how many of these children the registry's search catches is not tested here" |
| R-13 | the made-up data: "the prototype's data reset, before any enrolment" |
| R-16 | the made-up data: "list every source from which the data is made" |
| R-19 | what the prototype must not do outside the goal: "the list of other bodies the prototype draws on" |
| R-21 | what the prototype must not do outside the goal: "run every check of the screens; while they run and when they end, read the list of windows again" |
| R-23 | the delivery: "the note as delivered" |

## Elements of the goal no requirement's test reaches

| Element | The ruling or source that put it in the goal |
|---|---|
| F-1 — an entry missing | `docs/GOAL.md:74` brief:11 · brief:14 · ruling:G-07 · groundwork:search_rule.csv:10; as ruled, `docs/GOAL-QUESTIONS-PAPER.md:302` seen on SC-4, each entry missing named (Q-4, Q-5, Q-8) |
| F-2 — the date of birth in the wrong form | `docs/GOAL.md:82` ruling:G-07 · ruling:G-09 · groundwork:settings.csv:17; as ruled, `docs/GOAL-QUESTIONS-PAPER.md:303` a date naming no day refused too (Q-1); before the search (Q-7) |
| F-3 — a school not among the three | `docs/GOAL.md:90` brief:24 · ruling:G-07 · groundwork:settings.csv:18; as ruled, `docs/GOAL-QUESTIONS-PAPER.md:304` refused on SC-4 where it reaches the registry (Q-6) |
| F-4 — more than one learner found | `docs/GOAL.md:98` ruling:G-02 · ruling:G-05 · ruling:G-09 · ruling:Q-14 · groundwork:search_rule.csv:16 · groundwork:search_rule.csv:17 · groundwork:settings.csv:13; as ruled, `docs/GOAL-QUESTIONS-PAPER.md:305` SC-5 also says nothing was saved (Q-8) |
| F-5 — the same child, not caught | `docs/GOAL.md:106` brief:7 · brief:13 · brief:14 · R-01 · R-06 · R-07 · ruling:G-05 · groundwork:search_rule.csv:5 · groundwork:search_rule.csv:6 · groundwork:settings.csv:14; as ruled, `docs/GOAL-QUESTIONS-PAPER.md:306` unchanged |
| F-6 — a record not saved | `docs/GOAL-QUESTIONS-PAPER.md:313` added by the ruling on Q-3 |
| F-7 — a different child taken for a learner | `docs/GOAL-QUESTIONS-PAPER.md:313` added by the ruling on Q-12 |

**What round 6 must build that no requirement's test reaches:** all seven ways the goal goes wrong, F-1 to F-7; each is in the goal by the brief's search rule or a ruling, and its check under the ruling on G-12 is the only test it will have. **What no element of the goal carries:** the made-up data and its known numbers (R-08 to R-13, R-16), the simulation of other bodies (R-19), the windowless running of the checks (R-21) and the note to the Permanent Secretary (R-23).
