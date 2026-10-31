'use strict';
// The checks of the requirements whose test docs/count/count.csv pairs with an element of
// the goal: R-01 to R-07, R-14, R-15, R-17, R-18, R-20 and R-22, each written from its test
// in docs/REQUIREMENTS.md; and R-21. R-20 and R-21 read the list of windows, as their tests say.
//
// Each check starts from a fresh reset: the reset's own build() (reset.js), its files written
// into a new folder of the system's temporary folder, so that no check writes the data under
// src/data/ that the other test files count. The server is started in the check on a free
// port of 127.0.0.1, and its screens are fetched with Node's own fetch and read as text.
// Every word a check looks for on a screen is written here from the brief, the register, the
// goal or a ruling; none is taken from lib/screens.js.

// ---- what Node can see of a window or a connection: recorded before anything is loaded ----
const childProcess = require('node:child_process');
// Kept before the wrapping below, for the checks' own reading of the list of windows (R-20, R-21):
// the one program the checks start, told apart from any program the prototype might launch.
const execFileUnwrapped = childProcess.execFile;
const launches = [];
for (const fn of ['spawn', 'spawnSync', 'exec', 'execSync', 'execFile', 'execFileSync', 'fork']) {
  const original = childProcess[fn];
  childProcess[fn] = function recorded(...args) {
    launches.push({ fn, command: String(args[0]) });
    return original.apply(this, args);
  };
}
const net = require('node:net');
const outbound = [];
const connect = net.Socket.prototype.connect;
net.Socket.prototype.connect = function recorded(...args) {
  // net.connect hands the socket its arguments normalised, as [options, callback].
  const o = Array.isArray(args[0]) ? args[0][0] : args[0];
  outbound.push(o && typeof o === 'object' ? String(o.host || o.path) : String(args[1]));
  return connect.apply(this, args);
};

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { build } = require('../reset');
const { start } = require('../server');
const { fileStore } = require('../lib/enrol');

// R-17, docs/REQUIREMENTS.md:235, written here.
const LINE = 'Invented data, Progressa is fictional';
const seen = [];
const dirs = [];

// ---- the list of windows on the computer's screen (R-20, R-21: docs/REQUIREMENTS.md:276-293) ----
// Read by CGWindowListCopyWindowInfo through osascript's JavaScript bridge: a command that brings
// nothing forward, asks no permission and opens no window (tried before this check was written:
// _working/round-06-build-v2/_evidence/W0_probe.log). Started by the checks only, never by the
// prototype. A reading is a Map from each window's number to its owner; a window added is a number
// in a later reading that the first did not hold.
const WINDOWS_JXA = 'ObjC.import("CoreGraphics"); ' +
  'var a = ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, 0)); var r = []; ' +
  'for (var i = 0; i < a.count; i++) { var d = a.objectAtIndex(i); ' +
  'r.push(ObjC.unwrap(d.objectForKey("kCGWindowNumber")) + "\\t" + ObjC.unwrap(d.objectForKey("kCGWindowOwnerPID")) + ' +
  '"\\t" + ObjC.unwrap(d.objectForKey("kCGWindowOwnerName"))); } r.join("\\n")';
