# CONSTANTS — the coordination of Arne Laponin's orchestrators

**Amended only by a ruling.** Each amendment names the ruling that obliges it.

## 1. What this coordination is for

It holds the ledger of orchestrator events for the projects Arne Laponin runs with the orchestrator procedure, one row in section 8 for each.

## 5. Standing constraints and prohibitions

- The ledger of orchestrator events is written by `ledger.py` and by nothing else. No entry is ever
  edited or deleted; a correction is a later entry.
- A rehearsal runs against a scratch copy of this file, never against this one.

## 6. The map of places

**Read by the program:** the table whose first column is "Kind of thing". Its first three rows are
required; the last two are optional and default to the root.

| Kind of thing | Where it lives | New, or already there |
|---|---|---|
| the ledger of orchestrator events, one file per event | `_ledger/` | new |
| the page that answers "who" | `WHO.html` | new |
| the registry of orchestrators | `projects.txt` | new |
| the measures of the ledger *(optional)* | `MEASURES.md` | new |
| the log of guards *(optional)* | `_guards/` | new |

**The estate's root:** `/Users/arnelaponin/Documents/Dev/wai-demo/_coordination` — every path above is relative to it.
**The orchestrator's code:** `REG` — the coordination's own code; it has no orchestrator of its own.

## 8. The estates the coordination covers

**Read by the program:** the codes in the first column, which `who` compares with the codes the ledger
holds.

| Code | Estate | Root | Record of what is running |
|---|---|---|---|
| `MR` | the mini registry | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry` | `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/WHAT_IS_RUNNING.md` |

## 9. The accounts the coordination covers

**Read by the program:** the address in the first column and the name in the second. An entry
carrying an account not in this table is refused.

| Address | Name | Organisation | Sessions in five hours |
|---|---|---|---|
| `arne.laponin@gmail.com` | Arne Laponin | | |

## 10. The computers the coordination covers

**Read by the program:** one row per computer that runs sessions, with its name as `hostname` reports
it, its home folder and its projects folder; the content folder may be left blank. A path written on
one computer is read on another by putting this computer's projects folder in place of the writer's.
Entries carry their paths in the canonical form `~/IdeaProjects/…`, whatever the projects folder is
called; the programs translate it back on reading.

| Computer, as `hostname` reports it | Home folder | Projects folder | Content folder |
|---|---|---|---|
| `MacBookPro` | `/Users/arnelaponin` | `/Users/arnelaponin/Documents/Dev/wai-demo` | |

**The ledger's program keeps the ledger one by git:** `no` — `yes` only where this folder is a
repository with a remote; then add the line **The identity the ledger's commits carry:**
`` `Name <address>` ``.

---

*Read by: `ledger.py` and the checks that find the ledger through it; every instruction, through
`<coordination>`.*
