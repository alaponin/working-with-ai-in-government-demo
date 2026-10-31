---
kind: report
answers: C-2026-10-31-11
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_QUESTIONS_2026-10-31.md
written_by: a working session (MR · work · answers to the groundwork's questions), separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt is the start message delivered by a scheduled task; it does not show who typed or pasted it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname`, the round's first command, at 15:21:40 UTC, just before its started entry
window: 2026-10-31 15:21:48 UTC to 2026-10-31 15:30:29 UTC, no pause; closed at the last write of the 18 files the round names as written, REPORT_QUESTIONS_2026-10-31.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md 18410 bytes sha256 0bbc89264c1a0ee5f837e71aa3f1dbb03abb5ee10487c118aa3173f2ce4ae6cb · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/ · this file
ledger: MR C-2026-10-31-11 — the started entry is 20261031T152148Z_MR_started_C-2026-10-31-11.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write a short paper that recommends an answer to each of the groundwork's 14 open questions, for the owner's ruling

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md` (`C-2026-10-31-11`) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`, every program with `/usr/bin/python3` (3.9.6)

## 1. The answer first

`docs/QUESTIONS-PAPER.md` (18410 bytes) recommends one answer to each of the groundwork's 14 questions, as proposals: ages on 2026-10-31; the reset in the brief's order of lists, then entry number; seed 20261031; first learner number 1; the 8 over all three pairs of lists, each of the 4 spelt differently on the later list; 24, 22 and 22 entries; 20 children per school; the 4 differing in the family name alone; a school on every list; dates as YYYY-MM-DD on every list; a key table of all 68 entries; a table `list_entry, learner_number` written by the reset; a setting of 64 learners after reset; and "share" read with capitals ignored. The toy program built to all 14 together yields 60 children, 3 schools, 68 entries, 8 children on more than one list, 4 of them spelt differently, ages 6 to 12, 64 learners after reset, and 4 of the 8 caught by the brief's rule. No recommendation widens the search or lets it read the key table (A6). A1 to A9 are met, and A10 rests on `check.out`; its first run found `end.out` unnamed here, and it is now named. A11 stands for the `started` entry, and the `finished` entry follows this report.

## 2. The criteria, one by one

### A1 — the 14 questions listed — met

`list_questions.py` ran through `round_record.py run` at 15:25:56 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A1_questions.log`:

```
14
0 not found
EXIT=0
```

The list is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/QUESTIONS.md`, `GROUNDWORK.md` lines 43 to 56.

### A2, A3, A4 — sections, passages, positions — met

`check_paper.py` ran through `run` at 15:28:37 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A2_A3_A4_check.log`:

```
A2: 0 unanswered, 0 extra
A3: 0 not found, 0 wrong line
A4: sections not reading 2, 1, 1: 0
A4: table rows 26: both meet 15, divides 11, unmarked 0
```

A3 read 45 quoted passages in 7 files and the 14 quoted questions. A4 prints `2 1 1` for each of Q-1 to Q-14 in the same log. Every table row is marked `both meet` or `divides`.

### A5 — taken together — met

`taken_together.py` ran through `run` at 15:26:41 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A5_taken_together.log`:

```
children (child keys in the key table): 60
schools named on the lists: 3
entries: 68; per list in order: [24, 22, 22]
children on more than one list: 8
of those spelt differently, letter for letter heeding capitals: 4; capitals ignored: 4
ages: 6 to 12
learners after reset: 64; highest learner number 64; learners without a school 0
searches finding more than one: 0
of the 8, caught by the rule (both entries in one learner): 4
```

The learners after reset are 64, and the rule catches 4 of the 8. The program was written from the recommendations and was run once. It was not adjusted to reach these numbers.

### A6 — what each recommendation touches in the search rule or the key table — met

| Q | Touches |
|---|---|
| 1 | none |
| 2 | search rule, `at_reset`: gives the "fixed order"; nothing compared or forgiven changes |
| 3 | none |
| 4 | search rule, `on_none`: the first number the setting `learner_number` gives |
| 5 | key table: which entries it pairs; the search rule none |
| 6 | none |
| 7 | none |
| 8 | none: it fixes the data, not the comparison |
| 9 | search rule, `does_not_compare` school: a school on every list, still never compared |
| 10 | none: the form of the date is the clerk's form, so no step is added before the comparison |
| 11 | key table: names its entries and children and holds all 68; the search does not read it |
| 12 | search rule, `at_reset`: writes one row after each search; the search reads neither that row nor the key table |
| 13 | none: a setting the counts check |
| 14 | none: it fixes the data under the rule's own capitals |

No recommendation adds a compared field, forgives anything but capitals, or gives the search the key table.

### A7 — under 20 KB — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A7_size.log`:

```
   18410 docs/QUESTIONS-PAPER.md
```

### A8 — the sources unchanged — met

`before.sha256` was taken at 15:25:39 UTC, just after `start`. `after.sha256` was taken at 15:28:53 UTC. Their diff is empty. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A8_sources.log`:

```
EXIT=0
ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64  brief/MINI-REGISTRY-BRIEF.md
ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103  mini-registry/docs/REQUIREMENTS.md
d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb  mini-registry/docs/GAPS-PAPER.md
5ed9b62f282d433df7c337a2da30e4830c56170dca1e646ae5aacc2cc2795dce  mini-registry/docs/GROUNDWORK.md
```

The three CSVs of the groundwork are also unchanged, in the same log. The first three checksums are those of section 2.

### A9 — placement and trace checks, outside `run` — met

Both ran at 15:29:53 UTC, after this report was written, outside `run`. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A9_placement.out`:

```
placement check: clean
EXIT=0
```

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/A9_trace.out`:

```
trace check: clean
EXIT=0
```

### A10 — the record check — met where `check.out` exits 0

`RECORD.txt` (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record/RECORD.txt`) lists 3 runs, 12 files read and `## 4. Findings — 0`. The check is the last act before the `finished` entry, and its output is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record/check.out`.

**Written after `end`**, and so not on the record's lists: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/end.out` (the output of `end` itself, empty, closed at 15:28:54 UTC), `ls_ld.out`, `A9_placement.out`, `A9_trace.out`, `window.out`, `check.out` and this report.

