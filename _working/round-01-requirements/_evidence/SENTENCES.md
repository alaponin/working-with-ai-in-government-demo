# The inventory of the brief's units — round 1, the register of requirements

Written by `split_units.py` (beside this file) from `/Users/arnelaponin/Documents/Dev/wai-demo/brief/MINI-REGISTRY-BRIEF.md`, its five sections "What it is for", "What it must do", "The made-up data, in known numbers", "What it must not do" and "What it delivers". The title, the italic opening and "The rounds, in order" are out of the inventory. A unit is a sentence, a list item or a table row; each section heading is listed as a unit that is not a requirement; a table's separator line carries no words and is not a unit. Dispositions are read from `dispositions.tsv`.

### U-01 · line 5 · heading · not a requirement

> What it is for

Reason: a heading

### U-02 · line 7 · sentence · not a requirement

> Progressa's Ministry of Education, Youth and Skills (MoEYS) wants one list of learners instead of three.

Reason: context: what the ministry wants of the real registry, not of the prototype

### U-03 · line 7 · sentence · requirement

> Before anyone builds the real thing, the planning unit wants to see a small working prototype: a school clerk enrols a child, and the registry does not register the same child twice.

### U-04 · line 7 · sentence · not a requirement

> The prototype is for agreement.

Reason: purpose: what the prototype is for

### U-05 · line 7 · sentence · not a requirement

> It is not the registry.

Reason: context: a statement of scope that names nothing the prototype must do, be, hold or deliver

### U-06 · line 9 · heading · not a requirement

> What it must do

Reason: a heading

### U-07 · line 11 · sentence · requirement

> One goal: **enrol a learner.**

### U-08 · line 11 · sentence · requirement

> A school clerk enters a child's family name, given names, date of birth and school.

### U-09 · line 11 · sentence · requirement

> The registry searches for the child first:

### U-10 · line 13 · list item · requirement

> if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;

### U-11 · line 14 · list item · requirement

> if it finds none, it gives the child a new learner number and saves the record;

### U-12 · line 15 · list item · requirement

> the clerk sees which of the two happened.

### U-13 · line 17 · heading · not a requirement

> The made-up data, in known numbers

Reason: a heading

### U-14 · line 19 · sentence · requirement

> The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.

### U-15 · line 21 · table row · not a requirement

> | Setting | Value |

Reason: the table's header row: names its columns

### U-16 · line 23 · table row · requirement

> | Children | 60 |

### U-17 · line 24 · table row · requirement

> | Schools | 3 |

### U-18 · line 25 · table row · requirement

> | Children on more than one list | 8 |

### U-19 · line 26 · table row · requirement

> | Of those, children whose family name is spelt differently on one list | 4 |

### U-20 · line 27 · table row · requirement

> | Ages | 6 to 12 |

### U-21 · line 29 · sentence · requirement

> The numbers are fixed so that every later count has a known answer.

### U-22 · line 29 · sentence · requirement

> The data is made the same way every time it is reset.

### U-23 · line 31 · heading · not a requirement

> What it must not do

Reason: a heading

### U-24 · line 33 · list item · requirement

> Hold any real person's data. Every screen says "Invented data, Progressa is fictional".

### U-25 · line 34 · list item · requirement

> Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.

### U-26 · line 35 · list item · requirement

> Open a window on its own. Every check of the screens runs without one.

### U-27 · line 37 · heading · not a requirement

> What it delivers

Reason: a heading

### U-28 · line 39 · list item · requirement

> The working prototype, on your computer, with its checks passing.

### U-29 · line 40 · list item · requirement

> A one-page note to the Permanent Secretary: what the prototype shows, and what it does not.

---

Units: 29. Marked requirement: 20. Marked not a requirement: 9.
