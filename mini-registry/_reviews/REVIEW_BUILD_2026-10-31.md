---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_BUILD_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md (C-2026-10-31-25)
written_by: a session that neither wrote nor carried out the instruction — "MR · review · the goal built", started as a sub-agent from the start message of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_BUILD_2026-10-31.md (C-2026-10-31-26)
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` on the computer the session runs on, the first command of the session
window: 2026-10-31 19:42:54 UTC to 2026-10-31 19:50 UTC, no pause — opened at this task's started entry 20261031T194254Z_MR_started_C-2026-10-31-26.yaml; closed at the moment of writing
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md, its gap appended by the orchestrator
---

# REVIEW — Round 6, the goal built

**This review ran the project's checks, the screens as a clerk, a way the goal goes wrong, a planted fault and the four mechanical checks; the prototype does what the goal as ruled says on every screen and failure tried, but one requirement's check (R-20) is not the register's test and the report's reason for setting that test aside does not hold.**

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-review/_evidence/` (cited below as `<E>/`). The real `src/` was not changed: its sha256 at the start of this review (`<E>/src.start.sha256`, `<E>/data.start.sha256`) equals that at the end (`<E>/R6_figures.log`, "diff exit 0"; `<E>/R7_outputs.log`, "data unchanged").

## 1. The tests of success, one by one

