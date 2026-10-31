---
kind: instruction
commission_id: C-2026-10-31-03
version: 2
session_name: MR · work · answers to the register's gaps
kind_of_work: analysis
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md (sha256 ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103, accepted by the review of 13:18 UTC, 31 October 2026)
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md (sha256 ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64) · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_REQUIREMENTS_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31_v2.md
serves: the working prototype, deliverable 1 of the constants — the answers round 2 of the brief, the groundwork, needs before it can be drafted without supplying facts the brief does not carry
model: Opus — the positions are bounded by the brief and the register, and each choice is small and reversible for a prototype made for agreement; the risk is a position stated weakly or a passage misquoted, not a judgement that must be free to overturn the owner
effort: high — thirteen questions, each with at least two positions read against the same tests, and a recommendation that rounds 2, 3, 5 and 7 will build on
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review lists the thirteen questions again from the register and reads every position's cells against the others
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GAPS_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31_v2.md
running_record: MR — the estate's record is not yet cut over to the ledger; the row was added by hand to /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 2026-10-31 13:25 UTC for version 1, and again at 2026-10-31 13:45 UTC for version 2, before this version was issued, and no issued entry is written
---

## The start message

```text
MR · work · answers to the register's gaps
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md
```

---

# INSTRUCTION — Write the decision paper that answers the register's open questions G-01 to G-13, each with its positions and a recommendation, for the owner's ruling

**Suggested model: Opus, effort high.** The brief and the register bound every position; the risk is inexactness in stating and judging them, not open judgement (section 7 of the procedure).

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · answers to the register's gaps`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Those tools are deferred: before any command on the Mac, load them with ToolSearch by their full names — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`. Where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname` and record the tool name and the output. Only after that may you say the shell is unavailable, stating what you searched, what came back and the exact error. You do exactly the task in section 3 and nothing else.

**The estate's record of what is running has not been cut over to the ledger**, so **you write no ledger entry.** Your first act, once you have read this declaration, is to take up your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: in the Open table, in the row whose Who cell is `MR · work · answers to the register's gaps`, replace the Started cell with the time `date -u` prints, as `31 Oct 2026, HH:MM UTC`. Your last act before starting the review (section 10) is to close it: move that row into the Closed table, with the time it closed and one line saying what came of the round and what moved. Edit only your own row.

**Your account**, for your report's declaration, is the address the line of your own context names as the user's address, in lower case, or `unknown`; never from a file on the machine. **Your computer** is what `hostname` prints. **Who started you** is read from your own prompt: `owner` where the owner typed or pasted it, otherwise `unknown`.

**The interpreter.** `python3` on this shell is 3.7.9, which `round_record.py run` cannot trace (the review of round 1, "found, not fixed", item 4). Run every program of the layer, and every program you write, with `/usr/bin/python3` (3.9.6).

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure; section 5 is how a decision is closed.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md` — the page of the kind of work: the faults an analysis refuses (part 1), what its review runs (part 2), and what was checked before this instruction was issued (part 3).
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — the standing constraints (section 5). The project has no `CLAUDE.md`.
5. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md` — the register, and its closing section **Gaps against the brief**. Check its sha256 against the declaration first; where it differs, stop and say so in the report.
6. `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md` — the brief, the document that governs the project, highest in precedence. Check its sha256 against the declaration.
7. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_REQUIREMENTS_2026-10-31.md` — the review of round 1; its section 8 bears on G-14 and on R-05.
8. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md` — the report form.

## 3. The task

Write `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`, a short decision paper that answers the register's open questions **G-01 to G-13**, so that the owner can rule on them in one act and round 2, the groundwork, can be drafted from the brief, the register and his ruling without supplying a fact any of them lacks.

**First, the set.** List the thirteen questions from the register's section **Gaps against the brief**, each quoted word for word with the requirements it names, into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/QUESTIONS.md`, by a command, and count them by a command. G-14 is not among them: the orchestrator has closed it from the brief, whose line 13 reads "(capitals ignored)", so nothing but capitals is forgiven and a space is part of a name. The paper records G-14 as closed in one line quoting that passage, and does not reopen it.

