---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31_v2.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md (C-2026-10-31-13, version 2)
written_by: a session that neither wrote nor carried out the instruction. It is MR · review · the goal in full (C-2026-10-31-14, version 2), started as a sub-agent with an empty memory
started_by: sub-session. This session's prompt is the review's start message followed by the line that has it load its shell tool
account: arne.laponin@gmail.com. Read from the line of this session's own context that begins "The user's email address is"
model: claude-opus-5-5. Read from the line of this session's own context that names the model it is configured for. It is the band the review instruction names, Opus
computer: MacBookPro. Printed by `hostname` at 17:31:18 UTC, this session's first command
window: 2026-10-31 17:31:18 UTC (the started entry 20261031T173118Z_MR_started_C-2026-10-31-14.yaml) to 2026-10-31 17:39 UTC, no pause. It closes when this file is written
verdict: accepted
downstream_artefact: the orchestrator's closed entry for C-2026-10-31-14, which closes C-2026-10-31-13 with it (round 3 is no increment of a long delivery a record follows)
---

# REVIEW: the goal in full, enrol a learner (edition 2)

This review's evidence is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2-review/_evidence/`, written below as `R/`. The round's evidence is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/`, written below as `W/`. The report was at its path when this review started and was read as it stood. The goal read is `docs/GOAL.md`, 13891 bytes, sha256 `342515fd5ed96e45e23014568f67e8126edfeeccdb7f862dddd38e44acdb2aed` (`R/R_outputs.out`). None of the review's programs imports the round's.

## 1. The tests of success, one by one

| Test | Met? | Evidence read or produced here |
|---|---|---|
| A1: sets first, 0 missing and 0 extra | met | `W/A1_check.out`: `steps: 0 missing, 0 extra, 0 differing` and the same for failures. `W/record/runs.jsonl`: `inventory.py` ended 17:22:46.480Z; `W/record/window.out`: `STEPS_SET.md`/`FAILURES_SET.md` 17:22:46.47Z, `GOAL.md` 17:25:00.823Z. `inventory.py` now draws each member's sources from dispositions of 118 enumerated units, though the members' wordings are still typed (lines 22 to 37). The review's own listing of both sets is part 5. |
| A2: every source resolves | met | `W/A2_check.out` `0 without source, 0 unresolved`. Resolved again by `R/R_lookup.py`, ruled lines only: `members: 12 (steps 7, failures 5); tokens: 79; unresolved: 0` (`R/R_lookup.out`). 79 = the 52 + 27 of `W/A1_inventory.out`. |
| A3: every failure complete | met | `W/A3_check.out` `0 incomplete`. `R/R_lookup.out` lines 158 to 210 print all four fields of F-1 to F-5. Where a field is "not given", it names its gap. |
| A4: search step beside its rows | met | `W/A4_check.out` and report lines 66 to 86. `R/R_lookup.out` prints S-4 beside each of its 20 tokens. It compares rows 2 to 4 only, forgives by rows 5 and 6, and names rows 7 to 9 only to say "not compared" or "not read". `R/R_report_consistency.out` confirms which member cites each row (row 13 is cited by none). |
| A5: every screen carries R-17's line | met | `R/R_steps_screens.out`: `screens mentioned anywhere: 5`, `screens listed: 5`, `mentioned and not listed: []`, every listed screen `carries the line: True`. |
| A6: the gaps section | met | `R/R_outputs.out`: 13 gaps, each ending in `?`. No step, failure or screen answers one (read here; part 5). |
| A7: sources unchanged | met | `R/R_outputs.out`, 17:36:48Z: all eight checksums equal section 2 of the instruction. |
| A8: placement and trace, exit 0 | met | Both run again here (part 6), `clean`, `EXIT=0`. |
| A9: record check exits 0 | met | `W/record/check.out`, run 17:30:51.146Z, after the report's last write (17:30:50.910Z), shows `## Findings — 0`. It was run again here with `EXIT=0` (part 6). |
| A10: started and finished beside issued | met | `R/M4_ledger_show.out`: version 2 `issued` 17:13:18Z, `started` 17:16:20Z, `finished` 17:31:01Z. |
| A11: every fact beside its words, `0 unquoted` | met | `W/A11_quotes.out` `0 unquoted`. `R/R_lookup.py` reads each of the 111 quotations of `W/QUOTES.md` at the file and line it names: `not found at the line named: 0; on an unruled line of a paper: 0`. Whether each quotation carries its fact was judged here, field by field (part 5). One quotation is mispaired (part 8, item 1), and its field is still carried. |
| A12: no screen on an unsourced fact | met | Report lines 152 to 164, read against `R/R_lookup.out`. SC-1 to SC-3 rest on R-03, R-05 and R-07. SC-4 rests on the date refused, carried by G-07 «refused otherwise» (`GAPS-PAPER.md:254`) and settings row 17 «any other form refused», with G-09 making that refusal a screen. SC-5 rests on G-02 «refuse the entry» (`GAPS-PAPER.md:27`) and «says the entry cannot be completed» (`:102`). Version 1's SC-4 and SC-6 are gone. |
| A13: the first review answered item by item | met | Report lines 166 to 174 have one row each for G1 and items 1 to 4. Each was checked here; see part 5, "G1 and items 1 to 4". |

