---
kind: instruction
commission_id: C-2026-10-31-02
version: 1
session_name: MR · review · register of requirements
kind_of_work: drafting
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_REQUIREMENTS_2026-10-31.md
serves: the verdict on C-2026-10-31-01, the register of requirements
model: Opus — named in the instruction under review's reviewer line; the review lists the brief's requirements again by its own route and compares row by row, and the risk is a missed row on either side
effort: high — named in the same line; the surface is the whole brief and the whole register
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_REQUIREMENTS_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/
running_record: MR — the estate's record is not yet cut over to the ledger; the row was added by hand to /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 2026-10-31 13:00 UTC, before this instruction was issued, and no issued entry is written
---

## The start message

```text
MR · review · register of requirements
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_REQUIREMENTS_2026-10-31.md
```

---

# INSTRUCTION — Review the report of round 1, the register of requirements, against the instruction it answers

**Suggested model: Opus, effort high.** The instruction under review names it in its reviewer line.


## 1. Role and where to run

You are a reviewing session for the mini registry, started under the name `MR · review · register of requirements`. **Who may take it:** a session that neither wrote nor carried out the instruction under review. If you wrote either, stop and say so rather than reviewing.

You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`. Where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name; prove the shell with `date -u; hostname`. Only after that may you say it is unavailable, with what you searched, what came back and the exact error.

**The estate's record has not been cut over to the ledger**, so you write no ledger entry. Your first act, once this declaration is read, is to take up your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: in the Open table, in the row whose Who cell is `MR · review · register of requirements`, replace the Started cell with the time `date -u` prints. Your very last act, after the review is written, is to close it: move it into the Closed table with the time it closed and one line carrying the verdict and its ground. Your account, computer and who started you are read as the instruction under review, section 1, says; a review started by its working session as a sub-agent is started by `sub-session`.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md` — the review form; part one is what you write.
3. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md` — the page of the kind; part 2 is what you run, part 1 the faults you read the report against.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md` — the instruction under review.
5. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md` — the report under review. **It did not exist when this instruction was written**: read it as it stands. Where it is not at its path, say so and judge no criterion.
6. `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md` — the brief, and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`.
7. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md` — the one list of the kinds a gap carries.

## 3. The task, fixed

Review the report named in `upstream_artefact` against the instruction it answers. Do the eight things of part one of the review form, in that order, and write the review named in `downstream_artefact`. Change nothing else. Repair nothing. Commission nothing. Keep what your commands print in files under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements-review/_evidence/` and cite them by path.

What part one asks for, as it falls in this round:

- **The tests of success** — A1 to A9 of the instruction under review, each with whether it was met and on what evidence you read yourself.
- **One figure re-established** — at least the count of units the inventory marks requirement, worked out again from the brief by a route the report did not use (your own split of the five sections, by your own program or by hand line by line, kept in the evidence folder), and set beside the report's.
- **The outputs exist** — every output the report names, at its path and size, by one command.
- **The running application** — not applicable: no application model was written.
- **What a review of this kind runs** — the drafting page, part 2: every requirement looked up at its line in the brief; the set listed again by you from the brief, compared row by row with the inventory and with the register, and what is missing on either side counted. Read the register for each fault of part 1 of the page, and for the three failures of section 7 of the instruction under review — in particular a search rule wider than "capitals ignored".
- **The four mechanical checks**, each with its command, exit code and log:

```text
python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md
python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md <the further options the round's check.out prints on its line "# run with:">
python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
```

  The record is not cut over, so `ledger.py show` has nothing of this task to print: judge the working session's hand row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` — taken up and closed — in place of its entries, and quote `check`'s lines that name `MR`.
- **The verdict** — `accepted` or `not accepted`. Where not accepted, the gaps numbered G1 onward, their number in the section's first line, each tied to the test it fails and, where it shows a fault of the kind, to the line of the drafting page it breaks; each carries one kind from `FINDING-KINDS.md`; a gap that restates the brief quotes the brief's line beside it. Name any gap that shows a fault the drafting page does not yet carry.
- **Found, not fixed** — what you saw outside the tests.

Since the record is not cut over, write no `finished` entry and no `--kinds`; the count of gaps by kind goes in the review's verdict section instead, one line.

## 4. Constraints

- No figure from memory: every count by a command, with the command and its time.
- No operation that writes to version control; nothing opens a window on the owner's screen.
- About 15 KB: the verdict, the tests with the log cited by path, found-not-fixed. Do not restate the report.

## 5. The test of success

The review carries a verdict of one of the two kinds; every test of success A1 to A9 has a line; the count of requirement units is re-established by another route; every named output was looked for at its path; the drafting page's part 2 is reported as run, with the set listed again and compared both ways; the four mechanical checks are reported as run or as not run with the reason; and the hand row of this review is taken up and closed.
