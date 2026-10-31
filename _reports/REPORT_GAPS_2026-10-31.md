---
kind: report
answers: C-2026-10-31-03
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31.md
written_by: a working session (MR · work · answers to the register's gaps), separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — read from this session's own prompt, which shows it was started by a scheduled task and not who stored it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command, at 2026-10-31 13:25:50 UTC
window: 2026-10-31 13:25:50 UTC to 2026-10-31 13:34:31 UTC — opened at the round's first command (`date -u; hostname`), closed at this line's own write, the report's last; read by `date -u` and `stat` in one command, because `round_record.py window` needs a started entry in the ledger and this estate has none; the command and its output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md 34390 bytes sha256 d52fd3fcbf25b163b05f0a18cebef001f95fc364c17cf7e53e60216515f811bb · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/ (its files listed with their sizes and checksums in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/RECORD.txt, section 1) · this file
ledger: MR C-2026-10-31-03 — the estate's record is not cut over to the ledger (the instruction's running_record line names a row added by hand); the round took up its row in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 31 Oct 2026, 13:26 UTC, closes it by hand into the Closed table after this report, and writes no ledger entry
---

# ACCOUNT — Write the decision paper that answers the register's open questions G-01 to G-13, each with its positions and a recommendation, for the owner's ruling

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md` (`C-2026-10-31-03`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process` (`mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process`), proved by `date -u; hostname`, which printed `Sat Oct 31 13:25:50 UTC 2026` and `MacBookPro`

## 1. The answer first

The paper stands at `docs/GAPS-PAPER.md`: a summary table, then one section for each of G-01 to G-13, each with the question quoted, the passages of the brief or the register that bear on it (49 in all, each at its line), two or three positions, one table against the four tests (a) to (d), and one recommendation marked as a proposal for the owner's ruling. G-14 is recorded as closed in one line quoting the brief's line 13, "(capitals ignored)". Both checksums of the declaration hold at the end.

What the round found that changes the picture: three questions decide round 7's answer together. The paper recommends that at each reset every list entry is enrolled through the brief's own rule, so the search looks among learners only (G-03); that 60 counts different children, the 8 each on two lists (G-04); and that the made-up data records which entries are the same child in a key table read by the counts and never by the search (G-05). Ruled together, they give round 7 a known answer before it runs — 4 of the 8 caught, the 4 whose family name is spelt differently being missed — and round 5 a known count of learners after reset, 64. The position that would have made round 7's count 8 by construction (a shared key used to join the lists, G-05 Position B) is stated at its strongest and not recommended, with that reason in its table row. No recommendation forgives anything but capitals.

## 2. The criteria, one by one

### A1 — the set: 13 questions listed word for word, each found in the register — met

Program `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/list_questions.py`, run 1 of the record at 2026-10-31 13:28:38 UTC; output `QUESTIONS.md` beside it.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A1_questions.log`:
```
questions in the section: 14
questions listed (G-01 to G-13): 13
exit=0
13
0 not found
```

The `13` is `grep -c` over `QUESTIONS.md`; `0 not found` is a loop of `grep -F` of each quoted question over `docs/REQUIREMENTS.md`.

### A2 — coverage both ways, `0 unanswered, 0 extra` — met

Program `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/check_paper.py`, run 2 of the record at 2026-10-31 13:32:35 UTC. A question counts as answered only where the paper has a section headed by its identifier holding the question, word for word, as a quoted line.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A2_A5_check_paper.log`:
```
A2: questions listed 13, sections in the paper 13
A2: 0 unanswered, 0 extra
```

That the program catches each fault it reports was shown by planting five in a copy (`plant_faults.py`, run 3; the copy `planted/GAPS-PAPER_planted.md`) and running it over the copy (run 4).

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A2_A5_planted.log`:
```
  UNANSWERED G-13
  EXTRA G-15
A2: 1 unanswered, 1 extra
  NOT FOUND paper:47 ../brief/MINI-REGISTRY-BRIEF.md:14 'if it finds none, it gives the pupil a new learner number an'
  WRONG LINE paper:177 ../brief/MINI-REGISTRY-BRIEF.md:26, found at [27]
