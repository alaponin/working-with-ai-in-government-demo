---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOALQ_2026-10-31.md (C-2026-10-31-17, version 1)
written_by: a session that neither wrote nor carried out the instruction — MR · review · answers to the goal's questions (C-2026-10-31-18), started as a sub-agent with an empty memory
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` at 18:05:18 UTC, this session's first command
window: 2026-10-31 18:05:18 UTC (the started entry 20261031T180518Z_MR_started_C-2026-10-31-18.yaml) to 2026-10-31 18:17 UTC, no pause; closed at the moment of writing, this file's last write
verdict: accepted
downstream_artefact: the orchestrator's closed entry for C-2026-10-31-18, which closes C-2026-10-31-17 with it
---

# REVIEW — the paper answering the goal's 13 questions

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq-review/_evidence/` (below, `R/`). Evidence of the round: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/` (below, `W/`). The paper: `docs/GOAL-QUESTIONS-PAPER.md`, 19984 bytes, sha256 `9603caf1…5ef0cef`. The report was at its path when this review started and was read as it stands.

## 1. The tests of success, one by one

| Test | Met? | Evidence read or produced here |
|---|---|---|
| A1 — 13 questions, each at its line | met | `W/A1.log` `13` / `0 not found`. By another route, `R/R_paper.log` part 1: the numbered items after `GOAL.md:146` — `13 [1, …, 13]`. |
| A2 — 0 unanswered, 0 extra | met | `R/R_paper.log`: `in GOAL, not in the paper: []` · `in the paper, not in GOAL: []` · `questions quoted not word for word or at another line: 0`. |
| A3 — every passage at its line | met | `R/R_paper.log` part 2 prints each of the 27 quoted passages beside its whole source line, and the 13 quoted questions in part 1 — 40, the report's figure — with 11 ranges and 2 bare line references beside their first and last lines: `not holding: 0`. |
| A4 — 2, 1, 1 per section | met | `R/R_paper.log` part 3: Q-1 to Q-13 each `positions 2 tables 1 proposals 1`; 29 rows, 15 marked "both meet", 14 "divides". |
| A5 — 0 one-way; each position under the recommendations | met | `R/R_paper.log`: `declared pairs (B depends on A): 18` · `one-way between sections: 0` · table and sections agree both ways. Listed again from the words (`R/R_dependencies.txt`): every position is read under the recommendation of each question it rests on. Four bearings the paper does not declare and one rival's drawing are recorded in part 8; none changes a judgement. |
| A6 — 17 rows; R-17 on every screen | met | `R/R_paper.log` part 4: 17 goal headings, 17 rows, `missing: [] extra: []`; 5 screens, each `R-17 line: True`. Re-established by a walk of its own, part 2. |
| A7 — nothing widened | met | The report's A7 table read against the 13 proposals: none compares a fourth field or forgives anything but capitals (Q-4 compares spaces as entered), none reads the key table or the reset's record, none adds a goal or a look-up screen; Q-12 gives the clerk nothing to do (`GAPS-PAPER.md:281`). |
| A8 — under 20 KB; sources unchanged | met | `R/R_outputs.out`: `19984 …/GOAL-QUESTIONS-PAPER.md`. `R/R_sources.out`: each of the 14 files of `W/sha256_start.txt` hashed again here at 18:13:56Z, `same as at the round's start` 14 times; start and end lists `identical`. |
| A9 — placement and trace exit 0 | met | `W/A9_placement.log`, `W/A9_trace.log`; run again here, both `clean`, `EXIT=0` (part 6). |
| A10 — record check exits 0 | met | `W/record/check.out` `## Findings — 0`; run again here with its `# run with:` options, `EXIT=0` (part 6). The report could not quote its own run, which followed its last write; it says so. |
| A11 — started and finished beside issued | met | `R/R_ledger_show.out`: `issued` 17:43:55Z, `started` 17:54:34Z, `finished` 18:05:03Z, `EXIT=0`. |

