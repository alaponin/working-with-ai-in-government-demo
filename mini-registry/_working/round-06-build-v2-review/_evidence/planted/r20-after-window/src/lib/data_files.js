'use strict';
// Reads what the reset wrote under data/, for the checks in test/. The checks count these files; none
// takes an expected number from the modules that made the data.

const fs = require('node:fs');
const path = require('node:path');

const DATA = path.join(__dirname, '..', 'data');

function read(name) {
  return JSON.parse(fs.readFileSync(path.join(DATA, name), 'utf8'));
}

function bytes(name) {
  return fs.readFileSync(path.join(DATA, name), 'utf8');
}

function dataFiles() {
  return fs.readdirSync(DATA).filter((f) => f.endsWith('.json')).sort();
}

// The three lists by the names of brief line 19, as this check names them.
const LIST_NAMES = ['school_census', 'exam_candidate_list', 'social_grant_list'];

function load() {
  const lists = {};
  for (const l of LIST_NAMES) lists[l] = read(l + '.json');
  const keyTable = read('key_table.json');
  const childOf = new Map(keyTable.map((r) => [r.list_entry, r.same_child]));
  // Every entry, with its list, its name in the key table and its child.
  const entries = [];
  for (const l of LIST_NAMES) {
    for (const e of lists[l]) {
      const name = l + ':' + e.entry;
      entries.push(Object.assign({ list: l, list_entry: name, child: childOf.get(name) }, e));
    }
  }
  // Each child's entries, from the key table.
  const byChild = new Map();
  for (const e of entries) {
    if (!byChild.has(e.child)) byChild.set(e.child, []);
    byChild.get(e.child).push(e);
  }
  return {
    lists,
    keyTable,
    entries,
    byChild,
    schools: read('schools.json'),
    learners: read('learners.json'),
    enrolments: read('enrolments.json'),
    reads: read('reads.json'),
  };
}

// Completed years on a date, both given as YYYY-MM-DD.
function ageOn(born, on) {
  const [by, bm, bd] = born.split('-').map(Number);
  const [y, m, d] = on.split('-').map(Number);
  let age = y - by;
  if (m < bm || (m === bm && d < bd)) age -= 1;
  return age;
}

// YYYY-MM-DD, and a day that exists in the calendar.
function isIsoDate(s) {
  if (typeof s !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return false;
  const [y, m, d] = s.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return dt.getUTCFullYear() === y && dt.getUTCMonth() === m - 1 && dt.getUTCDate() === d;
}

module.exports = { DATA, LIST_NAMES, read, bytes, dataFiles, load, ageOn, isIsoDate };
