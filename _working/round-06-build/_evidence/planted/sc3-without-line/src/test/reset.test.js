'use strict';
// The checks of the reset: made twice it gives the same bytes, which are the
// bytes data/ holds; and every file it reads is under src/ (ruling G-10, R-16).

const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { bytes, dataFiles, read } = require('../lib/data_files');
const { build } = require('../reset');

const WANT = [
  'enrolments.json', 'exam_candidate_list.json', 'key_table.json', 'learners.json',
  'reads.json', 'school_census.json', 'schools.json', 'social_grant_list.json',
];

test('R-15: the reset made twice gives byte for byte the same files', () => {
  const one = build();
  const two = build();
  assert.deepEqual(Object.keys(one).sort(), WANT);
  for (const name of WANT) assert.equal(Buffer.compare(Buffer.from(one[name]), Buffer.from(two[name])), 0, name);
});

test('R-15: data/ holds exactly what the reset makes, byte for byte', () => {
  assert.deepEqual(dataFiles(), WANT);
  const made = build();
  for (const name of WANT) assert.equal(bytes(name), made[name], name);
});

test('G-10, R-16: the reset\'s record of its reads names only files under src/', () => {
  const reads = read('reads.json');
  assert.ok(reads.length > 0);
  for (const r of reads) {
    assert.equal(r.under_src, true, r.file);
    assert.ok(!r.file.startsWith('..') && !path.isAbsolute(r.file), r.file);
    assert.match(r.file, /^(reset\.js|lib\/[a-z_]+\.js)$/, r.file);
  }
  assert.ok(reads.some((r) => r.file === 'reset.js'));
  assert.ok(reads.some((r) => r.file === 'lib/names.js'));
});
