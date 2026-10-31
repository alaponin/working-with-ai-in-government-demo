"""A3: every requirement count.csv pairs with an element of the goal, and F-1 to F-7, against
the names of the checks that passed in the round's run of `node --test test/` (A2_tests.log).
A check counts for an identifier where the identifier stands in the part of its name before
the first ' — ', and the check is one of goal.test.js or requirements.test.js."""
import csv, re, sys

count_csv, log = sys.argv[1], sys.argv[2]
with open(count_csv, newline='') as f:
    rows = list(csv.DictReader(f))
reqs = sorted({r['requirement'] for r in rows if r['element'] != 'none'})
want = reqs + ['F-%d' % i for i in range(1, 8)]
names = []
for line in open(log, encoding='utf8'):
    m = re.match(r'^ok \d+ - (.*)$', line.rstrip('\n'))
    if m and ' — ' in m.group(1):
        names.append(m.group(1))
print('requirements paired with an element of the goal:', len(reqs), ' '.join(reqs))
print('ways the goal goes wrong: 7 F-1 to F-7')
print('passing checks of the two new files (named with " — "):', len(names))
missing = 0
for ident in want:
    hits = [n for n in names if re.search(r'(^|[ ,])' + re.escape(ident) + r'($|[ ,])', n.split(' — ')[0])]
    if not hits:
        missing += 1
    print('%-5s %d  %s' % (ident, len(hits), hits[0] if hits else 'NO CHECK'))
print('%d without a check' % missing)
sys.exit(1 if missing else 0)
