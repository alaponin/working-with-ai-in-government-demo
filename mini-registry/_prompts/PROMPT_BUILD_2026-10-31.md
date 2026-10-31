---
kind: instruction
commission_id: C-2026-10-31-25
version: 2
session_name: MR · work · the goal built
kind_of_work: building
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/COUNT.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/count.csv · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31_v2.md
serves: the working prototype, deliverable 1 of the constants — round 6 of the brief, the goal built: a school clerk enrols a learner, and the registry does not register the same child twice
model: Opus — the goal is settled step by step by the accepted goal and the owner's ruling on its thirteen questions; what remains is building it exactly, with a check for each requirement and each way it can go wrong; the risk is a screen or a failure built otherwise than ruled, or checked by its own description
effort: high — this is the prototype the brief delivers; round 7 counts on it and the note of round 8 describes it
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review runs the checks, goes through the screens as a clerk without a window, and sets up a way the goal goes wrong
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_BUILD_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/server.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/enrol.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/screens.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/goal.test.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/requirements.test.js · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/package.json · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31_v2.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · the goal built
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md
```

---

# INSTRUCTION — Build the goal: the enrolment screens, served on this Mac only, with a windowless check for every requirement and every way the goal can go wrong

**Suggested model: Opus, effort high.** The goal and the rulings settle every step; the risk is inexactness, and a check that reads the build's own description (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · the goal built`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run the layer's programs with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-25 --session "MR · work · the goal built" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · the goal built"
```

A session that can tell only that a scheduled task started it writes `unknown`, never `owner`. **Where it refuses because the task waits**, write nothing and stop, quoting what it printed. Your account is read from your own context only; your computer is what `hostname` prints. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md` — the page of the kind.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — invented data only, nothing connects outside the Mac, nothing opens a window.
5. **The sources, in order of precedence:** the brief; the accepted register, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`; the accepted groundwork, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/`; the owner's rulings on the gaps paper (`ruling:G-<nn>`, ruled parts only) and on the questions paper (`ruling:Q-<nn>`, ruled parts only); **the accepted goal, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md`, as the owner ruled it on `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md`** — its closing proposals and its section "Taken together", which gives every step, failure and screen as ruled, F-6 and F-7 among them, and the five screens; the accepted count, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/COUNT.md` and `count.csv`, which pairs each requirement with the elements its test reaches; and the accepted round 5, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/` as it stands.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

Record the sha256 of every source and of every file under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/` as you start, into the evidence folder.

## 3. The task

**Stage 1, before anything is written** (the building page, part 3): `node --version`; `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node reset.js && node --test test/` passing 29 of 29 as accepted; `ls -R /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src` as it stands. Where one fails, stop here, write nothing, and report the cause first.

**Stage 2, the build.** Add, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`, and change nothing round 5 made but `package.json`'s scripts:

- `lib/enrol.js` — the goal's steps S-1 to S-7 and failures F-1 to F-7, **exactly as ruled**: every check of the entry before the search (Q-7) — all four entered, an entry of spaces only being missing (Q-4, Q-5), the date of birth in the form `YYYY-MM-DD` and naming a real day (Q-1, ruling G-07), the school one of the three (Q-6); no age check (Q-2); every fault found and named (Q-8, Q-9); then the search, **by `lib/search.js` as round 5 built it, unchanged**; exactly one learner found → that learner shown, nothing new entered; none → the next learner number (one above the highest held, Q-4, ruling G-01), the record saved; more than one → nothing saved (F-4); a record that cannot be saved → F-6 (Q-3); F-5 and F-7 as the goal and the ruling on Q-12 describe them.
- `lib/screens.js` — the five screens SC-1 to SC-5, as HTML, each carrying the line **"Invented data, Progressa is fictional"** (R-17), each saying what the goal and the rulings say it shows (Q-8, Q-10), each result screen offering the way back to SC-1 (Q-13), SC-4 keeping the clerk's four entries (Q-8). No sixth screen; no screen for looking learners up (G-08).
- `server.js` — Node's own `http` module, listening on **127.0.0.1 only**, serving the screens; it opens no window and asks the system to open none.
- `test/goal.test.js` and `test/requirements.test.js` — with `node:test`, the server started in the test on a free local port, its screens fetched with Node's own `fetch` against `127.0.0.1` and read as text: **one check for each requirement whose test `count.csv` pairs with an element of the goal**, written from that requirement's test in the register; **one check for each way the goal goes wrong, F-1 to F-7**, set up and seen handled as ruled (ruling G-12); and a check that every screen any test reached carries R-17's line. Each check starts from a fresh reset, and from data the reset or the clerk's own entries would hold (the building page, item 3). For R-21 — no window — check what Node can see without one, and where the system cannot be asked without a permission or a window, say so in the report rather than claim it.
- `package.json` — a `start` script for the server; the `test` script still runs every file in `test/`.

## 4. Constraints and standing rules

