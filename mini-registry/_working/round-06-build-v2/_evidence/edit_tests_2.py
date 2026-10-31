"""Version 2, second edit: the first run of the new R-21 (A2_tests.log of 20:00:09 UTC, kept as
A2_tests_first.log) read no list while goal.test.js's checks ran, since they end within about a
second and the reading waited half a second before its first start. The readings now follow one
another from the moment the first list is read until the last check stops them, each started
while the checks run. Each replacement must find its text exactly once in each file.
Usage: edit_tests_2.py <src folder>"""
import os, sys

src = sys.argv[1]
OLD = """// R-21: the list read before the first check, every half second while the checks run, and when
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
NEW = """// R-21: the list read before the first check; then read again and again, each reading started as
// the one before it ends, while the checks run; and read when they end (the last check of this file).
const whileRunning = { start: null, readings: [], stopped: false, pending: null };
function readWhileRunning() {
  if (whileRunning.stopped) return;
  const startedAt = new Date().toISOString();
  whileRunning.pending = readWindows()
    .then((list) => whileRunning.readings.push({ at: 'reading started ' + startedAt, list }))
    .catch((e) => whileRunning.readings.push({ at: 'reading started ' + startedAt, error: e.message }))
    .finally(() => { whileRunning.pending = null; readWhileRunning(); });
}
test.before(async () => {
  whileRunning.start = await readWindows();
  readWhileRunning();
});
"""
R21_OLD = """  clearInterval(whileRunning.timer);
  if (whileRunning.pending) await whileRunning.pending;
"""
R21_NEW = """  whileRunning.stopped = true;
  if (whileRunning.pending) await whileRunning.pending;
"""
out = {}
for rel in ('test/requirements.test.js', 'test/goal.test.js'):
    p = os.path.join(src, rel)
    s = open(p, encoding='utf8').read()
    for old, new in ((OLD, NEW), (R21_OLD, R21_NEW)):
        n = s.count(old)
        if n != 1:
            sys.exit('%s: a replacement found %d times, not once: %r' % (rel, n, old[:70]))
        s = s.replace(old, new)
    out[p] = s
for p, s in out.items():
    open(p, 'w', encoding='utf8').write(s)
    print('written', p, len(s.encode('utf8')), 'bytes')
