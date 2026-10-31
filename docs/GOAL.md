# The goal in full — enrol a learner

**What this is.** Round 3 of the brief: the one goal of the prototype, **enrol a learner**, written step by step from the clerk opening the screen to the clerk seeing which of the two things happened, with every way it can go wrong and every screen it shows. Round 4 counts every requirement against it; round 6 builds it; under the ruling on G-12 the prototype's checks include a check for each way it can go wrong named here.

**Where it comes from.** In order of precedence: the brief (`../brief/MINI-REGISTRY-BRIEF.md`), the register (`docs/REQUIREMENTS.md`), the groundwork (`docs/GROUNDWORK.md`, `docs/groundwork/*.csv`), the owner's ruling D-2026-10-31-03 on `docs/GAPS-PAPER.md` (its summary rows, lines 26 to 38, and the recommendation closing each section — nothing else) and his ruling D-2026-10-31-05 on `docs/QUESTIONS-PAPER.md` (the proposal closing each section — nothing else). Each step and failure names its sources as `brief:<line>`, `R-<nn>`, `ruling:G-<nn>`, `ruling:Q-<n>` or `groundwork:<file>:<line>`. A fact none of them gives is not written here: where a step or a failure reaches such a fact, it says so and names the question in the closing section, **Gaps against the sources**.

**What it is not.** Enrolment is the only goal (the ruling on G-08): the reset of the made-up data is a command outside the clerk's screens and is not a step of this goal, and there is no screen for looking learners up.

**The order of the steps.** The steps are numbered in the order the sources give, with one exception: the sources do not settle whether the date's form (S-3) is held before or after the search (S-4). S-3 is numbered first for reading only; the order is gap 7.

---

## 1. The steps

### S-1 — The clerk opens the enrolment screen

- **The clerk:** opens the enrolment screen and sees an entry for each of the four: family name, given names, date of birth and school, the school chosen from the data's 3 schools.
- **The registry:** offers enrolment as the only thing the clerk's screens offer; there is no screen for looking learners up.
- **Screen:** SC-1, the enrolment screen.
- **Source:** brief:11 · R-02 · R-03 · ruling:G-07 · ruling:G-08 · groundwork:settings.csv:18

### S-2 — The clerk enters the child and submits

- **The clerk:** enters the family name, the given names and the date of birth, the date as YYYY-MM-DD; chooses the school from the data's 3; submits.
- **The registry:** the sources give it no act at this step; the search runs after the clerk has entered all four.
- **Screen:** SC-1, the enrolment screen.
- **Source:** brief:11 · R-03 · ruling:G-07 · groundwork:search_rule.csv:10 · groundwork:settings.csv:17

### S-3 — The registry holds the date of birth to its form

- **The clerk:** no act of the clerk's is given at this step.
- **The registry:** holds the date of birth to the form YYYY-MM-DD; a date in any other form is refused (F-2). Whether this comes before or after the search of S-4 is not settled by the sources (gap 7).
- **Screen:** none of its own; a date refused is shown on SC-4 (F-2).
- **Source:** ruling:G-07 · groundwork:settings.csv:17

### S-4 — The registry searches for the child first

- **The clerk:** no act of the clerk's is given at this step.
- **The registry:** searches after the clerk has entered all four, and first, before it does anything else with the entry and before any write (against S-3, gap 7); it looks among learners only; it compares the family name, the given names and the date of birth; two values that differ in capitals only are the same, and every difference but capitals makes two values differ; it does not compare the school, which is entered and saved and never searched on, nor any field but the three; it does not read the key table. If it finds exactly one learner the goal goes on at S-5; if it finds none, at S-6; on more than one, at F-4.
- **Screen:** none of its own; the search runs between SC-1 and the screen of S-7.
- **Source:** brief:11 · brief:13 · brief:14 · R-04 · R-05 · ruling:G-03 · ruling:G-05 · ruling:G-07 · groundwork:search_rule.csv:2 · groundwork:search_rule.csv:3 · groundwork:search_rule.csv:4 · groundwork:search_rule.csv:5 · groundwork:search_rule.csv:6 · groundwork:search_rule.csv:7 · groundwork:search_rule.csv:8 · groundwork:search_rule.csv:9 · groundwork:search_rule.csv:10 · groundwork:search_rule.csv:11 · groundwork:search_rule.csv:12 · groundwork:search_rule.csv:16

