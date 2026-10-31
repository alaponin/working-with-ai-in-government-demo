'use strict';
// The checks of the goal: one for each way it can go wrong, F-1 to F-7 of docs/GOAL.md as the
// owner ruled them on docs/GOAL-QUESTIONS-PAPER.md (D-2026-10-31-07), each set up and seen
// handled as ruled (ruling G-12); the checks of S-3 as ruled (no age, Q-2; a real day, Q-1);
// the way back from each result screen (Q-13); R-17's line on every screen reached; and R-21,
// the list of windows read before, while and after the checks of this file run.
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
    execFileUnwrapped('/usr/bin/osascript', ['-l', 'JavaScript', '-e', WINDOWS_JXA],
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


// ---- helpers of the goal's checks ----

// A store that records every act on the data during the enrolments (Q-7: on a fault, none).
function traced(acts) {
  return (inner) => ({
    schools: () => inner.schools(),
    learners: () => { acts.push('read learners'); return inner.learners(); },
    saveLearners: (l) => { acts.push('write learners'); return inner.saveLearners(l); },
  });
}

const bytesOf = (app) => fs.readFileSync(path.join(app.dir, 'learners.json'), 'utf8');
const faultLines = (text) => Array.from(text.matchAll(/<li>([\s\S]*?)<\/li>/g)).map((m) => wordsOf(m[1]));

// The way back of a result screen, followed: the address it names, with its hidden entries.
async function followWayBack(app, r) {
  const form = r.text.match(/<form method="get" action="\/">([\s\S]*?)<\/form>/);
  if (form) {
    const params = new URLSearchParams();
    for (const m of form[1].matchAll(/<input type="hidden" name="([^"]+)" value="([^"]*)">/g)) {
      params.append(m[1], m[2].replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>').replace(/&amp;/g, '&'));
    }
    return { kept: true, sc1: await get(app, '/?' + params.toString()) };
  }
  const link = r.text.match(/<a href="([^"]+)">/);
  assert.ok(link, 'a way back');
  return { kept: false, sc1: await get(app, link[1]) };
}

function valuesOn(sc1) {
  const v = {};
  for (const m of sc1.text.matchAll(/<input type="text" id="[^"]+" name="([^"]+)" value="([^"]*)">/g)) v[m[1]] = m[2];
  const sel = sc1.text.match(/<option value="([^"]*)" selected>/);
  v.school = sel ? sel[1] : '';
  return v;
}

// A learner the reset's data holds: number 5 (read from the data, not assumed).
const heldLearner = (app) => learnersOf(app).find((l) => l.learner_number === 5);
const fieldsOf = (l) => ({ family_name: l.family_name, given_names: l.given_names, date_of_birth: l.date_of_birth, school: l.school });

// ---- the ways the goal goes wrong ----

test('F-1 — an entry missing, or of spaces only: refused on SC-4, each entry missing named; nothing read, nothing saved', async () => {
  const acts = [];
  const app = await boot({ store: traced(acts) });
  try {
    const s = schoolsOf(app)[0];
    const bytes = bytesOf(app);
    const cases = [
      [{ family_name: '' }, ['Family name']],
      [{ given_names: '' }, ['Given names']],
      [{ date_of_birth: '' }, ['Date of birth']],
      [{ school: '' }, ['School']],
      [{ family_name: '   ' }, ['Family name']],          // spaces only are missing (Q-4)
      [{ given_names: ' \t ' }, ['Given names']],
      [{ family_name: '', given_names: '', date_of_birth: '', school: '' },
        ['Family name', 'Given names', 'Date of birth', 'School']],
    ];
    for (const [over, named] of cases) {
      const r = await post(app, Object.assign(child(s), over));
      assert.equal(r.screen, 'SC-4', JSON.stringify(over));
      assert.match(r.words, /entry refused/i);
      const lines = faultLines(r.text);
      assert.deepEqual(lines.map((l) => l.split(':')[0]), named, JSON.stringify(over));
      for (const l of lines) assert.match(l, /not entered/);
    }
    // An entry not sent at all is missing too.
    const r = await post(app, { given_names: 'Tesmira Kolva', date_of_birth: '2016-04-17', school: s });
    assert.deepEqual(faultLines(r.text), ['Family name: not entered']);
    assert.deepEqual(acts, [], 'the data was read or written');
    assert.equal(bytesOf(app), bytes);
  } finally { await app.close(); }
});

test('F-2 — a date of birth not in the form YYYY-MM-DD, or naming no day: refused on SC-4; nothing read, nothing saved', async () => {
  const acts = [];
  const app = await boot({ store: traced(acts) });
  try {
    const s = schoolsOf(app)[0];
    const bytes = bytesOf(app);
    for (const d of ['17/04/2016', '2016-4-17', '20160417', ' 2016-04-17', '2016-04-17 ', '17 April 2016', '٢٠١٦-٠٤-١٧']) {
      const r = await post(app, Object.assign(child(s), { date_of_birth: d }));
      assert.equal(r.screen, 'SC-4', d);
      assert.deepEqual(faultLines(r.text), ['Date of birth: not in the form YYYY-MM-DD'], d);
    }
    for (const d of ['2019-02-30', '2015-02-29', '2016-13-01', '2016-00-10', '2016-04-31', '2016-04-00']) {
      const r = await post(app, Object.assign(child(s), { date_of_birth: d }));
      assert.equal(r.screen, 'SC-4', d);
      assert.equal(faultLines(r.text).length, 1, d);
      assert.match(faultLines(r.text)[0], /^Date of birth: .*no day/, d); // Q-1
    }
    assert.deepEqual(acts, []);
    assert.equal(bytesOf(app), bytes);
    // A real day, 29 February of a leap year, is taken.
    const ok = await post(app, Object.assign(child(s), { date_of_birth: '2016-02-29' }));
    assert.equal(ok.screen, 'SC-3');
  } finally { await app.close(); }
});

test('F-2, Q-2 — no age is reckoned on the entry: a child under 6, over 12, or born after 2026-10-31 is enrolled', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[1];
    let n = learnersOf(app).length;
    for (const d of ['2025-06-01', '2005-01-01', '2030-01-01']) {
      const r = await post(app, Object.assign(child(s), { date_of_birth: d }));
      assert.equal(r.screen, 'SC-3', d);
      assert.equal(learnersOf(app).length, n + 1, d);
      n += 1;
    }
  } finally { await app.close(); }
});

