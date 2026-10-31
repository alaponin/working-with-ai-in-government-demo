#!/bin/zsh
# R-20's test as the register gives it (docs/REQUIREMENTS.md:276-279), run by the reviewer:
# read the list of windows by a command that brings nothing forward (CGWindowListCopyWindowInfo
# through osascript's JavaScript bridge: no permission asked, no dialog, nothing brought forward),
# start the prototype, reset, enrol a child through a windowless check, stop, read the list again.
# Only window numbers and counts are kept; owners' names are printed only for a window added.
E=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/_working/round-06-build-review/_evidence
S=/Users/arnelaponin/Documents/Dev/wai-demo/mini-registry/src
winlist() {
  osascript -l JavaScript -e 'ObjC.import("CoreGraphics"); var a = ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, 0)); var r=[]; for (var i=0;i<a.count;i++){var d=a.objectAtIndex(i); r.push(ObjC.unwrap(d.objectForKey("kCGWindowNumber"))+"\t"+ObjC.unwrap(d.objectForKey("kCGWindowOwnerPID"))+"\t"+ObjC.unwrap(d.objectForKey("kCGWindowOwnerName")));} r.join("\n")'
}
date -u +%Y-%m-%dT%H:%M:%SZ
winlist > $E/.win.before; echo "windows listed before: $(wc -l < $E/.win.before | tr -d ' ')"
cd $S
PORT=8141 node server.js > $E/server.windows.out 2>&1 & SP=$!; sleep 1
node reset.js > /dev/null
c=$(curl -s -o /dev/null -w '%{http_code}' --data-urlencode 'family_name=Brannick' --data-urlencode 'given_names=Solvey Amara' --data-urlencode 'date_of_birth=2017-03-09' --data-urlencode 'school=Kestrin Hill School' http://127.0.0.1:8141/enrol)
echo "enrolled through curl on 127.0.0.1: HTTP $c"
winlist > $E/.win.during; echo "windows owned by the server's process $SP while it runs: $(awk -F'\t' -v p=$SP '$2==p' $E/.win.during | wc -l | tr -d ' ')"
kill $SP; wait $SP 2>/dev/null; node reset.js > /dev/null
winlist > $E/.win.after; echo "windows listed after: $(wc -l < $E/.win.after | tr -d ' ')"
cut -f1 $E/.win.before | sort > $E/.ids.before; cut -f1 $E/.win.after | sort > $E/.ids.after
echo "windows added (in the second list, not the first): $(comm -13 $E/.ids.before $E/.ids.after | wc -l | tr -d ' ')"
for id in $(comm -13 $E/.ids.before $E/.ids.after); do awk -F'\t' -v i=$id '$1==i{print "  added: window " $1 " owner " $3}' $E/.win.after; done
echo "windows owned by node, curl or osascript in the second list: $(awk -F'\t' '$3=="node"||$3=="curl"||$3=="osascript"' $E/.win.after | wc -l | tr -d ' ')"
rm -f $E/.win.before $E/.win.during $E/.win.after $E/.ids.before $E/.ids.after
date -u +%Y-%m-%dT%H:%M:%SZ
