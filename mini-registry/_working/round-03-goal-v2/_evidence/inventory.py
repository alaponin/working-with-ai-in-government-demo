"""The sets of round 3, version 2, listed source first.

Every unit of the sources in scope is enumerated from the files themselves:
  - each non-empty line of the brief's five sections (lines 5 to 40), headings and table rules left out;
  - each of R-01 to R-23 (the register's ### sections);
  - each ruled unit of G-01 to G-13 (summary row and closing recommendation) and of Q-1 to Q-14
    (closing proposal);
  - each row of the three tables of the groundwork.
Each unit is given a disposition here, by hand: the steps (S-n) and failures (F-n) it carries, SC
where it carries the screens' line, or `none: <why>`. The program stops if a unit enumerated has no
disposition, or a disposition names no unit. Each member's sources are then the units that carry it,
and the two sets are written from them: STEPS_SET.md and FAILURES_SET.md, beside this program.
"""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sources import BRIEF, GW, lines, register_sections, ruled_g, ruled_q, resolve  # noqa: E402

E = Path(__file__).parent

STEPS = {
    'S-1': 'The clerk opens the enrolment screen: an entry for each of family name, given names, date of birth and school, the school chosen from the data\'s 3; enrolment is the only thing the screens offer, and there is no screen for looking learners up.',
    'S-2': 'The clerk enters the family name, the given names and the date of birth (as YYYY-MM-DD), chooses the school, and submits; the search runs after all four are entered.',
    'S-3': 'The registry holds the date of birth to the form YYYY-MM-DD and refuses any other form; where this falls against the search is not settled.',
    'S-4': 'The registry searches first, after all four are entered, among learners only, comparing family name, given names and date of birth, capitals ignored and nothing else forgiven; the school and every other field not compared; the key table not read.',
    'S-5': 'Exactly one learner found: the registry shows that learner and enters nothing new.',
    'S-6': 'None found: the registry gives the child a new learner number (in sequence, one above the highest held, never given twice, 1 where none is held) and saves the record of the four entries as entered.',
    'S-7': 'The clerk sees which of the two happened: an existing learner found and shown, or a new learner number given and shown; the two screens say different things.',
}
FAILURES = {
    'F-1': ('S-2', 'An entry missing: one or more of the four not entered; the search does not run.'),
    'F-2': ('S-3', 'The date of birth in a form other than YYYY-MM-DD: the date is refused.'),
    'F-3': ('S-2', 'A school not among the data\'s 3: the school is chosen from the 3.'),
    'F-4': ('S-4', 'More than one learner found: never reached under the data\'s settings; if reached, nothing new is entered and the registry says the entry cannot be completed.'),
    'F-5': ('S-4', 'The same child not caught: a child already held entered with a field differing in more than capitals is not found, and is saved again with a new learner number.'),
}

N = 'none: '
DATA = N + 'the made-up data or its reset, not a step of enrolment (ruling:G-08: reset is a command outside the screens)'
NOTSTEP = N + 'a constraint on the prototype as a whole, not a step or a way the goal goes wrong'

