# The page line that carries each gap — C-2026-10-31-27

Read by `check_gaps.py` as `GAPS.md` is. `_kinds/analysis.md` is read after the amendment (26 lines).

## GA1 — carried before this round by part 1, item 7; now also checked at issue by part 3

Source: `_kinds/analysis.md:14`
> 7. **To judge the positions of one question under another question's answer other than the one recommended, or under different answers for each position; or to declare a dependency between two answers in one direction only.** *(Added 31 October 2026 from the review `_reviews/REVIEW_QUESTIONS_2026-10-31.md`, gap G1, in the reviewer's proposed words.)*

Source: `_kinds/analysis.md:26`
> - Where the questions depend on one another, the instruction asks for every dependency, listed from every proposal's words and declared both ways, and for every rival judged under the other questions' recommendations

## GA2 — carried in part by part 1, items 3 and 7 (one direction, not neither; the counts not named); now carried by the line added to part 3

Source: `_kinds/analysis.md:10`
> 3. **To count over a set it has not listed.**

Source: `_kinds/analysis.md:14`
> or to declare a dependency between two answers in one direction only.**

Source: `_kinds/analysis.md:26`
> listed from every proposal's words and declared both ways

Source: `_kinds/analysis.md:26`
> with a run that builds each rival beside them and reads it against the ruled settings and the other recommendations' words, not the counts alone. *(Added 31 October 2026 from the reviews `_reviews/REVIEW_QUESTIONS_2026-10-31.md`, gap G1, and `_reviews/REVIEW_QUESTIONS_2026-10-31_v2.md`, gap G1.)*

## GC1 and GC2 — no page: the instruction's version 2

Source: `_prompts/PROMPT_COMMIT3_2026-10-31.md:118`
> **which lies in this instruction, not in the round**

Source: `_prompts/PROMPT_COMMIT3_2026-10-31.md:124`
> 1. **Keep every piece of evidence outside both repositories until step 5**: write it to a folder made with `mktemp -d`, and name that folder in the report.

Source: `_prompts/PROMPT_COMMIT3_2026-10-31.md:128`
> 5. Only then copy the folder's files into `/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-commit3-v2/_evidence/`, and write the report.

Source: `_prompts/PROMPT_COMMIT3_2026-10-31.md:132`
> - **B1** — The status recorded in step 4 is empty in both repositories, quoted from the file in the temporary folder.

Source: `_prompts/PROMPT_COMMIT3_2026-10-31.md:133`
> - **B2** — The files `git show --name-only HEAD` names in each repository are exactly the new and changed paths of that repository's "before" list — every one, and no other — compared by a command, file by file → `0 missing, 0 extra`.
