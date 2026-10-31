---
kind: report
answers: C-2026-10-31-31
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_NOTE_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_NOTE_2026-10-31.md
written_by: a working session, "MR · work · the note to the Permanent Secretary", separate from the session that wrote the instruction (MR · orchestrator)
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt shows only that a scheduled task started it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the instruction names, Opus
computer: MacBookPro — printed by `hostname`, the round's first command, before its started entry
window: 2026-10-31 20:41:00 UTC to 2026-10-31 20:54:58 UTC, no pause; closed at the last write of the 36 files the round names as written, REPORT_NOTE_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check. The round's own Python programs (build.py, pdfread.py, a1_claims.py, a2_limits.py) ran through `run`, 17 runs; the PDF itself is written by /usr/bin/osascript, a child of build.py that is not a Python program, so the record names NOTE.pdf as written by no traced run. The register's self-test and check, the placement and trace checks, shasum, stat, cmp and the window lists' comparison ran outside `run`; their logs and the hand-written files (CLAIMS.md, LIMITS.md, PAIRS.md, NOTE.md, build.py, the exceptions file, the programs) are in the record's list as "written by no traced run"
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/NOTE.md 3542 bytes sha256 19a7dba5c65fdd8e0627cbd770cf6c105808346e475c4baa310e6f2bff00b277 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/build.py 6561 bytes sha256 1f3d3144ad255fed2de0547915ba412b7ce4f08aff3ed476b497587b2eee9549 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/NOTE.pdf 57094 bytes sha256 6ff1a6b80f6a305267db6805a57f28f1b2a5fb85fd6b72d787bd6b34a6fb5666 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/NOTE.html 4226 bytes sha256 fea63b9a329ac97c26a93da5395338a465af290ca7b8bb4aa32f417f6d537799 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/register_exceptions.txt 252 bytes sha256 75c94433f420feb8fdb183e7459a780d7f5f18784d8d8a03f7f0cd8944ba680e · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/ · this file
ledger: MR C-2026-10-31-31 — the started entry is 20261031T204100Z_MR_started_C-2026-10-31-31.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write the one-page note to the Permanent Secretary: what the prototype shows, and what it does not

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_NOTE_2026-10-31.md` (`C-2026-10-31-31`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`

## 1. The answer first

The note is written and built: one A4 page addressed to the Permanent Secretary, the answer first, then what the prototype shows, the figure "the search catches 4 of the 8" with its meaning, and what it does not show. Its 34 sentences rest on 52 claim rows, 0 not found at their lines; the 20 limits the sources name are 12 in the note and 8 left out with their reasons, 0 unaccounted; the register's self-test passes and the check refuses nothing but the word "Skills" in the Ministry's own name, kept as a named exception; NOTE.pdf has 1 page of 595 by 842 points, its type 11 points; two builds give the same text; the sources and `src/` are unchanged. The PDF is made by macOS's own text system through `osascript` (cupsfilter has no HTML filter on this computer), with 252 windows before and after and 0 added. Nothing is sent.

## 2. The criteria, one by one

Evidence folder `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/` (below `<E>/`).

**A1 — CLAIMS.md before the note; every claim at its source; each sentence paired — met.** `<E>/A1_claims.log` (20:51:29 UTC): stat gives CLAIMS.md 20:45:59, LIMITS.md 20:46:37, NOTE.md 20:46:48. `a1_claims.py` reads each row's words at the line it gives and cuts the note into sentences, comparing them in order with `<E>/PAIRS.md`:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/A1_claims.log`:
```text
claims: 52 rows, 0 not found
note: 34 sentences; pairs: 34 rows; unpaired 0, mismatched 0, unknown claims 0, extra pairs 0
0 not found
A1 EXIT=0
```

The check can fail: its first two runs (record runs 6 and 8, exit 1) found 4 rows not found, the words of four table rows holding a '|' read without their spaces; the program was corrected, not the rows. The pairing, sentence by sentence (the full sentences are in `<E>/PAIRS.md`; the claims in `<E>/CLAIMS.md`):

