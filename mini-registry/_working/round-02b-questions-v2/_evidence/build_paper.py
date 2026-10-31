"""Build docs/QUESTIONS-PAPER.md from paper_src.md: each {Qn} is the question as listed in QUESTIONS.md,
{A5} the lines of the A5 log between its timestamp and its EXIT line.

usage: build_paper.py <paper_src.md> <QUESTIONS.md> <A5 log> <QUESTIONS-PAPER.md to write>
"""
import re
import sys

src, qpath, a5, out = sys.argv[1:5]
text = open(src, encoding="utf-8").read()
for line in open(qpath, encoding="utf-8"):
    m = re.match(r"^- (`docs/GROUNDWORK\.md:\d+` (\d+)\. .*)$", line.rstrip("\n"))
    if m:
        text = text.replace("{Q%s}\n" % m.group(2), "> %s\n" % m.group(1))
log = [l.rstrip("\n") for l in open(a5, encoding="utf-8")]
body = [l for l in log[1:] if not l.startswith("EXIT=")]
text = text.replace("{A5}", "\n".join(body))
left = re.findall(r"\{(Q\d+|A5)\}", text)
open(out, "w", encoding="utf-8").write(text)
print("placeholders left: %d" % len(left))
print("bytes: %d" % len(text.encode("utf-8")))