### S-5 — Exactly one learner found

- **The clerk:** sees the result at S-7.
- **The registry:** shows that learner and enters nothing new.
- **Screen:** SC-2, the screen of a learner found.
- **Source:** brief:13 · R-05 · groundwork:search_rule.csv:14

### S-6 — No learner found

- **The clerk:** sees the result at S-7.
- **The registry:** gives the child a new learner number — a whole number in sequence, one higher than the highest the registry holds, never given twice, and 1 as the first — and saves the record: the family name, given names, date of birth and school as entered, with that learner number.
- **Screen:** SC-3, the screen of a new learner.
- **Source:** brief:14 · R-03 · R-06 · ruling:G-01 · ruling:Q-4 · groundwork:lists.csv:11 · groundwork:lists.csv:12 · groundwork:lists.csv:13 · groundwork:lists.csv:14 · groundwork:lists.csv:15 · groundwork:search_rule.csv:15 · groundwork:settings.csv:9

### S-7 — The clerk sees which of the two happened

- **The clerk:** sees which of the two happened: on SC-2, that an existing learner was found, and that learner with its learner number; on SC-3, that a new learner number was given, and that number. The two screens say different things.
- **The registry:** shows the screen of what happened, SC-2 or SC-3.
- **Screen:** SC-2 or SC-3.
- **Source:** brief:15 · R-05 · R-07 · groundwork:search_rule.csv:18

---

## 2. The ways it can go wrong

### F-1 — An entry missing

- **At step:** S-2; the search of S-4 does not run.
- **What sets it off:** one or more of the four — family name, given names, date of birth, school — not entered.
- **What the clerk sees:** not given by the sources, which say only that the search does not run until all four are entered (gap 5).
- **What is saved:** no record: the one save the sources give follows the search finding none, and the search has not run.
- **Source:** brief:11 · brief:14 · ruling:G-07 · groundwork:search_rule.csv:10

### F-2 — The date of birth in the wrong form

- **At step:** S-3.
- **What sets it off:** a date of birth not in the form YYYY-MM-DD.
- **What the clerk sees:** SC-4: the date of birth is refused.
- **What is saved:** not settled by the sources: the date is refused; whether the search runs before the refusal, and so whether a record could be saved, is gap 7.
- **Source:** ruling:G-07 · ruling:G-09 · groundwork:settings.csv:17

### F-3 — A school not among the three

- **At step:** S-2, where the school is chosen.
- **What sets it off:** a school that is not one of the data's 3 schools. The sources say only that the school is chosen from the data's 3; whether such a school can reach the registry at all is gap 6.
- **What the clerk sees:** not given by the sources (gap 6).
- **What is saved:** not given by the sources (gap 6).
- **Source:** brief:24 · ruling:G-07 · groundwork:settings.csv:18

### F-4 — More than one learner found

- **At step:** S-4.
- **What sets it off:** the search of S-4 finds more than one learner. Under the data's settings it is never reached: no two different children share all three fields, and "share" ignores capitals.
- **What the clerk sees:** SC-5: the entry is refused, and the registry says the entry cannot be completed.
- **What is saved:** nothing new.
- **Source:** ruling:G-02 · ruling:G-05 · ruling:G-09 · ruling:Q-14 · groundwork:search_rule.csv:16 · groundwork:search_rule.csv:17 · groundwork:settings.csv:13

### F-5 — The same child, not caught

- **At step:** S-4, which then goes on at S-6.
- **What sets it off:** a child the registry already holds as a learner is entered with a family name, given names or date of birth that differs from that learner's in anything but capitals — a family name that differs by one letter among them. The search finds none.
- **What the clerk sees:** SC-3, the screen of a new learner: that a new learner number was given, and that number.
- **What is saved:** a second record for the same child, with a new learner number (S-6), so that the registry registers the same child twice. This is a limit of the search step, the brief's own rule: of the data's 8 children on more than one list, the search catches 4.
- **Source:** brief:7 · brief:13 · brief:14 · R-01 · R-06 · R-07 · ruling:G-05 · groundwork:search_rule.csv:5 · groundwork:search_rule.csv:6 · groundwork:settings.csv:14

