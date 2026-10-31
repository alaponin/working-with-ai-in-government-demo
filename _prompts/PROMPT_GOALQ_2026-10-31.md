---
kind: instruction
commission_id: C-2026-10-31-17
version: 1
session_name: MR · work · answers to the goal's questions
kind_of_work: analysis
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — the answers round 6, the build, needs to the 13 questions the accepted goal leaves open; the owner ruled at 19:42 Tallinn time, 31 October 2026, that they are answered now, before round 4
model: Opus — every position is bounded by the brief, the register, the groundwork, the goal and the owner's two rulings; most questions fix a behaviour any choice within the sources meets; the risk is inexactness and inconsistency across the answers, not open judgement
effort: high — thirteen answers that must hold together on five screens, so that round 6 can build the goal from them
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review checks every citation and walks the goal through with every recommendation applied
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOALQ_2026-10-31.md
waits_for: C-2026-10-31-15 — the second commit of the day accepted first, so that this round writes into a clean repository
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · answers to the goal's questions
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOALQ_2026-10-31.md
```

---

# INSTRUCTION — Write a short paper that recommends an answer to each of the goal's 13 open questions, for the owner's ruling

**Suggested model: Opus, effort high.** The sources bound every position; the risk is inexactness and inconsistency over thirteen answers (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · answers to the goal's questions`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only then may you say it is unavailable, with what you searched, what came back and the exact error. Run every program with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9).

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-17 --session "MR · work · answers to the goal's questions" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOALQ_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · answers to the goal's questions"
```

A session that can tell only that a scheduled task started it writes `unknown`, never `owner`. **Where the command refuses because the task waits**, write nothing anywhere and stop, quoting what it printed. Your account is read from your own context only; your computer is what `hostname` prints. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a running task names a file you would write, do not write it; say so and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure; section 5 on how a decision is closed.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md` — the page of the kind, items 1 to 7 of part 1, items 6 and 7 added today.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`.
5. **The sources, in order of precedence:** the brief; the accepted register, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`; the accepted groundwork, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/`; **the owner's first ruling**, `ruling:G-<nn>` — the summary rows of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, lines 26 to 38, and the closing recommendation of each of its sections, nothing else; **the owner's second ruling**, `ruling:Q-<nn>` — the closing proposal of each section of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md`, nothing else; and the accepted goal, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md`, whose closing section, "Gaps against the sources", holds the 13 questions.
6. The second reviews of today's two earlier papers, for what they found, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31_v2.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_QUESTIONS_2026-10-31_v2.md`, section 7 of each.
7. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

Record the sha256 of every source as you start, into the evidence folder, and check them again at the end.

## 3. The task

Write `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md`, **under 20 KB**: one recommended answer to each of the 13 questions, so that the owner can rule on all of them in one act and round 6 can build the goal from the sources and his ruling.

**Today's two earlier papers of this kind failed review** on consistency: options judged on facts the paper granted elsewhere, a setting credited to one option that any could take, a rival judged without another question's recommended answer, a dependency declared one way only. This paper is shaped to avoid every one:

- **"Given to every position"** first: everything the sources fix, cited by range where a list is long — the brief's section "What it must do", the register's R-02 to R-07 and R-16 to R-21, the groundwork's `search_rule.csv`, every ruled row of both rulings that bears on the goal, and the goal's steps, failures and screens — given to every position of every question.
- **The set**: the 13 questions, each quoted word for word from `GOAL.md` with its line, listed by a command into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/QUESTIONS.md` and counted.
- **The dependencies**: a table, in the paper, of every pair of questions where one answer bears on the other — 8 (what a refusal says) on 5, 6 and 7, for example — and each declared in **both** sections.
- **One short section per question**: the question; the source words that bear on it, quoted with path and line, or one line saying none does; **two positions only — the one recommended and its strongest rival** — each in two or three sentences, both judged with the recommended answer of every question it depends on; one small table, the two positions against the tests that bear (what the brief's "What it is for" says the prototype is for; the "must not" sentences; R-17's line on every screen; what rounds 4, 6 and 7 must do), a test that both meet marked so; and the recommendation in one sentence, marked as a proposal. Where any answer within the sources serves equally, say so.
- **Last, "Taken together"**: the goal walked through with all 13 recommendations applied — every step, every failure and every screen, one row each, saying what a recommendation changes in it or "unchanged"; and the list of screens the goal then has, each with R-17's line. A recommendation that adds a screen says so here and in its section.

Every fact a position or a recommendation states stands beside the source words that carry it (the drafting page's item 5 holds here too): a shared word is not a source.

## 4. Constraints and standing rules

- The paper recommends; it decides nothing. No recommendation lets the search compare anything but the three fields of the brief's line 13, forgive anything but capitals, or read the key table or the reset's record of entries; none adds a goal or a screen for looking learners up (G-08).
- No figure from memory; the sources are read and never changed; no operation that writes to version control; nothing opens a window.
- Keep the round's record with `round_record.py`: `start` before your first write, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`; run **your own** programs through `run`; **run the layer's own checks outside `run`**; `end` after your last write but the report; `check` last, before the `finished` entry.

## 5. Acceptance criteria

- **A1** — `QUESTIONS.md` lists the 13 questions, each a substring of `GOAL.md` at its line; a command prints `13` and `0 not found`.
- **A2** — A command compares the questions with the paper's sections → `0 unanswered, 0 extra`.
- **A3** — Every passage the paper quotes is in its file at the line it gives → `0 not found, 0 wrong line`.
- **A4** — Every section has two positions, one table and one recommendation marked as a proposal → per-section counts, every row 2, 1, 1.
- **A5** — Every dependency in the paper's table is declared in both sections → `0 one-way`; and no section judges a position under another question's answer other than its recommendation — the report says, per section, which recommendations each position is judged under.
- **A6** — "Taken together" has one row for each of the goal's steps, failures and screens: a command compares its rows with the goal's → `0 missing, 0 extra`; and every screen in its final list carries R-17's line.
- **A7** — No recommendation widens the search, reads the key table or the reset's record, or adds a goal: the report says, per question, what part of the search or the goal it touches.
- **A8** — The paper is under 20 KB: `wc -c` quoted. The sources are unchanged: their sha256 at the end equals that at the start.
- **A9** — The placement check over this instruction and the trace check over the report, run outside `run`, exit 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOALQ_2026-10-31.md`; `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md`.
- **A10** — The record check exits 0: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/record/check.out`.
- **A11** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-17` prints them beside the `issued` entry.

## 6. Evidence required

For every criterion: the command, its output trimmed but not edited, and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq/_evidence/`, cited by path. Every figure the report gives twice is the same both times, and the `finished` entry's outcome agrees with the report's first paragraph.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`, items 1 to 7.

- **A rival given less than "Given to every position" grants it**, or judged under another answer than the recommended one.
- **The screens drifting.** Answers to 1, 2, 4, 8, 9 and 11 can each add or change a screen; one that does so without saying it in "Taken together" leaves R-17 untested on it.
- **The unruled part of a paper read as ruled.**

## 8. Out of scope — do not touch

`src/`, the brief, the register, the groundwork, the goal, the earlier papers, `CONSTANTS.md`, `_kinds/`; round 4; any commit. Anything found but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-17`. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-17 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md --outcome "<one line: what came of the round, in the words of the report's first paragraph>" --moved "<one line, or nothing>" --account <the same account as your started entry> --by "MR · work · answers to the goal's questions"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · answers to the goal's questions
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOALQ_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.