A3: 1 not found, 1 wrong line
  G-09 1 4 1 (a row's cells do not match the positions)  <-- short
A5: lines closing G-14 with the brief's line 13 quoted: 0
```

### A3 — every passage at its line, `0 not found, 0 wrong line` — met

The same run and log. Every passage of the paper is written `` `<path>:<line>` «<words>» ``; the program reads each, and a passage counts as found only where its words are in the line it names.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A2_A5_check_paper.log`:
```
A3: passages quoted 49
A3: 0 not found, 0 wrong line
```

The questions themselves are quoted as lines beginning `> `; they are checked word for word by A2 and A1, not counted among the 49.

### A4 — at least 2 positions, the 4 rows (a) to (d), 1 recommendation, per question — met

The same run and log. Every row reads at least 2, 4 and 1; the program also checks that each table row has one cell per position.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A2_A5_check_paper.log`:
```
  G-01 3 4 1
  G-02 2 4 1
  G-03 3 4 1
  G-04 2 4 1
  G-05 3 4 1
  G-06 2 4 1
  G-07 2 4 1
  G-08 2 4 1
  G-09 2 4 1
  G-10 2 4 1
  G-11 2 4 1
  G-12 2 4 1
  G-13 2 4 1
A4: questions short of 2 positions, 4 rows (a)-(d) or 1 recommendation: 0
```

13 lines for the set of 13. Where the brief leaves only one reading open, the paper says so rather than inventing a rival: G-06 on whether 6 and 12 are included, and G-10 on comparing with a list of real persons, set aside beside the brief's line 33.

### A5 — G-14 closed in one line quoting line 13; nothing but capitals forgiven — met

The same run and log.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A2_A5_check_paper.log`:
```
A5: lines closing G-14 with the brief's line 13 quoted: 1
A5: sections headed G-14: 0
A5: recommendation sentences naming anything a search could forgive (read each):
  G-05: 'spelt'
decision wording ('the registry will', 'we decide', 'is decided'): 0
```

The one hit was read: G-05's recommendation uses "spelt" to fix that a family name "spelt differently" differs in at least one letter, not in capitals alone — it narrows, and forgives nothing. That no recommendation widens the rule through G-02, G-03 or G-05 is a reading: G-02 enters nothing new in every case; G-03 enrols the lists by the brief's line 13 and no other rule; G-05 keeps the record of sameness out of the search. The program's word list is a screen, not a proof.

### A6 — the brief and the register unchanged — met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A6_checksums.log`:
```
ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64  /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md
ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103  /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md
exit=0
```

The record agrees: both files carry the same checksum at the start and at the end (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/RECORD.txt`, section 2).

### A7 — the placement check and the trace check exit 0

Both run at 2026-10-31 13:34:07 UTC, under `/usr/bin/python3`, after this report's first write. Met.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A7_placement_check.log`:
```
placement check: clean
exit=0
```

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A7_trace_check.log`:
```
  agrees: the report answers C-2026-10-31-03, the instruction's commission_id
  agrees: the instruction's downstream_artefact is this report
  outputs: 3 of 3 named exist
  inputs: the ledger holds no issued entry for /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md; no checksum to compare
trace check: clean
exit=0
```

### A8 — the round's record check exits 0

Command: `/usr/bin/python3 -B round_record.py check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record --report <this report> --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/check.out`. Its output is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/check.out`, written again by each run. The run that decides this criterion is the round's last act before its row is closed, after the `window` line is written; its exit is quoted in the row it closes and read again by the review.

Files written after the end list (2026-10-31 13:33:07 UTC) and named here: this report, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A7_placement_check.log`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/A7_trace_check.log`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/ls_outputs.log`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/window.out`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/check.out`, and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` (its row closed).

### A9 — the row in WHAT_IS_RUNNING.md taken up and closed

The row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` was taken up at 31 Oct 2026, 13:26 UTC (the time `date -u` printed in the same command that wrote it), before `round_record.py start` at 13:26:52 UTC, so the record does not list that write. It is closed into the Closed table by hand after this report and the record's check; that write follows the end list and is named here.

## 3. Found, not fixed

- The register's G-14 stands open in `docs/REQUIREMENTS.md:341` while the orchestrator has closed it; the paper records the closing, and the register, out of scope, is unchanged.
- R-19's test (`docs/REQUIREMENTS.md:264`) reads a list of other bodies; if G-11 is ruled "none", that test passes on an empty list, and round 3 or 4 may want to say so in the test.
- R-05's test (`docs/REQUIREMENTS.md:79`) varies capitals only; if G-03 is ruled as recommended, the reset itself is a run of the search over 68 entries, which round 6 can reuse as a check.
- `WHAT_IS_RUNNING.md`'s head still states the three rules of the ledger while the record is not cut over (noted by round 1 too).

## 4. What I could not establish

- The window cannot be produced by `round_record.py window`: it reads the `started` entry from the ledger, and this estate has none. It is read by `date -u` and `stat` instead (section 5).
- That no recommendation widens the search by the back door (A5) rests on a reading; the program screens words and cannot decide meaning.
- Whether 4 of 8 is round 7's answer depends on the owner ruling G-03, G-04 and G-05 together; on another ruling the paper's figures 64 and 68 fall with it.

## 5. Corrections to the instruction

- The report form requires the `window` line to be printed by `round_record.py window`, which needs a `started` entry in the ledger; with the record not cut over there is none. The window opens at the round's first command (`date -u; hostname`, 13:25:50 UTC) and closes at this report's last write, read by `stat` in the same command that made it; the command and its output are kept in `record/window.out`.
- Section 1 orders the row taken up as the first act and section 4 orders `round_record.py start` before the first write into the estate; the row is in the estate. The row was taken first, as round 1 did, and is named under A9.
- The model line of the instruction names Opus; the session is configured for `claude-opus-5-5`, an Opus model.

## 6. What this round did not finish

Nothing of the task. The owner's ruling on the thirteen recommendations is his; the review follows, started by this session as a sub-agent once its row is closed.

## 7. The outputs, by path

Taken at Sat Oct 31 13:34:07 UTC 2026, before the report's last writes (these sections and its `window` line), so the report's own size here is before them; `WHAT_IS_RUNNING.md` is listed before its row is closed.

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/ls_outputs.log`:
```
-rw-r--r--@ 1 arnelaponin  staff  34390 Oct 31 15:32 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md
exit=0
drwxr-xr-x@ 16 arnelaponin  staff  512 Oct 31 15:34 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence
exit=0
-rw-r--r--@ 1 arnelaponin  staff  11896 Oct 31 15:33 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md
exit=0
-rw-r--r--@ 1 arnelaponin  staff  6657 Oct 31 15:26 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md
exit=0
```

Nothing was opened on the owner's screen.