## 2. One figure re-established

**The figure** is the number of ways the goal can go wrong that the sources state or rule. The goal gives 5, F-1 to F-5.

**The round's route** was `inventory.py`. It enumerates every unit in scope (118) and gives each unit a hand-written disposition naming the members it carries. The first edition of this review used the same unit-by-unit route.

**The route taken here** starts from the words instead. `R/R_failures.py` collects every unit in scope:

- the brief's lines 5 to 40
- every line of R-01 to R-23
- the 13 summary rows and 13 recommendations of G
- the 14 proposals of Q
- every table row

That gives 247 units. It keeps only the units carrying a word that marks a departure from the plain path: refus, otherwise, not, never, no, none, cannot, more than one, differ, twice, only, missing, wrong, before, fail. That leaves 100 hits. Each hit is given, by hand in `R/R_failures_dispositions.py`, the failure it states or rules, or "none" with the reason. The program stops on a hit without a disposition. `R/R_failures.out`:

```
units in scope: 247; units carrying a marker: 100; every hit disposed: True
the figure, this route: 5 failures ['X-DATE', 'X-MANY', 'X-MISSED', 'X-MISSING', 'X-SCHOOL']
the goal: 5 failures ['F-1 An entry missing', 'F-2 The date of birth in the wrong form', 'F-3 A school not among the three', 'F-4 More than one learner found', 'F-5 The same child, not caught']
```

**The two agree: 5.** By this route, X-MISSING and X-SCHOOL rest on G-07 alone (`GAPS-PAPER.md:32`, `:254`). G-07 states a constraint, and a failure is its breach. That fits the goal's own account: F-1 says only that the search waits, and whether F-3 can arise at all is gap 6. Route-specific finding: X-MISSED is ruled most directly by Q-8's proposal «each of the 4 the rule misses is missed for its spelling alone» (`QUESTIONS-PAPER.md:168`). F-5 does not cite it, but it is carried by G-05 and settings row 14 instead.

**Times and counts the report gives in its own words, read at their source:**

- The window opens at the `started` entry (17:16:20Z, `R/M4_ledger_show.out`). It closes at the report's last write, 17:30:50 (`R/R_outputs.out` stat: 19:30:50+0200). The `finished` entry follows at 17:31:01Z.
- "14 runs traced": `W/record/runs.jsonl` has 14 lines.
- A7 "at 17:27:50": the first line of `W/A7_shasum.out`.
- "5 screens (v1 had 7) and 13 gaps (v1 had 11)": `R/R_steps_screens.out` gives `v1: … screens listed 7, gaps 11` and `v2: … screens listed 5, gaps 13`.
- "fields: 29": 7 × 2 + 5 × 3 = 29.
- "gap references: 8": 1 each in S-3, S-4 and F-1, 2 in F-2 and 3 in F-3, as counted in `W/QUOTES.md`.

## 3. The outputs exist

`R/R_outputs.out`, 17:36:48Z:

- `docs/GOAL.md` is 13891 bytes with sha256 `342515fd…`, as declared.
- `W/` holds 24 entries, `W/record/` holds 8.
- The report is 19177 bytes.

All three outputs are at their paths. Version 1's report is unchanged under its own name, and version 1 of the goal is kept as `W/GOAL_v1.md`.

## 4. The running application

Not applicable. The round wrote a document, not an application model.

## 5. What a review of this kind runs (`_kinds/drafting.md`, part 2)

