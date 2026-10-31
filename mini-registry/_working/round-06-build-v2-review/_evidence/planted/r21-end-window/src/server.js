'use strict';
// The prototype's server: Node's own http module, listening on 127.0.0.1 only, serving
// the five screens of the goal. It opens no window and asks the system to open none:
// the clerk, or a windowless check, reads the screens at the address it prints.
//
//   GET  /        SC-1, the enrolment screen (the four entries kept where the way back
//                 from SC-4 or SC-5 carries them, Q-8, Q-13)
//   POST /enrol   the goal, by lib/enrol.js: SC-2, SC-3, SC-4 or SC-5
//   anything else is sent back to SC-1 (303); there is no other screen.
//
// Invented data, Progressa is fictional.

const http = require('node:http');
const path = require('node:path');
const { FIELDS, fileStore, enrolLearner } = require('./lib/enrol');
const screens = require('./lib/screens');

const HOST = '127.0.0.1';
const DEFAULT_PORT = 8126;

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on('data', (c) => chunks.push(c));
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

// Only the four entries are taken from what is sent; any other field is not read.
function fieldsOf(params) {
  const fields = {};
  for (const f of FIELDS) if (params.has(f)) fields[f] = params.get(f);
  return fields;
}

function send(res, status, html) {
  res.writeHead(status, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
  res.end(html);
}

function handler(store, schools) {
  return async (req, res) => {
    const url = new URL(req.url, 'http://' + HOST);
    try {
      if (req.method === 'GET' && url.pathname === '/') {
        return send(res, 200, screens.sc1(schools, fieldsOf(url.searchParams)));
      }
      if (req.method === 'POST' && url.pathname === '/enrol') {
        const fields = fieldsOf(new URLSearchParams(await readBody(req)));
        const r = enrolLearner(fields, store, schools);
        if (r.screen === 'SC-2') return send(res, 200, screens.sc2(r.learner));
        if (r.screen === 'SC-3') return send(res, 200, screens.sc3(r.learner));
        if (r.screen === 'SC-4') return send(res, 200, screens.sc4(r.faults, r.entry));
        return send(res, 200, screens.sc5(r.entry));
      }
      res.writeHead(303, { Location: '/' });
      return res.end();
    } catch (err) {
      // A fault the goal does not name (a data file that cannot be read): the entry cannot
      // be completed, and nothing was saved, on SC-5; no sixth screen.
      return send(res, 500, screens.sc5(null));
    }
  };
}

// Starts the server on 127.0.0.1 and the given port (0: a free one). The data is the
// reset's, under dataDir, or the store given.
function start(options) {
  const opts = options || {};
  const store = opts.store || fileStore(opts.dataDir || path.join(__dirname, 'data'));
  const schools = store.schools();
  const server = http.createServer(handler(store, schools));
  return new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(opts.port === undefined ? DEFAULT_PORT : opts.port, HOST, () => {
      resolve({ server, host: HOST, port: server.address().port, schools });
    });
  });
}

module.exports = { HOST, DEFAULT_PORT, start };

if (require.main === module) {
  const port = process.env.PORT === undefined ? DEFAULT_PORT : Number(process.env.PORT);
  start({ port }).then(({ host, port: p }) => {
    process.stdout.write('mini registry: http://' + host + ':' + p + '/ (Invented data, Progressa is fictional)\n');
  }, (err) => {
    process.stderr.write('mini registry: cannot start: ' + err.message + '\n');
    process.exitCode = 1;
  });
}
