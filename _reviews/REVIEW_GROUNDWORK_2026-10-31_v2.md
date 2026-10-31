---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md (C-2026-10-31-07, version 2)
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GROUNDWORK_2026-10-31.md (C-2026-10-31-08, version 2)
written_by: a session that neither wrote nor carried out the instruction — `MR · review · groundwork`, started as a sub-agent with an empty memory by the working session of version 2; it did not write or review the first edition
account: arne.laponin@gmail.com — read from the line of this session's own context that names the user's address
started_by: sub-session — this session's prompt is the review's start message followed by the line that has it load its shell tool
effort: unknown — the sub-agent's prompt does not show the level; this review's started entry wrongly carries `high` (section 8)
model: claude-opus-5-5 — read from the line of this session's own context that names the model it runs on; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` at 2026-10-31 14:57:49 UTC, this session's first command, through Desktop Commander's `start_process` (zsh)
window: 2026-10-31 14:57:49 UTC to 2026-10-31 15:02:23 UTC — opened at `date -u; hostname`, closed at this file's last write (this line's substitution, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2-review/_evidence/window_close.out); no pause
verdict: accepted
downstream_artefact: the orchestrator's `closed` entry for C-2026-10-31-08, which closes C-2026-10-31-07 with it
---

# REVIEW — the groundwork of the mini registry, version 2

Every log below is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2-review/_evidence/`, cited by name after this line; each opens with the UTC time of its run. The mechanical checks, the outputs and the re-runs are made by `run_mech.sh` there (logs `M1` to `M5`, `R2_outputs.out`, `B3_rerun.out`, 14:59:43 to 14:59:44 UTC, last run of the script); the figure re-established and gap 14's tracing by `F1_count.sh` (log `F1_count.out`, 15:01:19 UTC).

**In one line:** G1 is closed — the record check of version 2 exits 0 when run here, 0 findings — and nothing in the groundwork changed but the added gap 14, which quotes its three sources exactly and answers nothing; B1 to B6 and A9 are met.

## 1. The tests of success, one by one

| Test | Met | Evidence read by the reviewer |
|---|---|---|
| **B1** CSVs unchanged, `GROUNDWORK.md` changed by gap 14 alone | **met** | `R2_outputs.out`: against the checksums the first edition recorded (its `R2_outputs.out`, 14:45:08 UTC), `same docs/groundwork/settings.csv a94c31fe`, `same … lists.csv 1d08f58c`, `same … search_rule.csv 9a7c98ce` (full 64 characters equal), `CHANGED docs/GROUNDWORK.md f2284aff -> 5ed9b62f`. The round's copy `GROUNDWORK_v1.md` has the first edition's checksum `f2284aff…84df9`, 6850 bytes; its `diff` against the file now is one hunk, `55a56`, the one line of gap 14, `diff EXIT=1`. The round's own `before.sha256`/`after.sha256` read here differ in `GROUNDWORK.md` and their date lines only. |
| **B2** gap 14 a question quoting the ruled words and line 13, answering nothing | **met** | Gap 14 read in full (`GROUNDWORK.md` line 56). `F1_count.out`: each quotation found at its source line, 1 · 1 · 1 — "no two different children share all three fields" at `GAPS-PAPER.md:196` (G-05's recommendation), "the same family name, given names and date of birth (capitals ignored)" at brief line 13, "through the brief's own rule" at `GAPS-PAPER.md:133` (G-03's recommendation). It ends asking which of two readings holds and takes neither; 14 numbered gaps, 0 not ending in `?`; the three CSVs carry neither "share" nor "capitals ignored" (`grep EXIT=1`), and they are unchanged (B1). Its inference — that the reset would merge two children differing in capitals only — follows from line 13 ("shows that learner and enters nothing new") with G-03, and is stated as the reason for the question, not as an answer. |
| **B3** the checks of A2, A3, A4 print as for version 1 | **met** | Re-run here, outside any record, from version 1's evidence folder (`check_groundwork.py` read first: it only reads files): `B3_rerun.out` — `a2`, `a3`, `a4` each `EXIT=0`, and each output `diff` against version 1's log less its two header lines `EXIT=0`. `B3_a4.out` ends `0 uncovered`; `B3_a2.out` `0 without source, 0 unresolved` over 17, 16, 17 rows; `B3_a3.out` `compared fields: 3; forgiven: 1; school compared: no; key table read: no; failures: 0`. The round's own runs stand in its `runs.jsonl`: 3 runs, 14:54:45.824Z to 14:54:46.657Z, exit 0. |
| **B4** placement and trace checks, outside `run`, exit 0 | **met** | Run here: `M2_placement.out` `placement check: clean` `EXIT=0`; `M1_trace.out` over the v2 report `trace check: clean` `EXIT=0`. The round's first placement run (`B4_placement.out`) exited 1 on the report not yet written, the case B4's parenthesis allows. The round's `RECORD.txt` section 3 lists 3 runs, all `check_groundwork.py`: neither layer check ran through `run`. |
| **B5** the record check exits 0 | **met** | Run here with the options of the round's `check.out` line `# run with:` and an `--out` of my own: `M3_record_check.out` `## Findings — 0` `EXIT=0`. G1 is closed. |
| **B6** the three sources unchanged | **met** | `R2_outputs.out`: `ec6971e7…1f64` brief, `ad583b39…f103` register, `d03db64c…bb8bb` paper — the three of the instruction's section 2. |
| **A9** issued, started and finished stand, for version 2 | **met** | `M4_ledger_show.out`: `20261031T145031Z_MR_issued_C-2026-10-31-07.yaml` (version 2), `20261031T145311Z_MR_started_…` (version 2), `20261031T145727Z_MR_finished_C-2026-10-31-07.yaml` (version 2), beside the three entries of version 1. Accounts in section 6. |

