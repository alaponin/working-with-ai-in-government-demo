'use strict';
// The seeded generator (ruling Q-3: seed 20261031). mulberry32: the same seed
// gives the same sequence on every run, so the reset makes the data the same way.

const SEED = 20261031;

function makeRandom(seed) {
  let a = seed >>> 0;
  function next() {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }
  // A whole number from lo to hi, both included.
  function int(lo, hi) {
    return lo + Math.floor(next() * (hi - lo + 1));
  }
  function pick(items) {
    return items[int(0, items.length - 1)];
  }
  // Fisher-Yates, on a copy.
  function shuffle(items) {
    const out = items.slice();
    for (let i = out.length - 1; i > 0; i--) {
      const j = int(0, i);
      const tmp = out[i];
      out[i] = out[j];
      out[j] = tmp;
    }
    return out;
  }
  return { next, int, pick, shuffle };
}

module.exports = { SEED, makeRandom };
