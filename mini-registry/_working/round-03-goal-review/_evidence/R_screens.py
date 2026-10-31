"""Review of round 3: every screen the goal shows, against its list of screens, read from the whole file.

Counts every SC-n mentioned anywhere in GOAL.md (steps, failures, screens, gaps), the screens listed under
'## 3. The screens', the 'Named by' of each beside the members that actually name it, and the line of R-17.
"""
import re
from pathlib import Path

G = Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/docs/GOAL.md').read_text(encoding='utf-8')
LINE = 'Invented data, Progressa is fictional'
head, _, rest = G.partition('## 3. The screens')
screens, _, gaps = rest.partition('## Gaps against the sources')
listed = re.findall(r'^### (SC-\d+) ', screens, re.M)
anywhere = sorted(set(re.findall(r'SC-\d+', G)), key=lambda s: int(s[3:]))
named_by = {}
for blk in re.split(r'^### ', head, flags=re.M)[1:]:
    k = blk.split(' ', 1)[0]
    for s in set(re.findall(r'SC-\d+', blk)):
        named_by.setdefault(s, set()).add(k)
print('SC-n mentioned anywhere in the goal: %d %s' % (len(anywhere), anywhere))
print('screens listed: %d %s' % (len(listed), listed))
print('mentioned and not listed: %s; listed and never mentioned before the list: %s' % (
    [s for s in anywhere if s not in listed], [s for s in listed if s not in named_by]))
for blk in re.split(r'^### ', screens, flags=re.M)[1:]:
    k = blk.split(' ', 1)[0]
    nb = re.search(r'\*\*Named by:\*\* (.*)', blk).group(1)
    decl = set(re.findall(r'[SF]-\d+', nb))
    line = re.search(r'\*\*Carries the line:\*\* "(.*)"', blk)
    print('  %s named by (declared) %s, (found) %s, agree %s; carries the line: %s' % (
        k, sorted(decl), sorted(named_by.get(k, [])), decl == named_by.get(k, set()),
        bool(line and line.group(1) == LINE)))
print('views named in the gaps section without an SC number: %s' % re.findall(r'on which screen|a refusal', gaps))