- **Every claim looked up at its source.** `R/R_lookup.out` prints every field of S-1 to F-5 and, below it, the text each cited token resolves to. A `ruling:` token resolves at its ruled lines only. For each "registry does", "clerk sees" and "is saved" (7 + 5 + 5 = 17 fields), the source's words were read here against the fact the field states. A shared word was not accepted as a carrier:
  - **S-1 to S-7, "the registry":**
    - S-1 is carried by G-08 (`:281`, `:33`).
    - S-2 states no act. "after all four" is carried by G-07 (`:254`) and search_rule row 10.
    - S-3 is carried by G-07 «refused otherwise» and settings row 17. Its order against S-4 is left to gap 7.
    - S-4 is carried by brief:11, R-04's test «the search is the first act on the data, before any write», and rows 2 to 12 and 16.
    - S-5 is carried by brief:13.
    - S-6 is carried by brief:14, G-01 (`:73`), Q-4 «we recommend 1» (`QUESTIONS-PAPER.md:94`), R-03's test «the record saved holds F, G, D and S as entered», and lists rows 11 to 15.
    - S-7 is carried by R-07's test and search_rule row 18.
  - **F-1.** "Clerk sees" is gap 5. Its one fact, that the search does not run until all four are entered, is G-07 «all four entered before the search runs». "Is saved: no record" is a deduction from brief:14 (the one save follows "finds none") and G-07. It holds, and R-04's test «before any write» carries it directly, though F-1 does not cite R-04 (part 8, item 2).
  - **F-2.** "Clerk sees SC-4, the date refused" is carried by G-07 and settings row 17. G-09 is used only to make that refusal a screen, which is exactly what its row says. "Is saved" is gap 7.
  - **F-3.** Both fields are gap 6. The trigger is stated as the breach of G-07's «chosen from the data's three», with whether it can arise left open.
  - **F-4.** «refuse the entry» (`GAPS-PAPER.md:27`), «says the entry cannot be completed» and «enters nothing new» (`:102`, search_rule row 16).
  - **F-5.** "Clerk sees SC-3" follows from the search finding none (brief:14, R-07). "Is saved: a second record for the same child" is carried by brief:14 and R-06's test (b) together with G-05 «4 of the 8 caught» (`:196`) and settings row 14. One of its quotations is mispaired (part 8, item 1).

  **Result: 0 of the 17 fields state a fact their sources do not carry.** Version 1 had 2 failures (F-1, F-3) whose fields stated an unsourced refusal; version 2 has 0.
- **The sets, listed again by the review and compared both ways.**
  - Failures: part 2, 5 against 5, 0 missing either way.
  - Steps: `R/R_steps_screens.py` lists 7 steps from the sources, each with the source units that carry it, and matches each to a goal step that cites all of them: `missing from the goal: 0 []; in the goal and not the review: 0 []`.
- **Every screen the goal shows, against its list.** `R/R_steps_screens.out` shows 5 screens mentioned and the same 5 listed. Each is named by a step or failure, and each carries the line. The views of F-1 and F-3 are not screens in the goal: they are gaps 5 and 6, which is what the instruction's version 2 asks.
- **The faults of part 1 of the page:**
  - Item 1 (a fact supplied): none found (above).
  - Item 2 (a gap closed only for its examples): the test was applied to every field, not to F-1 and F-3 alone. `W/CHANGED_check.out` counts 7 of 7 steps and 5 of 5 failures changed in text, and the fact-level count is above.
  - Item 3 (working language): not applicable. The readers are rounds 4 and 6.
  - Item 4 (a limit): F-5 states the search's limit as a limit of S-4 (`GOAL.md:105`).
  - Item 5 (a shared word): applied above. One quotation shows the pattern, but its field is carried by other words (part 8, item 1).
- **The three failures of section 7 of the instruction.**
  - The sensible check invented: none. A date that is not a real date, an age, and a name's length are gaps 1, 2 and 4.
  - The unruled part read as ruled: none. 0 of the 111 quotations stand on an unruled line, and neither the paper's 64 (line 40) nor G-14 is used.
  - A screen forgotten: none. 5 screens are mentioned and 5 listed.
- **G1 and items 1 to 4 of the first edition:**
  - **G1 is closed for every step and failure** (above).
  - **Item 1 is closed.** The version 2 `started` entry reads `started_by: unknown` (`R/M4_ledger_show.out`), and so does the report's line 8.
  - **Item 2 is closed.** The rows the report names are confirmed by `R/R_report_consistency.out`: row 10 is cited by `['S-2', 'S-4', 'F-1']`, row 13 by `[]`, and rows 14, 15, 17 and 18 by S-5, S-6, F-4 and S-7.
  - **Item 3 is closed.** Gap 7 quotes `GAPS-PAPER.md:254` and settings row 17 against brief:11, R-04 (`REQUIREMENTS.md:62`) and search_rule row 11, and each quotation was found at its line here. S-3 and S-4 each keep neither order as fact.
  - **Item 4 is closed.** `R/R_report_consistency.out`: the `finished` outcome is identical to the first sentence of the report's section 1 (`identical: True`). The figures the report gives twice agree (part 2).

