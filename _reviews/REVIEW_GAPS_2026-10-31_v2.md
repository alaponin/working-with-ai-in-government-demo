---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31_v2.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md (C-2026-10-31-03, version 2)
written_by: a session that neither wrote nor carried out the instruction. It is a sub-agent with a fresh context and an empty memory, started by the working session (MR · review · answers to the register's gaps, C-2026-10-31-04, version 2)
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, this review's first command, at 2026-10-31 14:01:12 UTC
window: 2026-10-31 14:01:12 UTC to 2026-10-31 14:09:16 UTC — opened at the first command (`date -u; hostname`), with no pause, and closed at this line's own write, the review's last; read by `date -u` in the command kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2-review/_evidence/window.out
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md, or its re-scoping (procedure 6.4: this is the second round). The record is not cut over, so the act is made on the hand rows of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md
---

# REVIEW, edition 2: the decision paper on the register's open questions G-01 to G-13, second attempt

`<ev>` below means `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2-review/_evidence/`. The paper is `docs/GAPS-PAPER.md` (47002 bytes, sha256 `d03db64c…bb`), cited as `paper:<line>`, and the register is cited as `register:<line>`. The first edition, `_reviews/REVIEW_GAPS_2026-10-31.md`, is left as it was written.

## 1. The tests of success, one by one

| Test | Met | Evidence the reviewer read |
|---|---|---|
| A1 | yes | `<ev>E1_E4_questions_figures.log`: 14 question lines in the closing section and 13 open. Each question as the paper quotes it matches the register's line: `questions quoted differently: 0`. The round's `A1_questions.log` gives `13` and `0 not found` |
| A2 | yes | same log: `join` both ways between the register's 13 and the paper's sections and summary rows gives `0`, `0`, `0`, `0` |
| A3 | yes | `<ev>E2_citations.log` §1, the reviewer's own scan: `passages 85: at the named line 85, elsewhere 0, nowhere 0`. §4 places each of the 54 bare "line N" mentions beside the brief's line N. Each one was read and names what the sentence gives it |
| A4 | yes | `<ev>E6_positions_r12.log`: G-01, G-03 and G-05 have `3 4 1`, the other ten `2 4 1`. Every row has one cell per position. Decision wording: `0` |
| A5 | yes | `paper:20` closes G-14 by quoting line 13, «(capitals ignored)». No recommendation matches on anything but the three fields with capitals ignored (§5) |
| A6 | yes | `<ev>E3_E8_outputs.log`: `ec6971e7…1f64` and `ad583b39…f103`, the two checksums the declaration gives |
| A7 | yes | `<ev>M2_placement_check.log`: `placement check: clean`, exit 0. `<ev>M1_trace_check.log`: `trace check: clean`, exit 0 |
| A8 | yes | `<ev>M3_record_check.log`: `## Findings — 0`, exit 0 |
| A9 | yes | `WHAT_IS_RUNNING.md`, Closed table: the row `MR · work · answers to the register's gaps` (version 2) was taken up at 13:48 UTC and closed at 14:00 UTC |
| A10 | yes | `<ev>E2_citations.log` §3: `gap-line pairs 13; unquoted 0`. §2: every "register line N" a section names is quoted in that section, `unquoted register lines named: 0` |
| A11 | **no** | The report states that "no setting, count or screen is credited to one position while it is open to another" (report line 65). That is not so for G-10, and in G-01 a cell is still contradicted by the paper's own G-10 (G1, G2). The report's own count of the G3 cells disagrees with its table (G3) |
| A12 | **in part** | Rows G1, G3, item 2, item 4 and item 5 are closed (§5). Row G2 says the rule was "applied to all", but two sections still hold cells that the paper contradicts elsewhere (G1, G2) |

## 2. One figure re-established

- **The number of open questions.** The round's route was `list_questions.py`, a Python regex. The first edition used `sed`, `grep` and `comm`. This review used `awk` over the lines from the heading "Gaps against the brief" to the next heading, then `join` against the paper's `## G-` headings and its summary rows (`<ev>e1_run.sh`, `<ev>E1_E4_questions_figures.log`, 14:06:18 UTC). Both routes give **13**: 14 questions in the section, with G-14 set aside. They agree.
- **64, 68 and 4 of 8.** The round's route was the Python program `figures.py`. This review built a toy list of entries in `awk` to settings 1 to 4 (52 children on one list, 4 on two lists with the same fields, and 4 on two lists whose family names differ by one letter). It enrolled them by line 13's key with capitals ignored. The run gave `entries: 68`, `children: 60`, `learners after reset … 64`, `caught: 4` (same log). It also gave R-12, comparing letter for letter with capitals heeded: `4` (`<ev>E6_positions_r12.log`). Both routes agree.
- **The report's own counts.** "85 passages" and "13 pairs, 12 lines" agree with `<ev>E2_citations.log`. "79 cells in 13 sections" agrees with the round's `A11_A12_cells_diff.log`. "G2: 9 cells in 4 sections" agrees with the report's own A11 table. **"G3: 23 cells in 6 sections"** (report line 83) does not. The table names 17 position-and-test cells plus G-02's "all 8", which is **25 cells, in 7 sections** (`<ev>E3_E8_outputs.log`, E8 and E8b). See G3.
- **The window.** The report closes at 14:00:42 UTC. That matches `record/window.out`, the report's mtime of 16:00:42 local (`<ev>E3_E8_outputs.log`) and `check.out`, which ran at 14:00:43 UTC.

## 3. The outputs exist

`<ev>E3_E8_outputs.log`, 14:06:29 UTC, one command (`ls -ld`, `shasum`, `stat`), exit 0:
- `docs/GAPS-PAPER.md`: 47002 bytes, `d03db64c…bb`, as declared.
- `_working/round-01b-gaps-v2/_evidence/`: a folder of 26 files. `record/RECORD.txt` is 10782 bytes.
- `_reports/REPORT_GAPS_2026-10-31_v2.md`: 15695 bytes, `1f28ce55…498c`, the figures that `record/window.out` gives.

## 4. The running application

Not applicable. The round wrote a decision paper, not an application model.

## 5. What a review of this kind runs (`_kinds/analysis.md`, part 2)

- **Every citation read at its source.** All 85 passages are at their lines (`<ev>E2_citations.log` §1). Each was read against the sentence that cites it, and each bears as cited. The 54 bare brief-line mentions were read against the brief (§4).
- **The sets, listed again both ways.**
  - The questions: 13 against 13, with 0 missing either way (§2).
  - The register lines that name each gap: 13 pairs, all quoted in their sections (§3).
  - Every register line a cell relies on is quoted in its section (§2).
  - **The first edition's G1 is closed for every question.** The tests that `paper:276`, `:288`, `:298`, `:328` and `:329` once restated are now quoted: R-16 at `paper:320`–`321`, R-19 at `:348`–`349`, and the must-not section at `:378`.
- **Each table read test by test, with every fact looked up in the other positions' cells and in the other sections.** The reviewer's `grep` of the facts the cells turn on is `<ev>E7_cells_grep.log`. The findings:
  - **G-02:** closed. The data setting and the view are given to both positions (`paper:89`), and the rows judge only refusing against showing (`:97`–`100`).
  - **G-04 (first edition, item 2):** closed. B now has 52 children and 60 entries (`:157`, `:158`).
  - **G-12 (item 4):** closed. A (b) names R-16 to R-21 (`:394`), and `register:214` and `:294` are quoted.
  - **G-05 (item 5):** closed. The conflict is stated with `register:172` and `:79` quoted (`:179`), and settings 1 and 2 resolve it (`:181`, `:196`). The toy run gives R-12 = 4 with capitals heeded.
  - **G-01's Position C** is restated at its strongest (`:64`, `:70`). But two of its cells and the ground still say that C adds and builds a generator, which the paper grants elsewhere (G2).
  - **G-10:** one cell and the ground deny Position B a list that the register's own test makes under either position (G1).
  - G-03, G-06, G-07, G-08, G-09, G-11 and G-13 hold. Two lesser cases are listed in §8.
- **The three failures of the instruction's section 7.**
  - *The search widened by the back door:* none. G-02 enters nothing new under either position. G-03 B enrols the lists by line 13 alone (`:122`). G-05 A's key table is never opened by the enrolment, the search or the reset's enrolment (`:183`). Round 7's answer is 4, not 8 by construction (§2).
  - *Growing the prototype:* each addition is marked in its row (a): `:128`, `:276` and `:360`.
  - *The thin second position:* G-06 and G-10 say where only one reading is open (`:209`, `:323`). G-10's B is still judged in a weakened form (G1).
- **The faults of part 1 of the page.**
  - Item 1: none. The register is quoted throughout.
  - Item 2: G1.
  - Item 3: none.
  - Item 4: none.
  - Item 5: G1 and G2, where the paper's G-10 and G-12 contradict the cells. The report also contradicts itself (G3).
  - Item 6: G1, the generator and its seed credited to A.

## 6. The four mechanical checks

| Check | Command (full paths in the log) | Exit | Log | Lines that decide |
|---|---|---|---|---|
| trace | `/usr/bin/python3 trace_check.py --constants … --coordination … REPORT_GAPS_2026-10-31_v2.md` | 0 | `<ev>M1_trace_check.log` | `outputs: 3 of 3 named exist` · `trace check: clean` |
| placement | `/usr/bin/python3 placement_check.py --constants … PROMPT_GAPS_2026-10-31.md` | 0 | `<ev>M2_placement_check.log` | `placement check: clean` |
| record | `/usr/bin/python3 -B round_record.py check --record …/round-01b-gaps-v2/_evidence/record --report …_v2.md --tolerance 2 --out <ev>M3_record_check.out` (the options on the round's `# run with:` line, with `--out` changed) | 0 | `<ev>M3_record_check.log`, `<ev>M3_record_check.out` | `## Findings — 0` |
| ledger | `/usr/bin/python3 ledger.py check --constants …/_coordination/CONSTANTS.md` | 1 | `<ev>M4_ledger_check.log` | `not-cut-over: MR — the taken-up entry names …/WHAT_IS_RUNNING.md, which carries no markers` · `check: 1 defect` |

The record is not cut over, so `show` has nothing to print. The ledger's one defect is that declared state, not a fault of the round. In place of the entries, the working session's hand row was judged. It was taken up at 13:48 UTC and closed into the Closed table at 14:00 UTC, with the round's result and its `Moved` line. It names `MacBookPro`, as the report's declaration does. It names no account, and the declaration gives `arne.laponin@gmail.com`.

## 7. The verdict: not accepted

**Gaps: 3.** By kind: `item=2 · trace=1`.

This is the second verdict of not accepted on C-2026-10-31-03, and procedure 6.4 says what follows two such rounds. The verdict does not say that any of the thirteen recommendations is wrong. It says the paper does not yet state every position at its strongest, with no cell that the paper contradicts elsewhere, which is what version 2's G2 and G3 ask "for every question".

- **G1 (item): in G-10, Position B is denied the list that register test R-16 makes under either position, and A is credited with a generator and seed that both positions have.** The report states the rule closed for every question (A11, A12 row G2). It fails A11 and A12.
  - **The list.** Row (b) for B reads «register line 226's list is not made» (`paper:334`). The ground rests on it: «A makes that list by a record, and B makes none» (`paper:339`).
  - **Why that cell is wrong.** Register line 226 is the *Do* step of R-16's own test: `docs/REQUIREMENTS.md:226` «list every source from which the data is made: every file and program the reset reads.» That step runs whichever kind of evidence G-10 adopts, because the gap the register leaves open is only at `register:227`, «(what evidence shows this: gap G-10)». The paper itself grants the step elsewhere. G-12 gives every position «the checks written as programs by round 6» (`paper:385`), and recommends «the tests of R-01 to R-21 written as programs» (`paper:398`). So under either G-10 position, R-16's program makes the list of the reset's reads.
  - **What G-10's positions really differ on.** At its strongest, B is the maker's statement together with the list R-16's test makes. The two positions then differ only on what shows each listed source to be invented.
  - **The generator and its seed.** Row (d) credits A with «round 5 writes the generator and its fixed seed … the same seed gives line 29's same data» (`paper:336`). Yet B's own statement is made by «The person who wrote the generator and its name parts» (`paper:329`), and line 29 binds both positions.
  - **What this gap breaks.** `_kinds/analysis.md`, part 1: item 2 («Each position is stated at its strongest»), item 5 («To contradict itself») and item 6 («To credit one position with a setting, a count or a screen that any position could take»).
  - It is the fault of the first edition's G2 and G3, in a section that edition did not name.
- **G2 (item): in G-01, Position C is still said to add and build a generator that the paper provides elsewhere.** Version 2 restated C (`paper:64`). But three places still read as if C must bring its own generator:
  - row (a): «adds a seeded generator and a redraw» (`paper:68`);
  - row (d): «round 6 builds the generator and its redraw» (`paper:71`);
  - the ground: «A meets register line 93 by construction where C needs a generator and a redraw» (`paper:74`).

  Against them, the same section gives every position «wherever chance is used, it is drawn from a fixed seed (G-10)» (`paper:58`). G-10 says «round 5 writes the generator and its fixed seed, the seed G-01's Position C also draws on» (`paper:336`). The paper therefore names two rounds as the builder of one generator, and it counts against C a generator that G-10's recommendation builds anyway. The redraw remains C's own, so the ground can stand on the redraw alone. As written, it rests partly on a fact the paper contradicts. This fails A12, row G2, and breaks `_kinds/analysis.md`, part 1, item 5.
- **G3 (trace): the report's count of the cells changed under G3 does not agree with its own table.** Report line 83 reads «**G3:** 23 cells in 6 sections (G-02, G-03, G-04, G-05, G-07, G-09 as above, and G-10)». That list names seven sections, and the A11 table above it names 25 cells (`<ev>E3_E8_outputs.log`, E8b: `17` cells named, plus «all 8 cells» of G-02, over `7` rows). The hand row in `WHAT_IS_RUNNING.md` repeats «G3: 23 cells in 6 sections». A11 asks the report to name each cell changed under G3, so a total that does not hold at its source fails A11. It also breaks `_kinds/analysis.md`, part 1, item 5 («A figure given twice is the same both times»).

None of the three shows a fault that the analysis page lacks. Items 2, 5 and 6 already carry them.

## 8. Found, not fixed

1. **G-05, B (d), overstates B's cost.** It says that keeping the key out of the match «needs a rule that the search ignore a field it holds» (`paper:194`). Yet every position matches on the three fields alone (`paper:16`), and the paper's search already ignores one field it holds, the school (`paper:241`). The ground, that only A keeps the key out of everything the search reads (`paper:197`), still holds, so this is not counted as a gap.
2. **G-06's strongest Position B is set aside without being stated.** That form makes the dates of birth relative to the day of reset. The "Given" line (`paper:211`) rules it out by line 29, but R-15's test (`register:211`–`212`), the passage that decides the point, is not quoted in G-06.
3. **The report's declaration and the hand row disagree on who started the round.** The report's `started_by` says the session «was started by a scheduled task» (report line 8). The closed row says «taken up by the working session». The instruction forbids a scheduled task only for starting the review.
4. **`round_record.py check` misdescribes the hand row,** as «changed after the end list, by the ledger's own entries» (`<ev>M3_record_check.out`). The wording is the kit's, and it repeats the first edition's item 6.
5. **This review's evidence appears in the round's record check** as «added after the window closed, by another hand or later». It sits under the estate's root, so this is expected and not a finding against the round.
6. **The trace check compares no checksum of inputs** («the ledger holds no issued entry»), because the record is not cut over.
7. **This review ran as a sub-agent.** Its effort is `unknown`, because the prompt shows none. It runs on an Opus model, the band named.
