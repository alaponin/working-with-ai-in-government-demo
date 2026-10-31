---
kind: report
answers: C-2026-10-31-13
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31_v2.md
written_by: a working session (MR · work · the goal in full), separate from the session that wrote the instruction, started with an empty memory for version 2
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt says only that a scheduled task fired the stored prompt; it shows neither that the owner typed or pasted it nor that a working session started it; the started entry carries unknown
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command, at 17:16:14 UTC, before the started entry
window: 2026-10-31 17:16:20 UTC to 2026-10-31 17:30:50 UTC, no pause; closed at the last write of the 25 files the round names as written, REPORT_GOAL_2026-10-31_v2.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md 13891 bytes sha256 342515fd5ed96e45e23014568f67e8126edfeeccdb7f862dddd38e44acdb2aed · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/ · this file
ledger: MR C-2026-10-31-13 — the started entry is 20261031T171620Z_MR_started_C-2026-10-31-13.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write the goal in full: every step of enrolling a learner, and every way it can go wrong, each traced to its source (version 2)

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md` (`C-2026-10-31-13`, version 2) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`, every program with `/usr/bin/python3` (3.9.6)

Below, every evidence path is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/`.

## 1. The answer first

Version 2 of the goal closes G1 for every step and every failure: each fact of each field now stands beside the source words that carry it, or names the gap that holds it open (0 unquoted), and the refusal screens that only an unsourced fact made, for an entry missing and for a school not among the three, are gone. `docs/GOAL.md` is changed in place: 7 steps, 5 failures, 5 screens (version 1 had 7) and 13 gaps (version 1 had 11). F-1 now says only what the sources carry, that the search does not run until all four are entered; what the clerk then sees is gap 5. F-3 says only that the school is chosen from the data's 3; whether a school not among them can reach the registry, and what follows, is gap 6. The order of the date check and the search is not settled by the sources; S-3 and S-4 keep neither order as fact, and gap 7 quotes both sides. Every step and every failure changed in its text against version 1 (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/CHANGED_check.out`). A1 to A8 and A11 to A13 are met; A9 is answered by the record's check.out; A10 is the review's to establish, the `finished` entry following this report.

## 2. The criteria, one by one

### A1 — The sets come first — met