## 6. The four mechanical checks, run here

These were run directly at 17:34:07 to 17:34:09 UTC, not through `round_record.py run`.

| Check | Log | Lines that decide | Exit |
|---|---|---|---|
| Trace over the report | `R/M1_trace.out` | `outputs: 3 of 3 named exist` · `inputs: 9 of 9 pinned by 20261031T171318Z_MR_issued_C-2026-10-31-13.yaml hash the same now` · `trace check: clean` | 0 |
| Placement over the instruction | `R/M2_placement.out` | `in its place: …/_reports/REPORT_GOAL_2026-10-31_v2.md — a report` · `running_record: names the code MR (read from the constants)` · `placement check: clean` | 0 |
| `round_record.py check` | `R/M3_record_run.out`, `R/M3_check.out` | Run with the options on `W/record/check.out`'s `# run with:` line (`--tolerance 2`) and an `--out` of the review's own. Output: `## Findings — 0` · `quoted blocks read against the file they name: 12` | 0 |
| `ledger.py show … --id C-2026-10-31-13` | `R/M4_ledger_show.out` | Version 2: `issued` 17:13:18Z, `started` 17:16:20Z (`started_by: unknown`, `effort: unknown`), `finished` 17:31:01Z | 0 |
| `ledger.py check` | `R/M5_ledger_check.out` | `check: clean`. No line names `MR` | 0 |

**The accounts:** the version 2 `issued`, `started` and `finished` entries each read `account: arne.laponin@gmail.com`, the same as the report's declaration.

## 7. The verdict: accepted

A1 to A13 are met. The ground for the verdict:

- G1 is closed for every step and every failure: of the 17 "registry does", "clerk sees" and "is saved" fields, 0 state a fact their sources do not carry.
- The refusal screens that only an unsourced fact made are gone.
- The order of the date check and the search is left open as gap 7, with both sides quoted.
- Items 1 to 4 of the first edition are closed.
- The failures, re-established by a route the round did not use, number 5, as the goal gives.
- Both sets match the review's own listing with 0 missing either way.
- The four mechanical checks are clean.

No gap is named. The page of the kind needs no new fault from this review. The orchestrator writes one `closed` entry with the outcome `accepted`, which closes C-2026-10-31-13 with it. The items under "found, not fixed" become candidate instructions.

## 8. Found, not fixed

1. **F-5 has one mispaired quotation in `W/QUOTES.md`.** The phrase «so that the registry registers the same child twice» is quoted beside brief:7 and R-01, «the registry does not register the same child twice». Those passages state the purpose the failure breaks, not the fact that it happens. The fact is carried in the same field by brief:14 and R-06's test (b) with G-05 «4 of the 8 caught» and settings row 14. Q-8's proposal «each of the 4 the rule misses» (`QUESTIONS-PAPER.md:168`) carries it most directly. Nothing round 4 or round 6 reads changes.
2. **F-1's "no record" is reached by deduction** («the one save the sources give follows the search finding none»). R-04's test «the search is the first act on the data, before any write» (`REQUIREMENTS.md:67`) carries it directly but is not among F-1's sources.
3. **Gaps 5, 6 and 7 leave three outcomes open: what the clerk sees for F-1 and F-3, and what is saved for F-2 and F-3.** Under G-12 (`GAPS-PAPER.md:398`) round 6 writes a check for each way the goal goes wrong, so these checks have no expected result until the gaps are ruled. That is for the orchestrator to settle before round 4 or round 6, not a fault of the goal.
4. **S-6's "1 as the first" (Q-4) is never reached by a clerk's enrolment**, because the reset of G-03 makes the lists' children learners first. It is sourced and harmless.
5. **The ledger's entries still name `~/IdeaProjects/mini-registry/...`**, while the estate is at `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`. This is item 5 of the first edition; `show` resolves it "on this computer".
6. **The review instruction's body still names version 1's paths.** Section 2 names `REPORT_GOAL_2026-10-31.md`, section 3 names the `round-03-goal-review` evidence folder, and section 4's `--report` names `REVIEW_GOAL_2026-10-31.md`. The version 2 section overrides each, and this review followed it. The working instruction's A8 and A9 likewise carry version 1's paths, which its version 2 says to "read with this version's paths".
7. **`W/CHANGED_check.out` prints `screens: 7 in either version`** while version 2 lists 5. The counts on the same line (changed 3, unchanged 2, removed 2) are right.