## 2. One figure re-established

**The figure:** the number of screens the goal has once all 13 recommendations are applied — the paper's "Taken together", `GOAL-QUESTIONS-PAPER.md:315` «five, none added», with SC-4 renamed and F-6 and F-7 added.
**The paper's route:** a row per step, failure and screen of the goal, each saying what a recommendation changes in it.
**The route here:** `R/R_walk.txt` follows every path the goal and the 13 proposals open — each check of S-3 passed and failed, several faults at once, the three outcomes of the search, F-4 to F-7, and the way back from each result — to the view the clerk is left looking at, and counts each distinct view once, under the ruling on G-09 (`GAPS-PAPER.md:308` «every view the clerk can see, messages and refusals included, is a screen»).

```
distinct views: SC-1, SC-2, SC-3, SC-4, SC-5  -> 5 screens
views reached with no screen to show them: 0  (F-1 and F-3, which GOAL.md:112 leaves without a view, now reach SC-4)
screens added by a proposal: 0 ; screens renamed: 1 (SC-4, "the date of birth refused" -> "the entry refused", Q-5)
failures added: 2 (F-6, Q-3; F-7, Q-12) ; steps added: 0
```

**The two agree:** five screens, none added, two failures, no step. The count holds SC-4 as one screen whose lines vary with the faults found, as the goal and the paper both hold it.

The times the report gives in its own words were read at their sources. The window opens at the started entry, 17:54:34Z. It closes at the report's last write, 18:04:53, by `stat` (`R/R_outputs.out`), as `W/record/window.out` prints. The paper's last write is 18:02:31, by `stat`. `RECORD.txt` lists 11 runs. Runs 5 (18:02:11) and 10 (18:02:48) are A5, as the report says. Every log the report quotes for A2 to A6 comes from runs 7 to 11, all after the paper's last write. The `finished` entry, 18:05:03Z, follows the report's last write and `check.out` (18:04:54).

## 3. The outputs exist

`R/R_outputs.out`, 18:13:36 UTC: `docs/GOAL-QUESTIONS-PAPER.md` is 19984 bytes, sha256 `9603caf1d95b8f89927a35969e33947da9e93776e04f98ccd27a3a7965ef0cef`, as declared. The evidence folder holds 18 entries. The report is 11994 bytes. All three outputs are at their paths.

## 4. The running application

Not applicable: the round wrote a paper, not an application model.

## 5. What a review of this kind runs (`_kinds/analysis.md`, part 2)

- **Every citation, read at its source against the sentence that cites it.** `R/R_paper.log` prints all 40 quoted citations beside their whole source lines, and each range's first and last line. Each one says what the sentence citing it says:
  - `REQUIREMENTS.md:30-106` runs from `### R-02` to R-07's last test line, and `216-292` from `### R-16` to R-21's.
  - `GOAL.md:15-62`, `68-106` and `112-142` are the goal's steps, failures and screens.
  - `REQUIREMENTS.md:184` is R-13's set-up «before any enrolment», which is the ground Q-2 A gives for holding 6 to 12 to the data.
  - `GAPS-PAPER.md:398` is the ruled G-12 recommendation, cited for F-1's check.
  - `QUESTIONS-PAPER.md:38` is the ruled date, 2026-10-31, used by Q-2 B.
  - No citation rests on a shared word.
