"""a1_claims.py — A1: each claim's source words at the line it gives; each sentence of the note paired
with claim rows.

    /usr/bin/python3 a1_claims.py CLAIMS.md PAIRS.md NOTE.md ROOT

CLAIMS.md rows: | claim | what | path:line | words |  (words may hold '|').
PAIRS.md rows:  | sentence number | the sentence, exactly as in the note | claims, comma-separated |
The note's sentences are cut from NOTE.md with its marks removed (#, **, the list's '- '), each line
cut after '. ' or a final '.'; the PAIRS sentences must be those, in order, each naming claims that
exist in CLAIMS.md.
"""
import os
import re
import sys


def rows(path):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("| ") and not line.startswith("|---"):
            cells = line.rstrip("\n").split("|")
            out.append([c.strip() for c in cells[1:-1]])
    return out[1:]  # the header row dropped


def sentences(note):
    out = []
    for line in open(note, encoding="utf-8"):
        s = line.strip()
        if not s:
            continue
        s = re.sub(r"^#+\s*", "", s)
        s = re.sub(r"^- ", "", s)
        s = s.replace("**", "")
        for part in re.split(r"(?<=\.)\s+(?=[A-Z])", s):
            out.append(part.strip())
    return out


def main():
    claims_path, pairs_path, note_path, root = sys.argv[1:5]
    claims, bad = {}, 0
    for r in rows(claims_path):
        cid, what, src, words = r[0], r[1], r[2], " | ".join(r[3:]).strip()  # a '|' inside the words, with its spaces
        path, line_no = src.rsplit(":", 1)
        lines = open(os.path.join(root, path), encoding="utf-8").read().split("\n")
        at = lines[int(line_no) - 1] if int(line_no) <= len(lines) else ""
        ok = words in at
        bad += not ok
        claims[cid] = ok
        print("%-5s %-9s %s:%s  «%s»" % (cid, "found" if ok else "NOT FOUND", path, line_no, words[:90]))
    print("claims: %d rows, %d not found" % (len(claims), bad))

    note_s = sentences(note_path)
    pairs = rows(pairs_path)
    unpaired = mismatch = unknown = 0
    for i, s in enumerate(note_s):
        if i >= len(pairs):
            print("UNPAIRED sentence %d: %s" % (i + 1, s))
            unpaired += 1
            continue
        p = pairs[i]
        if p[1] != s:
            print("MISMATCH at %d:\n  note:  %s\n  pairs: %s" % (i + 1, s, p[1]))
            mismatch += 1
        ids = [x.strip() for x in p[2].split(",") if x.strip()]
        missing = [x for x in ids if x not in claims and x != "none"]
        if not ids or missing:
            print("UNKNOWN claims for sentence %d: %s" % (i + 1, p[2]))
            unknown += 1
    extra = max(0, len(pairs) - len(note_s))
    print("note: %d sentences; pairs: %d rows; unpaired %d, mismatched %d, unknown claims %d, extra pairs %d"
          % (len(note_s), len(pairs), unpaired, mismatch, unknown, extra))
    print("%d not found" % bad)
    return 0 if bad == 0 and unpaired == mismatch == unknown == extra == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
