"""Resolving a source token of round 3 (version 2) to the lines it may be read at, and finding a
quotation there.

brief:<n>               the brief's line n
R-<nn>                  the register's section ### R-<nn>, to the next heading
ruling:G-<nn>           the ruled lines of GAPS-PAPER.md only: its summary row (lines 26-38)
                        and the one-sentence recommendation closing its section
ruling:Q-<n>            the ruled line of QUESTIONS-PAPER.md only: the closing proposal of its section
groundwork:<file>:<n>   line n of docs/GROUNDWORK.md or docs/groundwork/<file>

Taken over from version 1's sources.py (_working/round-03-goal/_evidence/sources.py), with quote()
added: a quotation is found only where it stands whole, word for word, on one of the lines the
token resolves to.
"""
import re
from pathlib import Path

ROOT = Path('/Users/arnelaponin/Documents/Dev/wai-demo')
BRIEF = ROOT / 'brief/MINI-REGISTRY-BRIEF.md'
DOCS = ROOT / 'mini-registry/docs'
REGISTER = DOCS / 'REQUIREMENTS.md'
GAPS = DOCS / 'GAPS-PAPER.md'
QUESTIONS = DOCS / 'QUESTIONS-PAPER.md'
GW = {'GROUNDWORK.md': DOCS / 'GROUNDWORK.md',
      'search_rule.csv': DOCS / 'groundwork/search_rule.csv',
      'settings.csv': DOCS / 'groundwork/settings.csv',
      'lists.csv': DOCS / 'groundwork/lists.csv'}

_CACHE = {}


def lines(p):
    if p not in _CACHE:
        _CACHE[p] = p.read_text(encoding='utf-8').split('\n')
    return _CACHE[p]


def _sections(ls, head_re):
    out, cur = {}, None
    for i, l in enumerate(ls, 1):
        m = re.match(head_re, l)
        if m:
            cur = m.group(1)
            out[cur] = []
            continue
        if l.startswith('## ') or l.startswith('### ') or l.startswith('---'):
            cur = None
        if cur:
            out[cur].append(i)
    return out


def ruled_g():
    ls = lines(GAPS)
    out = {}
    for i in range(26, 39):
        m = re.match(r'\| (G-\d\d) \|', ls[i - 1])
        out.setdefault(m.group(1), []).append(i)
    for g, nums in _sections(ls, r'## (G-\d\d) ').items():
        rec = [n for n in nums if ls[n - 1].startswith('**Recommendation')]
        out[g].append(rec[-1])
    return out


def ruled_q():
    ls = lines(QUESTIONS)
    out = {}
    for q, nums in _sections(ls, r'## (Q-\d+) ').items():
        prop = [n for n in nums if ls[n - 1].startswith('**Proposal')]
        out[q] = [prop[-1]]
    return out


def register_sections():
    return _sections(lines(REGISTER), r'### (R-\d\d)$')


def resolve(token):
    """Return (path, [line numbers]) or (None, reason)."""
    token = token.strip()
    m = re.fullmatch(r'brief:(\d+)', token)
    if m:
        n = int(m.group(1))
        ls = lines(BRIEF)
        return (BRIEF, [n]) if 1 <= n <= len(ls) and ls[n - 1].strip() else (None, 'no such line')
    m = re.fullmatch(r'R-(\d\d)', token)
    if m:
        s = register_sections()
        return (REGISTER, s[token]) if token in s else (None, 'not in the register')
    m = re.fullmatch(r'ruling:(G-\d\d)', token)
    if m:
        g = ruled_g()
        n = int(m.group(1)[2:])
        return (GAPS, g[m.group(1)]) if 1 <= n <= 13 and m.group(1) in g else (None, 'not G-01 to G-13')
    m = re.fullmatch(r'ruling:Q-(\d+)', token)
    if m:
        q = ruled_q()
        k = 'Q-' + m.group(1)
        return (QUESTIONS, q[k]) if 1 <= int(m.group(1)) <= 14 and k in q else (None, 'not Q-1 to Q-14')
    m = re.fullmatch(r'groundwork:([\w.\-]+):(\d+)', token)
    if m:
        f, n = m.group(1), int(m.group(2))
        if f not in GW:
            return (None, 'no such groundwork file')
        ls = lines(GW[f])
        return (GW[f], [n]) if 1 <= n <= len(ls) and ls[n - 1].strip() else (None, 'no such line')
    return (None, 'not a source form')


def quote(token, words):
    """Return (path, line) where `words` stand whole on a line the token resolves to, or (None, why)."""
    p, nums = resolve(token)
    if p is None:
        return None, nums
    ls = lines(p)
    hit = [n for n in nums if words in ls[n - 1]]
    return (p, hit[0]) if hit else (None, 'words not at the lines the token resolves to')
