"""Version 2, gap G1 of the review: R-20 and R-21 read the list of windows before and after, as
their tests in docs/REQUIREMENTS.md say. This program makes the one change in the two test files
that hold a window check, src/test/requirements.test.js (R-20, R-21) and src/test/goal.test.js
(R-21), and nothing else. Each replacement must find its text exactly once, or nothing is written.
Usage: edit_tests.py <src folder>"""
import os, sys

src = sys.argv[1]

KEEP = """// ---- what Node can see of a window or a connection: recorded before anything is loaded ----
const childProcess = require('node:child_process');
const launches = [];
"""
KEEP_NEW = """// ---- what Node can see of a window or a connection: recorded before anything is loaded ----
const childProcess = require('node:child_process');
// Kept before the wrapping below, for the checks' own reading of the list of windows (R-20, R-21):
// the one program the checks start, told apart from any program the prototype might launch.
const execFileUnwrapped = childProcess.execFile;
const launches = [];
"""

HELPERS_AT = """const LINE = 'Invented data, Progressa is fictional';
const seen = [];
const dirs = [];
"""
HELPERS = HELPERS_AT + """
// ---- the list of windows on the computer's screen (R-20, R-21: docs/REQUIREMENTS.md:276-293) ----
// Read by CGWindowListCopyWindowInfo through osascript's JavaScript bridge: a command that brings
// nothing forward, asks no permission and opens no window (tried before this check was written:
// _working/round-06-build-v2/_evidence/W0_probe.log). Started by the checks only, never by the
// prototype. A reading is a Map from each window's number to its owner; a window added is a number
// in a later reading that the first did not hold.
const WINDOWS_JXA = 'ObjC.import("CoreGraphics"); ' +
  'var a = ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, 0)); var r = []; ' +
  'for (var i = 0; i < a.count; i++) { var d = a.objectAtIndex(i); ' +
  'r.push(ObjC.unwrap(d.objectForKey("kCGWindowNumber")) + "\\\\t" + ObjC.unwrap(d.objectForKey("kCGWindowOwnerPID")) + ' +
  '"\\\\t" + ObjC.unwrap(d.objectForKey("kCGWindowOwnerName"))); } r.join("\\\\n")';
const windowReads = [];
function readWindows() {
  windowReads.push('/usr/bin/osascript -l JavaScript -e <CGWindowListCopyWindowInfo>');
  return new Promise((resolve, reject) => {
    execFileUnwrapped('/usr/bin/osascript', ['-l', 'JavaScript', '-e', WINDOWS_JXA],
      { timeout: 30000, maxBuffer: 16 * 1024 * 1024 }, (err, stdout, stderr) => {
        if (err) return reject(new Error('the list of windows could not be read: ' + err.message + ' ' + stderr));
        const list = new Map();
        for (const row of stdout.split('\\n')) {
          if (!row.trim()) continue;
          const [number, pid, owner] = row.split('\\t');
          list.set(number, { pid: Number(pid), owner });
        }
        if (list.size === 0) return reject(new Error('the list of windows came back empty'));
        resolve(list);
      });
  });
}
function windowsAdded(before, after) {
  return Array.from(after.keys()).filter((n) => !before.has(n))
    .map((n) => 'window ' + n + ' of ' + after.get(n).owner + ' (pid ' + after.get(n).pid + ')');
}

// R-21: the list read before the first check, every half second while the checks run, and when
// they end (the last check of this file).
const whileRunning = { start: null, readings: [], timer: null, pending: null };
test.before(async () => {
  whileRunning.start = await readWindows();
  whileRunning.timer = setInterval(() => {
    if (whileRunning.pending) return;
    whileRunning.pending = readWindows()
      .then((list) => whileRunning.readings.push({ at: new Date().toISOString(), list }))
      .catch((e) => whileRunning.readings.push({ at: new Date().toISOString(), error: e.message }))
      .finally(() => { whileRunning.pending = null; });
  }, 500);
});
"""

