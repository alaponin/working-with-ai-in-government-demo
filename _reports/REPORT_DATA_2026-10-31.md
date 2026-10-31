---
kind: report
answers: C-2026-10-31-21
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_DATA_2026-10-31.md
written_by: a working session, MR · work · scaffold and made-up data, separate from the session that wrote the instruction (MR · orchestrator)
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt shows only that a scheduled task started it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command after its started entry
window: 2026-10-31 18:50:17 UTC to 2026-10-31 18:58:59 UTC, no pause; closed at the last write of the 51 files the round names as written, REPORT_DATA_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check. The round's node runs (reset and checks) went through `run` and are recorded as commands whose own reads are not traced (node is not a Python program); the reset's own reads are recorded by the reset itself in src/data/reads.json. The shell commands that wrote the evidence logs ran outside `run`: those files are on the record's list as written by no traced run
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/package.json 255 bytes sha256 5edcd8ce794903095d86953ee12a49d83afd4b0f235779c0971edf352cba4def · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/reset.js 2800 bytes sha256 4cb5e74df1671e7ee9c42b1f12d0967be7b78b824465427e1c7806c9c925b254 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/data_files.js 2366 bytes sha256 f53200d909b75b6f3100e77ee1aecf4912420c351935ce8d3a73da9227f6d164 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/lists.js 6044 bytes sha256 28672ec0926001c9068b75af51e5e7be823ef61ebeb8761001d67674b24dff14 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/names.js 2378 bytes sha256 9faa617d8891d79e529801f7e76b5fb0ef97b34d6ae6b0d63d65fae5b3a94f5c · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/random.js 1004 bytes sha256 f7165787e7e27f71bc1bf858f63b0bf2326b2d6b32060072086c0adc68fa47b2 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/lib/search.js 2303 bytes sha256 fc8c5ead71e0cd20d36c92eb8d035646eca408a10616dc893224c5b64285a17a · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/data.test.js 8738 bytes sha256 7e2dd9896dc3f99f4c49116d5f6778305bfdb914f12ec7b53c40690499ce933c · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/reset.test.js 1585 bytes sha256 c608d4f851b95809e4f9a9efc03fedf0bb2ae6be8d663af471f37ff8ac1c931a · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/test/search.test.js 3520 bytes sha256 3eb9433df671b90698f135c4c8b001b100c3f06ce85366cad6fd22894ac8b664 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/enrolments.json 5083 bytes sha256 4435bfa8398d2230c2a45738b633afcb2d3063f523e3390458328be0400bb3dd · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/exam_candidate_list.json 3623 bytes sha256 6be0ea384c1e95e1ff1c59fabe157a5f54ad9fc54d0a3e5050a6eb21476b4224 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/key_table.json 5024 bytes sha256 ae86a420f759f3927a108ee58b2dbd10ab3fd688447e248815f3979d7bbd30da · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/learners.json 11017 bytes sha256 32e01ac3a4a25a130d4b54cbaca140252690e13aa3c20a122210ce0232350b66 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/reads.json 296 bytes sha256 62ffc8413ccf864c57e238644419881854b992cfb18b9652cdc0eaae7f4b6f25 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/school_census.json 3907 bytes sha256 9c62470ee7bb837245f1e4d6b60348ca5d941e240be4ded670fe065adf6a137c · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/schools.json 85 bytes sha256 ba3aef875bd398e24c0cd29322b3173bb6c2b94457927c24532de000e4fa8512 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src/data/social_grant_list.json 3566 bytes sha256 ed1c694c37603d608b2c43bc0cd21c68cdb891e9393e7d2c1b1d674228ca166e · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/ · this file
ledger: MR C-2026-10-31-21 — the started entry is 20261031T185017Z_MR_started_C-2026-10-31-21.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Build the prototype's scaffold in Node.js and the reset that makes the made-up data in the known numbers, with a check for every number

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_DATA_2026-10-31.md` (`C-2026-10-31-21`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`

## 1. The answer first

