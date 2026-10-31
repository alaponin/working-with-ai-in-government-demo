"""List, for each of G-01 to G-13, the lines of the register outside its section
"Gaps against the brief" that name that gap, into REGISTER_LINES.md (gap G1 of the review).

usage: register_lines.py <REQUIREMENTS.md> <REGISTER_LINES.md>
"""
import re
import sys

reg_path, out_path = sys.argv[1], sys.argv[2]
lines = open(reg_path, encoding="utf-8").read().split("\n")
start = lines.index("## Gaps against the brief") + 1  # 1-based line of the heading
named = {"G-%02d" % i: [] for i in range(1, 14)}
for no, line in enumerate(lines[: start - 1], start=1):
    for g in sorted(set(re.findall(r"\bG-\d\d\b", line))):
        if g in named:
            named[g].append((no, line))
out = ["# The register lines that name each open question, outside its section \"Gaps against the brief\"", "",
       "Listed by `register_lines.py` from `docs/REQUIREMENTS.md`, lines 1 to %d (the section begins at line %d)." % (start - 1, start), ""]
total = 0
for g, rows in named.items():
    out.append("- **%s**: %s" % (g, ", ".join(str(n) for n, _ in rows) or "none"))
    total += len(rows)
out.append("")
distinct = sorted(set(n for rows in named.values() for n, _ in rows))
out.append("Gap-line pairs: %d; distinct lines: %d (%s)" % (total, len(distinct), ", ".join(map(str, distinct))))
open(out_path, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
