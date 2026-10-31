#!/bin/zsh
# The reviewer's own way the goal goes wrong: 2019-02-30 and the school left out, by curl on 127.0.0.1.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-v2-review/_evidence
SRC=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
PORT=8141
mkdir -p $E/screens
echo "# r2_wrong.sh started $(date -u +%Y-%m-%dT%H:%M:%SZ)"
/usr/bin/osascript -l JavaScript $E/windows.js | cut -f1 | sort > $E/win2.before.nums
echo "windows listed before: $(grep -c . $E/win2.before.nums)"
cd $SRC && node reset.js > /dev/null
echo "learners.json before: $(shasum -a 256 data/learners.json | cut -c1-16) learners $(node -e 'console.log(require("./data/learners.json").length)')"
PORT=$PORT node server.js > $E/server.wrong.out 2>&1 &
SP=$!
sleep 1
lsof -nP -iTCP:$PORT -sTCP:LISTEN | tail -n +2 | awk '{print "listening:", $1, $9}'
curl -s -o $E/screens/X1_refused.html -w 'POST /enrol (school left out): HTTP %{http_code}\n' \
  --data-urlencode 'family_name=Ostervald' --data-urlencode 'given_names=Mira Tamsin' \
  --data-urlencode 'date_of_birth=2019-02-30' http://127.0.0.1:$PORT/enrol
curl -s -o $E/screens/X2_refused_empty.html -w 'POST /enrol (school sent empty): HTTP %{http_code}\n' \
  --data-urlencode 'family_name=Ostervald' --data-urlencode 'given_names=Mira Tamsin' \
  --data-urlencode 'date_of_birth=2019-02-30' --data-urlencode 'school=' http://127.0.0.1:$PORT/enrol
echo "--- X1 as returned, the lines that say what it shows"
grep -n -E '<h1|<li|<p|value=|href=|Invented data|<option|type="hidden"|<form' $E/screens/X1_refused.html
echo "--- X2 differs from X1: $(cmp -s $E/screens/X1_refused.html $E/screens/X2_refused_empty.html && echo no || echo yes)"
# the way back, as the screen offers it
BACK=$(grep -o -E 'href="[^"]*"' $E/screens/X1_refused.html | head -1 | sed -e 's/href="//' -e 's/"$//' -e 's/&amp;/\&/g')
FORMACT=$(grep -o -E '<form[^>]*>' $E/screens/X1_refused.html | head -3)
echo "way back link: ${BACK:-none}; forms: $FORMACT"
echo "learners.json after: $(shasum -a 256 data/learners.json | cut -c1-16) learners $(node -e 'console.log(require("./data/learners.json").length)')"
kill $SP; wait $SP 2>/dev/null
sleep 0.5
echo "listening on $PORT now: $(lsof -nP -iTCP:$PORT -sTCP:LISTEN | tail -n +2 | grep -c .)"
/usr/bin/osascript -l JavaScript $E/windows.js | cut -f1 | sort > $E/win2.after.nums
echo "windows listed after: $(grep -c . $E/win2.after.nums); added: $(comm -13 $E/win2.before.nums $E/win2.after.nums | grep -c .)"
node reset.js > /dev/null
echo "# r2_wrong.sh ended $(date -u +%Y-%m-%dT%H:%M:%SZ)"
