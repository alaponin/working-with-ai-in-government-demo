# Instructions

This folder holds the instructions of the mini registry, one file to each instruction, and nothing else. An instruction sets one bounded task for a working session to carry out. The name of each file begins with `PROMPT_`.

**Who writes here.** The orchestrator session. It adds the instruction's row to the record of what is running before it issues the instruction.

**What governs it.** The orchestrator procedure, which is the skill `orchestrator` in the plugin `fa-project-ops`, section 6, and the instruction form beside it, `PROMPT-template.md`. Where this project's constants name a different place for instructions, the constants govern.

**When a file is written.** Before a working session starts on the task. A second attempt at the same task is the next version of the same file, never a new file.

A report or a review is never filed here. Each has a folder of its own.
