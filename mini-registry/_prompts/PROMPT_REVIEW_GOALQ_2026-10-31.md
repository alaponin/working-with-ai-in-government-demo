---
kind: instruction
commission_id: C-2026-10-31-18
version: 1
session_name: MR · review · answers to the goal's questions
kind_of_work: analysis
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOALQ_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOALQ_2026-10-31.md
serves: the verdict on C-2026-10-31-17, the answers to the goal's questions
model: Opus — named in the instruction under review's reviewer line
effort: high — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOALQ_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · answers to the goal's questions
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOALQ_2026-10-31.md
```

---

# INSTRUCTION — Review the report of the paper answering the goal's 13 questions

**Suggested model: Opus, effort high.**

## 1. Role and where to run

You are a reviewing session for the mini registry, `MR · review · answers to the goal's questions`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so. You run on the owner's Mac through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove it with `date -u; hostname`. Run programs with `/usr/bin/python3`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-18 --session "MR · review · answers to the goal's questions" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GOALQ_2026-10-31.md --effort unknown --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · answers to the goal's questions"
```

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the page of the kind, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GOALQ_2026-10-31.md` — its section 2, item 5, says what of each earlier paper is ruled; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GOALQ_2026-10-31.md`, read as it stands — where it is absent, say so and judge nothing; the paper, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL-QUESTIONS-PAPER.md`; the sources; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

The eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-03b-goalq-review/_evidence/`. Change nothing else; repair nothing; commission nothing.

- **The tests** A1 to A11, each on evidence you read or produced.
- **One figure re-established:** the number of screens the goal has once all 13 recommendations are applied, worked out by your own walk through the goal, set beside the paper's "Taken together".
- **What a review of this kind runs** (the analysis page, part 2): every citation read at its source against the sentence that cites it — a shared word is not a source; the 13 questions listed again by you and compared both ways; every dependency listed again by you, and each position read under the recommended answers it depends on; each table read against "Given to every position" and the other position's cells (page items 2, 5, 6 and 7). **A gap is a fault that a ruling on the paper would carry into round 6's build, not a sentence you would word differently; the verdict does not judge whether you would recommend the same.**
- **The mechanical checks**, run directly, not through `round_record.py run`: trace over the report; placement over the instruction under review; `round_record.py check` over the record the report's `record` line names, with the options its `check.out` prints on `# run with:` and an `--out` of your own; `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-17` and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, quoting the lines naming `MR`.
- **The verdict**, each gap with one kind from `FINDING-KINDS.md`, any fault the page lacks named; **found, not fixed.**

## 4. The last act

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-18 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GOALQ_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<count by kind; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · answers to the goal's questions"
```