`inventory.py` enumerates every unit of the sources in scope from the files themselves (the brief's five sections line by line, R-01 to R-23, the ruled units of G-01 to G-13 and Q-1 to Q-14, every row of the three tables), gives each a disposition, stops on a unit without one, and writes `STEPS_SET.md` and `FAILURES_SET.md` from the units that carry each member. It ran at 17:22:46 UTC (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/record/runs.jsonl`, run 2); `GOAL.md` was first written after it and last at 17:25:00 UTC (`RECORD.txt`). Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A1_inventory.out`:

```
units enumerated from the sources: 118; without a disposition: 0 []; dispositions for no unit: 0 []; unresolved: 0 []
units carrying a member or the screens' line: 50; units carrying none: 68
steps: 7, each with at least one source: True; tokens: 52
failures: 5, each with at least one source: True; tokens: 27
```

The comparison, by identifier, by each member's set of sources and, for a failure, its step, `check_goal.py a1`, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A1_check.out`:

```
steps: 0 missing, 0 extra, 0 differing
failures: 0 missing, 0 extra, 0 differing
```

### A2 — Every source resolves — met

`check_goal.py a2` with `sources.py`, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A2_check.out`:

```
steps: 7; failures: 5; tokens resolved: 82 (of them the screens' line: 3)
0 without source, 0 unresolved
```

### A3 — Every failure is complete — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A3_check.out`: each of F-1 to F-5 prints `step yes, trigger yes, clerk sees yes, saved yes, source yes`, and the last line is:

```
0 incomplete
```

A field present is not a fact sourced: where the sources give nothing, the field says so and names its gap (F-1 clerk sees, F-2 saved, F-3 clerk sees and saved). Whether each field's content is carried is A11.

### A4 — The search step beside the rows it cites — met

S-4's "The registry", printed by `check_goal.py a4` beside each row of `search_rule.csv` it cites. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A4_check.out`:

```
  groundwork:search_rule.csv:2  compares,family name,brief:13 · R-05
  groundwork:search_rule.csv:3  compares,given names,brief:13 · R-05
  groundwork:search_rule.csv:4  compares,date of birth,brief:13 · R-05
  groundwork:search_rule.csv:5  forgives,capitals: two values that differ in capitals only are the same,brief:13 · R-05
  groundwork:search_rule.csv:6  forgives_nothing_else,every difference but capitals makes two values differ,brief:13
  groundwork:search_rule.csv:7  does_not_compare,"school: entered and saved, never searched on",brief:13 · ruling:G-07
  groundwork:search_rule.csv:8  does_not_compare,any field but the three compared,brief:13
  groundwork:search_rule.csv:9  does_not_read,the key table,ruling:G-05
  groundwork:search_rule.csv:10  when,"after the clerk has entered all four: family name, given names, date of birth and school",brief:11 · ruling:G-07
  groundwork:search_rule.csv:11  when,first: before the registry does anything else with the entry,brief:11 · R-04
  groundwork:search_rule.csv:12  where,among learners only,ruling:G-03
  groundwork:search_rule.csv:16  on_more_than_one,enters nothing new and says the entry cannot be completed,ruling:G-02
rows cited: 12; compares rows in the file: 3; compares rows cited: 3
```

S-4 compares the three fields of rows 2 to 4, forgives capitals by row 5 and nothing else by row 6, and names the school (row 7), every other field (row 8) and the key table (row 9) only to say they are not compared or read. Rows 10 and 11 give when it runs; the order of row 11 against S-3 is gap 7. Row 16 is cited for the branch to F-4. Of the rows not cited by S-4: row 13 is the reset's (no step of this goal, the ruling on G-08); rows 14, 15 and 18 are cited by S-5, S-6 and S-7; row 17 by F-4.

### A5 — Every screen carries R-17's line — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A5_check.out`:

```
screens named by the steps and failures: 5 ['SC-1', 'SC-2', 'SC-3', 'SC-4', 'SC-5']
screens mentioned anywhere in the goal, gaps included: 5 ['SC-1', 'SC-2', 'SC-3', 'SC-4', 'SC-5']
screens listed: 5; listed screens stating the line: 5
```

### A6 — The gaps section — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A6_check.out`:

```
section present; gaps: 13; not a question: 0
probes for an answer in the steps, failures and screens: 17, found: 0 []
```

No step or failure answers a gap: where one reaches an open fact (S-3, S-4, F-1, F-2, F-3) it names the gap and stops.

### A7 — The sources unchanged — met

`shasum -a 256` at 17:27:50 UTC, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A7_shasum.out`: all eight checksums equal those of section 2 of the instruction (brief `ec6971e7…`, register `ad583b39…`, `GROUNDWORK.md` `5ed9b62f…`, `search_rule.csv` `9a7c98ce…`, `settings.csv` `a94c31fe…`, `lists.csv` `1d08f58c…`, `GAPS-PAPER.md` `d03db64c…`, `QUESTIONS-PAPER.md` `5146d23a…`). They were also equal at the round's start.

### A8 — The placement and trace checks, outside `run` — met

Both run directly, not through `run`, at 17:29:51 UTC, once this report existed. The placement check over the instruction, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A8_placement.out`:

```
placement check: clean
EXIT=0
```

The trace check over this report, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A8_trace.out`:

```
  outputs: 3 of 3 named exist
  inputs: 9 of 9 pinned by 20261031T171318Z_MR_issued_C-2026-10-31-13.yaml hash the same now
trace check: clean
EXIT=0
```

### A9 — The record check — answered by `check.out`

`round_record.py check` is run as the round's last act before the `finished` entry, outside `run`; its output stands in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/record/check.out`, which the review reads. `end` was run at 17:29:40 UTC with 0 findings (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/record/RECORD.txt`, section 4); 14 runs traced, every program of the round among them.

**Written after `end`**, and so not on the record's lists: in the evidence folder, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A8_placement.out`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A8_trace.out` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/ls_ld.out`; in the record's folder, `window.out` and `check.out`; and this report. **Written by hand, not by a traced run** (`RECORD.txt` section 1 says which): the programs themselves, `docs/GOAL.md`, the logs written by the shell's redirection of a traced run's output, `A7_shasum.out` and this report.

### A10 — The ledger's entries

The `started` entry is `20261031T171620Z_MR_started_C-2026-10-31-13.yaml`, `--started-by unknown`, `--effort unknown`; the `finished` entry follows this report. The review runs `ledger.py show`.

### A11 — Every fact beside the words that carry it — met

`quotes.py` takes each fact of each step's "The clerk" and "The registry" and each failure's "What sets it off", "What the clerk sees" and "What is saved" as a phrase that must stand in that field of the goal, and sets beside it the words of its source, found whole at the lines its token resolves to (a ruling only at its ruled lines) and among the member's own sources; or `gap G-<n>`, the gap existing. It writes `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/QUOTES.md`, one row per step and per failure. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A11_quotes.out`:

```
members: 12 (steps 7, failures 5); fields: 29; quotations: 111, every one found at its source: True; gap references: 8
0 unquoted
```

The test of version 1's fault, applied to every field: a shared word is not taken as a source. G-09's «messages and refusals included» is cited only for *that a refusal is a view the clerk sees, so a screen* (F-2's SC-4, F-4's SC-5), never for *that something is refused*; that is carried by G-07's «refused otherwise» (the date) and G-02's «refuse the entry» (more than one found). Of the five failures, two had fields version 1 sourced only by a shared word, F-1 and F-3; after this version, 0 do.

### A12 — No screen rests on an unsourced fact — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/A12_check.out`, each screen with the member that makes it and that member's A11 fact:

| Screen | Made by | The A11 fact that makes it |
|---|---|---|
| SC-1 the enrolment screen | S-1, S-2 | S-1 *opens the enrolment screen* ← R-03 «open the enrolment screen»; S-2 *enters the family name…* ← brief:11 |
| SC-2 a learner found | S-5, S-7 | S-5 *shows that learner and enters nothing new* ← brief:13, R-05, search_rule:14; S-7 ← R-07 «the second says that an existing learner was found, and shows that learner» |
| SC-3 a new learner | S-6, S-7, F-5 | S-6 *gives the child a new learner number* ← brief:14, R-06; S-7 and F-5 ← R-07 «the first screen says that a new learner number was given, and shows it» |
| SC-4 the date of birth refused | S-3, F-2 | S-3 *a date in any other form is refused* ← G-07 «refused otherwise», settings:17 «any other form refused»; F-2 *SC-4* ← G-09 «Every view the clerk can see is a screen, messages and refusals included» |
| SC-5 the entry cannot be completed | F-4 | F-4 *SC-5* ← G-09 (as above); *the entry is refused* ← G-02 «refuse the entry»; *says the entry cannot be completed* ← G-02 |

Version 1's SC-4 (an entry missing) and SC-6 (a school not among the three) are removed, being made only by the unsourced refusals of F-1 and F-3. Version 1's SC-5 is now SC-4, and its SC-7 is now SC-5, renumbered; `check_goal.py changed` compares by number, so it prints SC-4 and SC-5 as changed and SC-6 and SC-7 as removed.

### A13 — The review of version 1, item by item — met

| Item of `_reviews/REVIEW_GOAL_2026-10-31.md` | What changed | Where |
|---|---|---|
| G1 — F-1 and F-3 refused on screens no source carries | Applied to every field of every step and failure (A11, 0 unquoted). F-1 says only that the search does not run until all four are entered, its view gap 5; F-3 only that the school is chosen from the 3, its view and save gap 6; SC-4 and SC-6 of version 1 removed; the shared-word test set out under A11 | `docs/GOAL.md` F-1, F-3, section 3, gaps 5, 6, 8; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/QUOTES.md` |
| 1 — `started_by` owner where a scheduled task started the session | `unknown`, in the started entry and in this report's declaration | `20261031T171620Z_MR_started_C-2026-10-31-13.yaml`; this file, line 8 |
| 2 — the report's sentence on rows 10 and 13 contradicting itself | Rewritten from the A4 log: row 10 is cited by S-2, S-4 and F-1; row 13 by no member, being the reset's | this report, A4 |
| 3 — S-3 against S-4 on the order | Neither order kept as fact: S-3 numbered first for reading only, S-3 and S-4 each name gap 7, gap 7 quotes the ruling on G-07 and settings row 17 against brief line 11, R-04 and search_rule row 11; F-2 no longer says the search does not run | `docs/GOAL.md` "The order of the steps", S-3, S-4, F-2, gap 7 |
| 4 — the finished entry's outcome against the report | The outcome is the first sentence of section 1 of this report, word for word; each figure given twice here is the same both times | the `finished` entry; this report, section 1 |

**How many steps and failures changed** (`check_goal.py changed`, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/CHANGED_check.out`):

```
steps: 7 in either version; changed 7, unchanged 0, added 0, removed 0
failures: 5 in either version; changed 5, unchanged 0, added 0, removed 0
```

A change of text is counted; some are of wording only (S-1 "the school chosen from" for "a choice among", S-5 "sees the result at S-7"). The changes of fact: S-2's registry ("nothing yet" replaced by what the sources give), S-3 (the order and the check of all four and of the school taken out), S-4 (when it runs, the gap), S-6 ("1 as the first", Q-4's own words, for "1 where it holds none"), and every failure.

## 3. Found, not fixed

1. The ledger's entries name the estate as `~/IdeaProjects/mini-registry/...` while it is at `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` (the review of version 1, item 5; `WHAT_IS_RUNNING.md`, Open table).
2. Q-4's proposal says «Any first number serves; we recommend 1»; the groundwork's gap 4 asked for the number given «when the registry holds none». Version 1 wrote the second; this version writes the proposal's own words, "1 as the first".

## 4. What I could not establish

Nothing the instruction asks for. Whether the shared-word test is applied as the reviewer would apply it to F-2's "SC-4" (G-09 for *a refusal is a view*, G-07 for *the date is refused*) is the review's to judge.

## 5. Corrections to the instruction

Section 4 names the record at `_working/round-03-goal/_evidence/record`; version 2 moves it to `_working/round-03-goal-v2/_evidence/record`, and that path was used. Section 2's read list and checksums were all as stated.

## 6. What this round did not finish

Nothing of its task. The 13 gaps go to the owner or to the round that rules on them; round 4 counts against this version.

## 7. The outputs, by path

Each place the round wrote in, listed at 17:29:51 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/ls_ld.out`:

```
drwxr-xr-x@ 9 arnelaponin  staff  288 Oct 31 19:25 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs
EXIT=0
drwxr-xr-x@ 25 arnelaponin  staff  800 Oct 31 19:29 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence
EXIT=0
drwxr-xr-x@ 15 arnelaponin  staff  480 Oct 31 19:29 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports
EXIT=0
```

The listing's times are the computer's local time (UTC+2). `docs/GOAL.md` is 13891 bytes, sha256 `342515fd5ed96e45e23014568f67e8126edfeeccdb7f862dddd38e44acdb2aed` (`RECORD.txt`, section 1). Version 1's report and evidence are untouched; version 1 of the goal is kept as `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/GOAL_v1.md`, sha256 `5ed146df…01db6c089`, as the review of version 1 read it.
