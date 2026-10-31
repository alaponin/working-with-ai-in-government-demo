---
kind: report
answers: C-2026-10-31-25
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_BUILD_2026-10-31_v2.md
written_by: a working session, "MR · work · the goal built", version 2, separate from the session that wrote the instruction and from the session of version 1
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt shows only that a scheduled task started it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command after its started entry
window: 2026-10-31 19:55:53 UTC to 2026-10-31 20:05:13 UTC, no pause; closed at the last write of the 108 files the round names as written, REPORT_BUILD_2026-10-31_v2.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check. The shell scripts run through `run` (node, osascript, shasum, diff) are recorded as commands whose own reads are not traced; the round's Python programs (edit_tests.py, edit_tests_2.py, plant.py, a3_checks.py) are traced in full, and the two test files are recorded as written by runs 4 and 6. The scripts and logs of the evidence folder, written with Desktop Commander's write_file or by a shell redirection, are in the record's list as "written by no traced run".
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/goal.test.js 22891 bytes sha256 1f83c42e8168395f1073957abe15c0dee242a1dabd00cab7accc3ab4244c9273 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/requirements.test.js 22331 bytes sha256 53e5b9e003d083f0eced74373f7a076b55df6a75db29acb65a2827941ff38ec4 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/ · this file
ledger: MR C-2026-10-31-25 — the started entry is 20261031T195553Z_MR_started_C-2026-10-31-25.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Build the goal: the enrolment screens, served on this Mac only, with a windowless check for every requirement and every way the goal can go wrong — version 2

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md` (C-2026-10-31-25, version 2) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`

## 1. The answer first

R-20 and R-21 now do their register's tests: each reads the list of windows on the screen by `CGWindowListCopyWindowInfo` through `osascript -l JavaScript`, before and after (R-20: prototype started, data reset, a child enrolled, prototype stopped), and before, while and after every check of its file (R-21, in both test files), and expects 0 windows added by window number. Before the check was written the command was tried three times: exit 0, 252 windows each time, no error output, about 0.4 s, no window added, none owned by `osascript`, no permission dialog's window, the frontmost application unchanged. `node --test test/` passes 57 of 57, with 252 windows before and 252 after at every reading, 0 added. A planted "after" list with one window more fails R-20 and both R-21 checks by name; the planted faults of A4 fail as in version 1. Only `src/test/goal.test.js` and `src/test/requirements.test.js` changed; every other file under `src/`, and every source, is unchanged. The review's two "found, not fixed" items on Q-4 and on Q-6 with Q-8 are named as questions for the owner (section 3).

## 2. The criteria, one by one

### A1 — Stage 1 before any write: met

Run at the record's start, before `edit_tests.py`, the first write under `src/` (19:59:53 UTC by `RECORD.txt`, run 4). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A1_stage1.log`:

```text
v20.5.1
# tests 57
# pass 57
# fail 0
EXIT=0
```

57, not the 29 the task's section 3 names: `src/` now holds version 1's build, its 28 checks with round 5's 29 (section 5). `ls -R src` as it stood is in the same log.

### A2 — every check passes: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A2_tests.log`:

```text
# tests 57
# pass 57
# fail 0
EXIT=0
```

The first run after the change (`A2_tests_first.log`, 20:00:09 UTC) failed `R-21` of `goal.test.js` on `readings while they ran: 0`: that file's checks end within about a second, before the first half-second interval read anything. `edit_tests_2.py` made the readings follow one another from the first list on; the run above followed it.

### A3 — a check for each paired requirement and for F-1 to F-7: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A3_A5_A6_A7_A13.log`:

```text
requirements paired with an element of the goal: 13 R-01 R-02 R-03 R-04 R-05 R-06 R-07 R-14 R-15 R-17 R-18 R-20 R-22
ways the goal goes wrong: 7 F-1 to F-7
0 without a check
EXIT=0
```

Version 1's program, unchanged, over this round's TAP; each of the 20 is on its own line in the log with its check's name.

### A4 — the planted faults fail by name: met

Scratch copies under `_evidence/planted/`, made by `plant.py` without keeping file times. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A4_A12_planted.log`:

```text
not ok 26 - F-5 — the same child entered with a difference but capitals: not caught, a new learner number, a second record
not ok 53 - search: nothing but capitals forgiven (a space, a dropped name, another form of date)
```

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A4_A12_planted.log`:

```text
not ok 30 - R-17 — every screen any check of this file reached carries "Invented data, Progressa is fictional"
not ok 41 - R-17 — every screen, shown in turn, says "Invented data, Progressa is fictional"
not ok 45 - R-17 — every screen any check of this file reached carries the line
```

