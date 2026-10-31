# What is running in the mini registry

**One file. Read it before you start. Before you write anything, write your `started` entry in the
ledger with the command your instruction gives; when you stop, write your `finished` entry, never a
row. The Open and Closed tables below are produced from the ledger — until this record's
orchestrator has cut it over they are written by hand, a row added before you write and closed when
you stop.**

## The three rules

1. **Before you write anything into this estate, write your `started` entry** with the command your
   instruction gives, and read the produced Open block below — that block and nothing else, not a
   frozen table, whose heading says its rows are not open. If a task in that block names a file you
   were going to write, **you do not write it.** Say so to whoever commissioned you, and stop.
2. **When you finish, or when you stop without finishing, write your `finished` entry, never a
   row** — after your report is written, naming the report, with one line saying what
   came of it. A task with no `finished` entry is read as work still in progress.
3. **A change here that others depend on is announced** in the `moved` line of your `finished`
   entry, which is produced into the Closed table below. Anybody depending on this estate reads that
   table to find out what moved under them, because there is no other way for them to find out.

**Whoever raises an instruction writes its `issued` entry when it is raised, not when the work comes
back.** The gap between an instruction being written and a session starting on it is where
collisions happen.

## Open

| Started | Who | What | Files it will write |
|---|---|---|---|

## Closed

| Started | Closed | Who | What | What came of it, and what moved |
|---|---|---|---|---|
| 31 Oct 2026, 12:48 UTC (14:48 EET) | 31 Oct 2026, 12:49 UTC (14:49 EET) | a working session carrying out the project-inception skill, asked directly by the owner; row added by the session on taking the work up | **The inception of this project.** A writing round: the three places for instructions, reports and reviews and this record are made; the map of every other place is put to the owner, and each folder on it is made, with its note, once he has ruled; the constants are written from his answers. If the repository step runs, a repository is made at the project's root, with its ignore list; the first commit is made and pushed to the remote the owner named or agreed to. | Done. The three places, every folder on the map the owner ruled on ("the map as proposed"), each with its note, this record and `CONSTANTS.md` (code `MR`) are made; report `_reports/REPORT_INCEPTION_2026-10-31.md`. Also written, not named in the open row: the four pages copied into `_kinds/` from `../kinds/`, and a new coordination, `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md`, with this project as its first estate. The history is kept on this computer only, by the owner's choice: the repository and its first commit follow this row, and nothing is pushed. **Moved:** nothing; every path is new. |
