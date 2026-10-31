---
kind: instruction
commission_id: C-2026-11-01-01
version: 1
session_name: MR · orchestrator · from 2026-11-01
kind_of_work: none — the change of hands of the orchestrator role for the mini registry
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_records/HANDOVER_2026-11-01.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_FIRST_TASK_2026-11-01.md
serves: the change of hands on the mini registry — the role passes at the incoming session's taken-up entry, and this file is the report of its first task
model: Opus — the content is the constants and the produced state, and the work is exact: reading documents of record and running the programs that produce the views
effort: high — the work is exact and the programs that produce the views are the test
reviewer: the outgoing session does not review this; the owner reads the result file
review_instruction: none
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_FIRST_TASK_2026-11-01.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, by the outgoing session, once this file is complete and before its given-up entry
---

## The start message

```text
MR · orchestrator · from 2026-11-01
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_FIRST_TASK_2026-11-01.md
```

---

# FIRST TASK — take up the orchestrator role for the mini registry

## 1. Role and where to run

You are the incoming orchestrator session for the mini registry, started under the name `MR · orchestrator · from 2026-11-01`, and you do not yet hold the role: you hold it from your `taken-up` entry of step 0. The name begins with the orchestrator's code, which every session you later commission carries in turn (section 6.5 of the procedure). Run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh): load it with ToolSearch by its full name, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or, where that exact name is absent, search by function and load what comes back by its exact full name; prove it with `date -u; hostname`. Run the layer's programs with `/usr/bin/python3`, never `python3` (3.7.9 on this Mac). Do exactly the five steps of section 3, in order, step 0 first, and stop.