DISP = {
    # the brief, lines 5 to 40
    'brief:7': ['F-5'],
    'brief:11': ['S-1', 'S-2', 'S-4', 'F-1'],
    'brief:13': ['S-4', 'S-5', 'F-5'],
    'brief:14': ['S-4', 'S-6', 'F-1', 'F-5'],
    'brief:15': ['S-7'],
    'brief:19': DATA, 'brief:21': N + 'table head', 'brief:23': DATA,
    'brief:24': ['F-3'],
    'brief:25': DATA, 'brief:26': DATA, 'brief:27': N + 'ages of the made-up data; an age entered by the clerk is a gap (gap 2)',
    'brief:29': DATA,
    'brief:33': ['SC'],
    'brief:34': NOTSTEP, 'brief:35': NOTSTEP,
    'brief:39': N + 'a deliverable', 'brief:40': N + 'a deliverable',
    # the register
    'R-01': ['F-5'],
    'R-02': ['S-1'],
    'R-03': ['S-1', 'S-2', 'S-6'],
    'R-04': ['S-4'],
    'R-05': ['S-4', 'S-5', 'S-7'],
    'R-06': ['S-6', 'F-5'],
    'R-07': ['S-7', 'F-5'],
    'R-08': DATA, 'R-09': DATA, 'R-10': DATA, 'R-11': DATA, 'R-12': DATA, 'R-13': DATA, 'R-14': DATA, 'R-15': DATA,
    'R-16': NOTSTEP,
    'R-17': ['SC'],
    'R-18': NOTSTEP, 'R-19': NOTSTEP, 'R-20': NOTSTEP, 'R-21': NOTSTEP,
    'R-22': N + 'a deliverable', 'R-23': N + 'a deliverable',
    # the first ruling
    'ruling:G-01': ['S-6'],
    'ruling:G-02': ['F-4'],
    'ruling:G-03': ['S-4'],
    'ruling:G-04': DATA,
    'ruling:G-05': ['S-4', 'F-4', 'F-5'],
    'ruling:G-06': N + 'how ages of the made-up data are reckoned; an age entered by the clerk is a gap (gap 2)',
    'ruling:G-07': ['S-1', 'S-2', 'S-3', 'S-4', 'F-1', 'F-2', 'F-3'],
    'ruling:G-08': ['S-1'],
    'ruling:G-09': ['SC', 'F-2', 'F-4'],
    'ruling:G-10': NOTSTEP, 'ruling:G-11': NOTSTEP,
    'ruling:G-12': N + 'what the prototype\'s checks are; it is why each failure here is named (the goal\'s opening), not a step',
    'ruling:G-13': N + 'a deliverable',
    # the second ruling
    'ruling:Q-1': N + 'the date ages are reckoned on, for the made-up data; an age entered by the clerk is a gap (gap 2)',
    'ruling:Q-2': DATA, 'ruling:Q-3': DATA,
    'ruling:Q-4': ['S-6'],
    'ruling:Q-5': DATA, 'ruling:Q-6': DATA, 'ruling:Q-7': DATA, 'ruling:Q-8': DATA, 'ruling:Q-9': DATA,
    'ruling:Q-10': DATA, 'ruling:Q-11': DATA, 'ruling:Q-12': DATA, 'ruling:Q-13': DATA,
    'ruling:Q-14': ['F-4'],
    # search_rule.csv
    'groundwork:search_rule.csv:2': ['S-4'], 'groundwork:search_rule.csv:3': ['S-4'],
    'groundwork:search_rule.csv:4': ['S-4'], 'groundwork:search_rule.csv:5': ['S-4', 'F-5'],
    'groundwork:search_rule.csv:6': ['S-4', 'F-5'], 'groundwork:search_rule.csv:7': ['S-4'],
    'groundwork:search_rule.csv:8': ['S-4'], 'groundwork:search_rule.csv:9': ['S-4'],
    'groundwork:search_rule.csv:10': ['S-2', 'S-4', 'F-1'],
    'groundwork:search_rule.csv:11': ['S-4'], 'groundwork:search_rule.csv:12': ['S-4'],
    'groundwork:search_rule.csv:13': DATA,
    'groundwork:search_rule.csv:14': ['S-5'], 'groundwork:search_rule.csv:15': ['S-6'],
    'groundwork:search_rule.csv:16': ['S-4', 'F-4'], 'groundwork:search_rule.csv:17': ['F-4'],
    'groundwork:search_rule.csv:18': ['S-7'],
    # settings.csv
    'groundwork:settings.csv:2': DATA, 'groundwork:settings.csv:3': DATA, 'groundwork:settings.csv:4': DATA,
    'groundwork:settings.csv:5': DATA, 'groundwork:settings.csv:6': DATA, 'groundwork:settings.csv:7': DATA,
    'groundwork:settings.csv:8': DATA,
    'groundwork:settings.csv:9': ['S-6'],
    'groundwork:settings.csv:10': DATA, 'groundwork:settings.csv:11': DATA, 'groundwork:settings.csv:12': DATA,
    'groundwork:settings.csv:13': ['F-4'],
    'groundwork:settings.csv:14': ['F-5'],
    'groundwork:settings.csv:15': DATA, 'groundwork:settings.csv:16': DATA,
    'groundwork:settings.csv:17': ['S-2', 'S-3', 'F-2'],
    'groundwork:settings.csv:18': ['S-1', 'F-3'],
    # lists.csv
    **{'groundwork:lists.csv:%d' % n: DATA for n in range(2, 11)},
    **{'groundwork:lists.csv:%d' % n: ['S-6'] for n in range(11, 16)},
    'groundwork:lists.csv:16': N + 'the key table, read by the counts; S-4 says it is not read through search_rule.csv:9',
    'groundwork:lists.csv:17': N + 'the key table, read by the counts',
}


