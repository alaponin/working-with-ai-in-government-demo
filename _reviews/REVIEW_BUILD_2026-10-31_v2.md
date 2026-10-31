---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31_v2.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md (C-2026-10-31-25, version 2)
written_by: a session that neither wrote nor carried out the instruction — "MR · review · the goal built", started as a sub-agent from the start message of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_BUILD_2026-10-31.md (C-2026-10-31-26, version 2), with an empty memory, separate from the sessions of both versions and from the first edition's reviewer
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` on the computer the session runs on, the session's first command
window: 2026-10-31 20:05:54 UTC to 2026-10-31 20:12 UTC, no pause — opened at this task's started entry 20261031T200554Z_MR_started_C-2026-10-31-26.yaml; closed at the moment of writing
verdict: accepted
downstream_artefact: the orchestrator's closed entry for C-2026-10-31-26, which closes C-2026-10-31-25 with it
---

# REVIEW — Round 6, the goal built — edition 2

**This review ran the project's checks with the list of windows read by its own command before and after, a way the goal goes wrong, four planted faults and the four mechanical checks. G1 of the first edition is closed: R-20 and R-21 now read the list of windows and fail by name on a planted window; only the two test files changed. Accepted, with no gap; the record check's exit 1 is the kit's tracer, not the round (section 1, A9; section 8).**

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence/` (cited as `<E>/`). The real `src/` was not changed by this review: sha256 at the start equals that at the end, `src/` and `data/` both `diff exit 0` (`<E>/R6_end.log`).

## 1. The tests of success, one by one

| Test | Verdict | Evidence read or produced here |
|---|---|---|
| A1 — Stage 1 before any write | met | `A1_stage1.log` stamped `19:58:18Z`…`19:58:20Z`, `# pass 57`; the first write under `src/` is run 4 at `19:59:53` (`RECORD.txt:147-148`, `<E>/R5_figures.log`). 57, not 29: version 1's 28 checks stand; the report names the correction (its section 5). |
| A2 — every check passes | met | Own run, `<E>/R1_checks.log`: `v20.5.1`, `# tests 57`, `# pass 57`, `# fail 0`, `EXIT=0`, 57 lines `^ok`. |
| A3 — a check for each paired requirement and F-1 to F-7 | met | Own route over own TAP (`<E>/R5_figures.log`): the 13 requirements `count.csv` pairs with a goal element (`R-01 … R-07 R-14 R-15 R-17 R-18 R-20 R-22`, read from `count.csv` by `awk`) and F-1 to F-7 each name ≥1 `ok` line; `without a check: 0`. R-20's check now does R-20's test (A11). |
| A4 — planted faults fail by name | met | The round's `A4_A12_planted.log` (F-5, search, R-17 ×3). The reviewer's own F-4 plant fails `not ok 25 - F-4 …`, `expected: 'SC-5'`, `actual: 'SC-3'`, `# fail 1` (`<E>/R3_planted.log`). |
| A5 — round 5's files unchanged, the test files excepted | met | Round 5's files and `package.json` against the first review's `src.start.sha256`: `diff exit 0` (`<E>/R5_figures.log`); `data/` against the round's `data.end.sha256`: `diff exit 0`. |
| A6 — nothing connects, nothing opens | met | Own grep over `src/*.js` (`<E>/R5_figures.log`): `server.js:76` listens on `HOST` = `'127.0.0.1'`; every `fetch` is `app.base + …`; `child_process` and `net` only wrapped to record; `osascript` only at `goal.test.js:65,67` and `requirements.test.js:63,65`, through `execFileUnwrapped`, started by the checks; `dependencies in package.json: 0`. As the report's table says. |
| A7 — sources unchanged | met | The trace check, run here: `inputs: 10 of 10 pinned by 20261031T195352Z_MR_issued_C-2026-10-31-25.yaml hash the same now` (`<E>/R4_mechanical.log`). |
| A8 — placement and trace checks exit 0 | met | Run here: `placement check: clean`, `placement exit 0`; `trace check: clean`, `trace exit 0` (`<E>/R4_mechanical.log`). |
| A9 — the record check exits 0 | **not met as written; not counted as a gap** | Run here with the round's options: `record check exit 1`, `## Findings — 3`: `/data`, `/lib`, `/test` "read, not on the start list" (`<E>/record_check.out`). None exists (`ls`: "No such file or directory"). They are run 10's (`plant.py`, `cwd: "/"`) — `shutil.rmtree` of run 8's copies (`plant.py:37-38`), whose names are relative to a directory descriptor; the tracer resolves every path by `os.path.realpath(os.path.abspath(path))` (`record/_hook/sitecustomize.py:39`), so against `/`. The same run records 72 `remove` events on one-segment paths under `/` (`<E>/R6_end.log`). The fault is `round_record.py`'s, not the round's; no file is unaccounted for. The report declared it (its A9). See section 8. |
| A10 — started and finished beside issued | met | `ledger.py show` (`<E>/ledger_show.out`): for version 2, `issued` 20261031T195352Z, `started` 20261031T195553Z, `finished` 20261031T200525Z. |
| A11 — R-20 and R-21 read the list before and after | met | Read in the code (`requirements.test.js:56-82, 420-433, 462-476`; the same in `goal.test.js`): `CGWindowListCopyWindowInfo` by `/usr/bin/osascript -l JavaScript`, compared by window number. Own run (`<E>/R1_checks.log`): `ok 43 - R-20 …`, `# R-20: windows listed before: 252; windows listed after: 252; windows added: 0`; `ok 31` and `ok 46 - R-21 …`, `readings while they ran: 2` and `3`, `252`, `added at any reading: 0`. |
| A12 — the planted case fails by name | met | The round's plant (`A4_A12_planted.log`: `not ok 31`, `43`, `46`). The reviewer's own three window plants, section 5. |
| A13 — `src/` against version 1 shows only the test files | met | Own sha256 of `src/` against the round's `src.v1.sha256` (`<E>/R5_figures.log`): `13,14c13,14`, only `./test/goal.test.js` and `./test/requirements.test.js`; `src.v1.sha256`'s six lines of version 1's files equal the first review's `R7_outputs.log`, so the baseline is version 1's, read by another hand. |

