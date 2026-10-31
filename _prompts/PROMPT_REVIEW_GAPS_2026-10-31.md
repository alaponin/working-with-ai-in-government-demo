---
kind: instruction
commission_id: C-2026-10-31-04
version: 2
session_name: MR · review · answers to the register's gaps
kind_of_work: analysis
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31_v2.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31_v2.md
serves: the verdict on C-2026-10-31-03, the answers to the register's gaps
model: Opus — named in the instruction under review's reviewer line; the review lists the thirteen questions again and reads every position's cells against the others
effort: high — named in the same line; thirteen questions, four tests each
reviewer: not applicable — this instruction is the review
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31_v2.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2-review/_evidence/
running_record: MR — the estate's record is not yet cut over to the ledger; the row was added by hand to /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 2026-10-31 13:25 UTC for version 1, and again at 2026-10-31 13:45 UTC for version 2, before this version was issued, and no issued entry is written
---

## The start message

```text
MR · review · answers to the register's gaps
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GAPS_2026-10-31.md
```

---

# INSTRUCTION — Review the report of the decision paper on the register's open questions against the instruction it answers

**Suggested model: Opus, effort high.** The instruction under review names it in its reviewer line.

## 1. Role and where to run

You are a reviewing session for the mini registry, started under the name `MR · review · answers to the register's gaps`. **Who may take it:** a session that neither wrote nor carried out the instruction under review. If you wrote either, stop and say so rather than reviewing.

You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`. Where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name; prove the shell with `date -u; hostname`. Only after that may you say it is unavailable, with what you searched, what came back and the exact error. Run every program with `/usr/bin/python3` (3.9.6), not `python3` (3.7.9).

**The estate's record has not been cut over to the ledger**, so you write no ledger entry. Your first act, once this declaration is read, is to take up your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: in the Open table, in the row whose Who cell is `MR · review · answers to the register's gaps`, replace the Started cell with the time `date -u` prints. Your very last act, after the review is written, is to close it: move it into the Closed table with the time it closed and one line carrying the verdict and its ground. Edit only your own row. Your account, computer and who started you are read as the instruction under review, section 1, says; a review started by its working session as a sub-agent is started by `sub-session`.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REVIEW-template.md` — the review form; part one is what you write.
3. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md` — the page of the kind; part 2 is what you run, part 1 the faults you read the paper against.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md` — the instruction under review.
5. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md` — the report under review. **It did not exist when this instruction was written**: read it as it stands. Where it is not at its path, say so and judge no criterion.
6. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`.
7. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md` — the one list of the kinds a gap carries.

## 3. The task, fixed

Review the report named in `upstream_artefact` against the instruction it answers. Do the eight things of part one of the review form, in that order, and write the review named in `downstream_artefact`. Change nothing else. Repair nothing. Commission nothing. Keep what your commands print in files under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-review/_evidence/` and cite them by path.

What part one asks for, as it falls in this round:

- **The tests of success** — A1 to A9 of the instruction under review, each with whether it was met and on what evidence you read yourself.
- **One figure re-established** — at least the number of open questions, listed again by you from the register's closing section by a route the round did not use, and set beside the paper's.
- **The outputs exist** — every output the report names, at its path and size, by one command.
- **The running application** — not applicable: no application model was written.
- **What a review of this kind runs** — the analysis page, part 2: every citation of the paper read at its source against the sentence that cites it; the set of questions listed again and compared with what the paper covers; each question's table read test by test, every fact a judgement rests on looked up in the other position's cells. Read the paper for each fault of part 1 of the page and for the three failures of section 7 of the instruction under review — in particular any recommendation that would let the search forgive more than capitals, directly or through the data's record of which entries are the same child.
- **The four mechanical checks**, each with its command, exit code and log:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md
/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md <the further options the round's check.out prints on its line "# run with:", with an --out of your own under your evidence folder>
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
```

  The record is not cut over, so `ledger.py show` has nothing of this task to print: judge the working session's hand row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` — taken up and closed — in place of its entries, and quote `check`'s lines that name `MR`.
- **The verdict** — `accepted` or `not accepted`. Where not accepted, the gaps numbered G1 onward, their number in the section's first line, each tied to the test it fails and, where it shows a fault of the kind, to the line of the analysis page it breaks; each carries one kind from `FINDING-KINDS.md`; a gap that restates a source quotes the source's line beside it. Name any gap that shows a fault the analysis page does not yet carry. The verdict judges whether the paper does what the instruction asks — positions at their strongest, every citation true, every question answered with a recommendation — never whether you would recommend the same.
- **Found, not fixed** — what you saw outside the tests.

Since the record is not cut over, write no `finished` entry and no `--kinds`; the count of gaps by kind goes in the review's verdict section instead, one line.

## 4. Constraints

- No figure from memory: every count by a command, with the command and its time.
- No operation that writes to version control; nothing opens a window on the owner's screen.
- About 15 KB: the verdict, the tests with the log cited by path, found-not-fixed. Do not restate the report or the paper.

## 5. The test of success

The review carries a verdict of one of the two kinds; every test of success A1 to A9 has a line; the number of questions is re-established by another route; every named output was looked for at its path; the analysis page's part 2 is reported as run, with every citation read at its source and the set compared both ways; the four mechanical checks are reported as run or as not run with the reason; and the hand row of this review is taken up and closed.

---

## Version 2 — 31 October 2026, 2026-10-31 13:45 UTC: the review of the second attempt

The first edition of this review, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31.md`, found the paper not accepted, with gaps G1 to G3. The working instruction is now at its version 2, which appends those gaps and tests A10 to A12. This version reviews the second attempt: the report `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31_v2.md`, the paper as it now stands, and the round's record at `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2/_evidence/record`. It is written by a new session with an empty memory, as a new edition, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31_v2.md`, beside the first, which stays as it was written. Your evidence goes to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2-review/_evidence/`. Everything above governs, read with these paths; your hand row is the open row whose Who cell is `MR · review · answers to the register's gaps`.

**What this edition judges, beyond the first:** tests A1 to A12 of the working instruction's version 2. Whether each of G1, G2 and G3, and the first edition's "found, not fixed" items 2, 4 and 5, is closed — **for every question, not only the ones the first edition named**: list again for yourself, by command, the register lines that name each gap, and read every table again for a setting credited to one position while open to another, and for a cell the paper contradicts elsewhere. A gap closed only for the examples the first edition named is not closed. Re-establish one figure by a route the round did not use, as before.
