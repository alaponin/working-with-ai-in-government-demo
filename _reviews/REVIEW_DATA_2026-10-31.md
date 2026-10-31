---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_DATA_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md (C-2026-10-31-21)
written_by: a session that neither wrote nor carried out the instruction — MR · review · scaffold and made-up data, a sub-agent with a fresh context
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, this session's first command, beside its started entry
window: 2026-10-31 18:59:27 UTC to this file's last write (between 19:05:51 and 19:07 UTC), no pause; opened at this review's started entry (20261031T185927Z_MR_started_C-2026-10-31-22.yaml); the exact close, read by `stat` after the last write, is kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data-review/_evidence/W_window.log
verdict: accepted
downstream_artefact: the orchestrator's closed entry for C-2026-10-31-22, which closes C-2026-10-31-21 through its subject
---

# REVIEW — the scaffold and the made-up data (round 5)

This review ran the project's checks itself, counted the data by its own program, planted two faults in scratch copies, and ran the four mechanical checks. Every log is under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data-review/_evidence/` (below, `<ev>/`).

**Verdict: accepted.** All ten criteria are met on evidence read or produced here; every figure the review counted agrees with the report and with the setting or ruling that fixes it; no gap.

## 1. The tests of success, one by one

| Test | Met? | Evidence read or produced here |
|---|---|---|
| A1 Stage 1 before any write | met | `_working/round-05-data/_evidence/A1_stage1.log` stamped 18:51:33Z shows `v20.5.1`, `10.9.2`, `node -e "require('node:test')"` exit 0, and `ls -la src` with `README.md` alone. The round's `record/RECORD.txt` gives the first write under `src/`, `package.json`, at `2026-10-31T18:52:54.585Z`, after it. |
| A2 reset exits 0, every check passes | met | Re-run here: `<ev>/B2_project_checks.log` — `exit 0` after the reset, then `# tests 29`, `# pass 29`, `# fail 0`, `exit 0`. The round's own log `A2_reset_and_checks.log` reads the same (lines 161–169). Counted by file: 18 tests in `data.test.js`, 3 in `reset.test.js`, 8 in `search.test.js`. |
| A3 planted fault fails by name | met | The round's `A3_planted_fault.log`: `entries.school_census.pop(); // PLANTED FAULT (A3)`, then `not ok` 2, 5, 6, 15, 16, 17, 18, `# fail 7`, `exit 1`. Confirmed again by two plants of this review's own (part 5). Real `lib/lists.js` keeps `28672ec0…` (checked here at 19:02Z). |
| A4 reset twice identical | met | `A4_reset_twice.log`: `exit 0  (0: identical)`; `shasum` of `A4_first.sha256` and `A4_second.sha256` both `31feb778…`, computed here. This review's own reset (B1 against B3) left every byte of `src/` unchanged: `diff exit 0`. |
| A5 nothing connects, nothing opens | met | Re-searched here, `<ev>/B5_nothing_connects.log`: the only `require(` targets are `node:fs`, `node:path`, `node:test`, `node:assert/strict` and the project's own files; no `fetch`, `http`, `https`, `net`, `dgram`, `child_process`, `open(`, `spawn`, `exec`, `socket`, `listen`; `package.json` has no `dependencies`; no `node_modules`, no `package-lock.json`. |
| A6 reads only under `src/` | met | `src/data/reads.json` lists `lib/lists.js`, `lib/names.js`, `lib/random.js`, `lib/search.js`, `reset.js`, each `"under_src": true` (read in `<ev>/B4_own_count.log`). `reset.js` uses `fs` only for `mkdirSync` and `writeFileSync` (lines 64–66); `lists.js`, `names.js`, `random.js` and `search.js` load no `fs`. |
| A7 sources unchanged | met | `sources_sha256_start.txt` and `sources_sha256_end.txt` differ only in their header line (diffed here); 15 files each. The trace check run here: `inputs: 9 of 9 pinned by 20261031T184747Z_MR_issued_C-2026-10-31-21.yaml hash the same now`. |
| A8 placement and trace checks exit 0 | met | Re-run here (part 6): both `clean`, `exit 0`. |
| A9 record check exits 0 | met | Re-run here with the options of the round's `check.out` (part 6): `## Findings — 0`, `exit 0`. |
| A10 started and finished stand | met | `ledger.py show` re-run here prints `issued` 18:47:47Z, `started` 18:50:17Z and `finished` 18:59:12Z of version 1 (part 6). |

