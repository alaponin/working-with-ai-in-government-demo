#!/usr/bin/python3
"""Reviewer's own check: every row of the round's CLAIMS.md, its words looked up at path:line,
the full line printed so that it can be read against the note's sentence; and the note's
sentences matched against PAIRS.md by the reviewer's own split."""
import re, sys, datetime
ROOT = "/Users/arnelaponin/Documents/Dev/wai-demo"
EV = ROOT + "/mini-registry/_working/round-08-note-v2/_evidence"
print("run at", datetime.datetime.utcnow().isoformat() + "Z")
rows = []
for ln in open(EV + "/CLAIMS.md", encoding="utf-8"):
    if not ln.startswith("| K"):
        continue
    cells = [c.strip() for c in re.split(r" \| ", ln.strip().strip("|"))]
    if len(cells) < 4:
        print("BAD ROW", cells); continue
    if len(cells) > 4:  # a bar inside the words: keep it, joined back as written
        print("row with a bar inside its words:", cells[0])
        cells = cells[:3] + [" | ".join(cells[3:])]
    rows.append(cells)
nf = 0
for cid, what, src, words in rows:
    path, line = src.rsplit(":", 1)
    full = ROOT + "/" + path
    try:
        text = open(full, encoding="utf-8").read().split("\n")[int(line) - 1]
    except Exception as e:
        print(cid, "UNREADABLE", e); nf += 1; continue
    ok = words in text
    if not ok:
        nf += 1
    print("%s  %s  %s" % (cid, "found" if ok else "NOT FOUND", src))
    print("    claim: " + what)
    print("    words: " + words)
    print("    line : " + text[:900])
print("== CLAIM rows: %d; not found: %d" % (len(rows), nf))

# The note's sentences, by the reviewer's own split, against PAIRS.md
note = open(ROOT + "/mini-registry/docs/NOTE.md", encoding="utf-8").read()
sents = []
for para in note.split("\n"):
    p = para.strip()
    if not p:
        continue
    p = re.sub(r"^#+\s*", "", p)
    p = re.sub(r"^-\s*", "", p)
    p = p.replace("**", "")
    for s in re.split(r"(?<=[.])\s+(?=[A-Z])", p):
        if s.strip():
            sents.append(s.strip())
pairs = []
for ln in open(EV + "/PAIRS.md", encoding="utf-8"):
    m = re.match(r"\| (\d+) \| (.*) \| ([^|]*) \|\s*$", ln)
    if m:
        pairs.append((int(m.group(1)), m.group(2).strip(), [x.strip() for x in m.group(3).split(",")]))
print("== note sentences (reviewer's split): %d; PAIRS rows: %d" % (len(sents), len(pairs)))
ids = {r[0] for r in rows}
mism = 0
for i, s in enumerate(sents):
    ps = pairs[i][1] if i < len(pairs) else None
    same = (ps == s)
    if not same:
        mism += 1
    unknown = [k for k in (pairs[i][2] if i < len(pairs) else []) if k != "none" and k not in ids]
    print("%2d %s %s" % (i + 1, "same" if same else "DIFFERS", ("unknown claims " + str(unknown)) if unknown else ""))
    if not same:
        print("    note : " + s)
        print("    pairs: " + str(ps))
print("== sentences differing from PAIRS: %d" % mism)
used = set()
for _, _, ks in pairs:
    used.update(k for k in ks if k != "none")
print("== claim rows used by no sentence: %s" % sorted(ids - used))
