# The goal in full — enrol a learner

**What this is.** Round 3 of the brief: the one goal of the prototype, **enrol a learner**, written step by step from the clerk opening the screen to the clerk seeing which of the two things happened, with every way it can go wrong and every screen it shows. Round 4 counts every requirement against it; round 6 builds it; under the ruling on G-12 the prototype's checks include a check for each way it can go wrong named here.

**Where it comes from.** In order of precedence: the brief (`../brief/MINI-REGISTRY-BRIEF.md`), the register (`docs/REQUIREMENTS.md`), the groundwork (`docs/GROUNDWORK.md`, `docs/groundwork/*.csv`), the owner's ruling D-2026-10-31-03 on `docs/GAPS-PAPER.md` (its summary rows, lines 26 to 38, and the recommendation closing each section — nothing else) and his ruling D-2026-10-31-05 on `docs/QUESTIONS-PAPER.md` (the proposal closing each section — nothing else). Each step and failure names its sources as `brief:<line>`, `R-<nn>`, `ruling:G-<nn>`, `ruling:Q-<n>` or `groundwork:<file>:<line>`. A fact none of them gives is not written here; it is a question in the closing section.

**What it is not.** Enrolment is the only goal (the ruling on G-08): the reset of the made-up data is a command outside the clerk's screens and is not a step of this goal, and there is no screen for looking learners up.

---

## 1. The steps

### S-1 — The clerk opens the enrolment screen

- **The clerk:** opens the enrolment screen and sees an entry for each of the four: family name, given names, date of birth and school, the school a choice among the data's 3 schools.
- **The registry:** offers enrolment as the only goal of its screens; there is no screen for looking learners up.
- **Screen:** SC-1, the enrolment screen.
- **Source:** brief:11 · R-02 · R-03 · ruling:G-07 · ruling:G-08 · groundwork:settings.csv:18

### S-2 — The clerk enters the child and submits

- **The clerk:** enters the family name, the given names and the date of birth, the date as YYYY-MM-DD; chooses the school; submits.
- **The registry:** nothing yet: the search runs only after the clerk has entered all four.
- **Screen:** SC-1, the enrolment screen.
- **Source:** brief:11 · R-03 · ruling:G-07 · groundwork:settings.csv:17 · groundwork:search_rule.csv:10

### S-3 — The registry takes the entry

- **The clerk:** waits.
- **The registry:** takes the entry to the search only when all four are entered, the date of birth is in the form YYYY-MM-DD and the school is one of the data's 3; a date in any other form is refused. Where one of these does not hold, the goal goes on at F-1, F-2 or F-3.
- **Screen:** SC-1, the enrolment screen.
- **Source:** ruling:G-07 · groundwork:settings.csv:17 · groundwork:settings.csv:18 · groundwork:search_rule.csv:10

### S-4 — The registry searches for the child first

- **The clerk:** waits.
- **The registry:** searches first, before it does anything else with the entry and before any write; it looks among learners only; it compares the family name, the given names and the date of birth, and nothing else; two values that differ in capitals only are the same, and every other difference makes two values differ; it does not compare the school, which is entered and saved and never searched on, nor any field but the three; it does not read the key table. On exactly one learner found the goal goes on at S-5, on none at S-6, on more than one at F-4.
- **Screen:** none of its own; the search runs between SC-1 and the screen of S-7.
- **Source:** brief:11 · brief:13 · R-04 · R-05 · ruling:G-03 · ruling:G-05 · groundwork:search_rule.csv:2 · groundwork:search_rule.csv:3 · groundwork:search_rule.csv:4 · groundwork:search_rule.csv:5 · groundwork:search_rule.csv:6 · groundwork:search_rule.csv:7 · groundwork:search_rule.csv:8 · groundwork:search_rule.csv:9 · groundwork:search_rule.csv:11 · groundwork:search_rule.csv:12

### S-5 — Exactly one learner found

- **The clerk:** sees the learner found (S-7).
- **The registry:** shows that learner and enters nothing new.
- **Screen:** SC-2, the screen of a learner found.
- **Source:** brief:13 · R-05 · groundwork:search_rule.csv:14

### S-6 — No learner found

- **The clerk:** sees the new learner number (S-7).
- **The registry:** gives the child a new learner number — a whole number in sequence, one higher than the highest the registry holds, never given twice, and 1 where it holds none — and saves the record: the family name, given names, date of birth and school as entered, with that learner number.
- **Screen:** SC-3, the screen of a new learner.
- **Source:** brief:14 · R-06 · R-03 · ruling:G-01 · ruling:Q-4 · groundwork:settings.csv:9 · groundwork:search_rule.csv:15 · groundwork:lists.csv:11 · groundwork:lists.csv:12 · groundwork:lists.csv:13 · groundwork:lists.csv:14 · groundwork:lists.csv:15

### S-7 — The clerk sees which of the two happened

- **The clerk:** sees which of the two happened: on SC-2, that an existing learner was found, and that learner with its learner number; on SC-3, that a new learner number was given, and that number. The two screens say different things.
- **The registry:** shows the screen of what happened.
- **Screen:** SC-2 or SC-3.
- **Source:** brief:15 · R-07 · R-05 · groundwork:search_rule.csv:18

---

## 2. The ways it can go wrong

### F-1 — An entry missing

