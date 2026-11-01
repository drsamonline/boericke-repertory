#!/usr/bin/env python3
"""Draw the repository's social preview card locally — 1280x630 PNG.

The Open Graph image used to be fetched from an image service at page-view time,
which is a strange thing for an offline-first project to depend on. This renders
the same idea from local HTML in headless Chromium, commits the PNG, and the page
points at it by relative path.

    python3 scripts/social.py
"""
import os
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "docs", "assets", "social.png")
CHROME = shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")

CARD = """<!doctype html><meta charset="utf-8">
<style>
  html,body{margin:0;width:1280px;height:630px;overflow:hidden}
  body{
    background:#0b1412;color:#eef1ee;position:relative;
    font-family:ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    display:flex;flex-direction:column;justify-content:center;padding:0 84px;
  }
  .glow{position:absolute;width:760px;height:760px;right:-220px;top:-300px;border-radius:50%;
    background:radial-gradient(circle,#12664e 0%,rgba(18,102,78,0) 68%)}
  .head{display:flex;align-items:center;gap:20px;margin-bottom:30px;position:relative}
  .head svg{width:58px;height:58px;flex:none}
  .eyebrow{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:19px;letter-spacing:.22em;
    text-transform:uppercase;color:#7f9b92}
  h1{margin:0;font-size:92px;line-height:.95;letter-spacing:-.045em;font-weight:800;position:relative}
  h1 em{font-style:normal;color:#5ec8a0}
  p{margin:26px 0 0;font-size:26px;color:#a3b6af;max-width:860px;line-height:1.4;position:relative}
  .row{position:absolute;left:84px;bottom:58px;display:flex;gap:12px;align-items:center;
    font-family:ui-monospace,Menlo,Consolas,monospace;font-size:19px;color:#7f9b92}
  .pip{width:10px;height:10px;border-radius:50%;background:#5ec8a0;display:inline-block;margin-right:8px}
</style>
<div class="glow"></div>
<div class="head">
  <svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="11" fill="#9f1239"/>
  <g fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 11h13a5 5 0 0 1 5 5v21H17a5 5 0 0 1-5-5z"/><path d="M17 11v26"/><path d="M24 20h5M24 26h5"/></g></svg>
  <div class="eyebrow">Oscar E. Boericke, M.D. · 1927 · digitised</div>
</div>
<h1>The repertory,<br><em>indexed.</em></h1>
<p>6,110 rubrics · 1,461 remedies · 25 chapters — one HTML file, offline, no account.</p>
<div class="row"><span><i class="pip"></i>no network</span><span>·</span><span>0 dependencies</span><span>·</span><span>free to use</span></div>
"""


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "card.html")
        with open(page, "w", encoding="utf-8") as fh:
            fh.write(CARD)
        subprocess.run(
            [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size=1280,630",
             "--screenshot=" + OUT, "file://" + page],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    print("wrote", os.path.relpath(OUT, ROOT), os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
