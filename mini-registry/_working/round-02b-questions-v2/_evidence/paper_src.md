# The groundwork's open questions — a paper for the owner's ruling

**What this is.** `docs/GROUNDWORK.md` closes with 14 questions no source answers. This paper recommends one answer to each, so that you can rule on all 14 in one act and round 5 can make the data from the sources and your ruling. **Every recommendation is a proposal, not a decision.** A passage is quoted as `` `<path>:<line>` «<words>» ``, paths from the estate's root. Version 2: every dependency is declared in both sections, and each question's two positions are judged under the recommended answer of every question it depends on.

## Given to every position

Every fact below binds every position of every question; no position is judged on lacking one.

- **The brief**, whole, first in precedence; its rule of sameness: `../brief/MINI-REGISTRY-BRIEF.md:13` «if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;» · and `../brief/MINI-REGISTRY-BRIEF.md:29` «The data is made the same way every time it is reset.»
- **The register**, every requirement and its test, R-01 to R-23: `docs/REQUIREMENTS.md:15-320`.
- **The thirteen rulings**: the summary rows G-01 to G-13, `docs/GAPS-PAPER.md:26-38`, and the one-sentence recommendation closing each question's section — among them, whole: `docs/GAPS-PAPER.md:196` «**Recommendation — a proposal for the owner's ruling, not a decision.** We recommend Position A, with settings 1 to 4 for round 2 — the 4 differ in at least one letter, the other 4 match letter for letter and in the same capitals, so none of the 8 differs in capitals only, and no two different children share all three fields — which gives round 7 the known answer of 4 of the 8 caught and R-12 a count of 4 whether or not its comparison heeds capitals.»
- **The groundwork**: every settings row, `docs/groundwork/settings.csv:2-18` — the known numbers (rows 2 to 6), `docs/groundwork/settings.csv:7` «list_entries,68», `docs/groundwork/settings.csv:8` «lists_carrying_each_of_the_8,exactly 2», `docs/groundwork/settings.csv:14` «of_the_8_caught_by_the_search,4»; every field, `docs/groundwork/lists.csv:2-17`; every rule, `docs/groundwork/search_rule.csv:2-18`, among them `docs/groundwork/search_rule.csv:6` «every difference but capitals makes two values differ» and `docs/groundwork/search_rule.csv:9` «does_not_read,the key table».

**The tests**, the same for every question; a table carries only those that bear. **(a)** `../brief/MINI-REGISTRY-BRIEF.md:7` «wants one list of learners instead of three» · «The prototype is for agreement. It is not the registry.» **(b)** `../brief/MINI-REGISTRY-BRIEF.md:33` «Hold any real person's data.» · `../brief/MINI-REGISTRY-BRIEF.md:34` «Connect to anything outside your computer.» · `../brief/MINI-REGISTRY-BRIEF.md:35` «Open a window on its own.» No question touches (b). **(c)** `../brief/MINI-REGISTRY-BRIEF.md:29` «The numbers are fixed so that every later count has a known answer.» Every table's row "(c) known numbers" says whether the position can be built, with every other recommendation, to the brief's numbers, the settings and the other recommended values; the program of A13 decides it. **(d)** `../brief/MINI-REGISTRY-BRIEF.md:52` «The scaffold and the made-up data» · `../brief/MINI-REGISTRY-BRIEF.md:53` «The goal built» · `../brief/MINI-REGISTRY-BRIEF.md:54` «how many of the 8 the search catches».

## The set

The 14 questions, listed by command into `_working/round-02b-questions-v2/_evidence/QUESTIONS.md` from `docs/GROUNDWORK.md` lines 43 to 56; it printed `14` and `0 not found`. The pairs of dependent questions are in `_working/round-02b-questions-v2/_evidence/DEPENDENCIES.csv`.

---

## Q-1 — the date ages are reckoned on

{Q1}

**Depends on:** none. **Depended on by:** none.

**Passages:** `docs/GAPS-PAPER.md:31` «one fixed date held in the settings».

**Position A — 2026-10-31**, the date of the ruling, `docs/GROUNDWORK.md:5` «the owner's ruling of 31 October 2026». Ages 6 to 12 then mean a date of birth from 2013-11-01 to 2020-10-31.

**Position B — any other fixed date.** Round 5 makes the dates of birth to it in the same way.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |

**Proposal — not a decision.** Any date serves equally; we recommend 2026-10-31, because the record already holds it.

## Q-2 — the order of the reset's enrolment

{Q2}

**Depends on:** Q-11, Q-14. **Depended on by:** Q-5, Q-9.

**Passages:** `../brief/MINI-REGISTRY-BRIEF.md:19` «the school census, the examinations authority's candidate list and the social grant programme's list».

**Position A — the order of line 19:** the census, the candidate list, the grant list; within each, by entry number (Q-11), 1 upwards.

