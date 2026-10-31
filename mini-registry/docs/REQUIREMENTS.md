# The register of requirements — the mini registry

**Source.** The brief for Module 5, the mini registry (`../brief/MINI-REGISTRY-BRIEF.md`, sha256 `ec6971e74a6a8387de0e5bd7a5e1cdead6ddf711b8fdac3ccc1d4b7555e11f64`), its five sections "What it is for", "What it must do", "The made-up data, in known numbers", "What it must not do" and "What it delivers". Its title, its italic opening and its section "The rounds, in order" describe the work, not the registry, and are not drawn on.

**How it was drawn.** Every unit of those five sections — a sentence, a list item or a table row — was listed and given a disposition in the inventory of round 1 (`_working/round-01-requirements/_evidence/SENTENCES.md`, unit identifiers `U-01` onwards). Each requirement below cites the unit it rests on, by its identifier and its line in the brief, and quotes it word for word. A unit carrying two requirements is cited by two.

**How each requirement reads.** The requirement says no more than its unit says. Its test names what is set up, what is done and what is seen, so that a person or a program can run it on the prototype once it is built and say pass or fail. Every check of a screen in these tests is a windowless check: it reads the screen without opening a window (R-21). Where a test needs a fact the brief does not give, it names the open question in the closing section, **Gaps against the brief**, and does not answer it.

**Words used in the tests.** *Reset*: the prototype's own act of making its made-up data afresh (the brief, line 29). *F, G, D, S*: a family name, given names, a date of birth and a school entered by the clerk, chosen for the test.

---

## What it is for

### R-01

**Cites:** U-03, brief line 7

> Before anyone builds the real thing, the planning unit wants to see a small working prototype: a school clerk enrols a child, and the registry does not register the same child twice.

**Requirement.** The prototype is a small working prototype in which a school clerk enrols a child and the registry does not register the same child twice.

**Test.**
- *Set up:* the prototype started on the computer and its data reset; the number of learners the registry holds is read.
- *Do:* as a school clerk, enrol a child with F, G, D and S that the registry does not yet hold; read the number of learners; enrol the same child again with the same F, G, D and S; read the number of learners again.
- *See:* the first enrolment adds one learner; the second adds none. **Expected:** the count rises by 1 after the first enrolment and by 0 after the second. Pass if both hold.

## What it must do

### R-02

**Cites:** U-07, brief line 11

> One goal: **enrol a learner.**

**Requirement.** The prototype has one goal: to enrol a learner.

**Test.**
- *Set up:* the prototype started and its data reset.
- *Do:* by a windowless check, list every goal the prototype offers the clerk on its screens (what counts as a goal: gap G-08).
- *See:* **Expected:** one goal, enrolling a learner. Pass if the list holds that goal and no other.

### R-03

**Cites:** U-08, brief line 11

> A school clerk enters a child's family name, given names, date of birth and school.

**Requirement.** To enrol a child, the school clerk enters the child's family name, given names, date of birth and school.

**Test.**
- *Set up:* the prototype started and its data reset.
- *Do:* by a windowless check, open the enrolment screen; enter F, G, D and S for a child the registry does not yet hold (the form of a date and of a school: gap G-07); submit.
- *See:* the screen offers an entry for each of the four — family name, given names, date of birth, school — and the record saved holds F, G, D and S as entered. Pass if all four entries are offered and all four values are saved.

### R-04

**Cites:** U-09, brief line 11

> The registry searches for the child first:

**Requirement.** When the clerk has entered the child, the registry searches for the child before it does anything else with the entry.

**Test.**
- *Set up:* the prototype started and its data reset; a program records, in order, every read and every write the registry makes on its data during an enrolment.
- *Do:* enrol a child the registry does not hold (F, G, D, S); then enrol the same child again with the same entries.
- *See:* in each enrolment the search is the first act on the data, before any write; in the second enrolment there is no write. Pass if a search precedes every write in both, and the second has none.

### R-05

**Cites:** U-10, brief line 13

> if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;

**Requirement.** If the search finds exactly one learner with the same family name, given names and date of birth, capitals ignored, the registry shows that learner and enters nothing new.

**Test.**
- *Set up:* the prototype started and its data reset; enrol a child with F, G, D and S, and note the learner number it is given and the number of learners the registry then holds.
- *Do:* (a) enrol a child with exactly F, G and D; (b) enrol a child with F and G written in other capitals — for example every letter a capital — and the same D.
- *See:* in (a) and in (b), the screen shows the learner saved in the set-up, with its learner number, and the number of learners is unchanged. **Expected:** learners added: 0 in each of (a) and (b). Pass if both hold. (What the registry does when the search finds more than one: gap G-02.)

### R-06

**Cites:** U-11, brief line 14

> if it finds none, it gives the child a new learner number and saves the record;

**Requirement.** If the search finds no such learner, the registry gives the child a new learner number and saves the record.

