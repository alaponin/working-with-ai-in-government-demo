---
kind: instruction
commission_id: C-2026-10-31-26
version: 2
session_name: MR · review · the goal built
kind_of_work: building
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31_v2.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/count.csv · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md
serves: the verdict on C-2026-10-31-25, the goal built
model: Opus — named in the instruction under review's reviewer line
effort: high — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · the goal built
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_BUILD_2026-10-31.md
```

---

# INSTRUCTION — Review the report of round 6, the goal built

**Suggested model: Opus, effort high.**

## 1. Role and where to run

You are a reviewing session for the mini registry, `MR · review · the goal built`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so. You run on the owner's Mac through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove it with `date -u; hostname`. Run the layer's programs with `/usr/bin/python3`. **Open no window**: no browser, no `open`; read the screens as text from `127.0.0.1`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-26 --session "MR · review · the goal built" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_BUILD_2026-10-31.md --effort unknown --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · the goal built"
```

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the page of the kind, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md`; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31.md`, read as it stands — where it is absent, say so and judge nothing; the goal as ruled (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md` with the closing proposals and "Taken together" of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md`); `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/count.csv`; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

The eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-review/_evidence/`. Change nothing in `src/` or anywhere else; repair nothing; commission nothing. **A review of building that ran nothing says so in its first line, and does not accept.**

- **The tests** A1 to A10, each on evidence you read or produced.
- **The project's checks again, in your own run** (the building page, part 2): `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node reset.js && node --test test/`, the result kept.
- **One use of the screens as a school clerk** (part 2), without a window: start the server (`node server.js`, on 127.0.0.1), and with `curl` or a short program of your own — not the round's tests — enrol, from a fresh reset: (1) a child the registry holds, taken from `data/learners.json`, its family name in other capitals; (2) a new child; (3) the new child again. Quote each screen as returned, and set what it shows beside the goal's step and the ruling it follows. Stop the server.
- **One way the goal can go wrong** (part 2): set up, by your own requests, an entry with the date of birth `2019-02-30` and the school left out at once, and see SC-4 name both faults and keep the entries (Q-1, Q-6, Q-8, Q-9).
- **The planted fault**: in a scratch copy of `src/` under your evidence folder, make one failure behave otherwise than ruled — F-4 saving a record, say — run the checks there, and see one fail by name.
- **The mechanical checks**, run directly, not through `round_record.py run`: trace over the report; placement over the instruction under review; `round_record.py check` over the record the report's `record` line names, with the options its `check.out` prints on `# run with:` and an `--out` of your own; `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-25` and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, quoting the lines naming `MR`.
- **The verdict**, each gap with one kind from `FINDING-KINDS.md`, any fault the page lacks named; **found, not fixed.** A gap is a fault the prototype as delivered would carry, or round 7's count would inherit.

## 4. The last act

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-26 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<count by kind; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · the goal built"
```

---

## Version 2 — 31 October 2026, 2026-10-31 19:55 UTC: the review of the second attempt

The first edition, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31.md`, found G1: R-20's check read no list of windows. The working instruction's version 2 changes only the test files, so that the window checks read the list before and after. This edition is written by a new session with an empty memory as `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence/`; your entries name this edition's file in `--report`. Judge A1 to A13: run `node --test` yourself and read the window counts; read the window list yourself, by your own command, before and after a run; plant a fault that adds a window to the "after" list and see the check fail; confirm that nothing under `src/` changed but the test files. When you copy `src/` for a planted fault, do not keep file times. The first edition's walk through the screens stands; repeat it only if a screen-making file changed.
