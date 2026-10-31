"""A11: every fact of every step's "The clerk" and "The registry" and every failure's "What sets it off",
"What the clerk sees" and "What is saved", set beside the words of its source that carry that very
fact, or the gap that holds it open.

Each fact is a phrase that must stand word for word in that field of docs/GOAL.md. It carries:
  - quotations (token, words): the words must stand whole on a line the token resolves to (a ruling
    only at its ruled lines, sources.py), and the token must be among the member's own sources;
  - ('gap', n): gap n must exist in the goal's closing section;
  - ('absence',): the phrase says that the sources give nothing here (allowed only in a step's
    "The clerk" or "The registry", where it states that no act is given);
  - ('ref', 'S-n'): the phrase sends the reader to another step, which carries the fact.
A field is quoted when every phrase is found and carried, and its phrases cover the field's facts:
the program prints each field's text beside its phrases so that the cover can be read. Writes
QUOTES.md beside itself; prints `<n> unquoted`.
"""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sources import quote  # noqa: E402

E = Path(__file__).parent
GOAL = Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md')

G07 = 'ruling:G-07'
SR = 'groundwork:search_rule.csv:'
ST = 'groundwork:settings.csv:'
LI = 'groundwork:lists.csv:'
G09_VIEW = ('ruling:G-09', 'Every view the clerk can see is a screen, messages and refusals included')

