---
kind: instruction
commission_id: C-2026-10-31-33
version: 1
session_name: MR · work · the delivery commit
kind_of_work: none — the operations of the estate: committing both repositories to deliver the two deliverables
upstream_artefact: none — the owner's word, "One commit round, tests fixed (Recommended)", on the question form in MR · orchestrator, 23:42 Tallinn time, 31 October 2026, recorded with the ruling on D-2026-10-31-15
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT4_2026-10-31.md
serves: both deliverables of the constants — the working prototype and the note to the Permanent Secretary, owed when round 8 is accepted; with the history kept local, an artefact is delivered when committed (procedure 2.5.3)
model: Sonnet — mechanical: the tests are git's own readings, compared by command
effort: medium — two repositories, one commit each
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Sonnet, effort medium — the review re-reads both repositories and compares file by file
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_COMMIT4_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/.git/ · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/.git/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-commit4/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT4_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · the delivery commit
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COMMIT4_2026-10-31.md
```

---

# INSTRUCTION — Commit everything waiting in the mini registry and in the coordination, with no push, so that both deliverables are delivered

**Suggested model: Sonnet, effort medium.** Mechanical; git's own readings decide it (section 7 of the procedure, the first question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · the delivery commit`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh). Load it with ToolSearch by its full name before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function and load what comes back by its exact full name; prove the shell with `date -u; hostname`. Run the layer's programs with `/usr/bin/python3`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-33 --session "MR · work · the delivery commit" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COMMIT4_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · the delivery commit"
```

A session that can tell only that a scheduled task started it writes `unknown`. Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a task other than this one and its review is running, stop and say so.

## 2. Read first

`/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`, sections 2.5.3 and 2.5.5; the skill `repo-hygiene` (`/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/repo-hygiene/SKILL.md`), history kept local: commit, never push; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` section 6 and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/.gitignore`; the owner's word that the note is not sent (`/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T205234Z_MR_ruled_D-2026-10-31-14.yaml`), so its PDF stays ignored; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`. Read too the two reviews of the last commit round, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_COMMIT3_2026-10-31.md` and `_v2.md`, section 7 of each: their gaps are the ones this instruction is written to avoid.

## 3. The task

1. **Make a folder with `mktemp -d`; every piece of evidence goes there until step 5.** Name it in the report.
2. In each repository, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` and `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination`, record `git status --porcelain --ignored` into that folder: the "before" list.
3. In each, `git add -A` and commit, one commit each, with the identity git already has; set none. The message: one line, the delivery of the mini registry's two deliverables, committed at the owner's word, then for the mini registry one line per round committed. Push nothing; add no remote; change no ignore list; force-add nothing.
4. **Straight after both commits**, record into the same folder: `git status --porcelain` of each (it must be empty), `git log --oneline -3` and `git show --name-only --format= HEAD` of each.
5. Only then copy the folder's files into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-commit4/_evidence/`, write the report, and write the report's `window` line with `round_record.py window --write`, if it runs on this task's `started` entry; where it does not, keep its command and what it printed, and give the window from `date -u` and `stat` of the report, saying so.

## 4. Constraints

No push, no remote, no change to any file's content, no change to any ignore list. Touch no other repository. Nothing opens a window.

## 5. Acceptance criteria

- **B1** — The status recorded in step 4 is empty in both repositories, quoted from the temporary folder's file.
- **B2** — The files `git show --name-only HEAD` names in each repository are exactly the new and changed paths of its "before" list, compared by a command, file by file → `0 missing, 0 extra`.
- **B3** — After the report is written, `git status --porcelain` of each repository names only: in the mini registry, this round's evidence and report and `WHAT_IS_RUNNING.md`, which the ledger rebuilds at every entry; in the coordination, ledger entries, guard entries and produced files written after the commit's time. A command lists each line with its file's modification time against the commit's time; quoted.
- **B4** — Nothing ignored was committed: `git ls-files -ci --exclude-standard` prints nothing in either; and `docs/note/NOTE.pdf` is not in the commit.
- **B5** — `git remote -v` prints nothing in either.
- **B6** — The report records `ls -ld` of each place written, with its exit code, and its `window` line as step 5 says.
- **B7** — The trace check passes over the report: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT4_2026-10-31.md` exits 0.
- **B8** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-33` prints them.

The round keeps no `round_record.py` record: its writes are git acts and its own evidence, which B1 to B4 prove. The report's `record` line says so.

## 6. The report, and the review

Write the report from the report form, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-33`; do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-33 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT4_2026-10-31.md --outcome "<one line: the two commits, by their hashes and file counts>" --moved "<the two commits; nothing else>" --account <the same account as your started entry> --by "MR · work · the delivery commit"
```

Once it stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Sonnet and medium, never lower; `prompt` these three lines, word for word:

```text
MR · review · the delivery commit
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_COMMIT4_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, and end with one line: its verdict line and its path, or why it could not run.