### A5 — round 5's files unchanged, the test files alone excepted: met

`src.start.sha256` (19:58:18 UTC) against `src.end.sha256` (20:02:40 UTC). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A3_A5_A6_A7_A13.log`:

```text
files under src/ (data/ apart): 16; changed in this round: 2
data/: 8 files, unchanged
```

The two are `test/goal.test.js` and `test/requirements.test.js` (A13). `package.json` is as version 1 left it.

### A6 — nothing connects and nothing opens: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A3_A5_A6_A7_A13.log` prints every match over `src/` (data/ left out), `execFile` and `osascript` added to the pattern. Each, explained:

| Lines | What it is |
|---|---|
| `server.js:2`, `goal.test.js:11`, `requirements.test.js:9`, `:415` | comments, an assertion message |
| `server.js:76` `server.listen(…, HOST, …)` | `HOST` is `'127.0.0.1'`, as in version 1 |
| `goal.test.js:16,21`, `requirements.test.js:14,19` | `child_process` loaded to wrap its seven functions and record every program launched, as in version 1 |
| `goal.test.js:19`, `requirements.test.js:17` `const execFileUnwrapped = childProcess.execFile` | the one function kept before the wrapping, for the checks' own window reads, so that `launches` records only what the prototype might start |
| `goal.test.js:53,65,67`, `requirements.test.js:51,63,65` `osascript` | **`/usr/bin/osascript -l JavaScript`, started by the test only**, to read the list of windows by `CGWindowListCopyWindowInfo` for R-20 and R-21: it brings nothing forward, asks no permission and opens no window (`W0_probe.log`); nothing under `src/` but the two test files names it |
| `goal.test.js:28,30,32`, `requirements.test.js:26,28,30` `net` | the wrapper recording every outbound connection's host (R-18) |
| `goal.test.js:141,148`, `requirements.test.js:139,146` `fetch(app.base + …)` | `app.base` is `'http://127.0.0.1:' + port` |

No `http.request`, `https`, `dgram` or `open(`. `grep -c dependencies package.json` prints `0`.

### A7 — the sources unchanged: met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A3_A5_A6_A7_A13.log`:

```text
sources: 15 of 15 unchanged
```

The 15: the brief, `REQUIREMENTS.md`, the three tables of `docs/groundwork/`, `GAPS-PAPER.md`, `QUESTIONS-PAPER.md`, `GOAL.md`, `GOAL-QUESTIONS-PAPER.md`, `COUNT.md`, `count.csv`, `_kinds/building.md`, `CONSTANTS.md`, the instruction and the review of version 1. `docs/GROUNDWORK.md` is not among them; the record's start and end lists carry it, and `RECORD.txt` names no change to it.

### A8 — placement and trace checks: in `A8_checks.log`

Run outside `run` after this report is written, the trace check over this report: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A8_checks.log`. Their exits are in that log and in the `finished` entry's outcome.

### A9 — the record check: in `record/check.out`

`round_record.py check` runs after this report's last write, as the round's last act before the `finished` entry. **Not met as written:** `end`, and the check run once before this sentence was written, name 3 findings, `/data`, `/lib` and `/test` "read, not on the start list". `record/opened.jsonl` gives each as an `open` by run 10, `plant.py`, at 20:01:50 UTC, while `shutil.copytree` copied `src/data`, `src/lib` and `src/test` into the planted copies; `ls -d /data /lib /test` prints "No such file or directory" for each. The check therefore exits 1 on those 3, which nothing but the tracer's reading of `copytree`'s directory walk produced.

### A10 — the ledger entries: in `A10_ledger.log`

The `started` entry stands (`20261031T195553Z_MR_started_C-2026-10-31-25.yaml`); `ledger.py show` is run into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A10_ledger.log` after the `finished` entry.

### A11 — R-20 and R-21 read the list of windows before and after: met

Before the check was written, the command was tried. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/W0_probe.log`:

```text
frontmost application before: Claude
reading 1: exit 0, 252 windows listed, 408 ms, error stream: 0 bytes
reading 2: exit 0, 252 windows listed, 416 ms, error stream: 0 bytes
reading 3: exit 0, 252 windows listed, 416 ms, error stream: 0 bytes
frontmost application after: Claude
windows in reading 3 not in reading 1: 0
windows owned by osascript in any reading: 0
```

No command was refused. The run of `node --test` (A2). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A2_tests.log`:

