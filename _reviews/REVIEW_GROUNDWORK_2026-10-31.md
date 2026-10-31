---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md (C-2026-10-31-07)
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GROUNDWORK_2026-10-31.md (C-2026-10-31-08)
written_by: a session that neither wrote nor carried out the instruction — `MR · review · groundwork`, started as a sub-agent with a fresh context by the working session
account: arne.laponin@gmail.com — read from the line of this session's own context that names the user's address
started_by: sub-session — this session's prompt is the review's start message followed by the line that has it load its shell tool
effort: unknown — the sub-agent's prompt does not show the level it was started at; this review's started entry wrongly carries `high` (section 8)
model: claude-opus-5-5 — read from the line of this session's own context that names the model it runs on; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` at 2026-10-31 14:40:47 UTC, this session's first command, through Desktop Commander's `start_process` (zsh)
window: 2026-10-31 14:40:47 UTC to 2026-10-31 14:47:19 UTC — opened at `date -u; hostname`, closed at this file's last write (this line's substitution, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-review/_evidence/window_close.out); no pause
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md, to which the orchestrator appends the gap below
---

# REVIEW — the groundwork of the mini registry (round 2)

Every log below is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-review/_evidence/`, cited by name after this line; each opens with the UTC time of its run. The reviewer's own program is `review_check.py` there (log `R1_review_check.out`, 14:44:45 UTC); the outputs, checksums and times are `R2_outputs.out` (14:45:08 UTC); the mechanical checks `M1` to `M5` (14:43:03 to 14:43:05 UTC), run by `run_mech.sh`.

**In one line:** the content is right — every one of the 50 rows traces to a source the ruling allows, the settings are 17 by the reviewer's own route as by the round's, nothing of the paper's unruled lines is taken, the key table is out of the search's reach and no data is made — but A8 is not met: the round's record check exits 1, reproduced here, and the instruction makes its exit 0 a criterion.

## 1. The tests of success, one by one

| Test | Met | Evidence read by the reviewer |
|---|---|---|
| **A1** set listed first, `0 missing, 0 extra` | **met** | `SETTINGS_SET.md` last written 14:35:29 UTC, `settings.csv` born 14:35:50 UTC (`R2_outputs.out`, birth/modified times), so the set came first. Its 17 rows were read against the brief and the ruled lines; the reviewer's own set (section 2) gives the same 17, 0 missing, 0 extra. |
| **A2** every row traced, `0 without source, 0 unresolved` | **met** | `R1_review_check.out` [2]: every source part of every row is of the three forms, every `brief:<n>` line exists, every `R-<nn>` is a heading of the register, every `ruling:G-<nn>` is G-01 to G-13; and for every row a phrase carrying it is found in the cited text: `rows: settings 17, lists 16, search_rule 17; rows with a source problem: 0; support not found: 0`. |
| **A3** the search rule is the brief's | **met** | `R2_outputs.out`: three `compares` rows — family name, given names, date of birth — one `forgives` (capitals), one `forgives_nothing_else`, `does_not_compare` the school and any other field, `does_not_read` the key table. Brief line 13 «the same family name, given names and date of birth (capitals ignored)» read at its line. |
| **A4** `0 uncovered` | **met** | `R1_review_check.out` [3], the set listed from the register's own headings: 14 requirements, R-02 to R-15; 13 cited by a row, R-02 named in `GROUNDWORK.md` "Requirements the tables do not bear on"; `uncovered: 0`. |
| **A5** the gaps section | **met** | `R2_outputs.out`: 13 numbered gaps, 0 not ending in a question mark. Each read: none is answered in a table (`R1_review_check.out` [4]: no calendar date, no seed, no 64, no field linking a learner to an entry). |
| **A6** sources unchanged | **met** | `R2_outputs.out`: `ec6971e7…1f64` brief, `ad583b39…f103` register, `d03db64c…bb8bb` paper — the three of the instruction's section 2. |
| **A7** placement and trace checks exit 0 | **met** | Rerun here: `M2_placement.out` `placement check: clean` `EXIT=0`; `M1_trace.out` `trace check: clean` `EXIT=0`. |
| **A8** the round's record check exits 0 | **not met** | Rerun here with the round's `# run with:` options: `M3_record_check.out` `EXIT=1`, `## Findings — 10`, every one `read, not on the start list`: `CONSTANTS.md` sought at six folders from `/` to `wai-demo`, `/Users/arnelaponin/_coordination/CONSTANTS.md`, and the layer's `guard_log.py`, `ledger.py`, `placement_check.py`. The report says the same. See G1. |
| **A9** issued, started and finished stand | **met** | `M4_ledger_show.out` prints `20261031T142740Z_MR_issued_…`, `20261031T143024Z_MR_started_…` and `20261031T144026Z_MR_finished_C-2026-10-31-07.yaml`. The report could not show the finished entry; the review does. |