**Position B — any other fixed order.** With Q-14 as recommended no entries of two children match, so the order changes which numbers are given, never which entries are joined: all six orders of the lists give 64 learners and 4 caught.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |
| (d) round 7: caught | 4 | 4 | both meet |

**Proposal — not a decision.** Any fixed order serves equally; we recommend line 19's order, then entry number, because the brief already names the lists in it.

## Q-3 — the seed

{Q3}

**Depends on:** none. **Depended on by:** none.

**Passages:** `docs/GAPS-PAPER.md:35` «a fixed seed».

**Position A — 20261031.** The seed draws names, dates and shuffles; the numbers are the settings', whatever the seed.

**Position B — any other whole number.** The same holds of it.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |

**Proposal — not a decision.** Any seed serves equally; we recommend 20261031, the ruling's date, easy to recognise in the source.

## Q-4 — the first learner number

{Q4}

**Depends on:** Q-13. **Depended on by:** none.

**Passages:** `docs/GAPS-PAPER.md:26` «one above the highest held».

**Position A — 1.** The highest held when none is held is read as 0; with Q-13's 64, the numbers after reset run 1 to 64, so the highest equals the count of learners.

**Position B — any other first number**, such as 1001, numbers of one width: 1001 to 1064.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |
| (d) round 5 checks the highest number | = 64 | = 1064 | both meet |

**Proposal — not a decision.** Any first number serves; we recommend 1, so that the highest number is the count.

## Q-5 — which lists carry the 8

{Q5}

**Depends on:** Q-2, Q-6. **Depended on by:** Q-6, Q-9.

**Passages:** `../brief/MINI-REGISTRY-BRIEF.md:26` «children whose family name is spelt differently on one list».

**Position A — every pair of lists, each with a catch and a miss.** Census and candidate list: 3 (2 matching, 1 spelt differently); census and grant list: 3 (1 and 2); candidate and grant list: 2 (1 and 1). Each of the 4 is spelt differently on the later of its two lists in Q-2's order.

**Position B — every one of the 8 on the census and one other list:** 4 with each, 2 spelt differently in each; the same rule for which list.

| Test | A | B | Divides? |
|---|---|---|---|
| (a) one list of learners instead of three, on every pair | joins and misses on all 3 pairs | candidate and grant list never joined | divides |
| (c) known numbers | yes | yes | both meet |

**Proposal — not a decision.** We recommend Position A, so that every pair of lists shows both what the rule joins and what it misses.

## Q-6 — the spread over the lists

{Q6}

**Depends on:** Q-5. **Depended on by:** Q-5, Q-9.

**Passages:** `../brief/MINI-REGISTRY-BRIEF.md:19` «invented children spread over three lists» — which both positions meet.

**Position A — 24, 22 and 22.** With Q-5 as recommended the census carries 6 of the 8, the other two lists 5 each.

**Position B — every child on the census: 60, 4 and 4**, the census holding every child at school, each of the 60 at one of the 3 schools. With Q-5 as recommended it cannot be built: 2 of the 8 are off the census and each other list carries 5 of them. It needs Q-5's Position B, with which it meets every number.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | no: entries left per list after the 8, 54, −1, −1; needs Q-5's B | divides |

**Proposal — not a decision.** We recommend 24, 22 and 22, the one of the two that can be built with Q-5 as recommended.

## Q-7 — the spread over the schools

{Q7}

**Depends on:** Q-9. **Depended on by:** Q-9.

**Passages:** none beyond `docs/groundwork/settings.csv:3` «schools,3».

**Position A — 20 to each school.** With Q-9 as recommended a child's school is read from its entries.

**Position B — any other spread with at least one child at each school**, such as 25, 20 and 15, read the same way.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |

**Proposal — not a decision.** Any such spread serves; we recommend 20 each, so that no school is a special case.

## Q-8 — the other fields of the 4

{Q8}

**Depends on:** none. **Depended on by:** none.

**Passages:** `docs/groundwork/settings.csv:14` «of_the_8_caught_by_the_search,4» — which needs the other 4 to match on all three fields, so both positions give them that; they differ on the 4 alone.

**Position A — the 4 differ in the family name only;** their given names and date of birth match on both lists, letter for letter and in the same capitals.

**Position B — the 4's given names and date of birth left free**, so that some may differ too.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |
| (d) round 7: each miss is line 26's spelling | yes | a miss may also be a date | divides |

**Proposal — not a decision.** We recommend Position A, so that each of the 4 the rule misses is missed for its spelling alone.

## Q-9 — a school on the lists

{Q9}

**Depends on:** Q-2, Q-5, Q-6, Q-7, Q-14. **Depended on by:** Q-7.

**Passages:** `docs/REQUIREMENTS.md:49` «the school clerk enters the child's family name, given names, date of birth and school.» · `docs/groundwork/search_rule.csv:10` «after the clerk has entered all four» · `docs/groundwork/search_rule.csv:13` «every entry of the three lists is enrolled through this same rule».

