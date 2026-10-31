---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_NOTE_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_NOTE_2026-10-31.md (C-2026-10-31-31, version 1)
written_by: a session that neither wrote nor carried out the instruction — "MR · review · the note to the Permanent Secretary", started as a sub-agent from the start message of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_NOTE_2026-10-31.md (C-2026-10-31-32), with an empty memory, separate from the working session and from the orchestrator
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for; the band the review instruction names, Opus
computer: MacBookPro — printed by `hostname` on the computer the session runs on, the session's first command
window: 2026-10-31 20:55:55 UTC to 2026-10-31 21:05 UTC, no pause — opened at this task's started entry 20261031T205555Z_MR_started_C-2026-10-31-32.yaml; closed at the moment of writing
verdict: not accepted
downstream_artefact: the next version of /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_NOTE_2026-10-31.md, to which the orchestrator appends G1
---

# REVIEW — Round 8, the note to the Permanent Secretary

**The note is right in what it says: every claim of it stands at a source of the record, the register check is clean but for the Ministry's own name, the PDF is one A4 page, and "the search catches 4 of the 8" holds again by two routes of the reviewer's own. It is not accepted on one gap: the record names a limit that is neither in the note nor in the report's list of what was left out — no length and no character refused in a name, the other half of the ruled sentence whose first half the note states (G1).**

