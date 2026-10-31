---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md (C-2026-10-31-29)
written_by: a session that neither wrote nor carried out the instruction — "MR · review · the duplicates count" (C-2026-10-31-30), a sub-agent with a fresh context
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — read by the command hostname on the computer the session runs on, 2026-10-31 20:26:33 UTC
window: 2026-10-31 20:26:33 UTC to 2026-10-31 20:33:37 UTC, no pause; opens at this review's started entry 20261031T202633Z_MR_started_C-2026-10-31-30.yaml; closed at the moment of writing, the last write of this file, read by stat in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates-review/_evidence/R10_written.log
verdict: accepted
downstream_artefact: the orchestrator's closed entry for C-2026-10-31-30, which closes C-2026-10-31-29 with it (not an increment of a long delivery; no row written)
---

# REVIEW — the duplicates count, round 7

**The verdict: accepted.** The figure holds: by a second route that never read `enrolments.json` or `search.js`, the brief's rule applied to the three list files joins 4 of the 8 children the key table names on two entries — the same four (C19, C26, C31, C53), the same four missed (C24, C50, C56, C58), and the same eight reasons, 0 rows disagreeing. Every test A1 to A9 is met on evidence read here; the planted fault moves the round's own program from 4 to 3; the four mechanical checks are clean. No gap.

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates-review/_evidence/` (cited below by file name in that folder).

## 1. The tests of success, one by one

| Test | Met | Evidence read here |
|---|---|---|
| **A1** reset run, 57 of 57 | met | The round's `A1_stage1.log` read: `reset EXIT=0`, `# tests 57`, `# pass 57`, `# fail 0`, `test EXIT=0`, stamped 20:21:00Z to 20:21:02Z; counted by grep, 57 lines `ok `, 0 lines `not ok`. The reset wrote the 8 files of `src/data/` (log lines 4–12). |
| **A2** the set listed first | met | `A2_set.log` stamped 20:21:38Z; `runs.jsonl` run 1 (`count.py --stage set`) ended 20:21:38.795Z, before run 2 (the count, 20:21:50.917Z). 8 children, 68 rows, 60 children — the same as this review's own listing (`R2_route2.log`: "key table rows: 68; children named: 60", "children on two or more entries: 8"). |
| **A3** one row per child, 0 missing, 0 extra | met | `A3_compare.log`: "0 missing, 0 extra"; `a3_compare.py` read: it compares the set file against the csv both ways and counts duplicate rows. Confirmed independently: `R2_compare.log` "only in route2: -", "only in csv: -". |
| **A4** every `fields_differing` value read from the list files | met | `a4_values.py` read: it reads the list files by name, apart from `count.py`. Its 4 `DIFFERENT` lines are the csv's 4 non-`none` values. Confirmed by this review's own read of the files (`R2_route2.log`, `R9_all_fields.log`: of all four fields, school included, only `family_name` differs, on C24, C50, C56, C58, each at edit distance 1). |
| **A5** planted fault changes figure and both rows | met | `A5_planted.log`: P1 flips C19 to `caught=no` and C24 to `caught=yes` (diff names rows 2 and 3 only), figure stays 4 as the two edits cancel; P2 gives 3, P3 gives 5. The copies in `planted/` exist (5083 bytes each, times 22:22 local, not the original's). Repeated here with a different child (section 2, part 3). |
| **A6** figure in `DUPLICATES.md` is the program's output | met | `A6_figure.log`: "figure agrees with log: True", "log line quoted in DUPLICATES.md: True", 8 rows agree. Read here: `DUPLICATES.md` carries **"The search catches 4 of the 8."** and quotes `the search catches 4 of the 8`, the last line of `A3_count.log`. |
| **A7** nothing under `src/` changed but by the reset | met | `A7_unchanged.log` all four `diff EXIT 0`. Repeated here: the round's `src.start.sha256` (20:20:59Z) against `src/` now, 24 files → `diff EXIT 0` (`R5_outputs_src.log`); 24 − 8 data files = the report's 16. |
| **A8** placement and trace checks exit 0 | met | The round's first placement run exited 1 (report not yet written), the second 0 (`A8_placement_2.log`); trace `A8_trace.log` clean, 9 of 9 pinned inputs unchanged. Both re-run here, clean (section 6). |
| **A9** started and finished entries stand | met | The report says "after this report", which is right for the time it was written; `ledger.py show` run here prints the `issued` (20:16:11Z), `started` (20:19:35Z) and `finished` (20:26:09Z) of version 1 (`M4_ledger_show.log`). |

The report's times and counts given in its own words, read at their source: the window 20:19:35 to 20:25:57 UTC agrees with the started entry's `written` and with the report's mtime (2026-10-31T22:25:57+0200, `R5_outputs_src.log`); "9 runs" = 9 lines of `runs.jsonl`, run times as stated (`R6_record_counts.log`); "31 files the round names as written" = `window.out`'s count; run times for A2 to A6 agree with `runs.jsonl`.

## 2. One figure re-established

**The figure:** "the search catches 4 of the 8", with its eight rows.

**The report's route:** the reset's record `enrolments.json` — a child is caught when both its entries point to one learner number.

**The route taken here:** the rule itself, never its record. `route2.py` (in the evidence folder), run with `/usr/bin/python3 -I`, reads only `key_table.json`, `school_census.json`, `exam_candidate_list.json` and `social_grant_list.json`; takes each child the key table names on two entries; and joins two entries when family name, given names and date of birth are equal with capitals ignored and nothing else forgiven, as `docs/groundwork/search_rule.csv` lines 2–6 give it. It also asks whether two *different* children share the rule's key, which would let a join go to the wrong learner. `R2_route2.log`:

```text
rule keys shared by two or more different children: 0 
C19 | school_census:10 · social_grant_list:7 | yes | none
C24 | school_census:20 · exam_candidate_list:20 | no | family_name: "Prarasel" (school_census:20) vs "Praresel" (exam_candidate_list:20)
C26 | exam_candidate_list:22 · social_grant_list:17 | yes | none
C31 | school_census:11 · exam_candidate_list:13 | yes | none
C50 | school_census:17 · social_grant_list:19 | no | family_name: "Temnok" (school_census:17) vs "Tomnok" (social_grant_list:19)
C53 | school_census:13 · exam_candidate_list:8 | yes | none
C56 | school_census:22 · social_grant_list:9 | no | family_name: "Orowes" (school_census:22) vs "Orowus" (social_grant_list:9)
C58 | exam_candidate_list:14 · social_grant_list:2 | no | family_name: "Tumitem" (exam_candidate_list:14) vs "Tomitem" (social_grant_list:2)
the rule joins 4 of the 8
```

**Beside the round's**, by `compare.py` over this log and `docs/count/duplicates.csv` (`R2_compare.log`): "route2 joined: 4; csv caught=yes: 4", every child `entries:= caught/joined:= fields:=`, "disagreeing rows: 0". **The two routes agree**, on the figure and on all eight rows. The data read is the data the round counted: the 8 files of `src/data/` hash now as in the round's `data.after_reset.sha256` (`R2_compare.log`).

**The planted fault for this route too** (the checking page, part 1, item 1): over copies of the lists in which C26's grant-list family name was changed by one letter and C31's candidate-list family name put in capitals only, `route2.py` gives "the rule joins 3 of the 8", C26 `no`, C31 still `yes` ("equal only with capitals ignored") — `R4_planted.log`. The route can fail, and forgives capitals and nothing else.

**The check repeated on another member** (the checking page, part 2). The report quotes all 8 children's values in A4, so no member is unquoted; two were read here raw from the files by `grep`, apart from every program, one of each outcome (`R3_member.log`): **C26** — `exam_candidate_list.json` lines 150–154 and `social_grant_list.json` lines 115–119 both read "Velnokgal", "Tovsan", "2016-10-11", "Dunavel Lakeside School": the rule joins them. **C56** — `school_census.json` line 151 "Orowes" against `social_grant_list.json` line 60 "Orowus", given names "Etovn" and date "2020-04-14" on both: the rule does not join them. Both agree with the round's rows.

**The planted fault, on the round's program** (the checking page, part 2). `plant_review.py` copied `enrolments.json` with `shutil.copyfile` (no file times kept: the copy reads 22:29 local, the original 22:21) and moved C53's two entries apart — `exam_candidate_list:8` from learner 13 to 9999, a number no entry holds. The round's `count.py`, unchanged (sha256 `c8c0571d…`), run over the real file and then the copy (`R4_planted.log`):

```text
--- round's count.py over the REAL enrolments.json
the search catches 4 of the 8
--- round's count.py over planted Q1
C53 | school_census:13 · exam_candidate_list:8 | 13 · 9999 | caught=no | none
the search catches 3 of the 8
```

The figure changes as it must, and only C53's row. The real files hash the same after the plants.

## 3. The outputs exist

`R5_outputs_src.log`, 20:29:58 UTC: `docs/DUPLICATES.md` 3427 bytes, sha256 `7cd458b0…0f88`; `docs/count/duplicates.csv` 888 bytes, sha256 `5892c7a7…335e` — both as the report declares; `_working/round-07-duplicates/_evidence/` a folder of 25 entries, every log the report cites present; the report itself, 16579 bytes now (15234 at the round's A10 listing, written further after it, as the report says).

The sentence in `DUPLICATES.md` on what the figure shows and does not was read against its sources (`R7_sources.log`, `R8_quotes.log`): brief line 7 "The prototype is for agreement. It is not the registry", line 13 the rule, line 26 "whose family name is spelt differently on one list" (R-12, `docs/REQUIREMENTS.md:162`), and the three phrases given as F-5's at `docs/GOAL.md:105` — each found word for word.

## 4. The running application

Not applicable: the round wrote no application model; it counted from the reset's data. What a program can run was run here: the round's counting program, over the real data and a planted copy (section 2).

## 5. What a review of this kind runs, from the page of the kind

`kind_of_work: checking`; the page, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md`, part 2 names three things, each run here (section 2): the figure by a route the report did not use (agrees, 4 of 8); the check repeated on another member (C26 joined, C56 not, as the round says); the planted fault (4 → 3). The kind has no skill and no program of its own; the programs were this review's and the round's, the round's run unchanged.

The faults of part 1, read against the report: (1) the plant was made and seen to move the figure, in the round and here; (2) the set was listed from `key_table.json` before any count (run 1 before run 2) and counted both ways (A3); (3) each reason was read against the list files (A4), and re-read here; (4) the count ends at the real data the reset wrote afresh, 57 of 57; (5) nothing checked was changed (A7, repeated). None of the five is shown.

## 6. The four mechanical checks, run by the reviewer

Each run with `/usr/bin/python3` from the orchestrator's `scripts/`, 20:30:45 to 20:30:48 UTC:

- **Trace** over the report, with `--constants` the project's and `--coordination` the estate's: `trace check: clean`, `EXIT 0`; "outputs: 4 of 4 named exist", "inputs: 9 of 9 pinned by 20261031T201611Z_MR_issued_C-2026-10-31-29.yaml hash the same now" — `M1_trace.log`.
- **Placement** over the instruction under review: `placement check: clean`, `EXIT 0` — `M2_placement.log`.
- **Round record** — `round_record.py check --record …/round-07-duplicates/_evidence/record --report …/REPORT_DUPLICATES_2026-10-31.md --tolerance 2`, the options of the round's `check.out` `# run with:` line, with `--out` this review's `M3_round_record_check.out`: "## Findings — 0", "quoted blocks read against the file they name: 11", `EXIT 0` — `M3_round_record.log`. It names this review's own files and the round's `A9_ledger_show.log` as "added after the window closed, by another hand or later", as they are.
- **Ledger** `show --code MR --id C-2026-10-31-29` prints the `issued`, `started` and `finished` of version 1, `EXIT 0` — `M4_ledger_show.log`; `check` prints `check: clean`, `EXIT 0`, and no line naming `MR` — `M5_ledger_check.log`.

**The account on the three entries:** `issued` `account: arne.laponin@gmail.com`; `started` `account: arne.laponin@gmail.com`; `finished` `account: arne.laponin@gmail.com` — the same as the report's declaration `account: arne.laponin@gmail.com`. No finding.

## 7. The verdict, and what follows from it

**Accepted.** No gap: the figure, the eight rows and the eight reasons hold, by the data and by the rule. The orchestrator writes one `closed` entry for this review, outcome `accepted`, which closes C-2026-10-31-29 with it. The work is not an increment of a long delivery that a record follows; no row is written. The items below become candidate instructions.

## 8. Found, not fixed

- **The round's counting program does not mark a missed child whose fields agree.** Under this review's plant it printed `C53 | … | 13 · 9999 | caught=no | none` with no remark; such a row — the search missing a child whose three fields match — would be a fault of the search, and would pass into `duplicates.csv` with the reason "none". The real data has no such row (route 2: every missed child differs in a field). Candidate: a line `ANOMALY` for it, should the count be run again.
- **The review instruction's "two of the 8 the round did not quote" had no member:** the report quotes all 8 in A4. Two were read raw here instead (section 2).
- **The ledger renders the estate under `~/IdeaProjects/mini-registry/…`** in `show` (`instruction:`, `report:`, `outputs:`, `inputs:`), while the instruction declares `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`; `show` resolves them "on disk" all the same. The report names the same in `WHAT_IS_RUNNING.md`. It lies in `ledger.py`, not in the round.
- **The round's started entry carries `effort: unknown` and `started_by: unknown`**, as its instruction allows for a session that sees only that a scheduled task started it; this review's own is `--effort unknown --started-by sub-session`.
- **The trace check over this review** (`M6_trace_review.log`, run before the window line was set) prints one finding, `input-changed`, on the report: "absent at issue (20261031T201612Z_MR_issued_C-2026-10-31-30.yaml), sha256:7a0845ef1300 at start, sha256:7a0845ef1300 now". That is the report coming into being after the review was issued, as the review form says (part two, "The report did not exist when this instruction was written"); it hashes the same at this review's start and now. The program reads it as a change; it lies in `trace_check.py`, not in the round or this review.
- **The model:** this review ran on claude-opus-5-5, the band (Opus) the review instruction names; the effort it ran at is not shown to it.