---

## 3. The screens

Every view the clerk can see is a screen, messages and refusals included (the ruling on G-09). Each screen below carries the line "Invented data, Progressa is fictional" (R-17 · brief:33 · ruling:G-09). A failure whose view the sources do not give (F-1, F-3) has no screen here; its view is a gap (gaps 5 and 6).

### SC-1 — The enrolment screen

- **Named by:** S-1, S-2.
- **Shows:** an entry for each of family name, given names, date of birth and school; the school chosen from the data's 3.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-2 — A learner found

- **Named by:** S-5, S-7.
- **Shows:** that an existing learner was found, and that learner with its learner number.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-3 — A new learner

- **Named by:** S-6, S-7, F-5.
- **Shows:** that a new learner number was given, and that number.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-4 — The date of birth refused

- **Named by:** S-3, F-2.
- **Shows:** that the date of birth is refused.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-5 — The entry cannot be completed

- **Named by:** F-4.
- **Shows:** that the entry is refused and cannot be completed.
- **Carries the line:** "Invented data, Progressa is fictional".

---

## Gaps against the sources

Each is something the build will need that no source gives. Each is left open; no step, failure or screen above answers it.

1. **A date that is not a real date.** A date of birth in the form YYYY-MM-DD that names no day of the calendar, such as 2019-02-30: is it refused, and on which screen, or is it searched for and saved?
2. **An age outside 6 to 12.** The ages 6 to 12 are those of the made-up data: when the clerk enters a date of birth that makes the child younger than 6 or older than 12 on the date ages are reckoned on, or that falls after that date, is the entry refused, or is the child enrolled?
3. **A learner number that cannot be given.** When the registry cannot give a learner number or cannot save the record: what does the clerk see, and what is saved?
4. **What a name may hold.** Is there a longest family name or given names, are any characters refused, and is an entry of spaces only an entry made or an entry missing?
5. **An entry missing (F-1).** The sources say only that the search runs after the clerk has entered all four (`groundwork/search_rule.csv:10`; the ruling on G-07: "all four entered before the search runs"). Can the clerk submit with one of the four not entered; if so, what does the clerk see — the enrolment screen as it was, a message, or a refusal of the entry — and on which screen?
6. **A school not among the three (F-3).** The school is "chosen from the data's three" (the ruling on G-07; `groundwork/settings.csv:18`): can a school not among them reach the registry at all? If it can, what does the clerk see, is the entry refused, and is anything saved?
7. **The order of the date check and the search.** Two sets of passages do not settle which comes first. On one side, the ruling on G-07, `docs/GAPS-PAPER.md:254`: "the date entered as YYYY-MM-DD and refused otherwise, the school chosen from the data's three, and all four entered before the search runs", with `groundwork/settings.csv:17`: "YYYY-MM-DD; any other form refused". On the other, the brief's line 11: "The registry searches for the child first", R-04: "the registry searches for the child before it does anything else with the entry", and `groundwork/search_rule.csv:11`: "first: before the registry does anything else with the entry". Is a date in the wrong form refused before the search runs, or does the search run first; and so, for such a date, does the search run, and can a record be saved before the refusal?
8. **What a refusal says.** What do SC-4 and SC-5 say beyond that the date of birth is refused or that the entry cannot be completed, and are the clerk's four entries kept on the enrolment screen afterwards?
9. **More than one fault at once.** When more than one of F-1, F-2 and F-3 holds at once: does the clerk see every fault, or one only, and which?
10. **What SC-2 shows of the learner found.** Besides its learner number, which of the learner's fields does the screen show?
11. **A different school on a learner found.** When exactly one learner is found and the school the clerk chose is not the learner's school: is the clerk told, and is anything changed?
12. **A different child sharing the three fields.** A child the registry does not hold whose family name, given names and date of birth, capitals ignored, are those of a learner it holds — the school not compared — is found as that learner and nothing new is entered: is this a way the goal goes wrong, and what is the clerk to do?
13. **After the result.** Once the clerk has seen SC-2, SC-3, SC-4 or SC-5, how does the clerk begin the next enrolment: does the prototype return to SC-1?
