---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md (C-2026-10-31-01)
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_REQUIREMENTS_2026-10-31.md (C-2026-10-31-02)
written_by: a session that neither wrote nor carried out the instruction — `MR · review · register of requirements`, started as a sub-agent with a fresh context by the working session
account: arne.laponin@gmail.com — read from the line of this session's own context that names the user's address
started_by: sub-session — this session's prompt is the review's start message followed by the line that has it load its shell tool
effort: unknown — the sub-agent's prompt does not show the level it was started at
model: claude-opus-5-5 — read from the line of this session's own context that names the model it runs on; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` at 2026-10-31 13:13:24 UTC, this session's first command, through Desktop Commander's `start_process` (zsh)
window: 2026-10-31 13:13:24 UTC to 2026-10-31 13:18:00 UTC — opened at `date -u; hostname`, closed at this file's last write (the substitution of this line, made in the command whose output is kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/window_close.log); no pause
verdict: accepted
downstream_artefact: the orchestrator's closing of C-2026-10-31-01 and of this review — by hand, in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md, because the estate's record is not cut over to the ledger
---

# REVIEW — the register of requirements of the mini registry (round 1)

Every log below is in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/`, each cited once by its full path and by its name after that. The logs were written on MacBookPro between 13:15:10 and 13:16:17 UTC; each opens with the `date -u` of its run.

## 1. The tests of success, one by one

| Test | Met | Evidence read by the reviewer |
|---|---|---|
| **A1** inventory by a saved program, both counts printed | **met** | `split_units.py`, `SENTENCES.md`, `A1_inventory_count.log` exist at their paths (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/outputs_exist.log`); `SENTENCES.md` ends `Units: 29. Marked requirement: 20. Marked not a requirement: 9.`; the round's quoted block of `A1_inventory_count.log` is found in that log by the record's check (M3 below). Program read: it splits prose by sentence, list items and table rows whole, and asserts each unit is a substring of the brief. |
| **A2** both ways, `0 uncited, 0 unsupported` | **met** | Re-established by the reviewer's own program, not the round's: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/review_split.log` — `reviewer's requirement units with no R-: 0`, `R- numbers resting on no reviewer's requirement unit: 0 []`. |
| **A3** every quote a substring of the brief, `0 not found` | **met** | Checked more narrowly than A3 asks — each quote at the very line it cites: `quotes not at their cited line: 0` (`review_split.log`). |
| **A4** every test on a known number states it | **met** | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/register_reads.log`, the `Expected` lines: R-08 `3 lists` (line 121), R-09 `60` (134), R-10 `3` (147), R-11 `8` (160), R-12 `4` (173), R-13 `every age within 6 to 12; children outside: 0` (186), R-14 all five (199). The report's table agrees row for row. |
| **A5** gaps section, each a question, no answer elsewhere | **met** | `register_reads.log`: 14 gaps, none not ending in `?` (grep exit 1); `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/register_reads2.log`: `14`. No answer found in the register by the reviewer's reading of all 23 tests: each that needs a gap's fact names the gap and leaves the value open (R-02 G-08, R-03 G-07, R-06 G-01/G-03, R-09 G-04, R-11 G-05, R-13 G-06, R-16 G-10, R-17 G-09, R-19 G-11, R-22 G-12, R-23 G-13). A reading, as the report says; no command decides it. |
| **A6** brief unchanged | **met** | `outputs_exist.log`, 13:15:45 UTC: `ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64` — the declaration's checksum. |
| **A7** placement and trace checks exit 0 | **met** | Run again by the reviewer: M1 and M2 below, both `clean`, `exit=0`. |
| **A8** the round's record check exits 0 | **met** | Run again by the reviewer: M3 below, `## Findings — 0`, `exit=0`. The round's own `check.out` (13:13:00.616Z, after the window line's write at 13:13:00) also reads `## Findings — 0`. |
| **A9** hand row taken up and closed | **met** | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`, read at 13:13:24 UTC: the row `MR · work · register of requirements` stands in the Closed table, Started `31 Oct 2026, 13:05 UTC`, Closed `31 Oct 2026, 13:13 UTC`, with its outcome line. The taking-up precedes `round_record.py start` (`start.json` mtime 13:05:40 UTC, `register_reads2.log`). The report could only say "met in part" at its writing; the row is now closed. |

Times the report gives in its own words, read at their source (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/window.out` and `register_reads2.log`): run 2 at 13:08:01 = `A1_inventory_count.log` mtime; A2 at 13:10:00 = `A2_A3_compare.log`; A4 at 13:10:33; A7 at 13:12:06; the listing at 13:12:47; the window's close 13:13:00 = the report's mtime and the first line of the record's check (`the window closes at 2026-10-31T13:13:00.000Z`). All agree.

