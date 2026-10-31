---
kind: instruction
commission_id: C-2026-10-31-27
version: 1
session_name: MR · work · the pages against the kind item
kind_of_work: none — the method's own work in this estate: amending a page of a kind of work for a kind of gap that recurs
upstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_QUESTIONS_2026-10-31.md
inputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_QUESTIONS_2026-10-31_v2.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reviews/REVIEW_COMMIT3_2026-10-31.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COMMIT3_2026-10-31.md · /Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md
downstream_artefact: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31.md
serves: the working prototype, deliverable 1 of the constants — the ledger's check names the kind item recurring in three reviews of MR (the setting ledger.recurring_kind, 3), and the procedure, section 3, has a task amend the page of the kind of work for it
answers_kind: item — the kind ledger.py check names recurring in MR C-2026-10-31-12 versions 1 and 2 and MR C-2026-10-31-24 version 1
model: Sonnet — the content is the three reviews' own gaps; what remains is writing each as one line of the page it belongs to, which a reviewer can check line by line
effort: medium — three gaps, one page, a few lines
reviewer: a separate session started from the review instruction below, as a sub-agent of this session; Sonnet, effort medium — the review reads each gap against the line written for it
review_instruction: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_KIND_ITEM_2026-10-31.md
waits_for: C-2026-10-31-23 — the third commit of the day accepted first, since it stages every file
outputs: /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item/_evidence/ · /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31.md
running_record: MR — the issued entry is written in the ledger by ledger.py from this declaration, once this file is complete and before the start message is handed over
---

## The start message

```text
MR · work · the pages against the kind item
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_KIND_ITEM_2026-10-31.md
```

---

# INSTRUCTION — Amend the page of the kind of work for the three gaps of the kind item that the ledger names recurring

**Suggested model: Sonnet, effort medium.** The reviews settle the content; a reviewer checks each line against its gap.

## 1. Role and where to run

You are a working session for the mini registry, started under the name `MR · work · the pages against the kind item`. You run on the owner's Mac through Desktop Commander's `start_process` (zsh) and its file tools: load them with ToolSearch by their full names, `select:mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__start_process,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__read_file,mcp__remote-devices__plugin_8d52a3a6-3a2d-4a54-8d1d-e08585a97642_desktop-commander__write_file`, or by function where that name is absent; prove the shell with `date -u; hostname`. Run the layer's programs with `/usr/bin/python3`.

**Your first act** is this task's `started` entry:

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" started --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-27 --session "MR · work · the pages against the kind item" --shell native --instruction /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_KIND_ITEM_2026-10-31.md --effort unknown --started-by <owner where the owner typed or pasted your start message; otherwise unknown> --account <the address your own context names as the user's address, or unknown> --by "MR · work · the pages against the kind item"
```

A session that can tell only that a scheduled task started it writes `unknown`. Where it refuses because the task waits, write nothing and stop, quoting what it printed.

## 2. Read first

The procedure, `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md`, section 3 (the setting `ledger.recurring_kind`) and section 6.4; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/FINDING-KINDS.md`; the three reviews in the declaration's `upstream_artefact` and `inputs`, section 7 of each; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md` as it stands, its items 6 and 7 added today from two of these reviews; `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_COMMIT3_2026-10-31.md`, its section "Version 2"; `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/references/REPORT-template.md`.

## 3. The task

1. **List the three gaps** into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item/_evidence/GAPS.md`, each quoted from its review with its path and line: G1 of `REVIEW_QUESTIONS_2026-10-31.md`, G1 of `REVIEW_QUESTIONS_2026-10-31_v2.md`, and G1 and G2 of `REVIEW_COMMIT3_2026-10-31.md`.
2. **For each, say which page it belongs to and what the page already says.** The two analysis gaps belong to `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`: say for each whether items 6 and 7 of its part 1 already carry it, quoting them. The commit gaps came from an instruction of the kind `none`, which has no page; their cure is in the instruction's version 2 — quote it — and they are listed, not written into a page.
3. **Amend `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_kinds/analysis.md`** only where a gap is not yet carried. Where the page refuses a fault in its part 1 but nothing in its part 3 makes the orchestrator check for it before issuing, add one line to part 3 — for these gaps: that an instruction whose questions depend on one another asks for every dependency listed both ways and every rival judged under the other questions' recommendations, with a run that builds each rival beside them. Each line added ends with the reviews it comes from, in italics, as items 6 and 7 do. Change no other line.

## 4. Constraints

Write nothing but the outputs named. No operation that writes to version control; nothing opens a window. No figure from memory.

## 5. Acceptance criteria

- **A1** — `GAPS.md` holds the four gaps, each quoted from its review at the line it gives; a command shows each quotation is in its file → `0 not found`.
- **A2** — The report names, for each gap, the page line that carries it — an item already there, a line added, or "no page: the instruction's version 2" — each quoted.
- **A3** — `diff` of `_kinds/analysis.md` before and after shows only added lines, each ending with its source reviews.
- **A4** — The trace check over the report exits 0: `/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/trace_check.py" --constants /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/CONSTANTS.md --coordination /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31.md`.
- **A5** — The `started` and `finished` entries stand, as `ledger.py show --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-27` prints them beside the `issued` entry, which carries `answers_kind: item`.

The round keeps no `round_record.py` record: its one write is the page, which A3's `diff` proves. The report's `record` line says so.

## 6. Evidence, the report, and the review

Evidence under `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-kind-item/_evidence/`, each command with its output and time. Write the report from the report form, with `upstream_artefact` **this file's path** and `answers` `C-2026-10-31-27`; do not write the verdict. **Then the `finished` entry:**

```text
/usr/bin/python3 "/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts/ledger.py" finished --constants /Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md --code MR --id C-2026-10-31-27 --report /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_reports/REPORT_KIND_ITEM_2026-10-31.md --outcome "<one line: what the page now carries>" --moved "<_kinds/analysis.md amended, or nothing>" --account <the same account as your started entry> --by "MR · work · the pages against the kind item"
```

Once it stands, start the review as a sub-agent with your Agent tool: `subagent_type` `general-purpose`, never a fork, in the foreground; where the tool takes a model and an effort, Sonnet and medium, never lower; `prompt` these three lines, word for word:

```text
MR · review · the pages against the kind item
Carry out the instruction at /Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_prompts/PROMPT_REVIEW_KIND_ITEM_2026-10-31.md
Load the shell tool this session has for commands on the computer (desktop-commander where it is present).
```

Never create a scheduled task to start it. Wait for it, and end with one line: its verdict line and its path, or why it could not run.
