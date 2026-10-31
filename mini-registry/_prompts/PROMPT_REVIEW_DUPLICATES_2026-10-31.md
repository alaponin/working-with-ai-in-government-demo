---
kind: instruction
commission_id: C-2026-10-31-30
version: 1
session_name: MR · review · the duplicates count
kind_of_work: checking
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/search_rule.csv · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DUPLICATES_2026-10-31.md
serves: the verdict on C-2026-10-31-29, the duplicates count
model: Opus — named in the instruction under review's reviewer line
effort: high — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DUPLICATES_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · the duplicates count
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DUPLICATES_2026-10-31.md
```

---

# INSTRUCTION — Review the report of round 7, the duplicates count

**Suggested model: Opus, effort high.**

## 1. Role and where to run

You are a reviewing session for the mini registry, `MR · review · the duplicates count`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so. You run on the owner's Mac through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove it with `date -u; hostname`. Run the layer's programs with `/usr/bin/python3`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-30 --session "MR · review · the duplicates count" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DUPLICATES_2026-10-31.md --effort unknown --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · the duplicates count"
```

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the page of the kind, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/checking.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DUPLICATES_2026-10-31.md`; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DUPLICATES_2026-10-31.md`, read as it stands — where it is absent, say so and judge nothing; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/DUPLICATES.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/count/duplicates.csv`; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/search_rule.csv`; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

The eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-07-duplicates-review/_evidence/`. Change nothing under `src/`, and do not run the reset; repair nothing; commission nothing.

- **The tests** A1 to A9, each on evidence you read or produced.
- **The figure re-established by the second route** (the checking page, part 2 and part 3; the route is named here so that the report cannot borrow it): **do not read `enrolments.json` or `src/lib/search.js`.** With a program of your own, in Python with `/usr/bin/python3`, read the three list files and `key_table.json` in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/`, take each child the key table names on two entries, and apply the brief's rule yourself, as `search_rule.csv` gives it — family name, given names and date of birth equal, capitals ignored, nothing else forgiven. Count the children whose entries the rule joins. Set your figure and your eight rows beside the round's; where they differ, name the child and say which route is right, from the rule.
- **The check repeated on another member** (part 2): for two of the 8 the round did not quote in its report, read both list entries yourself and say whether the rule joins them.
- **The planted fault** (part 2): give the round's counting program a copy of `enrolments.json` — copied without keeping file times — in which one child's entries are moved apart, and see the figure change.
- **The mechanical checks**, run directly: trace over the report; placement over the instruction under review; `round_record.py check` over the record the report's `record` line names, with the options its `check.out` prints on `# run with:` and an `--out` of your own; `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-29` and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, quoting the lines naming `MR`.
- **The verdict**, each gap with one kind from `FINDING-KINDS.md`; **found, not fixed.** A gap is a fault the note to the Permanent Secretary would carry: a figure, a row or a reason that does not hold.

## 4. The last act

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-30 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DUPLICATES_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<count by kind; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · the duplicates count"
```
