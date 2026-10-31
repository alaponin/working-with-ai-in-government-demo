---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md (C-2026-10-31-13, version 1)
written_by: a session that neither wrote nor carried out the instruction. It is MR · review · the goal in full (C-2026-10-31-14), started as a sub-agent with an empty memory
started_by: sub-session. This session's prompt is the review's start message, followed by the line that has it load its shell tool
account: arne.laponin@gmail.com. Read from the line of this session's own context that begins "The user's email address is"
model: claude-opus-5-5. Read from the line of this session's own context that names the model it is configured for. It is the band the review instruction names, Opus
computer: MacBookPro. Printed by `hostname` at 16:24:18 UTC, this session's first command
window: 2026-10-31 16:24:23 UTC (the started entry 20261031T162423Z_MR_started_C-2026-10-31-14.yaml) to 2026-10-31 16:33 UTC, no pause. It closes when this file is written
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md, with G1 appended
---

# REVIEW: the goal in full, enrol a learner (edition 1)

This review's evidence is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-review/_evidence/`, written below as `R/`. The round's evidence is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/`, written below as `W/`. The goal is `docs/GOAL.md`: 11777 bytes, sha256 `5ed146df…01db6c089` (`R/R_outputs.out`). The report was at its path when this review started, and it was read as it stood.

## 1. The tests of success, one by one

| Test | Met? | Evidence read or produced here |
|---|---|---|
| A1: the sets come first, 0 missing and 0 extra | met | `W/A1_check.out` prints `0 missing, 0 extra, 0 differing` for both sets. `R/R_outputs.out` shows the order: `STEPS_SET.md` and `FAILURES_SET.md` last written at 16:20:54Z, and `GOAL.md` at 16:21:35Z. The sets were not drawn from the sources by a program. `list_sets.py` holds them as typed lists (`STEPS = [` at line 14, `FAILURES = [` at line 74), so A1 compares the session's list with its own goal. Part 5 therefore lists the sets again, starting from the sources. |
| A2: every source resolves | met | `W/A2_check.out` prints `0 without source, 0 unresolved`. The review's own resolver, `R/R_lookup.py`, does not import the round's `sources.py`, and it reads a ruling only at its ruled lines. Its log, `R/R_lookup.out`, prints `steps: 7; failures: 5; screens: 7; tokens not resolving: 0`. A token can resolve without carrying the claim it is cited for. That check is part 5, and G1 comes from it. |
| A3: every failure complete | met | `W/A3_check.out` prints `0 incomplete`, and `R/R_lookup.out` prints all four fields of F-1 to F-5. The field is present for every failure. Whether its content is sourced is G1. |
| A4: the search step beside its rows | met | `W/A4_check.out`, and report lines 70 to 86. S-4 compares the fields of rows 2 to 4 and nothing more. It names row 7 (school) and row 9 (key table) only to say they are not compared and not read. In `R/R_lookup.out`, each of the 10 rows is printed beside S-4's text. One sentence of the report about rows 10 and 13 contradicts itself (part 8, item 2). |
| A5: every screen carries R-17's line | met | `R/R_screens.py` reads the whole file, the gaps included. Its log, `R/R_screens.out`, shows 7 SC numbers mentioned anywhere, the same 7 listed, `mentioned and not listed: []`, and each listed screen `carries the line: True`. |
| A6: the gaps section | met | `GOAL.md:156` has 11 numbered gaps, and each ends in a question mark. No step or failure answers one. Gap 5 takes for granted that F-1 and F-3 lead to a refusal, which is G1. |
| A7: the sources unchanged | met | `R/R_outputs.out`, 16:31:07Z: the eight checksums equal those in section 2 of the instruction. |
| A8: placement and trace, exit 0 | met | `W/A8_placement.out` and `W/A8_trace.out`. Both were run again here and both are `clean`, `EXIT=0` (part 6). |
| A9: the record check exits 0 | met | `W/record/check.out` shows `## Findings — 0`. It was run again here and gave `EXIT=0` (part 6). |
| A10: started and finished beside issued | met | `R/M4_ledger_show.out`: `issued` at 16:14:17Z, `started` at 16:16:36Z and `finished` at 16:24:02Z, all version 1. |

## 2. One figure re-established

**The figure:** the number of ways the goal can go wrong that the sources state or rule. The goal gives 5, F-1 to F-5.

**The round's route:** `list_sets.py` holds five failures, typed by the session, each with a source fragment, and `sources.py` checks that each fragment appears at the cited line.

**The route taken here:** start from the sources instead of from the members. `R/R_inventory.py` lists every unit in scope from the files themselves:

- each non-empty line of the brief's five sections
- each of R-01 to R-23
- each ruled row of G-01 to G-13
- each closing proposal of Q-1 to Q-14
- each row of the three tables

That gives 117 units. The review then marks each unit with what it carries: a step or failure of its own, a screen, or nothing (with the reason). The program stops if any unit has no mark. `R/R_inventory.out`:

```
units enumerated from the sources: 117; without a disposition: 0 []; dispositions for no unit: 0 []
the figure: failures the sources state or rule, listed source first: 5 ['x-missing', 'x-date', 'x-school', 'x-many', 'x-missed']
```

**The two agree: 5.** The reported times and counts were also checked at their sources:

- The window opens at the started entry (16:16:36Z, `R/M4_ledger_show.out`) and closes at the report's last write, 16:23:52Z (`R/R_outputs.out`). The finished entry follows at 16:24:02Z.
- The 73 sources of `W/A1_list.out` add up from the two set tables to 50 + 23 = 73.
- The goal has 11 gaps, 7 screens, 7 steps and 5 failures. All four counts were read from the file.

## 3. The outputs exist

`R/R_outputs.out`, 16:31:07Z:

- `docs/GOAL.md` is 11777 bytes with sha256 `5ed146df4878630c8f5d279f18fec3e440f3a83dabc36af9285b45f01db6c089`, as declared.
- `W/` holds 17 entries, and `W/record/` holds 8.
- The report is 13495 bytes.

All three outputs are at their paths.

## 4. The running application

Not applicable. The round wrote a document, not an application model.

## 5. What a review of this kind runs (`_kinds/drafting.md`, part 2)

- **Every claim looked up at its source.** `R/R_lookup.out` prints each step and failure, field by field, and beside it the text of each cited source. For a `ruling:` token that text is the ruled part only: the summary row and the closing **Recommendation** for G, and the closing **Proposal** for Q.
  - S-1 to S-7, F-2, F-4 and F-5 are carried by their sources.
  - S-6's "1 where it holds none" is Q-4's proposal.
  - F-4's "never reached" is G-02's recommendation together with settings row 13 and Q-14's proposal.
  - F-5's "4 of the 8" is G-05's recommendation and settings row 14, and it is stated as a limit of the search step.
  - **F-1 and F-3 are not carried in what the clerk sees.** Both say "the entry is refused". The sources give "refused" only for the date, in G-07's "refused otherwise" and settings row 17. G-09's "refusals included" defines what counts as a screen; it does not say that an entry is refused. That is G1.
- **The sets, listed again by the review and compared both ways.** `R/R_inventory.out` lists 7 steps and 5 failures of the review's own, worded differently from the round's:

  ```
  steps: the review lists 7, the goal 7; missing from the goal: 0 []; in the goal and not the review: 0 []
  failures: the review lists 5, the goal 5; missing from the goal: 0 []; in the goal and not the review: 0 []
  ```

  So 0 are missing in either direction. Five carrying units are not cited by the goal member they support: brief:24, settings:3, lists:16, R-01, and R-05 with G-05 for F-4. Each of those members already has a source, so none of them is a gap.
- **Every screen the goal shows, against its list.** The goal names 7 screens and lists the same 7, and each carries the line (`R/R_screens.out`). The view between submitting and the result is S-4's, which the goal says has "none of its own". Gaps 1 and 11 ask about views and add none.
- **The faults of part 1 of the page, read against the goal.**
  - Item 1, supplying a fact: G1.
  - Item 2 does not apply, because this is a first version.
  - Item 3 does not apply. The readers are rounds 4 and 6, and the codes are their working words.
  - Item 4: F-5 states the search's limit as a limit of S-4 (`GOAL.md:102` and the line after it), as the page asks. The refusal of F-1 and F-3 says more than the record carries, and the goal does not say so. Only the report says it, at `REPORT_GOAL_2026-10-31.md:164`.
- **The three failures in section 7 of the instruction.**
  - The sensible check invented: no date, age or name check appears; each is a gap (gaps 1, 2 and 4). But the refusal on F-1 and F-3 is an effect invented around a failure the instruction did ask for (G1).
  - The unruled part of a paper read as ruled: none. No token reads outside the ruled lines, and the paper's line 20 (G-14) and line 40 (64 learners) are not cited.
  - A screen forgotten: none.

## 6. The four mechanical checks, run here

These were run directly at 16:28:11 to 16:28:12 UTC, not through `round_record.py run`.

| Check | Log | Lines that decide | Exit |
|---|---|---|---|
| Trace over the report | `R/M1_trace.out` | `outputs: 3 of 3 named exist` · `inputs: 9 of 9 pinned by 20261031T161417Z_MR_issued_C-2026-10-31-13.yaml hash the same now` · `trace check: clean` | 0 |
| Placement over the instruction | `R/M2_placement.out` | `running_record: names the code MR (read from the constants)` · `placement check: clean` | 0 |
| `round_record.py check` | `R/M3_record_run.out`, `R/M3_record_check.out` | Uses the options on `W/record/check.out`'s `# run with:` line (`--tolerance 2`) with `--out` of the review's own. Output: `## Findings — 0` · `quoted blocks read against the file they name: 12` | 0 |
| `ledger.py show … --id C-2026-10-31-13` | `R/M4_ledger_show.out` | `issued` 16:14:17Z, `started` 16:16:36Z, `finished` 16:24:02Z, all `version: 1` | 0 |
| `ledger.py check` | `R/M5_ledger_check.out` | `check: clean`. No line names `MR`. | 0 |

**The accounts:** `issued`, `started` and `finished` each read `account: arne.laponin@gmail.com`, the same as the report's declaration. The `started` entry also reads `effort: unknown` and `started_by: owner` (part 8, item 1).

## 7. The verdict: not accepted

**One gap, G1.** A1 to A10 are met. Both sets, listed again from the sources, match the goal with 0 missing in either direction, and every screen is listed and carries the line. One fault remains, and round 6 would inherit it.

**G1 (trace): F-1 and F-3 say that the entry "is refused" and give it a refusal screen, but no source they cite says so.**

- `GOAL.md:70` (F-1) and `GOAL.md:86` (F-3) both read «the entry is refused; the search does not run», on SC-4 and SC-6.
- Their sources carry the trigger and that the search waits:
  - `GAPS-PAPER.md:254` «all four entered before the search runs»
  - `GAPS-PAPER.md:254` «the school chosen from the data's three»
  - `groundwork/settings.csv:18` «chosen from the data's 3 schools»
- They give "refused" only for the date: `GAPS-PAPER.md:254` «the date entered as YYYY-MM-DD and refused otherwise» and `groundwork/settings.csv:17` «any other form refused».
- G-09, which both cite, defines what counts as a screen and does not say that anything is refused: `GAPS-PAPER.md:34` «Every view the clerk can see is a screen, messages and refusals included».
- The report concedes this at line 164, but the goal does not say it. Gap 5 (`GOAL.md:164`) then asks what a refusal says, which takes for granted that there is one.

**What follows.** Under G-12 (`GAPS-PAPER.md:398` «with a check for each way the goal can go wrong that round 3 names»), round 6 would write checks that expect refusal screens for an entry missing and for a school not among the three. Round 4 would count SC-4 and SC-6 among the screens R-17 is tested on. For F-3, the goal's own gap 10 (`GOAL.md:169`) cannot say how that refusal could ever be shown.

**What it fails, and the faults of the kind it shows:**

- It fails section 4 of the instruction, «Supply no step, check or failure the sources do not carry … a missing one is a gap» (line 82), and section 3, «A step or failure with no source is not written» (line 78).
- It shows item 1 of part 1 of the drafting page (`_kinds/drafting.md:8`) and item 4 (line 11), "to say more than the record carries, without saying so".
- **It also shows a fault the page lacks:** citing a source that uses the claim's word but does not carry the fact. G-09's "refusals" and G-07's "refused otherwise" both contain the word, so the round's fragment check (`list_sets.py` anchors `'messages and refusals included'`) passes while neither says that this entry is refused.

The next version applies the same test to every failure's "what the clerk sees" and "what is saved", and says how many still fail. Of the five, this review finds two that fail: F-1 and F-3.

## 8. Found, not fixed

1. **`started_by` reads `owner` in both the report (line 8) and the `started` entry, while the report says a scheduled task started the session.** The form gives `owner` only where the owner typed or pasted the start message. A session that can only tell it was started by a scheduled task should write `unknown` (`PROMPT-template.md`, "Who started you"). The same finding was made on the commit round. Kind: `form`. The verdict does not turn on it.
2. **Report line 90 contradicts itself.** It says «Rows 10 … and 13 to 18 are cited by S-2, S-3, S-5, S-6, S-7 and F-4», then «row 13 … is cited by no step». Row 10 is also cited by F-1.
3. **S-3 against S-4.** S-3 has the registry refuse a date in the wrong form before the search runs (`GOAL.md:30`). S-4 says the search runs «first, before it does anything else with the entry» (`GOAL.md:37`, citing search_rule row 11 and R-04). The sources do not settle which comes first. R-04's test reads only acts on the data, so a build passes it either way.
4. The `finished` entry's outcome says «A1-A8 met», while the report's section 1 says «A1 to A7 are met; A8 and A9 are answered». Its A8 section says "met".
5. The ledger's entries still name `~/IdeaProjects/mini-registry/...`, while the estate is at `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`. `show` resolves this "on this computer". It was already found by round 2 and by this report.
