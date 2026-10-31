---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31_v2.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md (C-2026-10-31-11, version 2)
written_by: a session that neither wrote nor carried out the instruction — MR · review · answers to the groundwork's questions (C-2026-10-31-12, version 2), started as a sub-agent with an empty memory
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` at 15:59:16 UTC, this session's first command
window: 2026-10-31 15:59:24 UTC (the started entry 20261031T155924Z_MR_started_C-2026-10-31-12.yaml) to 2026-10-31 16:09 UTC, no pause; closed at the moment of writing, this file's last write
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md, with G1 appended
---

# REVIEW — the paper answering the groundwork's 14 questions, second attempt (edition 2)

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2-review/_evidence/` (below, `R/`). Evidence of the round: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/` (below, `W/`). The paper: `docs/QUESTIONS-PAPER.md`, 19962 bytes, sha256 `5146d23a…0cce0`.

## 1. The tests of success, one by one

| Test | Met? | Evidence read or produced here |
|---|---|---|
| A1 — 14 questions, each at its line | met | `W/A1_questions.log` `14` / `0 not found`. Here by another route, `R/R_paper.log`: the numbered items under "Gaps against the sources" — `numbered items: 14 [1, …, 14]`. |
| A2 — 0 unanswered, 0 extra | met | `R/R_paper.log`: `in the groundwork, not answered: 0` · `in the paper, not in the groundwork: 0` · `question quoted not word for word or at another line: 0`. |
| A3 — every passage at its line | met | `R/R_paper.log` prints each of 52 citations (33 quoted passages, 14 quoted questions, 5 ranges) beside its whole source line: `citations read: 52; not holding: 0`. |
| A4 — 2, 1, 1 per section | met | `R/R_paper.log`: every Q-1 to Q-14 `positions 2 tables 1 proposals 1`; `rows 23 both meet 14 divides 9`, as `W/A2_A3_A4_A12_A13_check.log`. One row's mark is questioned in part 8, item 2. |
| A5 — the toy run | met | `W/A5_taken_together.log`: 60, 3, 68 (24, 22, 22), 8, 4, ages 6 to 12, 64 learners, 4 caught. Re-established by another route, part 2. |
| A6 — what each recommendation touches | met | The report's A6 table read against the 14 proposals: none compares a fourth field, forgives anything but capitals, or gives the search the key table; Q-12's table is written by the reset and "the search never reads it" (paper line 235). |
| A7 — under 20 KB | met | `R/R_outputs.out`: `19962 …/docs/QUESTIONS-PAPER.md`. |
| A8 — sources unchanged | met | `R/R_outputs.out`: the seven checksums now equal `W/before.sha256` line for line (the only diff line is that file's own timestamp); the first three are section 2's. |
| A9 — placement and trace exit 0 | met | `W/A9_placement.out`, `W/A9_trace.out`; run again here, both `clean`, `EXIT=0` (part 6). |
| A10 — record check exits 0 | met | `W/record/check.out` `## Findings — 0`; run again here, `EXIT=0` (part 6). |
| A11 — started and finished beside issued | met | `R/R_ledger_show.out`: version 2 `issued` 15:44:08Z, `started` 15:47:05Z, `finished` 15:58:56Z. |
| A12 — every dependent pair declared in both sections | **not met for every question** | The 15 pairs of `W/DEPENDENCIES.csv` are each declared both ways (`R/R_paper.log`: `pairs declared: 15; one-way: 0`). But the set was listed from the paper's own judgement, so a pair declared in neither section cannot show as one-way: Q-8 and Q-10 bear on each other and are declared in neither (G1). |
| A13 — each rival with every other recommendation; tables agree | **not met** | `W/A13_rivals.log` and `R/R_toy.log` agree on 13 rivals. They disagree on Q-10's: the round's program never reads the ruled settings rows 10 to 13 or Q-8 A's words; read literally on the lists, Q-10's rival cannot be built beside Q-8 as recommended. The paper's Q-10 table says it can (G1). |
| A14 — the first review answered item by item | met | The report's A14 table has rows for G1 and items 1, 2, 3 and 7; each line it names was read in the paper (`W/A14_lines.log`, and the paper itself: lines 10–12, 26 … 269, 125, 129, 131, 174, 180, 184). Whether G1 is closed is judged in part 7. |

## 2. One figure re-established

