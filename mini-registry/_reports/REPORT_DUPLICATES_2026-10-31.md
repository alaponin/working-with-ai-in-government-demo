---
kind: report
answers: C-2026-10-31-29
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DUPLICATES_2026-10-31.md
written_by: a working session, "MR · work · the duplicates count", separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt shows only that a scheduled task started it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command after its started entry
window: 2026-10-31 20:19:35 UTC to 2026-10-31 20:25:57 UTC, no pause; closed at the last write of the 31 files the round names as written, REPORT_DUPLICATES_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check. The round's five Python programs (count.py, a3_compare.py, a4_values.py, plant.py, a6_check.py) ran through `run`, traced in full (9 runs). Stage 1's `node reset.js` and `node --test test/`, the sha256 listings (shasum, diff) and the placement and trace checks ran outside `run`, the last two as the instruction says; their logs and the scripts, written with Desktop Commander's write_file or a shell redirection, are in the record's list as "written by no traced run".
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/DUPLICATES.md 3427 bytes sha256 7cd458b0e03accfed051e47249a27eb9f5534a025162b1c5bb78c9d959ed0f88 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/duplicates.csv 888 bytes sha256 5892c7a7093b136e1ff5809eb712eb7b53a787ae8cd6a94599121387622a335e · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/ · this file
ledger: MR C-2026-10-31-29 — the started entry is 20261031T201935Z_MR_started_C-2026-10-31-29.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Count how many of the 8 children on more than one list the prototype's search catches, from what its reset did, each of the 8 with its reason

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md` (C-2026-10-31-29) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`

## 1. The answer first

The search catches 4 of the 8. The reset was run afresh and 57 of 57 checks passed; the key table names 8 children on two list entries each (C19, C24, C26, C31, C50, C53, C56, C58); in the reset's record `enrolments.json` the two entries of C19, C26, C31 and C53 point to one learner each (caught), and those of C24, C50, C56 and C58 to two learners each (missed). Read field by field from the three list files, each of the 4 missed differs between its two entries in the family name only, by one letter (Prarasel/Praresel, Temnok/Tomnok, Orowes/Orowus, Tumitem/Tomitem), and each of the 4 caught matches on all three compared fields letter for letter. The planted faults move the rows and the figure as they must (4, 3 and 5). Nothing under `src/` changed: the reset rewrote `src/data/` byte for byte as it was. The figure agrees with the rulings' prediction, but it is the program's, read from the data.

## 2. The criteria, one by one

### A1 — Stage 1's output quoted, the reset run, 57 of 57: met

Run 20:21:00 to 20:21:02 UTC, outside `run`. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A1_stage1.log`:

```text
started 2026-10-31T20:21:00Z
v20.5.1
reset EXIT=0
# tests 57
# pass 57
# fail 0
test EXIT=0
ended 2026-10-31T20:21:02Z
```

The sha256 of every file of `src/data/` straight after: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/data.after_reset.sha256` (8 files, read 20:21:02 UTC).

### A2 — The set listed first, from key_table.json: met

Run 1 of the record (20:21:38 UTC), before any count; the list kept as `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A2_set.txt`. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A2_set.log`:

```text
key table rows: 68; children named: 60
children named on two or more entries:
  C19  2 entries  school_census:10 · social_grant_list:7
  C24  2 entries  school_census:20 · exam_candidate_list:20
  C26  2 entries  exam_candidate_list:22 · social_grant_list:17
  C31  2 entries  school_census:11 · exam_candidate_list:13
  C50  2 entries  school_census:17 · social_grant_list:19
  C53  2 entries  school_census:13 · exam_candidate_list:8
  C56  2 entries  school_census:22 · social_grant_list:9
  C58  2 entries  exam_candidate_list:14 · social_grant_list:2
count of the set: 8
```

### A3 — One row of duplicates.csv per child of the set, no other: met

The count is run 2 (20:21:50 UTC), which wrote `docs/count/duplicates.csv`; the comparison is run 3 (20:22:41 UTC). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A3_compare.log`:

```text
set: 8 children; csv: 8 rows
missing: -
extra: -
duplicate rows: -
0 missing, 0 extra
```

The count itself, one line per child in the set's order. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A3_count.log`:

```text
enrolments: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/enrolments.json (68 rows)
C19 | school_census:10 · social_grant_list:7 | 10 · 10 | caught=yes | none
C24 | school_census:20 · exam_candidate_list:20 | 20 · 42 | caught=no | family_name: "Prarasel" (school_census:20) vs "Praresel" (exam_candidate_list:20)
C26 | exam_candidate_list:22 · social_grant_list:17 | 44 · 44 | caught=yes | none
C31 | school_census:11 · exam_candidate_list:13 | 11 · 11 | caught=yes | none
C50 | school_census:17 · social_grant_list:19 | 17 · 61 | caught=no | family_name: "Temnok" (school_census:17) vs "Tomnok" (social_grant_list:19)
C53 | school_census:13 · exam_candidate_list:8 | 13 · 13 | caught=yes | none
C56 | school_census:22 · social_grant_list:9 | 22 · 52 | caught=no | family_name: "Orowes" (school_census:22) vs "Orowus" (social_grant_list:9)
C58 | exam_candidate_list:14 · social_grant_list:2 | 36 · 46 | caught=no | family_name: "Tumitem" (exam_candidate_list:14) vs "Tomitem" (social_grant_list:2)
the search catches 4 of the 8
```