R21_OLD = """test('R-21 — every check of this file ran to its end without launching a program (the window list itself: see the report)', () => {
  assert.equal(launches.length, 0, JSON.stringify(launches));
});
"""
R21_NEW = """test('R-21 — every check of this file ran to its end; the list of windows read before, while they ran and when they ended: 0 windows added at each reading', async (t) => {
  clearInterval(whileRunning.timer);
  if (whileRunning.pending) await whileRunning.pending;
  const end = await readWindows();
  const readings = whileRunning.readings.concat([{ at: 'when the checks ended', list: end }]);
  const refused = readings.filter((r) => r.error);
  assert.equal(refused.length, 0, refused.map((r) => r.at + ': ' + r.error).join('; '));
  const added = [];
  for (const r of readings) for (const w of windowsAdded(whileRunning.start, r.list)) added.push(r.at + ': ' + w);
  t.diagnostic('R-21: windows listed before the checks: ' + whileRunning.start.size + '; readings while they ran: ' +
    (readings.length - 1) + '; windows listed when they ended: ' + end.size + '; windows added at any reading: ' + added.length);
  assert.ok(readings.length >= 2, 'the list was read while the checks ran, and when they ended');
  assert.equal(added.length, 0, added.join('; '));
  assert.equal(launches.length, 0, 'a program launched other than the checks\\' own window reads: ' + JSON.stringify(launches));
});
"""

R20_OLD = """test('R-20 — a child enrolled through a windowless check: no program launched, nothing loaded that could open a window', async () => {
  const app = await boot();
  try {
    const r = await post(app, child(schoolsOf(app)[0]));
    assert.equal(r.screen, 'SC-3');
"""
R20_NEW = """test('R-20 — the list of windows read before and after: the prototype started, the data reset, a child enrolled through a windowless check, the prototype stopped; 0 windows added', async (t) => {
  const before = await readWindows();
  const app = await boot();
  let r;
  try {
    const files = build();
    for (const name of Object.keys(files)) fs.writeFileSync(path.join(app.dir, name), files[name]);
    r = await post(app, child(schoolsOf(app)[0]));
  } finally { await app.close(); }
  const after = await readWindows();
  const added = windowsAdded(before, after);
  t.diagnostic('R-20: windows listed before: ' + before.size + '; windows listed after: ' + after.size +
    '; windows added: ' + added.length);
  assert.equal(r.screen, 'SC-3');
  assert.equal(added.length, 0, added.join('; '));
  {
"""
R20_TAIL_OLD = """    assert.deepEqual(served, ['lib/enrol.js', 'lib/lists.js', 'lib/names.js', 'lib/random.js',
      'lib/screens.js', 'lib/search.js', 'reset.js', 'server.js']);
  } finally { await app.close(); }
});
"""
R20_TAIL_NEW = """    assert.deepEqual(served, ['lib/enrol.js', 'lib/lists.js', 'lib/names.js', 'lib/random.js',
      'lib/screens.js', 'lib/search.js', 'reset.js', 'server.js']);
  }
});
"""

HEAD_REQ_OLD = "// in docs/REQUIREMENTS.md; and R-21, as far as Node can see it.\n"
HEAD_REQ_NEW = "// in docs/REQUIREMENTS.md; and R-21. R-20 and R-21 read the list of windows, as their tests say.\n"
HEAD_GOAL_OLD = "// the way back from each result screen (Q-13); and R-17's line on every screen reached.\n"
HEAD_GOAL_NEW = ("// the way back from each result screen (Q-13); R-17's line on every screen reached; and R-21,\n"
                 "// the list of windows read before, while and after the checks of this file run.\n")

edits = {
    'test/requirements.test.js': [(HEAD_REQ_OLD, HEAD_REQ_NEW), (KEEP, KEEP_NEW), (HELPERS_AT, HELPERS),
                                  (R20_OLD, R20_NEW), (R20_TAIL_OLD, R20_TAIL_NEW), (R21_OLD, R21_NEW)],
    'test/goal.test.js': [(HEAD_GOAL_OLD, HEAD_GOAL_NEW), (KEEP, KEEP_NEW), (HELPERS_AT, HELPERS), (R21_OLD, R21_NEW)],
}
out = {}
for rel, pairs in edits.items():
    p = os.path.join(src, rel)
    s = open(p, encoding='utf8').read()
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            sys.exit('%s: a replacement found %d times, not once: %r' % (rel, n, old[:70]))
        s = s.replace(old, new)
    out[p] = s
for p, s in out.items():
    open(p, 'w', encoding='utf8').write(s)
    print('written', p, len(s.encode('utf8')), 'bytes')
