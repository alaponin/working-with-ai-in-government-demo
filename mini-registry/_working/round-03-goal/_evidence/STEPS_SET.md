# The set of steps of enrolling a learner

Listed by `list_sets.py`; every source checked at its line by `sources.py` (a ruling at its paper's ruled lines only).

| id | step | source |
|---|---|---|
| S-1 | the clerk opens the enrolment screen: an entry for each of family name, given names, date of birth and school, the school a choice among the data's 3; enrolment is the only goal the screens offer, and there is no screen for looking learners up | brief:11 · R-02 · R-03 · ruling:G-07 · ruling:G-08 · groundwork:settings.csv:18 |
| S-2 | the clerk enters the family name, the given names and the date of birth as YYYY-MM-DD, chooses the school, and submits | brief:11 · R-03 · ruling:G-07 · groundwork:settings.csv:17 · groundwork:search_rule.csv:10 |
| S-3 | the registry takes the entry to the search only when all four are entered, the date in the form YYYY-MM-DD and the school one of the 3; any other date form is refused | ruling:G-07 · groundwork:settings.csv:17 · groundwork:settings.csv:18 · groundwork:search_rule.csv:10 |
| S-4 | the registry searches first, before it does anything else with the entry, among learners only, on family name, given names and date of birth, capitals ignored and nothing else forgiven; the school and every other field not compared; the key table not read | brief:11 · brief:13 · R-04 · R-05 · ruling:G-03 · ruling:G-05 · groundwork:search_rule.csv:2 · groundwork:search_rule.csv:3 · groundwork:search_rule.csv:4 · groundwork:search_rule.csv:5 · groundwork:search_rule.csv:6 · groundwork:search_rule.csv:7 · groundwork:search_rule.csv:8 · groundwork:search_rule.csv:9 · groundwork:search_rule.csv:11 · groundwork:search_rule.csv:12 |
| S-5 | exactly one learner found: the registry shows that learner and enters nothing new | brief:13 · R-05 · groundwork:search_rule.csv:14 |
| S-6 | none found: the registry gives the child a new learner number, a whole number in sequence, one higher than the highest held, never given twice, 1 where none is held, and saves the record of the four entries as entered with that number | brief:14 · R-06 · R-03 · ruling:G-01 · ruling:Q-4 · groundwork:settings.csv:9 · groundwork:search_rule.csv:15 · groundwork:lists.csv:11 · groundwork:lists.csv:12 · groundwork:lists.csv:13 · groundwork:lists.csv:14 · groundwork:lists.csv:15 |
| S-7 | the clerk sees which of the two happened: an existing learner found, shown with its learner number; or a new learner number given, shown | brief:15 · R-07 · R-05 · groundwork:search_rule.csv:18 |
