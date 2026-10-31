---
kind: instruction
commission_id: C-2026-10-31-19
version: 1
session_name: MR · work · the count
kind_of_work: checking
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T181936Z_MR_ruled_D-2026-10-31-07.yaml · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COUNT_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — round 4 of the brief, the count: every requirement against the goal, both ways
model: Opus — the sets are settled and listed by program; the work is reading each requirement's test against every step, failure and screen of the goal, exactly, over a surface of 23 by 19; the risk is a pair missed or asserted without ground
effort: high — every later round, the build of round 6 above all, reads this count to know what each requirement asks of the goal
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review counts again by a second route this instruction names, and plants a fault
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_COUNT_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/COUNT.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/count.csv · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-04-count/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COUNT_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · the count
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COUNT_2026-10-31.md
```

---

# INSTRUCTION — Count every requirement against the goal, both ways, and report each total with its evidence

**Suggested model: Opus, effort high.** The sets are settled; the risk is inexactness over 23 requirements by 19 elements of the goal (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · the count`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run every program with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-19 --session "MR · work · the count" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COUNT_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · the count"
```

A session that can tell only that a scheduled task started it writes `unknown`, never `owner`. Your account is read from your own context only; your computer is what `hostname` prints. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md` — the page of the kind: part 1 is what you refuse, part 2 what your review runs.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`.
5. **The two sets and their sources:**
   - **the requirements**: R-01 to R-23 of the accepted register, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`, sha256 `ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103`;
   - **the goal as the owner ruled it**: the steps S-1 to S-7, the failures F-1 to F-5 and the screens SC-1 to SC-5 of the accepted goal, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md`, sha256 `342515fd5ed96e45e23014568f67e8126edfeeccdb7f862dddd38e44acdb2aed`, **as amended by the owner's ruling of 20:19 Tallinn time** on the thirteen recommendations of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md`, sha256 `9603caf1d95b8f89927a35969e33947da9e93776e04f98ccd27a3a7965ef0cef` — its section "Taken together" gives what each recommendation changes in each element and adds F-6 and F-7. **Only the closing proposals and "Taken together" are ruled**; the positions and tables are not.
   Check each sha256 first; where one differs, stop and say so.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

## 3. The task

Count every requirement against the goal, both ways, and write the count where later rounds read it.

1. **List both sets first, by a command**, into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-04-count/_evidence/`: `REQUIREMENTS_SET.txt` (23 lines, `R-01` to `R-23`, each with its heading line in the register) and `GOAL_SET.txt` (19 lines: S-1 to S-7, F-1 to F-7, SC-1 to SC-5, each with its line in `GOAL.md` or, for F-6 and F-7, in "Taken together"). Count each.
2. **The pairs, by this route:** for each requirement, read **its test** in the register — set up, do, see — and name every element of the goal the test passes through or ends at. Write one row per pair to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/count.csv`: `requirement,element,ground`, the `ground` quoting in a few words the part of the test that passes through that element. A requirement whose test passes through no element of the goal is written once with element `none` and a ground that says why — the requirement concerns the made-up data, the delivery, or what the prototype must not do outside the goal — quoting the test's words that show it.
3. **The count, both ways**, by a program saved in the evidence folder, from `count.csv` and the two sets:
   - **Requirements → goal:** how many requirements reach at least one element, how many reach none, and each of the latter by name with its ground.
   - **Goal → requirements:** how many elements are reached by at least one requirement, how many by none, and each of the latter by name, with the ruling or source that put it in the goal (from `GOAL.md` or "Taken together").
4. **`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/COUNT.md`**: the two totals each way in a short table, then the names of every member in one set and not reached from the other, each with its ground; then one line saying what round 6 must build that no requirement's test reaches, and what no element of the goal carries. Nothing else; the pairs are in the CSV.

## 4. Constraints and standing rules

- **Change nothing you check** (the checking page, item 5): the register and the goal are read only. A defect found in either goes to the report under "found, not fixed".
- **Plant a fault before trusting a zero** (item 1): in a copy of `count.csv` in the evidence folder, remove one pair and add one requirement absent from the register; run the program on the copy and show that it names both. Only then run it on the real file.
- No figure from memory; no operation that writes to version control; nothing opens a window.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-04-count/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`; run **your own** programs through `run`; **run the layer's own checks outside `run`**; `end` after your last write but the report; `check` last, before the `finished` entry.

## 5. Acceptance criteria

- **A1** — The sets listed first: a command prints `23` for `REQUIREMENTS_SET.txt` and `19` for `GOAL_SET.txt`, each line found at the place it names.
- **A2** — Every row of `count.csv` names a requirement in the first set and an element in the second or `none`, and every requirement appears at least once → the program prints `0 unknown, 0 absent`.
- **A3** — Every `ground` is words of that requirement's test: a command shows each ground is a substring of the requirement's test in the register, or, for `none`, of its test → `0 not found`.
- **A4** — The planted fault: the program run on the copy names the removed pair's requirement or element as unreached, where it was reached, and the added requirement as unknown; its output quoted.
- **A5** — The two totals each way are printed by the program and are the figures in `COUNT.md`; every member unreached from the other set is named in `COUNT.md` with its ground.
- **A6** — The register, the goal and the paper are unchanged: `shasum -a 256` prints the checksums of section 2.
- **A7** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COUNT_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COUNT_2026-10-31.md`.
- **A8** — The record check exits 0: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-04-count/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COUNT_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-04-count/_evidence/record/check.out`.
- **A9** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-19` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-04-count/_evidence/`, cited by path. Every figure the report gives twice is the same both times, and the `finished` entry's outcome agrees with the report's first paragraph.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md`.

- **The goal's own citations borrowed as the count.** Each step and failure of the goal names the requirements it rests on. That is **the review's route**, not yours: your pairs come from each requirement's test. Do not read the goal's citation columns to make a pair.
- **A pair asserted on a word.** A test that names "the clerk" does not pass through every screen; the ground is the part of the test that reaches that element.
- **The ruled amendments left out.** F-6, F-7 and what "Taken together" changes in each element are part of the set; an element counted as `GOAL.md` alone has it is not the goal the owner ruled.

## 8. Out of scope — do not touch

`src/`, the brief, the register, the goal, the papers, `CONSTANTS.md`, `_kinds/`; round 5; any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-19`. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-19 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COUNT_2026-10-31.md --outcome "<one line: the totals each way, in the words of the report's first paragraph>" --moved "<one line: what later rounds now read, or nothing>" --account <the same account as your started entry> --by "MR · work · the count"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · the count
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_COUNT_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.