## 2. One figure re-established — the number of settings

**The report's route:** `list_settings_set.py` searched fixed fragments chosen by the round and wrote `SETTINGS_SET.md`; `check_groundwork.py a1` compared it with `settings.csv`. **The route here:** `review_check.py` [1] finds the brief's table by its header row and reads the rows until the table ends (not by line numbers): 5 rows, lines 23 to 27. It finds the ruled text by its own marks — the `| G-nn |` rows under "Summary" and the lines opening `**Recommendation` under each `## G-nn` — 13 questions, 2 lines each (26–38 and 73 … 424), and searches only those. The reviewer listed every value-fixing phrase of those 26 lines with his own words, 20 in all: 13 map to a setting, 7 do not — three named and not fixed (the date of G-06, the order of G-03, the seed of G-10: gaps 1 to 3), two steps of the search (G-02's "never reached", G-07's "all four before the search"), and two values outside the build (G-13's A4 portrait PDF, G-12's R-01 to R-21). **Result:** `reviewer's set: 17 settings; settings.csv: 17 rows; fragments not found in ruled text: 0` and `missing from settings.csv: []; extra in settings.csv: []`. **The two agree.**

Counts and times the report gives in its own words, read at their source: the window opens at the started entry, 14:30:24 UTC (`M4_ledger_show.out`), and closes at 14:40:14 UTC, the report's last modification (`R2_outputs.out`), as declared; 17 / 16 / 17 rows and 13 gaps counted by command (`R1`, `R2`); 14 requirements (`R1` [3]); the four output sizes and checksums match the report's `outputs` line (`R2_outputs.out`).

## 3. The outputs exist

`R2_outputs.out`, one command at 14:45:08 UTC: `GROUNDWORK.md` 6850 bytes `f2284aff…84df9`, `settings.csv` 1127 `a94c31fe…8cfd`, `lists.csv` 2391 `1d08f58c…eef7`, `search_rule.csv` 1335 `9a7c98ce…6fdb` — each the size and checksum the report declares; the evidence folder present with 15 entries; the report itself, 13242 bytes.

## 4. The running application

Not applicable: nothing runs yet; round 2 writes tables, and the build is rounds 5 and 6.

## 5. What a review of this kind runs — the drafting page, part 2

**Every claim looked up at its source.** Each of the 50 rows of the three tables, at its cited lines, for `ruling:G-<nn>` at the summary row and the closing recommendation of that question and nowhere else in the paper (`R1_review_check.out` [2], one line per row with the phrase found). All found. Rows the reviewer weighed beyond the phrase: the list fields `given_names` and `date_of_birth` rest on the brief's line 13 with G-03 («enrols every list entry … through the brief's own rule»), which requires the lists to carry the three compared fields — a reading the ruling carries, not a supplied field; the list `school` is absent and asked as gap 9; `key_table.same_child` cites brief line 54, the rounds table, which is in the brief and states round 7's count.

**The sets listed again and compared.** Settings: 17 against 17, 0 missing either way (section 2). Requirements of A4: 14 against the tables and the document, 0 missing either way (section 1).

**The faults of part 1 read against the tables.** Item 1, a fact the source does not carry: none found — every value is a summary row's or a recommendation's words, and the gaps put the values those lines name but do not fix (gaps 1 to 4) and the details that live only in the unruled "Given to every position" line of G-05 (gap 8). Item 2: not engaged (no earlier gaps). Item 3: not engaged — the groundwork is for the build rounds, not an outside reader. Item 4: the limits the ruling names are carried (G-02 "never reached", the key table "never by the search"). **The three failures of section 7 of the instruction:** the paper read as ruled — no seed, no 64, no check digit, no date, no order of the 8 in any table (`R1` [4]); 64 is put as gap 13 for its unruled line 40. The key table let into the search — no rule row reads it, no row outside the key table names it, and the learners carry no field linking to an entry or key (`R1` [4]); gap 12 asks the question instead. The data made — no name or date in any value or rule (`R1` [4]).

**The outside-reader read:** not applicable, for the reason under item 3.

## 6. The four mechanical checks