### A11 — the ledger entries — the started entry stands

The `started` entry is `20261031T152148Z_MR_started_C-2026-10-31-11.yaml`, exit 0, account `arne.laponin@gmail.com`, started-by `unknown`. The `finished` entry is written after this report, so the review runs `show`.

## 3. Found, not fixed

- The Open block of `WHAT_IS_RUNNING.md` gives this task's files as `~/IdeaProjects/mini-registry/…`, while the estate's root is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry`. The two earlier reviews note the same.
- `settings.csv` holds no setting for the learners after reset, and `lists.csv` holds no school field on any list and no entry number. If the owner rules on Q-9, Q-11, Q-12 and Q-13, the groundwork needs rows it does not have now.

## 4. What I could not establish

- A11 for the `finished` entry: it is written after this report.

## 5. Corrections to the instruction

- After the paper was first written, and before any check ran, it was edited once, at 15:28:09 UTC, by an inline `/usr/bin/python3 -` heredoc that was not run through `run`. It changed two strings: the Q-9 rival's cell, from "34" to "40 of 64", and Q-2's dependency line, which gained Q-14. The 40 is 64 learners less the 24 census entries enrolled first. `RECORD.txt` lists the paper as "written by no traced run". Every check ran after that edit.
- `start.out` was first written to `/tmp` on the computer and then moved into the evidence folder, because the record's folder did not yet exist.
- The effort is written `unknown`, and started-by `unknown`, as section 1 requires for a scheduled start.

## 6. What this round did not finish

Nothing of the instruction is left. The 14 recommendations wait for the owner's ruling.

## 7. The outputs, by path

Each place the round wrote in, listed at 15:28:59 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/ls_ld.out`:

```
drwxr-xr-x@ 8 arnelaponin  staff  256 Oct 31 17:28 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs
exit 0
drwxr-xr-x@ 17 arnelaponin  staff  544 Oct 31 17:28 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence
exit 0
drwxr-xr-x@ 8 arnelaponin  staff  256 Oct 31 17:28 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions/_evidence/record
exit 0
drwxr-xr-x@ 11 arnelaponin  staff  352 Oct 31 17:14 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports
exit 0
```

Nothing was opened on the owner's screen, and nothing was committed.