const windowReads = [];
function readWindows() {
  windowReads.push('/usr/bin/osascript -l JavaScript -e <CGWindowListCopyWindowInfo>');
  return new Promise((resolve, reject) => {
    execFileUnwrapped('/usr/bin/osascript-absent', ['-l', 'JavaScript', '-e', WINDOWS_JXA],
      { timeout: 30000, maxBuffer: 16 * 1024 * 1024 }, (err, stdout, stderr) => {
        if (err) return reject(new Error('the list of windows could not be read: ' + err.message + ' ' + stderr));
        const list = new Map();
        for (const row of stdout.split('\n')) {
          if (!row.trim()) continue;
          const [number, pid, owner] = row.split('\t');
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

// R-21: the list read before the first check; then read again and again, each reading started as
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

// ---- helpers ----
function freshReset() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'mini-registry-check-'));
  const files = build();
  for (const name of Object.keys(files)) fs.writeFileSync(path.join(dir, name), files[name]);
  dirs.push(dir);
  return dir;
}

async function boot(opts) {
  const o = opts || {};
  const dir = o.dir || freshReset();
  const store = o.store ? o.store(fileStore(dir)) : fileStore(dir);
  const s = await start({ store, port: 0 });
  const conns = [];
  s.server.on('connection', (sock) => conns.push({ local: sock.localAddress, remote: sock.remoteAddress }));
  return {
    dir,
    base: 'http://127.0.0.1:' + s.port,
    address: s.server.address(),
    conns,
    close() {
      s.server.closeAllConnections();
      return new Promise((r) => s.server.close(r));
    },
  };
}

function screenOf(text) {
  const m = text.match(/data-screen="(SC-\d)"/);
  return m ? m[1] : null;
}

function wordsOf(html) {
  return html.replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/\s+/g, ' ').trim();
}

async function get(app, where) {
  const r = await fetch(app.base + where, { redirect: 'manual' });
  const text = await r.text();
  seen.push({ where: 'GET ' + where, status: r.status, text });
  return { status: r.status, text, words: wordsOf(text), screen: screenOf(text), location: r.headers.get('location') };
}

async function post(app, fields) {
  const r = await fetch(app.base + '/enrol', {
    method: 'POST',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(fields).toString(),
  });
  const text = await r.text();
  seen.push({ where: 'POST /enrol', status: r.status, text });
  return { status: r.status, text, words: wordsOf(text), screen: screenOf(text) };
}

const learnersOf = (app) => JSON.parse(fs.readFileSync(path.join(app.dir, 'learners.json'), 'utf8'));
const schoolsOf = (app) => JSON.parse(fs.readFileSync(path.join(app.dir, 'schools.json'), 'utf8'));
const numberShown = (words) => {
  const m = words.match(/[Ll]earner number:? (\d+)/);
  return m ? Number(m[1]) : null;
};

// A child the reset's data does not hold, made up here.
const child = (school) => ({
  family_name: 'Orlavin', given_names: 'Tesmira Kolva', date_of_birth: '2016-04-17', school,
});

test.after(() => {
  for (const d of dirs) fs.rmSync(d, { recursive: true, force: true });
});

// ---- the checks ----

test('R-01 — a child enrolled twice: the first enrolment adds one learner, the second none', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[0];
    const n0 = learnersOf(app).length;
    await post(app, child(s));
    const n1 = learnersOf(app).length;
    await post(app, child(s));
    const n2 = learnersOf(app).length;
    assert.equal(n1 - n0, 1);
    assert.equal(n2 - n1, 0);
  } finally { await app.close(); }
});

test('R-02 — the screens offer one goal, enrolling a learner, and no other', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[0];
    const pages = [
      await get(app, '/'),
      await post(app, child(s)),
      await post(app, child(s)),
      await post(app, Object.assign(child(s), { date_of_birth: '17/04/2016' })),
    ];
    // Every form and link of every screen: the enrolment form (POST /enrol) or the way back to SC-1.
    const targets = new Set();
    for (const p of pages) {
      for (const m of p.text.matchAll(/<form[^>]*method="(\w+)"[^>]*action="([^"]*)"/g)) targets.add(m[1] + ' ' + m[2]);
      for (const m of p.text.matchAll(/<a [^>]*href="([^"]*)"/g)) targets.add('get ' + m[1]);
    }
    assert.deepEqual(Array.from(targets).sort(), ['get /', 'post /enrol']);
    assert.equal((pages[0].text.match(/<form/g) || []).length, 1, 'SC-1 holds one form');
    assert.match(pages[0].words, /Enrol a learner/);
    // No screen for looking learners up (G-08): any other address goes back to SC-1.
    for (const where of ['/learners', '/search?family_name=Elpra', '/learner/1']) {
      const r = await get(app, where);
      assert.equal(r.status, 303, where);
      assert.equal(r.location, '/', where);
    }
  } finally { await app.close(); }
});

