"""List the set of steps and the set of failures of enrolling a learner, each from its sources.

Every source token of every member carries a fragment that must stand at the line(s) the token
resolves to (sources.py): for a ruling, only at the ruled lines of its paper. A member whose every
token is not found is printed and counted. Writes STEPS_SET.md and FAILURES_SET.md beside itself.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sources import found  # noqa: E402

E = Path(__file__).parent

STEPS = [
    ('S-1', 'the clerk opens the enrolment screen: an entry for each of family name, given names, date of birth and school, the school a choice among the data\'s 3; enrolment is the only goal the screens offer, and there is no screen for looking learners up', {
        'brief:11': 'One goal: **enrol a learner.**',
        'R-02': 'The prototype has one goal: to enrol a learner.',
        'R-03': 'the screen offers an entry for each of the four',
        'ruling:G-07': 'school chosen from the three',
        'ruling:G-08': 'there is no screen for looking learners up',
        'groundwork:settings.csv:18': "chosen from the data's 3 schools"}),
    ('S-2', 'the clerk enters the family name, the given names and the date of birth as YYYY-MM-DD, chooses the school, and submits', {
        'brief:11': "A school clerk enters a child's family name, given names, date of birth and school.",
        'R-03': 'submit',
        'ruling:G-07': 'Date as YYYY-MM-DD',
        'groundwork:settings.csv:17': 'YYYY-MM-DD',
        'groundwork:search_rule.csv:10': 'after the clerk has entered all four'}),
    ('S-3', 'the registry takes the entry to the search only when all four are entered, the date in the form YYYY-MM-DD and the school one of the 3; any other date form is refused', {
        'ruling:G-07': 'all four entered before the search',
        'groundwork:settings.csv:17': 'any other form refused',
        'groundwork:settings.csv:18': "chosen from the data's 3 schools",
        'groundwork:search_rule.csv:10': 'after the clerk has entered all four'}),
    ('S-4', 'the registry searches first, before it does anything else with the entry, among learners only, on family name, given names and date of birth, capitals ignored and nothing else forgiven; the school and every other field not compared; the key table not read', {
        'brief:11': 'The registry searches for the child first',
        'brief:13': '(capitals ignored)',
        'R-04': 'the search is the first act on the data, before any write',
        'R-05': 'capitals ignored',
        'ruling:G-03': 'the search then looks among learners only',
        'ruling:G-05': 'never by the search',
        'groundwork:search_rule.csv:2': 'compares,family name',
        'groundwork:search_rule.csv:3': 'compares,given names',
        'groundwork:search_rule.csv:4': 'compares,date of birth',
        'groundwork:search_rule.csv:5': 'capitals: two values that differ in capitals only are the same',
        'groundwork:search_rule.csv:6': 'every difference but capitals makes two values differ',
        'groundwork:search_rule.csv:7': 'school: entered and saved, never searched on',
        'groundwork:search_rule.csv:8': 'any field but the three compared',
        'groundwork:search_rule.csv:9': 'does_not_read,the key table',
        'groundwork:search_rule.csv:11': 'first: before the registry does anything else with the entry',
        'groundwork:search_rule.csv:12': 'where,among learners only'}),
    ('S-5', 'exactly one learner found: the registry shows that learner and enters nothing new', {
        'brief:13': 'it shows that learner and enters nothing new',
        'R-05': 'the registry shows that learner and enters nothing new',
        'groundwork:search_rule.csv:14': 'shows that learner and enters nothing new'}),
    ('S-6', 'none found: the registry gives the child a new learner number, a whole number in sequence, one higher than the highest held, never given twice, 1 where none is held, and saves the record of the four entries as entered with that number', {
        'brief:14': 'it gives the child a new learner number and saves the record',
        'R-06': 'gives the child a new learner number and saves the record',
        'R-03': 'the record saved holds F, G, D and S as entered',
        'ruling:G-01': 'one above the highest held, never given twice',
        'ruling:Q-4': 'we recommend 1',
        'groundwork:settings.csv:9': 'one higher than the highest held',
        'groundwork:search_rule.csv:15': 'gives the child a new learner number',
        'groundwork:lists.csv:11': 'learners,learner_number',
        'groundwork:lists.csv:12': 'learners,family_name',
        'groundwork:lists.csv:13': 'learners,given_names',
        'groundwork:lists.csv:14': 'learners,date_of_birth',
        'groundwork:lists.csv:15': 'learners,school'}),
    ('S-7', 'the clerk sees which of the two happened: an existing learner found, shown with its learner number; or a new learner number given, shown', {
        'brief:15': 'the clerk sees which of the two happened',
        'R-07': 'the first screen says that a new learner number was given, and shows it',
        'R-05': 'with its learner number',
        'groundwork:search_rule.csv:18': 'the clerk sees which of the two happened'}),
]

FAILURES = [
    ('F-1', 'S-3', 'one or more of the four entries not made', 'the entry refused; the search does not run', 'nothing', {
        'brief:11': 'family name, given names, date of birth and school',
        'ruling:G-07': 'all four entered before the search',
        'ruling:G-09': 'messages and refusals included',
        'groundwork:search_rule.csv:10': 'after the clerk has entered all four'}),
    ('F-2', 'S-3', 'the date of birth not in the form YYYY-MM-DD', 'the entry refused; the search does not run', 'nothing', {
        'ruling:G-07': 'refused otherwise',
        'ruling:G-09': 'messages and refusals included',
        'groundwork:settings.csv:17': 'any other form refused'}),
    ('F-3', 'S-3', 'a school not among the data\'s 3', 'the entry refused; the search does not run', 'nothing', {
        'brief:24': '| Schools | 3 |',
        'ruling:G-07': 'school chosen from the three',
        'ruling:G-09': 'messages and refusals included',
        'groundwork:settings.csv:18': "chosen from the data's 3 schools"}),
    ('F-4', 'S-4', 'the search finds more than one learner', 'that the entry cannot be completed', 'nothing new; never reached under the data\'s settings', {
        'ruling:G-02': 'says the entry cannot be completed',
        'ruling:G-09': 'messages and refusals included',
        'ruling:Q-14': 'ignore capitals',
        'groundwork:search_rule.csv:16': 'enters nothing new and says the entry cannot be completed',
        'groundwork:search_rule.csv:17': "never reached under the data's settings",
        'groundwork:settings.csv:13': 'different_children_sharing_family_name_given_names_and_date_of_birth,0'}),
    ('F-5', 'S-4', 'a child the registry holds, entered with family name, given names or date of birth differing from its learner\'s in anything but capitals (a family name spelt differently by one letter among them)', 'the screen of a new learner, as for a child not held', 'a second learner for the same child, with a new learner number (S-6); 4 of the data\'s 8 children on more than one list are missed so', {
        'brief:7': 'the registry does not register the same child twice',
        'brief:13': '(capitals ignored)',
        'R-06': 'differs from it by one letter, not by capitals alone',
        'ruling:G-05': '4 of the 8 caught',
        'groundwork:search_rule.csv:6': 'every difference but capitals makes two values differ',
        'groundwork:settings.csv:14': 'of_the_8_caught_by_the_search,4'}),
]


def check(anchors):
    bad = []
    for tok, frag in anchors.items():
        ok, where = found(tok, frag)
        if not ok:
            bad.append('%s «%s»: %s' % (tok, frag, where))
    return bad


def src(anchors):
    return ' · '.join(anchors)


def main():
    nbad = 0
    out = ['# The set of steps of enrolling a learner', '',
           'Listed by `list_sets.py`; every source checked at its line by `sources.py` (a ruling at its paper\'s ruled lines only).', '',
           '| id | step | source |', '|---|---|---|']
    for sid, text, anchors in STEPS:
        bad = check(anchors)
        nbad += len(bad)
        for b in bad:
            print('NOT FOUND', sid, b)
        out.append('| %s | %s | %s |' % (sid, text, src(anchors)))
    (E / 'STEPS_SET.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    out = ['# The set of failures of enrolling a learner', '',
           'Listed by `list_sets.py`; every source checked at its line by `sources.py` (a ruling at its paper\'s ruled lines only).', '',
           '| id | at step | what sets it off | what the clerk sees | what is saved | source |', '|---|---|---|---|---|---|']
    for fid, step, trig, sees, saved, anchors in FAILURES:
        bad = check(anchors)
        nbad += len(bad)
        for b in bad:
            print('NOT FOUND', fid, b)
        out.append('| %s | %s | %s | %s | %s | %s |' % (fid, step, trig, sees, saved, src(anchors)))
    (E / 'FAILURES_SET.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    na = sum(len(a) for *_, a in STEPS) + sum(len(a) for *_, a in FAILURES)
    print('steps: %d; failures: %d; sources checked: %d; not found: %d' % (len(STEPS), len(FAILURES), na, nbad))
    return 1 if nbad else 0


if __name__ == '__main__':
    sys.exit(main())
