---
kind: instruction
commission_id: C-2026-10-31-13
version: 2
session_name: MR · work · the goal in full
kind_of_work: drafting
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T141251Z_MR_ruled_D-2026-10-31-03.yaml · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T161245Z_MR_ruled_D-2026-10-31-05.yaml · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31_v2.md
serves: the working prototype, deliverable 1 of the constants — round 3 of the brief, the goal written in full: every step of enrolling a learner, and every way it can go wrong
model: Opus — the content is settled by the brief, the accepted register and groundwork, and the owner's two rulings; what remains is writing every step and every failure out exactly, and the risk is a failure invented or a step missed
effort: high — round 4 counts every requirement against this goal both ways, and round 6 builds it; a step missed here is missed in both
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review lists the steps and failures again from the sources by its own route
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOAL_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31_v2.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · the goal in full
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md
```

---

# INSTRUCTION — Write the goal in full: every step of enrolling a learner, and every way it can go wrong, each traced to its source

**Suggested model: Opus, effort high.** The sources settle the content; the risk is inexactness over every step and every failure (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · the goal in full`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run every program with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-13 --session "MR · work · the goal in full" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md --effort unknown --started-by <owner, sub-session or unknown, from your own prompt> --account <the address your own context names as the user's address, or unknown> --by "MR · work · the goal in full"
```

Your account is read from your own context only; your computer is what `hostname` prints. Where the command cannot run, record that as it stands. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md` — the page of the kind.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — the standing constraints.
5. **The sources, in order of precedence:**
   - the brief, `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`, its section "What it must do" above all;
   - the accepted register, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`;
   - the accepted groundwork, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/`, its `search_rule.csv` above all;
   - **the owner's first ruling**, `ruling:G-<nn>`: the thirteen summary rows of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, lines 26 to 38, and the one-sentence recommendation closing each of its sections — nothing else in that paper;
   - **the owner's second ruling**, `ruling:Q-<nn>`: the closing proposal of each of the fourteen sections of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md` — nothing else in that paper.
   Neither paper passed its review; each is the record of what was ruled, not accepted work.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

Check the sha256 of each against these, read 2026-10-31 16:12 UTC; where one differs, stop and say so: brief `ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64`; register `ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103`; `GROUNDWORK.md` `5ed9b62f282d433df7c337a2da30e4830c56170dca1e646ae5aacc2cc2795dce`; `search_rule.csv` `9a7c98ce9b57dde82ccca48c84c638b7efd5c08f26f1677e738ecc8d00386fdb`; `settings.csv` `a94c31fe9fc96410910e425b1a0dfc708ea6acf09f3fb9ab1c990e71f8ef9cfd`; `lists.csv` `1d08f58c5ea6d1caddfed7f6266800083bed696e7cd1b76c6efc53be72c9eef7`; `GAPS-PAPER.md` `d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb`; `QUESTIONS-PAPER.md` `5146d23a87cf9c0527c26c2965725bfa1125bd1a0a103ac83b68fb7dbd50cce0`.

## 3. The task

Write `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md`: the one goal, **enrol a learner**, written in full, as the build of round 6 will follow it and round 4 will count against it.

**First, the sets**, each listed by a command into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/` before the goal is written:
- `STEPS_SET.md` — every step of enrolling a learner that a source states, from the brief's section "What it must do", the register's R-02 to R-07, and the rulings that shape the steps (among them G-02, G-03, G-07, G-08, G-09, Q-4, Q-14), each with its source;
- `FAILURES_SET.md` — every way the goal can go wrong that a source states or rules: an entry missing or in the wrong form, a school not among the three, more than one learner found, and any other a source names, each with its source.

**Then the goal**, in three parts:

1. **The steps**, numbered, from the clerk opening the screen to the clerk seeing which of the two things happened. Each step: what the clerk does or sees, what the registry does, the screen it happens on, and its source.
2. **The ways it can go wrong**, numbered F-1 onward. Each: at which step, what sets it off, what the clerk sees, what is saved (or that nothing is), and its source.
3. **The screens**: every screen the steps and the failures name, every view the clerk sees counting as one (G-09), each stating that it carries the line "Invented data, Progressa is fictional" (R-17).

Close with **Gaps against the sources**: each step or failure the build will need that no source gives — a date that is not a real date, an age outside 6 to 12, a learner number that cannot be given — as a question, left open. Never answer one in the goal.

**The `source` of each step and failure** is one or more of `brief:<line>`, `R-<nn>`, `ruling:G-<nn>`, `ruling:Q-<nn>`, or `groundwork:<file>:<line>`, separated by ` · `. A step or failure with no source is not written.

## 4. Constraints and standing rules

- Supply no step, check or failure the sources do not carry (the drafting page, part 1, item 1); a missing one is a gap.
- The search is the groundwork's `search_rule.csv`, cited by its rows: three fields, capitals ignored, nothing else, the school not compared, the key table and the reset's record of entries never read.
- The goal is enrolment only (G-08): the reset is not one of its steps, and no screen for looking learners up is added.
- No figure from memory; the sources are read and never changed; no operation that writes to version control; nothing opens a window.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`; run **your own** programs through `run`; **run the layer's own checks outside `run`**; `end` after your last write but the report; `check` last, before the `finished` entry.