The scaffold stands under `src/` in Node.js with no dependencies: a seeded generator (seed 20261031), invented name parts written in the source, the generator of the three lists and the key table, the search rule as one module (`lib/search.js`, three fields, capitals ignored, nothing else, given the learners only), and `reset.js`, which writes 8 JSON files under `data/`. `node reset.js` exits 0 and `node --test test/` passes 29 checks of 29, each counting the files the reset wrote: 60 children, 3 schools of 20, 68 entries as 24, 22 and 22, 8 children on two lists in Q-5's pairs, 4 of them spelt differently on the later list, every age 6 to 12 on 2026-10-31, 64 learners numbered 1 to 64, 68 rows in the record of entries. The planted fault (one child dropped, in a scratch copy) fails 7 checks by name; the reset made twice gives identical `data/`; nothing in `src/` connects or opens; the reset reads only files under `src/`; the 15 sources are unchanged. The 64 is reached because the rule misses the 4 differently spelt children, not by any widening of the search.

## 2. The criteria, one by one

### A1 — Stage 1's four outputs, before any write — met

Run at 18:51:33 UTC, after the record's start list (18:51:23 UTC) and before any file under `src/` was written (the first, `package.json`, at 18:52:54 UTC by `RECORD.txt`).

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A1_stage1.log`:

```
$ node --version
v20.5.1
exit 0
$ npm --version
10.9.2
exit 0
$ node -e "require('node:test')"
exit 0
```

and `ls -la` of `src/` showed `README.md` alone (same log, exit 0).

### A2 — the reset exits 0, and every check passes — met

Both ran through `run` (record runs 1 and 2).

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A2_reset_and_checks.log`:

```
# tests 29
# suites 0
# pass 29
# fail 0
```

The reset's own line before the checks reads `exit 0`, and the checks end `exit 0`. The 29 checks by name are in the log: 18 over the data (`test/data.test.js`), 3 over the reset (`test/reset.test.js`: made twice byte for byte the same; `data/` equal to what the reset makes; the record of reads), 8 over the search rule (`test/search.test.js`). Every check of the data reads `data/*.json` through `lib/data_files.js`, a reader that imports nothing from the modules that made the data; each expected number is written in the check from the source it names.

| Number or rule the instruction names | Check (number in the log) |
|---|---|
| 60 children | 2 |
| 3 schools, 20 each (Q-7) | 3, 5 |
| 68 entries, 24, 22, 22 (Q-6) | 6 |
| every date YYYY-MM-DD (Q-10) | 8 |
| every age 6 to 12 on 2026-10-31 (Q-1) | 9 |
| every entry carries a school (Q-9) | 4 |
| 8 on exactly two lists, pairs of Q-5 | 10 |
| 4 spelt differently, on the later list (Q-5) | 11, 13 |
| the rest matching as Q-8 says | 12 |
| no two children share the three fields, capitals ignored (Q-14) | 14 |
| the key table's 68 rows, named as Q-11 gives | 15, 7 |
| 64 learners, numbered 1 to 64 (Q-13, Q-4) | 16 |
| the record of entries, 68 rows (Q-12) | 17, 18 |
| the reset twice, byte for byte | 19, 20 |
| the search compares its three fields, capitals ignored | 22 to 26, 29 |

15 rows, the 15 items of section 3's list of checks.

### A3 — the planted fault — met

In a scratch copy at `_working/round-05-data/_evidence/A3_planted/src`, one line added to `lib/lists.js` drops the last census-only child before the lists are numbered; the reset and the checks run there (record runs 3 and 4).

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A3_planted_fault.log`:

```
not ok 2 - R-09, G-04: 60 different children, named C01 to C60 (Q-11)
```

and with it `not ok` 5, 6, 15, 16, 17 and 18, ending `# fail 7` and `exit 1`. The real `src/lib/lists.js` keeps sha256 `28672ec0926001c9068b75af51e5e7be823ef61ebeb8761001d67674b24dff14`, the value on the `outputs` line.

### A4 — the reset the same every time — met