| Test | Verdict | Evidence read or produced here |
|---|---|---|
| A1 — Stage 1 before any write, 29 of 29 | met | `A1_stage1.log` opens `2026-10-31T19:32:07Z`, `# pass 29`, `EXIT=0`, closes `19:32:08Z`; the first file written under `src/`, `lib/enrol.js`, was last written at 19:32:38 UTC (`<E>/R8_times.log`). |
| A2 — every check passes | met | Own run, `<E>/R1_checks.log`: `v20.5.1`, `# tests 57`, `# pass 57`, `# fail 0`, `EXIT=0`. |
| A3 — a check for each paired requirement and F-1 to F-7 | **not met — G1** | The 13 requirements `count.csv` pairs with a goal element (R-01 to R-07, R-14, R-15, R-17, R-18, R-20, R-22) and F-1 to F-7 each have a check by name (read in both test files). But R-20's check does not do R-20's test in the register, and the report's reason for that does not hold (G1). |
| A4 — planted faults fail by name | met | The round's `A4_planted.log` shows the diff of each plant and `not ok 26 - F-5 …`, `not ok 53 - search: …`, `not ok 30/41/45 - R-17 …`. The reviewer's own plant (section 5) fails by name too. |
| A5 — round 5's files unchanged but `package.json` | met | `<E>/R6_figures.log`: the round's `src.start.sha256` against now differs only in `./package.json` and the five new files (and data/, left out of the reviewer's list); the round's diff `>     "start": "node server.js",`. |
| A6 — nothing connects, nothing opens | met | `<E>/R6_figures.log` greps `src/`: `server.js:76` `server.listen(…, HOST, …)` with `HOST = '127.0.0.1'` (`server.js:18`); every `fetch` is `app.base + …`; `child_process` and `net` only wrapped to record; `dependencies in package.json: 0`. The walk's `lsof` prints `TCP 127.0.0.1:8139 (LISTEN)` (`<E>/R2_walk.log`). |
| A7 — sources unchanged | met | The trace check, run here: `inputs: 10 of 10 pinned by 20261031T192636Z_MR_issued_C-2026-10-31-25.yaml hash the same now` (`<E>/R4_mechanical.log`). |
| A8 — placement and trace checks exit 0 | met | Run here: `placement check: clean` / `placement exit 0`; `trace check: clean` / `trace exit 0` (`<E>/R4_mechanical.log`). |
| A9 — the record check exits 0 | met | Run here with the round's options (section 6): second run `exit 0`, `## Findings — 0` (`<E>/record_check_2.out`). |
| A10 — started and finished stand beside issued | met | `ledger.py show`, `<E>/ledger_show.out`: three `issued` (19:09:33, 19:26:23, 19:26:36), `started` 19:28:28, `finished` 19:42:35. |

## 2. One figure re-established

- **57 checks = 29 + 13 + 15.** The report counted the TAP output of its run. Here the `test(` calls were counted by `grep -cE '^test\('` in each file (`<E>/R6_figures.log`): `data.test.js 18`, `reset.test.js 3`, `search.test.js 8` (= 29), `goal.test.js 13`, `requirements.test.js 15`, `total 57`; and the reviewer's own run prints 57 lines `^ok`. **Agrees.**
- **"learners 65 after the walk"** (report, section 2): the reviewer's own walk from a fresh reset gave `learners after (2): 65 65` (count, highest number). **Agrees.**
- **Times given in words.** The window's close, 19:42:21 UTC, is the report's last write (stat, `<E>/R8_times.log`: `2026-10-31T19:42:21Z`) and `window.out` line 7 (`last written 2026-10-31T19:42:21.476Z`), naming 94 files written. A1 "before any write": `A1_stage1.log` 19:32:07–19:32:08; the `src/` writes by stat, UTC (`<E>/R8_times.log`): `lib/enrol.js` 19:32:38, `lib/screens.js` 19:33:08, `server.js` 19:33:29, `test/requirements.test.js` 19:35:52, `test/goal.test.js` 19:36:50, `package.json` 19:37:05. **Agree.** The 19:31:38 run "shown in the session" cannot be read here; the logged run is enough for A1.

## 3. The outputs exist

`<E>/R7_outputs.log` (19:48:59 UTC), each at the size and sha256 the report's `outputs` line gives:

```text
3661 f1e54e4fa0364985170b2f3322787fd36225e4011937911774d86658a2c490b0  src/server.js
5324 378230f1b2f82d68ba94ec85acaa5c55d4981deb88124556ab625f4ede5b8a31  src/lib/enrol.js
4703 446a49e6567b3adc57df514416f2bbf5ad3551cfcd38bbeeccdac82e899dfa0b  src/lib/screens.js
18739 afbf7a8a03f8230fe5e8054d4767f426490caccc6e280b1356d5aca94d67a1e8  src/test/goal.test.js
17719 3a095ee99b35c196712017edcd9f968e8808fedd7bfd96d8e579a07c3825d8a2  src/test/requirements.test.js
286 61bd479d6b29fb2018cfefc2cac6ab59cf47ac4adf0e91f2458e548b6f8983ca  src/package.json
```

The evidence folder exists with 84 files; each of the 18 files the report cites was found at its path (same log). The report is at its path, 17806 bytes.

## 4. The running application

No application model was written (this is a Node prototype, not a model on the application's test server), so the form's part 4 reads **not applicable**; the building page's own use of the screens is part 5 below.

## 5. What a review of building runs (the building page, part 2)

**The project's checks again.** `cd src && node reset.js && node --test test/` at 19:44:38 UTC → `# pass 57`, `# fail 0`, `EXIT=0` (`<E>/R1_checks.log`).

**One use of the screens as a school clerk**, without a window, by `<E>/walk.sh` (curl on 127.0.0.1:8139; log `<E>/R2_walk.log`, screens `<E>/screens/`), from a fresh reset (64 learners, highest 64):

1. *A child the registry holds*, learner 12 of `data/learners.json` (Galtemzu / Jortovvin / 2013-11-27 / Dunavel Lakeside School), the family name entered as `gALTEMZU`. Returned (`W1_held.html`):
   ```text
   <h1>An existing learner was found</h1>
   <p>The registry already holds this learner. Nothing new was entered.</p>
   <dt>Learner number</dt><dd>12</dd>
   <dt>Family name</dt><dd>Galtemzu</dd>
   ```
   with the given names, date and school as held, and `<a href="/">Back to the enrolment screen</a>`; learners still 64. Goal S-4 → S-5 → S-7 on SC-2: capitals forgiven (R-05), the four fields shown (Q-10), the way back empty (Q-13). **As ruled.**
2. *A new child* (Brannick / Solvey Amara / 2017-03-09 / Kestrin Hill School). Returned (`W2_new.html`): `<h1>A new learner number was given</h1>` … `New learner number: <strong class="learner-number">65</strong>`; learners 65, the record saved as entered. S-6 → S-7 on SC-3, the number one above the highest held (G-01). **As ruled.**
3. *The new child again.* Returned (`W3_again.html`): SC-2, `<dd>65</dd>`, learners still 65. S-5: nothing new entered — the registry does not register the same child twice. **As ruled.**

Every screen carried `Invented data, Progressa is fictional` (R-17). SC-1 offered the four entries and the three schools. The server was stopped (`listening on 8139 now: 0`) and the data reset.

**One way the goal goes wrong.** From a fresh reset, an entry with the date of birth `2019-02-30` and the school left out (`X1_refused.html`; the same with `school=` sent empty, `X2_refused_empty.html`):

```text
<h1>The entry refused</h1>
<li>Date of birth: names no day of the calendar</li>
<li>School: not entered</li>
```

Both faults named (Q-9), the date as no day (Q-1), the school as missing (Q-5); `learners.json` sha256 `32e01ac3…` before and after, 64 learners — nothing saved (Q-7). The way back, followed with its hidden entries (`X3_back_kept.html`), reopened SC-1 with `value="Brannick"`, `value="Solvey Amara"`, `value="2019-02-30"` and no school chosen (Q-8, Q-13). **As ruled.**

**The planted fault.** In a scratch copy, `<E>/planted/f4-saves/src/` (by `<E>/plant.py`), F-4 was made to save a record and show SC-3. `<E>/R3_planted.log`:

```text
EXIT=1
not ok 25 - F-4 — more than one learner found: SC-5, the entry cannot be completed, nothing saved (set up by a record no clerk's entry can make)
# pass 56
# fail 1
```

with `'SC-3' !== 'SC-5'` in `<E>/R3_planted.tap`. One check fails, by name.

**R-20's test as the register gives it**, run here because G1 turns on it (`<E>/windows.sh`, `<E>/R5_windows.log`): the list of windows read through `CGWindowListCopyWindowInfo` from `osascript -l JavaScript` (no window, nothing brought forward; the command returned at once with the list), the prototype started, reset, a child enrolled by curl, stopped, the list read again:

```text
windows listed before: 252
enrolled through curl on 127.0.0.1: HTTP 200
windows owned by the server's process 37054 while it runs: 0
windows listed after: 252
windows added (in the second list, not the first): 0
```

The prototype passes R-20. The register's test can be run; the round's check does not run it.

**The faults of the page, part 1, read against the report.** Item 1 (a screen reported only after it was seen): the report quotes the screens from the server's output in `_evidence/screens/` — kept. Item 2: checks run, with results — kept. Item 3 (a test on a record the prototype cannot produce): the F-4 check writes a second learner itself; the instruction asks both for that check (ruling G-12) and for item 3, and the report names the conflict for the orchestrator — not counted against the round (section 8). Item 4: nothing added beyond the rulings that I found, but see section 8 on whitespace. Item 5: round 5's files untouched. Item 6: no window opened by the round's checks or this review.

## 6. The four mechanical checks, run by the reviewer

All in `<E>/R4_mechanical.log` (19:46:02–19:46:32 UTC), run directly, by `<E>/mech.sh`:

- **Trace** over the report: `trace check: clean`, `trace exit 0`.
- **Placement** over the instruction under review: `placement check: clean`, `placement exit 0`.
- **Record check**, `--record …/round-06-build/_evidence/record --report … --tolerance 2` (as `check.out` prints on `# run with:`), `--out <E>/record_check.out`: first run `exit 1`, `## Findings — 9`, every one a file of **this review's** planted copy (`<E>/planted/f4-saves/src/…`), which `shutil.copytree` gave its sources' times, inside the round's window. Those files were touched to now and the check run again, `--out <E>/record_check_2.out`: `record check (second run) exit 0`, `## Findings — 0`. The nine were the reviewer's doing, not the round's.
- **Ledger `show`** for C-2026-10-31-25 (`<E>/ledger_show.out`): `issued` ×3, `started` 20261031T192828Z, `finished` 20261031T194235Z. **Account:** `arne.laponin@gmail.com` on each `issued`, on the `started` and on the `finished`; the report's declaration names the same address. `started_by: unknown`, as the report declares.
- **Ledger `check`** (`<E>/ledger_check.out`): `check exit 1`, `check: 2 defects`. The lines naming MR:
  ```text
  input-changed: MR C-2026-10-31-26 — the started of 2026-10-31T19:42:54Z hashes 1 input otherwise than the issued of 2026-10-31T19:09:34Z: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_BUILD_2026-10-31.md (sha256:2a9543ef8b76 at issue, sha256:a6167418b262 at start)
  input-changed: MR C-2026-10-31-28 — the started of 2026-10-31T19:42:11Z hashes 1 input otherwise than the issued of 2026-10-31T19:36:07Z: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31_v2.md (absent at issue, sha256:69b0de25a5b8 at start)
  ```
  (each line cut before its closing clause, «— a finding for the orchestrator and no refusal: …»; the file holds them whole). No line names C-2026-10-31-25. The first is about this review (section 8).

## 7. The verdict

**Not accepted — 1 gap.**

**G1 (item)** — fails A3, and the task's line "one check for each requirement whose test `count.csv` pairs with an element of the goal, written from that requirement's test in the register" (`PROMPT_BUILD_2026-10-31.md`, section 3). `count.csv:65-67` pairs R-20 with S-2, S-3, S-4. R-20's test (`docs/REQUIREMENTS.md:277-279`): «*Set up:* read the list of windows open on the computer's screen, by a command that brings nothing forward.» … «*See:* **Expected:** windows opened: 0 — the second list is the first.» The round's check, `R-20 — a child enrolled through a windowless check: no program launched, nothing loaded that could open a window` (`src/test/requirements.test.js`), reads no list of windows; it asserts no `child_process` launch and no native addon. The report sets the test aside (section 4): «on macOS, reading other applications' windows needs the Screen Recording or Accessibility permission, and asking for it opens a system dialog — a window». That does not hold: the list of windows, with each window's number and owner, was read here by `CGWindowListCopyWindowInfo` through `osascript -l JavaScript`, without asking any permission and without a window (`<E>/R5_windows.log`: 252 before, 252 after, 0 added; this session sees no screen, but the call returned at once with the list, and it is not the image-capture call that asks for Screen Recording). The instruction allowed the fallback only «where the system cannot be asked without a permission or a window» (section 3, on R-21); here it can be asked. The prototype as delivered would carry an R-20 check that does not test R-20, and round 8's note would describe R-20 as checked. **The building page lacks this fault**; proposed for its part 1: *"To set a register's test aside as needing a permission or a window without trying a command that asks for neither; the attempt and what it printed are kept."*

Count by kind: `item=1`.

## 8. Found, not fixed

- **F-4 and the building page's item 3 conflict** in the instruction itself: ruling G-12 asks a check for F-4, which no clerk's entry or reset can reach (`docs/GOAL.md`, F-4: «Under the data's settings it is never reached»); the page refuses a test on a record nothing writes. The round wrote both checks and named the conflict. For the orchestrator to rule; no gap is counted for it.
- **A fourth school is lost on the way back** from SC-4 (SC-1 offers the three only, Q-6), against Q-8's «entries kept»; reported by the round; no ruling covers it.
- **"Spaces only" is read as any whitespace**: `isMissing` uses `trim()`, so a name of tabs or no-break spaces is also F-1; Q-4 says «spaces». A small widening the round did not name; the F-1 check tests `' \t '`.
- **SC-5 for a fault the goal does not name** (a data file unreadable) answers HTTP 500 and its way back carries no entries; reported by the round.
- **The schools are read once, at the server's start**; a reset that changed `schools.json` while the server ran would not be seen. Not reachable with the reset as built (the schools are fixed).
- **The ledger**: C-2026-10-31-25 carries three `issued` entries under `version: 1` with three instruction digests (2a9543…, 2075e6…, a61674…); the instruction was changed twice after this review's own `issued` (19:09:34) pinned it, and this review instruction was not re-issued — hence `ledger.py check`'s `input-changed` on C-2026-10-31-26. This review read the instruction as it stands (a61674…, the last `issued`). For the orchestrator.
- **The reviewer's own planted copy** first made the record check report 9 findings (section 6); a planted copy made with kept file times falls inside a round's window. A note for whoever writes the next review instruction: copy without keeping times.
- **Model**: this review ran on claude-opus-5-5, the band named. Effort `unknown`, as the started entry records.