test('R-03 — the enrolment screen offers the four entries, and the record saved holds them as entered', async () => {
  const app = await boot();
  try {
    const sc1 = await get(app, '/');
    assert.equal(sc1.screen, 'SC-1');
    for (const [name, label] of [['family_name', 'Family name'], ['given_names', 'Given names'],
      ['date_of_birth', 'Date of birth'], ['school', 'School']]) {
      assert.match(sc1.text, new RegExp('name="' + name + '"'), name);
      assert.ok(sc1.words.includes(label), label);
    }
    // The school chosen from the data's 3 (ruling G-07).
    const offered = Array.from(sc1.text.matchAll(/<option value="([^"]+)"/g)).map((m) => m[1]);
    assert.deepEqual(offered.sort(), schoolsOf(app).slice().sort());
    const entry = { family_name: 'Orlavin', given_names: 'Tesmira  Kolva', date_of_birth: '2016-04-17', school: offered[1] };
    const r = await post(app, entry);
    assert.equal(r.screen, 'SC-3');
    const saved = learnersOf(app).find((l) => l.learner_number === numberShown(r.words));
    assert.deepEqual({ family_name: saved.family_name, given_names: saved.given_names,
      date_of_birth: saved.date_of_birth, school: saved.school }, entry);
  } finally { await app.close(); }
});

test('R-04 — in each enrolment the search is the first act on the data, before any write; the second has no write', async () => {
  const acts = [];
  const app = await boot({
    store: (inner) => ({
      schools: () => { acts.push('read schools'); return inner.schools(); },
      learners: () => { acts.push('read learners (the search)'); return inner.learners(); },
      saveLearners: (l) => { acts.push('write learners'); return inner.saveLearners(l); },
    }),
  });
  try {
    const s = schoolsOf(app)[0];
    acts.length = 0; // the schools are read once, when the server starts, before any enrolment
    await post(app, child(s));
    const first = acts.splice(0);
    await post(app, child(s));
    const second = acts.splice(0);
    assert.deepEqual(first, ['read learners (the search)', 'write learners']);
    assert.deepEqual(second, ['read learners (the search)']);
  } finally { await app.close(); }
});

test('R-05 — exactly F, G and D, and F and G in other capitals: the learner of the set-up shown, nothing new', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[2];
    const setUp = await post(app, child(s));
    const number = numberShown(setUp.words);
    const held = learnersOf(app).length;
    const exact = await post(app, child(s));
    const caps = await post(app, Object.assign(child(s), { family_name: 'ORLAVIN', given_names: 'TESMIRA KOLVA' }));
    for (const r of [exact, caps]) {
      assert.equal(r.screen, 'SC-2');
      assert.equal(numberShown(r.words), number);
      for (const v of ['Orlavin', 'Tesmira Kolva', '2016-04-17', s]) assert.ok(r.words.includes(v), v);
      assert.equal(learnersOf(app).length, held);
    }
  } finally { await app.close(); }
});

test('R-06 — none found, then a family name one letter different: one record saved each time, each a number not held before', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[1];
    const before = learnersOf(app);
    const heldNumbers = new Set(before.map((l) => l.learner_number));
    const a = child(s);
    const b = Object.assign(child(s), { family_name: 'Orlavan' });
    let count = before.length;
    for (const e of [a, b]) {
      const r = await post(app, e);
      assert.equal(r.screen, 'SC-3');
      const after = learnersOf(app);
      assert.equal(after.length - count, 1);
      count = after.length;
      const saved = after[after.length - 1];
      assert.equal(saved.learner_number, numberShown(r.words));
      assert.ok(!heldNumbers.has(saved.learner_number), 'number held before');
      heldNumbers.add(saved.learner_number);
      assert.deepEqual([saved.family_name, saved.given_names, saved.date_of_birth, saved.school],
        [e.family_name, e.given_names, e.date_of_birth, e.school]);
    }
  } finally { await app.close(); }
});

