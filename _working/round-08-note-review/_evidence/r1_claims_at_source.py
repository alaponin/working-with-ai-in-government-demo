"""r1_claims_at_source.py — the reviewer's own route: for each row of the round's CLAIMS.md and
LIMITS.md, print the cited line in full, and whether the row's words stand in it.

    /usr/bin/python3 r1_claims_at_source.py CLAIMS.md LIMITS.md ROOT

Written by the reviewer; reads only; changes nothing. It splits a table row on ' | ' (space, bar,
space) so that a bar inside the words, written without spaces round it, is kept.
"""
import os
import sys


def rows(path, ncols):
    out = []
    for line in open(path, encoding="utf-8"):
        if line.startswith("| ") and not line.startswith("|---"):
            cells = line.rstrip("\n").strip()[2:-2].split(" | ")
            out.append(cells)
    return out[1:]


def at(root, src):
    path, ln = src.rsplit(":", 1)
    lines = open(os.path.join(root, path), encoding="utf-8").read().split("\n")
    return lines[int(ln) - 1]


def main():
    claims, limits, root = sys.argv[1:4]
    bad = 0
    for name, p, srccol, wordcol in (("CLAIM", claims, 2, 3), ("LIMIT", limits, 2, 3)):
        rs = rows(p, 0)
        print("== %s rows: %d" % (name, len(rs)))
        for r in rs:
            # rejoin cells beyond the expected count into the words column
            rid, what = r[0], r[1]
            src = r[srccol]
            words = " | ".join(r[wordcol:]) if name == "CLAIM" else r[wordcol]
            try:
                line = at(root, src)
            except Exception as e:  # noqa
                print("%s %s SOURCE UNREADABLE %s (%s)" % (name, rid, src, e))
                bad += 1
                continue
            ok = words in line
            bad += not ok
            print("%s %s %s | %s" % (name, rid, "found" if ok else "NOT FOUND", src))
            print("    says:  %s" % what)
            print("    words: %s" % words)
            print("    line:  %s" % line.strip()[:600])
    print("not found: %d" % bad)


if __name__ == "__main__":
    main()
