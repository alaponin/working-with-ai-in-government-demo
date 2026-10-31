---
kind: instruction
commission_id: C-2026-10-31-01
version: 1
session_name: MR · work · register of requirements
kind_of_work: drafting
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md (sha256 ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64, read 2026-10-31 12:57:59 UTC)
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants (owed when round 8 of the brief is accepted) — round 1 of the brief, the register of requirements, which rounds 3, 4 and 7 count against
model: Opus — the content is settled by the brief, the governing document in force; what remains is writing every requirement out exactly, and the risk is inexactness (a sentence of the brief missed, a requirement added) rather than misjudgement
effort: high — the surface is the whole brief, sentence by sentence, and a missed or invented requirement is the failure that every later round inherits
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Opus, effort high — the review lists the set again from the brief by its own route and compares it row by row
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_REQUIREMENTS_2026-10-31.md
waits_for: none
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md
running_record: MR — the estate's record is not yet cut over to the ledger; the row was added by hand to /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md at 2026-10-31 13:00 UTC, before this instruction was issued, and no issued entry is written
---

## The start message

```text
MR · work · register of requirements
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md
```

---

# INSTRUCTION — Write the register of requirements of the mini registry: every sentence of the brief that says what the registry must do, numbered, each with a test

**Suggested model: Opus, effort high.** The brief settles the content; the risk is a sentence missed or a requirement added over the whole of it (section 7 of the procedure, the second question).


## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · register of requirements`. You run on the owner's Mac, `MacBookPro`, through Desktop Commander's `start_process` (zsh) and its file tools. Those tools are deferred: before any command on the Mac, load them with ToolSearch by their full names — `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`. Bridged tool names carry a prefix that can vary by session: where that exact name is absent, search by function (`start_process`, `desktop-commander`, `+remote-devices process`) and load what comes back by its exact full name. Prove the shell with `date -u; hostname` and record the tool name and the output. Only after that may you say the shell is unavailable, stating what you searched, what came back and the exact error. You do exactly the task in section 3 and nothing else.

**The estate's record of what is running has not been cut over to the ledger** — the declaration's `running_record` line names a row added by hand. So **you write no ledger entry.** Your first act, once you have read this declaration, is to take up your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md`: in the Open table, in the row whose Who cell is `MR · work · register of requirements`, replace the Started cell with the time `date -u` prints, as `31 Oct 2026, HH:MM UTC`. Your last act before starting the review (section 10) is to close it: move that row into the Closed table, with the time it closed and one line saying what came of the round and what moved. The orchestrator enters this task in the ledger when it cuts the record over, and appends to this file a dated paragraph with any entry you then still owe; that paragraph governs from the moment it stands.

**Your account**, for your report's declaration, is the address the line of your own context names as the user's address ("The user's email address is …"), in lower case, or `unknown` where it names none; never from a file on the machine. **Your computer** is what `hostname` prints. **Who started you** is read from your own prompt: `owner` where the owner typed or pasted it, otherwise `unknown` — a session started by the orchestrator's scheduled task cannot tell, and does not guess.

Where the Mac cannot be reached at all, write nothing anywhere, and end with one line saying so and with the exact error.

## 2. Read first, in this order

1. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` — the procedure.
2. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md` — the page of the kind of work: the faults a drafting session refuses (part 1), what its review runs (part 2) and what was checked before this instruction was issued (part 3).
3. The kind has no skill of its own; this line says so.
4. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md` — the standing constraints (section 5) and the map of places (section 6). The project has no `CLAUDE.md`.
5. `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md` — the brief, the document this task consumes. Check its sha256 against the declaration first; where it differs, stop and say so in the report.
6. `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md` — the report form.

## 3. The task

Write `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/REQUIREMENTS.md`, the register of requirements of the mini registry. It holds every requirement the brief states, numbered `R-01` onwards, and each requirement carries a test.

Do it in two steps, in this order, because the drafting page asks for the set to be listed and counted before the draft:

**Step 1 — the inventory.** List every sentence of the brief in its five sections that bear on the prototype — "What it is for", "What it must do", "The made-up data, in known numbers", "What it must not do", "What it delivers" — into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/SENTENCES.md`. A unit is a sentence, a list item or a table row; split the brief into units by a small program saved beside the inventory, so that the count is established by a command and not by eye. For each unit give its line number in the brief, the unit quoted word for word, and one disposition: **requirement** — it says what the prototype must do, must be, must hold, must deliver or must not do — or **not a requirement**, with the reason in a few words (context, purpose, a heading). The set of units the brief's "The rounds, in order" section and its italic opening carry is out of the inventory: they describe the work, not the registry. State the number of units and the number marked requirement, each with the command that counted it.

**Step 2 — the register.** For every unit marked requirement, at least one numbered requirement in the register, and no requirement without such a unit. Each requirement has:
- its number, `R-01` onwards;
- the brief's line number and the unit quoted word for word;
- the requirement in one plain sentence, saying no more than the unit says;
- a **test**: what is set up, what is done, and what is seen, so that a person or a program could run it on the prototype once it is built, and say pass or fail, without opening a window where the brief forbids one. A known number in the brief is a known answer in the test.

Close the register with a section **Gaps against the brief**: each place where a test needs a fact the brief does not give (for example, what a learner number looks like), stated as a question against the brief and left open — never answered in the register.

## 4. Constraints and standing rules

- No figure from memory: every count is established by a command, with the command and its time, and claims no wider than the command.
- Supply no fact, rule or requirement the brief does not carry (the drafting page, part 1, item 1); a missing one is a gap, raised in the closing section.
- The brief is read and never changed; it sits outside this repository.
- No operation that writes to version control. Reading state (`git status`, `git log`) is permitted and reported.
- Nothing opens a window on the owner's screen: no `open`, no Finder, no application brought forward.
- Keep the round's record with `round_record.py`, as the report form's `record` line requires: `start` before your first write into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`, with `--record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record --root /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry --read /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`, run the inventory program through `run`, `end` after your last write but the report, and `check` as your last act before closing your row.