test('R-07 — the clerk sees which of the two happened, and the two screens say different things', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[0];
    const first = await post(app, child(s));
    const second = await post(app, child(s));
    assert.match(first.words, /new learner number was given/i);
    assert.ok(numberShown(first.words) !== null);
    assert.match(second.words, /existing learner was found/i);
    assert.equal(numberShown(second.words), numberShown(first.words));
    assert.doesNotMatch(first.words, /existing learner was found/i);
    assert.doesNotMatch(second.words, /new learner number was given/i);
    assert.notEqual(first.words, second.words);
  } finally { await app.close(); }
});

// The counts of R-09 to R-13 over the reset's files in a folder; the expected numbers are the
// brief's (lines 23 to 27), ages reckoned in completed years on 2026-10-31 (rulings G-06, Q-1).
function counts(dir) {
  const read = (n) => JSON.parse(fs.readFileSync(path.join(dir, n), 'utf8'));
  const lists = ['school_census', 'exam_candidate_list', 'social_grant_list'];
  const entries = new Map();
  for (const l of lists) for (const e of read(l + '.json')) entries.set(l + ':' + e.entry, Object.assign({ list: l }, e));
  const byChild = new Map();
  for (const r of read('key_table.json')) {
    if (!byChild.has(r.same_child)) byChild.set(r.same_child, []);
    byChild.get(r.same_child).push(entries.get(r.list_entry));
  }
  const multi = Array.from(byChild.values()).filter((es) => new Set(es.map((e) => e.list)).size >= 2);
  const age = (born) => {
    const [by, bm, bd] = born.split('-').map(Number);
    let a = 2026 - by;
    if (10 < bm || (10 === bm && 31 < bd)) a -= 1;
    return a;
  };
  return {
    children: byChild.size,
    schools: new Set(Array.from(entries.values()).map((e) => e.school)).size,
    on_more_than_one_list: multi.length,
    spelt_differently: multi.filter((es) => new Set(es.map((e) => e.family_name)).size > 1).length,
    ages_outside_6_to_12: Array.from(entries.values()).filter((e) => age(e.date_of_birth) < 6 || age(e.date_of_birth) > 12).length,
  };
}
const KNOWN = { children: 60, schools: 3, on_more_than_one_list: 8, spelt_differently: 4, ages_outside_6_to_12: 0 };

function resetInto(dir) {
  const files = build();
  for (const name of Object.keys(files)) fs.writeFileSync(path.join(dir, name), files[name]);
}

test('R-14 — reset, count, enrol one child, reset again, count again: both runs give the known numbers', async () => {
  const dir = freshReset();
  assert.deepEqual(counts(dir), KNOWN);
  const app = await boot({ dir });
  try {
    const r = await post(app, child(schoolsOf(app)[0]));
    assert.equal(r.screen, 'SC-3');
  } finally { await app.close(); }
  resetInto(dir);
  assert.deepEqual(counts(dir), KNOWN);
});

test('R-15 — reset, copy, enrol one child, reset again, copy: the two copies are the same, record by record', async () => {
  const dir = freshReset();
  const copy = () => Object.fromEntries(fs.readdirSync(dir).sort().map((n) => [n, fs.readFileSync(path.join(dir, n), 'utf8')]));
  const first = copy();
  const app = await boot({ dir });
  try {
    await post(app, child(schoolsOf(app)[0]));
  } finally { await app.close(); }
  assert.notEqual(fs.readFileSync(path.join(dir, 'learners.json'), 'utf8'), first['learners.json'], 'the enrolment changed the data');
  resetInto(dir);
  const second = copy();
  assert.deepEqual(Object.keys(second), Object.keys(first));
  let differ = 0;
  for (const n of Object.keys(first)) {
    const a = JSON.parse(first[n]);
    const b = JSON.parse(second[n]);
    const len = Math.max(a.length || 0, b.length || 0);
    for (let i = 0; i < len; i++) if (JSON.stringify(a[i]) !== JSON.stringify(b[i])) differ += 1;
  }
  assert.equal(differ, 0);
});