The report names the first edition's two "found, not fixed" items (Q-4, any whitespace as "spaces"; Q-6 with Q-8, a fourth school lost on the way back) as questions for the owner (its section 3), as version 2 asks.

## 2. One figure re-established

- **"252 windows before and 252 after, 0 added."** The report read the counts from its tests' diagnostics. Here, by the reviewer's own program (`<E>/windows.js`, `CGWindowListCopyWindowInfo` with `kCGNullWindowID`, five fields per window) around the whole `node reset.js && node --test test/`: `reading win.before.tsv: exit 0, 252 windows listed, 0 bytes on the error stream, 397 ms`; `win.after.tsv: exit 0, 252 …, 383 ms`; added by number `0`, gone `0`, owned by `osascript` or `node` `0`; the frontmost application `Claude` before and after (`<E>/R1_checks.log`). **Agrees.**
- **"57 of 57."** `grep -cE '^test\('` per file: `data 18`, `goal 13`, `requirements 15`, `reset 3`, `search 8`, `total 57` (`<E>/R5_figures.log`). **Agrees.**
- **Times given in words.** The window's close, 20:05:13 UTC, is the report's mtime by `stat` (`2026-10-31T20:05:13Z`) and `window.out` line 7 (`last written 2026-10-31T20:05:13.634Z`, 108 files). The two test files last written 20:00:49 (`stat`; `RECORD.txt:112-113`, "written by run 4, 6"). A2's first failed run then the passing one, 20:00:52. **Agree.**

## 3. The outputs exist

`<E>/R5_figures.log` (20:09:59 UTC): `22891 1f83c42e…9273 goal.test.js`, `22331 53e5b9e0…8ec4 requirements.test.js`, as the report's `outputs` line gives them. The evidence folder exists; each of the 17 files the report cites was found at its path (`found …`, same log). The report is at its path, 16856 bytes.

## 4. The running application

Not applicable: no application model on a test server; the prototype's own use of the screens is part 5.

## 5. What a review of building runs (the building page, part 2)

**The project's checks again**, in this review's own run, with the window list read by its own command around it: `<E>/R1_checks.log`, section 2 above. `EXIT=0`, 57 of 57.

**One use of the screens as a school clerk.** Not repeated, as the review instruction's version 2 allows: no screen-making file changed — `server.js f1e54e4f…`, `lib/enrol.js 378230f1…`, `lib/screens.js 446a49e6…` are version 1's (`<E>/src.start.sha256` against `src.v1.sha256`). The first edition's walk stands (`_working/round-06-build-review/_evidence/R2_walk.log`).

**One way the goal goes wrong**, repeated here because it is cheap, by curl on 127.0.0.1:8141 from a fresh reset (`<E>/r2_wrong.sh`, `<E>/R2_wrong.log`, screens `<E>/screens/`): Ostervald / Mira Tamsin / `2019-02-30`, the school left out, and again with `school=` sent empty. Returned (`X1_refused.html`; `X2` identical):

```text
<h1>The entry refused</h1>
<li>Date of birth: names no day of the calendar</li>
<li>School: not entered</li>
<input type="hidden" name="family_name" value="Ostervald">
<input type="hidden" name="date_of_birth" value="2019-02-30">
```

Both faults named (Q-8, Q-9); the date as no day (Q-1, G-07), the school as missing (Q-6, Q-5); the four entries kept in the way back (Q-8); R-17's line on the screen; `learners.json` `32e01ac3…` and 64 learners before and after — nothing saved (Q-7). Windows 252 before, 252 after, 0 added; the server stopped (`listening on 8141 now: 0`). **As ruled.**