## 2. One figure re-established — the number of settings

**The round's route** (version 1, standing for version 2): `list_settings_set.py` searched fragments it chose and wrote `SETTINGS_SET.md`; `check_groundwork.py a1` compared. **The first edition's route:** a program finding the brief's table by its header row and the ruled lines by their marks. **The route here:** neither program — I read the brief's lines 23 to 27 and the 13 ruled lines (the summary rows 26–38 and the recommendations at 73 … 424, whose line numbers `F1_count.sh` lists by grep) and wrote by hand, in `F1_reviewer_settings.tsv`, one row per value those lines fix: the setting, the one line it rests on and the phrase there. `F1_count.sh` then checks each phrase with `grep -F` at that single line and sets the names beside `settings.csv`. Left out by reading, as not settings of the build: G-02's "never reached" and G-07's "all four entered before the search runs, the school not searched on" (steps of the search, in `search_rule.csv`); the date of G-06 and the seed of G-10 (named, not fixed: gaps 1 and 3); G-12's R-01 to R-21 and G-13's A4 page (outside the tables). **Result** (`F1_count.out`): `reviewer's list: 17 settings; phrases not found at their line: 0` · `settings.csv: 17 rows` · `missing from settings.csv: 0` · `extra in settings.csv: 0`. **The two agree.**

Counts and times the report gives in its own words, read at their source: the window opens at the started entry, 14:53:11 UTC (`M4_ledger_show.out`), and closes at 14:57:16 UTC, the report's last modification (`R2_outputs.out`, `14:56:20 / 14:57:16`); `before.sha256` at 14:54:03 and `after.sha256` at 14:55:27 UTC, read in the files; `GROUNDWORK_v1.md` written at 14:54:16.747Z, after the start list of 14:54:16.602Z (`RECORD.txt`), as "just after `start`" says; `RECORD.txt` header `start list: 226 files; end list: 233 files; runs traced: 3`, section 2 `— 7` reads each `yes`, `## 4. Findings — 0`, as the report says; `GROUNDWORK.md` 7429 bytes `5ed9b62f…`, as its `outputs` line says.

## 3. The outputs exist

`R2_outputs.out`, one block at 14:59:44 UTC: `docs/GROUNDWORK.md` 7429 bytes `5ed9b62f…5dce`; the evidence folder `round-02-groundwork-v2/_evidence` present, 16 entries; the report itself, 11106 bytes. The three CSVs, which version 2 did not name as outputs, are present at their first edition's sizes and checksums. `M1_trace.out`: `outputs: 3 of 3 named exist`.

## 4. The running application

Not applicable: nothing runs yet; round 2 writes tables, and the build is rounds 5 and 6.

## 5. What a review of this kind runs — the drafting page, part 2

