---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md (C-2026-10-31-11)
written_by: a session that neither wrote nor carried out the instruction — MR · review · answers to the groundwork's questions (C-2026-10-31-12), started as a sub-agent
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` at 15:30:57 UTC, this session's first command
window: 2026-10-31 15:31:02 UTC (the started entry 20261031T153102Z_MR_started_C-2026-10-31-12.yaml) to 2026-10-31 15:41 UTC, no pause; closed at the moment of writing, this file's last write
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md, with G1 appended
---

# REVIEW — the paper answering the groundwork's 14 questions

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-review/_evidence/` (below, `R/`). Evidence of the round: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/` (below, `W/`).

## 1. The tests of success, one by one

| Test | Met? | Evidence read or produced here |
|---|---|---|
| A1 — 14 questions, each at its line | met | `W/A1_questions.log` prints `14` / `0 not found`. Re-done by another route: `R/R_questions_citations.log` reads the numbered items under "Gaps against the sources" — `numbered items ... 14; numbers [1, ..., 14]` — and `QUESTIONS.md lines 14; same as this listing: True`. |
| A2 — 0 unanswered, 0 extra | met | `W/A2_A3_A4_check.log`; and here, both ways: `in the groundwork, not answered in the paper: 0` · `in the paper, not in the groundwork: 0` · `quoted at another line or not word for word: 0`. |
| A3 — every passage at its line | met | `W/A2_A3_A4_check.log` `0 not found, 0 wrong line`; here `citations 45; not found at their line 0`, each read in full against the sentence citing it (part 5). |
| A4 — 2, 1, 1 per section | met | `W/A2_A3_A4_check.log`: every Q-1 to Q-14 reads `2 1 1`; table rows 26, both meet 15, divides 11 — counted again by hand from the paper, 15 and 11. |
| A5 — the toy run | met | `W/A5_taken_together.log`: 60, 3, 68, 8, 4, ages 6 to 12, 64 learners after reset, 4 of the 8 caught; re-established by another route in part 2. |
| A6 — what each recommendation touches | met | The report's table, section A6, read against the 14 recommendations: none adds a compared field, forgives anything but capitals, or gives the search the key table; Q-12's table is written by the reset and read by round 7 only. |
| A7 — under 20 KB | met | `R/R_outputs.out`: `18410 /Users/.../docs/QUESTIONS-PAPER.md`. |
| A8 — sources unchanged | met | `W/A8_sources.log` diff empty; `R/R_outputs.out` prints the same seven checksums now, the first three being those of the instruction's section 2. |
| A9 — placement and trace exit 0 | met | `W/A9_placement.out`, `W/A9_trace.out`; run again here, both `clean`, `EXIT=0` (part 6). |
| A10 — record check exits 0 | met | `W/record/check.out` `## Findings — 0`; run again here, `EXIT=0` (part 6). |
| A11 — started and finished beside issued | met | `R/R_ledger_show.out` prints `issued` 15:07:57Z, `started` 15:21:48Z, `finished` 15:30:40Z, all version 1. |

Every acceptance criterion is met. The verdict turns on section 3 of the instruction, which the criteria do not count (part 7).

## 2. One figure re-established

**The figure:** "Taken together" — 60 children, 3 schools, 68 entries (24, 22, 22), 8 on more than one list, 4 spelt differently, ages 6 to 12, 64 learners after reset, 4 of the 8 caught.
**The round's route:** `W/taken_together.py`, seeded random draws of name parts and dates, the 8 laid by a `PAIRS` list and the reset run once in the order of Q-2.
**The route here:** `R/r_toy.py` (sha256 `56f1d8d8…89125`), written from the paper's words: no random draw; names and dates laid by arithmetic, both bounds of Q-1's date range laid; the lists composed table-first from Q-5's pairs and Q-6's totals; the reset a separate function that sees only what an entry carries and compares by `casefold`. Log `R/R_toy.log`:

```
  children: 60
  schools: 3
  entries: 68
  per_list: [24, 22, 22]
  on_two: 8
  spelt_differently: 4
  spelt_differently_capitals_ignored: 4
  ages: (6, 12)
  learners: 64
  highest: 64
  without_school: 0
  more_than_one: 0
  caught: 4
```

