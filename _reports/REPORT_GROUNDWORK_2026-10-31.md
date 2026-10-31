---
kind: report
answers: C-2026-10-31-07
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31.md
written_by: a working session (MR · work · groundwork), separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt is the start message delivered by a scheduled task; it does not show who typed or pasted it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command after its started entry
window: 2026-10-31 14:30:24 UTC to 2026-10-31 14:40:14 UTC, no pause; closed at the last write of the 19 files the round names as written, REPORT_GROUNDWORK_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md 6850 bytes sha256 f2284affe810c2886d8a1899681e3d16af96a547dea10f7acc6bcbfca2584df9 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/settings.csv 1127 bytes sha256 a94c31fe9fc96410910e425b1a0dfc708ea6acf09f3fb9ab1c990e71f8ef9cfd · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/lists.csv 2391 bytes sha256 1d08f58c5ea6d1caddfed7f6266800083bed696e7cd1b76c6efc53be72c9eef7 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/search_rule.csv 1335 bytes sha256 9a7c98ce9b57dde82ccca48c84c638b7efd5c08f26f1677e738ecc8d00386fdb · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/ · this file
ledger: MR C-2026-10-31-07 — the started entry is 20261031T143024Z_MR_started_C-2026-10-31-07.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write the groundwork of the mini registry: the settings, the lists and the search rule, as tables the build reads, every row traced to its source

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md` (`C-2026-10-31-07`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`, every program with `/usr/bin/python3` (3.9.6)

## 1. The answer first

The groundwork is written: `settings.csv` 17 settings, `lists.csv` 16 fields over five tables (the three lists, the learners, the key table), `search_rule.csv` 17 rows, and `GROUNDWORK.md` with one section per table and 13 gaps against the sources, each a question left open. Every row names its source as `brief:<line>`, `R-<nn>` or `ruling:G-<nn>`, and a program finds 0 without source and 0 unresolved. The set of settings was listed first from the brief's table (lines 23 to 27) and the ruled lines of the paper (the summary rows, lines 26 to 38, and the thirteen recommendation sentences) and matches `settings.csv` with 0 missing and 0 extra. The search rule compares the brief's three fields of line 13, forgives capitals and nothing else, does not compare the school and does not read the key table. Three values the ruling names but does not fix are gaps, not rows: the date ages are reckoned on (G-06), the order of the reset's enrolment (G-03) and the seed (G-10). The paper's figure of 64 learners after reset stands on its line 40, which is not ruled, and is put as a gap. A1 to A7 are met. A8 is not met: the record's check exits 1 on 10 reads by the layer's placement check of files not on the start list, none of them a source of the round.

## 2. The criteria, one by one

### A1 — The set of settings, listed first — met

`list_settings_set.py` wrote `SETTINGS_SET.md` at 14:35:29 UTC, before the first table was written (the record lists `settings.csv` as last changed 14:35:50 UTC). It checks every fragment a setting rests on at its line. Its log, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A1_list.out`:

```
settings in the set: 17; fragments not found: 0
```

The comparison, `check_groundwork.py a1`, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A1_check.out`:

```
set 17, settings.csv 17 rows
0 missing, 0 extra
```

`SETTINGS_SET.md` sections 4 to 6 also list what the ruled lines fix that is not a setting (G-01, G-02, G-03, G-05 and G-07, placed in the lists or the search rule), the six questions that fix no value the tables carry (G-08 to G-13), and the three values named and not fixed (G-06, G-03 and G-10).

### A2 — Every row traced — met

`check_groundwork.py a2` reads the three CSVs. For each row it checks the form of every part of `source`, that a brief line exists and carries every number of a setting's value, that an `R-<nn>` is a heading of the register, and that a `G-<nn>` is one of G-01 to G-13. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A2_check.out`:

```
settings.csv: 17 rows
lists.csv: 16 rows
search_rule.csv: 17 rows
0 without source, 0 unresolved
```

### A3 — The search rule is the brief's — met

`check_groundwork.py a3`, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A3_check.out`:

```
compares: ['family name', 'given names', 'date of birth']
forgives: ['capitals: two values that differ in capitals only are the same']
forgives_nothing_else: ['every difference but capitals makes two values differ']
does_not_compare: ['school: entered and saved, never searched on', 'any field but the three compared']
does_not_read: ['the key table']
compared fields: 3; forgiven: 1; school compared: no; key table read: no; failures: 0
```

### A4 — The requirements the build reads are covered — met

`check_groundwork.py a4` lists the requirements under the register's headings "What it must do" and "The made-up data, in known numbers", 14 in all, R-02 to R-15. Thirteen are cited by a row, and R-02 is named in `GROUNDWORK.md`, "Requirements the tables do not bear on", with its reason. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A4_check.out`:

```
  R-02: named in GROUNDWORK.md
0 uncovered
```

### A5 — The gaps section — met

