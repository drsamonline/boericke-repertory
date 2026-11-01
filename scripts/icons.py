#!/usr/bin/env python3
"""Rasterise docs/icon.svg into the PNG sizes the manifest and the releases need.

One source of truth (the SVG), rendered locally with headless Chromium and then
downscaled with Pillow. No icon service, no download, nothing to trust.

    python3 scripts/icons.py
"""
import os
import shutil
import subprocess
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SVG = os.path.join(ROOT, "docs", "icon.svg")
OUT = os.path.join(ROOT, "docs", "assets")
SIZES = [512, 192, 180, 32]
CHROME = shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")


def render(size):
    """Render the SVG at `size` px square, transparent background."""
    wrapper = (
        '<!doctype html><meta charset="utf-8">'
        '<style>html,body{margin:0;background:transparent}'
        'img{display:block;width:%dpx;height:%dpx}</style>'
        '<img src="file://%s" alt="">' % (size, size, SVG)
    )
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "icon.html")
        with open(page, "w", encoding="utf-8") as fh:
            fh.write(wrapper)
        png = os.path.join(tmp, "icon.png")
        subprocess.run(
            [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--default-background-color=00000000", "--window-size=%d,%d" % (size, size),
             "--screenshot=" + png, "file://" + page],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        return Image.open(png).convert("RGBA")


def main():
    os.makedirs(OUT, exist_ok=True)
    big = render(512)
    for size in SIZES:
        img = big if size == 512 else big.resize((size, size), Image.LANCZOS)
        path = os.path.join(OUT, "icon-%d.png" % size)
        img.save(path, "PNG", optimize=True)
        print("wrote", os.path.relpath(path, ROOT), img.size)

    # Windows wants an .ico with several sizes inside one file; Pillow writes it.
    ico = os.path.join(OUT, "icon.ico")
    big.save(ico, "ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("wrote", os.path.relpath(ico, ROOT), os.path.getsize(ico), "bytes")


if __name__ == "__main__":
    main()
