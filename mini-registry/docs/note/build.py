"""build.py — the note to the Permanent Secretary, built from its source.

    /usr/bin/python3 build.py

Reads ../NOTE.md (the source, the only place the note is written), makes NOTE.html beside this
file with Python's standard library, then NOTE.pdf from that HTML: one A4 page, 595.28 by 841.89
points, made by macOS's own text system (NSAttributedString reading the HTML, NSPrintOperation
saving the PDF to a file) through /usr/bin/osascript -l JavaScript. The script is given on standard
input. It shows no print panel and no progress panel and creates no window; the HTML names no
outside resource, so nothing is fetched. The PDF is a build: never edited by hand, made again from
the source. It is not sent; sending it is the owner's.

The type is 11 points (never below 10); where the note does not fit one page the build says so and
exits 1, and the cure is in the source, never a smaller type.
"""
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.normpath(os.path.join(HERE, "..", "NOTE.md"))
HTML_OUT = os.path.join(HERE, "NOTE.html")
PDF_OUT = os.path.join(HERE, "NOTE.pdf")

TYPE_PT = 11
MARGIN_MM = 20

# macOS's HTML reader takes one CSS pixel as one point of the page (a CSS "pt" comes out a third
# larger), so sizes are written in px and the build reads back the point sizes the page holds.
CSS = """
body { font-family: 'Times New Roman', Times, serif; font-size: %(pt)spx; line-height: 1.2; color: #000; }
h1 { font-size: %(h1)spx; font-weight: bold; margin: 0 0 5px 0; }
h2 { font-size: %(h2)spx; font-weight: bold; margin: 8px 0 3px 0; }
p { margin: 0 0 5px 0; text-align: left; }
p.to { margin: 0 0 7px 0; }
ul { margin: 0; padding-left: 14px; }
li { margin: 0 0 3px 0; }
""" % {"pt": TYPE_PT, "h1": TYPE_PT + 3, "h2": TYPE_PT + 1}


def inline(text):
    """Escape, then **bold**."""
    out = html.escape(text, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)


def to_html(md):
    blocks, para, items = [], [], []

    def flush():
        if para:
            text = " ".join(para)
            cls = ' class="to"' if text.startswith("**To ") else ""
            blocks.append("<p%s>%s</p>" % (cls, inline(text)))
            para.clear()
        if items:
            blocks.append("<ul>" + "".join("<li>%s</li>" % inline(i) for i in items) + "</ul>")
            items.clear()

    for line in md.splitlines():
        s = line.rstrip()
        if not s:
            flush()
        elif s.startswith("# "):
            flush()
            blocks.append("<h1>%s</h1>" % inline(s[2:]))
        elif s.startswith("## "):
            flush()
            blocks.append("<h2>%s</h2>" % inline(s[3:]))
        elif s.startswith("- "):
            if para:
                flush()
            items.append(s[2:])
        else:
            if items:
                flush()
            para.append(s)
    flush()
    title = re.sub(r"<[^>]+>", "", blocks[0])
    return ('<!DOCTYPE html>\n<html lang="en-GB"><head><meta charset="utf-8"><title>%s</title>'
            "<style>%s</style></head><body>\n%s\n</body></html>\n" % (title, CSS, "\n".join(blocks)))


JXA = r"""
ObjC.import('Cocoa');
function run(argv) {
  var src = argv[0], out = argv[1], mm = parseFloat(argv[2]);
  var data = $.NSData.dataWithContentsOfFile(src);
  var opts = $.NSMutableDictionary.alloc.init;
  opts.setObjectForKey($.NSHTMLTextDocumentType, $.NSDocumentTypeDocumentOption);
  opts.setObjectForKey($.NSNumber.numberWithInt(4), $.NSCharacterEncodingDocumentOption);
  var astr = $.NSAttributedString.alloc.initWithDataOptionsDocumentAttributesError(data, opts, null, null);
  var lo = 1e9, hi = 0, len = astr.length, txt = astr.string.js;
  for (var i = 0; i < len; i++) {
    if (txt.charAt(i).trim().length === 0) continue;
    var s = astr.attributeAtIndexEffectiveRange($.NSFontAttributeName, i, null).pointSize;
    if (s < lo) lo = s; if (s > hi) hi = s;
  }
  var pw = 595.28, ph = 841.89, m = mm * 72 / 25.4;
  var info = $.NSPrintInfo.sharedPrintInfo.copy;
  info.paperSize = $.NSMakeSize(pw, ph);
  info.topMargin = m; info.bottomMargin = m; info.leftMargin = m; info.rightMargin = m;
  info.horizontalPagination = $.NSFitPagination;
  info.verticalPagination = $.NSAutoPagination;
  info.verticallyCentered = false; info.horizontallyCentered = false;
  info.jobDisposition = $.NSPrintSaveJob;
  info.dictionary.setObjectForKey($.NSURL.fileURLWithPath(out), $.NSPrintJobSavingURL);
  var tv = $.NSTextView.alloc.initWithFrame($.NSMakeRect(0, 0, pw - 2 * m, 10));
  tv.textContainer.widthTracksTextView = true;
  tv.textStorage.setAttributedString(astr);
  tv.layoutManager.ensureLayoutForTextContainer(tv.textContainer);
  var used = tv.layoutManager.usedRectForTextContainer(tv.textContainer);
  tv.setFrameSize($.NSMakeSize(pw - 2 * m, used.size.height + 1));
  var op = $.NSPrintOperation.printOperationWithViewPrintInfo(tv, info);
  op.showsPrintPanel = false; op.showsProgressPanel = false;
  var ok = op.runOperation;
  return 'saved=' + ok + ' text_height_pt=' + used.size.height.toFixed(1) + ' usable_height_pt=' + (ph - 2 * m).toFixed(1)
    + ' smallest_type_pt=' + lo.toFixed(2) + ' largest_type_pt=' + hi.toFixed(2);
}
"""


def main():
    with open(SOURCE, encoding="utf-8") as f:
        md = f.read()
    page = to_html(md)
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print("source %s, %d bytes" % (SOURCE, len(md.encode("utf-8"))))
    print("wrote %s, %d bytes" % (HTML_OUT, len(page.encode("utf-8"))))
    r = subprocess.run(["/usr/bin/osascript", "-l", "JavaScript", "-", HTML_OUT, PDF_OUT, str(MARGIN_MM)],
                       input=JXA, capture_output=True, text=True, timeout=120)
    print("osascript exit %d: %s %s" % (r.returncode, r.stdout.strip(), r.stderr.strip()))
    if r.returncode != 0 or not os.path.exists(PDF_OUT):
        print("the PDF was not made")
        return 2
    m = re.search(r"text_height_pt=([\d.]+) usable_height_pt=([\d.]+)", r.stdout)
    print("wrote %s, %d bytes; type %d pt, margins %d mm" % (PDF_OUT, os.path.getsize(PDF_OUT), TYPE_PT, MARGIN_MM))
    t = re.search(r"smallest_type_pt=([\d.]+)", r.stdout)
    if not t or float(t.group(1)) < 10:
        print("type below 10 points, or not read: the build refuses it")
        return 1
    if not m or float(m.group(1)) > float(m.group(2)):
        print("the note does not fit one page: shorten the source, never the type")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
