#!/bin/zsh
# The reviewer's own walk: one use of the screens as a school clerk, and one way the goal goes wrong.
# No window: curl on 127.0.0.1 only. Written by "MR · review · the goal built"; not the round's tests.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-review/_evidence
S=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
P=8139
B=http://127.0.0.1:$P
mkdir -p $E/screens
cd $S
count() { /usr/bin/python3 -c "import json;l=json.load(open('$S/data/learners.json'));print(len(l), max(x['learner_number'] for x in l))"; }
start_server() { PORT=$P node server.js > $E/server.$1.out 2>&1 & SP=$!; sleep 1; echo "server pid $SP: $(cat $E/server.$1.out)"; lsof -nP -a -p $SP -iTCP -sTCP:LISTEN | tail -n +2; }
stop_server() { kill $SP; wait $SP 2>/dev/null; echo "server stopped, pid $SP; listening on $P now: $(lsof -nP -iTCP:$P -sTCP:LISTEN | wc -l | tr -d ' ')"; }
show() { echo "--- $1 (HTTP $2)"; sed -n '/<main/,/<\/main>/p' $E/screens/$1; }

date -u +%Y-%m-%dT%H:%M:%SZ
echo '=== THE CLERK: from a fresh reset'
node reset.js
echo "learners (count, highest number): $(count)"
start_server walk
c=$(curl -s -o $E/screens/W0_SC-1.html -w '%{http_code}' $B/); show W0_SC-1.html $c
echo '=== (1) a child the registry holds: learner 12, Galtemzu / Jortovvin / 2013-11-27 / Dunavel Lakeside School, family name entered as gALTEMZU'
c=$(curl -s -o $E/screens/W1_held.html -w '%{http_code}' --data-urlencode 'family_name=gALTEMZU' --data-urlencode 'given_names=Jortovvin' --data-urlencode 'date_of_birth=2013-11-27' --data-urlencode 'school=Dunavel Lakeside School' $B/enrol); show W1_held.html $c
echo "learners after (1): $(count)"
echo '=== (2) a new child: Brannick / Solvey Amara / 2017-03-09 / Kestrin Hill School'
c=$(curl -s -o $E/screens/W2_new.html -w '%{http_code}' --data-urlencode 'family_name=Brannick' --data-urlencode 'given_names=Solvey Amara' --data-urlencode 'date_of_birth=2017-03-09' --data-urlencode 'school=Kestrin Hill School' $B/enrol); show W2_new.html $c
echo "learners after (2): $(count)"
/usr/bin/python3 -c "import json;print('saved:', json.load(open('$S/data/learners.json'))[-1])"
echo '=== (3) the new child again, the same four'
c=$(curl -s -o $E/screens/W3_again.html -w '%{http_code}' --data-urlencode 'family_name=Brannick' --data-urlencode 'given_names=Solvey Amara' --data-urlencode 'date_of_birth=2017-03-09' --data-urlencode 'school=Kestrin Hill School' $B/enrol); show W3_again.html $c
echo "learners after (3): $(count)"
echo '=== the way back from SC-3, followed'
c=$(curl -s -o $E/screens/W4_back.html -w '%{http_code}' $B/); echo "GET / -> HTTP $c, screen $(grep -o 'data-screen="SC-[0-9]"' $E/screens/W4_back.html)"
stop_server

echo
echo '=== THE WAY IT GOES WRONG: from a fresh reset, date of birth 2019-02-30, the school left out'
node reset.js
shasum -a 256 data/learners.json
start_server wrong
c=$(curl -s -o $E/screens/X1_refused.html -w '%{http_code}' --data-urlencode 'family_name=Brannick' --data-urlencode 'given_names=Solvey Amara' --data-urlencode 'date_of_birth=2019-02-30' $B/enrol); show X1_refused.html $c
echo '--- the same with the school sent empty, as SC-1 sends "(choose a school)"'
c=$(curl -s -o $E/screens/X2_refused_empty.html -w '%{http_code}' --data-urlencode 'family_name=Brannick' --data-urlencode 'given_names=Solvey Amara' --data-urlencode 'date_of_birth=2019-02-30' --data-urlencode 'school=' $B/enrol); show X2_refused_empty.html $c
shasum -a 256 data/learners.json
echo "learners: $(count)"
echo '--- the way back of SC-4, followed: the address its form names, with its hidden entries'
q=$(/usr/bin/python3 - $E/screens/X1_refused.html <<'PY'
import re,sys,html,urllib.parse
t=open(sys.argv[1]).read()
f=re.search(r'<form method="get" action="/">(.*?)</form>',t,re.S).group(1)
print(urllib.parse.urlencode([(m[0],html.unescape(m[1])) for m in re.findall(r'<input type="hidden" name="([^"]+)" value="([^"]*)">',f)]))
PY
)
echo "GET /?$q"
c=$(curl -s -o $E/screens/X3_back_kept.html -w '%{http_code}' "$B/?$q"); show X3_back_kept.html $c
stop_server
node reset.js
echo "after the final reset: $(count)"
date -u +%Y-%m-%dT%H:%M:%SZ