**The window list, read by the reviewer's own command before and after a run**: section 2, first figure.

**The planted faults**, each in a scratch copy under `<E>/planted/`, made by `cp -R` without kept times (`src/server.js mtime 2026-10-31T22:07:38` local, the real one `21:33:29`), `<E>/r3_planted.sh`, `<E>/R3_planted.log`:

- *A window added to R-20's "after" list* (`after.set("999999", …)`): `EXIT=1`, `not ok 43 - R-20 …`, `# R-20: windows listed before: 252; windows listed after: 253; windows added: 1`, `# fail 1`.
- *A window added to R-21's "when they ended" list in `goal.test.js`*: `not ok 31 - R-21 …`, `windows listed when they ended: 253; windows added at any reading: 1`, `# fail 1`.
- *The list cannot be read* (`/usr/bin/osascript-absent`): `EXIT=1`, R-20 and R-21 `not ok` with every other check of that file (the `before` hook fails), `# fail 15` — the check fails, it does not pass silently.
- *F-4 saves a record* (`lib/enrol.js:103`): `not ok 25 - F-4 …`, `# fail 1` (`<E>/r3b_planted_f4.sh`).

Each fails by name; the real `src/` untouched.

**The faults of the page, part 1, read against the report.** Item 1: the counts quoted are from the test runs' output. Item 2: checks run with results. Item 3: unchanged since edition 1 (F-4's check writes its own record; for the orchestrator). Item 4: nothing added beyond the task. Item 5: round 5's files untouched. Item 6: no window opened, by the round's checks or this review (0 added at every reading). Item 7, added from G1: the command was tried before the check was written (`W0_probe.log`, three readings, `exit 0`, `0 bytes` on the error stream) — kept.

## 6. The four mechanical checks, run by the reviewer

All in `<E>/R4_mechanical.log` (20:08:59–20:09:01 UTC), run directly by `<E>/r4_mech.sh`, not through `round_record.py run`:

- **Trace** over the report: `trace check: clean`, `trace exit 0`.
- **Placement** over the instruction: `placement check: clean`, `placement exit 0`.
- **Record check**, `--record …/round-06-build-v2/_evidence/record --report …_v2.md --tolerance 2` (as `check.out` prints on `# run with:`), `--out <E>/record_check.out`: `record check exit 1`, `## Findings — 3` — the three of A9, nothing else. This review's own files appear only as "added after the window closed, by another hand or later", not as findings.
- **Ledger `show`** for C-2026-10-31-25 (`<E>/ledger_show.out`): version 1's three `issued`, `started`, `finished`; version 2's `issued` 195352Z (`subject: "MR C-2026-10-31-26"`), `started` 195553Z, `finished` 200525Z. **Account:** `arne.laponin@gmail.com` on each; the report's declaration names the same. `started_by: unknown`, as declared.
- **Ledger `check`** (`<E>/ledger_check.out`): `check exit 0`, `check: clean`. No line names MR.

## 7. The verdict

**Accepted — no gap.** G1 of the first edition is closed: R-20's and R-21's checks read the list of windows before, while and after, as `docs/REQUIREMENTS.md:268-292` says; they pass on the real `src/` with 252 windows and 0 added, which the reviewer's own reading agrees with, and fail by name when a window is planted in either list or when the list cannot be read. Only the two test files changed against version 1. Every other test stands in this review's own run. A9's literal exit 1 is a fault of the kit's tracer, which neither the prototype as delivered nor round 7's count would carry; it is named in section 8 for the orchestrator.

## 8. Found, not fixed

- **`round_record.py`'s tracer resolves names given relative to a directory descriptor against the working directory** (`record/_hook/sitecustomize.py:39`, `os.path.realpath(os.path.abspath(path))`, no `dir_fd`). Any `shutil.rmtree` under `run` records each name as `/<name>`: here 72 `remove` events and the 3 `open`s that make `check` exit 1. For the kit; until fixed, a round that removes a tree under `run` cannot get the record check to exit 0.
- **The report names the wrong call** for those three: «while `shutil.copytree` copied …» (report, A9); the opens come from `shutil.rmtree(dest)` (`plant.py:37-38`), run 10 removing run 8's copies — hence only run 10. Minor; the conclusion holds.
- **The round's `A8_checks.log` was written at 20:04:28 UTC**, before the report's last write (20:05:13): the round's trace check read an earlier state of the report. This review's trace check over the final report is clean.
- **The window checks compare window numbers only and count every window of the login session**, as the register's test reads; a window another program opens during a run would fail R-20 or R-21 (named by the report), and a window opened and closed between two readings is not seen (inherent in reading at intervals).
- **Still for the owner or the orchestrator, from edition 1**: Q-4 (any whitespace read as "spaces"), Q-6 with Q-8 (a fourth school lost on the way back), and F-4 against the building page's item 3 — named again by the report, ruled by no one yet.
- **Model**: claude-opus-5-5, the band named. Effort `unknown`, as the started entry records.