test('R-17 — every screen, shown in turn, says "Invented data, Progressa is fictional"', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[0];
    const shown = [
      await get(app, '/'),                                                        // SC-1
      await post(app, child(s)),                                                  // SC-3, a new learner saved
      await post(app, child(s)),                                                  // SC-2, an existing learner found
      await post(app, Object.assign(child(s), { family_name: '  ' })),            // SC-4
    ];
    fs.chmodSync(path.join(app.dir, 'learners.json'), 0o444);
    shown.push(await post(app, Object.assign(child(s), { family_name: 'Orlavek' }))); // SC-5 (F-6)
    fs.chmodSync(path.join(app.dir, 'learners.json'), 0o644);
    assert.deepEqual(shown.map((r) => r.screen), ['SC-1', 'SC-3', 'SC-2', 'SC-4', 'SC-5']);
    assert.equal(shown.filter((r) => !r.words.includes(LINE)).length, 0);
  } finally { await app.close(); }
});

test('R-18 — every connection has both its ends on this computer', async () => {
  const app = await boot();
  try {
    assert.equal(app.address.address, '127.0.0.1');
    const s = schoolsOf(app)[0];
    await get(app, '/');
    await post(app, child(s));
    await post(app, child(s));
    assert.ok(app.conns.length > 0);
    const outside = app.conns.filter((c) => c.local !== '127.0.0.1' || c.remote !== '127.0.0.1');
    assert.equal(outside.length, 0, JSON.stringify(outside));
    assert.ok(outbound.length > 0, 'the fetches were recorded');
    assert.equal(outbound.filter((h) => h !== '127.0.0.1').length, 0, JSON.stringify(outbound));
  } finally { await app.close(); }
});

test('R-20 — the list of windows read before and after: the prototype started, the data reset, a child enrolled through a windowless check, the prototype stopped; 0 windows added', async (t) => {
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
    assert.equal(launches.length, 0, JSON.stringify(launches));
    assert.equal(Object.keys(require.cache).filter((f) => f.endsWith('.node')).length, 0, 'a native addon loaded');
    const src = path.join(__dirname, '..');
    const served = Object.keys(require.cache).filter((f) => !f.startsWith(path.join(src, 'test')))
      .map((f) => path.relative(src, f)).sort();
    assert.deepEqual(served, ['lib/enrol.js', 'lib/lists.js', 'lib/names.js', 'lib/random.js',
      'lib/screens.js', 'lib/search.js', 'reset.js', 'server.js']);
  }
});

test('R-22 — on this computer the prototype starts and a child the registry does not hold is enrolled', async () => {
  const app = await boot();
  try {
    const r = await post(app, child(schoolsOf(app)[1]));
    assert.equal(r.status, 200);
    assert.equal(r.screen, 'SC-3');
    assert.ok(numberShown(r.words) > 0);
  } finally { await app.close(); }
});

test('R-17 — every screen any check of this file reached carries the line', () => {
  assert.ok(seen.length > 0);
  const without = seen.filter((p) => p.status !== 303 && !wordsOf(p.text).includes(LINE));
  assert.equal(without.length, 0, without.map((p) => p.where).join(', '));
});

test('R-21 — every check of this file ran to its end; the list of windows read before, while they ran and when they ended: 0 windows added at each reading', async (t) => {
  whileRunning.stopped = true;
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
  assert.equal(launches.length, 0, 'a program launched other than the checks\' own window reads: ' + JSON.stringify(launches));
});
