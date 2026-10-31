"""The figure re-established by a route the round did not use.
The round enumerated every unit of the sources and gave each a disposition
(inventory.py). This route starts from the words that mark a departure from the
goal's plain path -- refusal, negation, condition, limit -- and reads only the
units that carry such a word, in the ruled part of each paper only. Each hit is
given, by hand below, the failure it states or rules, or why it states none.
The program stops on a hit without a disposition and on a disposition without
a hit, then counts the distinct failures and sets them beside the goal's."""
import re, sys, pathlib
MR = pathlib.Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry')
BRIEF = (MR.parent / 'brief/MINI-REGISTRY-BRIEF.md').read_text().split('\n')
REQ = (MR / 'docs/REQUIREMENTS.md').read_text().split('\n')
GAPS = (MR / 'docs/GAPS-PAPER.md').read_text().split('\n')
QP = (MR / 'docs/QUESTIONS-PAPER.md').read_text().split('\n')
GW = {f: (MR / 'docs/groundwork' / f).read_text().split('\n') for f in ('search_rule.csv', 'settings.csv', 'lists.csv')}
GOAL = (MR / 'docs/GOAL.md').read_text()

units = []  # (id, text)
for i in range(5, 41):  # the brief's five sections, lines 5 to 40
    if BRIEF[i - 1].strip() and not BRIEF[i - 1].startswith('#') and not BRIEF[i - 1].startswith('|---'):
        units.append(('brief:%d' % i, BRIEF[i - 1]))
cur = None
for i, l in enumerate(REQ, 1):  # each R block, requirement and test, until the gaps section
    if l.startswith('## Gaps'): break
    m = re.match(r'### (R-\d+)', l)
    if m: cur = m.group(1); continue
    if cur and l.strip() and not l.startswith('#') and not l.startswith('**Cites'):
        units.append(('%s@%d' % (cur, i), l))
for i in range(26, 39):
    units.append(('G-row@%d' % i, GAPS[i - 1]))
for i, l in enumerate(GAPS, 1):
    if l.startswith('**Recommendation'): units.append(('G-rec@%d' % i, l))
for i, l in enumerate(QP, 1):
    if l.startswith('**Proposal'): units.append(('Q-prop@%d' % i, l))
for f, L in GW.items():
    for i, l in enumerate(L[1:], 2):
        if l.strip(): units.append(('%s:%d' % (f, i), l))

MARK = re.compile(r"refus|otherwise|\bnot\b|\bnever\b|\bno\b|\bnone\b|cannot|more than one|differ|twice|\bonly\b|missing|wrong|\bbefore\b|\bfail", re.I)
hits = [(u, t) for u, t in units if MARK.search(t)]

# Dispositions, written by hand after reading each hit. Failure classes:
#   X-MISSING  an entry of the four not made     X-DATE   date not in its form
#   X-SCHOOL   school not among the three        X-MANY   more than one learner found
#   X-MISSED   the same child not caught (registered twice)
D = {}
def d(keys, v):
    for k in keys.split(): D[k] = v
if len(sys.argv) > 1 and sys.argv[1] == 'list':
    for u, t in hits: print(u, '|', t.strip()[:220])
    print('units in scope: %d; units carrying a marker: %d' % (len(units), len(hits))); sys.exit(0)
exec((pathlib.Path(__file__).parent / 'R_failures_dispositions.py').read_text())
missing = [u for u, _ in hits if u not in D]
extra = [k for k in D if k not in {u for u, _ in hits}]
if missing or extra:
    print('hits without a disposition:', missing); print('dispositions for no hit:', extra); sys.exit(1)
classes = {}
for u, _ in hits:
    for c in re.findall(r'X-[A-Z]+', D[u]): classes.setdefault(c, []).append(u)
print('units in scope: %d; units carrying a marker: %d; every hit disposed: True' % (len(units), len(hits)))
for c, us in sorted(classes.items()): print('  %-10s stated or ruled by %d hit(s): %s' % (c, len(us), ', '.join(us)))
goal_f = re.findall(r'^### (F-\d+) — (.*)$', GOAL, re.M)
print('the figure, this route: %d failures %s' % (len(classes), sorted(classes)))
print('the goal: %d failures %s' % (len(goal_f), [f'{a} {b}' for a, b in goal_f]))