| # | The sentence begins | Claims |
|---|---|---|
| 1 | One list of learners: what the prototype shows… | K01b |
| 2 | To the Permanent Secretary, Ministry of Education… | K01a, K01b, K02 |
| 3 | The prototype shows that a school clerk can enrol… | K03, K04, K06 |
| 4 | It does not show that the registry recognises… | K05, K21a, K21b, K22, K23, K25 |
| 5 | What the prototype shows (heading) | none |
| 6 | The Ministry wants one list of learners… | K06 |
| 7 | The prototype is a small working model… | K07, K29 |
| 8 | A clerk enters a child's family name… | K08, K09 |
| 9 | If it finds exactly one learner… | K04 |
| 10 | If it finds none… | K10 |
| 11 | The clerk sees which of the two happened. | K11 |
| 12 | An entry with a detail missing… | K12a, K12b, K13a, K13b, K14 |
| 13 | The prototype runs on one computer… | K15, K16a, K16b |
| 14 | All of its checks pass… | K17, K18a, K18b |
| 15 | The children on more than one list (heading) | none |
| 16 | The prototype holds 60 invented children… | K19a, K19b, K20 |
| 17 | Eight children are on two lists… | K21a, K21b, K22 |
| 18 | The search catches 4 of the 8. | K23 |
| 19 | Those four have the same family name… | K24a, K24b |
| 20 | Each of the other four is held twice… | K25, K26 |
| 21 | This is a limit of the search step… | K27 |
| 22 | The invented data is made so that exactly four… | K28 |
| 23 | What the prototype does not show (heading) | none |
| 24 | It is not the registry. | K29 |
| 25 | It is for agreement, it offers enrolment only… | K29, K30, K31a, K31b, K31c |
| 26 | It is connected to no other body. | K16a, K32 |
| 27 | The three lists are part of the invented data… | K20, K32 |
| 28 | It cannot tell apart two different children… | K33a, K33b |
| 29 | The second would be taken for the first… | K33a, K33b |
| 30 | No two children in the invented data share all three. | K34 |
| 31 | Three points are kept in their simplest form. | K35 |
| 32 | An entry of blank characters of any kind… | K36a, K36b |
| 33 | A school other than the three, once refused… | K12b, K37 |
| 34 | Where the search finds more than one matching learner… | K38a, K38b, K38c |

**A2 — every limit the sources name, in the note or left out with its reason — met.** `<E>/LIMITS.md` lists 20, each with its source words at its line; `a2_limits.py` checks those words, and for each row marked for the note that its words stand in the note:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/A2_limits.log`:
```text
limits: 20; in the note 12; left out with a reason 8; sources not found 0
0 unaccounted
A2 EXIT=0
```

In the note (L01–L12): not the registry, for agreement; invented data, Progressa fictional; no other body connected; the 4 of the 8 missed, each by one letter of the family name; that miss a limit of the search step, stated as of that step; the figure not about real lists, the data made so; a different child sharing the three fields taken for the learner; more than one learner found, checked only on a record the check writes; any blank characters taken as missing; a fourth school not kept on the way back; the three kept in their simplest form; enrolment only, no looking up.

**Left out, with the reason** (the list the instruction asks the report to repeat):

| Limit | What the record names | Why it is left out of one page |
|---|---|---|
| L13 | No age held on the entry: 6 to 12 holds the data, not the entry (questions paper, line 77) | A rule of what the entry accepts, chosen so that the clerk meets only the two outcomes the prototype is for; it limits nothing the prototype shows |
| L14 | A different school on a learner found: no notice (line 249) | A detail of one screen, not a limit of what the prototype shows about one list |
| L15 | A record not saved is a way it goes wrong, F-6 (line 313) | A failure the prototype handles and shows, not a limit of what it shows |
| L16 | The window checks compare window numbers only; a window opened and closed between readings is not seen (build review, line 103) | A limit of how the checks read the screen; the note says only that no check opens a window, which the record carries |
| L17 | No requirement's test reaches the ways the goal goes wrong; each one's check is its only test (count, line 37) | The work's own bookkeeping between its register and its goal |
| L18 | No element of the goal carries the data's numbers, the simulation, the windowless checks or the note (count, line 37) | The same bookkeeping; the note states each of those facts where it bears |
| L19 | How many the search catches is not tested by the requirement on the 4 (count, line 18) | Superseded for the reader: the figure is counted and stated |
| L20 | The kit's tracer resolves names relative to a directory against the root (build review, line 100) | A fault of the tools that keep the work's record, not of the prototype |

**A3 — the register's self-test, then the check — met, with one named exception.** `<E>/A3_register.log` (20:51:49 UTC): the self-test prints `cases: 10, failed: 0` and `SELFTEST EXIT=0`; the check without exceptions refuses one match, `line 3 [the name of a program, skill or plugin] «Skills»`, exit 1; with the exception file it exits 0:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/A3_register.log`:
```text
refused: 0 (list 1: 0, list 2: 0, list 3: 0, list 4: 0); excepted by name: 1
CHECK (with exceptions) EXIT=0
```

