---
kind: instruction
commission_id: C-2026-10-31-22
version: 1
session_name: MR · review · scaffold and made-up data
kind_of_work: building
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DATA_2026-10-31.md
serves: the verdict on C-2026-10-31-21, the scaffold and the made-up data
model: Opus — named in the instruction under review's reviewer line
effort: high — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DATA_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · scaffold and made-up data
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DATA_2026-10-31.md
```

---

# INSTRUCTION — Review the report of round 5, the scaffold and the made-up data

**Suggested model: Opus, effort high.**

## 1. Role and where to run

You are a reviewing session for the mini registry, `MR · review · scaffold and made-up data`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so. You run on the owner's Mac through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove it with `date -u; hostname`. Run the layer's programs with `/usr/bin/python3`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-22 --session "MR · review · scaffold and made-up data" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_DATA_2026-10-31.md --effort unknown --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · scaffold and made-up data"
```

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the page of the kind, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/building.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md`; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md`, read as it stands — where it is absent, say so and judge nothing; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`; the groundwork's `settings.csv` and the ruled proposals of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md`; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

The eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data-review/_evidence/`. Change nothing in `src/` or anywhere else; repair nothing; commission nothing. **A review of building that ran nothing says so in its first line, and does not accept.**

- **The tests** A1 to A10, each on evidence you read or produced.
- **The project's checks again, in your own run** (the building page, part 2): `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node reset.js && node --test test/`, the result kept.
- **One figure re-established by your own program** (not the round's tests): read the JSON files in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/` with a short program of your own — in Python with `/usr/bin/python3`, so that it shares no code with the round — and count: children, schools and children per school, entries per list, the 8 and their pairs of lists, the 4 spelt differently and on which list, ages on 2026-10-31, learners after reset, and how many of the 8 the brief's rule would join, applying the rule yourself from `search_rule.csv`. Set every number beside the setting or ruling that fixes it.
- **The planted fault** (the building page, part 2, in its spirit here): in a scratch copy of `src/` under your evidence folder, change one thing a check must catch — a fifth child spelt differently, or a date in another form — run the checks there, and see them fail. The real `src/` stays untouched.
- **One use of the screens, and one way the goal can go wrong:** not applicable — round 5 builds no screen and no goal; say so, and instead read the search-rule module against `search_rule.csv`, line by line, since round 6 will use it as it stands.
- **The mechanical checks**, run directly, not through `round_record.py run`: trace over the report; placement over the instruction under review; `round_record.py check` over the record the report's `record` line names, with the options its `check.out` prints on `# run with:` and an `--out` of your own; `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-21` and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, quoting the lines naming `MR`.
- **The verdict**, each gap with one kind from `FINDING-KINDS.md`, any fault the page lacks named; **found, not fixed.** A gap is a fault that round 6's build or round 7's count would inherit.

## 4. The last act

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-22 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DATA_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<count by kind; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · scaffold and made-up data"
```
