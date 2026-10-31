# The mini registry: the brief for Module 5

*The project you build in Module 5, with the orchestrator plugin. Give this page to your orchestrator session as the document that governs the project. Everything in it is invented for Progressa, the fictional country every course here uses.*

## What it is for

Progressa's Ministry of Education, Youth and Skills (MoEYS) wants one list of learners instead of three. Before anyone builds the real thing, the planning unit wants to see a small working prototype: a school clerk enrols a child, and the registry does not register the same child twice. The prototype is for agreement. It is not the registry.

## What it must do

One goal: **enrol a learner.** A school clerk enters a child's family name, given names, date of birth and school. The registry searches for the child first:

- if it finds exactly one learner with the same family name, given names and date of birth (capitals ignored), it shows that learner and enters nothing new;
- if it finds none, it gives the child a new learner number and saves the record;
- the clerk sees which of the two happened.

## The made-up data, in known numbers

The prototype starts with invented children spread over three lists: the school census, the examinations authority's candidate list and the social grant programme's list.

| Setting | Value |
|---|---|
| Children | 60 |
| Schools | 3 |
| Children on more than one list | 8 |
| Of those, children whose family name is spelt differently on one list | 4 |
| Ages | 6 to 12 |

The numbers are fixed so that every later count has a known answer. The data is made the same way every time it is reset.

## What it must not do

- Hold any real person's data. Every screen says "Invented data, Progressa is fictional".
- Connect to anything outside your computer. Other bodies, if the project needs them, are simulated.
- Open a window on its own. Every check of the screens runs without one.

## What it delivers

1. The working prototype, on your computer, with its checks passing.
2. A one-page note to the Permanent Secretary: what the prototype shows, and what it does not.

## The rounds, in order

One piece of work at a time. Each is an instruction, a work session, a review and your ruling.

| # | Piece of work | Kind |
|---|---|---|
| 1 | The register of requirements: what the registry must do, numbered, each with a test | drafting |
| 2 | The groundwork: the tables the build reads (the lists, the settings above, the search rule) | drafting |
| 3 | The goal written in full: every step of enrolling a learner, and every way it can go wrong | drafting |
| 4 | The count: every requirement against the goal, both ways | checking |
| 5 | The scaffold and the made-up data, in the known numbers above | building |
| 6 | The goal built | building |
| 7 | The duplicates count: how many of the 8 the search catches | checking |
| 8 | The note to the Permanent Secretary | drafting |

The project's setup writes its constants before round 1.
