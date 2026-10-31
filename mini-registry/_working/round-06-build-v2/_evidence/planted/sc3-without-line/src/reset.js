'use strict';
// The reset: makes the three lists and the key table (ruling Q-11), then enrols
// every list entry by the search rule, in the order of ruling Q-2 (the lists in
// the order of brief line 19, within each by entry number from 1), giving learner
// numbers from 1 (ruling Q-4). It writes the learners and the record of which
// entry made or found which learner (ruling Q-12), all as JSON under data/, and
// records every file it reads (ruling G-10). It reads nothing outside src/.
// Invented data, Progressa is fictional.

const fs = require('node:fs');
const path = require('node:path');
const { SEED } = require('./lib/random');
const { LISTS, generate } = require('./lib/lists');
const { enrol } = require('./lib/search');

const SRC = __dirname;
const DATA = path.join(SRC, 'data');

function json(value) {
  return JSON.stringify(value, null, 2) + '\n';
}

// Every file the reset reads: itself and every module it loads, found from the
// module tree Node itself keeps. The reset reads no other file.
function readsOfReset() {
  const self = require.cache[__filename];
  const seen = new Set();
  const stack = [self];
  while (stack.length) {
    const m = stack.pop();
    if (!m || seen.has(m.filename)) continue;
    seen.add(m.filename);
    for (const child of m.children) stack.push(child);
  }
  return Array.from(seen).map((f) => ({
    file: path.relative(SRC, f).split(path.sep).join('/'),
    under_src: !path.relative(SRC, f).startsWith('..') && !path.isAbsolute(path.relative(SRC, f)),
  })).sort((a, b) => (a.file < b.file ? -1 : a.file > b.file ? 1 : 0));
}

// The data, as the bytes of each file under data/, made in memory.
function build() {
  const { lists, keyTable, schools } = generate(SEED);
  const learners = [];
  const enrolments = [];
  for (const list of LISTS) {
    for (const e of lists[list]) {
      const result = enrol(learners, e);
      enrolments.push({ list_entry: list + ':' + e.entry, learner_number: result.learner_number });
    }
  }
  const files = {};
  files['schools.json'] = json(schools);
  for (const list of LISTS) files[list + '.json'] = json(lists[list]);
  files['key_table.json'] = json(keyTable);
  files['learners.json'] = json(learners);
  files['enrolments.json'] = json(enrolments);
  files['reads.json'] = json(readsOfReset());
  return files;
}

function reset() {
  const files = build();
  fs.mkdirSync(DATA, { recursive: true });
  for (const name of Object.keys(files).sort()) {
    fs.writeFileSync(path.join(DATA, name), files[name]);
  }
  return files;
}

module.exports = { build, reset };

if (require.main === module) {
  const files = reset();
  for (const name of Object.keys(files).sort()) {
    process.stdout.write('wrote data/' + name + ' ' + Buffer.byteLength(files[name]) + ' bytes\n');
  }
}
