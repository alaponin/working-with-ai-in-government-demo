#!/bin/zsh
# Reviewer's own run of the register's self-test, then its check over NOTE.md and over the PDF's text.
S="/Users/arnelaponin/Library/Application Support/Claude/local-agent-mode-sessions/ffbe2f0e-bc4b-46d3-ad76-b08a7882aae9/7bbcb800-2754-4c5e-97ea-ccb874ea3fee/rpm/plugin_018SiGJfFaxxAvevS4xGQJgb/skills/orchestrator/scripts"
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=$M/_working/round-08-note-v2-review/_evidence
X=$M/docs/note/register_exceptions.txt
date -u +%Y-%m-%dT%H:%M:%SZ
echo "# self-test"
/usr/bin/python3 -B "$S/readers_register_selftest.py"; echo "SELFTEST EXIT=$?"
echo "# check over NOTE.md, no exceptions"
/usr/bin/python3 -B "$S/readers_register_check.py" $M/docs/NOTE.md; echo "CHECK (no exceptions) EXIT=$?"
echo "# check over NOTE.md, with the build folder's exceptions"
cat "$X"; shasum -a 256 "$X"
/usr/bin/python3 -B "$S/readers_register_check.py" $M/docs/NOTE.md --exceptions "$X"; echo "CHECK (with exceptions) EXIT=$?"
echo "# check over the PDF's text extracted here by Ghostscript, with the exceptions"
/usr/bin/python3 -B "$S/readers_register_check.py" $E/note_text.gs.txt --exceptions "$X" --quiet; echo "CHECK (PDF text, gs, with exceptions) EXIT=$?"
echo "# the words of NOTE.md (markup removed) against the words of the PDF's text"
/usr/bin/python3 -I - $M/docs/NOTE.md $E/note_text.gs.txt $M/_working/round-08-note-v2/_evidence/text.build1.txt $M/_working/round-08-note-v2/_evidence/text.build2.txt <<'PY'
import re, sys, hashlib
def words(t):
    t = t.replace("**", "").replace("•", " ")
    t = re.sub(r"(?m)^\s*#+\s*", "", t)
    t = re.sub(r"(?m)^\s*-\s+", "", t)
    return t.split()
md, gs, b1, b2 = [open(p, encoding="utf-8").read() for p in sys.argv[1:5]]
wm, wg, w1, w2 = words(md), words(gs), words(b1), words(b2)
print("words: NOTE.md %d, PDF text (gs) %d, build1 text %d, build2 text %d" % (len(wm), len(wg), len(w1), len(w2)))
print("NOTE.md == PDF text (gs), word for word:", wm == wg)
print("build1 == build2, word for word:", w1 == w2, "; byte for byte:", b1 == b2)
print("build2 text == PDF text (gs), word for word:", w2 == wg)
if wm != wg:
    for i, (a, b) in enumerate(zip(wm, wg)):
        if a != b:
            print("first difference at word", i, repr(a), repr(b)); break
PY
