# The set of failures of enrolling a learner

Listed by `list_sets.py`; every source checked at its line by `sources.py` (a ruling at its paper's ruled lines only).

| id | at step | what sets it off | what the clerk sees | what is saved | source |
|---|---|---|---|---|---|
| F-1 | S-3 | one or more of the four entries not made | the entry refused; the search does not run | nothing | brief:11 · ruling:G-07 · ruling:G-09 · groundwork:search_rule.csv:10 |
| F-2 | S-3 | the date of birth not in the form YYYY-MM-DD | the entry refused; the search does not run | nothing | ruling:G-07 · ruling:G-09 · groundwork:settings.csv:17 |
| F-3 | S-3 | a school not among the data's 3 | the entry refused; the search does not run | nothing | brief:24 · ruling:G-07 · ruling:G-09 · groundwork:settings.csv:18 |
| F-4 | S-4 | the search finds more than one learner | that the entry cannot be completed | nothing new; never reached under the data's settings | ruling:G-02 · ruling:G-09 · ruling:Q-14 · groundwork:search_rule.csv:16 · groundwork:search_rule.csv:17 · groundwork:settings.csv:13 |
| F-5 | S-4 | a child the registry holds, entered with family name, given names or date of birth differing from its learner's in anything but capitals (a family name spelt differently by one letter among them) | the screen of a new learner, as for a child not held | a second learner for the same child, with a new learner number (S-6); 4 of the data's 8 children on more than one list are missed so | brief:7 · brief:13 · R-06 · ruling:G-05 · groundwork:search_rule.csv:6 · groundwork:settings.csv:14 |