**Then, for each of G-01 to G-13:**
- the question, quoted, with the requirements it bears on;
- every passage of the brief or the register that bears on it, quoted with its path and line — or the statement that none does;
- **at least two positions**, each stated at its strongest from those passages before either is judged;
- one table, position by test, against these four tests, the same for every question: **(a)** what the brief's section "What it is for" says the prototype is for — a small working prototype, for agreement, not the registry; **(b)** the brief's "must not" sentences; **(c)** the known numbers, so that every later count has a known answer (the brief's lines on the made-up data); **(d)** what the later rounds of the brief must be able to do with it — round 5's made-up data, round 6's goal built, round 7's count of the 8 duplicates;
- **a recommendation**, in one sentence, with its ground in a line, marked as a proposal for the owner's ruling and never as a decision.

Open the paper with a summary table: one row per question, the recommendation in a few words. Keep the paper to what the owner reads in one sitting: the summary, then one short section per question.

## 4. Constraints and standing rules

- The paper recommends; it decides nothing (the analysis page, part 1, item 1). Write "we recommend", never "the registry will".
- No fact, rule or figure from memory: every passage quoted from its file with its line, every count by a command with its time.
- Where the brief and a position disagree, the brief governs; a position that would contradict a sentence of the brief is stated with that sentence beside it and is not recommended.
- The brief and the register are read and never changed.
- No operation that writes to version control. Nothing opens a window on the owner's screen.
- Keep the round's record with `round_record.py`, as the report form's `record` line requires: `start` before your first write into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`, run your listing program through `run`, `end` after your last write but the report, and `check` as your last act before closing your row.

## 5. Acceptance criteria

- **A1** — The set: `QUESTIONS.md` lists G-01 to G-13, each quoted word for word from the register, and a command prints `13`; a second command shows each quoted question is a substring of `docs/REQUIREMENTS.md` → `0 not found`.
- **A2** — Coverage both ways: a command compares the questions in `QUESTIONS.md` with the sections of `docs/GAPS-PAPER.md` and prints `0 unanswered, 0 extra`.
- **A3** — Every passage the paper quotes from the brief or the register is found in its file at the line it gives: a command prints `0 not found, 0 wrong line`.
- **A4** — Every question has at least two positions, a table against the four tests (a) to (d), and one recommendation marked as a proposal: a command prints, per question, the number of positions, of table rows and of recommendations, and the report states that every row reads at least 2, 4 and 1.
- **A5** — G-14 is recorded as closed in one line quoting the brief's line 13, and no recommendation in the paper forgives anything but capitals in the search.
- **A6** — The brief and the register are unchanged at the end: `shasum -a 256` prints the two checksums the declaration gives.
- **A7** — The placement check passes over this instruction: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_GAPS_2026-10-31.md` exits 0; and the trace check passes over the report: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md` exits 0.
- **A8** — The round's record check passes: `/usr/bin/python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/record/check.out` exits 0, its `check.out` cited by path.
- **A9** — The record is not cut over, so in place of ledger entries: the row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` taken up with its start time and, at the end, closed into the Closed table.

## 6. Evidence required

For every criterion: the command as run, its output trimmed but not edited, and the time, kept in files under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps/_evidence/` and cited by path. A criterion without evidence is not met. The measurement window closes at the moment of writing.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`, which this round refuses in itself and which this section does not retype.

The ways this round goes wrong while appearing to succeed:

- **The thin second position.** A question with one real answer and a straw man beside it looks covered and is not. Where the brief leaves only one position open, say so and quote why, rather than inventing a weak rival.
- **The search rule widened by the back door.** G-02 (more than one match), G-03 (where the search looks) and G-05 (how the data marks the same child) can each be answered in a way that makes the search forgive spelling — by matching on a list's record of sameness rather than on the three fields. Round 7 counts how many of the 8 the brief's rule catches; a recommendation that makes that count trivially 8 has changed the brief.
- **Growing the prototype.** A recommendation that adds a goal, a screen, a body to connect to or a field the clerk enters fails test (a); say so in its table row.

## 8. Out of scope — do not touch

- `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`, the brief, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/`.
- The groundwork itself (round 2): this round answers questions, it does not draft tables.
- Any commit: the owner's.
- Anything discovered but not asked for goes to the report under "found, not fixed", not into the work.

## 9. The report

Write the report named in `downstream_artefact`, from `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`. Set its `upstream_artefact` to this file's path; set its `answers` to `C-2026-10-31-03`; and its `ledger` line says that the record is not cut over and the row was kept by hand. Say which kind of session wrote it. Do not commit or push; do not send anything to anybody; do not write the verdict — the verdict is the review's.

If a file this instruction names does not exist, stop and say so in the report. Do not reconstruct it from memory or from inference.

After everything else is written, the report records, for each place the round wrote in, `ls -ld "<path>"` and its exit code. Open nothing on the owner's screen.

Then close your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` by hand, as section 1 says. **Write no `finished` entry**: the record is not cut over.

## 10. The review

The orchestrator wrote and issued the review of this task together with this instruction: the declaration's `review_instruction` line names it. Once your row is closed, your one act is to start that review yourself, automatically, as a sub-agent with your Agent tool:

- `subagent_type`: `general-purpose` — never a fork; the review has a fresh context;
- in the foreground, because your next act depends on it;
- `prompt`: these three lines, word for word:

```text
MR · review · answers to the register's gaps
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_GAPS_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

- where the Agent tool takes a model and an effort, as its own description says at the moment of use, Opus and effort high, and never lower.

Never create a scheduled task to start it. Wait for the sub-agent, add nothing to it, and end with one line: the review's verdict line as it returned it, and the review's path. Where the sub-agent could not reach the Mac, or the Agent tool cannot give the model named, say so in that one line instead; the orchestrator starts the review at its next "check". Do not judge the review, do not act on its verdict, and route nothing.

---

## Version 2 — 31 October 2026, 2026-10-31 13:45 UTC: the gaps of the review

The review of version 1, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_GAPS_2026-10-31.md`, is **not accepted**, with three gaps. Its section 7 states them, with every line they rest on; read it in full before anything else, after the declaration. This version is carried out by a new session with an empty memory. It changes the paper in place, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GAPS-PAPER.md`; it keeps its evidence in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2/_evidence/` and its record in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01b-gaps-v2/_evidence/record`, and writes its report to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_GAPS_2026-10-31_v2.md`. Version 1's report and evidence stay as they were written. Everything above governs, read with these paths; your hand row is the open row whose Who cell is `MR · work · answers to the register's gaps`. The review of this version is the review instruction's version 2, which section 10 starts as before.

**What this version must do, beyond version 1:**

- **G1 — every register passage that bears on a question, quoted, or the statement that none does.** For each of G-01 to G-13, list the lines of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md` outside its section **Gaps against the brief** that name that gap (the review's `E2_citations.log`, section 3, found them at lines 40, 53, 80, 91, 133, 159, 185, 227, 238, 264, 305 and 319 — establish the set yourself by command, do not copy it). Quote each in the question's section with its line, or say in one line why it does not bear. Where a judgement rests on a register test, quote the test; never restate it (the review names `paper:276`, `:288`, `:298`, `:328` and `:329`).
- **G2 — every position at its strongest, and no cell the paper contradicts elsewhere.** In G-01, Position C is restated in its strongest form: an opaque number from a seeded generator, the same after every reset, as the paper's own G-10 proposes. Then judge it again on all four tests. **Apply the rule to every question**, not to G-01 alone: where any section's cell denies a position a fact the paper grants in another section, correct it, and say in the report how many cells you changed and in which sections.
- **G3 — a setting open to every position is given to every position.** In G-02, the data setting "no two children share all three fields" and the count of what the clerk sees are given to A and B alike, and the two positions are judged on the one thing that divides them: refusing, or showing every learner found. **Apply the rule to every question**: where a setting, a count or a screen any position could take is credited to one alone, give it to all. The review's "found, not fixed" names two further cases, which this version also settles: G-04, the two-lists setting given to A and not to B (item 2), and G-12, A's row (b), which names too few of the must-not requirements — the register's section "What it must not do" holds R-16 to R-21 (item 4).
- **The conflict the review found in G-05** (its "found, not fixed", item 5): G-05 proposes that some of the 8 differ in capitals only, while R-12's test compares family names letter for letter. State the conflict in G-05's section, with both passages quoted, and let the recommendation say how it is resolved, or name it as a question for round 2.

**Further tests of success for this version** (A1 to A9 stand, read with this version's paths):

- **A10** — A command lists, for each of G-01 to G-13, the register lines that name the gap and whether each is quoted in its section or answered by a line saying why it does not bear → `0 unquoted`.
- **A11** — The report gives, for every one of the 13 questions, the settings, counts and screens each position's cells rely on, and states that none is credited to one position while open to another, naming each cell this version changed under G2 and G3, with its line in the new paper.
- **A12** — The verdict of the review of version 1 is answered gap by gap: the report has one row per gap, G1 to G3 and the review's items 2, 4 and 5, each with what changed and the lines of the new paper where it shows.
