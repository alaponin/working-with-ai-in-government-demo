---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md (C-2026-10-31-03)
written_by: a session that neither wrote nor carried out the instruction — a sub-agent with a fresh context, started by the working session (MR · review · answers to the register's gaps, C-2026-10-31-04)
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, this review's first command, at 2026-10-31 13:34:56 UTC
window: 2026-10-31 13:34:56 UTC to 2026-10-31 13:41:48 UTC — opened at the first command (`date -u; hostname`), no pause, closed at this line's own write, the review's last; the command kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-review/_evidence/window.out
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md (version 2), to which the orchestrator appends the gaps below; the record is not cut over, so the act is made on the hand rows of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md
---

# REVIEW — the decision paper on the register's open questions G-01 to G-13

Evidence folder, cited below as `<ev>`: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-review/_evidence/`. The paper is `docs/GAPS-PAPER.md` (34390 bytes, sha256 `d52fd3fc…11bb`), cited as `paper:<line>`.

## 1. The tests of success, one by one

All nine are met on evidence read here. The verdict turns on part 5, which A1 to A9 do not test.

| Test | Met | Evidence read by the reviewer |
|---|---|---|
| A1 | yes | `<ev>E1_questions.log`: 14 question lines in the register's section, 13 open once G-14 is set aside; `QUESTIONS.md`'s ids `diff` against the reviewer's list, exit 0; the round's `A1_questions.log` prints `13` and `0 not found` |
| A2 | yes | `<ev>E1_questions.log`: `comm` both ways between the register's 13 and the paper's `## G-` sections and summary rows, `0`, `0`, `0`, `0`; the 13 questions as the paper quotes them `diff` the register's lines, exit 0, 0 lines differ |
| A3 | yes | `<ev>E2_citations.log`: `passages 49: at the named line 49, elsewhere 0, nowhere 0`, by the reviewer's own scan |
| A4 | yes | `<ev>E6_positions.log`, by `awk`: every section reads 2 or 3 positions, 4 rows (a) to (d), 1 recommendation, each row with one cell per position; 13 lines "We recommend"; decision wording 0 |
| A5 | yes | `paper:18` closes G-14 quoting `../brief/MINI-REGISTRY-BRIEF.md:13` «(capitals ignored)». Read: no recommendation matches on anything but the three fields with capitals ignored; G-05 keeps the record of sameness out of the search. `<ev>E4_figures.log` runs the recommendations of G-03, G-04 and G-05 together and the rule catches `4` of the 8, not 8 |
| A6 | yes | `<ev>E3_checksums.log`: `ec6971e7…1f64` and `ad583b39…f103`, the declaration's two |
| A7 | yes | `<ev>M2_placement_check.log` `placement check: clean`, exit 0; `<ev>M1_trace_check.log` `trace check: clean`, exit 0 |
| A8 | yes | `<ev>M3_record_check.log`: `## Findings — 0`, exit 0; the round's own `record/check.out` also reads `Findings — 0` |
| A9 | yes | `WHAT_IS_RUNNING.md`, Closed table: the row `MR · work · answers to the register's gaps` started 13:26 UTC, closed 13:34 UTC |

## 2. One figure re-established

- **The number of open questions.** The round's route: `list_questions.py`, a Python regex over the lines after the heading. Here: `sed` from the heading to the end of the file, `grep -E` on the list marker, `wc -l`, then `comm` against the paper's headings and summary rows (`<ev>E1_questions.log`, 13:37:40 UTC). Both give **13** (14 in the section, G-14 set aside). They agree.
- **The paper's 64, 68 and "4 of the 8".** The paper reaches them by reasoning (`paper:38`, `paper:115`, `paper:138`). Here they come from a run of a toy data set built to the brief's numbers and the settings of G-04 and G-05, with every entry enrolled through line 13's rule (`<ev>e4_figures.py`, `<ev>E4_figures.log`, 13:39:22 UTC). It printed `entries: 68`, `children (distinct keys): 60`, `learners after reset: 64` and `of the 8 on two lists, held as one learner (caught): 4`. They agree.
- **The report's times.** The window close, 13:34:31 UTC, matches `record/window.out` (`close read: 2026-10-31 13:34:31 UTC`) and the report's mtime of 15:34:31 local (`<ev>E3_outputs.log`). The record check ran at `13:34:31.537Z` (`record/check.out`, line 1), after the close. Row closed 13:34 UTC.

## 3. The outputs exist

`<ev>E3_outputs.log`, 13:39:02 UTC, one command (`ls -ld` and `shasum`), exit 0:

- `docs/GAPS-PAPER.md`: 34390 bytes, `d52fd3fc…11bb`, as declared.
- `_working/round-01b-gaps/_evidence/`: a folder, 21 files. `record/RECORD.txt` is 7402 bytes and found.
- `_reports/REPORT_GAPS_2026-10-31.md`: 15301 bytes, `0bfa5400…4c73`, the size and checksum in `record/window.out`.

## 4. The running application

Not applicable. The round wrote no application model; it wrote a decision paper.

## 5. What a review of this kind runs (`_kinds/analysis.md`, part 2)

- **Every citation read at its source.** `<ev>E2_citations.log`, section 1: all 49 quoted passages are at their lines. Each was read against the sentence that cites it, and each bears as cited. Section 2 of the same log puts all 38 bare "line N" references beside the brief's line N; each names the content the sentence gives it. **But the register is barely cited.** Section 3 lists, for each question, the register line outside the gaps section that names it ("gap G-xx"). In **11 of 13** sections the paper quotes no register passage at all, and it never states that none bears. Three judgements rest on a register test that is restated and not quoted (G1).
- **The set listed again and compared both ways.** 13 against 13: `0` either way, for sections and for summary rows (§2).
- **The tables, read test by test.** Every fact a judgement rests on was looked up in the other positions' cells. Most tables hold. Two do not: in G-01 a fact the paper grants elsewhere is denied to one position (G2); in G-02 a setting open to both positions is credited to one (G3). Lesser cases are listed in §8.
- **One figure worked out again.** See §2.
- **The three failures of the instruction's section 7.**
  - *Search widened by the back door:* none. G-02 B enters nothing new, G-03 B enrols by line 13 alone, and G-05 A's key table is read by the counts only. Round 7's answer is 4, not 8 by construction (`<ev>E4_figures.log`).
  - *Growing the prototype:* each addition is marked in its row (a): G-03 B "the reset gains one act", G-08 B and G-11 B fail (a) as stated.
  - *The thin second position:* G-06 and G-10 say where only one reading is open. G-01 C and G-02 A are weakened by the cells named in G2 and G3.
- **The faults of part 1.** Item 1: G1. Item 2: G2 and G3. Item 3: none, the set was listed first. Item 4: none of the 49 passages is miscited. Item 5: G2, where the paper's G-10 contradicts its G-01 cell, and G3, where its G-09 rule makes G-02 B's refusal a screen.

## 6. The four mechanical checks

| Check | Command (full paths in the log) | Exit | Log | Decisive line |
|---|---|---|---|---|
| trace | `/usr/bin/python3 trace_check.py --constants … --coordination … REPORT_GAPS_2026-10-31.md` | 0 | `<ev>M1_trace_check.log` | `outputs: 3 of 3 named exist` · `trace check: clean` |
| placement | `/usr/bin/python3 placement_check.py --constants … PROMPT_GAPS_2026-10-31.md` | 0 | `<ev>M2_placement_check.log` | `placement check: clean` |
| record | `/usr/bin/python3 -B round_record.py check --record …/round-01b-gaps/_evidence/record --report … --tolerance 2 --out <ev>M3_record_check.out` (the options of the round's `# run with:` line, `--out` changed) | 0 | `<ev>M3_record_check.log`, `<ev>M3_record_check.out` | `## Findings — 0` |
| ledger | `/usr/bin/python3 ledger.py check --constants …/_coordination/CONSTANTS.md` | 1 | `<ev>M4_ledger_check.log` | `not-cut-over: MR — the taken-up entry names …/WHAT_IS_RUNNING.md, which carries no markers` · `check: 1 defect` |

The record is not cut over, so `show` has nothing to print. The ledger's one defect is that declared state, not a fault of the round. In place of the entries, the working session's hand row was judged: taken up at 13:26 UTC and closed into the Closed table at 13:34 UTC, with the round's result and `Moved: nothing`. It agrees with the report's declaration of account `arne.laponin@gmail.com` and computer `MacBookPro`; the row names no account.

## 7. The verdict: not accepted

**Gaps: 3.** By kind: `item=1 · other=2`.

None of the three fails a test of success A1 to A9. Each fails the task of the instruction's section 3, which the tests do not reach (see §8, item 1). The verdict does not say that any recommendation is wrong. It says the paper does not yet show every position at its strongest, from every passage that bears on it.

- **G1 (item)** — **register passages that bear on a question are left unquoted, and register tests are restated instead of quoted.** The instruction asks, for each question, for "every passage of the brief or the register that bears on it, quoted with its path and line — or the statement that none does" (`_prompts/PROMPT_GAPS_2026-10-31.md:62`). Each register test that names a gap bears on it by construction: `docs/REQUIREMENTS.md` lines 40, 53, 80, 91, 133, 159, 185, 227, 238, 264, 305 and 319 (`<ev>E2_citations.log`, section 3). Yet 11 of the 13 sections quote no register line, and none says that none bears. Where a judgement rests on a register test, the paper paraphrases it:
  - `paper:276` "That is R-16's test as written" and `paper:288` "the only position that R-16's test can pass or fail by a program". The R-16 test, `docs/REQUIREMENTS.md:225` to `:227`, names no program.
  - `paper:298` "R-19's list of bodies is empty, and its test says so", against `docs/REQUIREMENTS.md:264` to `:266`.
  - `paper:328`/`:329`, the register's tests "carry" the must-not sentences and the known numbers.

  This breaks `_kinds/analysis.md`, part 1, item 1: "Where the paper rests on a law, a strategy or the instruction, it quotes the passage and says where it is."

- **G2 (other: a position judged on a fact the paper grants elsewhere)** — **G-01, Position C.** Its cells hold random numbers against the brief's line 29:
  - (c), `paper:63`: "numbers differ after every reset, against line 29";
  - (d), `paper:64`: "round 5's data cannot be compared reset to reset (R-15)".

  The ground then rests on that: A is "the only one of the three that is both silent about the child and the same after every reset" (`paper:67`). Yet in G-10 the paper itself proposes a generator with "a fixed seed" and says "the same seed gives line 29's same data" (`paper:276`, `paper:285`). At its strongest, an opaque number drawn from a seeded generator is the same after every reset, so C meets (c) and (d) as A does. A may still be the better answer on (a). As written, its ground rests on a cell that holds only against C's weakest form. This breaks `_kinds/analysis.md`, part 1, item 2 ("Each position is stated at its strongest") and item 5 ("To contradict itself").

- **G3 (other: a setting open to every position credited to one)** — **G-02, Position A against Position B.**
  - *The data setting.* B is defined as two things: the made-up data holds no two children sharing all three fields, and a refusal if the case still arises (`paper:83`). The first is a setting of the data (G-05's third setting, `paper:169`), open to A as much as to B. Yet A's (c) reads "no known answer unless G-03 and G-05 fix it" (`paper:89`) and B's reads "learners sharing all three: 0, after every reset". Under the same setting, A's case also arises 0 times. A's (d), "round 7 must decide whether 'more than one' counts as caught" (`paper:90`), then never arises either.
  - *The added screen.* Row (a) counts against A that it "adds an outcome and a screen" (`paper:87`). B's refusal, "the entry cannot be completed" (`paper:83`), is also a third thing the clerk sees. By the paper's own G-09 recommendation ("every refusal or message are screens", `paper:250`) it is a screen too. The ground "line 15 knows two outcomes; B keeps to both" (`paper:93`) holds of B no more than of A.

  The only real difference between the positions, refusing or showing every learner found, is not judged on its own. This breaks `_kinds/analysis.md`, part 1, item 2: "so that a fact counted against one and not the other can be seen". **It also shows a fault the page lacks:** positions that differ on more than the question asks, so that a setting any of them could take is credited to one alone.

## 8. Found, not fixed

1. **The tests of success do not reach the task's passages clause.** A3 tests only the passages quoted, so G1 passed all nine tests. A test counting the register lines that name each question against what the paper quotes, as `<ev>E2_citations.log` section 3 does, would catch it.
2. **G-04 has a lesser case of G3.** A's (c) is given the two-lists setting ("68 if each is on exactly two lists", `paper:138`). B's (c) reads "the number of children is then not given", though the same setting gives 52. B's (d) reads "round 5 must work out how many children to make" (`paper:139`), while A must equally fix 68 entries. Not counted as a gap, because the ground rests on line 25, which stands.
3. **G-09, Position B, is read as a separate dialog.** B is "a message shown in a box of its own is part of the page beneath it" (`paper:252`). Its cells read it as a box "without the words" (`paper:257`) and "the hardest thing for a windowless check to read" (`paper:259`). The ground, line 33's "every screen", does not depend on them.
4. **G-12, A (b), names too few must-not tests.** It names R-17, R-18, R-20 and R-21 as carrying the must-not sentences (`paper:328`). The register's section "What it must not do" holds R-16 to R-21 (`docs/REQUIREMENTS.md:214` to `:292`).
5. **G-05's capitals-only setting meets R-12's letter-for-letter test.** G-05 proposes that some of the 8 differ "in capitals only" (`paper:169`). R-12's test compares family names "letter for letter" (`docs/REQUIREMENTS.md:172`). Unless round 2 makes that comparison ignore capitals, R-12 counts those children among the "spelt differently", above 4.
6. **`round_record.py check` misdescribes the hand row.** It reports the change to `WHAT_IS_RUNNING.md` as "changed after the end list, by the ledger's own entries" (`<ev>M3_record_check.out`). With the record not cut over, that write was the hand row. The wording is the kit's, not the round's.
7. **The reviewer's evidence shows up in the round's record check.** It sits under the estate's root, so the check lists it as "added after the window closed, by another hand or later". That is expected, not a finding against the round.
8. **This review is a sub-agent.** Its effort is `unknown`: the prompt shows none. It runs on an Opus model, the band named.