| Check | Command (in `run_mech.sh`) | Exit | Lines that decide |
|---|---|---|---|
| trace over the report | `trace_check.py --constants …/mini-registry/CONSTANTS.md --coordination …/_coordination/CONSTANTS.md …/REPORT_GROUNDWORK_2026-10-31.md` | 0 | `outputs: 6 of 6 named exist` · `inputs: 6 of 6 pinned by 20261031T142740Z_MR_issued_C-2026-10-31-07.yaml hash the same now` · `trace check: clean` (`M1_trace.out`) |
| placement over the instruction | `placement_check.py --constants …/mini-registry/CONSTANTS.md …/PROMPT_GROUNDWORK_2026-10-31.md` | 0 | `placement check: clean` (`M2_placement.out`) |
| the round's record | `round_record.py check --record …/round-02-groundwork/_evidence/record --report …/REPORT_GROUNDWORK_2026-10-31.md --tolerance 2 --out …/M3_record_check.check.out` | **1** | `## Findings — 10`, all reads not on the start list; `quoted blocks read against the file they name: 10`; the window `closes at 2026-10-31T14:40:14.000Z` (`M3_record_check.out`, `M3_record_check.check.out`) |
| ledger `show` | `ledger.py show --constants …/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-07` | 0 | issued, started and finished all printed (`M4_ledger_show.out`) |
| ledger `check` | `ledger.py check --constants …/_coordination/CONSTANTS.md` | 0 | `check: clean` — no line names `MR` (`M5_ledger_check.out`) |

**The accounts.** `issued`: `account: arne.laponin@gmail.com`; `started`: `account: arne.laponin@gmail.com`; `finished`: `account: arne.laponin@gmail.com`. The report's declaration: `account: arne.laponin@gmail.com`. All agree. The `started` entry carries `effort: unknown` and `started_by: unknown`, as the report's section 5 and declaration say.

## 7. The verdict — not accepted

**One gap.**

**G1 (other: the round's record check fails on reads by the layer's own program)** — fails **A8**. The instruction's A8: `PROMPT_GROUNDWORK_2026-10-31.md`, section 5 «The round's record check passes: `… round_record.py check --record … --out …/check.out` exits 0.» Rerun here, it exits 1 (`M3_record_check.out`) on 10 reads, none of them a source of the round, all made by `placement_check.py` when the round ran it through `round_record.py run` at 14:37:21 UTC (the report, A8; the instruction's section 4 asks for "your checking programs" to be run through `run`). Nothing in the content turns on it: every other line of the record's check is found as stated. It is not a fault of the drafting page's part 1, and the page does not need it. Its cure lies with the orchestrator: either the next version names on the start list the files the layer's checks read (the coordination's constants and the layer's scripts) or runs the layer's own checks outside `run`, or the layer's `round_record.py` treats the placement check's search for `CONSTANTS.md` up the tree as its own reads. Once the record's check exits 0, nothing else of this review stands in the way.

## 8. Found, not fixed

- **The instruction's line numbers for the outcomes.** `PROMPT_GROUNDWORK_2026-10-31.md`, section 3, item 3: «on none, on exactly one (lines 14 and 15 of the brief)». At the brief, line 13 is "exactly one", line 14 "none" and line 15 "the clerk sees which". The round cited the right lines (`search_rule.csv` rows 14, 15, 18) and did not list the slip under its corrections to the instruction.
- **"No two different children share all three fields"** (`settings.csv` row 13, G-05's recommendation, `GAPS-PAPER.md:196`) does not say whether capitals are ignored in "share"; the paper's unruled setting 3 (`GAPS-PAPER.md:181`) adds «capitals ignored». Round 5 needs to know whether two different children may differ only in capitals (under G-03 the reset would merge them). The groundwork does not raise it among its gaps; a candidate question for the owner, not answered here.
- **The paths of the ledger.** Every entry for C-2026-10-31-07 writes its paths as `~/IdeaProjects/mini-registry/…` and `~/IdeaProjects/brief/…`, while the estate's root is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` (`M4_ledger_show.out`; the constants, section 6). The report's section 3 says so too.
- **The effort of this review — the reviewer's own slip.** This review's started entry, `20261031T144054Z_MR_started_C-2026-10-31-08.yaml`, was written with `--effort high`; the sub-agent's prompt shows no level, so by the review instruction's section 1 it should read `unknown`. The entry is left as written; the finished entry does not carry effort.

Repaired nothing; commissioned nothing; nothing committed; no window opened.
