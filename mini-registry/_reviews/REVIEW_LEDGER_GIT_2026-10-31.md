---
kind: review
reviews: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_LEDGER_GIT_2026-10-31.md
of_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_LEDGER_GIT_2026-10-31.md (C-2026-10-31-05)
written_by: a session that neither wrote nor carried out the instruction (MR · review · ledger under local git, started by sub-session)
model: claude-sonnet-5-5 — read from the line of this session's own context that names the model it is configured for
computer: MacBookPro — printed by `hostname` at 2026-10-31 14:19:41 UTC
window: 2026-10-31 14:19:41 UTC to 2026-10-31 14:21 UTC — opened at the first command (`date -u; hostname`), closed at this review's last write; no pause
verdict: accepted
downstream_artefact: the orchestrator's decision on C-2026-10-31-05; no ledger entry is written, the record being not cut over (the hand row, closed in WHAT_IS_RUNNING.md)
---

# REVIEW — the ledger under local git

Evidence: `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-ledger-git-review/_evidence/` — `review_A.log` (A1-A3, commit listing), `review_B.log` (checksums, blobs, README, config), `review_C.log` (mechanical checks, times, scope). Kind of work: `none`, so no page of the kind and no application to run.

## 1. The tests of success, one by one

Verdict: **accepted**. Gaps: 0 (by kind: none).

| Test | Met | Evidence read here (not the report's) |
|---|---|---|
| A1 step 0 | met | `review_A.log` 14:20:13: toplevel prints `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination`; `ls-files _ledger/README.md` prints `_ledger/README.md`; `remote -v` and `remote` print nothing. |
| A2 every entry committed | met | `review_A.log`: tracked `.yaml` under `_ledger` 7, on disk 7. |
| A3 nothing left over | met | `status --porcelain` empty; `--ignored` prints only `!! MEASURES.md` and `!! WHO.html`; `check-ignore -v` ties them to `.gitignore` lines 1 and 2; `.gitignore` is those two lines, 21 bytes, sha256 `941c16ca…5fb8` (as the report). |
| A4 no entry changed | met | `review_B.log`: my sha256 of all 11 files in `_ledger/` (7) and `_guards/` (4) equals `before.sha256` line for line (diff exit 0) and equals `after.sha256` with the README added (diff exit 0). All 15 committed blobs equal the disk files (`same` x15); `git diff --stat HEAD` prints nothing. The one added line is `_ledger/README.md`, which is not an entry and which the report names. No git attribute file, no autocrlf/eol/filter setting (`review_B.log` config). |
| A5 ledger reads | met | `review_C.log`: `ledger.py check` exit 1, one defect line, `not-cut-over: MR …`, `check: 1 defect`. |
| A6 trace check | met | `review_C.log` 14:20:42: `outputs: 5 of 5 named exist`, `trace check: clean`, exit 0. |
| A7 row taken up and closed | met | The work session's row is in the Closed table of `WHAT_IS_RUNNING.md`: Started 14:16 UTC, Closed 14:19 UTC, one line of what came of it and a **Moved** line; no Open row remains for it. The report window (14:16:49 to 14:19:13) agrees with the evidence stamps (first `step1_before.log` 14:17:21 local-to-UTC, last `window.out` 14:19:13) and with the report's mtime 16:19:13 +0200 = 14:19:13 UTC. |

## 2. One figure re-established

The number of ledger entries committed. Report's route: `git ls-files _ledger | grep -c '\.yaml$'` against `ls _ledger/*.yaml` (A2), 7 = 7. Route here: `git show --stat HEAD` read by eye (7 `_ledger/…yaml` rows, 4 `_guards` rows, `_ledger/README.md`, `.gitignore`, `CONSTANTS.md`, `projects.txt` = **15 files**, 192 insertions), and `git ls-tree -r --name-only HEAD | wc -l` = 15. Entries: 7, against the report's 7; files: 15, against the report's 15. They agree. Counts and times in the report's own words, read at source: one commit only (`git log --all`), `f30bc0451cbd52f947832c417af6c64ec8375b8a`, 16:17:46 +0200 = 14:17:46 UTC; identity `Arne Laponin <arne.laponin@gmail.com>` from `~/.gitconfig` (none set in the repository); message in one line as the task asks; `_ledger/` still holds 7 entries now at 14:20, so none appeared after the commit either.

## 3. The outputs exist

`review_A.log` and `review_B.log`: `.git/` exists with one commit and no remote; `.gitignore` 21 bytes; `_ledger/README.md` 563 bytes, sha256 `bbae7c14…034d`, four sentences, naming the procedure's section 9 by the path the instruction gives; the evidence folder and the report exist (trace check). The report is now 9629 bytes, the `ls -ld` listing inside it (8267) was taken before its last write; see section 8.

## 4. Running application

Not applicable: the kind is `none` and the round wrote no application model.

## 5. Page of the kind

Not applicable: `kind_of_work` reads `none — the operations of the estate: putting the coordination's ledger under version control`; there is no page and no program of the kind.

## 6. The four mechanical checks

- Trace check over the report: run, exit 0, clean (`review_C.log`).
- Placement check over the instruction under review: run, exit 0, clean; the `.git`, `.gitignore`, README and evidence folder are "not judged" (of none of the three kinds, or folders).
- Check of the round's record: **not run, there is none** — the instruction's section 5 rules that the round keeps no `round_record.py` record, and the report's `record` line says so.
- Ledger: `ledger.py show --code MR --id C-2026-10-31-05` exits 1, `no entry` — expected, the round wrote no `issued`, `started` or `finished` entry because the record is not cut over; the criterion is judged on the hand rows (A7, met). `ledger.py check` exit 1 on `not-cut-over: MR` alone, the declared defect. No account to compare against the declaration, since no entry exists.

## 7. Verdict

**Accepted.** A1 to A7 are met on evidence read here; the count of entries is re-established by another route; no checksum in `_ledger/` or `_guards/` differs from the round's `before.sha256`, and every committed blob equals its disk file. Gaps: 0. Count by kind: none. With no ledger entry written, the orchestrator closes the matter by hand in the record.

## 8. Found, not fixed

1. The report names itself `claude-opus-5-5`; the instruction's model line names Sonnet. The report says so itself (its section 5); recorded here as the form asks. This review ran on `claude-sonnet-5-5`, as named.
2. `_coordination/CONSTANTS.md` section 5 ("written by `ledger.py` and by nothing else") and the README's second sentence do not hold of the README, which was written by hand as the instruction demanded. `ledger.py check` accepts it. The wording is the orchestrator's to narrow; the report found the same.
3. The `ls -ld` listing inside the report shows itself at 8267 bytes; the file is 9629 bytes at the close of the round. A report cannot list its own final size; harmless, the trace check only needs it to exist.
4. The commit's dates are in +0200 local time, against the UTC of the ledger's entries (the report notes it).
5. The ledger holds no `issued` entry for C-2026-10-31-05, so the trace check compared no input checksum. Expected until the cut-over.
6. `_coordination` was a git repository nowhere before this round and now carries a history on this computer only, by D-2026-10-31-01; nothing is yet backed up off the machine. `CONSTANTS.md`'s line on keeping the ledger by git stays `no` (a repository with a remote), as the instruction ruled out of scope.
7. The mini registry's own repository still has uncommitted and untracked files (this round's evidence, report and row among them); out of scope for both rounds.
