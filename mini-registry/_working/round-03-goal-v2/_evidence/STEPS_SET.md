# The steps of enrolling a learner, listed source first

Written by `inventory.py` from the dispositions of 118 units of the sources; each member's sources are the units that carry it.

| Step | What it is | Sources |
|---|---|---|
| S-1 | The clerk opens the enrolment screen: an entry for each of family name, given names, date of birth and school, the school chosen from the data's 3; enrolment is the only thing the screens offer, and there is no screen for looking learners up. | brief:11 · R-02 · R-03 · ruling:G-07 · ruling:G-08 · groundwork:settings.csv:18 |
| S-2 | The clerk enters the family name, the given names and the date of birth (as YYYY-MM-DD), chooses the school, and submits; the search runs after all four are entered. | brief:11 · R-03 · ruling:G-07 · groundwork:search_rule.csv:10 · groundwork:settings.csv:17 |
| S-3 | The registry holds the date of birth to the form YYYY-MM-DD and refuses any other form; where this falls against the search is not settled. | ruling:G-07 · groundwork:settings.csv:17 |
| S-4 | The registry searches first, after all four are entered, among learners only, comparing family name, given names and date of birth, capitals ignored and nothing else forgiven; the school and every other field not compared; the key table not read. | brief:11 · brief:13 · brief:14 · R-04 · R-05 · ruling:G-03 · ruling:G-05 · ruling:G-07 · groundwork:search_rule.csv:2 · groundwork:search_rule.csv:3 · groundwork:search_rule.csv:4 · groundwork:search_rule.csv:5 · groundwork:search_rule.csv:6 · groundwork:search_rule.csv:7 · groundwork:search_rule.csv:8 · groundwork:search_rule.csv:9 · groundwork:search_rule.csv:10 · groundwork:search_rule.csv:11 · groundwork:search_rule.csv:12 · groundwork:search_rule.csv:16 |
| S-5 | Exactly one learner found: the registry shows that learner and enters nothing new. | brief:13 · R-05 · groundwork:search_rule.csv:14 |
| S-6 | None found: the registry gives the child a new learner number (in sequence, one above the highest held, never given twice, 1 where none is held) and saves the record of the four entries as entered. | brief:14 · R-03 · R-06 · ruling:G-01 · ruling:Q-4 · groundwork:lists.csv:11 · groundwork:lists.csv:12 · groundwork:lists.csv:13 · groundwork:lists.csv:14 · groundwork:lists.csv:15 · groundwork:search_rule.csv:15 · groundwork:settings.csv:9 |
| S-7 | The clerk sees which of the two happened: an existing learner found and shown, or a new learner number given and shown; the two screens say different things. | brief:15 · R-05 · R-07 · groundwork:search_rule.csv:18 |