FACTS = {
    'S-1': {
        'The clerk': [
            ('opens the enrolment screen', [('R-03', 'open the enrolment screen')]),
            ('sees an entry for each of the four: family name, given names, date of birth and school',
             [('R-03', 'the screen offers an entry for each of the four — family name, given names, date of birth, school')]),
            ("the school chosen from the data's 3 schools",
             [(G07, "the school chosen from the data's three"), (ST + '18', "chosen from the data's 3 schools")]),
        ],
        'The registry': [
            ("offers enrolment as the only thing the clerk's screens offer",
             [('ruling:G-08', "enrolment is the only thing the clerk's screens offer"),
              ('R-02', 'The prototype has one goal: to enrol a learner.'), ('brief:11', 'One goal: **enrol a learner.**')]),
            ('there is no screen for looking learners up', [('ruling:G-08', 'there is no screen for looking learners up')]),
        ],
    },
    'S-2': {
        'The clerk': [
            ('enters the family name, the given names and the date of birth',
             [('brief:11', "A school clerk enters a child's family name, given names, date of birth and school.")]),
            ('the date as YYYY-MM-DD', [(G07, 'the date entered as YYYY-MM-DD'), (ST + '17', 'YYYY-MM-DD')]),
            ("chooses the school from the data's 3", [(G07, "the school chosen from the data's three")]),
            ('submits', [('R-03', 'submit.')]),
        ],
        'The registry': [
            ('the sources give it no act at this step', [('absence',)]),
            ('the search runs after the clerk has entered all four',
             [(SR + '10', 'after the clerk has entered all four'), (G07, 'all four entered before the search runs')]),
        ],
    },
    'S-3': {
        'The clerk': [("no act of the clerk's is given at this step", [('absence',)])],
        'The registry': [
            ('holds the date of birth to the form YYYY-MM-DD', [(G07, 'the date entered as YYYY-MM-DD'), (ST + '17', 'YYYY-MM-DD')]),
            ('a date in any other form is refused', [(G07, 'refused otherwise'), (ST + '17', 'any other form refused')]),
            ('Whether this comes before or after the search of S-4 is not settled by the sources', [('gap', 7)]),
        ],
    },
    'S-4': {
        'The clerk': [("no act of the clerk's is given at this step", [('absence',)])],
        'The registry': [
            ('searches after the clerk has entered all four',
             [(SR + '10', 'after the clerk has entered all four'), (G07, 'all four entered before the search runs')]),
            ('and first, before it does anything else with the entry',
             [('brief:11', 'The registry searches for the child first'), ('R-04', 'before it does anything else with the entry'),
              (SR + '11', 'first: before the registry does anything else with the entry')]),
            ('before any write', [('R-04', 'the search is the first act on the data, before any write')]),
            ('against S-3, gap 7', [('gap', 7)]),
            ('it looks among learners only',
             [('ruling:G-03', "the clerk's search then looks among learners only"), (SR + '12', 'where,among learners only')]),
            ('it compares the family name, the given names and the date of birth',
             [(SR + '2', 'compares,family name'), (SR + '3', 'compares,given names'), (SR + '4', 'compares,date of birth'),
              ('brief:13', 'the same family name, given names and date of birth')]),
            ('two values that differ in capitals only are the same',
             [(SR + '5', 'two values that differ in capitals only are the same'), ('brief:13', '(capitals ignored)'),
              ('R-05', 'capitals ignored')]),
            ('every difference but capitals makes two values differ',
             [(SR + '6', 'every difference but capitals makes two values differ')]),
            ('it does not compare the school, which is entered and saved and never searched on',
             [(SR + '7', 'school: entered and saved, never searched on'), (G07, 'the school not searched on')]),
            ('nor any field but the three', [(SR + '8', 'does_not_compare,any field but the three compared')]),
            ('it does not read the key table',
             [(SR + '9', 'does_not_read,the key table'), ('ruling:G-05', 'read by the counts and never by the search')]),
            ('If it finds exactly one learner the goal goes on at S-5', [('brief:13', 'if it finds exactly one learner')]),
            ('if it finds none, at S-6', [('brief:14', 'if it finds none')]),
            ('on more than one, at F-4', [(SR + '16', 'on_more_than_one')]),
        ],
    },
    'S-5': {
        'The clerk': [('sees the result at S-7', [('ref', 'S-7')])],
        'The registry': [
            ('shows that learner and enters nothing new',
             [('brief:13', 'it shows that learner and enters nothing new'),
              ('R-05', 'the registry shows that learner and enters nothing new'),
              (SR + '14', 'on_exactly_one,shows that learner and enters nothing new')]),
        ],
    },
    'S-6': {
        'The clerk': [('sees the result at S-7', [('ref', 'S-7')])],
        'The registry': [
            ('gives the child a new learner number', [('brief:14', 'it gives the child a new learner number'),
                                                      ('R-06', 'the registry gives the child a new learner number')]),
            ('a whole number in sequence, one higher than the highest the registry holds, never given twice',
             [('ruling:G-01', 'a whole number given in sequence, one higher than the highest the registry holds, never given twice'),
              (ST + '9', 'a whole number in sequence, one higher than the highest held, never given twice')]),
            ('and 1 as the first', [('ruling:Q-4', 'Any first number serves; we recommend 1')]),
            ('saves the record', [('brief:14', 'saves the record'), (SR + '15', 'saves the record')]),
            ('the family name, given names, date of birth and school as entered',
             [('R-03', 'the record saved holds F, G, D and S as entered'),
              (LI + '12', 'the family name as entered by the clerk'), (LI + '13', 'the given names as entered by the clerk'),
              (LI + '14', 'the date of birth as entered by the clerk'), (LI + '15', 'the school as chosen by the clerk')]),
            ('with that learner number', [(LI + '11', 'learners,learner_number'),
                                          ('R-06', 'holding the entries made and a learner number that no learner held before')]),
        ],
    },
    'S-7': {
        'The clerk': [
            ('sees which of the two happened', [('brief:15', 'the clerk sees which of the two happened')]),
            ('on SC-2, that an existing learner was found, and that learner',
             [('R-07', 'the second says that an existing learner was found, and shows that learner')]),
            ('with its learner number', [('R-05', 'the screen shows the learner saved in the set-up, with its learner number')]),
            ('on SC-3, that a new learner number was given, and that number',
             [('R-07', 'the first screen says that a new learner number was given, and shows it')]),
            ('The two screens say different things', [('R-07', 'the two screens say different things')]),
        ],
        'The registry': [
            ('shows the screen of what happened, SC-2 or SC-3',
             [(SR + '18', 'tells,the clerk sees which of the two happened'), ('R-07', 'Pass if each screen says which of the two happened')]),
        ],
    },
    'F-1': {
        'What sets it off': [
            ('one or more of the four — family name, given names, date of birth, school — not entered',
             [(G07, 'all four entered before the search runs'),
              (SR + '10', 'after the clerk has entered all four: family name, given names, date of birth and school')]),
        ],
        'What the clerk sees': [
            ('not given by the sources', [('gap', 5)]),
            ('which say only that the search does not run until all four are entered',
             [(G07, 'all four entered before the search runs'), (SR + '10', 'after the clerk has entered all four')]),
        ],
        'What is saved': [
            ('no record', [('brief:14', 'if it finds none, it gives the child a new learner number and saves the record'),
                           (G07, 'all four entered before the search runs')]),
            ('the one save the sources give follows the search finding none',
             [('brief:14', 'if it finds none, it gives the child a new learner number and saves the record')]),
            ('and the search has not run', [(G07, 'all four entered before the search runs')]),
        ],
    },
    'F-2': {
        'What sets it off': [
            ('a date of birth not in the form YYYY-MM-DD',
             [(G07, 'the date entered as YYYY-MM-DD and refused otherwise'), (ST + '17', 'YYYY-MM-DD; any other form refused')]),
        ],
        'What the clerk sees': [
            ('SC-4', [G09_VIEW]),
            ('the date of birth is refused', [(G07, 'refused otherwise'), (ST + '17', 'any other form refused')]),
        ],
        'What is saved': [
            ('not settled by the sources', [('gap', 7)]),
            ('the date is refused', [(G07, 'refused otherwise')]),
            ('whether the search runs before the refusal, and so whether a record could be saved, is gap 7', [('gap', 7)]),
        ],
    },
    'F-3': {
        'What sets it off': [
            ("a school that is not one of the data's 3 schools",
             [('brief:24', '| Schools | 3 |'), (ST + '18', "chosen from the data's 3 schools")]),
            ("The sources say only that the school is chosen from the data's 3",
             [(G07, "the school chosen from the data's three"), (ST + '18', "school_entry,chosen from the data's 3 schools")]),
            ('whether such a school can reach the registry at all is gap 6', [('gap', 6)]),
        ],
        'What the clerk sees': [('not given by the sources (gap 6)', [('gap', 6)])],
        'What is saved': [('not given by the sources (gap 6)', [('gap', 6)])],
    },
    'F-4': {
        'What sets it off': [
            ('the search of S-4 finds more than one learner', [(SR + '16', 'on_more_than_one')]),
            ("Under the data's settings it is never reached",
             [('ruling:G-02', "Never reached under the data's settings"), (SR + '17', "never reached under the data's settings")]),
            ('no two different children share all three fields',
             [('ruling:G-05', 'no two different children share all three fields'),
              (ST + '13', 'different_children_sharing_family_name_given_names_and_date_of_birth,0')]),
            ('"share" ignores capitals', [('ruling:Q-14', 'We recommend that "share" ignore capitals, as the search does.')]),
        ],
        'What the clerk sees': [
            ('SC-5', [G09_VIEW]),
            ('the entry is refused', [('ruling:G-02', 'refuse the entry')]),
            ('the registry says the entry cannot be completed',
             [('ruling:G-02', 'says the entry cannot be completed'), (SR + '16', 'says the entry cannot be completed')]),
        ],
        'What is saved': [
            ('nothing new', [('ruling:G-02', 'the registry enters nothing new'), (SR + '16', 'enters nothing new')]),
        ],
    },
    'F-5': {
        'What sets it off': [
            ("a child the registry already holds as a learner is entered with a family name, given names or date of birth that differs from that learner's in anything but capitals",
             [(SR + '6', 'every difference but capitals makes two values differ'), ('brief:13', '(capitals ignored)')]),
            ('a family name that differs by one letter among them',
             [('R-06', 'a family name that differs from it by one letter, not by capitals alone')]),
            ('The search finds none', [(SR + '5', 'two values that differ in capitals only are the same'),
                                       (SR + '6', 'every difference but capitals makes two values differ')]),
        ],
        'What the clerk sees': [
            ('SC-3, the screen of a new learner', [('brief:14', 'if it finds none'),
                                                   ('R-07', 'the first screen says that a new learner number was given, and shows it')]),
            ('that a new learner number was given, and that number',
             [('R-07', 'the first screen says that a new learner number was given, and shows it')]),
        ],
        'What is saved': [
            ('a second record for the same child, with a new learner number',
             [('brief:14', 'it gives the child a new learner number and saves the record'),
              ('R-06', 'one record is saved, holding the entries made and a learner number that no learner held before')]),
            ('so that the registry registers the same child twice',
             [('brief:7', 'the registry does not register the same child twice'),
              ('R-01', 'the registry does not register the same child twice')]),
            ("of the data's 8 children on more than one list, the search catches 4",
             [(ST + '14', 'of_the_8_caught_by_the_search,4'), ('ruling:G-05', '4 of the 8 caught')]),
        ],
    },
}

