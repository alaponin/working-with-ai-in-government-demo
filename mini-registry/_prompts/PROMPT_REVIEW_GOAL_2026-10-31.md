---
kind: instruction
commission_id: C-2026-10-31-14
version: 2
session_name: MR · review · the goal in full
kind_of_work: drafting
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31_v2.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31_v2.md
serves: the verdict on C-2026-10-31-13, the goal in full
model: Opus — named in the instruction under review's reviewer line
effort: high — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31_v2.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · the goal in full
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOAL_2026-10-31.md
```

---

# INSTRUCTION — Review the report of round 3, the goal in full

**Suggested model: Opus, effort high.**

## 1. Role and where to run

You are a reviewing session for the mini registry, `MR · review · the goal in full`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so. You run on the owner's Mac through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove it with `date -u; hostname`. Run programs with `/usr/bin/python3`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-14 --session "MR · review · the goal in full" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOAL_2026-10-31.md --effort unknown --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · the goal in full"
```

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the page of the kind, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOAL_2026-10-31.md` — its section 2, item 5, says what of each paper is ruled; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOAL_2026-10-31.md`, read as it stands — where it is absent, say so and judge nothing; the goal, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md`; the sources; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

The eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-review/_evidence/`. Change nothing else; repair nothing; commission nothing.

- **The tests** A1 to A10, each on evidence you read or produced.
- **One figure re-established:** the number of failures the sources state or rule, listed again by you from the sources by a route the round did not use, and set beside the goal's.
- **What a review of this kind runs** (the drafting page, part 2): every step and failure looked up at its source — for a `ruling:` source, at the ruled part of its paper only; the sets of steps and of failures listed again by you and compared both ways with the goal, what is missing either way counted; every screen the goal shows checked against its list of screens. Read the goal for each fault of part 1 of the page and the three failures of section 7 of the instruction under review — above all a check or failure no source carries. **A gap is a fault that round 4's count or round 6's build would inherit, not a sentence you would word differently.**
- **The mechanical checks**, run directly, not through `round_record.py run`: trace over the report; placement over the instruction under review; `round_record.py check` over the record the report's `record` line names, with the options its `check.out` prints on `# run with:` and an `--out` of your own; `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-13` and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, quoting the lines naming `MR`.
- **The verdict**, each gap with one kind from `FINDING-KINDS.md`, any fault the page lacks named; **found, not fixed.**

## 4. The last act

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-14 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<count by kind; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · the goal in full"
```

---

## Version 2 — 31 October 2026, 2026-10-31 17:14 UTC: the review of the second attempt

The first edition, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31.md`, found the goal not accepted on G1. The working instruction is now at version 2, which appends G1 and items 1 to 4 of the first edition's "found, not fixed", with tests A11 to A13. This edition is written by a new session with an empty memory, as `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOAL_2026-10-31_v2.md`, beside the first; its evidence goes to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03-goal-v2-review/_evidence/`. Your entries are those of sections 1 and 4, with `--report` in the `finished` entry naming this edition's file.

**What this edition judges:** tests A1 to A13; whether G1 is closed **for every step and failure** — read each "registry does", "clerk sees" and "is saved" against the words of its source yourself, and count those whose source does not carry the fact (a shared word is not enough); and whether items 1 to 4 are closed. The same bar as before: a gap is a fault that round 4's count or round 6's build would inherit.
