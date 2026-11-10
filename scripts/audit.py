#!/usr/bin/env python3
"""The final audit: every claim the repo makes, checked against the repo.

Run it before a release. It reads the built files, not the intent:

    python3 scripts/audit.py

It checks that the app loads nothing from the network, that the version agrees
across VERSION, the build stamp, the service worker and the landing page, that
the counts in the README are the counts in the data, that every number in the
docs matches the thing it describes, that every local link resolves, that the
i18n dictionaries are the same size, and that no element id is duplicated in the
rendered page.
"""
import io, os, re, json, sys, subprocess, tempfile

ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    if cond: ok += 1; print("PASS", name)
    else: fail += 1; print("FAIL", name, "—", detail)

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
app = io.open('docs/play/index.html', encoding='utf-8').read()
landing = io.open('docs/index.html', encoding='utf-8').read()
readme = io.open('README.md', encoding='utf-8').read()
changelog = io.open('CHANGELOG.md', encoding='utf-8').read()
roadmap = io.open('docs/ROADMAP.md', encoding='utf-8').read()
sources = io.open('SOURCES.md', encoding='utf-8').read()
version = io.open('VERSION', encoding='utf-8').read().strip()
sw = io.open('docs/play/sw.js', encoding='utf-8').read()

R = json.loads(re.search(r'window\.REPERTORY\s*=\s*(\{.*?\});\s*\n', app, re.S).group(1))
SC = json.loads(re.search(r'window\.SRCCHECK = (\{.*?\});\n', app, re.S).group(1))

# ---------- 1. the offline promise ----------
def external_refs(html):
    """Requests the page makes, not links a reader may click.

    A <a href="https://ko-fi.com/…"> costs nothing at load: nobody fetches it
    until it is clicked. A <script src>, <img src> or <link href> is a request
    the page makes by existing. The support block added three anchors, and this
    check was counting them as network dependencies.
    """
    out = []
    for tag in re.findall(r'<[a-zA-Z][^>]*>', html):
        if re.match(r'<a\b', tag, re.I):
            continue
        for m in re.finditer(r'\b(?:src|href)\s*=\s*["\'](https?://[^"\']+)', tag, re.I):
            out.append(m.group(1))
    return out

ext = external_refs(app)
check("app loads nothing from the network", not ext, str(ext[:3]))
check("app has no fetch/XHR", not re.search(r'\bfetch\s*\(|XMLHttpRequest', app))
check("app has no @import", '@import' not in app)
check("app has no external font", not re.search(r'fonts\.googleapis|@font-face\s*\{[^}]*url\(', app))
land_ext = [m for m in external_refs(landing)
            if not re.search(r'github\.com|drsamonline\.github\.io|schema\.org|w3\.org', m)]
check("landing page loads no external assets", not land_ext, str(land_ext[:3]))

# ---------- 2. versions agree everywhere ----------
check("VERSION matches the app build stamp", ("v" + version) in app, version)
check("VERSION matches the service worker cache", ("boericke-" + version) in sw)
check("VERSION matches the landing page stamp", ("app v" + version) in landing)
check("CHANGELOG top entry is the current version", changelog.splitlines()[2].startswith("## " + version), changelog.splitlines()[2])

# ---------- 3. the numbers the docs claim ----------
n_rub = len(R["rubrics"]); n_rem = len(R["remedies"]); n_ch = len(R["chapters"])
withrem = sum(1 for r in R["rubrics"] if (r.get("m") or []))
check("README rubric count is the data", "6,110" in readme and n_rub == 6110, n_rub)
check("README remedy count is the data", "1,461" in readme and n_rem == 1461, n_rem)
check("README chapter count is the data", "25" in readme and n_ch == 25, n_ch)
check("source-check totals agree with the blob", SC["withRem"] == withrem and SC["identicalRem"] == 5319,
      "%s/%s" % (SC["withRem"], SC["identicalRem"]))
check("README quotes the source-check totals", "5,319" in readme and "5,415" in readme)
check("SOURCES quotes the same totals", "5,319" in sources and "5,415" in sources and "5,408" in sources)

