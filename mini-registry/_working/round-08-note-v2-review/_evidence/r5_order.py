#!/usr/bin/python3
"""Reviewer's own route to the order of the round's writes: Desktop Commander's own history of tool calls
(~/.claude-server-commander/tool-history.jsonl), every write or edit of the round's lists, the note and the report,
in the window of version 2's working session (21:11 to 21:25 UTC). Read only."""
import json, os, re
H = os.path.expanduser("~/.claude-server-commander/tool-history.jsonl")
want = re.compile(r"round-08-note-v2/_evidence/(CLAIMS|LIMITS|PAIRS)\.md|docs/NOTE\.md|REPORT_NOTE_2026-10-31_v2\.md")
print("history:", H)
n = 0
for ln in open(H, encoding="utf-8"):
    try:
        r = json.loads(ln)
    except Exception:
        continue
    t = r.get("timestamp", "")
    if not ("2026-10-31T21:1" in t or "2026-10-31T21:2" in t):
        continue
    tool = r.get("toolName", "")
    a = r.get("arguments", {}) or {}
    p = a.get("path") or a.get("file_path") or ""
    cmd = a.get("command", "") if tool == "start_process" else ""
    if tool in ("write_file", "edit_block") and want.search(p):
        n += 1
        extra = ""
        if p.endswith("CLAIMS.md"):
            c = a.get("content", "") or a.get("new_string", "")
            extra = " K-rows in this call: %d; K41c present: %s" % (len(re.findall(r"^\| K", c, re.M)), "| K41c |" in c)
        print(t, tool, a.get("mode", ""), p, extra)
    elif tool == "start_process" and want.search(cmd) and re.search(r"(>|tee|cp |mv |sed -i|cat <<)", cmd):
        print(t, "start_process (writes?)", cmd[:200].replace("\n", " "))
print("calls listed:", n)
