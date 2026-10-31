---
kind: instruction
commission_id: C-2026-10-31-07
version: 2
session_name: MR · work · groundwork
kind_of_work: drafting
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T141251Z_MR_ruled_D-2026-10-31-03.yaml · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md
serves: the working prototype, deliverable 1 of the constants — round 2 of the brief, the groundwork: the tables the build reads (the lists, the settings, the search rule)
model: Opus — the content is settled by the brief, the accepted register and the owner's ruling on the thirteen answers; what remains is writing it out exactly as tables, and the risk is a value or a rule that none of the three carries
effort: high — every row of every table must trace to its source, and a rule widened here is built in round 6 and counted in round 7
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review traces every row to its source by its own route and lists the settings again from the brief and the ruling
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GROUNDWORK_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · groundwork
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md
```

---

# INSTRUCTION — Write the groundwork of the mini registry: the settings, the lists and the search rule, as tables the build reads, every row traced to its source

**Suggested model: Opus, effort high.** The brief, the register and the owner's ruling settle the content; the risk is inexactness over every row (section 7 of the procedure, the second question).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · groundwork`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Those tools are deferred: before any command, load them with ToolSearch by their full names — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`. Where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname`; only after that may you say it is unavailable, with what you searched, what came back and the exact error. Run every program, the layer's and your own, with `/usr/bin/python3` (3.9.6), never `python3` (3.7.9). You do exactly the task in section 3 and nothing else.

**The estate's record is cut over to the ledger.** Your first act, once you have read this declaration and before you read anything further, is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-07 --session "MR · work · groundwork" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md --effort <high only where your start shows it, otherwise unknown> --started-by <owner, sub-session or unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · groundwork"
```

It prints the name of the file it wrote as its last line; your report records that name, the exit code and the time. **Your effort**: a session started by the orchestrator's scheduled task cannot see its effort, and writes `unknown`. **Who started you**, from your own prompt only: `owner` where he typed or pasted it, otherwise `unknown`; never guess. **Your account** is read from the line of your own context that names the user's address, in lower case, or `unknown`; never from a file. **Your computer** is what `hostname` prints. Where the command refuses because the task waits for something, write nothing and stop, saying what it printed. Where it cannot run, record that in your report as it stands.

Then read the produced Open block of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: where another task there names a file you were going to write, do not write it — say so in your report and stop.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md` — the page of the kind: part 1 is what you refuse, part 2 what your review runs, part 3 what was checked before this was issued.
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — the standing constraints (section 5): every figure established by a command, nothing real, nothing connected, no window. The project has no `CLAUDE.md`.
5. **The three sources, in order of precedence:**
   - `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md` — the brief, highest; its table of known numbers and its line 13 rule.
   - `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md` — the accepted register, R-01 to R-23.
   - **The owner's ruling on the thirteen answers**, `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/_ledger/20261031T141251Z_MR_ruled_D-2026-10-31-03.yaml`: he ruled the thirteen recommendations "as `docs/GAPS-PAPER.md` lines 26 to 38 give them". **What is ruled** is each of those thirteen summary rows, and the one-sentence recommendation that closes each question's section of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, where it says the same in more words. **Nothing else in that paper is ruled** — not its positions, its tables, its "given to every position" lines, nor any value it proposes in passing. The paper did not pass its review; it is the record of what was ruled, not accepted work.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md` — the report form.

Check the sha256 of each source against these, read 2026-10-31 14:26 UTC; where one differs, stop and say so in the report:
- brief `ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64`
- register `ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103`
- paper `d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb`

## 3. The task

Write the groundwork: the tables the build of rounds 5 and 6 will read, and a short document that explains them. The groundwork describes; it does not make the children — round 5 makes the made-up data from it.

1. **`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/settings.csv`** — one row per setting the build needs: `setting,value,source`. It holds the five known numbers of the brief's table, and every further setting the ruling gives (for example the 68 list entries of G-04). A setting the build needs and no source gives is not a row; it is a gap (item 5).
2. **`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/lists.csv`** — the structure of each table the prototype holds: the three lists (the school census, the examinations authority's candidate list, the social grant programme's list), the learners, and the key table of G-05. One row per field: `table,field,meaning,source`. A field no source names is not a row; it is a gap.
3. **`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/groundwork/search_rule.csv`** — the search rule, one row per thing it does: `part,rule,source` — what it compares (the brief's line 13: family name, given names, date of birth, capitals ignored, nothing else), where it looks (G-03), what it does on none, on exactly one (lines 14 and 15 of the brief) and on more than one (G-02). Nothing it does not compare is forgiven.
4. **`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md`** — one short section per table: what it is for, which round reads it, and its rows' sources in a sentence. The source of every row is in the table itself; the document does not restate them.
5. **A closing section of `GROUNDWORK.md`, "Gaps against the sources"** — each fact the build will need that none of the three sources gives (a value the ruling names but does not fix, such as the fixed date of G-06, or a field the lists need), as a question, left open. Never answer one.

**The `source` column** names exactly one of: `brief:<line>`, `R-<nn>`, or `ruling:G-<nn>`; where a row rests on more than one, separate them by ` · `. A row with no source is not written.

## 4. Constraints and standing rules

- Supply no value, field or rule the sources do not carry (the drafting page, part 1, item 1). A missing one is a gap.
- No figure from memory: every count by a command, with its time.
- The brief, the register and the paper are read and never changed.
- No operation that writes to version control; nothing opens a window on the owner's screen.
- Keep the round's record with `round_record.py`: `start` before your first write into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`; run your checking programs through `run`; `end` after your last write but the report; `check` as your last act before the `finished` entry.

