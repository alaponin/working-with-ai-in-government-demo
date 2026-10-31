---
kind: report
answers: C-2026-10-31-11
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_QUESTIONS_2026-10-31_v2.md
written_by: a working session (MR · work · answers to the groundwork's questions), separate from the session that wrote the instruction
account: arne.laponin@gmail.com — read from the line of this session's own context that begins "The user's email address is"
started_by: unknown — this session's prompt is the start message delivered by a scheduled task; it does not show who typed or pasted it
model: claude-opus-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname` at 15:46:58 UTC, the round's first command, just before its started entry
window: 2026-10-31 15:47:05 UTC to 2026-10-31 15:58:34 UTC, no pause; closed at the last write of the 24 files the round names as written, REPORT_QUESTIONS_2026-10-31_v2.md, read by stat; printed by round_record.py window, its command and output kept in /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/record/window.out
record: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/record — kept by round_record.py; its RECORD.txt is the list of what the round read and changed, and check.out is the round's last run of its check
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/QUESTIONS-PAPER.md 19962 bytes sha256 5146d23a87cf9c0527c26c2965725bfa1125bd1a0a103ac83b68fb7dbd50cce0 · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/ · this file
ledger: MR C-2026-10-31-11 — the started entry is 20261031T154705Z_MR_started_C-2026-10-31-11.yaml; the finished entry follows this report and names this file
---

# ACCOUNT — Write a short paper that recommends an answer to each of the groundwork's 14 open questions, for the owner's ruling (version 2)

**Answers:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_QUESTIONS_2026-10-31.md` (`C-2026-10-31-11`, version 2) · **Run on:** MacBookPro, zsh through Desktop Commander's `start_process`, every program with `/usr/bin/python3`

## 1. The answer first

`docs/QUESTIONS-PAPER.md` was changed in place (19962 bytes) and keeps the 14 recommendations of version 1. Each section now declares what it depends on and what depends on it. The 15 dependent pairs are in `DEPENDENCIES.csv`, and none is declared one-way. Every position is judged under the recommended answer of every question it depends on. A new program builds each rival with all the other recommendations. Two rivals cannot be built that way, and their tables now say so. Q-6's rival (60, 4, 4) needs Q-5's rival. Q-9's rival, now at its strongest (a school on the census only, with the reset supplying one to every other learner), cannot carry Q-7's 20 per school for the 36 children who have no school on any list. The recommendations taken together yield 60 children, 3 schools, 68 entries, 8 on more than one list, 4 of them spelt differently, ages 6 to 12, and 64 learners after reset, and the brief's rule catches 4 of the 8. A1 to A10 and A12 to A14 are met. For A11, the `started` entry stands, and the `finished` entry follows this report.

## 2. The criteria, one by one

The evidence folder is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/`. Each log opens with the time it was written.

### A1 — the 14 questions listed — met

`list_questions.py` ran through `run` at 15:53:07 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A1_questions.log`:

```
14
0 not found
EXIT=0
```

### A2, A3, A4, A12, A13 — sections, passages, positions, dependencies, rivals — met

`check_paper.py` ran through `run` at 15:56:19 UTC, after the paper was built at 15:56:18. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A2_A3_A4_A12_A13_check.log`:

```
A2: 0 unanswered, 0 extra
A3: 0 not found, 0 wrong line
A4: sections not reading 2, 1, 1: 0
A4: table rows 23: both meet 14, divides 9, unmarked 0
A12: pairs in the table 15; declared in the paper 15; 0 one-way; 0 not in the table
A13: 0 disagreements
```

A3 read 33 quoted passages, the 14 quoted questions and 5 ranges, all inside their files. A4 prints `2 1 1` for each of Q-1 to Q-14. For A12, the table is `DEPENDENCIES.csv`, with each pair and why it holds, and the log has one line per pair. For A13, the log reads each section's row "(c) known numbers" against the verdict of `A13_rivals.log`.

### A5 — taken together — met

`toy.py together` ran through `run` at 15:53:08 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A5_taken_together.log`:

```
children: 60
schools: 3
entries: 68; per list in the order of line 19: [24, 22, 22]
children on more than one list: 8
of those spelt differently: 4 (capitals ignored: 4)
ages: 6 to 12
children per school: [20, 20, 20]
learners after reset: 64; highest learner number: 64; learners without a school: 0
searches finding more than one: 0
of the 8, caught by the brief's rule: 4
```

There are 64 learners after reset, and the rule catches 4 of the 8. The program was written from the recommendations and run once, with no adjustment.

### A13 — each rival with every other recommendation — met

`toy.py rivals` ran through `run` at 15:53:08 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A13_rivals.log`, the two rivals that cannot be met:

```
Q-6 rival (B: every child on the census, 60, 4 and 4), with every other recommendation: can be met: no
    entries still needed per list after the 8 are laid [54, -1, -1]
```

```
Q-9 rival (B: a school on the census only; the reset gives every other learner one), with every other recommendation: can be met: no
    children per school read from the lists [8, 7, 9], not [20, 20, 20] (36 children carry no school on the lists)
```

The other 12 print `can be met: yes`. The further runs in the same log support the figures the paper gives. Q-6 B with Q-5 B can be met. Q-14 B with one pair laid gives `learners after reset 63, against the setting 64`. Under Q-9 B, the reset supplies the school of 40 learners, and 36 children have no school on any list. All six orders of the lists give 64 learners and 4 caught. The paper and the program agree on all 14: `0 disagreements`.

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
| 10 | none: the lists' dates are in the clerk's form, so no step comes before the comparison |
| 11 | key table: names its entries and children and holds all 68; the search does not read it |
| 12 | search rule, `at_reset`: one row written after each search; the search reads neither it nor the key table |
| 13 | none: a setting the counts check |
| 14 | none: it fixes the data under the rule's own capitals |

### A7 — under 20 KB — met

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A7_size.log`:

```
   19962 docs/QUESTIONS-PAPER.md
```

That is under 20,000 bytes and under 20,480.

### A8 — the sources unchanged — met

`before.sha256` was taken at 15:48:48 UTC, just after `start`, and `after.sha256` at 15:56:33 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A8_sources.log`:

```
EXIT=0
ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64  brief/MINI-REGISTRY-BRIEF.md
ad583b3958fb5c5fdf6683b5c2487b6f0c425d66cebc7c46811e2e19af13f103  mini-registry/docs/REQUIREMENTS.md
d03db64c6e49a1b92467c1e6e19929c321964bd89f6cb715d15dd570f37bc8bb  mini-registry/docs/GAPS-PAPER.md
5ed9b62f282d433df7c337a2da30e4830c56170dca1e646ae5aacc2cc2795dce  mini-registry/docs/GROUNDWORK.md
```

The diff is empty. The three groundwork CSVs are also unchanged, in the same log. The first three checksums are those of section 2.

### A9 — placement and trace checks, outside `run` — met

Both ran directly at 15:58:07 UTC, after this report was written, the trace check over this version's report. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A9_placement.out`:

```
placement check: clean
EXIT=0
```

Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/A9_trace.out`:

```
trace check: clean
EXIT=0
```

### A10 — the record check — met where `check.out` exits 0

`RECORD.txt` (`/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/record/RECORD.txt`) lists 5 traced runs and `## 4. Findings — 0`. `check` runs last, before the `finished` entry, into `record/check.out`. Its first run, at 15:58:20 UTC, found one file unnamed here, kept as `record/check_first_run.out`: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/end.out`, the output of `end` itself, closed at 15:56:46 UTC, which is now named by its full path. Written after `end`, and so not on the record's lists: that `end.out`, `ls_ld.out`, `record/check_first_run.out`, `A9_placement.out`, `A9_trace.out`, `record/window.out`, `record/check.out` and this report.

### A11 — the ledger entries — the started entry stands

The started entry is `20261031T154705Z_MR_started_C-2026-10-31-11.yaml` (exit 0). The `finished` entry is written after this report.

### A14 — the review of version 1, answered item by item — met

| Item | What changed | Where in the new paper |
|---|---|---|
| G1 | Every section carries "Depends on" and "Depended on by". There are 15 pairs, listed in `DEPENDENCIES.csv`, and none is one-way (A12). Both positions are judged under the other recommendations, and the toy builds each rival with them (A13). Q-6 B's row now reads "no", and the section names Q-5's B as what it needs. Q-9 B is the other rival that cannot be built, and its section names Q-7. | lines 26, 44, 63, 81, 100, 119, 137, 155, 174, 193, 212, 231, 250, 269; Q-6 lines 125, 129; Q-9 line 184 |
| found 1 | "Given to every position" cites the register R-01 to R-23 (`docs/REQUIREMENTS.md:15-320`), all thirteen summary rows (`docs/GAPS-PAPER.md:26-38`) and every settings row (`settings.csv:2-18`), and quotes `GAPS-PAPER.md:196` whole. | lines 10, 11, 12 |
| found 2 | Q-9 names the questions its figures rest on: Q-2, Q-5, Q-6, Q-7 and Q-14. | line 174, and line 180 for the figures |
| found 3 | Q-6's recommendation says no more about line 19 than line 19 says. The passage is now quoted as met by both positions, and the recommendation rests on what can be built. | line 131 |
| found 7 | Q-9's rival is stated at its strongest: a school on the census only, and the reset supplies one to every other learner, so every learner holds one. It is judged on Q-7's spread and on the reset's four entries. | lines 180, 184 |

## 3. Found, not fixed

- The Open block of `WHAT_IS_RUNNING.md` gives this task's files under `~/IdeaProjects/mini-registry/…`, while the estate's root is `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` (also the review's item 8).
- `settings.csv` has no setting for the learners after reset. `lists.csv` has no school field on any list and no entry number. If the owner rules Q-9, Q-11, Q-12 and Q-13 as recommended, the groundwork needs rows it lacks now.
- The review's items 4 and 5 were not among the items taken up, but the rewrite changes both. Q-11's and Q-13's rows "(c)" now read "both meet", and Q-13 no longer names Q-8. Items 6 and 9 concern version 1's report and the review's own trace, and nothing changed for them.
- The toy lays Q-14's rival pair as two census-only children. Other layings were not tried.

## 4. What I could not establish

- A11 for the `finished` entry, which is written after this report.

## 5. Corrections to the instruction

- **The started entry carries `--started-by owner`.** It should read `unknown`, as this declaration reads: the prompt came from a scheduled task and shows no one typing it. The entry was written before this was noticed and is not rewritten.
- A9 and A10 are read with this version's paths: the report `REPORT_QUESTIONS_2026-10-31_v2.md` and the record under `round-02b-questions-v2`, as the version-2 section says.
- The evidence folder was made by `mkdir -p` in the same command as `start`, just before it.
- At 15:52:56 UTC the first try of the A1, A5 and A13 runs failed with exit 127. zsh did not split the command held in a variable, so no program ran. Its three logs were overwritten by the run at 15:53:07, and no log of the failed try is kept.

## 6. What this round did not finish

Nothing of the instruction is left. The 14 recommendations wait for the owner's ruling.

## 7. The outputs, by path

Each place the round wrote in, listed at 15:56:53 UTC. Log `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/ls_ld.out`:

```
drwxr-xr-x@ 8 arnelaponin  staff  256 Oct 31 17:56 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs
exit 0
drwxr-xr-x@ 23 arnelaponin  staff  736 Oct 31 17:56 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence
exit 0
drwxr-xr-x@ 8 arnelaponin  staff  256 Oct 31 17:56 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-02b-questions-v2/_evidence/record
exit 0
drwxr-xr-x@ 12 arnelaponin  staff  384 Oct 31 17:30 /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports
exit 0
```

Nothing was opened on the owner's screen, and nothing was committed.
