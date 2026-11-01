# Changelog

## 1.1.0 — 2026-11-01

- **The landing page is its own design now.** `docs/index.html` was a brochure in the app's own
  palette; it is now a cool-ink, verdigris page with a grotesque display face, deliberately a
  different object from the warm-paper serif app. Light is the base palette, the system
  preference decides the first paint, and the header toggle is remembered under `brl_theme` —
  a separate key from the app's `br_theme`, so one never moves the other.
- **The demo is the app, not a picture of it.** The page embeds `play/` in a browser frame and
  drives it with four guided buttons (search, chart, remedy sheet, cases). The app screenshot
  sits behind the frame as a poster and is replaced only once the frame has loaded.
- **Deep links in the app.** `?q=`, `?pick=`, `?remedy=`, `?tab=` — dependency-free, works from
  `file://`, and it is what the guided demo drives. A view can now be linked or bookmarked.
- **Badges are drawn locally.** `scripts/badges.py` writes `docs/assets/badge-*.svg`; the README
  and the landing page reference them by relative path. Every `shields.io` and `socialify.git.ci`
  image is gone — an offline-first repo no longer needs the network to describe itself.
- **Icons and social card, generated.** `scripts/icons.py` rasterises `docs/icon.svg` into
  512/192/180/32 PNGs and a six-size `.ico`; `scripts/social.py` draws the 1280×630 card. Adds
  `docs/manifest.webmanifest`.
- **Fixed: the active tab was invisible.** A blanket `button{background:accent}` rule painted the
  segmented control accent-on-accent; the tabs are now transparent with a card-coloured pill.
- **`docs/ROADMAP.md`** — the enhancement list, each item held to "offline, no internet, no
  external dependency", including the releases-with-icons work.

## 1.0.0 — 2026-10-25

- **Licence: PolyForm Noncommercial 1.0.0.** Every repository now carries the canonical text
  from polyformproject.org with the Required Notice line, and the four places a repo states
  its licence agree: LICENSE, the SPDX headers, the README and package.json.
- **The public demo is the app.** A build now fails if `docs/play/index.html` is not the app,
  because a demo running older code is two code paths for one program.