```text
ok 31 - R-21 — every check of this file ran to its end; the list of windows read before, while they ran and when they ended: 0 windows added at each reading
ok 43 - R-20 — the list of windows read before and after: the prototype started, the data reset, a child enrolled through a windowless check, the prototype stopped; 0 windows added
ok 46 - R-21 — every check of this file ran to its end; the list of windows read before, while they ran and when they ended: 0 windows added at each reading
# R-21: windows listed before the checks: 252; readings while they ran: 2; windows listed when they ended: 252; windows added at any reading: 0
# R-20: windows listed before: 252; windows listed after: 252; windows added: 0
# R-21: windows listed before the checks: 252; readings while they ran: 3; windows listed when they ended: 252; windows added at any reading: 0
```

Check 31 is `goal.test.js`'s, 46 `requirements.test.js`'s. R-20 also keeps version 1's assertions: no program launched, no native addon, the modules loaded.

### A12 — the planted case fails by name: met

No window can be added without opening one, which the constants and the building page (part 1, item 6) forbid; so the plant gives every reading after the first one window more (number 999999, owner "planted window") in both files, and R-20's "after" list one more again (999998), since R-20's "before" is itself a later reading. `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A4_A12_planted.log`:

```text
not ok 31 - R-21 — every check of this file ran to its end; the list of windows read before, while they ran and when they ended: 0 windows added at each reading
not ok 43 - R-20 — the list of windows read before and after: the prototype started, the data reset, a child enrolled through a windowless check, the prototype stopped; 0 windows added
not ok 46 - R-21 — every check of this file ran to its end; the list of windows read before, while they ran and when they ended: 0 windows added at each reading
# R-20: windows listed before: 253; windows listed after: 254; windows added: 1
# pass 54
# fail 3
```

The diff of the plant against `src/` is at the head of the same block of the log. A first planting (`A4_A12_planted_first.log`) put the window in every later reading only, and R-20 passed, its two lists both holding it; hence the second line of the plant.

### A13 — `src/` against version 1's checksums: met

Version 1's checksums: its `src.end.sha256` for round 5's files and its report's `outputs` line for the six it wrote, 16 files (`src.v1.sha256`). `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/A3_A5_A6_A7_A13.log`:

```text
version 1 files listed: 16
13,14c13,14
< afbf7a8a03f8…  ./test/goal.test.js
< 3a095ee99b35…  ./test/requirements.test.js
---
> 1f83c42e8168…  ./test/goal.test.js
> 53e5b9e003d0…  ./test/requirements.test.js
changed against version 1: ./test/goal.test.js ./test/requirements.test.js 
```

## 3. Found, not fixed

**Two questions for the owner**, from the review of version 1, named and not fixed:

- **Q-4 — is "spaces only" any whitespace?** `lib/enrol.js` reads an entry as missing when `trim()` leaves nothing, so an entry of tabs or no-break spaces is refused as missing (F-1); the ruling on Q-4 says «spaces». Either the ruling is read as any whitespace, or the check is narrowed to the space character.
- **Q-6 with Q-8 — what does SC-1 show for a fourth school on the way back?** SC-4 keeps the four entries in its way back, but SC-1 offers only the three schools (Q-6), so a school not among them comes back as "(choose a school)"; Q-8's «entries kept» does not say whether it must be shown.

Further:

- **The window checks count every window on the screen**, as the register's tests say, not only the prototype's. A window opened by another program during a run (a notification, another app) would fail R-20 or R-21 though the prototype opened nothing; each failure names the window's owner and process.
- **`windowReads`** in both test files lists every window read the checks made, and no check asserts on it.

## 4. What I could not establish

- Whether a window opened by the prototype in another login session, or on a display this session's user does not own, would be listed: `CGWindowListCopyWindowInfo` lists the windows of the session it runs in.

## 5. Corrections to the instruction

- Stage 1's "passing 29 of 29 as accepted" now reads 57 of 57: version 1's 28 checks stand under `src/`.
- A8 names `REPORT_BUILD_2026-10-31.md` and A9 the record of `round-06-build`; read with this version's paths, the trace and record checks run over this report and `round-06-build-v2/_evidence/record`.
- `CONSTANTS.md` of the coordination and the brief, read here, lie outside `--root`; they were named with `--read` at the record's start.

## 6. What this round did not finish

Nothing of version 2. Round 7 counts the 8 on what `lib/search.js` and `src/data` hold; round 8 describes the five screens and can now describe R-20 and R-21 as checked by the list of windows.

## 7. The outputs, by path

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2/_evidence/outputs.log` (20:02:48 UTC) lists the two files changed under `src/` with size and sha256, as the `outputs` line gives them, and `ls -ld` of each place written, each `exit 0`: `src/test`, `_working/round-06-build-v2/_evidence`, `_reports`.
