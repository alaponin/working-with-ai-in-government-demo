"""The review's own list of the steps, from the sources, compared both ways with the
goal's steps by the source that carries each; and the screens checked against
their list. Does not import the round's programs."""
import re, pathlib
MR = pathlib.Path('/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry')
GOAL = (MR / 'docs/GOAL.md').read_text()
V1 = (MR / '_working/round-03-goal-v2/_evidence/GOAL_v1.md').read_text()

# The steps, listed here from the sources (read in R_lookup.out), each with the
# source units that carry it; a goal step matches when it cites every one of them.
MINE = [
    ('open the enrolment screen; enrolment the only thing offered', ['R-03', 'ruling:G-08']),
    ('enter the four, school chosen from three, submit', ['brief:11', 'R-03', 'ruling:G-07']),
    ('the date held to YYYY-MM-DD, refused otherwise', ['ruling:G-07', 'groundwork:settings.csv:17']),
    ('search first, three fields, capitals ignored, among learners', ['brief:11', 'R-04', 'groundwork:search_rule.csv:2', 'groundwork:search_rule.csv:12']),
    ('exactly one found: show it, enter nothing new', ['brief:13', 'R-05']),
    ('none found: new learner number, save the record', ['brief:14', 'R-06', 'ruling:G-01']),
    ('the clerk sees which of the two happened', ['brief:15', 'R-07']),
]
steps = re.findall(r'^### (S-\d+) — .*?\n(.*?)(?=^### |^---)', GOAL, re.S | re.M)
src = {sid: set(re.search(r'\*\*Source:\*\* (.*)', b).group(1).split(' · ')) for sid, b in steps}
matched_goal = set(); missing = []
for name, need in MINE:
    hit = [sid for sid, s in src.items() if set(need) <= s and sid not in matched_goal]
    print('%-62s -> %s' % (name, hit or 'NONE'))
    if not hit: missing.append(name)
    matched_goal.update(hit[:1])
extra = [sid for sid in src if sid not in matched_goal]
print('steps: the review lists %d, the goal %d; missing from the goal: %d %s; in the goal and not the review: %d %s'
      % (len(MINE), len(src), len(missing), missing, len(extra), extra))

# Screens
body, gaps = GOAL.split('## Gaps against the sources')
mentioned = sorted(set(re.findall(r'SC-\d+', GOAL)), key=lambda s: int(s[3:]))
listed = re.findall(r'^### (SC-\d+) — ([^\n]*)\n(.*?)(?=^### |^---|^## )', GOAL, re.S | re.M)
named_by_members = set(re.findall(r'SC-\d+', GOAL.split('## 3. The screens')[0]))
LINE = '"Invented data, Progressa is fictional"'
print('screens mentioned anywhere: %d %s' % (len(mentioned), mentioned))
print('screens listed: %d %s' % (len(listed), [s for s, _, _ in listed]))
print('mentioned and not listed: %s; listed and named by no step or failure: %s'
      % ([s for s in mentioned if s not in {x for x, _, _ in listed}], [s for s, _, _ in listed if s not in named_by_members]))
for s, t, b in listed:
    nb = re.search(r'\*\*Named by:\*\* (.*)', b).group(1)
    print('  %s %-38s named by %-14s carries the line: %s' % (s, t, nb, LINE in b))
# Counts of version 1 against version 2, as the report gives them
for name, txt in (('v1', V1), ('v2', GOAL)):
    g = txt.split('## Gaps against the sources')[1]
    print('%s: steps %d, failures %d, screens listed %d, gaps %d' % (name,
          len(re.findall(r'^### S-\d+', txt, re.M)), len(re.findall(r'^### F-\d+', txt, re.M)),
          len(re.findall(r'^### SC-\d+', txt, re.M)), len(re.findall(r'^\d+\. \*\*', g, re.M))))
