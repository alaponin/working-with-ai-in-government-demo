"""The checks of round 3 over docs/GOAL.md: a1 (sets against goal), a2 (sources resolve), a3 (failures
complete), a4 (the search step beside the rows it cites), a5 (screens and R-17's line), a6 (gaps)."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from sources import resolve, GW, lines  # noqa: E402

E = Path(__file__).parent
GOAL = Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md')
LINE = '"Invented data, Progressa is fictional"'


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


def toks(s):
    return [t.strip() for t in s.split(' · ')] if s else []


def body():
    t = GOAL.read_text(encoding='utf-8')
    head, _, gaps = t.partition('\n## Gaps against the sources')
    return t, head, gaps


def set_rows(name):
    rows = {}
    for l in (E / name).read_text(encoding='utf-8').split('\n'):
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if cells and re.fullmatch(r'[SF]-\d+', cells[0]):
            rows[cells[0]] = cells
    return rows


def a1():
    _, head, _ = body()
    st, fa = blocks(head, 'S'), blocks(head, 'F')
    ss, fs = set_rows('STEPS_SET.md'), set_rows('FAILURES_SET.md')
    for label, sset, goal, srccol in (('steps', ss, st, 2), ('failures', fs, fa, 5)):
        missing = [k for k in sset if k not in goal]
        extra = [k for k in goal if k not in sset]
        diff = []
        for k in sset:
            if k in goal:
                a, b = set(toks(sset[k][srccol])), set(toks(field(goal[k], 'Source')))
                if a != b:
                    diff.append('%s sources differ: set-only %s goal-only %s' % (k, sorted(a - b), sorted(b - a)))
                if label == 'failures' and not field(goal[k], 'At step').startswith(sset[k][1]):
                    diff.append('%s step differs' % k)
        print('%s: set %d, goal %d' % (label, len(sset), len(goal)))
        for d in diff:
            print('  ' + d)
        print('%s: %d missing, %d extra, %d differing' % (label, len(missing), len(extra), len(diff)))


def a2():
    t, head, _ = body()
    st, fa = blocks(head, 'S'), blocks(head, 'F')
    nos, unres = 0, 0
    for k, b in list(st.items()) + list(fa.items()):
        s = field(b, 'Source')
        if not s:
            nos += 1
            print('  without source:', k)
            continue
        for tk in toks(s):
            p, r = resolve(tk)
            if p is None:
                unres += 1
                print('  unresolved:', k, tk, r)
    m = re.search(r'carries the line "Invented data, Progressa is fictional" \(([^)]*)\)', t)
    for tk in toks(m.group(1)):
        p, r = resolve(tk)
        if p is None:
            unres += 1
            print('  unresolved: screens', tk, r)
    print('steps: %d; failures: %d; screens\' line sources: %d' % (len(st), len(fa), len(toks(m.group(1)))))
    print('%d without source, %d unresolved' % (nos, unres))


def a3():
    _, head, _ = body()
    inc = 0
    for k, b in blocks(head, 'F').items():
        have = {f: bool(field(b, f)) for f in ('At step', 'What sets it off', 'What the clerk sees', 'What is saved', 'Source')}
        ok = all(have.values())
        inc += not ok
        print('%s: step %s, trigger %s, clerk sees %s, saved %s, source %s' % (
            k, *('yes' if have[f] else 'NO' for f in ('At step', 'What sets it off', 'What the clerk sees', 'What is saved', 'Source'))))
    print('%d incomplete' % inc)


def a4():
    _, head, _ = body()
    b = blocks(head, 'S')['S-4']
    print('S-4, the registry:', field(b, 'The registry'))
    rows = lines(GW['search_rule.csv'])
    cited = [tk for tk in toks(field(b, 'Source')) if tk.startswith('groundwork:search_rule.csv:')]
    for tk in cited:
        n = int(tk.rsplit(':', 1)[1])
        print('  %s  %s' % (tk, rows[n - 1]))
    print('rows cited: %d; compares rows in the file: %d' % (
        len(cited), sum(1 for r in rows if r.startswith('compares,'))))


def a5():
    _, head, _ = body()
    sc = blocks(head, 'SC')
    named = set()
    for pre in ('S', 'F'):
        for b in blocks(head, pre).values():
            named |= set(re.findall(r'SC-\d+', '\n'.join(b)))
    with_line = [k for k, b in sc.items() if (field(b, 'Carries the line') or '').rstrip('.') == LINE]
    print('screens named by the steps and failures: %d %s' % (len(named), sorted(named)))
    print('screens listed: %d; listed screens stating the line: %d' % (len(sc), len(with_line)))
    print('named, not listed: %s; listed, not named: %s' % (sorted(named - set(sc)), sorted(set(sc) - named)))


PROBES = ['2019-02-30', 'calendar', 'younger', 'older', 'longest', 'spaces only', 'cannot save',
          'cannot be given', 'return', 'keeps the entries', 'one refusal', 'different school']


def a6():
    _, head, gaps = body()
    if not gaps:
        print('section absent')
        return
    items = re.findall(r'^\d+\. (.*)$', gaps, re.M)
    notq = [i for i in items if not i.rstrip().endswith('?')]
    hits = [p for p in PROBES if p in head.split('## 1. The steps', 1)[1]]
    print('section present; gaps: %d; not a question: %d' % (len(items), len(notq)))
    print('probes for an answer in the steps, failures and screens: %d, found: %d %s' % (len(PROBES), len(hits), hits))


if __name__ == '__main__':
    {'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4, 'a5': a5, 'a6': a6}[sys.argv[1]]()
