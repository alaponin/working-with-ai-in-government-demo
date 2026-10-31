"""List the register's open questions G-01 to G-13, word for word, from its section
"Gaps against the brief", into QUESTIONS.md. G-14 is left out: the orchestrator has closed it.

usage: list_questions.py <REQUIREMENTS.md> <QUESTIONS.md>
"""
import re
import sys

reg_path, out_path = sys.argv[1], sys.argv[2]
lines = open(reg_path, encoding="utf-8").read().split("\n")
start = lines.index("## Gaps against the brief")
pat = re.compile(r"^- \*\*(G-\d\d)\*\* (.*)$")
rows = []
for no, line in enumerate(lines[start:], start=start + 1):
    m = pat.match(line)
    if m:
        rows.append((m.group(1), no, line[2:]))  # the line without its list marker
kept = [r for r in rows if int(r[0][2:]) <= 13]
out = ["# The register's open questions, G-01 to G-13", "",
       "Listed by `list_questions.py` from `docs/REQUIREMENTS.md`, section \"Gaps against the brief\" "
       "(line %d). Each question is the register's line without its list marker, word for word. "
       "G-14 is not listed: it is closed from the brief, line 13." % (start + 1), ""]
for gid, no, text in kept:
    out.append("- `docs/REQUIREMENTS.md:%d` %s" % (no, text))
out.append("")
out.append("Questions listed: %d (of %d in the section)" % (len(kept), len(rows)))
open(out_path, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("questions in the section: %d" % len(rows))
print("questions listed (G-01 to G-13): %d" % len(kept))