**The figure:** "Taken together": 60 children, 3 schools, 68 entries (24, 22, 22), 8 on more than one list, 4 spelt differently, ages 6 to 12, 64 learners after reset (highest number 64), and 4 of the 8 caught.
**The round's route:** `W/toy.py together`, which draws names, dates and schools from `random.Random(20261031)` and lays the 8 from a `PAIRS_A` list.
**The route here:** `R/r_toy.py`, written from the paper's words, not from `toy.py`. It makes no random draw: names come by arithmetic from fixed parts, dates are spaced by arithmetic from Q-1's lower bound to its upper, the schools are laid by Q-7's counts, and the entries are numbered by a fixed permutation. Q-5's pairs are taken from paper line 104 and the totals from line 123. The reset runs in Q-2's order and compares by `casefold`. It also reads, on the lists as made, the ruled settings rows 10 to 13 and Q-8 A's words. Log `R/R_toy.log`:

```
TOGETHER: the 14 recommendations
   can be met: yes
   children=60 schools=3 entries=68 per_list=[24, 22, 22] on_more_than_one=8 each_on_exactly_2=True spelt=4 capitals_only=0 ages=(6, 12) learners=64 highest=64 more_than_one=0 caught=4 key_rows=68 row12_other4_letter_for_letter=4 of 4 q8A_4_given_and_date_letter_for_letter=4 of 4 row13_sharing=0 per_school_from_lists=[20, 20, 20] …
```

**The two agree** on every number. The same run gives 64 learners and 4 caught for all six orders of the lists, entries read either way (Q-2). It gives Q-6 B with Q-5 B as buildable, and Q-14 B with one pair laid as `learners 63 against Q-13's 64`, which is the paper's figure.

The times the report gives in its own words were read at their sources. The window opens at the started entry, 15:47:05Z, and closes at the report's last write, 15:58:34 by `stat`, which is `W/record/window.out`. The runs are in `W/record/runs.jsonl`: 15:53:08, 15:53:08, 15:53:09, 15:56:19 and 15:56:19, five runs as `RECORD.txt` says. The paper was written at 15:56:19 by `stat` and `build_paper.log` at 15:56:18. A7 and A8 ran at 15:56:33 and A9 at 15:58:07. "33 quoted passages" matches this review's count, 33.

## 3. The outputs exist

`R/R_outputs.out`, 16:06:44 UTC: `docs/QUESTIONS-PAPER.md` is 19962 bytes, sha256 `5146d23a87cf9c0527c26c2965725bfa1125bd1a0a103ac83b68fb7dbd50cce0`, as declared. The evidence folder holds 23 entries. The report is 14445 bytes. All three outputs are at their paths.

## 4. The running application

Not applicable: the round wrote a paper, not an application model.

## 5. What a review of this kind runs (`_kinds/analysis.md`, part 2)

- **Every citation, read at its source against the sentence that cites it.** `R/R_paper.log` prints all 52 citations beside their source lines, and the prose references to a line beside their context. Each one says what the sentence citing it says. The range `docs/REQUIREMENTS.md:15-320` runs from `### R-01` to the last test line of R-23. `GAPS-PAPER.md:26-38` covers rows G-01 to G-13, and `settings.csv:2-18` covers every row. `GAPS-PAPER.md:196` is quoted whole: `quoted == source line 196: True`.
- **The set, listed again and compared both ways.** There are 14 questions in the groundwork and 14 in the paper, with 0 missed, 0 extra and 0 off their line (A1, A2). The set of dependent pairs was listed again here from the words of every proposal and of every ruled row the proposals touch. That listing finds the one pair the paper's table lacks, Q-8 and Q-10 (G1).
- **The tables, read against "Given to every position" and against the other position's cells.** No table denies a rival a fact the sources grant. One table credits a rival with a ruled setting it breaks: Q-10's rival breaks `settings.csv:12` on the lists (G1). Every figure a rival's cell gives was run in `R/R_toy.log`: Q-6's "54, −1, −1", Q-9's 40 and 36, and Q-14's 63.
- **One figure, worked out again by another route.** See part 2.

Part 1 of the page, read against the paper. Items 1, 4 and 6 are not shown. G1 shows items 3 and 7, and through them items 2 and 5.

## 6. The four mechanical checks, run here