## 2. One figure re-established

**The figure:** units of the five sections marked requirement — the report's **20** (of 29).
**The report's route:** `split_units.py`, which takes a list item whole, lists headings as units, and reads dispositions from the round's own `dispositions.tsv`.
**The reviewer's route:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/review_split.py`, written for this review: it finds the five sections itself, counts no heading and no header row, splits **every** sentence, inside list items too, and carries the reviewer's own disposition of each sentence, typed by hand from the brief read line by line (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/brief_numbered.log`).
**Result** (`review_split.log`, 13:15:10 UTC):

```
reviewer's units (sentences, list-item sentences, data rows; no headings): 26
reviewer's units marked requirement: 23; not: 3
round's inventory units: 29; marked requirement: 20
round's register requirements: 23
```

**They agree.** 23 sentence-level requirement units = the round's 20 units + 3, because the three "must not" items (lines 33, 34, 35) are two sentences each; 26 = 29 − 5 headings − 1 header row + 3. The 23 sentences match the 23 requirements one to one: the two sentences of line 33 → R-16 and R-17, of line 34 → R-18 and R-19, of line 35 → R-20 and R-21 (`register_reads2.log`, the six `Requirement.` lines). The three units both sides mark not a requirement are U-02, U-04, U-05; dispositions differing: 0.

## 3. The outputs exist

One command at 13:15:45 UTC, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/outputs_exist.log`:

```
-rw-r--r--@ 1 arnelaponin  staff  18400 Oct 31 15:09 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md
ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103  /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md
drwxr-xr-x@ 19 arnelaponin  staff  608 Oct 31 15:13 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence
-rw-r--r--@ 1 arnelaponin  staff  14860 Oct 31 15:13 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
```

The register at the size and checksum the report declares; the evidence folder, its `record/RECORD.txt`, `SENTENCES.md`, `split_units.py`, `compare_register.py`, `dispositions.tsv`, `record/check.out` and `record/window.out` each found (exit 0 each); the report at 14860 bytes, the size `window.out` gives after its last write.

## 4. The running application

Not applicable: round 1 wrote no application model; its one output beside its evidence is a document.

## 5. What a review of this kind runs — the drafting page, part 2

Page: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md`. The kind has no skill and no program of its own; the checks are run by the reviewer's program (section 2) and by reading.

- **Every claim looked up at its source.** Each of R-01 to R-23 found at the brief's line it cites: `quotes not at their cited line: 0` (`review_split.log`). Each requirement sentence read against its unit: none says more than its unit, with the two readings named under section 8.
- **The set listed again and compared row by row, both ways.** Reviewer's set → inventory: `missing from the inventory: 0`, `dispositions differing: 0`; → register: `requirement units with no R-: 0`. Inventory → reviewer's set: 6 units unmatched, all headings or the header row, `of which marked requirement: 0`. Register → reviewer's set: `R- numbers resting on no reviewer's requirement unit: 0`. Missing on either side: **0**.
- **Outside reader's words.** Not applicable: the register is read by later rounds of this project, not by an outside reader; the note of round 8 is.
- **The faults of part 1, read against the register.** (1) No fact supplied: the open questions are raised as G-01 to G-14, not filled. (2) Not applicable: no earlier review. (3) Not applicable, as above. (4) The brief's limits marked not a requirement ("The prototype is for agreement.", "It is not the registry.") are in the report's list of what was left out, with the reason (report §1; `SENTENCES.md` U-04, U-05); the inventory was written (13:08:01) before the register (13:09:34).
- **The three failures of the instruction's section 7.** *The search rule widened:* not found. `register_reads.log`, a search of the register for `capital|ignor|accent|diacrit|space|spell|forgiv|fuzzy|similar|normal|trim|whitespace|letter`, returns R-05's rule word for word with "capitals ignored" and nothing else forgiven; R-05's test varies capitals only; R-06's test (b) expects a family name one letter different to get a **new** learner (learners added: 1), which holds the rule narrow; R-12 counts the 4 in the data and says the search's catch is not tested. *Data and prohibitions dropped:* not found — every table row (R-09 to R-13), both sentences of line 29 (R-14, R-15) and all six "must not" sentences (R-16 to R-21) carry a requirement and a test. *A test that restates its requirement:* not found — 23 of 23 tests have the three parts (`register_reads.log`: 23 `Set up`, 23 `Do`, 23 `See`), each naming what is entered, the state of the data and what is seen; the weakest, R-16, names its sources and leaves its evidence to G-10.

## 6. The four mechanical checks

Run under `python3` as the instruction writes them, which on this shell is `/usr/local/bin/python3` 3.7.9 (`M1_trace_check.log`).

| Check | Exit | Log | Lines that decide |
|---|---|---|---|
| M1 `trace_check.py` over the report | 0 | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/M1_trace_check.log` | `agrees: the report answers C-2026-10-31-01` · `outputs: 3 of 3 named exist` · `trace check: clean` |
| M2 `placement_check.py` over the instruction | 0 | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/M2_placement_check.log` | `in its place: …REPORT_REQUIREMENTS_2026-10-31.md — a report` · `placement check: clean` |
| M3 `round_record.py check`, with the options of the round's `check.out` line `# run with:` (`--tolerance 2`), `--out` sent to this review's folder so as not to overwrite the round's evidence | 0 | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/M3_round_record_check.log`, output `M3_check.out` beside it | `## Findings — 0` · `quoted blocks read against the file they name: 8` |
| M4 `ledger.py check` | 1 | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/M4_ledger_check.log` | `not-cut-over: MR — the taken-up entry names …/WHAT_IS_RUNNING.md, which carries no markers — the orchestrator runs views --cut-over MR (section 6)` · `check: 1 defect` |

M4's one defect is the line naming `MR`, quoted whole above: the estate's record is not cut over, which the instruction's `running_record` line declares. It is the estate's state, not a fault of the round. `ledger.py show` has nothing of this task; in its place the hand row is judged under A9: taken up (13:05 UTC) and closed (13:13 UTC). No account is carried by a hand row; the report's `account` is `arne.laponin@gmail.com`.

## 7. The verdict

**Accepted.** Every test of success A1 to A9 is met on evidence the reviewer read or produced; the count of requirement units, re-established by another split and another hand's dispositions, agrees with the report's (20 units, 23 sentences, 23 requirements, nothing missing on either side); the drafting page's part 2 and the three failures of section 7 find no fault; the trace, placement and record checks exit 0, and the ledger check's one defect is the declared absence of the cut-over. Gaps: 0. Count by kind: none.

## 8. Found, not fixed

1. **G-14 asks a question the brief's words already settle.** The brief, line 13: "if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored)"; the register's G-14: "The brief forgives capitals only: does it mean the search to treat a space before or after a name, or between given names, as part of the name?" No test needs it (R-05's test varies capitals only), so it is not a gap in the instruction's sense, and as an open question it invites round 2 or 3 to widen the rule. Not a fault of A5 or of section 7, since nothing in the register forgives spaces; a ruling for the orchestrator.
2. **R-05's test reads "enters nothing new" as the count of learners unchanged.** A prototype that wrote some other record on a found learner would pass. Round 3, the goal in full, may want it tighter.
3. **R-01's "small" is untested**, and R-14's requirement ("the data holds them every time") leans on the next sentence of line 29, which R-15 carries; neither says more than the brief, but the two overlap.
4. **`python3` on this shell is 3.7.9.** The four checks ran under it; the round found `round_record.py run` needs 3.8 for its trace. The instructions' commands do not name the interpreter.
5. **The round's outputs are not committed** (`register_reads2.log`: `?? docs/REQUIREMENTS.md`, `?? _reports/…`, ` M WHAT_IS_RUNNING.md`). The history is local and the commit is the owner's.
6. **This review ran `round_record.py check` with its own `--out`**, departing from the round's `# run with:` line in that one option, so that the round's `record/check.out` stays as the round wrote it.
