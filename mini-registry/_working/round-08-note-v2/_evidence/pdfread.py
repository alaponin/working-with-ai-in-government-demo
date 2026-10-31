"""pdfread.py — read a PDF's page count, page size and text by PDFKit, and the list of windows by
CGWindowListCopyWindowInfo; both through /usr/bin/osascript -l JavaScript, the script on standard
input. Neither opens, reveals or brings forward a window.

    /usr/bin/python3 pdfread.py info PDF
    /usr/bin/python3 pdfread.py text PDF
    /usr/bin/python3 pdfread.py windows          (one line per window: number, owner)
"""
import subprocess
import sys

PDF_JS = r"""
ObjC.import('Quartz');
function run(argv) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[1]));
  if (doc.isNil()) return 'cannot read';
  if (argv[0] === 'text') return doc.string.js;
  var out = ['pages=' + doc.pageCount];
  for (var i = 0; i < doc.pageCount; i++) {
    var b = doc.pageAtIndex(i).boundsForBox($.kPDFDisplayBoxMediaBox);
    out.push('page ' + (i + 1) + ': width=' + b.size.width.toFixed(2) + ' height=' + b.size.height.toFixed(2));
  }
  return out.join('\n');
}
"""

WIN_JS = r"""
ObjC.import('CoreGraphics'); ObjC.import('Foundation');
function run() {
  var a = ObjC.castRefToObject($.CGWindowListCopyWindowInfo($.kCGWindowListOptionAll, $.kCGNullWindowID));
  var o = [];
  for (var i = 0; i < a.count; i++) {
    var d = a.objectAtIndex(i);
    o.push(ObjC.unwrap(d.objectForKey('kCGWindowNumber')) + '\t' + ObjC.unwrap(d.objectForKey('kCGWindowOwnerName')));
  }
  return o.join('\n');
}
"""


def main():
    mode = sys.argv[1]
    if mode == "windows":
        r = subprocess.run(["/usr/bin/osascript", "-l", "JavaScript", "-"], input=WIN_JS,
                           capture_output=True, text=True, timeout=60)
    else:
        r = subprocess.run(["/usr/bin/osascript", "-l", "JavaScript", "-", mode, sys.argv[2]], input=PDF_JS,
                           capture_output=True, text=True, timeout=60)
    sys.stdout.write(r.stdout)
    if r.stderr:
        sys.stderr.write(r.stderr)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