## 5. Acceptance criteria

- **A1 — The set of settings, listed first.** Before the tables are written, list into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/SETTINGS_SET.md`, by a command, the five rows of the brief's table of known numbers with their lines, and every value the ruled recommendations fix, with the question each comes from. Then a command compares that list with `settings.csv` and prints `0 missing, 0 extra`.
- **A2 — Every row traced.** A program saved in the evidence folder reads the three CSVs, and for each row checks that its `source` is of the three forms, that a `brief:<line>` line exists and, for a number, carries that number, that an `R-<nn>` exists in the register, and that a `ruling:G-<nn>` names one of G-01 to G-13 → it prints `0 without source, 0 unresolved`, and the count of rows of each table.
- **A3 — The search rule is the brief's.** A command shows that `search_rule.csv` compares exactly the three fields of the brief's line 13, forgives capitals and nothing else, and does not compare the school → its output, quoted.
- **A4 — The requirements the build reads are covered.** Every requirement in the register's sections "What it must do" and "The made-up data, in known numbers" is cited by at least one row, or is named in `GROUNDWORK.md` with one line saying why the groundwork does not bear on it → a command prints `0 uncovered`.
- **A5** — The closing section "Gaps against the sources" exists; each gap is a question, and no answer to it appears in a table.
- **A6** — The three sources are unchanged at the end: `shasum -a 256` prints the three checksums of section 2.
- **A7** — The placement check passes over this instruction: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GROUNDWORK_2026-10-31.md` exits 0; the trace check passes over the report: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31.md` exits 0.
- **A8** — The round's record check passes: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/record/check.out` exits 0.
- **A9** — The `started` and `finished` entries of this task stand in the ledger, as `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-07` prints them, beside the `issued` entry, each carrying the account the report's declaration names, or `unknown`.

## 6. Evidence required

For every criterion: the command as run, its output trimmed but not edited, and the time, kept under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/` and cited by path. A criterion without evidence is not met. The measurement window closes at the moment of writing.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md`, which this round refuses in itself.

- **The paper read as ruled.** The paper proposes many things in passing — a seed, a date, which of the 8 sit on which two lists. Only the thirteen recommendations are ruled. A value taken from anywhere else in the paper is a value no source gives: a gap.
- **The key table let into the search.** G-05's key table records which entries are the same child for the counts. A rule row that reads it, or a lists row that gives the search access to it, makes round 7's count of the 8 trivially 8.
- **The data made instead of described.** Sixty names, dates or schools written into the groundwork are round 5's work, and none of them has a source.

## 8. Out of scope — do not touch

- `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`, the brief, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/`.
- The goal written in full (round 3) and the made-up data (round 5).
- Any commit: the owner's.
- Anything discovered but not asked for goes to the report under "found, not fixed".

## 9. The report

Write the report named in `downstream_artefact`, from the report form, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`, with `upstream_artefact` set to this file's path and `answers` to `C-2026-10-31-07`. Say which kind of session wrote it. Do not commit or push; send nothing; do not write the verdict. If a file this instruction names does not exist, stop and say so; do not reconstruct it.

