---
kind: instruction
commission_id: C-2026-10-31-21
version: 1
session_name: MR · work · scaffold and made-up data
kind_of_work: building
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/COUNT.md · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T184610Z_MR_ruled_D-2026-10-31-09.yaml · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — round 5 of the brief, the scaffold and the made-up data, in the known numbers
model: Opus — the content is settled to the last number by the groundwork and the owner's rulings; what remains is building it exactly and proving every number by a check that runs; the risk is a number met by construction in the check rather than by the data
effort: high — every later round, the build and the count of the 8 above all, runs on this data
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review runs the checks itself, counts the data by its own program, and plants a fault
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DATA_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/package.json · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/reset.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · scaffold and made-up data
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md
```

---

# INSTRUCTION — Build the prototype's scaffold in Node.js and the reset that makes the made-up data in the known numbers, with a check for every number

**Suggested model: Opus, effort high.** The groundwork and the owner's rulings settle every number; the risk is inexactness, and a check that passes by construction (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · scaffold and made-up data`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run the layer's programs with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-21 --session "MR · work · scaffold and made-up data" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · scaffold and made-up data"
```

A session that can tell only that a scheduled task started it writes `unknown`, never `owner`. Your account is read from your own context only; your computer is what `hostname` prints. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md` — the page of the kind: part 1 is what you refuse, part 2 what your review runs, part 3 what was checked before this was issued.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — the standing constraints: invented data only, nothing connects outside the Mac, nothing opens a window.
5. **The sources, in order of precedence:** the brief; the accepted register, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md` (R-08 to R-16 above all); the accepted groundwork, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/settings.csv`, `lists.csv`, `search_rule.csv`; **the owner's first ruling** (`ruling:G-<nn>`: the summary rows of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, lines 26 to 38, and each section's closing recommendation, nothing else); **the owner's second ruling** (`ruling:Q-<nn>`: the closing proposal of each section of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md`, nothing else); the accepted count, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/COUNT.md`; and **the owner's ruling on the stack**, `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T184610Z_MR_ruled_D-2026-10-31-09.yaml`: Node.js.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

Record the sha256 of every source into the evidence folder as you start, and check them again at the end.

## 3. The task

**Stage 1, before anything is written** (the building page, part 3): show that the tools answer and the project stands as expected — `node --version` (v20.5.1 at issue), `npm --version`, `node -e "require('node:test')"`, and `ls -la /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src` showing only `README.md`. Where one fails, stop at this stage, write nothing, and report the cause in the report's first paragraph.

**Stage 2, the build.** Under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/` only:

- `package.json` — name, `"private": true`, a `reset` script and a `test` script (`node --test test/`); **no dependencies**: Node 20's own modules serve, and nothing is fetched from the network.
- `lib/` — the modules the reset and the checks need, among them: the seeded generator (ruling Q-3: seed 20261031); the invented name parts, written by you as invented words, no real person's name list loaded from anywhere (R-16, ruling G-10); the generator of the three lists to every setting of `settings.csv` and the rulings (Q-1, Q-2, Q-4 to Q-11, Q-14); **the search rule exactly as `search_rule.csv` gives it** — family name, given names and date of birth, capitals ignored, nothing else; the school not compared; the key table and the reset's record of entries never read by it — as one module that round 6 will use as it stands.
- `reset.js` — the reset: it makes the three lists, the key table (Q-11) and then enrols every list entry by the search rule, in the order of ruling Q-2, giving learner numbers from 1 (Q-4), and writes the learners and the record of which entry made or found which learner (Q-12). It writes everything under `data/`, as JSON files, and records every file it reads (G-10). It reads nothing outside `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`.
- `data/` — what `reset.js` writes. Its files are made by the reset, never by hand.
- `test/` — the checks, with `node:test`, one check for **every** number and rule the sources fix for the data: 60 children; 3 schools, 20 children each (Q-7); 68 entries, 24, 22 and 22 (Q-6); every date `YYYY-MM-DD` (Q-10); every age 6 to 12 on 2026-10-31 (Q-1); every entry carries a school (Q-9); 8 children on exactly two lists, in the pairs of ruling Q-5, and 4 of them with their family name spelt differently, on the later list (Q-5), the rest matching as ruling Q-8 says; no two different children sharing all three fields, capitals ignored (Q-14); the key table's 68 rows, named as Q-11 gives; 64 learners after reset (Q-13), numbered 1 to 64; the record of entries, 68 rows; the reset made twice gives byte-for-byte the same `data/`; and the search rule compares exactly its three fields, capitals ignored. **Each check counts the data the reset wrote**; none reads its expected number from the module that made the data.

## 4. Constraints and standing rules

- Invented data only; every name part invented by you in the source.
- Nothing connects outside the Mac: no `fetch`, `http`, `https`, `net` or `dgram` in `src/`, no npm install.
- **Nothing opens a window**: no `open`, no browser, no GUI from anything in `src/` or anything you run.
- Write nothing outside `src/`, your evidence folder and your report. Repair nothing in the groundwork or the rulings; a defect there goes to "found, not fixed" (the building page, item 5).
- No operation that writes to version control.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`; run your own commands through `run` where `round_record.py` can trace them, and say where it cannot (it traces Python programs in full and other commands only as commands); **run the layer's own checks outside `run`**; `end` after your last write but the report; `check` last, before the `finished` entry.

## 5. Acceptance criteria

- **A1** — Stage 1's four outputs quoted, before any write.
- **A2** — `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node reset.js` exits 0, and `node --test test/` exits 0 with every check passing; the output quoted, with the number of checks.
- **A3** — **The planted fault** (the checking page's lesson, here for building): in a scratch copy of `src/` under your evidence folder, change the generator so that one child is missing, run the reset and the checks there, and see the checks fail by name; its output quoted. The real `src/` is untouched by it.
- **A4** — The reset is the same every time: `node reset.js` twice, `shasum -a 256` of every file in `data/` after each, identical.
- **A5** — Nothing connects and nothing opens: a command over `src/` prints every occurrence of `fetch`, `http`, `https`, `net`, `dgram`, `child_process` and `open(` → none, or each explained; `package.json` has no `dependencies`.
- **A6** — The reset's record of its reads names only files under `src/` (G-10, R-16): quoted.
- **A7** — The sources are unchanged: their sha256 at the end equals that at the start.
- **A8** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md`.
- **A9** — The record check exits 0: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/record/check.out`.
- **A10** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-21` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/`, cited by path. Every figure the report gives twice is the same both times, and the `finished` entry's outcome agrees with the report's first paragraph.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md`.

- **The check that passes by construction.** A test that compares the data with a constant the generator also read proves only that the generator read it. Every check counts what `data/` holds, from the files.
- **The search widened to make 64.** The 4 differently spelt children must stay unmatched by the rule; 64 is reached because the rule misses them, not by a tweak.
- **A ruled number met by luck.** The pairs of Q-5 and the spread of Q-6 are laid down by the generator, not hoped for from the seed; the reset twice proves it is the same, the checks that it is right.

## 8. Out of scope — do not touch

The screens and the enrolment goal (round 6); the count of the 8 (round 7); everything outside `src/`, your evidence and your report; any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-21`. List every file written under `src/` with its size and sha256. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-21 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md --outcome "<one line: what came of the round, in the words of the report's first paragraph>" --moved "<one line: what rounds 6 and 7 now build on>" --account <the same account as your started entry> --by "MR · work · scaffold and made-up data"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · scaffold and made-up data
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DATA_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.