Run directly, outside `round_record.py run`, by `R/r_mechanical.sh`, at 16:06:42–44 UTC:

| Check | Command (abridged) | Exit | Log |
|---|---|---|---|
| trace | `trace_check.py --constants …/mini-registry/CONSTANTS.md --coordination …/_coordination/CONSTANTS.md …/REPORT_QUESTIONS_2026-10-31_v2.md` | 0 | `R/R_trace.out` |
| placement | `placement_check.py --constants …/mini-registry/CONSTANTS.md …/PROMPT_QUESTIONS_2026-10-31.md` | 0 | `R/R_placement.out` |
| record | `round_record.py check --record W/record --report …_v2.md --tolerance 2 --out R/R_record_check.out`, the options `W/record/check.out` prints on `# run with:` | 0 | `R/R_record_check.log` |
| ledger show | `ledger.py show --constants …/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-11` | 0 | `R/R_ledger_show.out` |
| ledger check | `ledger.py check --constants …/_coordination/CONSTANTS.md` | 0 | `R/R_ledger_check.out` |

The lines that decide:

```
inputs: 6 of 6 pinned by 20261031T154408Z_MR_issued_C-2026-10-31-11.yaml hash the same now
trace check: clean
placement check: clean
## Findings — 0
check: clean
```

The record check lists this review's own files as `added after the window closed …, by another hand or later`, as it should. `ledger.py check` prints no line naming `MR`; its whole output is `check: clean`.

**The account on the three entries of version 2**, as `show` prints them: the `issued`, the `started` and the `finished` each read `account: arne.laponin@gmail.com`. The report's declaration names the same address, so they agree. The version 2 `started` entry reads `started_by: owner`, while the report declares `unknown`. The report records this itself (part 8, item 4).

## 7. The verdict: not accepted

**One gap, G1.** Every criterion A1 to A11 is met, every citation holds, the first review's items 1, 2, 3 and 7 are closed, and the recommendations taken together give the known numbers by a second route. Q-6's case is closed: its rival's row reads "no" and names Q-5's B, and the dependency is declared both ways. The version-2 section, however, asks for G1 to be closed "for every question, not for Q-6 alone", and that is not done. One other pair of questions has the same fault, so a ruling taken from the paper could still hand round 5 settings no data meets.

**G1 (item): Q-10's rival is credited with meeting every number beside Q-8 as recommended, which it cannot, and the dependency between Q-8 and Q-10 is declared in neither section.**

*What the instruction asks.* The version-2 section reads: «List every pair of questions where one answer bears on the other. Declare each dependency **in both sections**. Judge **both** positions of each question under the **recommended** answer of every question it depends on. Where a rival cannot be built alongside the other recommendations, its table says so in the row of the known numbers». The paper defines that row at line 14: «Every table's row "(c) known numbers" says whether the position can be built, with every other recommendation, to the brief's numbers, the settings and the other recommended values».

*What the paper says.*
- Q-8's Position A, `QUESTIONS-PAPER.md:159`: «the 4 differ in the family name only; their given names and date of birth match on both lists, letter for letter and in the same capitals.»
- Q-8's passage, `QUESTIONS-PAPER.md:157`, reads ruled row 14 as needing «the other 4 to match on all three fields». The ruled row it rests on is `docs/groundwork/settings.csv:12` «the_other_4_of_the_8,match letter for letter and in the same capitals».
- Q-10's Position B, `QUESTIONS-PAPER.md:199`: «each list its own form, turned into YYYY-MM-DD by the reset before the search.»
- Q-10's table, `QUESTIONS-PAPER.md:203`: «| (c) known numbers | yes | yes | both meet |». Lines 155 and 193 both read «**Depends on:** none. **Depended on by:** none.»

*Why the two cannot both hold.* If each list holds a date in its own form, no child on two lists has the same letters for its date of birth on both. That breaks Q-8 A's words for each of the 4, and ruled row 12, as Q-8 reads it, for each of the other 4. `R/R_toy.log` shows it:

```
Q-10 B each list its own form of date, turned by the reset
   can be met: no - ruled row 12: other 4 letter for letter 0 of 4; Q-8 A as worded: the 4's given names and date letter for letter 0 of 4
```