**The two agree** on every number. The same run checks the paper's claims about what does not matter: all six orders of the lists, and each list's entries reversed, give `learners 64 caught 4` (Q-2's Position B holds); three other layings of names give the same numbers (Q-3); Q-1's bounds give ages 13, 12, 6 and 5 for 2013-10-31, 2013-11-01, 2020-10-31 and 2020-11-01, so "2013-11-01 to 2020-10-31" is exact; Q-6's 18, 17 and 17 hold; Q-9's rival cell, `without a school 40`, holds; and Q-14's rival, one pair differing in capitals only, gives `learners 63`, "64 less the merged pairs".

The times and counts the report gives in its own words were read at their sources: the window against `W/record/window.out` and the started entry (15:21:48) and the report's last write (15:30:29); the run times against `W/record/runs.jsonl` (15:25:57, 15:26:41, 15:28:37); "45 quoted passages in 7 files" against the log and this review's own count, 45; "3 runs, 12 files read" against `W/record/RECORD.txt`; `before.sha256` at 15:25:39.827, after the start list at 15:25:39.626. One sentence does not hold as worded (part 8, item 6).

## 3. The outputs exist

`R/R_outputs.out`, 15:37:49 UTC: `docs/QUESTIONS-PAPER.md` 18410 bytes, sha256 `0bbc89264c1a0ee5f837e71aa3f1dbb03abb5ee10487c118aa3173f2ce4ae6cb`, as the report declares; the evidence folder, 17 entries; the report, 11241 bytes. All three outputs found at their paths.

## 4. The running application

Not applicable: the round wrote a paper, no application model.

## 5. What a review of this kind runs — `_kinds/analysis.md`, part 2

- **Every citation read at its source against the sentence that cites it.** `R/R_questions_citations.log` prints each of the 45 `path:line` citations beside the whole source line, and the 7 references to a line in prose (lines 13, 19, 26, 40, 54). Every one says what the sentence citing it says. Two quote less than the passage holds, without misquoting it (part 8, item 1).
- **The set listed again and compared both ways.** 14 and 14; 0 missed, 0 extra, 0 off their line (part 1, A1 and A2).
- **The tables read against "Given to every position" and against the other position's cells.** No table denies a rival a fact the sources or the paper grant. Where a rival's cell gives a figure, the figure was run (part 2). One table judges its two positions under different answers to another question. That is G1.
- **One figure worked out again by another route.** Part 2.

The faults of part 1 of the page, read against the paper: items 1, 3, 4 and 6 are not shown. Item 2 and item 5 are shown once each, by G1.

## 6. The four mechanical checks, run here

Run directly, outside `round_record.py run`, by `R/r_mechanical.sh`, at 15:37:48–49 UTC:

| Check | Command | Exit | Log |
|---|---|---|---|
| trace | `trace_check.py --constants …/mini-registry/CONSTANTS.md --coordination …/_coordination/CONSTANTS.md …/REPORT_QUESTIONS_2026-10-31.md` | 0 | `R/R_trace.out` |
| placement | `placement_check.py --constants …/mini-registry/CONSTANTS.md …/PROMPT_QUESTIONS_2026-10-31.md` | 0 | `R/R_placement.out` |
| record | `round_record.py check --record …/round-02b-questions/_evidence/record --report …/REPORT_QUESTIONS_2026-10-31.md --tolerance 2 --out R/R_record_check.out`, the options of `check.out`'s `# run with:` | 0 | `R/R_record_check.log` |
| ledger show | `ledger.py show --constants …/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-11` | 0 | `R/R_ledger_show.out` |
| ledger check | `ledger.py check --constants …/_coordination/CONSTANTS.md` | 0 | `R/R_ledger_check.out` |

The lines that decide:

```
trace check: clean
placement check: clean
## Findings — 0
check: clean
```

The record check lists this review's own files as `added after the window closed …, by another hand or later`, which is as it should be. `ledger.py check` prints no line naming `MR`: its whole output is `check: clean`.

**The account on the three entries**, as `show` prints them: `issued` `account: arne.laponin@gmail.com`; `started` `account: arne.laponin@gmail.com`; `finished` `account: arne.laponin@gmail.com`. The report's declaration names `arne.laponin@gmail.com`. They agree.

## 7. The verdict: not accepted

**One gap, G1.** Every criterion A1 to A11 is met, every citation holds, and the recommendations taken together give the known numbers by a second route. The paper fails one rule of its instruction's section 3, at one pair of questions. As written, that pair lets a ruling carry an impossible setting into round 5.

**G1 (item) — Q-6 judges its rival without Q-5 as recommended, so the rival is credited with numbers it cannot reach.** The instruction, section 3: «Where one answer depends on another, say so in one line, "depends on Q-<n>", and judge it with that answer as recommended; never assume another question's recommendation silently.» Q-5 declares the dependency in one direction: `QUESTIONS-PAPER.md:93` «Depends on Q-6 and Q-2.» Q-6 carries no "depends on" line. It judges Position A under Q-5 as recommended, `QUESTIONS-PAPER.md:113` «With Q-5 as recommended, 18, 17 and 17 children are on one list only», but grants Position B, `QUESTIONS-PAPER.md:115` «every child on the census: 60, 4 and 4», the row `QUESTIONS-PAPER.md:120` «| (c) 60, 8, 68 | yes | yes | both meet |». Under Q-5 as recommended, `QUESTIONS-PAPER.md:95`, the candidate list carries 3 + 2 = 5 of the 8 and the grant list 3 + 2 = 5, and 2 of the 8 are on the candidate and grant lists, off the census. Position B's 4 entries per list and "every child on the census" cannot both hold with that. `R/R_toy.log`: «Q-6 B (60, 4, 4) with Q-5 A as recommended: cannot be built: entries still needed per list after the 8 are laid [54, -1, -1]». The two positions of one table are judged under two different answers to Q-5. That is page item 2, «The judgements go in one table, position by test, so that a fact counted against one and not the other can be seen», and page item 5, «To contradict itself or the instruction». **What it carries into round 5:** the owner may rule Q-6 B and otherwise take the recommendations. The paper tells him B meets 60, 8 and 68, so nothing would warn him, and round 5 would receive settings no data can meet. Only Q-6 B with Q-5 B is buildable: `R/R_toy.log` «Q-6 A with Q-5 B … children 60 entries 68 … learners 64 caught 4» shows that Q-5's own rival holds under Q-6 as recommended. Q-6 is the only question with this fault. Each other rival was read with every other recommendation, and none is unbuildable without the paper saying so. Q-14's rival against Q-13's setting is flagged in both sections.

**A fault the page lacks.** Part 1 of `_kinds/analysis.md` has no item for answers that depend on each other. Proposed wording, for the orchestrator to judge: *To judge the positions of one question under an answer to another question other than the one recommended, or under different answers for each position; or to declare a dependency between two answers in one direction only.*

Kinds: `item=1`.

## 8. Found, not fixed

1. **"Given to every position" is a selection, not "everything the sources fix".** The register is not cited in it at all. The summary rows G-02, G-04, G-08, G-09, G-12 and G-13 are not cited. `settings.csv` lines 9 to 13 and 15 to 18 are not cited. The ruled line `GAPS-PAPER.md:196` is quoted without «and no two different children share all three fields», which bears on Q-2's rival and on Q-14. No table was found to deny a rival anything these grant, and the paper had about 1.6 KB of room to cite them by range.
2. **Q-9's rival cell, "40 of 64", also rests on Q-2's order and Q-5's pairs, but the section names only Q-6.** Under the other five orders the figure is 40, 42, 43, 41 and 43 (`R/R_toy.log`). The figure holds with the recommendations, and the recommendation does not rest on it.
3. **Q-6's recommendation, «as line 19's "spread" reads», reads more into line 19 than it says.** `../brief/MINI-REGISTRY-BRIEF.md:19` says «invented children spread over three lists». Position B also has children on all three lists. Several rows labelled "(a)" apply line 19, line 26 or R-03, while the paper quotes line 7 as test (a).
4. **Q-11's and Q-13's dividing rows judge a route, not test (c) as quoted.** Under each rival the count still has a known answer: 60 = 52 + 8, and 64 derived. The recommendations stand on a stated convenience in any case.
5. **Q-13 says it depends on Q-8, but 64 also holds under Q-8's rival.** Under that rival the 4 still go uncaught.
6. **The report's section 5 says the edit at 15:28:09 came "before any check ran" and that "Every check ran after that edit".** By `W/record/runs.jsonl`, runs 1 (A1, 15:25:57) and 2 (A5, 15:26:41) ran before it. By `W/record/opened.jsonl` neither reads the paper. Every check that does read the paper, run 3 at 15:28:37 and A7 and A8 at 15:28:53, ran after the edit. No criterion turns on this.
7. **Q-9's rival may not be the strongest.** "Holds none" leaves 40 learners without the school R-03's record holds. A rival with a school on the census only, that still gives every learner one, was not weighed.
8. **The ledger's entries name the round's files under `~/IdeaProjects/mini-registry/…`, while the estate is at `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`.** `show` resolves both to `on disk`. The report records the same.
9. **The trace check over this review prints one finding, `input-changed`, at 15:40:54 UTC, and exits 1.** The finding concerns the report: it was `absent at issue` of C-2026-10-31-12, and its sha256 at this review's start, `84a719bda9ec…`, is the same as now. The review form explains this case: the report coming into being after the issue is not a change to it.