def units():
    out = []
    bl = lines(BRIEF)
    for n in range(5, 41):
        l = bl[n - 1].strip()
        if not l or l.startswith('#') or re.fullmatch(r'\|[-| ]+\|', l):
            continue
        if l.startswith('| Setting'):
            out.append('brief:%d' % n)
            continue
        out.append('brief:%d' % n)
    out += sorted(register_sections())
    out += ['ruling:' + g for g in sorted(ruled_g())]
    out += ['ruling:' + q for q in sorted(ruled_q(), key=lambda k: int(k[2:]))]
    for f in ('search_rule.csv', 'settings.csv', 'lists.csv'):
        for n in range(2, len([x for x in lines(GW[f]) if x.strip()]) + 1):
            out.append('groundwork:%s:%d' % (f, n))
    return out


def order(tok):
    kinds = ['brief', 'R', 'ruling:G', 'ruling:Q', 'groundwork']
    k = next(i for i, p in enumerate(kinds) if tok.startswith(p))
    nums = [int(x) for x in re.findall(r'\d+', tok)]
    return (k, tok.split(':')[1] if tok.startswith('groundwork') else '', nums)


def main():
    us = units()
    undisposed = [u for u in us if u not in DISP]
    stray = [d for d in DISP if d not in us]
    unresolved = [u for u in us if resolve(u)[0] is None]
    print('units enumerated from the sources: %d; without a disposition: %d %s; dispositions for no unit: %d %s; unresolved: %d %s'
          % (len(us), len(undisposed), undisposed, len(stray), stray, len(unresolved), unresolved))
    if undisposed or stray or unresolved:
        sys.exit(1)
    carry = {}
    for u in us:
        d = DISP[u]
        if isinstance(d, list):
            for m in d:
                carry.setdefault(m, []).append(u)
    none = sum(1 for u in us if not isinstance(DISP[u], list))
    print('units carrying a member or the screens\' line: %d; units carrying none: %d' % (len(us) - none, none))
    for name, members, fname in (('steps', STEPS, 'STEPS_SET.md'), ('failures', FAILURES, 'FAILURES_SET.md')):
        rows = []
        empty = [m for m in members if m not in carry]
        for m, desc in members.items():
            srcs = ' · '.join(sorted(carry.get(m, []), key=order))
            if name == 'steps':
                rows.append('| %s | %s | %s |' % (m, desc, srcs))
            else:
                rows.append('| %s | %s | %s | %s |' % (m, desc[0], desc[1], srcs))
        head = ('| Step | What it is | Sources |\n|---|---|---|' if name == 'steps'
                else '| Failure | At step | What it is | Sources |\n|---|---|---|---|')
        text = ('# The %s of enrolling a learner, listed source first\n\n'
                'Written by `inventory.py` from the dispositions of %d units of the sources; each member\'s sources are the units that carry it.\n\n%s\n%s\n'
                % (name, len(us), head, '\n'.join(rows)))
        (E / fname).write_text(text, encoding='utf-8')
        print('%s: %d, each with at least one source: %s; tokens: %d' % (
            name, len(members), not empty, sum(len(carry.get(m, [])) for m in members)))
    print('screens\' line: %s' % ' · '.join(sorted(carry['SC'], key=order)))
    for u in us:
        d = DISP[u]
        print('  %-34s %s' % (u, ', '.join(d) if isinstance(d, list) else d))


if __name__ == '__main__':
    main()