The search still catches 4, because the reset turns every date before it compares. The settings, though, are read on the lists, and that is where the paper's own row (c) reads them. The round's program says `can be met: yes` because it checks only the counts, `W/toy.py`, the `fails` list. It never reads rows 10 to 13 or Q-8 A's words. So A13's `0 disagreements` holds only against a check that cannot see this case. A12's `0 one-way` is likewise read over `W/DEPENDENCIES.csv`, a set listed from the paper's own judgement and not from the proposals' words. A pair declared in neither section therefore cannot show.

*Where it breaks the page.* Page item 7 reads «To judge the positions of one question under … another question's answer other than the one recommended … or to declare a dependency between two answers in one direction only». Here Q-10's rival is judged as if Q-8 A did not say "letter for letter". Page item 3 reads «To count over a set it has not listed»: the pairs were not listed from their source. Through those, item 2 applies, a fact counted for one position that the table does not show against it, and item 5 applies, the paper contradicting its own definition of row (c).

*What it carries into round 5.* The owner may rule Q-10's rival and otherwise take the recommendations. The paper tells him that rival meets every number and depends on nothing, so nothing warns him. Round 5 would then receive three forms of date on the lists together with "match on both lists, letter for letter" for the 4 and the ruled "letter for letter" for the other 4. No data meets those as worded. Either the rival needs Q-8 to say "match once turned", or its row reads "no" and names what it needs, as Q-6's now does.

*Checked here and found sound.* The other 13 rivals were built here by `R/r_toy.py`, each beside every other recommendation and read against rows 10 to 13 as well. For Q-1, 2, 3, 4, 5, 7, 8, 11, 12, 13 and 14 the result is `can be met: yes`, as the tables say. For Q-6 it is no, `[54, -1, -1]`. For Q-9 it is no: with the reset supplying schools in turn, the learners give `[32, 15, 11]` and 2 children have learners at two schools. Both agree with the tables. No other proposal's words were found to bear on another answer outside the 15 pairs.

**A fault the page lacks.** Item 7 names a dependency declared in one direction only, but not one declared in neither direction, and it does not say against what "can be built" is tested. Proposed wording, for the orchestrator to judge: *To test whether positions can be built together on the counts alone, leaving out the ruled settings and the words of the other recommendations; or to list the pairs of dependent answers from the paper's own judgement instead of from every proposal's words, so that a pair declared in neither section cannot be found.*

Kinds: `item=1`.

## 8. Found, not fixed

1. **Q-6's rival is not the strongest beside Q-5 as recommended.** Under Q-5 A, any spread in which the lists hold at least 6, 5 and 5 entries and sum to 68 meets every test. `R/R_toy.log` shows `28, 20, 20` and `58, 5, 5`, both `can be met: yes`. In that case the instruction asks for the rival "any other value", with a pick made for a stated convenience. The paper's line 131 instead offers 24, 22 and 22 as «the one of the two that can be built». The recommended value is buildable, so nothing is carried into round 5.
2. **Q-14's row (c), `QUESTIONS-PAPER.md:279`, is marked "divides" though both of its cells begin "yes".** The rival meets the row when it lays no pair, and what divides is what the rival permits. The instruction asks for a test that both positions meet to be marked so.
3. **Q-9's "no" rests, in the round's program, on reading a child's school from the lists only**, which under the rival holds by definition (`W/toy.py`, «children per school, read from the schools the lists carry»). This review reached "no" by its own route: a reset that supplies schools in turn, read from the learners, with 2 children at two schools. Neither program settles whether some other draw reaches 20 each. The paper's row (d) stands either way.
4. **The version 2 `started` entry reads `started_by: owner`; the report declares `unknown`.** The report states this under its corrections. The accounts on all three entries agree with the declaration.
5. **The ledger's entries name the round's files under `~/IdeaProjects/…`, while the estate is at `/Users/arnelaponin/Documents/Dev/wai-demo/`.** `show` resolves both to `on disk`. This is the first review's item 8, still standing.
6. **Stale paths in the instructions.** The working instruction's A9 and A10 commands, and its section 9's `--report`, still name version 1's paths, and the report reads them with version 2's. This review instruction's section 2 names `REPORT_QUESTIONS_2026-10-31.md`, its section 3 names the `round-02b-questions-review` evidence folder, and its section 4 `--report` names the first edition. This review followed the version-2 section and the declaration: it reviewed the `_v2` report, put its evidence in `round-02b-questions-v2-review`, and wrote this file.