- **The set, listed again and compared both ways.** The goal has 13 questions and the paper 13 sections: 0 missed, 0 extra, 0 off their line (A1, A2). The goal has 17 steps, failures and screens, and "Taken together" has 17 rows: 0 missing, 0 extra (A6).
- **The dependencies, listed again.** `R/R_dependencies.txt` lists the pairs from the words of every position and proposal, not from the paper's table. It finds all 18 of the paper's pairs, each declared in both sections, and every position read under the recommendation it rests on. It also finds four bearings the paper does not declare: 8←4, 9←4, 2←7 and 8←13. Under the recommended answers, none changes any position's judgement (part 8, item 1).
- **Each table read against "Given to every position" and the other position's cells.** No table credits one position with a setting, count or screen open to all (page item 6). Every recommendation, taken with the other twelve, builds without contradiction:
  - all checks run before the search;
  - every fault is named on SC-4, and the entries are kept;
  - F-6 is shown on SC-5;
  - SC-2 shows the number and the four fields;
  - F-7 is named;
  - every result screen leads back to SC-1;
  - the search compares the three fields and forgives capitals only.
  Three rival cells are weaker than the sources make them (part 8, items 2 to 4). Each is a rival denied something, and none carries a fault into round 6's build under the recommendation.
- **One figure, worked out again by another route.** Part 2.

Part 1 of the page, read against the paper:
- Items 1, 3, 4, 6 and 7 are not shown. Every proposal is marked as one, and every governing passage is quoted.
- Item 2 shows in the three rival cells of part 8. None reaches a gap, by the test this review was given.
- Item 5 is not shown. F-7 stands "at S-4" in its section, line 259, and on the S-5 row of "Taken together", line 299. That reads as the goal's own F-5 pattern, a failure met at S-4 that goes on to the next step, not as a contradiction.

## 6. The four mechanical checks, run here

Run directly, outside `round_record.py run`, by `R/r_mechanical.sh`, at 18:13:35–36 UTC:

