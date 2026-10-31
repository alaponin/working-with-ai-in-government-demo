# The groundwork — the mini registry

**What this is.** The tables the build reads: the settings, the structure of the lists, and the search rule. They are round 2 of the brief. They describe; they make no data. Round 5 makes the made-up data from them, and round 6 builds the goal on them.

**Where it comes from.** Three sources, in order of precedence: the brief (`../brief/MINI-REGISTRY-BRIEF.md`), the register of requirements (`docs/REQUIREMENTS.md`, R-01 to R-23), and the owner's ruling of 31 October 2026 on the thirteen recommendations of `docs/GAPS-PAPER.md` (decision D-2026-10-31-03). Of that paper, only the thirteen summary rows and the one-sentence recommendation closing each question's section are ruled. Every row of every table names its source in its own `source` column, as `brief:<line>`, `R-<nn>` or `ruling:G-<nn>`. A fact none of the three gives is not a row; it is a question in the closing section.

## The settings — `docs/groundwork/settings.csv`

**What it is for.** The values the build is held to: the five known numbers of the brief, and the values the ruling fixes about them — the count of list entries, how the 8 lie over the lists, what "spelt differently" means, how ages are reckoned, the form of a learner number and of the entries.

**Who reads it.** Round 5, which makes the made-up data to these numbers and checks them after every reset; round 6, which builds the learner number and the entry form; round 7, which holds its count against the known answer of 4 of the 8.

**Its sources.** The five known numbers rest on the brief's table, lines 23 to 27, with the register's tests R-09 to R-14; every further row rests on the ruling, G-01 and G-04 to G-07.

## The lists — `docs/groundwork/lists.csv`

**What it is for.** The structure of each table the prototype holds: the three lists (the school census, the examinations authority's candidate list, the social grant programme's list), the learners, and the key table that records which entries are the same child. The three lists are data inside the prototype, not bodies it connects to (the ruling on G-11).

**Who reads it.** Round 5, which fills the tables; round 6, which reads and writes the learners; round 7, which counts the 8 against the key table.

**Its sources.** The fields of the three lists rest on the brief's lines 13, 19 and 26 and on the ruling on G-03, under which the reset enrols every list entry by the brief's rule; the learners' fields on the brief's lines 11 and 14 and R-03; the key table on R-11 and the ruling on G-05. **The key table is read by the counts only.** No row of the search rule reads it, and nothing in this file gives the search access to it.

## The search rule — `docs/groundwork/search_rule.csv`

**What it is for.** Everything the search does, one row each: what it compares, what it forgives, what it does not compare or read, when it runs, where it looks, what the reset does with it, and what follows on none, on exactly one and on more than one.

**Who reads it.** Round 3, which writes the goal in full from it; round 6, which builds it; round 7, which counts what it catches.

**Its sources.** What it compares and forgives is the brief's line 13 alone: family name, given names and date of birth, capitals ignored, and nothing else forgiven; the outcomes are lines 13 to 15, with the ruling on G-02 for more than one; where it looks and the reset's enrolment are the ruling on G-03; when it runs is line 11 with the ruling on G-07.

## Requirements the tables do not bear on

Of the register's sections "What it must do" and "The made-up data, in known numbers", one requirement is cited by no row:

- **R-02** — the one goal. It is a matter of the screens the clerk is offered (the ruling on G-08), which round 3 writes and round 6 builds; no setting, field or step of the search carries it.

The ruling's answers to G-08 to G-13 likewise fix no value, field or step of these tables: they bear on the screens (G-08, G-09), the evidence for R-16 (G-10), the bodies of R-19 (G-11), the checks of R-22 (G-12) and the note of R-23 (G-13).

## Gaps against the sources

Each is a fact the build will need that none of the three sources gives. Each is left open, and no table answers it.

1. **The date ages are reckoned on.** The ruling on G-06 holds ages to "one fixed date held in round 2's settings", and gives no date: what is that date?
2. **The order of the reset's enrolment.** The ruling on G-03 has the reset enrol every list entry "in a fixed order", and does not give it: in what order are the three lists, and the entries within each list, enrolled?
3. **The seed.** The ruling on G-10 makes the data "from invented name parts and a fixed seed", and gives no seed: what is the seed?
4. **The first learner number.** The ruling on G-01 gives each new learner "one higher than the highest the registry holds": what number is given when the registry holds none?
5. **Which lists carry the 8.** The ruling on G-04 puts each of the 8 on exactly two lists: which two lists carry each of them, and on which of its two lists is each of the 4 spelt differently?
6. **The spread over the lists.** The ruling on G-04 fixes 68 entries in all: how many entries does each of the three lists hold?
7. **The spread over the schools.** The brief fixes 3 schools: how are the 60 children spread over them?
8. **The other fields of the 4.** The ruling on G-05 says "the 4 differ in at least one letter" and "the other 4 match letter for letter and in the same capitals": do the given names and the date of birth of the 4 also match on both their lists, and does the other 4's match cover all three of the fields the search compares?
9. **A school on the lists.** The learner's record holds a school (R-03), and the reset makes learners from list entries (the ruling on G-03): which of the three lists carry a school, and what school does a learner made at reset from an entry with none hold?
10. **The form of a date on the lists.** The ruling on G-07 fixes the form the clerk enters, YYYY-MM-DD: in what form do the three lists hold a date of birth?
11. **The key table's keys.** The ruling on G-05 gives a key table read by the counts: how does it name a list entry, in what form does it name the child, and does it hold every one of the 68 entries or only those of the 8?
12. **A learner and the entries it came from.** Round 7 counts how many of the 8 the search catches (the brief's line 54), against the key table, which names list entries, while the search makes learners: does a learner record the list entries the reset enrolled into it, and if so, by what field — which no source names?
13. **The learners after reset.** The paper's line 40 gives 64 learners after reset, and that line is not ruled: is the number of learners after reset a setting the build is held to, and what is it?
14. **Capitals in "share".** The ruling on G-05 says "no two different children share all three fields", and does not say whether capitals are ignored in "share"; the brief's line 13 compares "the same family name, given names and date of birth (capitals ignored)", and under the ruling on G-03 the reset enrols every list entry "through the brief's own rule", so two different children who differ in capitals only would be merged into one learner: may two different children differ in capitals only, or do no two different children share all three fields with capitals ignored?