After everything else is written, record `ls -ld "<path>"` of each place the round wrote in, with its exit code. Open nothing on the owner's screen.

**The round's last entry is its `finished` entry**, after the report:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-07 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31.md --outcome "<one line: what came of the round, in the words of the report's first paragraph>" --moved "<one line: what changed that later rounds depend on, or nothing>" --account <the same account as your started entry> --by "MR · work · groundwork"
```

## 10. The review

The review instruction was written and issued with this one. Once your `finished` entry stands, your one act is to start it as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork; in the foreground; where the tool takes a model and an effort, Opus and high, never lower; `prompt` these three lines, word for word:

```text
MR · review · groundwork
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GROUNDWORK_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, add nothing, and end with one line: its verdict line as it returned it, and its path — or, where it could not run or the tool could not give the model, that fact. Do not judge it, do not act on it, route nothing.

---

## Version 2 — 31 October 2026, 2026-10-31 14:51 UTC: the gap of the review

The review of version 1, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GROUNDWORK_2026-10-31.md`, is **not accepted** on one gap, G1: the round's record check exits 1 on 10 reads that the layer's placement check made when it was run through `round_record.py run`. The review found nothing wrong in the groundwork itself: every row traced, the set of settings complete, the search rule the brief's. **The cause is this instruction**: its section 4 told the round to run "your checking programs" through `run`, and the layer's own checks read files the start list cannot carry.

This version is carried out by a new session with an empty memory. **It does not redo the groundwork.** The three tables stand as version 1 wrote them, and `GROUNDWORK.md` changes by one added gap. Read the review in full after the declaration. Your `started` and `finished` entries are those of section 1 and section 9, with the same commands but for `--report` in the `finished` entry, which names this version's report, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md`; the program reads the version from this declaration.

**What this version does, in this order:**

1. Record the sha256 of `docs/GROUNDWORK.md` and the three CSVs into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/before.sha256`.
2. Start a new record: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" start --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`.
3. **Add one gap** to the closing section of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GROUNDWORK.md`, "Gaps against the sources", numbered 14, from the review's "found, not fixed", item 2: the ruling on G-05 says that no two different children share all three fields, and does not say whether capitals are ignored in "share"; under the ruling on G-03 the reset would merge two children who differ in capitals only. State it as a question, quote the ruled recommendation's words and the brief's line 13, and leave it open. Change nothing else in the file or the tables.
4. Run the round's own checking programs of version 1 (those of A2, A3 and A4, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork/_evidence/`) again through `round_record.py run`, against the files as they now stand, so that version 2's record holds their result.
5. `end` the record, after your last write but the report.
6. **Run the layer's own checks outside `run`**: the placement check and the trace check of A7, run directly, their output kept as files in the evidence folder.
7. Record the sha256 of the four files again into `after.sha256`, beside the first.
8. `check` the record: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GROUNDWORK_2026-10-31_v2.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02-groundwork-v2/_evidence/record/check.out`, as the last act before the `finished` entry.

**One correction to section 3, item 3**, from the review's "found, not fixed": the brief's line 13 is the outcome on exactly one learner, line 14 on none, and line 15 what the clerk sees. Version 1's table already cites them rightly; nothing in it changes for this.

**The tests of success of this version** (in place of A1 to A8; A9 stands, read for version 2):

- **B1** — `diff before.sha256 after.sha256` shows the three CSVs unchanged and `GROUNDWORK.md` the one file changed; a `diff` of `GROUNDWORK.md` against version 1's copy in the record shows only the added gap 14.
- **B2** — Gap 14 is a question quoting the ruled words and the brief's line 13, and answers nothing.
- **B3** — The round's own checks of A2, A3 and A4, re-run in step 4, print what they printed for version 1, with A4 still `0 uncovered`.
- **B4** — The placement check and the trace check, run outside `run`, exit 0 (the placement check's only findings, if any, the outputs not yet written at the time it ran).
- **B5** — The record check of step 8 exits 0, its `check.out` cited by path.
- **B6** — The three sources are unchanged: `shasum -a 256` prints the checksums of section 2.