**Test.**
- *Set up:* the prototype started and its data reset; read the number of learners and every learner number the registry holds (what a learner number looks like: gap G-01; where the search looks: gap G-03).
- *Do:* (a) enrol a child whose family name, given names and date of birth, capitals ignored, match none of the records the search looks in; (b) then enrol a child with the same given names and date of birth as the child of (a), and a family name that differs from it by one letter, not by capitals alone.
- *See:* after each of (a) and (b), one record is saved, holding the entries made and a learner number that no learner held before. **Expected:** learners added: 1 after (a) and 1 after (b); each new learner number unlike every number held before it. Pass if both hold.

### R-07

**Cites:** U-12, brief line 15

> the clerk sees which of the two happened.

**Requirement.** After the search, the clerk sees which of the two happened: an existing learner was found and shown, or a new learner number was given and the record saved.

**Test.**
- *Set up:* the prototype started and its data reset.
- *Do:* by a windowless check, enrol a child the registry does not hold, and read the screen that follows; then enrol the same child again, and read the screen that follows.
- *See:* the first screen says that a new learner number was given, and shows it; the second says that an existing learner was found, and shows that learner. Pass if each screen says which of the two happened and the two screens say different things.

## The made-up data, in known numbers

### R-08

**Cites:** U-14, brief line 19

> The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.

**Requirement.** The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.

**Test.**
- *Set up:* the prototype's data reset, before any enrolment.
- *Do:* read the lists the data holds, and for each child the lists it is on.
- *See:* **Expected:** 3 lists — the school census, the examinations authority's candidate list and the social grant programme's list — and every child on at least one of them. Pass if both hold.

### R-09

**Cites:** U-16, brief line 23

> | Children | 60 |

**Requirement.** The made-up data holds 60 children.

**Test.**
- *Set up:* the prototype's data reset, before any enrolment.
- *Do:* count the children in the data, by the unit of counting that gap G-04 asks after.
- *See:* **Expected:** 60. Pass if the count is 60.

### R-10

**Cites:** U-17, brief line 24

> | Schools | 3 |

**Requirement.** The made-up data has 3 schools.

**Test.**
- *Set up:* the prototype's data reset, before any enrolment.
- *Do:* count the different schools the data names.
- *See:* **Expected:** 3. Pass if the count is 3.

### R-11

**Cites:** U-18, brief line 25

> | Children on more than one list | 8 |

**Requirement.** In the made-up data, 8 children are on more than one list.

**Test.**
- *Set up:* the prototype's data reset, before any enrolment.
- *Do:* for each child, count the lists that carry it, by what the data records of which entries are the same child (gap G-05); count the children carried by two lists or more.
- *See:* **Expected:** 8. Pass if the count is 8.

### R-12

**Cites:** U-19, brief line 26

> | Of those, children whose family name is spelt differently on one list | 4 |

**Requirement.** Of the children on more than one list, 4 have their family name spelt differently on one list.

**Test.**
- *Set up:* the prototype's data reset, before any enrolment; the children of R-11.
- *Do:* for each of them, compare the family name each list gives it, letter for letter; count the children whose family name is spelt differently on one list.
- *See:* **Expected:** 4. Pass if the count is 4. This test counts the data; how many of these children the registry's search catches is not tested here.

### R-13

**Cites:** U-20, brief line 27

> | Ages | 6 to 12 |

**Requirement.** The children in the made-up data are aged 6 to 12.

**Test.**
- *Set up:* the prototype's data reset, before any enrolment.
- *Do:* reckon each child's age from its date of birth (on what date, and whether 6 and 12 are included: gap G-06); count the children whose age falls outside 6 to 12.
- *See:* **Expected:** every age within 6 to 12; children outside: 0. Pass if the count is 0.

### R-14

**Cites:** U-21, brief line 29

> The numbers are fixed so that every later count has a known answer.

**Requirement.** The numbers of the table are fixed: the data holds them every time.

**Test.**
- *Set up:* the prototype started.
- *Do:* reset the data and run the counts of R-09 to R-13; enrol one child; reset the data again and run the same counts again.
- *See:* **Expected**, after each reset: children 60, schools 3, children on more than one list 8, of those with the family name spelt differently on one list 4, ages within 6 to 12 (children outside: 0). Pass if both runs give these numbers.

### R-15

**Cites:** U-22, brief line 29

> The data is made the same way every time it is reset.

**Requirement.** Every reset makes the data the same way.

**Test.**
- *Set up:* the prototype started.
- *Do:* reset the data and keep a copy of it; enrol one child; reset the data again and keep a second copy.
- *See:* compare the two copies record by record. **Expected:** records that differ: 0. Pass if the two copies are the same.

## What it must not do

### R-16

**Cites:** U-24, brief line 33

> Hold any real person's data. Every screen says "Invented data, Progressa is fictional".

**Requirement.** The prototype holds no real person's data.

**Test.**
- *Set up:* the prototype's source and its data after a reset.
- *Do:* list every source from which the data is made: every file and program the reset reads.
- *See:* each source is part of the prototype and makes invented records; none is a record of persons brought in from elsewhere. Pass if no source carries a real person's data (what evidence shows this: gap G-10).

### R-17

**Cites:** U-24, brief line 33

> Hold any real person's data. Every screen says "Invented data, Progressa is fictional".

**Requirement.** Every screen of the prototype says "Invented data, Progressa is fictional".