## 5. Acceptance criteria

- **A1** — The inventory exists, made by a program saved in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/`, and its output prints the count of units and the count marked requirement → both numbers stated in the report with the command and its output.
- **A2** — Both ways: every unit marked requirement in the inventory is cited by at least one `R-` number in the register, and every `R-` number cites a unit marked requirement → one command (saved in the evidence folder) that compares the two lists and prints `0 uncited, 0 unsupported`.
- **A3** — Every requirement quotes its unit word for word: a command that checks each quoted unit is a substring of the brief prints `0 not found`.
- **A4** — Every requirement has a test in the three parts of section 3, and every test that rests on a known number of the brief (60 children, 3 schools, 8 on more than one list, 4 of those spelt differently, ages 6 to 12) states that number as its expected result → the report lists each such requirement with the number its test expects.
- **A5** — The closing section **Gaps against the brief** exists; each gap is a question, and no answer to it appears elsewhere in the register.
- **A6** — The brief is unchanged at the end: `shasum -a 256` of it prints `ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64`.
- **A7** — The placement check passes over this instruction: `python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/placement_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REQUIREMENTS_2026-10-31.md` exits 0; and the trace check passes over the report: `python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md` exits 0.
- **A8** — The round's record check passes: `python3 -B "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/round_record.py" check --record /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_REQUIREMENTS_2026-10-31.md --out /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/record/check.out` exits 0, its `check.out` cited by path.
- **A9** — The record is not cut over, so in place of ledger entries: the row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` taken up with its start time and, at the end, closed into the Closed table.

## 6. Evidence required

For every criterion: the command as run, its output trimmed but not edited, and the time, kept in files under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-01-requirements/_evidence/` and cited by path. A criterion without evidence is not met. The measurement window closes at the moment of writing.

## 7. How this round can fail

**The faults of the kind, by reference:** part 1 of `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/drafting.md`, which this round refuses in itself and which this section does not retype.

The ways this round goes wrong while appearing to succeed:

- **The search rule widened.** The brief's rule matches exactly one learner on family name, given names and date of birth, *capitals ignored*. Nothing else is ignored. A requirement or test that also forgives accents, spaces or spelling has added to the brief; and the four children whose family name is spelt differently on one list are expected *not* to be caught by that rule — how many it catches is round 7's count, not a requirement here. Write the rule as the brief writes it.
- **The data and the prohibitions dropped as context.** The rows of the table of known numbers, the sentence that the data is made the same way every time it is reset, and every "must not" sentence are requirements on the prototype, and each needs a test as much as the enrolment goal does.
- **A test that restates its requirement.** "The registry does not register the same child twice" is not a test. A test names what is entered, in what state the data stands, and what the clerk or a program sees.

## 8. Out of scope — do not touch

- `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/`, every other file in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/`, and the brief.
- The groundwork (round 2) and the goal written in full (round 3): this round names requirements and tests, not tables, screens or steps.
- Any commit: the owner's.
- Anything discovered but not asked for goes to the report under "found, not fixed", not into the work.

## 9. The report

Write the report named in `downstream_artefact`, from `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`, in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/`. Set its `upstream_artefact` to this file's path, so that the trace check finds the two declarations agreeing; set its `answers` to `C-2026-10-31-01`; and its `ledger` line says that the record is not cut over and the row was kept by hand. Say which kind of session wrote it. Do not commit or push; do not send anything to anybody; do not write the verdict — the verdict is the review's.

If a file this instruction names does not exist, stop and say so in the report. Do not reconstruct it from memory or from inference.

After everything else is written, the report records, for each place the round wrote in, `ls -ld "<path>"` and its exit code. Open nothing on the owner's screen.

Then close your row in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` by hand, as section 1 says. **Write no `finished` entry**: the record is not cut over.

## 10. The review

The orchestrator wrote and issued the review of this task together with this instruction: the declaration's `review_instruction` line names it. Once your row is closed, your one act is to start that review yourself, automatically, as a sub-agent with your Agent tool:

- `subagent_type`: `general-purpose` — never a fork; the review has a fresh context;
- in the foreground, because your next act depends on it;
- `prompt`: these three lines, word for word:

```text
MR · review · register of requirements
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_REQUIREMENTS_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

- where the Agent tool takes a model and an effort, as its own description says at the moment of use, Opus and effort high, and never lower.

Never create a scheduled task to start it. Wait for the sub-agent, add nothing to it, and end with one line: the review's verdict line as it returned it, and the review's path. Where the sub-agent could not reach the Mac, or the Agent tool cannot give the model named, say so in that one line instead; the orchestrator starts the review at its next "check". Do not judge the review, do not act on its verdict, and route nothing.