`node reset.js` twice (record runs 5 and 6), `shasum -a 256 data/*` after each into `A4_first.sha256` and `A4_second.sha256`, both 704 bytes and both sha256 `31feb778e9950b9886aaa300c2ca45d10a08801537183b3cf5f2d9985d1d2c56` by the record's `RECORD.txt`. The diff of the two, in

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A4_reset_twice.log`:

```
exit 0  (0: identical)
```

### A5 — nothing connects and nothing opens — met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A5_nothing_connects.log`: `grep -rnE` for `fetch`, `http`, `https`, `net` as a word, `dgram`, `child_process` and `open(` over every `.js`, `.json` and `.md` file of `src/`, `data/` included, and a second grep for `net` as any substring over every file: both print nothing and end `exit 1  (1: no occurrence)`. `package.json` has no `dependencies` key (`grep -c` prints 0), and there is no `node_modules` or `package-lock.json`. Nothing in the round opened a window: every command ran in the shell, the checks with `node:test`.

### A6 — the reset's record of its reads — met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A6_reads.log` quotes `src/data/reads.json`: five files, `lib/lists.js`, `lib/names.js`, `lib/random.js`, `lib/search.js` and `reset.js`, each `"under_src": true`. The reset finds them from the module tree Node keeps for it; it reads no file by `fs`. Check 21 holds it.

### A7 — the sources unchanged — met

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/A7_sources_unchanged.log`:

```
exit 0  (0: all 15 unchanged)
```

The 15 files are listed with their sha256 in `sources_sha256_start.txt` (18:51:34 UTC) and `sources_sha256_end.txt` (18:56:45 UTC): the brief, the register, the groundwork and its three CSVs, the two papers, the count, the ruling D-2026-10-31-09, the building page, the constants, the procedure, the report form and this instruction.

### A8 — the placement and trace checks — met

Both run outside `run`, after this report was first written; both print `clean` and exit 0. They are run again, outside `run`, after the report's last write, with the record check, and their output kept in `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/record/A8_checks.log`. The trace check reads `outputs: 7 of 7 named exist` and `inputs: 9 of 9 pinned by 20261031T184747Z_MR_issued_C-2026-10-31-21.yaml hash the same now`.

### A9 — the record check

Run as the round's last act before the `finished` entry, with this report; its output is `record/check.out`. Its exit is given in the `finished` entry's outcome. The `end` list itself found 0 findings (`RECORD.txt`, section 4).

### A10 — the ledger entries

Read with `ledger.py show` after the `finished` entry, into `record/A10_ledger_show.log`; the review reads them there.

## 3. Found, not fixed

- The data alone cannot say which of a child's two spellings is "the" different one: both differ from each other. Check 13 holds the consequence Q-5 fixes instead — the earlier list's spelling is the first learner's, the later list's makes a second, higher-numbered learner. Round 7 reads the 4 the same way. (`src/test/data.test.js`)
- `WHAT_IS_RUNNING.md`'s Open block names this round's outputs under `~/IdeaProjects/mini-registry/`, a path that does not exist on this Mac (`ls ~/IdeaProjects`: no such file); the instruction's paths under `~/Documents/Dev/wai-demo/mini-registry/` were used. (`WHAT_IS_RUNNING.md`, produced by `ledger.py views`)
- `src/data/schools.json` (the 3 schools, for round 6's choice of school, ruling G-07) is not named among the instruction's examples; it is written by the reset like every other file under `data/`.

## 4. What I could not establish

Nothing the instruction asks.

## 5. Corrections to the instruction

None. The round ran on the model the instruction names.

## 6. What this round did not finish

Nothing. Round 6 builds the screens on `lib/search.js` as it stands and on `data/learners.json`; round 7 counts the 8 from `data/key_table.json` and `data/enrolments.json`.

## 7. The outputs, by path

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-05-data/_evidence/ls_places.log` (18:56:54 UTC) holds `ls -ld` of `src/`, `src/lib/`, `src/data/`, `src/test/`, `src/package.json`, `src/reset.js`, the evidence folder and `_reports/`, each `exit 0`. The 18 files under `src/` with their sizes and sha256 are on the `outputs` line and in `_working/round-05-data/_evidence/outputs_src.txt`; `src/README.md` was there before the round and is untouched.
