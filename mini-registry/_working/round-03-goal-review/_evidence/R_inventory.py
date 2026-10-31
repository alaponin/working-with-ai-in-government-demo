"""Review of round 3: the sets of steps and failures listed again, source first.

The round typed its members into list_sets.py and anchored each to a fragment of its sources. This
route runs the other way: the program enumerates every unit of every source in scope (each non-empty
line of the brief's five sections; each requirement of the register; each ruled row and recommendation
of G-01 to G-13; each closing proposal of Q-1 to Q-14; each row of the three tables), and the review's
own table below gives each unit a disposition: the review's own member(s) it carries, 'SCREEN', or '-'
with the reason. A unit with no disposition stops the program. The review's members are then set
beside the goal's both ways, and for each unit carried the goal member is checked to cite it.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from R_lookup import L, members, resolve  # noqa: E402  (the review's own resolver)

# the review's own members, in its own words, and the goal member each is set beside
MINE = {
    'm-open':   ('the clerk opens the one screen of the one goal: four entries, the school a choice of the 3', 'S-1'),
    'm-enter':  ('the clerk enters the four, the date as YYYY-MM-DD, and submits', 'S-2'),
    'm-gate':   ('nothing is searched until all four are entered; a date in another form is refused', 'S-3'),
    'm-search': ('the search, first, among learners, on the three fields, capitals alone forgiven, school and key table not read', 'S-4'),
    'm-one':    ('exactly one found: that learner shown, nothing new entered', 'S-5'),
    'm-none':   ('none found: a new learner number in sequence, 1 first, and the four saved as entered', 'S-6'),
    'm-tell':   ('the clerk sees which of the two happened, the two screens differing', 'S-7'),
    'x-missing': ('an entry not made: the search does not run', 'F-1'),
    'x-date':   ('a date not YYYY-MM-DD: refused', 'F-2'),
    'x-school': ('a school not among the 3: the school is chosen from the 3', 'F-3'),
    'x-many':   ('more than one learner found: nothing new, the entry cannot be completed; never reached', 'F-4'),
    'x-missed': ('the same child entered with a difference beyond capitals: not found, held twice (4 of the 8 caught)', 'F-5'),
}

D = {}  # unit -> list of members, or a reason string


def d(unit, what):
    D[unit] = what


# the brief, its five sections (lines 7 to 40)
for n, w in {7: ['x-missed'], 11: ['m-open', 'm-enter', 'm-search'], 13: ['m-search', 'm-one'], 14: ['m-none'],
             15: ['m-tell'], 19: '- the data: the three lists', 23: '- the data: 60 children',
             24: ['m-open', 'x-school'], 25: '- the data: 8', 26: '- the data: 4 (bears on x-missed through G-05)',
             27: '- the data: ages; no check on an entry is ruled (a gap)', 29: '- the reset (G-08: not a step)',
             33: 'SCREEN', 34: '- a constraint on the build, not a step', 35: '- a constraint on the checks, not a step',
             39: '- a deliverable', 40: '- a deliverable'}.items():
    d('brief:%d' % n, w)
# the register
for r, w in {'R-01': ['m-one'], 'R-02': ['m-open'], 'R-03': ['m-open', 'm-enter', 'm-none'], 'R-04': ['m-search'],
             'R-05': ['m-search', 'm-one', 'm-tell', 'x-many'], 'R-06': ['m-none', 'x-missed'], 'R-07': ['m-tell'],
             'R-17': 'SCREEN'}.items():
    d(r, w)
for i in list(range(8, 17)) + list(range(18, 24)):
    d('R-%02d' % i, '- the data, the reset, or a constraint on the build or the deliverables')
# the first ruling
for g, w in {'G-01': ['m-none'], 'G-02': ['x-many'], 'G-03': ['m-search'], 'G-04': '- the data',
             'G-05': ['m-search', 'x-missed', 'x-many'], 'G-06': '- ages; no check on an entry is ruled (a gap)',
             'G-07': ['m-enter', 'm-gate', 'x-missing', 'x-date', 'x-school'], 'G-08': ['m-open'], 'G-09': 'SCREEN',
             'G-10': '- the evidence for R-16', 'G-11': '- other bodies', 'G-12': '- the checks: one per failure named, not a step',
             'G-13': '- the note'}.items():
    d('ruling:' + g, w)
# the second ruling
for q in range(1, 15):
    d('ruling:Q-%d' % q, {4: ['m-none'], 14: ['x-many']}.get(q, '- the data, the reset or the counts; no step of enrolment'))
# the tables
SR = {2: ['m-search'], 3: ['m-search'], 4: ['m-search'], 5: ['m-search'], 6: ['m-search', 'x-missed'], 7: ['m-search'],
      8: ['m-search'], 9: ['m-search'], 10: ['m-gate', 'x-missing'], 11: ['m-search'], 12: ['m-search'],
      13: '- the reset (G-08: not a step)', 14: ['m-one'], 15: ['m-none'], 16: ['x-many'], 17: ['x-many'], 18: ['m-tell']}
ST = {3: ['m-open'], 9: ['m-none'], 13: ['x-many'], 14: ['x-missed'], 17: ['m-enter', 'm-gate', 'x-date'],
      18: ['m-open', 'x-school']}
LI = {11: ['m-none'], 12: ['m-none'], 13: ['m-none'], 14: ['m-none'], 15: ['m-none'], 16: ['m-search']}
for f, tab, last in (('search_rule.csv', SR, 18), ('settings.csv', ST, 18), ('lists.csv', LI, 17)):
    for n in range(2, last + 1):
        d('groundwork:%s:%d' % (f, n), tab.get(n, '- the data, the lists or the counts; no step of enrolment'))


def units():
    """Every unit in scope, enumerated from the files, not from the table above."""
    out = []
    on = False
    for n, l in enumerate(L['brief'], 1):
        if l.startswith('## '):
            on = l[3:].strip() in ('What it is for', 'What it must do', 'The made-up data, in known numbers',
                                   'What it must not do', 'What it delivers')
            continue
        if on and l.strip() and not re.match(r'\|\s*(Setting|---)', l):
            out.append('brief:%d' % n)
    out += ['R-%s' % m for m in re.findall(r'^### R-(\d\d)$', '\n'.join(L['reg']), re.M)]
    out += ['ruling:%s' % m for m in re.findall(r'^\| (G-\d\d) \|', '\n'.join(L['gaps'][25:38]), re.M)]
    out += ['ruling:%s' % m for m in re.findall(r'^## (Q-\d+) ', '\n'.join(L['qs']), re.M)]
    for f in ('search_rule.csv', 'settings.csv', 'lists.csv'):
        out += ['groundwork:%s:%d' % (f, n) for n in range(2, len(L[f]) + 1) if L[f][n - 1].strip()]
    return out


def main():
    us = units()
    nodisp = [u for u in us if u not in D]
    unused = [u for u in D if u not in us]
    print('units enumerated from the sources: %d; without a disposition: %d %s; dispositions for no unit: %d %s' % (
        len(us), len(nodisp), nodisp, len(unused), unused))
    if nodisp:
        return 1
    goal = members()
    carried = {m: [] for m in MINE}
    for u in us:
        if isinstance(D[u], list):
            for m in D[u]:
                carried[m].append(u)
    print('units carrying a step or failure: %d; screen units: %d; units of no step or failure: %d' % (
        sum(isinstance(D[u], list) for u in us), sum(D[u] == 'SCREEN' for u in us),
        sum(isinstance(D[u], str) and D[u] != 'SCREEN' for u in us)))
    print()
    for kind, pre in (('steps', 'm-'), ('failures', 'x-')):
        mine = [m for m in MINE if m.startswith(pre)]
        gpre = 'S-' if pre == 'm-' else 'F-'
        g = [k for k in goal if k.startswith(gpre)]
        mapped = {MINE[m][1] for m in mine}
        missing = [m for m in mine if MINE[m][1] not in goal]
        extra = [k for k in g if k not in mapped]
        print('%s: the review lists %d, the goal %d; missing from the goal: %d %s; in the goal and not the review: %d %s' % (
            kind, len(mine), len(g), len(missing), missing, len(extra), extra))
        for m in mine:
            gk = MINE[m][1]
            cites = [t.strip() for t in goal.get(gk, {}).get('Source', '').split(' · ')]
            notcited = [u for u in carried[m] if u not in cites]
            print('  %-9s -> %-4s units %2d, cited by the goal %2d, not cited %s' % (
                m, gk, len(carried[m]), len(carried[m]) - len(notcited), notcited))
    print()
    print('the figure: failures the sources state or rule, listed source first: %d %s' % (
        len([m for m in MINE if m.startswith('x-')]), [m for m in MINE if m.startswith('x-')]))
    print()
    print('what each failure shows the clerk, against the ruled or stated words of its own sources:')
    for k in [k for k in goal if k.startswith('F-')]:
        sees = goal[k].get('What the clerk sees', '')
        hits = []
        for t in [t.strip() for t in goal[k].get('Source', '').split(' · ')]:
            key, nums = resolve(t)
            for n in nums:
                line = L[key][n - 1]
                for w in re.findall(r'[^.;|]*(?:refus|cannot be completed)[^.;|]*', line):
                    hits.append('%s: «%s»' % (t, w.strip()))
        print('  %s sees: %s' % (k, sees))
        for h in hits:
            print('      ' + h)
        if not hits:
            print('      (no cited source carries a refusal or "cannot be completed")')
    return 0


if __name__ == '__main__':
    sys.exit(main())