- Change nothing round 5 made — `lib/search.js`, the generator, `reset.js`, its tests, its data form — but `package.json`'s scripts. A defect found there goes to "found, not fixed" (the building page, item 5).
- Nothing connects outside the Mac: the server listens on 127.0.0.1 only; no outbound request anywhere but to that address in the tests; no npm dependency, no install.
- **Nothing opens a window**: no `open`, no browser, no GUI, from `src/` or from anything you run.
- Build each step and failure as ruled, and nothing more (the building page, item 4).
- Write nothing outside the files named in `outputs`. No operation that writes to version control.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`; run your own commands through `run` where it can trace them, and say where it cannot; **run the layer's own checks outside `run`**; `end` after your last write but the report; `check` last, before the `finished` entry.

## 5. Acceptance criteria

- **A1** — Stage 1's outputs quoted, before any write; 29 of 29.
- **A2** — `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node --test test/` exits 0 with every check passing, round 5's 29 among them; the output quoted with the count.
- **A3** — Every requirement `count.csv` pairs with an element of the goal has its check, and F-1 to F-7 each have theirs: a command lists them against the checks' names → `0 without a check`.
- **A4** — **The planted fault**: in a scratch copy of `src/` under the evidence folder, make the search forgive one more thing than capitals, and separately drop R-17's line from one screen; run the checks there; see each fail by name. The real `src/` is untouched.
- **A5** — Round 5's files are unchanged: their sha256 at the end equals that at the start, `package.json` alone excepted, its diff quoted.
- **A6** — Nothing connects and nothing opens: a command over `src/` prints every `listen`, `fetch`, `http.request`, `https`, `net`, `dgram`, `child_process` and `open(` with its line → each one on 127.0.0.1 or explained; `package.json` has no `dependencies`.
- **A7** — The sources are unchanged: their sha256 at the end equals that at the start.
- **A8** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31.md`.
- **A9** — The record check exits 0: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/record/check.out`.
- **A10** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-25` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/`, cited by path. Every screen the report describes is quoted from what the server returned in this round, never from the code that makes it (the building page, item 1). Every figure the report gives twice is the same both times.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md`.

- **A check that reads the builder's description.** A test that compares a screen with a string `screens.js` also exports proves only that the module exports it; the check reads what the server returned.
- **A ruled failure built as a sensible one.** F-1 to F-7 are what the rulings say: an age outside 6 to 12 is enrolled (Q-2); a different school on a learner found raises no notice (Q-11); a different child sharing the three fields is taken for the learner, a limit of the rule (Q-12).
- **The search touched to make a test pass.** `lib/search.js` stays as round 5 made it; a test that fails against it is a finding, not a reason to change it.

## 8. Out of scope — do not touch

Round 5's files, but `package.json`'s scripts; the count of the 8 (round 7); the note (round 8); everything outside `outputs`; any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-25`. List every file written or changed under `src/` with its size and sha256. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-25 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31.md --outcome "<one line: what came of the round, in the words of the report's first paragraph>" --moved "<one line: what rounds 7 and 8 now build on>" --account <the same account as your started entry> --by "MR · work · the goal built"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · the goal built
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_BUILD_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.

---

## Version 2 — 31 October 2026, 2026-10-31 19:55 UTC: the gap of the review

The review of version 1, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31.md`, is **not accepted** on one gap, G1 (item): R-20's check reads no list of windows, as the register's test says it must (`docs/REQUIREMENTS.md:277-279`), and the reason the report gave — a permission and a dialog — does not hold. The reviewer read the list of windows, each with its number and owner, by `CGWindowListCopyWindowInfo` through `osascript -l JavaScript`, with no permission asked and no window opened: 252 before, 252 after, 0 added (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-review/_evidence/R5_windows.log`). Everything else in version 1 stood in the reviewer's own run. Read the review's sections 7 and 8 in full.

This version is carried out by a new session with an empty memory. It changes **only** `src/test/requirements.test.js` — and `src/test/goal.test.js` only if a window check lives there — and nothing else under `src/`. Your entries are those of sections 1 and 9, with `--report` in the `finished` entry naming `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31_v2.md`; evidence and record under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/` (record at `…/record`). The program reads the version from this declaration.

**What this version must do:**

- **R-20 and R-21, as their tests say**, for every requirement whose test reads the list of windows: the check reads the list of windows before and after, by a command that brings nothing forward and asks no permission — `CGWindowListCopyWindowInfo` through `osascript -l JavaScript`, as the review did, or another you show to ask neither — and expects 0 windows added, by window number. The check is a test of the prototype's checks and runs in `node --test`; `osascript` is started by the test only, and A6's listing names it and says why.
- **Before you trust it** (the checking page's item 1, here for building): in a scratch copy, make the check run while a window is added — or, if no window can be added without opening one, show the check failing on a planted "after" list with one window more — and see it fail by name.
- **Where a command is refused**, keep the command and what it printed; only then may the report say the list could not be read (the building page, item 7, added today).
- **Name, do not fix,** the review's "found, not fixed" items on the whitespace read as "spaces" (Q-4) and the fourth school lost on the way back (Q-6, Q-8): each goes to the report as a question for the owner.

**The tests of success of this version** (A1 to A10 stand, read with this version's paths, A5 allowing the change to the test files):

- **A11** — R-20's and R-21's checks read the list of windows before and after; their output, from a run of `node --test`, quoted with the window counts.
- **A12** — The planted case fails by name; its output quoted.
- **A13** — The diff of `src/` against version 1's checksums shows only the test files changed; quoted.
