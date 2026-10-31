---
kind: report
answers: C-2026-10-31-01
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_REQUIREMENTS_2026-10-31.md
written_by: a working session (MR · work · register of requirements), separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — read from this session's own prompt, which shows it was started by a scheduled task and not who stored it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command, at 2026-10-31 13:04:44 UTC
window: 2026-10-31 13:04:44 UTC to 2026-10-31 13:13:00 UTC — opened at the round's first command (`date -u; hostname`), closed at this line's own write, the report's last; read by `date -u` and `stat` in one command, because `round_record.py window` needs a started entry in the ledger and this estate has none; the command and its output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md 18400 bytes sha256 ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/ (its files listed with their sizes and checksums in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/RECORD.txt, section 1) · this file
ledger: MR C-2026-10-31-01 — the estate's record is not cut over to the ledger (the instruction's running_record line names a row added by hand); the round took up its row in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 31 Oct 2026, 13:05 UTC, closes it by hand into the Closed table after this report, and writes no ledger entry
---

# ACCOUNT — Write the register of requirements of the mini registry: every sentence of the brief that says what the registry must do, numbered, each with a test

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md` (`C-2026-10-31-01`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process` (`mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process`), proved by `date -u; hostname`, which printed `Sat Oct 31 13:04:44 UTC 2026` and `MacBookPro`

## 1. The answer first

The register stands at `docs/REQUIREMENTS.md`: 23 requirements, R-01 to R-23, each citing one unit of the brief by identifier and line, quoting it word for word, stating it in one sentence and giving a test in three parts (set up, do, see), closed by **Gaps against the brief** with 14 open questions (G-01 to G-14). It rests on an inventory made by program: the brief's five sections split into 29 units, 20 marked requirement and 9 not (5 headings, the table's header row, and three sentences of "What it is for" — the ministry's wish, the prototype's purpose, and "It is not the registry."). Three units each carry two requirements (lines 33, 34, 35: each "must not" item states a prohibition and a second sentence), so 20 units give 23 requirements. The search rule is written as the brief writes it — capitals ignored, nothing else; the four differently spelt children are counted in the data (R-12) and not tested against the search. The brief's sha256 is unchanged.

Judgement calls a reviewer may read otherwise: U-05 "It is not the registry." and U-04 "The prototype is for agreement." are marked not a requirement; U-21 "The numbers are fixed so that every later count has a known answer." is marked requirement.

## 2. The criteria, one by one

### A1 — the inventory, made by a program, with both counts — met

Program `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/split_units.py`, dispositions in `dispositions.tsv` beside it, output `SENTENCES.md` beside it; run through `round_record.py run` (run 2 of the record) at 2026-10-31 13:08:01 UTC.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A1_inventory_count.log`:
```
units: 29
marked requirement: 20
marked not a requirement: 9
exit=0
$ grep -c '^### U-' SENTENCES.md
29
$ grep -c '^### U-.* · requirement$' SENTENCES.md
20
```

A first try, at 13:07:46 UTC, ran under `python3` 3.7.9, whose audit hooks `round_record.py` needs and lacks (`AttributeError: module 'sys' has no attribute 'addaudithook'`); its counts were the same, and its log is kept as `A1_inventory_count_try1_python37.log`. The record lists it as run 1 and says "traced in full", which its opens were not. The run that counts is run 2, under `/usr/bin/python3` 3.9.6.

### A2 — both ways, `0 uncited, 0 unsupported` — met

Program `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/compare_register.py`, run 3 of the record, at 2026-10-31 13:10:00 UTC. It also counts as unsupported a requirement whose cited line or quote differs from the inventory's for its unit.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A2_A3_compare.log`:
```
A2: 0 uncited, 0 unsupported
A3: 0 not found
tests without the three parts: 0
```

That the comparison catches a fault was shown by planting three in a copy (`planted/REQUIREMENTS_planted.md`): R-23 removed, R-10's quote altered, R-02 made to cite U-02.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A2_A3_planted.log`:
```
UNCITED U-07
UNCITED U-29
UNSUPPORTED R-02: cites U-02, not a unit marked requirement
UNSUPPORTED R-10: line or quote differs from the inventory's U-17
NOT FOUND R-10
A2: 2 uncited, 2 unsupported
A3: 1 not found
```

### A3 — every quote a substring of the brief, `0 not found` — met

The same run, the same log, line `A3: 0 not found` (quoted above).

### A4 — every test on a known number states it as its expected result — met

Read by `grep -n -E "^### R-(0[89]|1[0-4])$|Expected" REQUIREMENTS.md` at 2026-10-31 13:10:33 UTC, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A4_known_numbers.log`.

| Requirement | Known number of the brief | Expected result its test states |
|---|---|---|
| R-08 | three lists (line 19) | 3 lists, by name |
| R-09 | 60 children | 60 |
| R-10 | 3 schools | 3 |
| R-11 | 8 on more than one list | 8 |
| R-12 | 4 of those spelt differently | 4 |
| R-13 | ages 6 to 12 | every age within 6 to 12; children outside: 0 |
| R-14 | all five settings | 60, 3, 8, 4, ages within 6 to 12, after each reset |

### A5 — **Gaps against the brief** exists, each gap a question, no answer elsewhere — met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A5_gaps.log`:
```
$ grep -n "^## Gaps against the brief$" REQUIREMENTS.md
324:## Gaps against the brief
$ grep -c "^- \*\*G-[0-9][0-9]\*\*" REQUIREMENTS.md
14
$ grep -c "^- \*\*G-[0-9][0-9]\*\*.*?$" REQUIREMENTS.md
14
```

