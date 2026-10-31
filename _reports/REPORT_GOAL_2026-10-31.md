---
kind: report
answers: C-2026-10-31-13
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31.md
written_by: a working session (MR · work · the goal in full), separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: owner — this session's prompt is the stored prompt of a scheduled task on the owner's account, fired by its schedule; the started entry carries owner
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command after its started entry
window: 2026-10-31 16:16:36 UTC to 2026-10-31 16:23:52 UTC, no pause; closed at the last write of the 18 files the round names as written, REPORT_GOAL_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md 11777 bytes sha256 5ed146df4878630c8f5d279f18fec3e440f3a83dabc36af9285b45f01db6c089 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/ · this file
ledger: MR C-2026-10-31-13 — the started entry is 20261031T161636Z_MR_started_C-2026-10-31-13.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write the goal in full: every step of enrolling a learner, and every way it can go wrong, each traced to its source

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md` (`C-2026-10-31-13`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`, every program with `/usr/bin/python3` (3.9.6)

## 1. The answer first

The goal is written, `docs/GOAL.md`: 7 steps (S-1 the clerk opens the enrolment screen, S-2 enters and submits, S-3 the registry takes the entry, S-4 the search, S-5 exactly one found, S-6 none found, S-7 the clerk sees which happened), 5 ways it can go wrong (F-1 an entry missing, F-2 the date in the wrong form, F-3 a school not among the three, F-4 more than one learner found, F-5 the same child not caught because a field differs in more than capitals), 7 screens each stating R-17's line, and 11 gaps against the sources, each a question left open. The sets of steps and failures were listed by program first, every source of every member checked at its line — a ruling only at its paper's ruled lines — 73 sources, 0 not found; the goal matches both sets with 0 missing and 0 extra. A1 to A7 are met; A8 and A9 are answered in their sections below; A10 is the review's to establish, the `finished` entry following this report. F-5 is a limit of the search step the sources name (the ruling on G-05: 4 of the 8 caught), written as a way the goal goes wrong so that the build and the count carry it; it widens nothing.

## 2. The criteria, one by one

### A1 — The sets come first — met

`list_sets.py` wrote `STEPS_SET.md` and `FAILURES_SET.md` at 16:20:54 UTC; `GOAL.md` was last written at 16:21:35 UTC (`RECORD.txt`, section 1). Its log, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A1_list.out`:

```
steps: 7; failures: 5; sources checked: 73; not found: 0
```

The comparison, by identifier and by the set of sources of each member (and, for a failure, its step), `check_goal.py a1`, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A1_check.out`:

```
steps: set 7, goal 7
steps: 0 missing, 0 extra, 0 differing
failures: set 5, goal 5
failures: 0 missing, 0 extra, 0 differing
```

### A2 — Every source resolves — met

`check_goal.py a2` (with `sources.py`, both in the evidence folder) resolves every token: a brief line exists, an `R-<nn>` is a section of the register, a `ruling:G-<nn>` is one of G-01 to G-13, a `ruling:Q-<n>` one of Q-1 to Q-14, a `groundwork:<file>:<line>` exists; it also resolves the three sources of the screens' line. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A2_check.out`:

```
steps: 7; failures: 5; screens' line sources: 3
0 without source, 0 unresolved
```

### A3 — Every failure is complete — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A3_check.out`:

```
F-1: step yes, trigger yes, clerk sees yes, saved yes, source yes
F-2: step yes, trigger yes, clerk sees yes, saved yes, source yes
F-3: step yes, trigger yes, clerk sees yes, saved yes, source yes
F-4: step yes, trigger yes, clerk sees yes, saved yes, source yes
F-5: step yes, trigger yes, clerk sees yes, saved yes, source yes
0 incomplete
```

### A4 — The search step cites `search_rule.csv` and compares nothing more — met

`check_goal.py a4` prints S-4 beside the rows it cites. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A4_check.out`:

```
  groundwork:search_rule.csv:2  compares,family name,brief:13 · R-05
  groundwork:search_rule.csv:3  compares,given names,brief:13 · R-05
  groundwork:search_rule.csv:4  compares,date of birth,brief:13 · R-05
  groundwork:search_rule.csv:5  forgives,capitals: two values that differ in capitals only are the same,brief:13 · R-05
  groundwork:search_rule.csv:6  forgives_nothing_else,every difference but capitals makes two values differ,brief:13
  groundwork:search_rule.csv:7  does_not_compare,"school: entered and saved, never searched on",brief:13 · ruling:G-07
  groundwork:search_rule.csv:8  does_not_compare,any field but the three compared,brief:13
  groundwork:search_rule.csv:9  does_not_read,the key table,ruling:G-05
  groundwork:search_rule.csv:11  when,first: before the registry does anything else with the entry,brief:11 · R-04
  groundwork:search_rule.csv:12  where,among learners only,ruling:G-03
rows cited: 10; compares rows in the file: 3
```

The step itself, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md:37-37`:

```
- **The registry:** searches first, before it does anything else with the entry and before any write; it looks among learners only; it compares the family name, the given names and the date of birth, and nothing else; two values that differ in capitals only are the same, and every other difference makes two values differ; it does not compare the school, which is entered and saved and never searched on, nor any field but the three; it does not read the key table. On exactly one learner found the goal goes on at S-5, on none at S-6, on more than one at F-4.
```