Evidence of this review: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note-review/_evidence/` (cited as `<E>/`); the round's own evidence `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-08-note/_evidence/` (cited as `<W>/`). Nothing of the round was changed or rebuilt here.

## 1. The tests of success, one by one

| Test | Verdict | Evidence read or produced here |
|---|---|---|
| A1 — CLAIMS.md before the note; every claim at its source; each sentence paired | met | `<E>/R5_counts.log`: CLAIMS.md `20:45:59Z`, LIMITS.md `20:46:37Z`, NOTE.md `20:46:48Z`. The reviewer's own program over every row, splitting on spaced bars so that a bar inside the words is kept (`<E>/r1_claims_at_source.py`, `<E>/R1_claims_at_source.log`): `== CLAIM rows: 52`, every row `found`, `not found: 0`, each cited line printed in full and read against the note's sentence (section 5). PAIRS.md 34 rows; the round's A1 log `note: 34 sentences; pairs: 34 rows; unpaired 0`. One row carries its fact only weakly (K32, section 8); the fact itself stands in the record. |
| A2 — every limit the sources name, in the note or left out with its reason → `0 unaccounted` | **not met** | The reviewer's own list from the same record (`<E>/R6_limits_relisted.md`): 21 limits; 20 match L01–L20; **1 missing** — `docs/GOAL-QUESTIONS-PAPER.md:115` «We recommend no length and no character refused, and Position A: spaces only are an entry missing.», ruled by D-2026-10-31-07 («Rule all 13 as recommended», its line 8). `grep -n -i -E "no length|longest|character refused|characters refused|any character"` over NOTE.md, LIMITS.md, CLAIMS.md, PAIRS.md and the report: `grep exit 1 (1 = no line found)` (`<E>/R6_limits_grep.log`). G1. |
| A3 — the register's self-test, then the check | met | Run here (`<E>/R3_register.log`): `cases: 10, failed: 0`, `SELFTEST EXIT=0`; over NOTE.md without exceptions `line 3 [the name of a program, skill or plugin] «Skills»`, `exit 1`; with `docs/note/register_exceptions.txt` `refused: 0 … excepted by name: 1`, `CHECK (with exceptions) EXIT=0`; over the PDF's text extracted here, the same, `EXIT=0`. The exception is in the build folder with its reason and repeated in the report (its A3). |
| A4 — one page, A4, 595 by 842 | met | Section 2. |
| A5 — R-23's test from the PDF's text | met | The text extracted here by Ghostscript (`<E>/R2b_pdf_text.log`, `<E>/note_text.gs.txt`): one page; line 2 `To the Permanent Secretary, Ministry of Education, Youth and Skills`; line 3 `The prototype shows that a school clerk can enrol a child in a single list of learners…`; line 5 `…It does not show that the registry recognises the same child when the family name is`; heading `What the prototype does not show`. |
| A6 — two builds give the same text | met | Not rebuilt here (change nothing). `<E>/R5_counts.log`: `text.build1.txt` and `text.build2.txt` `cmp` equal, both sha256 `da5b4083…0492`; build 2's text and the Ghostscript text of the PDF now: `643` words each, `same: True`; `<W>/A6_build_twice.log`: `BUILD1 EXIT=0`, `BUILD2 EXIT=0`, `smallest_type_pt=11.00`, `windows added: 0`. |
| A7 — sources unchanged | met | Run here: the round's `sources.start.sha256` (its first line a stamp) by `shasum -a 256 -c`: 15 `OK`, `SHASUM -c EXIT=0` (`<E>/R5b_sources.log`); `src/` against `src.start.sha256`: `src files: 24, changed or unreadable: 0` (`<E>/R5_counts.log`). |
| A8 — placement and trace checks exit 0 | met | Run here, section 6: `placement exit 0`, `trace exit 0`. |
| A9 — started and finished beside issued | met | Section 6: `issued` 20:38:12Z, `started` 20:41:00Z, `finished` 20:55:34Z. |

## 2. One figure re-established

- **"The search catches 4 of the 8."** The round's route: round 7's counting program, carried as `docs/DUPLICATES.md:5`. Here, from `docs/count/duplicates.csv` by the reviewer's own commands (`<E>/r2_figure.sh`, `<E>/R2_figure.log`): Python's `csv` module, the caught column `4 ['C19', 'C26', 'C31', 'C53']`, and independently the rows whose two learner numbers are one, `4` — the same four; the missed four differ in `family_name` only, `4`; `awk: caught 4 of 8`. **Agrees.**
- **The page count of NOTE.pdf.** The round's route: PDFKit through `osascript`. Here, three other routes, none opening a window (`<E>/R2_figure.log`): Spotlight `kMDItemNumberOfPages = 1`; Ghostscript's bbox device, `1` page box; the file's bytes, `page objects: 1`, `/Pages /Count: ['1']`, `MediaBox: ['0 0 595 842']`. **Agrees: one A4 page.** The words of NOTE.md and of the PDF's text: `643` and `643`, `same sequence: True`.
- **Times and counts the report gives in words**, read at their source (`<E>/R5_counts.log`): the window's close, 20:54:58, is the report's mtime by `stat` (`2026-10-31T20:54:58Z`) and `window.out` line 7 (`files the round names as written: 36`); `runs.jsonl` 17 lines (13 exit 0, 3 exit 1, 1 exit 2 — "record runs 6 and 8, exit 1" and "runs 2 and 4, exits 1 and 2" fit); windows `252` before and `252` after, the two lists byte for byte the same; 15 sources, 24 files of `src/`. **Agree.**

## 3. The outputs exist

`<E>/R5_counts.log` (21:02:29 UTC), each `found` at the size and sha256 the report's `outputs` line gives: NOTE.md `3542 19a7dba5…b277`; build.py `6561 1f3d3144…9549`; NOTE.pdf `57094 6ff1a6b8…5666`; NOTE.html `4226 fea63b9a…7799`; register_exceptions.txt `252 75c94433…680e`; the evidence folder, 33 files; the report, 16001 bytes.

## 4. The running application

Not applicable: the round wrote a document and its build, no application model.

## 5. What a review of drafting runs (the drafting page, part 2)

**Every claim looked up at its source, against the sentence that states it.** Each of the 52 rows' cited line was printed in full (`<E>/R1_claims_at_source.log`) and read against the note's sentence the row is paired with, not only for the shared words. Every fact the note states is carried by the record. Two readings that do not change that: K32 rests the sentence «no system of the census, the examinations authority or the social grant programme is linked to it» on brief:34's «Other bodies, if the project needs them, are simulated.», which carries simulation, not the absence of a link; the absence is carried by the same line's first sentence (K16a, «Connect to anything outside your computer.» under "must not") and by `docs/GAPS-PAPER.md:36` «None: the three lists are data inside the prototype, not bodies it connects to» (`<E>/R6_limits_grep.log`). The note's claim stands; the row is the page's item 5 at the level of the list (section 8). K07's «agree what the registry is to do» elaborates brief:7's «for agreement» without adding a fact.

**The limits listed again from the record and compared row by row.** `<E>/R6_limits_relisted.md`: 21 listed from the seven sources the instruction names; 12 in the note, 8 in the report's left-out list with reasons, **1 missing** (M12, G1). LIMITS.md holds no row outside this list. The left-out reasons were read: each is a reason, and none says the note states what it does not, but L16's «which the record carries (0 added at every reading)» rests the note's «none of them opens a window» on readings at intervals; the accepted build review's A6 «nothing connects, nothing opens | met» carries it, so it is not a gap.

**The note read for internal words and codes.** No path, file name, identifier, requirement or failure code, round or date; the register check refuses nothing but the excepted «Skills» (section 1, A3). «the search step», «learner number», «capital letters aside» are the reader's words. «catches» is the brief's own word for the figure and is explained in the same sentence («as one child»); not refused by the check.

**The faults of the page, part 1, read against the report.** Item 1: no fact supplied beyond the record (above). Item 2: not engaged — no earlier gap. Item 3: met. **Item 4: broken by G1** — «Every limit that an accepted document names is either in the draft or in the report's list of what was left out, with the reason.» The limit of one step is stated as of that step («This is a limit of the search step as it is defined»). Item 5: one row weak (K32), the fact carried elsewhere.

## 6. The four mechanical checks, run by the reviewer

All in `<E>/R4_mechanical.log` (21:01:01–21:01:03 UTC), by `<E>/r4_mech.sh`, run directly:

- **Trace** over the report: `inputs: 10 of 10 pinned by 20261031T203812Z_MR_issued_C-2026-10-31-31.yaml hash the same now`, `trace check: clean`, `trace exit 0`.
- **Placement** over the instruction: `placement check: clean`, `placement exit 0`.
- **Record check**, with the options `check.out` prints on `# run with:` (`--record …/round-08-note/_evidence/record --report …REPORT_NOTE_2026-10-31.md --tolerance 2`) and `--out <E>/record_check.out`: `## Findings — 1`, `read, not on the start list (no checksum at the start): /Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`; `record check exit 1`. The report names it (its section 5) and A7 shows the brief unchanged. Reported, not a test. This review's own files appear only as "added after the window closed".
- **Ledger `show`** for C-2026-10-31-31 (`<E>/ledger_show.out`, `show exit 0`): `issued` 20:38:12Z, `started` 20:41:00Z (`started_by: unknown`, `effort: unknown`), `finished` 20:55:34Z. **Account:** `account: arne.laponin@gmail.com` on all three; the report's declaration names the same.
- **Ledger `check`** (`<E>/ledger_check.out`): `check exit 0`, `check: clean`; lines naming MR: `(none)`.

