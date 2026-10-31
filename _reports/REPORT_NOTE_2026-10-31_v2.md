---
kind: report
answers: C-2026-10-31-31
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_NOTE_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_NOTE_2026-10-31_v2.md
written_by: a working session, "MR · work · the note to the Permanent Secretary", version 2, with an empty memory, separate from the session that wrote the instruction (MR · orchestrator)
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt shows only that a scheduled task started it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the instruction names, Opus
computer: MacBookPro — printed by `hostname`, the round's first command, before its started entry
window: 2026-10-31 21:11:42 UTC to 2026-10-31 21:24:27 UTC, no pause; closed at the last write of the 38 files the round names as written, REPORT_NOTE_2026-10-31_v2.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check. The round's own Python programs (a1_claims.py, a2_limits_v2.py, pdfread.py, build.py) ran through `run`, 12 runs; the PDF itself is written by /usr/bin/osascript, a child of build.py that is not a Python program. The register's self-test and check, the placement and trace checks, shasum, stat, cmp, diff and the windows comparison ran outside `run`; their logs and the hand-written files (LIMITS.md, CLAIMS.md, PAIRS.md, the change to NOTE.md, a2_limits_v2.py) are in the record's list as written by no traced run. Four files were written before `start` (section 5)
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/NOTE.md 3753 bytes sha256 c537d7041de582a060d79d608bf9af08d2bab5d7ee5fb40e3df07056bd8083fb · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/build.py 6561 bytes sha256 1f3d3144ad255fed2de0547915ba412b7ce4f08aff3ed476b497587b2eee9549 (unchanged) · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/NOTE.pdf 57324 bytes sha256 46a1e66e74cbbb85c1bc195689057e2c788700e12c1e19b654ecd8758725a677 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/NOTE.html 4437 bytes sha256 5167c1e6b8ec9487e32cf8923d798c5e0e38127c781bb2e02d16b3d63db036a1 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/ · this file
ledger: MR C-2026-10-31-31 — the started entry is 20261031T211142Z_MR_started_C-2026-10-31-31.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write the one-page note to the Permanent Secretary: what the prototype shows, and what it does not (version 2)

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_NOTE_2026-10-31.md` (`C-2026-10-31-31`, version 2) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`

## 1. The answer first

G1 is closed in the note: it now says that a name is not limited in length and no character in it is refused. The limits were listed again from every ruled answer — the 13 rows of the gaps paper and its G-14, the 14 of the earlier questions paper, the 13 of the goal's questions paper, the rulings of 21:56, the brief and the register, and version 1's rows — 65 rows, 38 of them limits; **besides Q-4's, 7 limits were missing from version 1's list** (G-05, G-07, G-14 of the gaps paper; Q-9, Q-10, Q-14 of the earlier questions paper; G-12): 2 of them already stated in version 1's note, 2 added to the note, 3 left out with their reason. The note changed by three insertions and nothing else; it is still one A4 page (text 612.9 of 728.5 points used, type 11 points); 60 claim rows, 0 not found; 36 sentences, each paired; 0 unaccounted; the register check refuses nothing but the excepted "Skills"; two builds give the same text; the 21 sources and `src/` are unchanged. Nothing is sent: the owner does not send the note.

## 2. The criteria, one by one

Evidence folder `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/` (below `<E>/`).

