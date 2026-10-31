---
kind: instruction
commission_id: C-2026-10-31-29
version: 1
session_name: MR · work · the duplicates count
kind_of_work: checking
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/key_table.json
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/enrolments.json · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/learners.json · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/search.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/reset.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/search_rule.csv · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — round 7 of the brief, the duplicates count: how many of the 8 the search catches
model: Opus — one figure, established from what the prototype's own reset did, with every one of the 8 accounted for and the reason for each; the risk is a figure read from a ruling's prediction rather than from the data
effort: high — the note to the Permanent Secretary quotes this figure, and a figure quoted is the one that must be right
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review counts again by a second route this instruction names, and plants a fault
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DUPLICATES_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/DUPLICATES.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/duplicates.csv · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · the duplicates count
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md
```

---

# INSTRUCTION — Count how many of the 8 children on more than one list the prototype's search catches, from what its reset did, each of the 8 with its reason

**Suggested model: Opus, effort high.** One figure, settled by the data; the risk is inexactness, or the figure taken from a prediction (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · the duplicates count`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run the layer's programs with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-29 --session "MR · work · the duplicates count" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · the duplicates count"
```

A session that can tell only that a scheduled task started it writes `unknown`. Your account is read from your own context only; your computer is what `hostname` prints. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md` — the page of the kind.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`.
5. **The set and its sources:** the 8 are the children the key table, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/key_table.json`, names on two list entries — a child is named by `same_child`, an entry by `list_entry`. What the search did is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/enrolments.json`, the reset's record of which learner each list entry made or found (ruling Q-12). The search itself is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/search.js`, which applies `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/search_rule.csv`. The brief's line 54 names this round. The rulings on Q-5 and Q-8 predict which of the 8 differ and how; **a prediction is not the figure**.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

Record the sha256 of every file in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/` and of the sources as you start.

## 3. The task

**Stage 1 — the data as the reset makes it.** `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node reset.js && node --test test/`: the reset run afresh, every check passing (57 of 57 as accepted). Then record the sha256 of every file in `src/data/` — the data this count reads. Where a check fails, stop here and report it.

**Stage 2 — the set, listed first** (the checking page, item 2): from `key_table.json`, by a program saved in the evidence folder, every child named on two or more entries, each with its entries; count them. Write the list into the evidence folder before counting anything else.

**Stage 3 — the count, by this route:** for each of those children, read in `enrolments.json` the learner number each of its entries made or found. **Caught**: every entry of the child points to one learner. **Missed**: its entries point to two or more. Then, for each child, the reason, read from the list files themselves: which of the three compared fields — family name, given names, date of birth, capitals ignored — differ between its entries, quoting both values.

Write `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/duplicates.csv` — `child,entries,learner_numbers,caught,fields_differing` — one row per child; and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/DUPLICATES.md`: the figure in one line, "the search catches N of the 8", a table of the 8 with the same columns in words, and one sentence on what the figure shows and what it does not, in the words of the brief's and the register's limits (R-12, F-5).

## 4. Constraints and standing rules

- **Change nothing you check** (the checking page, item 5): nothing under `src/` but what the reset itself rewrites in `src/data/`. A defect goes to "found, not fixed".
- **Plant a fault before trusting the figure** (item 1): in a scratch copy of `enrolments.json` in the evidence folder — copied without keeping file times — point one caught child's second entry to another learner, and one missed child's second entry to its first learner; run the counting program on the copy and see the figure and both rows change as they must.
- No figure from memory or from a ruling's prediction; no operation that writes to version control; nothing opens a window.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`; run **your own** programs through `run`; **run the layer's own checks outside `run`**; `end` after your last write but the report; `check` last, before the `finished` entry. Where the record check names reads it cannot attribute to the round, quote it and say so; do not chase them.

## 5. Acceptance criteria

- **A1** — Stage 1's output quoted: the reset run, 57 of 57.
- **A2** — The set listed first: the program prints the children on two or more entries and their count, from `key_table.json`.
- **A3** — Every child of the set has one row of `duplicates.csv`, and no other row: a command compares them → `0 missing, 0 extra`.
- **A4** — Every `fields_differing` value is read from the list files: the report quotes, for each child, the two values of each differing field, by a command that reads them.
- **A5** — The planted fault changes the figure and both rows as it must; the output quoted.
- **A6** — The figure in `DUPLICATES.md` is the program's output, quoted beside it.
- **A7** — Nothing under `src/` changed but `src/data/` by the reset: the sha256 of every other file at the end equals that at the start.
- **A8** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md`. Where the trace check names an input changed that the reset rewrote in Stage 1, say so; it is expected.
- **A9** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-29` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates/_evidence/`, cited by path. Every figure the report gives twice is the same both times, and the `finished` entry's outcome agrees with the report's first paragraph.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md`.

- **The prediction copied.** The rulings say 4; the data says what it says. The figure is the program's.
- **The reset's own test re-quoted.** Round 5's checks already assert the 8 and the 4; this round counts what `enrolments.json` holds, by its own program.
- **A reason guessed.** "Spelt differently" is read field by field from the list files, both values quoted.

## 8. Out of scope — do not touch

Everything under `src/` but what the reset rewrites; the note (round 8); any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-29`. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-29 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md --outcome "<one line: the figure, in the words of the report's first paragraph>" --moved "<docs/DUPLICATES.md and docs/count/duplicates.csv, for round 8's note>" --account <the same account as your started entry> --by "MR · work · the duplicates count"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · the duplicates count
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DUPLICATES_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.