No line `ANOMALY` was printed: every entry of the 8 has exactly one row in `enrolments.json`.

### A4 — Every fields_differing value read from the list files, both values quoted: met

A program apart from the count, `a4_values.py`, reads the set from `A2_set.txt` and the three list files by name and prints every compared field of both entries of each child (run 4, 20:22:42 UTC). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A4_values.log`:

```text
C19  school_census:10 · social_grant_list:7
    family_name   "Praquinvel" | "Praquinvel"  -> equal, letter for letter
    given_names   "Joren Kekesa" | "Joren Kekesa"  -> equal, letter for letter
    date_of_birth "2017-04-19" | "2017-04-19"  -> equal, letter for letter
C24  school_census:20 · exam_candidate_list:20
    family_name   "Prarasel" | "Praresel"  -> DIFFERENT
    given_names   "Linbrimel Osrin" | "Linbrimel Osrin"  -> equal, letter for letter
    date_of_birth "2016-03-07" | "2016-03-07"  -> equal, letter for letter
C26  exam_candidate_list:22 · social_grant_list:17
    family_name   "Velnokgal" | "Velnokgal"  -> equal, letter for letter
    given_names   "Tovsan" | "Tovsan"  -> equal, letter for letter
    date_of_birth "2016-10-11" | "2016-10-11"  -> equal, letter for letter
C31  school_census:11 · exam_candidate_list:13
    family_name   "Miquin" | "Miquin"  -> equal, letter for letter
    given_names   "Madanta Celcello" | "Madanta Celcello"  -> equal, letter for letter
    date_of_birth "2019-12-11" | "2019-12-11"  -> equal, letter for letter
C50  school_census:17 · social_grant_list:19
    family_name   "Temnok" | "Tomnok"  -> DIFFERENT
    given_names   "Ostovvin" | "Ostovvin"  -> equal, letter for letter
    date_of_birth "2018-12-10" | "2018-12-10"  -> equal, letter for letter
C53  school_census:13 · exam_candidate_list:8
    family_name   "Orobenwes" | "Orobenwes"  -> equal, letter for letter
    given_names   "Celgrelo Maisa" | "Celgrelo Maisa"  -> equal, letter for letter
    date_of_birth "2014-12-17" | "2014-12-17"  -> equal, letter for letter
C56  school_census:22 · social_grant_list:9
    family_name   "Orowes" | "Orowus"  -> DIFFERENT
    given_names   "Etovn" | "Etovn"  -> equal, letter for letter
    date_of_birth "2020-04-14" | "2020-04-14"  -> equal, letter for letter
C58  exam_candidate_list:14 · social_grant_list:2
    family_name   "Tumitem" | "Tomitem"  -> DIFFERENT
    given_names   "Brihallo Niahaln" | "Brihallo Niahaln"  -> equal, letter for letter
    date_of_birth "2014-04-12" | "2014-04-12"  -> equal, letter for letter
children read: 8
```

The 4 `DIFFERENT` lines are the 4 non-`none` values of `duplicates.csv`, with the same two values; no field of the 8 is equal with capitals ignored only.

### A5 — The planted fault changes the figure and both rows as it must: met

`plant.py` (run 5, 20:22:42 UTC) copied `enrolments.json` three times with `shutil.copyfile`, which keeps no file times, into `_evidence/planted/`, and changed the copies only; the count ran over each (runs 6 to 8). P1 is the instruction's plant; P2 and P3 are its two edits alone, added so that the figure is seen to move, since P1's two edits cancel in the total (section 5). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A5_planted.log`:

```text
P1: social_grant_list:7 learner_number 10 -> 11
P1: exam_candidate_list:20 learner_number 42 -> 20
--- count over planted P1
C19 | school_census:10 · social_grant_list:7 | 10 · 11 | caught=no | none
C24 | school_census:20 · exam_candidate_list:20 | 20 · 20 | caught=yes | family_name: "Prarasel" (school_census:20) vs "Praresel" (exam_candidate_list:20)
the search catches 4 of the 8
--- count over planted P2
the search catches 3 of the 8
--- count over planted P3
the search catches 5 of the 8
--- diff real csv vs P1 csv
< C19,school_census:10 · social_grant_list:7,10 · 10,yes,none
> C19,school_census:10 · social_grant_list:7,10 · 11,no,none
diff EXIT 1
```