- **At step:** S-3.
- **What sets it off:** the clerk submits with one or more of the four — family name, given names, date of birth, school — not entered.
- **What the clerk sees:** SC-4: the entry is refused; the search does not run.
- **What is saved:** nothing.
- **Source:** brief:11 · ruling:G-07 · ruling:G-09 · groundwork:search_rule.csv:10

### F-2 — The date of birth in the wrong form

- **At step:** S-3.
- **What sets it off:** a date of birth not in the form YYYY-MM-DD.
- **What the clerk sees:** SC-5: the entry is refused; the search does not run.
- **What is saved:** nothing.
- **Source:** ruling:G-07 · ruling:G-09 · groundwork:settings.csv:17

### F-3 — A school not among the three

- **At step:** S-3.
- **What sets it off:** a school that is not one of the data's 3 schools.
- **What the clerk sees:** SC-6: the entry is refused; the search does not run.
- **What is saved:** nothing.
- **Source:** brief:24 · ruling:G-07 · ruling:G-09 · groundwork:settings.csv:18

### F-4 — More than one learner found

- **At step:** S-4.
- **What sets it off:** the search finds more than one learner with the same family name, given names and date of birth, capitals ignored. Under the data's settings it is never reached: no two different children share all three fields, capitals ignored.
- **What the clerk sees:** SC-7: the entry cannot be completed.
- **What is saved:** nothing new.
- **Source:** ruling:G-02 · ruling:G-09 · ruling:Q-14 · groundwork:search_rule.csv:16 · groundwork:search_rule.csv:17 · groundwork:settings.csv:13

### F-5 — The same child, not caught

- **At step:** S-4, which then goes on at S-6.
- **What sets it off:** a child the registry already holds as a learner is entered with a family name, given names or date of birth that differs from that learner's in anything but capitals — a family name spelt differently by one letter among them. The search finds none.
- **What the clerk sees:** SC-3, the screen of a new learner, as for a child the registry does not hold.
- **What is saved:** a second learner for the same child, with a new learner number (S-6). This is a limit of the search step, the brief's own rule: of the data's 8 children on more than one list, the search catches 4, and the 4 whose family name is spelt differently on one list are missed so.
- **Source:** brief:7 · brief:13 · R-06 · ruling:G-05 · groundwork:search_rule.csv:6 · groundwork:settings.csv:14

---

## 3. The screens

Every view the clerk can see is a screen, messages and refusals included (the ruling on G-09). Each screen below carries the line "Invented data, Progressa is fictional" (R-17 · brief:33 · ruling:G-09).

### SC-1 — The enrolment screen

- **Named by:** S-1, S-2, S-3.
- **Shows:** an entry for each of family name, given names, date of birth and school; the school a choice among the data's 3.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-2 — A learner found

- **Named by:** S-5, S-7.
- **Shows:** that an existing learner was found, and that learner with its learner number.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-3 — A new learner

- **Named by:** S-6, S-7, F-5.
- **Shows:** that a new learner number was given, and that number.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-4 — Refused: an entry missing

- **Named by:** F-1.
- **Shows:** that the entry is refused.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-5 — Refused: the date of birth's form

- **Named by:** F-2.
- **Shows:** that the entry is refused.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-6 — Refused: the school

- **Named by:** F-3.
- **Shows:** that the entry is refused.
- **Carries the line:** "Invented data, Progressa is fictional".

### SC-7 — The entry cannot be completed

- **Named by:** F-4.
- **Shows:** that the entry cannot be completed.
- **Carries the line:** "Invented data, Progressa is fictional".

---

## Gaps against the sources

Each is something the build will need that no source gives. Each is left open; no step, failure or screen above answers it.

1. **A date that is not a real date.** A date of birth in the form YYYY-MM-DD that names no day of the calendar, such as 2019-02-30: is the entry refused, and on which screen, or is it searched for and saved?
2. **An age outside 6 to 12.** A date of birth that makes the child younger than 6 or older than 12 on the settings' fixed date, or that falls after that date: is the entry refused, or is the child enrolled?
3. **A learner number that cannot be given.** When the registry cannot give a learner number or cannot save the record: what does the clerk see, and what is saved?
4. **What a name may hold.** Is there a longest family name or given names, are any characters refused, and is an entry of spaces only an entry made or an entry missing?
5. **What a refusal says.** What do SC-4 to SC-7 say beyond that the entry is refused or cannot be completed, and are the clerk's four entries kept on the enrolment screen afterwards?
6. **More than one fault at once.** When an entry is missing and the date is in the wrong form, or both other faults hold: does the clerk see one refusal naming every fault, or one fault only, and which?
7. **What SC-2 shows of the learner found.** Besides its learner number, which of the learner's fields does the screen show?
8. **A different school on a learner found.** When exactly one learner is found and the school the clerk chose is not the learner's school: is the clerk told, and is anything changed?
9. **A different child sharing the three fields.** A child the registry does not hold whose family name, given names and date of birth, capitals ignored, are those of a learner it holds — the school not compared — is found as that learner and nothing new is entered: is this a way the goal goes wrong, and what is the clerk to do?
10. **A school not among the three reaching the registry.** The enrolment screen offers the school as a choice among the 3: by what way can a school not among them reach the registry, so that F-3 is set off and SC-6 shown?
11. **After the result.** Once the clerk has seen SC-2, SC-3 or a refusal, how does the clerk begin the next enrolment: does the prototype return to SC-1?
