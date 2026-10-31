---
kind: report
answers: C-2026-10-31-25
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31.md
written_by: a working session, "MR · work · the goal built", separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt shows only that a scheduled task started it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command after its started entry
window: 2026-10-31 19:28:28 UTC to 2026-10-31 19:42:21 UTC, no pause; closed at the last write of the 94 files the round names as written, REPORT_BUILD_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check. The shell commands run through `run` (node, the clerk's walk) are recorded as commands whose own reads are not traced; the two Python programs of the round (a3_checks.py, a4_plant.py) are traced in full. The files written with Desktop Commander's write_file, and the edits made by short Python one-liners outside `run`, are in the record's list of files changed as "written by no traced run".
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/server.js 3661 bytes sha256 f1e54e4fa0364985170b2f3322787fd36225e4011937911774d86658a2c490b0 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/enrol.js 5324 bytes sha256 378230f1b2f82d68ba94ec85acaa5c55d4981deb88124556ab625f4ede5b8a31 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/screens.js 4703 bytes sha256 446a49e6567b3adc57df514416f2bbf5ad3551cfcd38bbeeccdac82e899dfa0b · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/goal.test.js 18739 bytes sha256 afbf7a8a03f8230fe5e8054d4767f426490caccc6e280b1356d5aca94d67a1e8 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/requirements.test.js 17719 bytes sha256 3a095ee99b35c196712017edcd9f968e8808fedd7bfd96d8e579a07c3825d8a2 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/package.json 286 bytes sha256 61bd479d6b29fb2018cfefc2cac6ab59cf47ac4adf0e91f2458e548b6f8983ca · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/ · this file
ledger: MR C-2026-10-31-25 — the started entry is 20261031T192828Z_MR_started_C-2026-10-31-25.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Build the goal: the enrolment screens, served on this Mac only, with a windowless check for every requirement and every way the goal can go wrong

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md` (C-2026-10-31-25) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`

## 1. The answer first

The goal is built under `src/`: `lib/enrol.js` runs S-1 to S-7 and F-1 to F-7 as ruled (every check of the entry before the search, every fault named, no age check, the search by round 5's `lib/search.js` unchanged, F-4 and F-6 on SC-5), `lib/screens.js` makes the five screens SC-1 to SC-5, each with "Invented data, Progressa is fictional", and `server.js` serves them with Node's own `http` on 127.0.0.1 only, opening no window. `node --test test/` passes 57 of 57: round 5's 29, and 28 new checks, one or more for each of the 13 requirements `count.csv` pairs with the goal and for each of F-1 to F-7 (`0 without a check`). The two planted faults fail by name: the search forgiving spaces fails F-5 (and round 5's search check), R-17's line dropped from SC-3 fails the three R-17 checks. Round 5's files are unchanged but `package.json`, which gains a `start` script; the 15 sources are unchanged. What changes the picture: F-4 cannot be reached from the reset's data or from any clerk's entry, so its handling is seen only on a record the check writes itself (section 3); and the list of windows on the screen was not read (section 4).

## 2. The criteria, one by one

### A1 — Stage 1 before any write: met

Run at 19:31:38 UTC before the record's start (19:31:50), shown in the session, then again through `run` into the log. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A1_stage1.log`:

```text
v20.5.1
# tests 29
# pass 29
# fail 0
EXIT=0
```

`ls -R src` as it stood is in the same log: `README.md data lib package.json reset.js test`, `lib` holding `data_files.js lists.js names.js random.js search.js`, `test` holding `data.test.js reset.test.js search.test.js`.

### A2 — every check passes, round 5's 29 among them: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A2_tests.log`:

```text
# tests 57
# pass 57
# fail 0
EXIT=0
```

57 = round 5's 29 (`data.test.js`, `reset.test.js`, `search.test.js`) + 13 in `goal.test.js` + 15 in `requirements.test.js`.

### A3 — a check for each paired requirement and each of F-1 to F-7: met

The command is `a3_checks.py` over `count.csv` and the A2 log; it prints one line per member, 20 lines for 13 + 7. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A3_checks.log`:

```text
requirements paired with an element of the goal: 13 R-01 R-02 R-03 R-04 R-05 R-06 R-07 R-14 R-15 R-17 R-18 R-20 R-22
ways the goal goes wrong: 7 F-1 to F-7
0 without a check
EXIT=0
```

Each of the 20 identifiers is printed on its own line with the name of its passing check in the same log. R-21 is not paired by `count.csv`; it has a check in each new file, for what Node can see (section 4).

### A4 — the planted faults fail by name: met

The scratch copies are under `_evidence/planted/`, made by `a4_plant.py`; the real `src/` was only copied. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A4_planted.log`:

```text
=== search-forgives-spaces: $ cd planted/search-forgives-spaces/src && node --test test/
EXIT=1
not ok 26 - F-5 — the same child entered with a difference but capitals: not caught, a new learner number, a second record
not ok 53 - search: nothing but capitals forgiven (a space, a dropped name, another form of date)
```

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A4_planted.log`:

```text
=== sc3-without-line: $ cd planted/sc3-without-line/src && node --test test/
EXIT=1
not ok 30 - R-17 — every screen any check of this file reached carries "Invented data, Progressa is fictional"
not ok 41 - R-17 — every screen, shown in turn, says "Invented data, Progressa is fictional"
not ok 45 - R-17 — every screen any check of this file reached carries the line
```

### A5 — round 5's files unchanged, `package.json` alone excepted: met

The start list `src.start.sha256` (19:31:57 UTC) against the end list `src.end.sha256` (19:39:12 UTC). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A5_round5.log`:

```text
changed: ./package.json
18 of 19 round 5 files unchanged, 1 changed
7a8
>     "start": "node server.js",
```

The files under `src/data/` were rewritten by `node reset.js` in Stage 1 and at the end of the clerk's walk, to the same bytes: they are among the 18.

### A6 — nothing connects, nothing opens: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A6_connects.log` prints every match over `src/` (data/ left out). Each, explained:

| Line | What it is |
|---|---|
| `server.js:2` | a comment |
| `server.js:76` `server.listen(…, HOST, …)` | `HOST` is `'127.0.0.1'` (`server.js:18`); no other address is accepted |
| `goal.test.js:10`, `requirements.test.js:9` | comments |
| `goal.test.js:15`, `requirements.test.js:14` `require('node:child_process')` | loaded only to wrap its seven functions and record every program launched; the R-20 and R-21 checks assert none was |
| `goal.test.js:24,26,28`, `requirements.test.js:23,25,27` `net` | the wrapper recording every outbound connection's host (R-18) |
| `goal.test.js:87,94`, `requirements.test.js:86,93` `fetch(app.base + …)` | `app.base` is `'http://127.0.0.1:' + port` |
| `requirements.test.js:362` | an assertion message |

No `http.request`, `https`, `dgram` or `open(` in `src/`. `package.json`: `grep -c dependencies` prints `0`; its keys are `name version private description scripts`. The clerk's walk read the listening socket: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/clerk_walk.log`:

```text
node    32090 arnelaponin   16u  IPv4 0x91cf73a2e9a6202      0t0  TCP 127.0.0.1:8126 (LISTEN)
```

### A7 — the sources unchanged: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A7_sources.log`:

```text
sources: 15 of 15 unchanged
```

The 15: the brief, `REQUIREMENTS.md`, the three groundwork tables, `GROUNDWORK.md`, `GAPS-PAPER.md`, `QUESTIONS-PAPER.md`, `GOAL.md`, `GOAL-QUESTIONS-PAPER.md`, `COUNT.md`, `count.csv`, `_kinds/building.md`, `CONSTANTS.md` and the instruction; their start sha256 equal those the `issued` entry carries.

### A8 — placement and trace checks: met

Run outside `run`, the trace check over this report as written. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A8_checks.log`:

```text
placement check: clean
placement exit 0
  outputs: 8 of 8 named exist
  inputs: 10 of 10 pinned by 20261031T192636Z_MR_issued_C-2026-10-31-25.yaml hash the same now
trace check: clean
trace exit 0
```

### A9 — the record check: in `_evidence/record/check.out`

`round_record.py check` is run after this report's last write, as the round's last act before the `finished` entry; its exit and findings are in `check.out` and in that entry's outcome, not here, since this report is written before it runs.

### A10 — the ledger entries: in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/A10_ledger.log`

The `started` entry stands (`20261031T192828Z_MR_started_C-2026-10-31-25.yaml`); the `finished` entry follows this report and the record's check, and `ledger.py show` is run into that log after it — the one file of the round written after this report.

### The screens, as the server returned them in this round

From `node server.js` (the `start` script) on `src/data`, read with curl on 127.0.0.1; the HTML of each in `_evidence/screens/`, the run in `clerk_walk.log`. SC-3, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/screens/2_new.html`:

```text
<p class="notice"><strong>Invented data, Progressa is fictional</strong></p>
<h1>A new learner number was given</h1>
<p>New learner number: <strong class="learner-number">65</strong></p>
```

SC-2 for the same child in other capitals, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/screens/3_again.html`:

```text
<h1>An existing learner was found</h1>
<p>The registry already holds this learner. Nothing new was entered.</p>
<dt>Learner number</dt><dd>65</dd>
```

SC-4 for a family name of one space, 2019-02-30 and a fourth school, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/screens/4_refused.html`:

```text
<h1>The entry refused</h1>
<li>Family name: not entered</li>
<li>Date of birth: names no day of the calendar</li>
<li>School: not one of the three schools</li>
```

SC-5 with `learners.json` made read-only (F-6), `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/screens/5_cannot.html`:

```text
<h1>The entry cannot be completed</h1>
<p>The entry is refused and cannot be completed. Nothing was saved.</p>
```

`clerk_walk.log` gives `learners 65` after the walk (the read-only attempt saved nothing), `learners after reset 64`, and a count of 1 for the line in each of the six screens read.

## 3. Found, not fixed

- **F-4 is reached only on a record the check writes.** Under the data's settings no two learners share the three fields (`settings.csv:13`), and no clerk's entry can add such a pair, since the search finds the first. The ruling on G-12 asks a check for F-4; the building page (part 1, item 3) refuses a test on a record the prototype cannot produce. The round has both: `F-4 — on the reset's data the search never finds more than one` (each of the 64 learners' fields finds that learner alone), and `F-4 — more than one learner found`, which writes a second learner sharing learner 5's fields into its own temporary folder, named as such in the check's name. For the orchestrator to rule which governs.
- **A school not among the three is lost on the way back.** SC-4 keeps it in the way back, but SC-1 offers the three alone, so it is shown as "(choose a school)" (`screens/6_back_kept.html`). No ruling covers it.
- **A fault the goal does not name** — a data file that cannot be read during an enrolment — is shown on SC-5 with status 500, so that no sixth screen exists (`server.js`). No ruling covers it.
- **The checks' fresh reset is the reset's own `build()`, written to a temporary folder**, not `node reset.js` into `src/data`: `node --test` runs the test files at once, and round 5's checks read `src/data` while they run. R-14 and R-15 therefore reset that temporary folder, not `src/data`.
- **A3's program counted 27 named checks of the new files, not 28**: `F-1, F-2, F-3 at once (Q-9): …` has no " — " in its name; it is in `A2_tests.log` as `ok 23`.
- **Another round wrote under this estate inside this round's window**: "MR · work · the pages against the kind item" (C-2026-10-31-27, started 19:28:35 UTC) wrote `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/00_start.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/A1_gaps.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/A2_page_lines.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/A3_page_state.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/A5_show_before_finished.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/GAPS.planted.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/S7_listing.txt` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/check_lines.sh`, then `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31_v2.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/A4_trace_check.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/A5_show.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/window.cmd.txt` and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item-v2/_evidence/window.out`, besides the files under `_kinds/`, `_prompts/`, `_reports/`, `_reviews/` and `_working/round-kind-item*/` that `RECORD.txt` lists as "written by no traced run"; none is this round's, and none is under `src/`.
- **F-6's check makes `learners.json` read-only**; run as the superuser, the write would succeed and the check would fail.