Must and did: under P1, C19 goes from caught to missed and C24 from missed to caught, the other 6 rows unchanged (the diff names rows 2 and 3 only), the figure 4 − 1 + 1 = 4; under P2, 3; under P3, 5. Learner 11 is C31's (school census 11, A3).

### A6 — The figure in DUPLICATES.md is the program's output, quoted beside it: met

Run 9 (20:23:28 UTC). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A6_figure.log`:

```text
log's figure line: ['the search catches 4 of the 8']
DUPLICATES.md figure: 4 of 8
figure agrees with log: True
log line quoted in DUPLICATES.md: True
table rows: 8; csv rows: 8; caught=yes in csv: 4; disagreements: 0
```

### A7 — Nothing under src/ changed but src/data/ by the reset: met

Start listing 20:20:59 UTC (`src.start.sha256`, before the reset), end listing 20:23:28 UTC (`src.end.sha256`), after the round's last act on `src/`. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A7_unchanged.log`:

```text
--- every file under src/ but src/data/:
diff EXIT 0
files compared: 16
--- src/data/ (rewritten by the reset):
diff EXIT 0
--- src/data/ after reset against end:
diff EXIT 0
--- sources start against now:
diff EXIT 0
```

The 16 files outside `src/data/` are unchanged; the reset rewrote the 8 files of `src/data/` with the same bytes as before it; the sources (search_rule.csv, QUESTIONS-PAPER.md, the brief, checking.md, the instruction, REQUIREMENTS.md, GOAL.md) are unchanged.

### A8 — Placement and trace checks, outside run, exit 0: met

A first placement run, at 20:23:41 UTC before this report existed (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A8_placement.log`), exited 1 on its one finding, that the report was "named among the outputs and does not exist". Run again once the report was written, at 20:25:13 UTC. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A8_placement_2.log`:

```text
placement check: clean
EXIT 0
```

The trace check over this report, 20:25:13 UTC. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A8_trace.log`:

```text
  agrees: the report answers C-2026-10-31-29, the instruction's commission_id
  agrees: the instruction's downstream_artefact is this report
  outputs: 4 of 4 named exist
  inputs: 9 of 9 pinned by 20261031T201611Z_MR_issued_C-2026-10-31-29.yaml hash the same now
trace check: clean
EXIT 0
```

The trace check names no input changed: the reset of Stage 1 rewrote `enrolments.json` and `learners.json` with the same bytes (A7).

### A9 — The started and finished entries stand: after this report

The `finished` entry is written after this report; `ledger.py show` is kept in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A9_ledger_show.log`.

## 3. Found, not fixed

- The reset's own checks (round 5) already assert the 8 and the 4; this round's count does not lean on them and agrees with them. Nothing to fix.
- Each missed child is held twice: C24 as learners 20 and 42, C50 as 17 and 61, C56 as 22 and 52, C58 as 36 and 46 (A3). Recorded for round 8's note; not a defect, the brief's rule.
- `WHAT_IS_RUNNING.md` names this round's outputs under `~/IdeaProjects/mini-registry/…`, not the estate's root `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`; the paths the ledger renders differ from those the instruction declares. Lives in `ledger.py views`.

## 4. What I could not establish

Nothing asked for is left unestablished.

## 5. Corrections to the instruction

- A5's plant, as written, moves one child each way, so the figure under it is 4 again; "the figure … change as they must" is met by the figure staying 4 while both rows flip. P2 and P3 were added so that the figure is also seen to move (3 and 5).
- Stage 1 names `node reset.js` and `node --test` without saying whether they run through `run`; they ran outside it, as the layer's own checks, and are not traced (node is not a Python program).

## 6. What this round did not finish

Nothing. Round 8's note reads `docs/DUPLICATES.md` and `docs/count/duplicates.csv`.

## 7. The outputs, by path

Taken at 20:25:14 UTC, after the report's first writing; the report's size there is that of its first writing, changed since by the A8 and window lines. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/A10_outputs.log`:

```text
-rw-r--r--@ 1 arnelaponin  staff  3427 Oct 31 22:23 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/DUPLICATES.md
EXIT 0
drwxr-xr-x@ 4 arnelaponin  staff  128 Oct 31 22:21 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count
EXIT 0
-rw-r--r--@ 1 arnelaponin  staff  888 Oct 31 22:21 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/duplicates.csv
EXIT 0
drwxr-xr-x@ 26 arnelaponin  staff  832 Oct 31 22:25 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence
EXIT 0
-rw-r--r--@ 1 arnelaponin  staff  15234 Oct 31 22:24 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md
EXIT 0
```

The times `ls` prints are local (EET, UTC+2). Written after `end`, and so outside the record's end list: `A8_placement_2.log`, `A8_trace.log`, `A10_outputs.log`, `A9_ledger_show.log`, `record/window.out`, `record/check.out` and this report.
