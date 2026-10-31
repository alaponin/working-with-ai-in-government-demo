---
kind: instruction
commission_id: C-2026-10-31-11
version: 2
session_name: MR · work · answers to the groundwork's questions
kind_of_work: analysis
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31_v2.md
serves: the working prototype, deliverable 1 of the constants — the answers round 5, the made-up data, needs to the 14 questions the accepted groundwork leaves open; the owner ruled at 17:05 Tallinn time, 31 October 2026, that they are answered now, before round 3
model: Opus — every position is bounded by the brief, the register, the owner's thirteen rulings and the groundwork, and most questions fix a value that any choice within the sources meets; the risk is inexactness and inconsistency across questions, not open judgement
effort: high — fourteen questions whose answers must hold together, so that round 5 can make the data to the known numbers
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review checks every citation and runs the recommendations together by its own route
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_QUESTIONS_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31_v2.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · answers to the groundwork's questions
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md
```

---

# INSTRUCTION — Write a short paper that recommends an answer to each of the groundwork's 14 open questions, for the owner's ruling

**Suggested model: Opus, effort high.** The sources bound every position; the risk is inexactness and inconsistency over fourteen answers (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · answers to the groundwork's questions`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run every program with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-11 --session "MR · work · answers to the groundwork's questions" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md --effort unknown --started-by <owner, sub-session or unknown, from your own prompt> --account <the address your own context names as the user's address, or unknown> --by "MR · work · answers to the groundwork's questions"
```

**Where it refuses because the task waits** for the commit of the day, write nothing anywhere and stop, quoting what it printed. Where it cannot run, record that as it stands. Your account is read from your own context only; your computer is what `hostname` prints. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure; section 5 on how a decision is closed.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md` — the page of the kind, including its item 6, added today.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`.
5. **The sources, in order of precedence:** the brief, `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`; the accepted register, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`; the owner's thirteen rulings, which are the summary rows of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, lines 26 to 38, and the one-sentence recommendation closing each of its question sections — **nothing else in that paper is ruled**; and the accepted groundwork, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/` — its closing section, "Gaps against the sources", holds the 14 questions.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

Check the sha256 of each against these, read 2026-10-31 15:06 UTC; where one differs, stop and say so: brief `ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64`; register `ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103`; gaps paper `d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb`; groundwork, the four files as they stand when you start — record their checksums first.

## 3. The task

Write `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md`, **under 20 KB**: one recommended answer to each of the 14 questions, so that the owner can rule on all of them in one act and round 5 can make the data from the sources and his ruling.

