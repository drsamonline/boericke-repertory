#!/usr/bin/env python3
"""Draw this repository's badges as local SVG files.

An offline-first app should not need an image service to describe itself, and a
landing page that breaks its own promise on the first screen is a bad joke.
These are drawn here, committed, and referenced by relative path — they render
on GitHub Pages, in the README, and from `file://` with no network at all.

    python3 scripts/badges.py

Keep the claims true: the counts below are the ones the app prints in its own
status line, and the licence text is the one in LICENSE.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "docs", "assets")

INK = "#0b1412"        # label side — the landing page's ink
CREAM = "#eef1ee"      # value text
GREEN = "#0f6a51"      # offline / zero-dependency claims
SLATE = "#2c3d38"      # neutral facts
COPPER = "#8a4a1f"     # licence, the one claim with a condition

CH = 6.6  # approximate advance width of the 11px face used below

BADGES = [
    ("rubrics",  "rubrics",   "6,110",          SLATE),
    ("remedies", "remedies",  "1,461",          SLATE),
    ("chapters", "chapters",  "25",             SLATE),
    ("offline",  "offline",   "no network",     GREEN),
    ("deps",     "deps",      "0 runtime",      GREEN),
    ("file",     "single file", "891 kB",       INK),
    ("licence",  "licence",   "free · credit",  COPPER),
]


def badge(label, value, colour):
    lw = int(len(label) * CH) + 16
    vw = int(len(value) * CH) + 16
    total = lw + vw
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="22" role="img" '
        'aria-label="%s: %s">'
        "<title>%s: %s</title>"
        '<linearGradient id="s" x2="0" y2="100%%">'
        '<stop offset="0" stop-color="#fff" stop-opacity=".08"/>'
        '<stop offset="1" stop-color="#000" stop-opacity=".10"/></linearGradient>'
        '<clipPath id="r"><rect width="%d" height="22" rx="4" fill="#fff"/></clipPath>'
        '<g clip-path="url(#r)">'
        '<rect width="%d" height="22" fill="%s"/>'
        '<rect x="%d" width="%d" height="22" fill="%s"/>'
        '<rect width="%d" height="22" fill="url(#s)"/>'
        "</g>"
        '<g fill="%s" font-family="ui-sans-serif,Segoe UI,Helvetica,Arial,sans-serif" '
        'font-size="11" text-anchor="middle">'
        '<text x="%d" y="15">%s</text>'
        '<text x="%d" y="15">%s</text>'
        "</g></svg>"
    ) % (total, label, value, label, value, total, lw, INK, lw, vw, colour, total,
         CREAM, lw // 2, label, lw + vw // 2, value)


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, label, value, colour in BADGES:
        path = os.path.join(OUT, "badge-%s.svg" % name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(badge(label, value, colour))
        print("wrote", os.path.relpath(path))


if __name__ == "__main__":
    main()