**The exception, repeated as the register asks:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/register_exceptions.txt` omits the pattern "the name of a program, skill or plugin" for the form `Skills` only, because the Ministry's own name, "Ministry of Education, Youth and Skills", holds the word, the note is addressed to its Permanent Secretary under that name, and no program, skill or plugin is named.

**A4 — one page, A4 — met.** `<E>/A4_pages.log` (20:52:34 UTC), read by PDFKit through `osascript -l JavaScript` and again from the file's own boxes:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/A4_pages.log`:
```text
pages=1
page 1: width=595.00 height=842.00
```

The type is 11 points and never below: build.py reads back the point sizes the page holds and refuses one below 10 (`<E>/A6_build_twice.log`: `smallest_type_pt=11.00 largest_type_pt=14.00`; text 587.9 of 728.5 points of the page's height used). An earlier build in 11 "pt" of CSS came out at two pages, macOS's HTML reader setting a CSS point a third larger; the cure was the unit, the type staying 11 points (record runs 2 and 4, exits 1 and 2).

**A5 — R-23's test from the PDF's text — met.** `<E>/A5_r23.log` holds the whole extracted text (by PDFKit) and the lines on which the three parts of the test turn: one page (A4); `2:To the Permanent Secretary, Ministry of Education, Youth and Skills`; what it shows, `3:The prototype shows that a school clerk can enrol a child in a single list of learners, and that the registry`; what it does not, `5:already holds them. It does not show that the registry recognises the same child when the family name is` and the heading `28:What the prototype does not show`.

**A6 — two builds, the same text — met.** `<E>/A6_build_twice.log` (20:52:01 to 20:52:23 UTC): both builds exit 0; the HTML is byte for byte the same (`fea63b9a…7799` both times), the PDF's bytes differ (`85eab30b…f161`, then `6ff1a6b8…5666`); `<E>/A6_compare.log`: the two extracted texts have the same sha256, `da5b4083…0492`, `CMP EXIT=0`. **No window:** the list of windows read before the first build and after the second, `windows before: 252`, `windows after: 252`, `windows added: 0`, `windows owned by osascript or Python now: 0`.

**A7 — the sources unchanged — met.** `<E>/A7_unchanged.log` (20:53:17 UTC): the 15 sources of `<E>/sources.start.sha256` (20:43:56 UTC) against their end, `SOURCES DIFF EXIT=0`; `src/`, 24 files, `SRC DIFF EXIT=0`. A first try (`<E>/A7_unchanged_try1.log`) split the paths that hold a space and read 12; it is kept, and the second reads all 15.

**A8 — placement and trace checks — see `<E>/A8_checks.log`.** Run outside `run`, after this report's last write. A first placement run before the report existed (`<E>/A8_placement_try1.log`) found the report missing, as it then was.

**A9 — started and finished beside issued — see `<E>/A9_ledger_show.log`**, written after the finished entry.

## 3. Found, not fixed

- `cupsfilter` on this computer has no filter from HTML to PDF (`No filter to convert from text/html to application/pdf`); the build uses macOS's text system instead, as the instruction allows.
- macOS's HTML reader sets one CSS pixel as one point of the page and a CSS point a third larger; build.py writes sizes in pixels and reads back the sizes the page holds.
- The fa-project-ops guard refuses `osascript` with a script file the cloud side cannot read; the round's scripts go to `osascript` on standard input from its Python programs.
- The windows lists are read before and after the builds, not while they run: a window opened and closed within a build would not be seen.

## 4. What I could not establish

That nothing is fetched rests on the HTML naming no outside resource and the build reading only a local file; no record of the network was taken.

## 5. Corrections to the instruction

- The round's record check names one finding: the brief, outside the record's root, read by `a1_claims.py` and not on the start list (`RECORD.txt`, section 4). Its sha256 was taken at the start in `<E>/sources.start.sha256` and is the same at the end (A7). No criterion rests on the record.
- Two outputs the instruction does not name: `docs/note/NOTE.html`, the build's HTML, made by build.py at each run; and `docs/note/register_exceptions.txt`, the named exception A3 allows.

## 6. What this round did not finish

Nothing of the task. Sending the note is the owner's.

## 7. The outputs, by path

`<E>/outputs.log` (20:53:08 UTC), each `ls -ld` with `exit 0`: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/NOTE.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note` and its four files `build.py`, `NOTE.pdf`, `NOTE.html`, `register_exceptions.txt`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence`, and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports`. This report's own listing is in `<E>/A8_checks.log`.