**Times and counts the report gives in its own words, read at their source.** The window opens at 18:50:17 UTC, the `written` of the started entry; it closes at 18:58:59 UTC, and `stat` of the report reads `2026-10-31 18:58:59 UTC` (`window.out` line 7: `last written 2026-10-31T18:58:59.917Z`). "51 files the round names as written": `window.out` line 7 says 51; `RECORD.txt` lists 50 changed inside the end list, the report being the 51st. "18 files under `src/`": 5 in `lib/`, 3 in `test/`, 8 in `data/`, `reset.js`, `package.json`. "15 sources": 15 lines below each header. "7 checks" fail in A3: counted above.

## 2. One figure re-established

**The figures:** every number the instruction's section 3 fixes. **The report's route:** the round's 29 `node:test` checks, through `lib/data_files.js`. **This review's route:** `<ev>/count_data.py`, Python run with `/usr/bin/python3 -I`, sharing no code with the round. It reads `src/data/*.json`, and applies the search rule itself, its compared fields read from `docs/groundwork/search_rule.csv`, in Q-2's order. Its output is `<ev>/B4_own_count.log` (19:01:33 UTC):

| Figure | Counted here | Fixed by | Agrees |
|---|---|---|---|
| children | 60 | `settings.csv:2` · G-04 | yes |
| schools; children per school | 3; 20, 20, 20 | `settings.csv:3` · Q-7 | yes |
| entries per list; in all; key-table rows | 24, 22, 22; 68; 68 | Q-6 · `settings.csv:7` · Q-11 | yes |
| children on more than one list; on exactly two | 8; 8 | `settings.csv:4`, `:8` | yes |
| the 8 by pair: census+candidate, census+grant, candidate+grant | 3, 3, 2 | Q-5 A | yes |
| spelt differently; in capitals only; other field differing | 4; 0; 0 | `settings.csv:5`, `:11` · Q-8 A | yes |
| the 4 by pair | 1, 2, 1 | Q-5 A | yes |
| the 4, on the later list | C24 census:20 `Prarasel` → candidate:20 `Praresel`; C50 census:17 `Temnok` → grant:19 `Tomnok`; C56 census:22 `Orowes` → grant:9 `Orowus`; C58 candidate:14 `Tumitem` → grant:2 `Tomitem` | Q-5 (the later list in Q-2's order) | yes |
| the other 4, letter for letter | 4 | `settings.csv:12` | yes |
| dates not `YYYY-MM-DD` | 0 | Q-10 | yes |
| ages on 2026-10-31, lowest and highest | 6 and 12 (6: 11, 7: 10, 8: 3, 9: 12, 10: 9, 11: 11, 12: 12 entries) | `settings.csv:6`, `:16` · Q-1 | yes |
| three-field keys shared by two children | 0 | `settings.csv:13` · Q-14 | yes |
| learners by the rule applied here | 64 | Q-13 | yes |
| searches finding more than one | 0 | `search_rule.csv:17` | yes |
| of the 8, joined by the rule | 4 (of the 4 spelt differently: 0) | `settings.csv:14` · G-05 | yes |
| `learners.json` rows, numbered 1–64 | 64, yes | Q-13 · Q-4 | yes |
| `learners.json` and `enrolments.json` equal to what this review's rule makes | yes, yes | G-03 · Q-12 | yes |

The sha256 of the 8 data files printed by the program equal those on the report's `outputs` line.

## 3. The outputs exist

The record check run here (part 6) reads each of the 18 files under `src/` named on the `outputs` line at the size and sha256 declared (`output as declared: …`, 18 lines, `<ev>/round_record_check.out`). The trace check reads `outputs: 7 of 7 named exist`. `src/README.md` is unchanged and still tracked by git; `git status` shows `src/` untracked, never committed, as the instruction asked. `ls_places.log` holds the `ls -ld` of the 8 places written. `RECORD.txt` section 1 names no file changed outside `src/`, the round's evidence folder and the report.

## 4. The running application

Not applicable: round 5 writes no application model and no screen; the screens and the enrolment goal are round 6's.

## 5. What a review of building runs (`_kinds/building.md`, part 2)

- **The project's checks again, in my own run:** `cd …/src && node reset.js && node --test test/`, kept in `<ev>/B2_project_checks.log` — reset `exit 0`, `# pass 29`, `# fail 0`, `exit 0`. `src/` is byte-identical before and after (`<ev>/B1_src_before.sha256`, `<ev>/B3_src_after.sha256`).
- **The planted fault, of this review's own** (scratch copies under `<ev>/`, diffs `<ev>/P1.diff`, `<ev>/P2.diff`):
  - P1, a fifth child spelt differently (one row of `THE_EIGHT` set to `true`): `<ev>/P1_fifth_spelt.log` — `not ok` 11, 12, 13, 16, 18; `# fail 5`; `exit 1`.
  - P2, one date in another form (`social_grant_list:1` written `01.05.2015`): `<ev>/P2_date_form.log` — `not ok 8 - Q-10, G-07: every date YYYY-MM-DD…`; `# fail 1`; `exit 1`.
  - Real `src/lib/lists.js` keeps `28672ec0…` afterwards.
- **One use of the screens, and one way the goal can go wrong:** not applicable, as the review instruction says: round 5 builds no screen and no goal. Instead, **`src/lib/search.js` read against `docs/groundwork/search_rule.csv`, row by row:**
  - compares family name, given names, date of birth (rows 2–4): `COMPARED`, line 12. Agrees.
  - forgives capitals (row 5): `same()`, `toLowerCase` on both sides, line 16. Agrees.
  - forgives nothing else (row 6): no trim or normalisation. Check 25 shows a trailing space, a dropped name and `09.03.2016` all unmatched. Agrees.
  - does not compare the school or any other field (rows 7–8): `isMatch` reads only `COMPARED` (line 20). Check 26. Agrees.
  - does not read the key table (row 9): the module requires nothing and names neither `key_table` nor `enrolments`. Check 29. Agrees.
  - when: after all four entered, and first (rows 10–11): this is not in the module, and is round 6's to place. See part 8.
  - where: among learners only (row 12): `search(learners, entry)`. Agrees.
  - at reset, the same rule in a fixed order (row 13): `reset.js` lines 46–51 call `enrol` per list in `LISTS` order, entries in number order. Agrees.
  - exactly one: shows it, enters nothing (row 14): `found`, line 42. Agrees.
  - none: a new number by `learner_number` (row 15): highest + 1, line 30. Agrees (see part 8).
  - more than one: nothing entered, cannot be completed; never reached (rows 16–17): `refused`, line 45, and 0 such searches counted here. Agrees.
  - tells which happened (row 18): `outcome` returned. Agrees.
- **The faults of the kind (part 1) read against the report:**
  - 1: nothing is reported as a running screen.
  - 2: the checks were run and their results kept.
  - 3: tests start from data the reset writes. The search unit tests use one invented record of the data's form.
  - 4: nothing was widened past what was asked.
  - 5: the defects seen in the groundwork and records are reported, not repaired.
  - 6: no window was opened.
  - None is broken.

## 6. The four mechanical checks, run here

All in `<ev>/M_mechanical_checks.log` (19:02:22–19:02:23 UTC):

```text
/usr/bin/python3 <orchestrator>/scripts/trace_check.py --constants …/mini-registry/CONSTANTS.md --coordination …/_coordination/CONSTANTS.md …/REPORT_DATA_2026-10-31.md   → trace check: clean · exit 0
/usr/bin/python3 <orchestrator>/scripts/placement_check.py --constants …/mini-registry/CONSTANTS.md …/PROMPT_DATA_2026-10-31.md                                      → placement check: clean · exit 0
/usr/bin/python3 -B <orchestrator>/scripts/round_record.py check --record …/round-05-data/_evidence/record --report …/REPORT_DATA_2026-10-31.md --tolerance 2 --out <ev>/round_record_check.out   → ## Findings — 0 · quoted blocks read against the file they name: 5 · exit 0
/usr/bin/python3 <orchestrator>/scripts/ledger.py show --constants …/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-21   → issued, started, finished, version 1 · exit 0
/usr/bin/python3 <orchestrator>/scripts/ledger.py check --constants …/_coordination/CONSTANTS.md                                   → check: clean · exit 0
```

`ledger.py check` prints no line naming `MR`; its whole output is `check: clean`.

**The account on the three entries:** the `issued`, `started` and `finished` entries each read `account: arne.laponin@gmail.com`. The report's declaration names the same address. They agree.

## 7. The verdict

**Accepted — no gap.** Every criterion A1 to A10 is met on evidence read or produced here. Every number of the instruction's section 3 is re-established by a separate program. Faults planted by this review fail the checks by name. The search module matches `search_rule.csv` row for row. No fault of the kind is shown, so nothing is owed to the page of the kind.

## 8. Found, not fixed

- **Check 9, ages 6 to 12, passes on a date it cannot read.** `ageOn` (`src/lib/data_files.js:57-63`) gives `NaN` for `01.05.2015`, and `NaN` escapes `a < 6 || a > 12` (`src/test/data.test.js:70`). In P2 only check 8 failed. Today check 8 guards the data; check 9 alone would not.
- **The search module does not hold the "when" of the rule.** `same()` turns both sides with `String()`, so a missing field on both sides compares equal. `enrol` saves without asking that all four be entered (`search_rule.csv:10` «after the clerk has entered all four»). It also saves without refusing another date form (`settings.csv:17` «YYYY-MM-DD; any other form refused»). Round 6's entry screen must enforce both before it calls `enrol`.
- **"Never given twice" depends on the learners held.** `nextLearnerNumber` (`src/lib/search.js:30-34`) is highest + 1 over the learners held, so `settings.csv:9` «never given twice» holds only while no learner is removed. Round 6 should never remove one.
- **No two children share a family name.** The generator gives all 60 children different family names (`src/lib/lists.js:72-80`), more than Q-14 asks. So the data hold no two different children with one family name. This sets no number wrong, but round 6 has no list case where the search must tell such children apart by given names or date.
- **Paths in the ledger entries.** The ledger's entries for C-2026-10-31-21 name paths under `~/IdeaProjects/mini-registry/`, as the report found of `WHAT_IS_RUNNING.md`. `show` resolves them to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/` "on this computer".
- **This review's files on the round's record.** The record check run here lists this review's evidence files as "added after the window closed". The round's record has the whole `mini-registry/` as its root. It is not a finding of the record, which reads 0.
- **Model and effort.** The review ran on Opus, the band its instruction names. Its effort is recorded as `unknown`, as the review form says for a sub-agent.
- **The trace check over this review.** It agrees on every declaration, and prints one `input-changed` for the report: «absent at issue (20261031T184748Z_MR_issued_C-2026-10-31-22.yaml), sha256:ac43579f604c at start, sha256:ac43579f604c now». The review form explains this: the report did not exist when the review instruction was issued, and its being hashed at start is the report coming into being. The hash at start equals the hash now, so the report did not change during the review. The program flags a case the form names as expected; that gap is the program's, not the round's.
- **`src/` at the end.** At 19:05:03 UTC `src/` is byte-identical to its state before this review (`<ev>/B6_src_end.sha256` against `<ev>/B1_src_before.sha256`: `diff exit 0`).
