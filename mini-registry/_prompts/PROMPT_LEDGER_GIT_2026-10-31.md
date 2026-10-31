---
kind: instruction
commission_id: C-2026-10-31-05
version: 1
session_name: MR · work · ledger under local git
kind_of_work: none — the operations of the estate: putting the coordination's ledger under version control
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/ · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_guards/
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — the owner's ruling on D-2026-10-31-01 ("Local git, no remote", 16:12 Tallinn time, 31 October 2026), which lets the record of what is running be cut over to the ledger before round 2 is issued
model: Sonnet — mechanical, admitting no judgement: the test is the cut-over's own step-0 readings and a git status
effort: medium — a handful of commands; the one risk is a ledger entry changed or left out of the commit
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Sonnet, effort medium — the review re-runs the readings and compares every entry's checksum
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_LEDGER_GIT_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/.git/ · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/.gitignore · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/README.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-ledger-git/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md
running_record: MR — the estate's record is not yet cut over to the ledger; the row was added by hand to /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 2026-10-31 14:15 UTC, before this instruction was issued, and no issued entry is written
---

## The start message

```text
MR · work · ledger under local git
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_LEDGER_GIT_2026-10-31.md
```

---

# INSTRUCTION — Make the coordination folder a git repository on this computer, with no remote, and commit the ledger

**Suggested model: Sonnet, effort medium.** The work is mechanical and the check that decides it can be pointed at (section 7 of the procedure, the first question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · ledger under local git`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Load them with ToolSearch by their full names before any command — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`. Where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`. Only after that may you say it is unavailable, with what you searched, what came back and the exact error. Run every program with `/usr/bin/python3`. You do exactly the task in section 3 and nothing else.

**The estate's record has not been cut over to the ledger**, so **you write no ledger entry.** Your first act is to take up your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: in the Open table, in the row whose Who cell is `MR · work · ledger under local git`, replace the Started cell with the time `date -u` prints. Your last act before starting the review is to close it into the Closed table, with the time and one line on what came of it and what moved. Edit only your own row. Your account, computer and who started you are read as the round-1 instruction, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md`, section 1, says.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — sections 2.5.3 and 9.1, step 0: what the repository must answer.
2. The kind of work is `none`; there is no page of the kind and no skill.
3. `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md` — the coordination's constants: section 5 (the ledger is written by `ledger.py` and nothing else; no entry is ever edited) and section 6 (the map).
4. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md` — the report form.

## 3. The task

In `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination`, which today is no git repository:

1. Before anything else, record the sha256 of every file in `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/` and `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_guards/` into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-ledger-git/_evidence/before.sha256`.
2. `git init` the folder. Add no remote.
3. Write `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/README.md`: three or four sentences saying that the folder holds the ledger of orchestrator events of the owner's orchestrators, one file per event; that every file in it is written by `ledger.py` and by nothing else; and that no entry is ever edited or deleted, a correction being a later entry. Name the procedure, section 9, by its path above.
4. Write `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/.gitignore` listing the two produced files the program rebuilds on every entry, `WHO.html` and `MEASURES.md`, and nothing else.
5. Commit, in one commit, everything else in the folder: `CONSTANTS.md`, `projects.txt`, every file in `_ledger/` and `_guards/`, the README and the ignore list. The commit uses the identity git is already configured with on this Mac; set none. Its message says in one line what it is: the coordination's ledger put under version control on this computer, by the owner's ruling on D-2026-10-31-01.
6. After the commit, record the sha256 of every file in `_ledger/` and `_guards/` again into `after.sha256`, beside the first.

A new entry may be written by the orchestrator while you work. Where `ls /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger` shows a file at commit time that `before.sha256` does not carry, commit it as well and say so; never change one.

## 4. Constraints and standing rules

- Change no file in `_ledger/` or `_guards/`; edit nothing in `CONSTANTS.md` or `projects.txt`. Their checksums before and after are the proof.
- No remote, no push: the owner ruled the history local.
- Touch no other repository; nothing under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` but your evidence, your report and your row.
- Nothing opens a window on the owner's screen. No figure from memory.

## 5. Acceptance criteria

- **A1** — The cut-over's step 0, as the owner ruled it read, holds: `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination rev-parse --show-toplevel` prints `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination`; `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination ls-files _ledger/README.md` prints `_ledger/README.md`; `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination remote -v` prints nothing.
- **A2** — Every entry is committed: `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination ls-files _ledger | grep -c '\.yaml$'` equals `ls /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/*.yaml | wc -l` at the time of the commit.
- **A3** — Nothing is left over: `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination status --porcelain` prints nothing, and `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination status --porcelain --ignored` names only `WHO.html` and `MEASURES.md` as ignored.
- **A4** — No entry changed: `diff before.sha256 after.sha256` shows no line removed or changed (an added line is a new entry, named in the report).
- **A5** — The ledger still reads: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md` exits 1, and its only defect line is `not-cut-over: MR`.
- **A6** — The trace check passes over the report: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md` exits 0.
- **A7** — The row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` taken up and closed by hand.

The round keeps no `round_record.py` record: its every write is a git act or one of the two small files above, and A1 to A4 prove them. The report's `record` line says so.

## 6. Evidence required

For every criterion: the command as run, its output, and the time, kept under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-ledger-git/_evidence/` and cited by path.

## 7. How this round can fail

The kind is `none`; there is no page of the kind.

- **An entry changed by the commit.** Line-ending or attribute rewriting, or an editor touching a file. A4 catches it; set no git attribute and run no formatter.
- **The produced files committed.** `WHO.html` and `MEASURES.md` change with every entry; committed, they make every later status dirty.
- **A remote added "to be safe".** The owner ruled against it.

## 8. Out of scope — do not touch

- The cut-over itself: it is the orchestrator's.
- `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, including its line on keeping the ledger by git, which stays `no`: that line means a repository with a remote.
- The mini registry's own repository and its uncommitted files.

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` set to this file's path and `answers` to `C-2026-10-31-05`; its `ledger` line says the record is not cut over and the row was kept by hand. Record `ls -ld` of each output and its exit code. Do not write the verdict. Then close your row. **Write no `finished` entry.**

## 10. The review

Once your row is closed, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Sonnet and medium, never lower; `prompt` these three lines, word for word:

```text
MR · review · ledger under local git
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_LEDGER_GIT_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, and end with one line: its verdict line as it returned it and its path, or, where it could not run, why. Do not judge it, and route nothing.
