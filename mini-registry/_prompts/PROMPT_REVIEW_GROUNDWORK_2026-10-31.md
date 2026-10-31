---
kind: instruction
commission_id: C-2026-10-31-08
version: 2
session_name: MR · review · groundwork
kind_of_work: drafting
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31_v2.md
serves: the verdict on C-2026-10-31-07, the groundwork
model: Opus — named in the instruction under review's reviewer line; every row traced to its source by the reviewer's own route
effort: high — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31_v2.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2-review/_evidence/
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · review · groundwork
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GROUNDWORK_2026-10-31.md
```

---

# INSTRUCTION — Review the report of round 2, the groundwork, against the instruction it answers

**Suggested model: Opus, effort high.**

## 1. Role and where to run

You are a reviewing session for the mini registry, started under the name `MR · review · groundwork`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so.

You run on the owner's Mac through Desktop Commander's `start_process` (zsh). Load it with ToolSearch by its full name before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function and load what comes back by its exact full name; prove the shell with `date -u; hostname`. Run every program with `/usr/bin/python3`.

**Your first act**, once this declaration is read, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-08 --session "MR · review · groundwork" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GROUNDWORK_2026-10-31.md --effort <high where your prompt shows it, otherwise unknown> --started-by sub-session --account <the address your own context names as the user's address, or unknown> --by "MR · review · groundwork"
```

`--started-by` is `sub-session` when the working session started you as a sub-agent, as it is meant to; `owner` where the owner started you. The account is read from your own context only.

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the page of the kind, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md` — its section 2, item 5, says what of the paper is ruled and what is not; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31.md`, which did not exist when this was written — read it as it stands, and where it is absent say so and judge nothing; the three sources it names; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`; and `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

Review the report against the instruction it answers: the eight things of part one of the review form, in order, written to `downstream_artefact`, with your evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-review/_evidence/`. Change nothing else; repair nothing; commission nothing.

As it falls here:
- **The tests** A1 to A9, each on evidence you read or produced yourself.
- **One figure re-established:** the number of settings the sources fix, listed again by you from the brief's table and the ruled recommendations by a route the round did not use, and set beside `settings.csv`'s rows.
- **The outputs exist**, at their paths and sizes, by one command.
- **The running application:** not applicable; nothing runs yet.
- **What a review of this kind runs** (the drafting page, part 2): every row of the three tables looked up at its source — for a `ruling:G-<nn>` row, at the thirteen ruled rows and the closing recommendation of that question's section, and nowhere else in the paper; the set of settings and the set of requirements A4 names listed again by you and compared with the tables and the document, what is missing either way counted. Read the tables for each fault of part 1 of the page and for the three failures of section 7 of the instruction under review — in particular any row that gives the search access to the key table, and any value taken from a part of the paper that was not ruled.
- **The four mechanical checks**, each with command, exit code and log: the trace check over the report (`/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31.md`); the placement check over the instruction under review; `round_record.py check` over the record the report's `record` line names, with the options its `check.out` prints on its line `# run with:` and an `--out` of your own; and the ledger, `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-07`, which must print the `issued`, `started` and `finished` entries, and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, whose lines naming `MR` you quote. Quote the account of each entry beside the report's.
- **The verdict:** `accepted` or `not accepted`; gaps numbered, each tied to its test and, where it shows a fault of the kind, to the page's line; each with one kind from `FINDING-KINDS.md`; name any fault the page lacks.
- **Found, not fixed.**

## 4. The last act

After the review is written, the very last act is the `finished` entry, carrying the verdict:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-08 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31.md --verdict <accepted or not-accepted> [--kinds "<the count of the gaps by kind, as item=2 · trace=1; left out, brackets and all, where there is no gap>"] --outcome "<one line: the verdict and its ground>" --moved nothing --account <the same account as your started entry> --by "MR · review · groundwork"
```

The program refuses a kind not in `FINDING-KINDS.md`; run it again with the kinds as the list names them.

## 5. Constraints and the test of success

No figure from memory; no operation that writes to version control; nothing opens a window; about 15 KB, not restating the report. The review carries a verdict of one of the two kinds; every test A1 to A9 has a line; the number of settings is re-established by another route; every row is looked up at its source; the four mechanical checks are reported as run or not run with the reason; and the `started` and `finished` entries stand.

---

## Version 2 — 31 October 2026, 2026-10-31 14:51 UTC: the review of the second attempt

The first edition, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31.md`, found the groundwork not accepted on one gap, G1: the record check failed on the layer's own reads. The working instruction is now at version 2, which re-establishes the record and adds one gap, and judges by tests B1 to B6 and A9. This edition is written by a new session with an empty memory as `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31_v2.md`, beside the first, which stays as written; its evidence goes to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2-review/_evidence/`. Your `started` and `finished` entries are those of sections 1 and 4, with the same commands, and with `--report` naming this edition's file; the program reads the version from this declaration.

**What this edition judges:** tests B1 to B6 and A9 of the working instruction's version 2, each re-run by you; whether G1 is closed — the record check of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/record` exits 0 when you run it; and that nothing in the groundwork changed but the added gap 14, which you compare yourself against the checksums the first edition recorded. The first edition's tracing of every row stands: re-trace only gap 14 and any line that differs. Re-establish one figure by a route the round did not use.