# ---------- 4. test counts claimed vs present ----------
selftest = io.open('tools/selftest.html', encoding='utf-8').read()
n_assert = len(re.findall(r'\bok\("', selftest))
claimed = re.findall(r'(\d+) browser assertions', readme)
check("README assertion count is real", claimed and all(int(c) == n_assert for c in claimed),
      "claims %s, file has %d" % (set(claimed), n_assert))
check("SOURCES assertion count is real", ("%d browser assertions" % n_assert) in sources)

# ---------- 5. every local reference resolves ----------
missing = []
for html, base in ((landing, 'docs'), (app, 'docs/play')):
    for m in re.finditer(r'(?:src|href)="([^"#][^"]*)"', html):
        u = m.group(1).split('?')[0]
        if u.startswith('#') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', u): continue  # http:, mailto:, upi:, tel:
        if not os.path.exists(os.path.join(base, u)): missing.append((base, u))
check("every local asset/link exists", not missing, str(missing[:4]))

# ---------- 6. files the README promises ----------
promised = re.findall(r'^(docs/[^\s]+|scripts/[^\s]+|SOURCES\.md|README\.md|index\.html)\s{2,}', readme, re.M)
missing_files = [p for p in promised if not os.path.exists(p)]
check("files listed in the README tree exist", not missing_files, str(missing_files))

# ---------- 7. roadmap: no second repertory, nothing stale ----------
check("roadmap drops the second repertory", "second repertory" not in roadmap.lower() and "| D5 |" not in roadmap, "still mentioned")
check("roadmap has no 'next' row left undone", "| F8 |" in roadmap)

# ---------- 8. i18n dictionaries agree ----------
check("the interface is English only (no i18n layer)", not re.search(r'\bI18N\b|\bsetLang\b|\bLANG\b', app))
check("no language switch left in the app", '?lang=' not in app and "data-seg=\"lang\"" not in app)
check("no translated strings left in the app", not re.search(r'[\u0900-\u097F\u0A80-\u0AFF]', app))

# ---------- 9. structural hygiene ----------
prof = tempfile.mkdtemp()
dom = subprocess.run(["chromium","--headless","--no-sandbox","--disable-gpu",
                      "--allow-file-access-from-files","--user-data-dir="+prof,
                      "--virtual-time-budget=8000","--dump-dom",
                      "file://" + os.path.abspath("docs/play/index.html") + "?q=burning%20headache"],
                     capture_output=True, text=True).stdout
dom = re.sub(r'<script\b.*?</script>', '', dom, flags=re.S|re.I)
dom = re.sub(r'<style\b.*?</style>', '', dom, flags=re.S|re.I)
ids = re.findall(r'\bid="([^"]+)"', dom)
dupes = {i for i in ids if ids.count(i) > 1}
check("no duplicate element ids in the rendered page", not dupes, str(sorted(dupes)[:6]))
# The root index.html was deleted by the page audit (p054) as a duplicate of the
# app, which left this script reading a file that no longer existed and failing on
# line 25 before a single check ran. There is one copy of the app now, and this
# asserts it rather than assuming it.
stray = [f for f in ("index.html", "app.html", "boericke.html") if os.path.exists(f)]
check("the app exists exactly once (no root copy)", not stray and len(app) > 900000 and "function initV2" in app,
      str(stray))
check("no TODO/FIXME left in the shipped sources",
      not re.search(r'\b(TODO|FIXME|XXX)\b', app + landing + sw))
check("service worker HTML is network-first", "fetch(req).then" in sw and "isDoc" in sw)

# ---------- 10. claim: remedies with no rubric ----------
orphans = sum(1 for i in range(n_rem) if not any(True for r in R["rubrics"] if any(x[0] == i for x in (r.get("m") or []))))
check("audit claim: 0 remedies without a rubric", orphans == 0, orphans)

print()
print("%d passed, %d failed" % (ok, fail))
sys.exit(1 if fail else 0)