## 5. Acceptance criteria

- **A1** — The sets come first: a command compares `STEPS_SET.md` with the goal's steps, and `FAILURES_SET.md` with its failures → `0 missing, 0 extra` for each.
- **A2** — Every source resolves: a program, saved in the evidence folder, checks that each `brief:<line>` exists, each `R-<nn>` is in the register, each `ruling:G-<nn>` is one of G-01 to G-13, each `ruling:Q-<nn>` one of Q-1 to Q-14, and each `groundwork:<file>:<line>` exists → `0 without source, 0 unresolved`, and the counts of steps and failures.
- **A3** — Every failure is complete: the program prints, per failure, whether it has its step, its trigger, what the clerk sees, what is saved, and its source → `0 incomplete`.
- **A4** — The search step cites `search_rule.csv` and compares nothing the file does not: the report quotes the step beside the rows it cites.
- **A5** — Every screen carries R-17's line: a command counts the screens the goal names and the screens it states carry the line → the two counts equal.
- **A6** — The closing section "Gaps against the sources" exists; each gap is a question, and no step or failure answers one.
- **A7** — The sources are unchanged at the end: `shasum -a 256` prints the checksums of section 2.
- **A8** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31.md`.
- **A9** — The record check exits 0: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/record/check.out`.
- **A10** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-13` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal/_evidence/`, cited by path.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md`.

- **The sensible check invented.** A date in the future, an age outside 6 to 12, a name too long: each is reasonable and none is sourced. Each is a gap, not a failure.
- **The unruled part of a paper read as ruled.** Only each paper's closing recommendations are ruled; the positions, tables and passing values are not.
- **A screen forgotten.** A refusal, a message or the result the clerk sees is a screen (G-09); a screen the goal shows but does not list leaves R-17 untested for it.

## 8. Out of scope — do not touch

`src/`, the brief, the register, the groundwork, both papers, `CONSTANTS.md`, `_kinds/`; the count of round 4; the data of round 5; any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-13`. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-13 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31.md --outcome "<one line: what came of the round, in the words of the report's first paragraph>" --moved "<one line, or nothing>" --account <the same account as your started entry> --by "MR · work · the goal in full"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · the goal in full
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOAL_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.

---

## Version 2 — 31 October 2026, 2026-10-31 17:14 UTC: the gap of the review

The review of version 1, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31.md`, is **not accepted** on one gap, G1: F-1 (an entry missing) and F-3 (a school not among the three) say the entry "is refused" and give it a refusal screen, SC-4 and SC-6, which no source they cite carries. The sources carry that the search does not run until all four are entered, and that the school is chosen from the three; they say "refused" only of a date in the wrong form. Round 6 would build, and round 4 count, screens nobody ruled. Read the review's sections 7 and 8 in full, after the declaration.

This version is carried out by a new session with an empty memory. It changes `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md` in place; its evidence and record go to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2/_evidence/` (record at `…/record`), its report to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31_v2.md`. Version 1's report and evidence stay as written. Your entries are those of sections 1 and 9, with `--report` in the `finished` entry naming this version's report; the program reads the version from this declaration. **Who started you**: a session that can tell only that a scheduled task started it writes `unknown`, in the entry and in the report — never `owner` (the review's "found, not fixed", item 1).

**What this version must do, beyond version 1:**

- **G1, for every failure and every step, not for F-1 and F-3 alone.** For each failure's "what the clerk sees" and "what is saved", and each step's "what the registry does", quote beside it, in the evidence folder, the words of its source that carry that very fact. A word shared with the source is not enough: G-09's "refusals" defines what counts as a screen and says nothing is refused. Where no source carries the fact, the goal says only what the sources carry (for F-1: the search does not run until all four are entered), and the rest — what the clerk then sees, whether it is a refusal, whether F-3 can arise at all where the school is chosen from three — becomes a question in "Gaps against the sources". Remove any screen that only an unsourced fact made. The report says how many steps and failures changed.
- **The order of the date check and the search** (the review's "found, not fixed", item 3): S-3 refuses a date in the wrong form before the search, and S-4 says the search runs first, before anything else is done with the entry; the sources do not settle which comes first. State the conflict with both passages quoted, keep neither order as fact, and add it as a gap.
- **The report's own consistency** (items 2 and 4): every figure the report gives twice is the same both times, and the `finished` entry's outcome agrees with the report's first paragraph.

**Further tests of success for this version** (A1 to A10 stand, read with this version's paths):

- **A11** — A file in the evidence folder, one row per step and per failure, quotes beside each "registry does", "clerk sees" and "is saved" the source words that carry it, or reads "gap G-<n>" → a command prints `0 unquoted`.
- **A12** — No screen in the goal rests on an unsourced fact: the report lists each screen with the step or failure that makes it and that row of A11's file.
- **A13** — The review of version 1 is answered item by item: one row each for G1 and items 1 to 4 of its "found, not fixed", with what changed and where.