It compares the three fields of rows 2 to 4 and nothing else; the school (row 7) and the key table (row 9) are named only as not compared and not read. Rows 10 (all four entered) and 13 to 18 are cited by S-2, S-3, S-5, S-6, S-7 and F-4; row 13, the reset's enrolment, is cited by no step, the reset being no step of the goal (G-08).

### A5 — Every screen carries R-17's line — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A5_check.out`:

```
screens named by the steps and failures: 7 ['SC-1', 'SC-2', 'SC-3', 'SC-4', 'SC-5', 'SC-6', 'SC-7']
screens listed: 7; listed screens stating the line: 7
named, not listed: []; listed, not named: []
```

### A6 — The gaps section — met

`check_goal.py a6` finds "Gaps against the sources", counts its numbered gaps, checks each ends in a question mark, and searches the steps, failures and screens for twelve marks of an answer to one. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A6_check.out`:

```
section present; gaps: 11; not a question: 0
probes for an answer in the steps, failures and screens: 12, found: 0 []
```

### A7 — The sources unchanged — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A7_shasum.out`, the eight checksums of the instruction's section 2:

```
ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64  brief/MINI-REGISTRY-BRIEF.md
ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103  mini-registry/docs/REQUIREMENTS.md
5ed9b62f282d433df7c337a2da30e4830c56170dca1e646ae5aacc2cc2795dce  mini-registry/docs/GROUNDWORK.md
9a7c98ce9b57dde82ccca48c84c638b7efd5c08f26f1677e738ecc8d00386fdb  mini-registry/docs/groundwork/search_rule.csv
a94c31fe9fc96410910e425b1a0dfc708ea6acf09f3fb9ab1c990e71f8ef9cfd  mini-registry/docs/groundwork/settings.csv
1d08f58c5ea6d1caddfed7f6266800083bed696e7cd1b76c6efc53be72c9eef7  mini-registry/docs/groundwork/lists.csv
d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb  mini-registry/docs/GAPS-PAPER.md
5146d23a87cf9c0527c26c2965725bfa1125bd1a0a103ac83b68fb7dbd50cce0  mini-registry/docs/QUESTIONS-PAPER.md
```

The record's list of reads (`RECORD.txt`, section 2) gives the same checksum at the start and the end for each source its programs read.

### A8 — Placement and trace checks, outside `run` — met

Both run directly, not through `run`, at 16:23:27 UTC, once this report was written. The placement check over the instruction, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A8_placement.out`:

```
placement check: clean
EXIT=0
```

The trace check over this report, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/A8_trace.out`:

```
  outputs: 3 of 3 named exist
  inputs: 9 of 9 pinned by 20261031T161417Z_MR_issued_C-2026-10-31-13.yaml hash the same now
trace check: clean
EXIT=0
```

### A9 — The record check — answered by `check.out`

`round_record.py check` is run as the round's last act before the `finished` entry, outside `run`; its output stands in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/record/check.out`, which the review reads. `end` was run at 16:22:26 UTC with 0 findings (`RECORD.txt`, section 4).

**Written after `end`**, and so not on the record's lists: in the evidence folder, `A8_placement.out`, `A8_trace.out` and `ls_ld.out`; in the record's folder, `window.out` and `check.out`; and this report.

### A10 — The ledger entries — the started entry stands; the rest is the review's

The `started` entry, `20261031T161636Z_MR_started_C-2026-10-31-13.yaml`, exit 0 at 16:16:36 UTC, account `arne.laponin@gmail.com`. The `finished` entry is written after this report; `ledger.py show` is run by the review.

## 3. Found, not fixed

- `WHAT_IS_RUNNING.md`, the Open block, gives this task's files as `~/IdeaProjects/mini-registry/...`; the estate's root is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` (already found by round 2).
- The register's R-07 test reads "the first screen says that a new learner number was given ... the second says that an existing learner was found"; the brief's line 15 says only "which of the two happened". The goal keeps R-07's two screens (SC-2, SC-3) and adds nothing to what they say.
- The ruling on G-02 says both "refuse the entry" (its summary row) and "says the entry cannot be completed" (its recommendation); the goal takes the recommendation's words for SC-7 and the groundwork's row 16, which agree with it.

## 4. What I could not establish

- What a refusal for an entry missing (F-1) or a school not among the three (F-3) says: the ruling on G-07 says "refused otherwise" of the date alone, and "all four entered before the search" and "school chosen from the three" of the others; with the ruling on G-09 ("messages and refusals included") the goal states that the entry is refused and the search does not run, and puts the wording as gap 5.
- Whether SC-4 to SC-6 are three screens or one screen with three messages: the goal lists them as three views (G-09: every view is a screen), so that R-17 is tested on each; gap 6 asks how several faults at once are shown.

## 5. Corrections to the instruction

- The instruction's section 1 asks for `--effort unknown`; it was written so. The scheduled task shows no effort.
- The session runs on claude-opus-5-5, the band the instruction names.

## 6. What this round did not finish

Nothing of section 3. The 11 gaps of `GOAL.md` are left open for the owner's ruling; gaps 1 to 4 bear on round 6's checks of the entry.

## 7. The outputs, by path

Each place the round wrote in, listed at 16:23:28 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/ls_ld.out`:

```
drwxr-xr-x@ 9 arnelaponin  staff  288 Oct 31 18:21 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs
EXIT=0
drwxr-xr-x@ 19 arnelaponin  staff  608 Oct 31 18:23 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence
EXIT=0
drwxr-xr-x@ 14 arnelaponin  staff  448 Oct 31 18:23 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports
EXIT=0
```
