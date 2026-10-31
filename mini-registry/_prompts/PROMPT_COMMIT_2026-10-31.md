---
kind: instruction
commission_id: C-2026-10-31-09
version: 1
session_name: MR · work · commit of the day
kind_of_work: none — the operations of the estate: committing the day's files in the two local repositories
upstream_artefact: none — the owner's word, "Commit both now (Recommended)", on the question form in MR · orchestrator, 17:05 Tallinn time, 31 October 2026, recorded with the ruling on D-2026-10-31-04
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — an artefact is delivered when it is committed, the history being kept local (procedure 2.5.3), and nothing since inception is
model: Sonnet — mechanical, admitting no judgement: the test is a clean git status in each repository and every file accounted for
effort: medium — two repositories, one commit each; the one risk is a file committed that the ignore list keeps out, or one left out
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Sonnet, effort medium — the review re-reads both repositories' status and log
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_COMMIT_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/.git/ · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/.git/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-commit/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · commit of the day
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COMMIT_2026-10-31.md
```

---

# INSTRUCTION — Commit the day's files in the mini registry's repository and in the coordination's, with no push

**Suggested model: Sonnet, effort medium.** Mechanical; the check that decides it is `git status` (section 7 of the procedure, the first question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · commit of the day`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh). Load it with ToolSearch by its full name before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`; where that exact name is absent, search by function and load what comes back by its exact full name; prove the shell with `date -u; hostname`. Run every program with `/usr/bin/python3`. You do exactly the task in section 3.

**Your first act**, once you have read this declaration, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-09 --session "MR · work · commit of the day" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COMMIT_2026-10-31.md --effort unknown --started-by <owner, sub-session or unknown, from your own prompt> --account <the address your own context names as the user's address, or unknown> --by "MR · work · commit of the day"
```

Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where a task other than this one and its review is **running**, stop and say so; a task that is only issued or waiting does not stop you.

## 2. Read first

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`, sections 2.5.3 and 2.5.5.
2. The kind is `none`; no page of the kind.
3. The skill `repo-hygiene`, at `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/repo-hygiene/SKILL.md` — follow it for the sweep of each repository, with "the history is kept local": commit, never push.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`, section 6 (**Where the history is kept:** `local`), and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/.gitignore`.
5. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

## 3. The task

In each of the two repositories, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` and `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination`:

1. Record `git status --porcelain --ignored` before anything, into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-commit/_evidence/`.
2. Stage every file `git status` shows as new or changed and the ignore list does not keep out — `git add -A` — and nothing the ignore list keeps out. Edit no file to do it, and change no ignore list.
3. Commit, one commit per repository, with the identity git is already configured with; set none. The message: one line saying it is the day's work of 31 October 2026 committed at the owner's word, then, for the mini registry, one line per round naming its instruction file. Push nothing; add no remote.
4. Record `git status --porcelain --ignored`, `git log --oneline -3` and `git show --stat HEAD` after, into the evidence folder.

A new ledger entry may be written in `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/` while you work, by this task's own entries among others. Your `started` entry is written before the commit and is committed with it; your `finished` entry, written after, stays uncommitted, and the report says so.

## 4. Constraints

- No push, no remote, no change to any ignore list, no edit of any file's content.
- Commit nothing the ignore list keeps out; force-add nothing.
- Touch no other repository. Nothing opens a window on the owner's screen.

## 5. Acceptance criteria

- **A1** — `git -C /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry status --porcelain` and `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination status --porcelain`, run straight after the two commits and before anything else is written, print nothing; the report quotes both outputs.
- **A2** — Each repository holds one new commit, `git log --oneline -3` quoted, and `git remote -v` prints nothing in either.
- **A3** — Nothing ignored was committed: `git -C <repo> ls-files -ci --exclude-standard` prints nothing in either.
- **A4** — No file's content was changed by the round: for each repository, the count of files in `git show --stat HEAD` equals the count of new and changed lines in the "before" status, and the report gives both.
- **A5** — The trace check passes over the report: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT_2026-10-31.md` exits 0.
- **A6** — The `started` and `finished` entries of this task stand in the ledger, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-09` prints them.

The round keeps no `round_record.py` record: its writes are git acts and its own evidence, which A1 to A4 prove. The report's `record` line says so.

## 6. Evidence required

For every criterion: the command, its output and the time, under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-commit/_evidence/`, cited by path.

## 7. How this round can fail

The kind is `none`; no page.
- **The report and evidence left out of the commit.** They are written after the commit; that is expected, and the report says which files of this round stand uncommitted — never a second commit made to chase them.
- **A produced file committed.** `WHO.html` and `MEASURES.md` are ignored in `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination`; nothing forces them in.

## 8. Out of scope

Any file's content; any push; the plugin; any repository but the two.

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` `none — the owner's word, as the declaration gives it` and `answers` `C-2026-10-31-09`. Record `ls -ld` of each place written. Do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-09 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_COMMIT_2026-10-31.md --outcome "<one line: the two commits, by their hashes and file counts>" --moved "<one line: the two commits; nothing else>" --account <the same account as your started entry> --by "MR · work · commit of the day"
```

## 10. The review

Once your `finished` entry stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Sonnet and medium, never lower; `prompt` these three lines, word for word:

```text
MR · review · commit of the day
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_COMMIT_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, and end with one line: its verdict line and its path, or why it could not run. Do not judge it; route nothing.