STEP_FIELDS = ('The clerk', 'The registry')
FAIL_FIELDS = ('What sets it off', 'What the clerk sees', 'What is saved')


def blocks(text, prefix):
    out, cur = {}, None
    for l in text.split('\n'):
        m = re.match(r'### (%s-\d+) ' % prefix, l)
        if m:
            cur = m.group(1)
            out[cur] = []
            continue
        if l.startswith('## ') or l.startswith('### ') or l.startswith('---'):
            cur = None
        if cur:
            out[cur].append(l)
    return out


def field(block, name):
    for l in block:
        if l.startswith('- **%s:**' % name):
            return l.split(':**', 1)[1].strip()
    return None


def main():
    text = GOAL.read_text(encoding='utf-8')
    head, _, gaps = text.partition('\n## Gaps against the sources')
    gap_nums = {int(n) for n in re.findall(r'^(\d+)\. ', gaps, re.M)}
    members = {**blocks(head, 'S'), **blocks(head, 'F')}
    rows, unquoted, quotes_n, gaps_n, problems = [], 0, 0, 0, []
    for m, b in members.items():
        own = set(t.strip() for t in (field(b, 'Source') or '').split(' · '))
        names = STEP_FIELDS if m.startswith('S') else FAIL_FIELDS
        cells = []
        for fname in names:
            ftext = field(b, fname)
            facts = FACTS.get(m, {}).get(fname)
            bad = []
            if not ftext or not facts:
                bad.append('no field' if not ftext else 'no facts listed')
                facts = facts or []
            parts = []
            for phrase, carriers in facts:
                if phrase not in (ftext or ''):
                    bad.append('phrase not in the field: %r' % phrase)
                said = []
                for c in carriers:
                    if c[0] == 'gap':
                        gaps_n += 1
                        said.append('gap G-%d' % c[1])
                        if c[1] not in gap_nums:
                            bad.append('gap %d absent' % c[1])
                    elif c[0] == 'absence':
                        said.append('none given (a statement that the sources give no act)')
                        if m.startswith('F'):
                            bad.append('absence used in a failure')
                    elif c[0] == 'ref':
                        said.append('see %s' % c[1])
                        if c[1] not in members:
                            bad.append('ref to no member %s' % c[1])
                    else:
                        tok, words = c
                        quotes_n += 1
                        p, at = quote(tok, words)
                        if tok not in own:
                            bad.append('%s not among %s\'s sources' % (tok, m))
                        if p is None:
                            bad.append('%s: %s %r' % (tok, at, words))
                        else:
                            said.append('`%s` «%s» (%s:%d)' % (tok, words, p.name, at))
                parts.append('*%s* ← %s' % (phrase, '; '.join(said)))
            ok = not bad
            unquoted += not ok
            if bad:
                problems.append('%s %s: %s' % (m, fname, ' | '.join(bad)))
            cells.append('**%s:** %s<br>%s' % (fname, ftext, '<br>'.join(parts)))
        rows.append('| %s | %s |' % (m, ' <br><br> '.join(cells)))
    out = ('# A11 — every fact beside the source words that carry it\n\n'
           'Written by `quotes.py` from `docs/GOAL.md`. One row per step and per failure; in each, every field the test names, '
           'its text in the goal, and each of its facts with the words of its source that carry it, or the gap that holds it open.\n\n'
           '| Member | Fields, their facts and the words that carry them |\n|---|---|\n' + '\n'.join(rows) + '\n')
    (E / 'QUOTES.md').write_text(out, encoding='utf-8')
    fields_n = sum(len(STEP_FIELDS if m.startswith('S') else FAIL_FIELDS) for m in members)
    print('members: %d (steps %d, failures %d); fields: %d; quotations: %d, every one found at its source: %s; gap references: %d'
          % (len(members), sum(1 for m in members if m.startswith('S')), sum(1 for m in members if m.startswith('F')),
             fields_n, quotes_n, not any(':' in p and 'words not' in p for p in problems), gaps_n))
    for p in problems:
        print('  ' + p)
    print('%d unquoted' % unquoted)


if __name__ == '__main__':
    main()