## 7. The verdict

**Not accepted — 1 gap.**

**G1 (item)** — fails A2, and breaks the drafting page's part 1, item 4: «Every limit that an accepted document names is either in the draft or in the report's list of what was left out, with the reason.» The ruled questions paper names, at `docs/GOAL-QUESTIONS-PAPER.md:115`, «We recommend no length and no character refused, and Position A: spaces only are an entry missing.», ruled whole by D-2026-10-31-07, line 8, «Rule all 13 as recommended». The second half of that sentence is in the note («An entry of blank characters of any kind, not only spaces, is treated as missing»); the first — a name of any length and of any characters is accepted and saved — is in no row of LIMITS.md, not in the note, and not in the report's list of what was left out. The round listed its sibling of the same kind, L13, «6 to 12 holds the data, not the entry» (line 77), and gave its reason; this one it did not list, so A2's `0 unaccounted` was counted over a set short by one. The Permanent Secretary reads that the prototype refuses a detail missing, a date naming no day and a fourth school, and is not told that it refuses nothing a name holds. The next version either states it in the note or names it in the report's left-out list with its reason, and lists the set again from the seven sources, saying how many still fail.

**The page of the kind:** G1 is a fault its item 4 already carries; the page lacks none.

## 8. Found, not fixed

- **K32 cites a shared word** (the page's item 5): brief:34's «Other bodies … are simulated» for «no system … is linked to it». The fact is carried by brief:34's first sentence and by `docs/GAPS-PAPER.md:36` (G-11), which the instruction's named record does not include.
- **A school other than the three** reaches the registry only when sent around the screen: `docs/GOAL-QUESTIONS-PAPER.md:142` «SC-1 offers the 3 alone under both positions», `:144` «as a windowless check can send it». The note says such a school is refused and «is not shown again when the clerk returns to correct the entry» without saying the clerk's screen offers only the three; a reader may take the limit as larger than it is.
- **«Progressa is fictional»** is said to the Permanent Secretary, whom the constants (section 4) place inside Progressa's story. It is the screens' own line and carried by the record; for the owner.
- **A limit of an accepted document outside the named record:** `_reviews/REVIEW_DATA_2026-10-31.md:125` — all 60 children have different family names, so «round 6 has no list case where the search must tell such children apart by given names or date». Not in the instruction's section 2, item 5, so not counted; for the orchestrator.
- **The ledger split a path holding spaces:** the `issued` and `started` entries of C-2026-10-31-31 pin the input `/Users/arnelaponin/Library/Application absent` (`<W>/A9_ledger_show.log`) — the register's path, cut at its first space; the register was never pinned, and the trace check counts it among `10 of 10 … hash the same`. A fault of the kit, not the round.
- **The report's A8 and A9** cite their logs without quoting their results; the logs hold `placement exit 0`, `trace exit 0` and the three entries. The round's A8, A9 and `check.out` were written after its window closed, as the report says.
- **Model:** claude-opus-5-5, the band named. Effort `unknown` in this task's started entry, as no prompt showed it.
