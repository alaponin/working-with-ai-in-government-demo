#!/bin/zsh
# The screens as the server returned them in this round: `node server.js` (package.json's start script) on src/data, as a clerk
# would use it, read with curl on 127.0.0.1 (no window); the listening socket read with lsof;
# the server stopped; then `node reset.js`, so that src/data is again what the reset makes.
M=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry
E=$M/_working/round-06-build/_evidence
S=$E/screens
mkdir -p $S
cd $M/src
date -u +%FT%TZ
echo '$ PORT=8126 node server.js   (the start script of package.json, run directly so that its process is the one stopped)'
PORT=8126 node server.js > $E/server.out 2>&1 &
SERVER=$!
for i in {1..50}; do curl -s --noproxy '*' -o /dev/null http://127.0.0.1:8126/ && break; sleep 0.1; done
echo '$ lsof -nP -iTCP:8126 -sTCP:LISTEN'
lsof -nP -iTCP:8126 -sTCP:LISTEN
post() { curl -s --noproxy '*' -o "$S/$1.html" -w "$1 HTTP %{http_code}\n" -X POST http://127.0.0.1:8126/enrol "${@:2}"; }
curl -s --noproxy '*' -o $S/1_SC-1.html -w "1_SC-1 HTTP %{http_code}\n" http://127.0.0.1:8126/
post 2_new --data-urlencode 'family_name=Orlavin' --data-urlencode 'given_names=Tesmira Kolva' --data-urlencode 'date_of_birth=2016-04-17' --data-urlencode 'school=Kestrin Hill School'
post 3_again --data-urlencode 'family_name=ORLAVIN' --data-urlencode 'given_names=tesmira kolva' --data-urlencode 'date_of_birth=2016-04-17' --data-urlencode 'school=Kestrin Hill School'
post 4_refused --data-urlencode 'family_name= ' --data-urlencode 'given_names=Tesmira Kolva' --data-urlencode 'date_of_birth=2019-02-30' --data-urlencode 'school=Arvenhold Academy'
chmod 444 data/learners.json
post 5_cannot --data-urlencode 'family_name=Orlavek' --data-urlencode 'given_names=Tesmira Kolva' --data-urlencode 'date_of_birth=2016-04-17' --data-urlencode 'school=Kestrin Hill School'
chmod 644 data/learners.json
curl -s --noproxy '*' -o $S/6_back_kept.html -w "6_back_kept HTTP %{http_code}\n" 'http://127.0.0.1:8126/?family_name=+&given_names=Tesmira+Kolva&date_of_birth=2019-02-30&school=Arvenhold+Academy'
curl -s --noproxy '*' -o /dev/null -w "7_lookup HTTP %{http_code} -> %{redirect_url}\n" http://127.0.0.1:8126/learners
echo '$ node -e learners after the walk'
node -e "const l=require('./data/learners.json');console.log('learners',l.length,'last',JSON.stringify(l[l.length-1]))"
kill $SERVER; wait $SERVER 2>/dev/null
echo 'server stopped'; cat $E/server.out
echo '$ node reset.js'
node reset.js
node -e "const l=require('./data/learners.json');console.log('learners after reset',l.length)"
echo '$ grep -c "Invented data, Progressa is fictional" screens/*.html'
grep -c 'Invented data, Progressa is fictional' $S/*.html
date -u +%FT%TZ