Once you have read the declaration block above, and before you read anything further, write this task's `started` entry in the ledger of orchestrator events:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-11-01-01 --session "MR · orchestrator · from 2026-11-01" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_FIRST_TASK_2026-11-01.md --account <the address your own context names as the user's address, or unknown> --by "MR · orchestrator · from 2026-11-01"
```

**Your account**, on this entry and on every entry below that records your own act, is read from one line of your own context: the line that names the user's address — for a Cowork session, the system-supplied sentence that begins "The user's email address is" — in lower case; where your context names none, write `unknown`, and on the `taken-up` below add `--account-word` with the owner's word on it, quoted: the program refuses the entry without an account, and `unknown` without that word. Never take it from a file on the machine.

What the instruction form says of a session without a shell on the computer the session runs on, and of a command that cannot run, holds here word for word. The estate's record of what is running is cut over to the ledger (2026-10-31 14:25 UTC).

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — what the project is for, what it delivers, what governs it, where each kind of thing lives.
3. The handover note named in `upstream_artefact`.

Read nothing else. The estate is not surveyed by this task.

## 3. The task, in five steps

0. **Write the `taken-up` entry**, before step 1, naming your predecessor, the handover note and this task:

   ```text
   /usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" taken-up --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --session "MR · orchestrator · from 2026-11-01" --estate "the mini registry" --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md --constants-of-estate /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --predecessor "MR · orchestrator" --handover /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_records/HANDOVER_2026-11-01.md --first-task /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_FIRST_TASK_2026-11-01.md --account <the address your own context names as the user's address, or unknown with --account-word "<the owner's word, quoted>"> --by "MR · orchestrator · from 2026-11-01"
   ```

   The program refuses it while the code has a holder with no `given-up` after it, and prints the remedy. The outgoing session writes its `given-up` as its last act; where it has not, and the owner has said that it is gone, first write the `given-up` on its behalf, then the `taken-up`:

   ```text
   /usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" given-up --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --session "MR · orchestrator" --for "MR · orchestrator" --handover /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_records/HANDOVER_2026-11-01.md --successor "MR · orchestrator · from 2026-11-01" --reason "<the owner's word that the holder is gone, and its date>" --account arne.laponin@gmail.com --by "MR · orchestrator · from 2026-11-01"
   ```

   (`arne.laponin@gmail.com` is the account the holder's own `taken-up` carries; `where --code MR` prints it on its holder line — check it there before you use it.)
1. **Read the constants.** Say, in one paragraph, what the project delivers and by when, and where each of the three kinds of document lives.
2. **Produce the state.** Run the programs that produce the views, then the ledger's `check` and `who`, and report what each printed, with the command, its exit code and the time. Produce them; do not write them.

   ```text
   /usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" views --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR
   /usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" check --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
   /usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" who --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md
   ```

   The register of instructions is not yet in the travelling layer (section 11 of the procedure); say so. The project keeps no record of a long delivery; say so.
3. **Check the named claims.** For each claim in section 4 below, run the check named there and report what it returned. A claim that the check confirms is a fact from that moment; a claim the check contradicts is a finding; a claim that cannot be checked stops this task (section 5).
4. **Write the result file** named in `downstream_artefact`: the paragraph from step 1, the outputs of step 2, and one row per claim from step 3, with what was run and what came back. No more than 15000 bytes. Give its full path, list it with `ls -ld` and its exit code, and then write this task's `finished` entry:

   ```text
   /usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-11-01-01 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_FIRST_TASK_2026-11-01.md --outcome "<one line: what the result file comes to>" --moved nothing --account <the address your own context names as the user's address, or unknown> --by "MR · orchestrator · from 2026-11-01"
   ```

   Write nothing else anywhere. Beyond the result file, the one thing this task writes is its own entries in the ledger — `started`, `taken-up`, the `given-up` on a gone holder's behalf where one is owed, `finished`, and, once the owner has read the result, `closed`. What `views` and `who` rebuild is produced, not written.

## 4. The claims to be checked

*Supplied by the outgoing session, which writes this task from the form, and by nobody else.*

| # | The claim | Where it can be checked |
|---|---|---|
| 1 | No task of MR is open, and the ledger's check is clean | `ledger.py who` and `ledger.py check` over `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md` (step 2's output) |
| 2 | Both deliverables are committed: the prototype under `src/` and the note's source `docs/NOTE.md` in commit `8484d16`, with `docs/note/NOTE.pdf` not tracked; the coordination's ledger in commit `ab3cc36` | `git -C /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry show --stat 8484d16 -- src docs/NOTE.md`, `git -C /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry ls-files docs/note/NOTE.pdf` (prints nothing), `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination log --oneline -1 ab3cc36` |
| 3 | The prototype's checks pass, 57 of 57, and the window checks add no window | `cd /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src && node reset.js && node --test test/` |
| 4 | The `closed` entry of C-2026-10-31-27 misstates its ground: the review's version 2 did name `MR C-2026-10-31-27` as its subject | `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T215347Z_MR_closed_C-2026-10-31-27.yaml` against `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-28` |
| 5 | Everything written after the delivery commit is uncommitted, as the handover note's section 2 lists | `git -C /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry status --porcelain` and `git -C /Users/arnelaponin/Documents/Dev/wai-demo/_coordination status --porcelain` |

## 5. The stopping rule

**At the first claim that cannot be checked, stop.** Write what you have, name the claim, say what would be needed to check it, and hand the file over as it stands. Do not work around it, do not substitute a different check, and do not proceed to the remaining claims. A first task that stopped and said where is worth more than one that completed approximately.

## 6. Out of scope — do not touch

- Any instruction, report, review or engagement artefact. This task commissions nothing, writes no instruction, judges nothing and changes nothing; its own entries in the ledger, named in step 4, are the one thing it writes outside the result file.
- The handover note, which is the outgoing session's record.
- Any version-control operation that writes.

## 7. The test of success

The result file exists at its path, within its size; it carries the paragraph from the constants, the output of every program that produces a view, and one row per claim with the command that checked it; and either every claim has a row or the file names the claim at which the task stopped.

## 8. What follows

The owner reads the result file, the report of this first task; the role passed earlier, at step 0's `taken-up`. This session then closes the task with one entry, which records the owner's act and judges nothing of its own:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" closed --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-11-01-01 --outcome accepted --ground "the owner read the result file /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_FIRST_TASK_2026-11-01.md on <the date>" --account <the address your own context names as the user's address, or unknown> --by "MR · orchestrator · from 2026-11-01"
```

The change of hands stands in the ledger as the outgoing session's `given-up` and this session's `taken-up`, and the registry of orchestrators produced from them shows it; neither session writes a row for it.
