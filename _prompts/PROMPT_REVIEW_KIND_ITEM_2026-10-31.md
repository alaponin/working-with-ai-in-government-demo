---
kind: instruction
commission_id: C-2026-10-31-28
version: 1
session_name: MR · review · the pages against the kind item
kind_of_work: none — the method's own work in this estate: amending a page of a kind of work for a kind of gap that recurs
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_KIND_ITEM_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_KIND_ITEM_2026-10-31.md
serves: the verdict on C-2026-10-31-27, the pages against the kind item
model: Sonnet — named in the instruction under review's reviewer line
effort: medium — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_KIND_ITEM_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · the pages against the kind item
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_KIND_ITEM_2026-10-31.md
```

---

# INSTRUCTION — Review the report of the round that amended the page for the kind item

**Suggested model: Sonnet, effort medium.**

## 1. Role and where to run

You are a reviewing session for the mini registry, `MR · review · the pages against the kind item`. **Who may take it:** a session that neither wrote nor carried out the instruction under review. You run on the owner's Mac through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove it with `date -u; hostname`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-28 --session "MR · review · the pages against the kind item" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_KIND_ITEM_2026-10-31.md --effort unknown --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · the pages against the kind item"
```

## 2. The task, fixed

Read the procedure, the review form (`/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`), the instruction under review, its report as it stands (where absent, say so and judge nothing), the three reviews it names and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`. Do the eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-review/_evidence/`; change nothing, repair nothing, commission nothing.

- **The tests** A1 to A5, each on evidence you read.
- **One figure re-established:** list the gaps of kind `item` in the three reviews yourself, from their section 7, and set the count beside the report's.
- **Each gap against its line**: read the page line the report names for each gap, and say whether it would make the next instruction of the kind carry the cure.
- **The mechanical checks**, run directly: the trace check over the report; `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-27`, whose `issued` entry must carry `answers_kind: item`; `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, quoting the lines naming `MR`.
- **The verdict**, each gap with one kind from `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`; **found, not fixed.**

## 3. The last act

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-28 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_KIND_ITEM_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<count by kind; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · the pages against the kind item"
```
