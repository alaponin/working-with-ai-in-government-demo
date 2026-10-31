# Working with AI in Government — demo project

The worked example for **Module 5 of *Working with AI in Government***: a small prototype built from start to finish by AI sessions under an orchestrator. A person rules on every decision, and every piece of work is reviewed before it is accepted.

> **All data here is invented.** Progressa, its Ministry of Education, Youth and Skills (MoEYS), its schools and its children are fictional. No real person's data is held anywhere in this repository.

## What was built

Progressa's MoEYS wants one list of learners instead of three. The **mini registry** is a prototype for reaching agreement on that, not the registry itself. A school clerk enrols a child, and the registry searches first so that the same child is never registered twice:

- exactly one match on family name, given names and date of birth (capitals ignored): the registry shows that learner and saves nothing new;
- no match: it gives the child a new learner number and saves the record;
- either way, the clerk sees which of the two happened.

It starts with 60 invented children across three schools and three lists: the school census, the examinations candidate list and the social grant list. Eight children are on more than one list, and four of those have their family name spelt differently on one list. The numbers are fixed, so every count has a known answer.

The project delivered two things:

1. **The working prototype**, with its checks passing: [`mini-registry/src/`](mini-registry/src/)
2. **A one-page note to the Permanent Secretary** on what the prototype shows and what it does not: [`mini-registry/docs/NOTE.md`](mini-registry/docs/NOTE.md)

## Run it

You need Node.js 22. There are no dependencies, so there is nothing to install.

```sh
cd mini-registry/src
node reset.js                  # make the invented data (the same every time)
node --test test/*.test.js     # the checks: 57 tests, no window opened
node server.js                 # the prototype, at http://127.0.0.1:8126 (PORT=… to change)
```

The server listens on `127.0.0.1` only and connects to nothing outside your computer.

## How it was made

The work followed the [brief](brief/MINI-REGISTRY-BRIEF.md) in eight rounds. Each round was an instruction, a work session, an independent review and the owner's ruling:

| # | Piece of work | Kind | Result |
|---|---|---|---|
| 1 | The register of requirements, each with a test | drafting | [`REQUIREMENTS.md`](mini-registry/docs/REQUIREMENTS.md) |
| 2 | The groundwork: the lists, the settings, the search rule | drafting | [`GROUNDWORK.md`](mini-registry/docs/GROUNDWORK.md) |
| 3 | The goal in full: every step of enrolling, every way it fails | drafting | [`GOAL.md`](mini-registry/docs/GOAL.md) |
| 4 | Every requirement traced against the goal, both ways | checking | [`COUNT.md`](mini-registry/docs/COUNT.md) |
| 5 | The scaffold and the invented data | building | [`src/`](mini-registry/src/) |
| 6 | The goal built | building | [`src/`](mini-registry/src/) |
| 7 | How many of the 8 duplicates the search catches | checking | [`DUPLICATES.md`](mini-registry/docs/DUPLICATES.md) |
| 8 | The note to the Permanent Secretary | drafting | [`NOTE.md`](mini-registry/docs/NOTE.md) |

Each kind of work has a page listing the faults its sessions refuse to make, in [`kinds/`](kinds/). The page grows each time a review finds a new fault.

## What is where

| Path | What it holds |
|---|---|
| [`brief/`](brief/) | The brief: the document that governs the project |
| [`kinds/`](kinds/) | The four kinds of work (analysis, drafting, building, checking) and the faults each one refuses |
| [`mini-registry/`](mini-registry/) | The project itself |
| ├ `CONSTANTS.md` | What the project is for, the documents that govern it, and where everything lives |
| ├ `docs/` | The drafted documents and the tables the build reads |
| ├ `src/` | The prototype, its invented data and its checks |
| ├ `_prompts/` | Every instruction given to a work or review session |
| ├ `_reports/` | Every work session's report |
| ├ `_reviews/` | Every review of a report |
| ├ `_working/` | Each round's evidence: scripts, logs and outputs |
| ├ `_records/` | Handover and cut-over records |
| └ `WHAT_IS_RUNNING.md` | The state of the work |
| [`_coordination/`](_coordination/) | The orchestrator's ledger: one append-only file per event (`_ledger/`), guard checks (`_guards/`) and the measures drawn from them (`MEASURES.md`) |

To follow the project from start to finish, read the brief, then `mini-registry/CONSTANTS.md`, then the reports and reviews in date order. The latest state is in [`mini-registry/_records/HANDOVER_2026-11-01.md`](mini-registry/_records/HANDOVER_2026-11-01.md).

## Notes

- Absolute paths in the records (`/Users/arnelaponin/…`) are the author's machine, kept as the sessions wrote them.
- `mini-registry/` and `_coordination/` began as separate repositories, and their histories are merged here.