## 4. What I could not establish

- **R-20 and R-21, the list of windows.** The register's tests read the list of windows on the screen before and after. No command was run for it: on macOS, reading other applications' windows needs the Screen Recording or Accessibility permission, and asking for it opens a system dialog — a window. What Node can see is checked instead: no program launched by any of the 28 new checks (the seven `child_process` functions wrapped before anything loads), no native addon loaded, and the server's modules are `lib/enrol.js`, `lib/screens.js`, `lib/search.js` and `server.js` with the reset's own. That no window opened is shown only as far as that goes.

## 5. Corrections to the instruction

- The checks write into the system's temporary folder (`os.tmpdir()`, a folder per check, removed when the file's checks end), outside the files the `outputs` line names; done so that no check writes `src/data` while round 5's checks read it.
- The instruction names `/usr/bin/python3` for the layer's programs; `a3_checks.py` and `a4_plant.py`, the round's own, ran with it too.

## 6. What this round did not finish

Nothing of the task. Round 7 counts the 8 on what `lib/search.js` and `src/data` hold; round 8 describes the five screens.

## 7. The outputs, by path

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build/_evidence/outputs.log` (19:39:31 UTC) lists each file under `src/` written or changed, with its size and sha256 as the `outputs` line gives them, and `ls -ld` of each place written, each `exit 0`: `src`, `src/lib`, `src/test`, `_working/round-06-build/_evidence`, `_reports`.