**Position A — every list carries a school**, one of the 3, the same on both lists of each of the 8; a learner takes the school of the entry that made it. The search does not compare it.

**Position B, at its strongest — the census alone carries a school**, being the schools' own list, and the reset gives each learner made from an entry without one a school of the 3, drawn by the seed, so that every learner holds one. With Q-2, Q-5, Q-6 and Q-14 as recommended, 40 of the 64 learners take their school from the reset, and 36 of the 60 children carry none on any list.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | no: Q-7's 20 each cannot be read for the 36; needs Q-7 to spread the census's children only | divides |
| (d) round 6: the reset enrols with all four entered | every entry carries four | 40 entries carry three; a step no source names adds the fourth | divides |

**Proposal — not a decision.** We recommend that every list carry a school, so that every learner's record is one the clerk's own four entries could make.

## Q-10 — the form of a date on the lists

{Q10}

**Depends on:** none. **Depended on by:** none.

**Passages:** `docs/GAPS-PAPER.md:32` «Date as YYYY-MM-DD».

**Position A — YYYY-MM-DD on all three lists.**

**Position B — each list its own form**, turned into YYYY-MM-DD by the reset before the search.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |
| (d) round 6 builds the search rule as written | nothing before the comparison | a turning step no row of the rule names | divides |

**Proposal — not a decision.** We recommend YYYY-MM-DD on every list, so that nothing stands between a list's date and the comparison.

## Q-11 — the key table's keys

{Q11}

**Depends on:** none. **Depended on by:** Q-2, Q-12.

**Passages:** `docs/groundwork/lists.csv:16` «the table is read by the counts only and never by the search».

**Position A — every one of the 68 entries.** An entry is named by its list and its number in it, `school_census:7`, each list numbered 1 upwards after a shuffle by the seed, so that a number tells nothing of the child; the child is named `C01` to `C60`.

**Position B — only the 16 entries of the 8**, named the same way; each of the other 52 entries is a child on one list only.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes: 60 = 52 + 8 | both meet |
| (d) round 7 reads the 8 | yes | yes | both meet |

**Proposal — not a decision.** Both meet every test; we recommend all 68, for the convenience that every count of children reads one table.

## Q-12 — a learner and the entries it came from

{Q12}

**Depends on:** Q-11. **Depended on by:** none.

**Passages:** `../brief/MINI-REGISTRY-BRIEF.md:54` «how many of the 8 the search catches».

**Position A — yes:** the reset writes, after each entry's search, one row `list_entry, learner_number` to a table of the registry, `list_entry` as Q-11 names it; the search never reads it.

**Position B — no record:** round 7 finds each entry's learner by comparing its three fields with the learners, capitals ignored.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes | both meet |
| (d) round 7 counts what the search caught | what the reset's searches did | what the rule, run again, gives | divides |

**Proposal — not a decision.** We recommend the table `list_entry, learner_number`, so that round 7 counts what the search did.

## Q-13 — the learners after reset

{Q13}

**Depends on:** Q-14. **Depended on by:** Q-4, Q-14.

**Passages:** `docs/GAPS-PAPER.md:40` «64» (not ruled): 60 children, and the 4 the rule does not catch each held twice, with Q-14 as recommended.

**Position A — a setting, 64,** checked by round 5 after every reset.

**Position B — no setting:** the build is held to the brief's numbers, and 64 is derived.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes: 64, derived | both meet |
| (d) round 5 checks the learners after every reset | yes | no check before round 7 | divides |

**Proposal — not a decision.** We recommend a setting of 64 learners after reset, so that round 5 checks it.

## Q-14 — capitals in "share"

{Q14}

**Depends on:** Q-13. **Depended on by:** Q-2, Q-9, Q-13.

**Passages:** `../brief/MINI-REGISTRY-BRIEF.md:13` «(capitals ignored)».

**Position A — capitals ignored:** no entries of two different children share all three fields, capitals ignored, the 4's other spellings included.

**Position B — capitals heeded:** two different children may differ in capitals only. Laying no such pair, its data are A's; each pair it lays, the reset makes one learner.

| Test | A | B | Divides? |
|---|---|---|---|
| (c) known numbers | yes | yes if it lays no pair; one pair gives 63 learners against Q-13's 64 | divides |

**Proposal — not a decision.** We recommend that "share" ignore capitals, as the search does.

---

## Taken together

`_working/round-02b-questions-v2/_evidence/toy.py together` builds a toy data set to the 14 recommendations together and enrols it by the brief's rule. Its output, from `_working/round-02b-questions-v2/_evidence/A5_taken_together.log`:

```
{A5}
```

`toy.py rivals` builds each rival with every other recommendation; its log, `_working/round-02b-questions-v2/_evidence/A13_rivals.log`, prints `can be met: no` for Q-6 and Q-9 alone, as their tables say.
