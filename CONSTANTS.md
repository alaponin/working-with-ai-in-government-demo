# CONSTANTS — the mini registry

**Amended only by a ruling.** Each amendment names the ruling that obliges it.

## 1. What this project is for

The project builds a small working prototype for the planning unit of Progressa's Ministry of Education, Youth and Skills (MoEYS): a school clerk enrols a learner, and the registry does not register the same child twice. The prototype is for agreement, not the registry itself. It is the toy prototype of Module 5 of Working with AI in Government, and its record is what that module teaches from.

## 2. What it delivers, and by when

| Deliverable | Owed by | The document that obliges it |
|---|---|---|
| the working prototype, on the owner's computer, with its checks passing | no date set: owed when round 8 of the brief is accepted | the brief, `../brief/MINI-REGISTRY-BRIEF.md`, "What it delivers", item 1 |
| a one-page note to the Permanent Secretary: what the prototype shows, and what it does not | no date set: owed when round 8 of the brief is accepted | the brief, `../brief/MINI-REGISTRY-BRIEF.md`, "What it delivers", item 2 |

## 3. The documents that govern it

By path, in order of precedence, highest first. A later document does not override an earlier one by
being later; it overrides it only where this order says so.

| # | Document | Path | What it governs |
|---|---|---|---|
| 1 | the brief for Module 5, the mini registry | `../brief/MINI-REGISTRY-BRIEF.md` | what the prototype is for, what it must and must not do, the made-up data in known numbers, what it delivers, and the rounds in order |
| 2 | the pages of the four kinds of work: analysis, drafting, building, checking | `_kinds/` | the faults a session of each kind refuses, what its review runs, and what is checked before an instruction of the kind is issued |
| 3 | the orchestrator procedure | `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/SKILL.md` | how the work is commissioned, carried out, reviewed and recorded |

## 4. Who it reports to

The owner, Arne Laponin, receives every deliverable and every decision paper. Inside Progressa's story, the head of MoEYS's planning unit receives the decision papers, and the Permanent Secretary receives the note.

## 5. Standing constraints and prohibitions

- No real person's data is held: all data is invented, and every screen says "Invented data, Progressa is fictional" (the brief, "What it must not do").
- Nothing connects to anything outside the owner's computer; another body the project needs is simulated (the brief, "What it must not do").
- Nothing opens a window on its own: every check of the screens runs without one (the brief, "What it must not do").
- No figure is stated from recollection: each is established, with the command that established it (the owner's word at inception).

## 6. The map of places

**The three kinds of document, one kind to a place.** These three rows are what the placement check
and the register of instructions read.

| Kind | Place | Prefix |
|---|---|---|
| instruction | `_prompts/` | `PROMPT_` |
| report | `_reports/` | `REPORT_` |
| review | `_reviews/` | `REVIEW_` |

**The three paths above are the defaults and a project may override any of them.** They are the same
three folders that govern a project before this file exists — section 6.1 of the procedure — so a
project that keeps them is writing down what was already true, and the rule and the record agree.
Where this file names a different path, that path governs from the moment it is written, and the
override is worth a line saying why. A project already under way records where each kind already
lives and nothing is moved to fit the table (section 8.3).

**Everything else this project produces**, one row per kind of thing the method names. For a project
already under way, this records where each kind **already** lives; nothing is moved to fit the table.

| Kind of thing | Where it lives | New, or already there |
|---|---|---|
| the pages of the four kinds of work, copied from `wai-demo/kinds/` so that their growth is kept in this project's history | `_kinds/` | new |
| the drafted documents: the register of requirements, the groundwork, the goal in full, the count, the note to the Permanent Secretary | `docs/` | new |
| the prototype's source, its made-up data and its windowless checks | `src/` | new |
| one folder per working round, with its evidence: commands, their output, passages quoted | `_working/<round>/_evidence/` | new |

**The estate's root:** `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` — every path above is relative to it.
**The marketplace working copy on this machine:** `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb` — there is no marketplace working copy here: this is the folder the plugin is installed in, which may change when the plugin is updated. Where it is no longer there, `skills/project-inception/scripts/find_install.py` names the folder it moved to, and this line, the orchestrator's folder below and the governing procedure of section 3 are corrected to it.
**The orchestrator's folder on this machine:** `/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator` — the skill's folder in the local repository, for
example `~/Documents/Dev/orchestrator-local/plugins/fa-project-ops/skills/orchestrator`. The forms' placeholder
for the orchestrator's folder is filled with this path (section 11 of the procedure).
**The coordination's constants:** `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination/CONSTANTS.md` — the file that describes the ledger, the computers and the
accounts, written from `references/COORDINATION-template.md`. The forms' placeholder for it is filled
with this path.
**The orchestrator's code:** `MR` — the capital letters the orchestrator's own session name
begins with. Every session started from an instruction of this project carries it at the front of
its name, so that the owner can tell from his list of sessions which orchestrator a session belongs
to (section 6.5 of the procedure).
**Where the history is kept:** `local` — `github`, a repository on this computer pushed to its
remote by the owner; `local`, a repository on this computer only, into which the session commits its
own files at the end of every session (`repo-hygiene`); `none`, no repository, because git could not
be installed. Left out, `github`.

## 6a. The kinds of work of this project (optional)

Where this table is absent, the four kinds of the SDD method and their pages in the orchestrator's
`references/` apply: application design, feature design, platform implementation and the method's own
work. Where it stands, an instruction's `kind_of_work` names one of its kinds, and the instruction and
its review read the page named here. Each page is in the same three parts as the method's: the faults
a session of the kind refuses, what its review runs, and what is checked before an instruction of the
kind is issued.

| Kind of work | Its page |
|---|---|
| analysis | `_kinds/analysis.md` |
| drafting | `_kinds/drafting.md` |
| building | `_kinds/building.md` |
| checking | `_kinds/checking.md` |

## 7. The records this project keeps

| Record | Path | Written by |
|---|---|---|
| the record of what is running | `WHAT_IS_RUNNING.md` | its Open and Closed tables produced from the ledger of orchestrator events by `ledger.py views`, from the estate's cut-over on, and by hand, a row per round, before it; its head and its Held table by hand |
| the register of instructions | `_records/REGISTER.md` | produced by program |
| the facts a person keeps that no program derives | `_records/FACTS.md` | by hand |
| the record of each long delivery | `_records/delivery/<delivery>.md` | the review writes the row |

---

*Read by: every program of the travelling layer, as its argument; every instruction, for the places
its outputs go to; the incoming session's first task, as its first step.*