**Every claim looked up at its source.** The first edition's tracing of the 50 rows stands (its section 5); no row of the tables changed (B1), so none is re-traced. The one line that differs, gap 14, is traced in B2: its three quotations at `GAPS-PAPER.md:196`, brief line 13 and `GAPS-PAPER.md:133` — the first and third ruled recommendations, the second the brief — and nothing taken from an unruled line of the paper.

**The sets listed again and compared.** Settings: 17 against 17, 0 missing either way (section 2). Requirements of A4: re-run, 14 requirements, `0 uncovered` (B3).

**The faults of part 1 read against what changed.** Item 1, a fact the source does not carry: gap 14 supplies none; it raises the question the first edition found, against the ruling, as the page requires. Item 2: the first edition's gap G1 was a single gap with no set of examples; the round closed it by its cause (the layer checks run outside `run`), and the record check now exits 0. Items 3 and 4: not engaged, as in the first edition. **The three failures of section 7 of the instruction:** the paper read as ruled — gap 14 quotes only ruled lines and the brief; the key table let into the search — no table changed, and `B3_a3.out` `key table read: no`; the data made — no name or date in gap 14.

## 6. The four mechanical checks

| Check | Exit | Lines that decide |
|---|---|---|
| trace over the v2 report (`M1_trace.out`) | 0 | `outputs: 3 of 3 named exist` · `inputs: 6 of 6 pinned by 20261031T145031Z_MR_issued_C-2026-10-31-07.yaml hash the same now` · `trace check: clean` |
| placement over the instruction (`M2_placement.out`) | 0 | `in its place: …/REPORT_GROUNDWORK_2026-10-31_v2.md — a report` · `placement check: clean` |
| the round's record, `--tolerance 2` from its `# run with:` (`M3_record_check.out`, `M3_record_check.check.out`) | 0 | `## Findings — 0`; `the window closes at 2026-10-31T14:57:16.000Z`; `quoted blocks read against the file they name: 8`; the files this review wrote are listed as `added after the window closed … by another hand or later`, not as findings |
| ledger `show` (`M4_ledger_show.out`) | 0 | issued, started and finished of version 2 all printed, with version 1's three |
| ledger `check` (`M5_ledger_check.out`) | 0 | `check: clean` — no line names `MR` |

**The accounts.** Version 2's `issued`: `account: arne.laponin@gmail.com`; `started`: `account: arne.laponin@gmail.com`; `finished`: `account: arne.laponin@gmail.com`. The report's declaration: `account: arne.laponin@gmail.com`. All agree. The `started` entry carries `effort: unknown` and `started_by: unknown`, as the report's declaration says.

## 7. The verdict — accepted

**No gap.** G1 of the first edition is closed: the record check of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/record` exits 0 when run here. B1 to B6 and A9 are each met on evidence read or produced here; the groundwork is the first edition's, byte for byte, but for gap 14, which is right. The drafting page lacks no fault this review found.

## 8. Found, not fixed

- **G-05's recommendation points at the unruled settings.** `GAPS-PAPER.md:196` reads «with settings 1 to 4 for round 2 — …», and setting 3 of the unruled "Given to every position" line (`GAPS-PAPER.md:181`) reads «no two different children share family name, given names and date of birth, capitals ignored». Gap 14 rightly does not take that line as ruled (the instruction's section 2, item 5), but does not mention that the ruled sentence names it; the owner, ruling gap 14, may want to see both lines side by side.
- **The paths of the ledger.** Every entry of C-2026-10-31-07, version 2 included, writes its paths as `~/IdeaProjects/…` while the estate's root is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` (`M4_ledger_show.out`); the program resolves them "on disk" here. The first edition and the report say the same.
- **The review instruction's version 2 and its sections 3 and 4.** Section 3 names the evidence folder `round-02-groundwork-review` and section 4's `--report` the first edition's file; version 2 names `round-02-groundwork-v2-review` and this edition's file. Version 2 was followed.
- **The effort of this review — the reviewer's own slip, repeated from the first edition.** This review's started entry, `20261031T145749Z_MR_started_C-2026-10-31-08.yaml`, was written with `--effort high`; the prompt shows no level, so by the review form it should read `unknown`. Left as written; the finished entry does not carry effort.

Repaired nothing; commissioned nothing; nothing committed; no window opened.