| Check | Command (abridged) | Exit | Log |
|---|---|---|---|
| trace | `trace_check.py --constants …/mini-registry/CONSTANTS.md --coordination …/_coordination/CONSTANTS.md …/REPORT_GOALQ_2026-10-31.md` | 0 | `R/R_trace.out` |
| placement | `placement_check.py --constants …/mini-registry/CONSTANTS.md …/PROMPT_GOALQ_2026-10-31.md` | 0 | `R/R_placement.out` |
| record | `round_record.py check --record W/record --report …/REPORT_GOALQ_2026-10-31.md --tolerance 2 --out R/R_record_check.out` (the options of `W/record/check.out`'s `# run with:`) | 0 | `R/R_record_check.log` |
| ledger show | `ledger.py show --constants …/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-17` | 0 | `R/R_ledger_show.out` |
| ledger check | `ledger.py check --constants …/_coordination/CONSTANTS.md` | 0 | `R/R_ledger_check.out` |

The lines that decide:

```
inputs: 8 of 8 pinned by 20261031T174355Z_MR_issued_C-2026-10-31-17.yaml hash the same now
trace check: clean
placement check: clean
## Findings — 0
check: clean
```

The record check lists this review's own files as `added after the window closed …, by another hand or later`, as it should. `ledger.py check` prints no line naming `MR`; its whole output is `check: clean`.

**The account on the three entries**, as `show` prints them: the `issued`, the `started` and the `finished` each read `account: arne.laponin@gmail.com`. That is the address in the report's declaration, so they agree. The `started` entry reads `started_by: unknown`, as the report declares.

## 7. The verdict: accepted

Every criterion A1 to A11 is met on evidence read or produced here.
- Every citation holds at its source and says what the sentence citing it says.
- The 13 questions, the 17 rows and the 18 declared dependencies agree with this review's own listings both ways.
- With all 13 proposals applied, the goal has five screens. A walk by another route gives the same count, and every screen carries R-17's line.
- No proposal widens the search, reads the key table or the reset's record, or adds a goal.
- The 13 proposals hold together. Taken with every other recommendation, no rival hands round 6 a contradiction the paper hides.
- The four mechanical checks are clean, and the sources are unchanged.

The faults found are in how three rivals are drawn or judged, and in four bearings the paper does not declare. Under the definition this review was given, none is a fault that a ruling on the paper would carry into round 6's build. They stand under part 8.

No gap is named. The page of the kind needs no new fault from this review. Part 8, item 1, notes that the fault the second questions review proposed for the page is not on it yet.

The orchestrator writes one `closed` entry with the outcome `accepted`, which closes C-2026-10-31-17 with it. The items under "found, not fixed" become candidate instructions.

## 8. Found, not fixed

1. **Four bearings are not declared** (`R/R_dependencies.txt`). None changes a judgement under the recommended answers.
   - **8←4 and 9←4.** Q-4 A (line 106) sends a name of spaces to F-1 on SC-4. The table's own ground for 8←1, 3, 5, 6, 7 is line 31: «SC-4 and SC-5 name the faults these send to them».
   - **2←7.** Q-2 B (line 69), «on SC-4 before the search», is Q-7 A's order. Because it does not write "Q-7", the round's A5 program, which looks for `Q-<n>`, cannot see it.
   - **8←13.** Q-8 A's «The entries are kept on SC-1» holds only where the clerk comes back to SC-1. The paper's own line 284 shows this.

   The report says it could not establish the set's completeness (its part 4), and these four are the reason. The second questions review proposed adding a fault to the page for "pairs listed from the paper's own judgement" (`REVIEW_QUESTIONS_2026-10-31_v2.md`, section 7). `_kinds/analysis.md` does not yet carry it, and the cause here is the same.
2. **Q-13's rival is not drawn at its strongest.** Line 280 reads «No way back; the clerk opens SC-1 again at S-1, empty». "Empty" is Q-8 B's own words (line 185, «SC-1 opens empty»). Line 284, «Q-8: entries kept | met | lost | divides», then counts that against B.
   - Under Q-8 A, a reopened SC-1 can hold the kept entries. Drawn so, Q-13's table has no dividing row. Section 3 of the instruction asks that such a case be said: «Where any answer within the sources serves equally, say so».
   - The recommendation builds and agrees with Q-8 A.
   - A ruling of B as drawn would sit against Q-8 A, and line 284 shows that conflict. It is not hidden.
3. **Q-6's rival is denied two things its own words give it.**
   - Line 151 reads «F-3 has no view». But under B such a school «is searched for and saved» (line 146), so the clerk sees SC-2 or SC-3.
   - Line 152 reads «none can be written». But the ruled G-12 (`GAPS-PAPER.md:398`, given to every position) asks for a check for each way the goal goes wrong, and B's outcome can be checked.
   - The recommendation stands on row (a), line 150, alone.
4. **Q-7's table has no row for the words on which its rival is strongest.**
   - The words are the brief's «searches for the child first» (line 11), R-04's requirement «before it does anything else with the entry» (`REQUIREMENTS.md:62`), and `groundwork/search_rule.csv:11` «first: before the registry does anything else with the entry».
   - All three are in the quoted question, line 156. Position A says how it reads them (line 164, «"First" is read as R-04's test reads it»).
   - The table tests only R-04's test line, where both meet, and a build-cost row.
   - Under A, the check that the school is one of the data's 3 runs before the search. If round 6 reads the three schools from the data rather than from a setting, that check is a read of the data before the search, against R-04's «See» line (`REQUIREMENTS.md:67`), though not against its «Pass if». Neither the paper nor the groundwork says where the three names are held.
5. **The same test is measured two ways.** Q-2's row (a), line 73, counts «a refusal the brief does not name» against B. Q-1's row (a), line 53, does not count that against A, although no source names a refusal of a date in the right form that names no day either (`settings.csv:17` refuses "any other form").
6. **G-06 is left out of the list of first-ruling rows that bear on the goal**, at line 12. It bears on Q-2. Its content reaches every position through `settings.csv:15-16`, inside the range given whole at line 11.
7. **The ledger's entries name the estate under `~/IdeaProjects/mini-registry/`**, while it is at `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`. `show` resolves the instruction to `on disk`. This is the report's own item, and it stands from the earlier reviews.
