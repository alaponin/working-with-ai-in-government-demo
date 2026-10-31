"""Review of round 3: every step and failure of GOAL.md looked up at its source, by the review's own resolver.

A ruling is read at its ruled part only: for G-nn the summary row of GAPS-PAPER.md (lines 26-38, found by
its first cell) and the line beginning '**Recommendation' in its section; for Q-n the line beginning
'**Proposal' in its section of QUESTIONS-PAPER.md. Nothing of the round's sources.py is imported.
Prints each member's claims, then each token beside the text it resolves to.
"""
import re
import sys
from pathlib import Path

ROOT = Path('/Users/arnelaponin/Documents/Dev/wai-demo')
DOCS = ROOT / 'mini-registry/docs'
F = {'brief': ROOT / 'brief/MINI-REGISTRY-BRIEF.md', 'reg': DOCS / 'REQUIREMENTS.md',
     'gaps': DOCS / 'GAPS-PAPER.md', 'qs': DOCS / 'QUESTIONS-PAPER.md', 'goal': DOCS / 'GOAL.md',
     'search_rule.csv': DOCS / 'groundwork/search_rule.csv', 'settings.csv': DOCS / 'groundwork/settings.csv',
     'lists.csv': DOCS / 'groundwork/lists.csv', 'GROUNDWORK.md': DOCS / 'GROUNDWORK.md'}
L = {k: p.read_text(encoding='utf-8').splitlines() for k, p in F.items()}


def section_lines(key, head):
    """Line numbers (1-based) from a heading matching head to the next heading of level 2 or 3."""
    ls, out, on = L[key], [], False
    for i, l in enumerate(ls, 1):
        if re.match(head, l):
            on = True
            continue
        if on and re.match(r'#{2,3} ', l):
            break
        if on:
            out.append(i)
    return out


def ruled(token):
    m = re.fullmatch(r'ruling:G-(\d\d)', token)
    if m:
        g = 'G-' + m.group(1)
        row = [i for i in range(26, 39) if L['gaps'][i - 1].startswith('| %s |' % g)]
        rec = [i for i in section_lines('gaps', r'## %s ' % g) if L['gaps'][i - 1].startswith('**Recommendation')]
        return 'gaps', row + rec
    m = re.fullmatch(r'ruling:Q-(\d+)', token)
    if m:
        q = 'Q-' + m.group(1)
        return 'qs', [i for i in section_lines('qs', r'## %s ' % q) if L['qs'][i - 1].startswith('**Proposal')]
    return None, []


def resolve(token):
    m = re.fullmatch(r'brief:(\d+)', token)
    if m:
        n = int(m.group(1))
        return 'brief', [n] if n <= len(L['brief']) and L['brief'][n - 1].strip() else []
    m = re.fullmatch(r'R-(\d\d)', token)
    if m:
        return 'reg', section_lines('reg', r'### %s$' % token)
    if token.startswith('ruling:'):
        return ruled(token)
    m = re.fullmatch(r'groundwork:([\w.]+):(\d+)', token)
    if m and m.group(1) in L:
        n = int(m.group(2))
        return m.group(1), [n] if n <= len(L[m.group(1)]) else []
    return None, []


def members():
    out, cur = {}, None
    for l in L['goal']:
        m = re.match(r'### ((?:S|F|SC)-\d+) — (.*)', l)
        if m:
            cur = m.group(1)
            out[cur] = {'title': m.group(2)}
            continue
        if l.startswith('## ') or l.startswith('---'):
            cur = None
        if cur:
            m = re.match(r'- \*\*(.*?):\*\* (.*)', l)
            if m:
                out[cur][m.group(1)] = m.group(2)
    return out


def main():
    ms = members()
    unres = 0
    for k, v in ms.items():
        if k.startswith('SC'):
            continue
        print('=' * 100)
        print(k, '—', v['title'])
        for f, t in v.items():
            if f not in ('title', 'Source'):
                print('  [%s] %s' % (f, t))
        for tok in [t.strip() for t in v.get('Source', '').split(' · ') if t.strip()]:
            key, nums = resolve(tok)
            if not nums:
                unres += 1
                print('  !! %s does not resolve' % tok)
                continue
            text = [L[key][n - 1].strip() for n in nums if L[key][n - 1].strip()]
            if key == 'reg':
                text = [t for t in text if t.startswith('**Requirement') or t.startswith('- *')]
            print('  -- %s -> %s:%s' % (tok, key, ','.join(map(str, nums)) if len(nums) < 4 else '%d-%d' % (nums[0], nums[-1])))
            for t in text:
                print('       | ' + t[:400])
    print('=' * 100)
    print('steps: %d; failures: %d; screens: %d; tokens not resolving: %d' % (
        sum(k.startswith('S-') for k in ms), sum(k.startswith('F-') for k in ms), sum(k.startswith('SC-') for k in ms), unres))


if __name__ == '__main__':
    sys.exit(main())