**Test.**
- *Set up:* the prototype started and its data reset; the list of its screens (what counts as a screen: gap G-09).
- *Do:* by a windowless check, show each screen in turn, among them the screen after a new learner is saved and the screen after an existing learner is found, and read its text.
- *See:* the text of each screen holds the words "Invented data, Progressa is fictional". **Expected:** screens without them: 0. Pass if the count is 0.

### R-18

**Cites:** U-25, brief line 34

> Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.

**Requirement.** The prototype connects to nothing outside the computer it runs on.

**Test.**
- *Set up:* the prototype on the computer; a program that records every network connection the prototype's processes open, with both its ends.
- *Do:* start the prototype; reset the data; enrol a child the registry does not hold; enrol the same child again; run every check of the prototype; stop it.
- *See:* every recorded connection has both its ends on the computer itself. **Expected:** connections to anything outside the computer: 0. Pass if the count is 0.

### R-19

**Cites:** U-25, brief line 34

> Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.

**Requirement.** Where the project needs another body, that body is simulated.

**Test.**
- *Set up:* the list of other bodies the prototype draws on (which they are: gap G-11).
- *Do:* for each body on the list, find in the prototype what stands for it, and run the prototype's part that uses it with the computer cut off from every network.
- *See:* each body is answered by a simulation on the computer, and the part that uses it works. **Expected:** bodies reached outside the computer: 0. Pass if every body on the list is simulated.

### R-20

**Cites:** U-26, brief line 35

> Open a window on its own. Every check of the screens runs without one.

**Requirement.** The prototype opens no window on its own.

**Test.**
- *Set up:* read the list of windows open on the computer's screen, by a command that brings nothing forward.
- *Do:* start the prototype; reset the data; enrol a child through a windowless check; stop the prototype; read the list of windows again.
- *See:* **Expected:** windows opened: 0 — the second list is the first. Pass if no window was added.

### R-21

**Cites:** U-26, brief line 35

> Open a window on its own. Every check of the screens runs without one.

**Requirement.** Every check of the prototype's screens runs without a window.

**Test.**
- *Set up:* read the list of windows open on the computer's screen, by a command that brings nothing forward.
- *Do:* run every check of the screens; while they run and when they end, read the list of windows again.
- *See:* every check runs to its end and gives its result. **Expected:** windows opened: 0 at each reading. Pass if no window was added at any reading.

## What it delivers

### R-22

**Cites:** U-28, brief line 39

> The working prototype, on your computer, with its checks passing.

**Requirement.** The working prototype is delivered on the owner's computer, with its checks passing.

**Test.**
- *Set up:* the owner's computer, with the prototype as delivered (which checks are its checks: gap G-12).
- *Do:* run the prototype's checks there; start the prototype and enrol a child the registry does not hold.
- *See:* **Expected:** checks failing: 0; the enrolment completes on that computer. Pass if both hold.

### R-23

**Cites:** U-29, brief line 40

> A one-page note to the Permanent Secretary: what the prototype shows, and what it does not.

**Requirement.** A one-page note to the Permanent Secretary is delivered, saying what the prototype shows and what it does not.

**Test.**
- *Set up:* the note as delivered.
- *Do:* count its pages (on what page: gap G-13); read it.
- *See:* **Expected:** 1 page, addressed to the Permanent Secretary, saying what the prototype shows and saying what it does not. Pass if all three hold.

---

## Gaps against the brief

Each is a question the brief does not answer and a test above needs. None is answered in this register.

- **G-01** (R-06) What does a learner number look like, and how is a new one made?
- **G-02** (R-05) What does the registry do when its search finds more than one learner with the same family name, given names and date of birth, capitals ignored?
- **G-03** (R-04, R-05, R-06) Where does the search look: among the learners the registry has saved, among the children on the three lists, or both — and are the children on the three lists learners with a learner number when the prototype starts?
- **G-04** (R-09) Is "Children 60" the number of different children, each counted once however many lists carry it, or the number of entries across the three lists?
- **G-05** (R-11, R-12) How does the made-up data record that entries on two lists are the same child, so that the 8 and the 4 can be counted?
- **G-06** (R-13) On what date is a child's age reckoned, and are the ages 6 and 12 themselves within "6 to 12"?
- **G-07** (R-03) In what form does the clerk enter a date of birth; is the school chosen from the data's three schools or written in; and must all four entries be made before the search runs?
- **G-08** (R-02) Does anything else the prototype offers — resetting the data, looking at a learner — count as a goal under "One goal"?
- **G-09** (R-17) What counts as a screen: does a message the prototype shows, such as a refusal of an entry, count?
- **G-10** (R-16) What evidence does the brief accept that no real person's data is held?
- **G-11** (R-19) Which other bodies, if any, does the project need — and are the census, the examinations authority and the social grant programme, whose lists the data holds, among them?
- **G-12** (R-22) Which checks are "its checks": the tests of this register, or a set a later round names?
- **G-13** (R-23) On what size of page, and in what form, is the note's one page counted?
- **G-14** (R-05) The brief forgives capitals only: does it mean the search to treat a space before or after a name, or between given names, as part of the name?