14 gaps, 14 ending in a question mark. Where a test needs a gap's answer it names the gap ("gap G-04") and leaves the value open; no test states an answer (for example R-09 counts "by the unit of counting that gap G-04 asks after", and R-13 leaves the date and the bounds to G-06). That no answer appears is a reading, not a command's result.

### A6 — the brief unchanged — met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A6_brief_sha.log`:
```
ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64  /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md
exit=0
```

The record agrees: the brief's checksum at the start and at the end of the window is the same (`record/RECORD.txt`, section 2).

### A7 — the placement check and the trace check exit 0

Both run at 2026-10-31 13:12:06 UTC, under `/usr/bin/python3`, after the report's first write.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A7_placement_check.log`:
```
placement check: clean
exit=0
```

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A7_trace_check.log`:
```
  agrees: the report answers C-2026-10-31-01, the instruction's commission_id
  agrees: the instruction's downstream_artefact is this report
  outputs: 3 of 3 named exist
  inputs: the ledger holds no issued entry for /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md; no checksum to compare
trace check: clean
exit=0
```

Met. A first run of the placement check, at 13:10:45 UTC before this report existed, exited 1 on the one finding that the report was missing; its log was renamed after the end list to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A7_placement_check_before_report.log`, a change after `end` named here.

### A8 — the round's record check exits 0

Command: `python3 -B round_record.py check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record --report <this report> --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/check.out`, under `/usr/bin/python3`. Its output is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/check.out`, written again by each run.

A first run, at 2026-10-31 13:12:22 UTC, exited 1 on one finding: a log renamed after the end list was named in this report without its full path. The report was corrected; the run that decides this criterion is the round's last act before its row is closed, after the `window` line is written, and its exit is quoted in the row it closes and read again by the review. Files written after the end list and named here: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A7_placement_check.log`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A7_placement_check_before_report.log`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/A7_trace_check.log`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/check.out`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/window.out`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/ls_outputs.log`, and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` (its row closed).

### A9 — the row in WHAT_IS_RUNNING.md taken up and closed — met in part at the moment of writing

The row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` was taken up at 31 Oct 2026, 13:05 UTC (the time `date -u` printed in the same command that wrote it), before `round_record.py start` at 13:05:40 UTC, so the record does not list that write. It is closed into the Closed table after this report and the record's check, by hand; that write follows the end list and is named here so that the check does not read it as unexplained.

## 3. Found, not fixed

- `/usr/local/bin/python3`, first on the PATH of this shell, is Python 3.7.9; `round_record.py run` needs 3.8 or later for its trace, and records a run under 3.7 as "traced in full" although its sitecustomize failed. The round used `/usr/bin/python3` (3.9.6).
- `WHAT_IS_RUNNING.md`'s head still states the three rules of the ledger (write `started` and `finished` entries) while the record is not cut over; the instruction governs, and no entry was written.

## 4. What I could not establish

- The window cannot be produced by `round_record.py window`: it reads the `started` entry from the ledger, and this estate has none. The `window` line is read by `stat` and `date -u` instead, see section 5.
- That no gap's answer appears elsewhere in the register (A5) rests on a reading; no command decides it.

## 5. Corrections to the instruction

- The report form requires the `window` line to be printed by `round_record.py window`, which needs a `started` entry in the ledger; with the record not cut over there is none. The window is opened at the round's first command (`date -u; hostname`, 13:04:44 UTC) and closed at this report's last write, read by `stat` in the same command that made it; the command and its output are kept in `record/window.out`.
- The model line of the instruction names Opus; the session is configured for `claude-opus-5-5`, an Opus model.

## 6. What this round did not finish

Nothing of the task. The review follows, started by this session as a sub-agent once its row is closed.

## 7. The outputs, by path

Taken at Sat Oct 31 13:12:47 UTC 2026, before the report's last write (its `window` line), so the report's own size here is before that write.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/ls_outputs.log`:
```
$ ls -ld "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md"
-rw-r--r--@ 1 arnelaponin  staff  18400 Oct 31 15:09 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md
exit=0
$ ls -ld "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence"
drwxr-xr-x@ 19 arnelaponin  staff  608 Oct 31 15:12 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence
exit=0
$ ls -ld "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md"
-rw-r--r--@ 1 arnelaponin  staff  13150 Oct 31 15:12 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
exit=0
$ ls -ld "/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md"
-rw-r--r--@ 1 arnelaponin  staff  4055 Oct 31 15:05 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md
exit=0
```

Nothing was opened on the owner's screen.