`check_groundwork.py a5` finds the section, counts its numbered gaps, checks that each ends in a question mark, and searches the three tables for eight marks of an answer (a calendar date, a seed, an order of the lists, a first number, 64, a spread per list or per school, a key's form, a field linking a learner to its entries). Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A5_check.out`:

```
gaps: 13; not a question: 0; probes for an answer in a table: 8, found: 0 []
```

### A6 — The three sources unchanged — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A6_shasum.out`:

```
ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64  brief/MINI-REGISTRY-BRIEF.md
ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103  mini-registry/docs/REQUIREMENTS.md
d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb  mini-registry/docs/GAPS-PAPER.md
```

These are the three checksums of the instruction's section 2. The record's list of reads gives the same checksums at the start and at the end for all three.

### A7 — Placement and trace checks — met

The placement check's first run, at 14:37:20 UTC before this report existed, exited 1 on the report missing (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A7_placement.out`). Run again once the report was written, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A7_placement_2.out`:

```
placement check: clean
EXIT=0
```

The trace check over this report, log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/A7_trace.out`:

```
  outputs: 6 of 6 named exist
  inputs: 6 of 6 pinned by 20261031T142740Z_MR_issued_C-2026-10-31-07.yaml hash the same now
trace check: clean
EXIT=0
```

### A8 — The round's record check — not met

`round_record.py check` over this report exits 1, with 10 findings, at its run of 14:39:39 UTC; it is run again as the round's last act before the `finished` entry, and that run's output stands in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record/check.out`. Every finding is a read by the layer's `placement_check.py`, run through `round_record.py run` at 14:37:21 UTC, of a file not on the start list: `CONSTANTS.md` looked for at six folders from `/` up to `wai-demo`, where none exists, three of the layer's own scripts, and `/Users/arnelaponin/_coordination/CONSTANTS.md`, which does not exist. No source of the round is among them, and every other line of the check is found as stated: the 3 files written after `end` are named in this report, the four outputs match their declared sizes and checksums, and 10 quoted blocks are found in the logs they name. The cause could not be removed without taking the start list again over files the round had already written, so the criterion is not met as written.

**Written after `end`**, and so not on the record's lists: in the evidence folder, `A7_placement_2.out`, `A7_trace.out` and `ls_ld.out`, and in the record's folder, `window.out` and `check.out`; and this report.

### A9 — The ledger entries — not established in this report

The `finished` entry is written after this report, so `ledger.py show` can only be run after it; the review runs it. The `started` entry stands: `20261031T143024Z_MR_started_C-2026-10-31-07.yaml`, exit 0, 14:30:24 UTC, account `arne.laponin@gmail.com`.

## 3. Found, not fixed

- `WHAT_IS_RUNNING.md`, the Open block, gives this task's files as `~/IdeaProjects/mini-registry/...`, while the estate's root is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` (the constants, section 6). The ledger's one form for paths is `~/IdeaProjects/…` (the procedure, section 9); the produced table does not put the computer's own folder in its place.
- The layer's `placement_check.py`, run through `round_record.py run`, reads `CONSTANTS.md` at six places up the tree from `/`, three of the layer's own scripts and `/Users/arnelaponin/_coordination/CONSTANTS.md`, none of them on the start list: 10 findings of the record (`RECORD.txt`, section 4). They are the layer's program looking for files, not reads of this round's sources.
- The paper's G-05 recommendation refers to "settings 1 to 4 for round 2", which are written out only in the section's unruled "Given to every position" line. The groundwork takes from them only what the recommendation sentence itself says, and puts the rest as gap 8.

## 4. What I could not establish

- Whether the brief's line 19 ("three lists") is meant to be a setting. It is carried in `lists.csv` as the three list tables, not as a row of `settings.csv`, because the set of A1 is the brief's table and the ruled values.
- A9 for the `finished` entry: it is written after this report.

## 5. Corrections to the instruction

- Section 1 asks for the effort to be written as `high` only where the start shows it; the scheduled task shows none, and the `started` entry carries `unknown`.
- The session runs on claude-opus-5-5, the band the instruction names.

## 6. What this round did not finish

Nothing of section 3 is left. The 13 gaps of `GROUNDWORK.md` are left open for the owner's ruling; most of them bear on round 5, which makes the data.

## 7. The outputs, by path

Each place the round wrote in, listed at 14:38:51 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/ls_ld.out`:

```
drwxr-xr-x@ 7 arnelaponin  staff  224 Oct 31 16:36 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs
exit 0
drwxr-xr-x@ 5 arnelaponin  staff  160 Oct 31 16:35 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork
exit 0
drwxr-xr-x@ 17 arnelaponin  staff  544 Oct 31 16:38 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence
exit 0
drwxr-xr-x@ 8 arnelaponin  staff  256 Oct 31 16:37 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record
exit 0
drwxr-xr-x@ 9 arnelaponin  staff  288 Oct 31 16:38 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports
exit 0
```

Nothing was opened on the owner's screen; nothing was committed.