**G1, and the rule behind it.** `<E>/LIMITS.md` lists every closing proposal of the three papers and every other limit the record names, each with the column "A limit?" and "v1" (version 1's row, or `none`). `a2_limits_v2.py` counts the limits version 1's list lacked:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/A2_limits.log`:
```text
limits version 1's list lacked: 8 (G05, G07, G12, G14, P09, P10, P14, Q04a); besides Q-4's: 7 (G05, G07, G12, G14, P09, P10, P14)
```

| Row | The limit | Ruled by | Where it goes now |
|---|---|---|---|
| Q04a | A name has no longest length and no character refused (goal's questions paper, line 115) | D-2026-10-31-07 | **added to the note**: «A name is not limited in length, and no character in it is refused.» |
| G07 | A date of birth only as YYYY-MM-DD, any other form refused (gaps paper, line 32; the goal, line 32, F-2) | D-2026-10-31-03 | **added to the note**: «a date of birth not written as year, month and day or not naming a real day» |
| G05 | None of the 8 differs in capitals only (gaps paper, line 30 and 196) | D-2026-10-31-03 | **added to the note**: «None of the eight differs in capital letters alone, so the figure does not show capital letters being set aside.» |
| G14 | A space is part of a name; the search forgives capitals only (gaps paper, line 20, closed from the brief) | the brief | already in version 1's note: «the search treats every difference other than capital letters as a different child» |
| P14 | No two different children share all three, capitals ignored (earlier questions paper, line 281) | D-2026-10-31-05 | already in version 1's note: «No two children in the invented data share all three.» |
| G12 | The checks are the register's own tests, as programs (gaps paper, line 37) | D-2026-10-31-03 | left out, with its reason (below) |
| P09 | Every list carries a school, the same on both lists of the 8 (earlier questions paper, line 187) | D-2026-10-31-05 | left out, with its reason (below) |
| P10 | Every list holds dates as YYYY-MM-DD (earlier questions paper, line 206) | D-2026-10-31-05 | left out, with its reason (below) |

The other 27 rows that are not limits (settings of the invented data, definitions, refusals the note already states) are each listed with where they stand; none is left without a place.

**A1 — CLAIMS.md before the note; every claim at its source; each sentence paired — met, with one row added after the change.** `<E>/A1_claims.log` (21:20:48 UTC): stat gives LIMITS.md 21:19:03; NOTE.md's last write 21:20:12; CLAIMS.md and PAIRS.md 21:20:32. CLAIMS.md was written with version 1's 52 rows and seven new ones (K32b, K39a–b, K40a–b, K41a–b) before LIMITS.md and before the note was changed (stat keeps only its last write); one row, **K41c**, was added after the change, when the pairing showed that «so the figure does not show capital letters being set aside» needed the gaps paper's line 179, «so that line 13's «(capitals ignored)» is exercised by the data», beside line 196. `a1_claims.py` is version 1's program, unchanged:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/A1_claims.log`:
```text
claims: 60 rows, 0 not found
note: 36 sentences; pairs: 36 rows; unpaired 0, mismatched 0, unknown claims 0, extra pairs 0
0 not found
A1 EXIT=0
```

The pairing is in `<E>/PAIRS.md`: version 1's 34 sentences, with sentence 12 changed (now K12a, K12b, K13a, K13b, K14, K39a, K39b, K40b), sentence 13 added («A name is not limited in length…», K40a, K33b), sentence 24 added («None of the eight differs in capital letters alone…», K41a, K41b, K41c, K40b), and K32b — the gaps paper's line 36, «None: the three lists are data inside the prototype, not bodies it connects to» — added to sentences 28 and 29, the source the review of version 1 named for K32's fact. The other sentences and their claims are version 1's, row for row.

**A2 — every limit, in the note or left out with its reason → 0 unaccounted — met.** `<E>/A2_limits.log` (21:20:48 UTC):

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/A2_limits.log`:
```text
rows: 65; limits among them: 38; in the note 37; left out with a reason 28; sources not found 0; rulings not found 0
0 unaccounted
A2 EXIT=0
```

The program can fail: run over version 1's note, the same list gives `5 unaccounted` and `A2(before) EXIT=1` (`<E>/A2_limits_before_change.log`), the five rows the change carries (G05, G07, Q01, Q04a, C21). The four rulings are read at their line 8: D-03 and D-07 «Rule all 13 as recommended», D-05 «Rule all 14 as recommended», D-11 «let's currently go with simplest approaches».

**Left out, with the reason** — every row marked `left out` that is a limit (the list the report repeats):

| Row | The limit | Why it is left out of one page |
|---|---|---|
| G12 | The checks are the register's own tests, as programs | The note says that all of the prototype's checks pass and calls them its checks; which tests those are is the work's own bookkeeping (as C17), and the reader is told what the prototype does and refuses, not how it is tested |
| P09 | Every list carries a school, the same on both lists of each of the 8 | The search does not compare the school, so the figure would be the same without it; the note names the three details the search compares, and the school is not among them |
| P10 | Every list holds dates as YYYY-MM-DD, none in another form | A way the invented data is made uniform; the note says the data is made so and that the figure does not say how many children a registry would hold twice on real lists, which covers real lists written in other forms; one page |
| Q02 | No age is held on the entry: 6 to 12 holds the data, not the entry | A rule of what the entry accepts, chosen so that the clerk meets only the two outcomes the prototype is for; it limits nothing the prototype shows, and one page has no room for the rules of entry beyond the refusals named |
| Q03 | A record not saved, or a number not given, is a way it goes wrong | A failure the prototype handles and shows, not a limit of what it shows; one page |
| Q11 | A different school on a learner found: no notice, nothing changed | A detail of what one screen shows, not a limit of what the prototype shows about one list of learners; one page |
| V16 | The window checks compare window numbers only; a window opened and closed between readings is not seen | A limit of how the checks read the screen; the note says only that no check opens a window, which the record carries |
| V20 | The kit's tracer: the build's record check exits 1 | A fault of the tools that keep the work's record, not of the prototype |
| C17 | No requirement's test reaches the ways the goal goes wrong; each one's check is its only test | The work's own bookkeeping between its register and its goal |
| C18 | No element of the goal carries the data's numbers, the simulation, the windowless checks or the note | The same bookkeeping; the note states each of those facts where it bears |
| C19 | How many the search catches is not tested by the requirement on the 4 | Superseded for the reader: the figure is counted and stated |

Q02, Q03, Q11, V16, V20, C17, C18 and C19 are version 1's L13, L15, L14, L16, L20, L17, L18 and L19, their reasons unchanged. The rows that are not limits and are left out carry their reason in `<E>/LIMITS.md` (G01, G03, G06, G09, G10, G13, P01–P07, P11–P13, Q13).

**A3 — the register's self-test, then the check — met, with one named exception.** `<E>/A3_register.log` (run outside `run`): `cases: 10, failed: 0`, `SELFTEST EXIT=0`; the check without exceptions refuses one match, `line 3  [the name of a program, skill or plugin]  «Skills»`, `CHECK (no exceptions) EXIT=1`; with the exception file:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/A3_register.log`:
```text
refused: 0 (list 1: 0, list 2: 0, list 3: 0, list 4: 0); excepted by name: 1
CHECK (with exceptions) EXIT=0
```

Over the PDF's extracted text the same, `CHECK (PDF text, with exceptions) EXIT=0` (`<E>/A3_register_pdftext.log`). **The exception, repeated as the register asks:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note/register_exceptions.txt`, unchanged since version 1, omits the pattern "the name of a program, skill or plugin" for the form `Skills` only, because the Ministry's own name, "Ministry of Education, Youth and Skills", holds the word, the note is addressed to its Permanent Secretary under that name, and no program, skill or plugin is named.

**A4 — one page, A4 — met.** `<E>/A4_pages.log` (21:21:59 UTC), by PDFKit through `osascript -l JavaScript`, by the file's own bytes and by Spotlight:

`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence/A4_pages.log`:
```text
pages=1
page 1: width=595.00 height=842.00
```

The bytes give `/MediaBox [0 0 595 842]` and one page object; `kMDItemNumberOfPages = 1`. The type is 11 points (build.py: `smallest_type_pt=11.00 largest_type_pt=14.00`), the three insertions taking the text from 587.9 to 612.9 of 728.5 points of the page's height (`<E>/A6_build_twice.log`).

**A5 — R-23's test from the PDF's text — met.** `<E>/A5_r23.log` holds the whole extracted text (PDFKit), numbered, and the lines on which the test turns: one page (A4, above); addressed, `2:To the Permanent Secretary, Ministry of Education, Youth and Skills`; what it shows, `3:The prototype shows that a school clerk can enrol a child in a single list of learners, and that the registry`; what it does not, `5:already holds them. It does not show that the registry recognises the same child when the family name is` and the heading `30:What the prototype does not show`. The three insertions stand in the PDF's text (searched with its lines joined): «not written as year, month and day», «A name is not limited in length, and no character in it is refused.», «None of the eight differs in capital letters alone, so the figure does not show capital letters being set aside.»

**A6 — two builds, the same text — met.** `<E>/A6_build_twice.log` (21:21:38 to 21:21:48 UTC): `BUILD1 EXIT=0`, `BUILD2 EXIT=0`; the HTML byte for byte the same (`5167c1e6…36a1` both times), the PDF's bytes differ (`cdb7a645…2b6e`, then `46a1e66e…a677`); `<E>/A6_compare.log`: both texts `4a6756a6…d24b`, `CMP EXIT=0`, 687 words each. **No window:** `windows before: 253`, `windows after: 253`, `windows added: 0`, `windows owned by osascript or Python now: 0`. build.py is version 1's, unchanged (`1f3d3144…9549`, `<E>/note_diff.log`).

**A7 — the sources unchanged — met.** `<E>/A7_unchanged.log` (21:22:18 UTC): the 21 sources of `<E>/sources.list` (version 1's 15, with the earlier questions paper, the gaps paper, the review of version 1, the rulings D-05 and D-14 and the review instruction), sha256 at the start (`<E>/sources.start.sha256`, 21:14 UTC) against the end, `SOURCES DIFF EXIT=0`, `sources at start: 21; at end: 21`; `src/`, 24 files, `SRC DIFF EXIT=0`.

**A8 — placement and trace checks — see `<E>/A8_checks.log`**, run outside `run` after this report's last write.

**A9 — started and finished beside issued — see `<E>/A9_ledger_show.log`**, written after the finished entry.

**The change to the note, word by word.** `<E>/note_diff.log` compares version 1 (`<E>/NOTE.v1.md`, copied before the change) with the note now: «that does name» becomes «written as year, month and day or not naming»; «A name is not limited in length, and no character in it is refused.» is inserted after the refusals; «None of the eight differs in capital letters alone, so the figure does not show capital letters being set aside.» closes the figure's paragraph. Nothing else moved.

## 3. Found, not fixed

- **A school other than the three** (the review of version 1, section 8): the clerk's screen offers only the three, and such a school reaches the registry only when sent around it (goal's questions paper, lines 142 and 144). The note says such a school is refused, without saying the screen offers only the three. Not a missing limit, and this version changes the note only for missing limits; for the orchestrator.
- **«Progressa is fictional»** is said to a reader whom the constants place inside Progressa's story; carried by the record; for the owner, as the review of version 1 said.
- **All 60 children have different family names** (`_reviews/REVIEW_DATA_2026-10-31.md:125`), outside the record this instruction names; not counted.
- The ledger's `issued` entry pins an input path cut at its first space (the review of version 1, section 8); a fault of the kit.
- `cupsfilter` has no filter from HTML to PDF on this computer; the build uses macOS's own text system, as in version 1.

## 4. What I could not establish

That nothing is fetched rests on the HTML naming no outside resource and the build reading only a local file; no record of the network was taken.

## 5. Corrections to the instruction

- Four files were written into the evidence folder before `round_record.py start`: `sources.list`, `sources.start.sha256`, `src.start.sha256` and `NOTE.v1.md` (at 21:14:44 UTC, `start` at 21:14:44.958Z). They are the start checksums and the copy of version 1's note; the record's start list does not carry them.
- One claim row, K41c, was added to CLAIMS.md after the note's change (A1).
- The instruction's A8 names the trace check over `REPORT_NOTE_2026-10-31.md`; read with this version's paths, it is run over this report, `REPORT_NOTE_2026-10-31_v2.md`.
- The brief, outside the record's root, is named to `start` with `--read`, so that its read is on the start list (version 1's one finding).

## 6. What this round did not finish

Nothing of the task. The note is kept as a source and built; it is not sent (the owner's word of 22:52 Tallinn time).

## 7. The outputs, by path

`<E>/outputs.log` (21:22:32 UTC), each `ls -ld` with `exit 0`: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/NOTE.md`, `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/note` and its files `build.py` (unchanged), `NOTE.pdf`, `NOTE.html`, `register_exceptions.txt` (unchanged), `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-v2/_evidence`, and `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports`.