**The previous paper of this kind failed review twice** on consistency across a large grid: options judged on facts the paper granted elsewhere, settings credited to one option that any option could take (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31.md` and `_v2.md`, section 7). This paper is shaped to avoid that:

- **First, one section "Given to every position"**: everything the sources fix — the brief, the register, the thirteen rulings, the groundwork — stated once, by citation, and given to every position of every question. No position may be judged on lacking one of them.
- **Then the set**: the 14 questions, each quoted word for word from `GROUNDWORK.md` with its line, listed by a command into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/QUESTIONS.md` and counted.
- **Then one short section per question**, in this order: the question; the passages of the sources that bear on it, quoted with path and line, or one line saying none does; **two positions only — the one you recommend and its strongest rival** — each in two or three sentences; one small table, the two positions against the tests that bear (from: what the brief's "What it is for" section says the prototype is for; the brief's "must not" sentences; the known numbers; what rounds 5, 6 and 7 must do), a test that both meet marked so; and the recommendation in one sentence, marked as a proposal. **Where any value within the sources serves equally** — a seed, a date, a first number — say so: the rival is "any other value", the table shows both meet every test, and the recommendation picks one value for a stated convenience.
- **Where one answer depends on another**, say so in one line, "depends on Q-<n>", and judge it with that answer as recommended; never assume another question's recommendation silently.
- **Last, "Taken together"**: a small program, saved in the evidence folder, that builds a toy data set to the recommendations together and prints the known numbers it yields — children, schools, entries, children on more than one list, of those spelt differently, the ages' range, learners after reset — and how many of the 8 the brief's rule catches. Its output is quoted in the paper.

## 4. Constraints and standing rules

- The paper recommends; it decides nothing. No recommendation lets the search compare anything but the three fields of the brief's line 13, forgive anything but capitals, or read the key table.
- No passage restated where it can be quoted; no figure from memory.
- The sources are read and never changed.
- No operation that writes to version control; nothing opens a window.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`; run **your own** programs through `run`; **run the layer's own checks (placement, trace) outside `run`**, directly, their output kept as files; `end` after your last write but the report; `check` last, before the `finished` entry.

## 5. Acceptance criteria

- **A1** — `QUESTIONS.md` lists the 14 questions, each a substring of `GROUNDWORK.md` at its line; a command prints `14` and `0 not found`.
- **A2** — A command compares the questions with the paper's sections and prints `0 unanswered, 0 extra`.
- **A3** — Every passage the paper quotes is in its file at the line it gives: a command prints `0 not found, 0 wrong line`.
- **A4** — Every question section has exactly two positions, one table and one recommendation marked as a proposal: a command prints the counts per section, and every row reads 2, 1, 1.
- **A5** — The "Taken together" program runs and prints, for the recommendations together: 60 children, 3 schools, 8 children on more than one list, 4 of those spelt differently, ages within 6 to 12, and 68 entries; the report quotes its output with the learners after reset and the number of the 8 the rule catches.
- **A6** — No recommendation widens the search or lets it read the key table: the report says, per question, which part of the search rule or the key table it touches, or "none".
- **A7** — The paper is under 20 KB: `wc -c` quoted.
- **A8** — The sources are unchanged at the end: `shasum -a 256` prints the checksums of section 2 and of the groundwork as recorded at the start.
- **A9** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31.md`.
- **A10** — The record check exits 0: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record/check.out`.
- **A11** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-11` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/`, cited by path.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`, items 1 to 6.

- **A rival given less than the sources give it.** The "Given to every position" section exists so that no table can deny a rival what the sources grant; before writing each table, read it against that section.
- **A value from the gaps paper taken as ruled.** The paper proposes a seed, a date and which lists carry the 8 in passing; those are not ruled. You may recommend the same values, but as your recommendation, with your ground.
- **The toy run made to agree.** A5's program builds the data from the recommendations as written; where it does not reach a known number, the recommendations are wrong, not the program.

## 8. Out of scope — do not touch

`src/`, the brief, the register, both earlier papers, the groundwork, `CONSTANTS.md`, `_kinds/`; round 3; any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` this file's path and `answers` `C-2026-10-31-11`. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-11 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31.md --outcome "<one line: what came of the round, in the words of the report's first paragraph>" --moved "<one line, or nothing>" --account <the same account as your started entry> --by "MR · work · answers to the groundwork's questions"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · answers to the groundwork's questions
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_QUESTIONS_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.

---

## Version 2 — 31 October 2026, 2026-10-31 15:45 UTC: the gap of the review

The review of version 1, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_QUESTIONS_2026-10-31.md`, is **not accepted** on one gap, G1: Q-6 judges its rival without Q-5 as recommended, so the paper credits that rival with 60, 8 and 68, which it cannot reach alongside Q-5's recommendation; and the dependency between Q-5 and Q-6 is declared in one direction only. A ruling taken from the paper as it stands could hand round 5 settings no data meets. Read the review's sections 7 and 8 in full, after the declaration.

This version is carried out by a new session with an empty memory. It changes `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md` in place, still **under 20 KB**; its evidence and record go to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/` (record at `…/record`), and its report to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_QUESTIONS_2026-10-31_v2.md`. Version 1's report and evidence stay as written. Your `started` and `finished` entries are those of sections 1 and 9, with the same commands but for `--report` in the `finished` entry, which names this version's report; the program reads the version from this declaration. The task no longer waits for anything.

**What this version must do, beyond version 1:**

- **G1, for every question, not for Q-6 alone.** List every pair of questions where one answer bears on the other. Declare each dependency **in both sections**. Judge **both** positions of each question under the **recommended** answer of every question it depends on. Where a rival cannot be built alongside the other recommendations, its table says so in the row of the known numbers, and the section says which other answer it would need. Q-6's rival is the case the review found; check every other.
- **The review's "found, not fixed", items 1, 2, 3 and 7:**
  - item 1: "Given to every position" cites, by range where a list is long, the register, all thirteen ruled summary rows and the settings rows of `docs/groundwork/settings.csv`, and quotes the ruled line `GAPS-PAPER.md:196` whole;
  - item 2: Q-9 names every question its figures rest on;
  - item 3: Q-6's recommendation says no more than the brief's line 19 says;
  - item 7: Q-9's rival is stated at its strongest, weighing the form the review names, a school on the census only that still gives every learner one.

**Further tests of success for this version** (A1 to A11 stand, read with this version's paths):

- **A12** — A table in the evidence folder lists every pair of dependent questions; a command shows each pair declared in both sections → `0 one-way`.
- **A13** — A program, saved in the evidence folder, builds each question's rival together with every other question's recommendation and prints, per rival, whether the brief's known numbers can be met; the paper's table for each rival agrees with that output → the report quotes it and names `0 disagreements`.
- **A14** — The verdict of the review of version 1 is answered item by item: the report has one row each for G1 and the four "found, not fixed" items taken up, with what changed and the lines of the new paper where it shows.