test('F-3 — a school not among the three, sent around SC-1: refused on SC-4; nothing read, nothing saved', async () => {
  const acts = [];
  const app = await boot({ store: traced(acts) });
  try {
    const bytes = bytesOf(app);
    for (const school of ['Arvenhold Academy', 'Velmora Primary']) {
      const r = await post(app, child(school));
      assert.equal(r.screen, 'SC-4', school);
      assert.equal(faultLines(r.text).length, 1);
      assert.match(faultLines(r.text)[0], /^School: not one of the (data's )?(3|three) schools$/);
    }
    assert.deepEqual(acts, []);
    assert.equal(bytesOf(app), bytes);
  } finally { await app.close(); }
});

test('F-1, F-2, F-3 at once (Q-9): every fault found is named on SC-4, in the order of the entries', async () => {
  const app = await boot();
  try {
    const bytes = bytesOf(app);
    const r = await post(app, { family_name: '', given_names: 'Tesmira Kolva', date_of_birth: '2016-02-30', school: 'Arvenhold Academy' });
    assert.equal(r.screen, 'SC-4');
    const lines = faultLines(r.text);
    assert.equal(lines.length, 3);
    assert.deepEqual(lines.map((l) => l.split(':')[0]), ['Family name', 'Date of birth', 'School']);
    assert.equal(bytesOf(app), bytes);
  } finally { await app.close(); }
});

test('F-4 — on the reset\'s data the search never finds more than one: each learner\'s three fields find that learner alone', async () => {
  const app = await boot();
  try {
    const learners = learnersOf(app);
    for (const l of learners) {
      const r = await post(app, fieldsOf(l));
      assert.equal(r.screen, 'SC-2', 'learner ' + l.learner_number);
      assert.equal(numberShown(r.words), l.learner_number);
    }
    assert.equal(learnersOf(app).length, learners.length);
  } finally { await app.close(); }
});

test('F-4 — more than one learner found: SC-5, the entry cannot be completed, nothing saved (set up by a record no clerk\'s entry can make)', async () => {
  // Under the data's settings F-4 is never reached (the check above); to see it handled, the
  // check itself writes a second learner sharing learner 5's three fields into its own folder.
  const dir = freshReset();
  const learners = JSON.parse(fs.readFileSync(path.join(dir, 'learners.json'), 'utf8'));
  const five = learners.find((l) => l.learner_number === 5);
  const highest = Math.max(...learners.map((l) => l.learner_number));
  learners.push(Object.assign({}, five, { learner_number: highest + 1, family_name: five.family_name.toUpperCase() }));
  fs.writeFileSync(path.join(dir, 'learners.json'), JSON.stringify(learners, null, 2) + '\n');
  const app = await boot({ dir });
  try {
    const bytes = bytesOf(app);
    const r = await post(app, fieldsOf(five));
    assert.equal(r.screen, 'SC-5');
    assert.match(r.words, /cannot be completed/i);
    assert.match(r.words, /nothing was saved/i);
    assert.equal(numberShown(r.words), null);
    assert.equal(bytesOf(app), bytes);
  } finally { await app.close(); }
});

test('F-5 — the same child entered with a difference but capitals: not caught, a new learner number, a second record', async () => {
  const app = await boot();
  try {
    const five = heldLearner(app);
    const variants = [
      { family_name: five.family_name.slice(0, -1) + (five.family_name.endsWith('e') ? 'a' : 'e') }, // one letter
      { family_name: five.family_name + ' ' },                                                        // a space
      { given_names: five.given_names.split(' ').reverse().join(' ') },                               // names in another order
      { given_names: five.given_names.replace(' ', '-') },                                            // a hyphen
      { family_name: 'É' + five.family_name.slice(1) },                                               // an accent
      { date_of_birth: five.date_of_birth.slice(0, 8) + String(Number(five.date_of_birth.slice(8)) + 1).padStart(2, '0') }, // a day
    ];
    let highest = Math.max(...learnersOf(app).map((l) => l.learner_number));
    for (const v of variants) {
      const n = learnersOf(app).length;
      const r = await post(app, Object.assign(fieldsOf(five), v));
      assert.equal(r.screen, 'SC-3', JSON.stringify(v));
      assert.match(r.words, /new learner number was given/i);
      assert.equal(numberShown(r.words), highest + 1, JSON.stringify(v));
      highest += 1;
      assert.equal(learnersOf(app).length, n + 1);
    }
    assert.deepEqual(heldLearner(app), five, 'the learner held is unchanged');
  } finally { await app.close(); }
});

test('F-6 — a record that cannot be saved: SC-5, nothing saved, no learner number given', async () => {
  const app = await boot();
  try {
    const file = path.join(app.dir, 'learners.json');
    const bytes = bytesOf(app);
    const highest = Math.max(...learnersOf(app).map((l) => l.learner_number));
    fs.chmodSync(file, 0o444); // the data's file cannot be written
    let r;
    try {
      r = await post(app, child(schoolsOf(app)[2]));
    } finally { fs.chmodSync(file, 0o644); }
    assert.equal(r.screen, 'SC-5');
    assert.match(r.words, /cannot be completed/i);
    assert.match(r.words, /nothing was saved/i);
    assert.equal(numberShown(r.words), null);
    assert.equal(bytesOf(app), bytes);
    // No number was used up: the same child, once the file can be written, gets the next one.
    const again = await post(app, child(schoolsOf(app)[2]));
    assert.equal(again.screen, 'SC-3');
    assert.equal(numberShown(again.words), highest + 1);
  } finally { await app.close(); }
});

test('F-7 — a different child sharing a learner\'s three fields, at another school: taken for that learner on SC-2, no notice, nothing saved', async () => {
  const app = await boot();
  try {
    const five = heldLearner(app);
    const other = schoolsOf(app).find((s) => s !== five.school);
    const bytes = bytesOf(app);
    const r = await post(app, { family_name: five.family_name.toLowerCase(), given_names: five.given_names,
      date_of_birth: five.date_of_birth, school: other });
    assert.equal(r.screen, 'SC-2');
    assert.equal(numberShown(r.words), five.learner_number);
    assert.ok(r.words.includes(five.school), 'the learner\'s own school shown (Q-10)');
    assert.ok(!r.words.includes(other), 'no notice of the school chosen (Q-11)');
    assert.equal(bytesOf(app), bytes);
  } finally { await app.close(); }
});

// ---- the way back (Q-13), and SC-4 keeping the entries (Q-8) ----

test('S-7, Q-13 — each result screen offers the way back to SC-1: empty after SC-2 and SC-3, the entries kept after SC-4 and SC-5', async () => {
  const app = await boot();
  try {
    const s = schoolsOf(app)[1];
    const sc3 = await post(app, child(s));
    const sc2 = await post(app, child(s));
    const refusedEntry = Object.assign(child(s), { family_name: 'O\'Rávin & "Sons" <b>', date_of_birth: '2016/04/17' });
    const sc4 = await post(app, refusedEntry);
    fs.chmodSync(path.join(app.dir, 'learners.json'), 0o444);
    let sc5;
    try {
      sc5 = await post(app, Object.assign(child(s), { family_name: 'Orlavek' }));
    } finally { fs.chmodSync(path.join(app.dir, 'learners.json'), 0o644); }
    assert.deepEqual([sc3.screen, sc2.screen, sc4.screen, sc5.screen], ['SC-3', 'SC-2', 'SC-4', 'SC-5']);
    for (const r of [sc3, sc2]) {
      const back = await followWayBack(app, r);
      assert.equal(back.sc1.screen, 'SC-1');
      assert.deepEqual(valuesOn(back.sc1), { family_name: '', given_names: '', date_of_birth: '', school: '' });
    }
    const back4 = await followWayBack(app, sc4);
    assert.equal(back4.sc1.screen, 'SC-1');
    const v4 = valuesOn(back4.sc1);
    assert.equal(wordsOf('<i>' + v4.family_name + '</i>'), refusedEntry.family_name);
    assert.deepEqual([v4.given_names, v4.date_of_birth, v4.school], [refusedEntry.given_names, refusedEntry.date_of_birth, s]);
    const back5 = await followWayBack(app, sc5);
    assert.deepEqual(valuesOn(back5.sc1), Object.assign(child(s), { family_name: 'Orlavek' }));
  } finally { await app.close(); }
});

test('R-17 — every screen any check of this file reached carries "Invented data, Progressa is fictional"', () => {
  const ids = new Set(seen.map((p) => screenOf(p.text)));
  assert.deepEqual(Array.from(ids).sort(), ['SC-1', 'SC-2', 'SC-3', 'SC-4', 'SC-5']);
  const without = seen.filter((p) => !wordsOf(p.text).includes(LINE));
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
