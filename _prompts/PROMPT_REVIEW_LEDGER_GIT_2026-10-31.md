---
kind: instruction
commission_id: C-2026-10-31-06
version: 1
session_name: MR · review · ledger under local git
kind_of_work: none — the operations of the estate: putting the coordination's ledger under version control
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_LEDGER_GIT_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_LEDGER_GIT_2026-10-31.md
serves: the verdict on C-2026-10-31-05, the ledger under local git
model: Sonnet — named in the instruction under review's reviewer line; the review re-runs mechanical readings
effort: medium — named in the same line
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_LEDGER_GIT_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-ledger-git-review/_evidence/
running_record: MR — the estate's record is not yet cut over to the ledger; the row was added by hand to /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 2026-10-31 14:15 UTC, before this instruction was issued, and no issued entry is written
---

## The start message

```text
MR · review · ledger under local git
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_LEDGER_GIT_2026-10-31.md
```

---

# INSTRUCTION — Review the report of the round that put the coordination's ledger under local git

**Suggested model: Sonnet, effort medium.**

## 1. Role and where to run

You are a reviewing session for the mini registry, started under the name `MR · review · ledger under local git`. **Who may take it:** a session that neither wrote nor carried out the instruction under review; if you did either, stop and say so.

You run on the owner's Mac through Desktop Commander's `start_process` (zsh). Load it with ToolSearch by its full name before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function and load what comes back by its exact full name; prove the shell with `date -u; hostname`. Run every program with `/usr/bin/python3`.

The estate's record is not cut over, so you write no ledger entry. Your first act is to take up your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` — the Open row whose Who cell is `MR · review · ledger under local git` — with the time `date -u` prints; your very last act is to close it into the Closed table with the verdict and its ground. Edit only your own row. A review started by its working session as a sub-agent is started by `sub-session`.

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`; the review form, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md`; the instruction under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_LEDGER_GIT_2026-10-31.md`; the report under review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md`, which did not exist when this was written — read it as it stands, and where it is absent say so and judge nothing; `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`; and `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`.

## 3. The task, fixed

Review the report against the instruction it answers: the eight things of part one of the review form, in order, written to `downstream_artefact`, evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-ledger-git-review/_evidence/`. Change nothing else; repair nothing; commission nothing; run no git command that writes.

As it falls here:
- **The tests** A1 to A7, each re-run by you, not read from the report.
- **One figure re-established:** the number of ledger entries committed, counted by a route the report did not use (for example `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination show --stat HEAD` against `ls`), and set beside the report's.
- **No entry changed:** compute the sha256 of every file in `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/` and `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_guards/` yourself and compare with the round's `before.sha256`, and compare each committed blob with the file on disk (`git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination diff --stat HEAD` prints nothing for them).
- **The page of the kind and the running application:** not applicable; the kind is `none`.
- **The mechanical checks:** the trace check, `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md`; the placement check over the instruction under review; and `ledger.py check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`. The round kept no `round_record.py` record, by its instruction; say so. Judge the hand row in place of ledger entries.
- **The verdict:** `accepted` or `not accepted`; gaps numbered, each with one kind from `FINDING-KINDS.md`, and the count by kind in one line, since no `finished` entry is written.
- **Found, not fixed.**

## 4. The test of success

A verdict of one of the two kinds; every test A1 to A7 with a line; the count of committed entries re-established; every entry's checksum compared; the checks reported as run or not run with the reason; the hand row taken up and closed.
