"""Review's own resolver (does not import the round's programs).
For every step and failure of docs/GOAL.md: print each field, then each cited
source token with the text it resolves to. A ruling token resolves only to its
ruled lines: for G, the summary row (GAPS-PAPER.md 26-38) and the closing
Recommendation of its section; for Q, the closing Proposal of its section.
Also checks every quotation of the round's QUOTES.md against the line it names."""
import re, sys, pathlib
MR = pathlib.Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry')
BRIEF = (MR.parent / 'brief/MINI-REGISTRY-BRIEF.md').read_text().split('\n')
REQ = (MR / 'docs/REQUIREMENTS.md').read_text().split('\n')
GAPS = (MR / 'docs/GAPS-PAPER.md').read_text().split('\n')
QP = (MR / 'docs/QUESTIONS-PAPER.md').read_text().split('\n')
GW = {f: (MR / 'docs/groundwork' / f).read_text().split('\n') for f in ('search_rule.csv', 'settings.csv', 'lists.csv')}
GOAL = (MR / 'docs/GOAL.md').read_text()

def rblock(n):
    out, on = [], False
    for i, l in enumerate(REQ, 1):
        if l.startswith('### '):
            on = (l.strip() == '### R-%02d' % n)
            continue
        if on and l.startswith('## '):
            break
        if on and l.strip():
            out.append((i, l))
    return out

def g_ruled(n):
    rows = [(i, GAPS[i - 1]) for i in range(26, 39) if GAPS[i - 1].startswith('| G-%02d ' % n)]
    on = False
    for i, l in enumerate(GAPS, 1):
        if l.startswith('## '):
            on = l.startswith('## G-%02d ' % n)
        elif on and l.startswith('**Recommendation'):
            rows.append((i, l))
    return rows

def q_ruled(n):
    on = False
    for i, l in enumerate(QP, 1):
        if l.startswith('## '):
            on = l.startswith('## Q-%d ' % n)
        elif on and l.startswith('**Proposal'):
            return [(i, l)]
    return []

def resolve(tok):
    tok = tok.strip()
    m = re.fullmatch(r'brief:(\d+)', tok)
    if m:
        n = int(m.group(1)); return [(n, BRIEF[n - 1])] if 0 < n <= len(BRIEF) and BRIEF[n - 1].strip() else []
    m = re.fullmatch(r'R-(\d+)', tok)
    if m: return rblock(int(m.group(1)))
    m = re.fullmatch(r'ruling:G-(\d+)', tok)
    if m: return g_ruled(int(m.group(1)))
    m = re.fullmatch(r'ruling:Q-(\d+)', tok)
    if m: return q_ruled(int(m.group(1)))
    m = re.fullmatch(r'groundwork:([a-z_]+\.csv):(\d+)', tok)
    if m:
        f, n = m.group(1), int(m.group(2)); L = GW.get(f, [])
        return [(n, L[n - 1])] if 0 < n <= len(L) and L[n - 1].strip() else []
    return []

members = re.findall(r'^### ((?:S|F)-\d+) — (.*?)\n(.*?)(?=^### |^---|^## )', GOAL, re.S | re.M)
unres = 0; ntok = 0
for mid, title, body in members:
    print('=' * 100); print(mid, '—', title)
    fields = re.findall(r'^- \*\*(.+?):\*\* (.*)$', body, re.M)
    src = ''
    for k, v in fields:
        if k == 'Source': src = v; continue
        print('  [%s] %s' % (k, v))
    for tok in src.split(' · '):
        ntok += 1
        r = resolve(tok)
        if not r:
            unres += 1; print('  !! UNRESOLVED', tok); continue
        for i, l in r:
            print('    <%s> %d: %s' % (tok, i, l.strip()[:400]))
print('=' * 100)
print('members: %d (steps %d, failures %d); tokens: %d; unresolved: %d' % (
    len(members), sum(1 for m in members if m[0].startswith('S')), sum(1 for m in members if m[0].startswith('F')), ntok, unres))

# The round's QUOTES.md: does each «quotation» stand at the file:line it names?
Q = (MR / '_working/round-03-goal-v2/_evidence/QUOTES.md').read_text()
FILES = {'MINI-REGISTRY-BRIEF.md': BRIEF, 'REQUIREMENTS.md': REQ, 'GAPS-PAPER.md': GAPS, 'QUESTIONS-PAPER.md': QP}
FILES.update(GW)
ruled_g = {i for n in range(1, 14) for i, _ in g_ruled(n)}
ruled_q = {i for n in range(1, 15) for i, _ in q_ruled(n)}
nq = bad = outside = 0
for quote, f, ln in re.findall(r'«(.+?)» \(([A-Za-z_.\-]+):(\d+)\)', Q):
    nq += 1; ln = int(ln)
    line = FILES[f][ln - 1] if f in FILES else ''
    norm = lambda s: s.replace('**', '')
    if norm(quote) not in norm(line):
        bad += 1; print('QUOTE NOT AT ITS LINE:', f, ln, quote)
    if f == 'GAPS-PAPER.md' and ln not in ruled_g: outside += 1; print('GAPS line not ruled:', ln, quote)
    if f == 'QUESTIONS-PAPER.md' and ln not in ruled_q: outside += 1; print('QUESTIONS line not ruled:', ln, quote)
print('QUOTES.md quotations read: %d; not found at the line named: %d; on an unruled line of a paper: %d' % (nq, bad, outside))
