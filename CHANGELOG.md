# Changelog

## 1.2.0 — 2026-11-01

Everything below runs inside the same single file. No dependency was added, no request is
made after load, and the app still opens from `file://` with the Wi-Fi off.

**Search**
- **Query operators.** `"exact phrase"`, `-exclude` and `a or b` are parsed properly instead of
  being treated as literal words. Quoted phrases match across the path separators.
- **Typo tolerance.** When nothing matches at all, terms are retried against a vocabulary built
  from the rubric names at load time, at edit distance 1 including transpositions — so
  `burnign headache` still finds *burning headache*.
- **Browse by chapter.** The book's own tree, expanded lazily, with a count per chapter.
- **Saved searches**, and a **remedy alias table** so *Gelsemium* finds the source's *Gels*.
- **Similar rubrics** — computed from the words of the rubric name inside the same chapter, and
  labelled as a heuristic rather than a curated cross-reference.

**Repertorisation**
- **Must-have rubrics** (Boenninghausen-style elimination): remedies that miss one are faded, or
  filtered out entirely.
- **Configurable grade weights** (1/2/3), printed on the chart and in the print sheet so a chart
  stays auditable.
- **Filter the chart** by remedy name; **undo** the last selection change with `Ctrl`/`Cmd + Z`.

**Cases**
- **Encrypted vault.** AES-256-GCM with a key derived by PBKDF2-SHA256 (200,000 rounds) in the
  browser; the passphrase is never stored. Verified by `scripts/vault_test.mjs`.
- **Patient grouping and case search**, autosaved draft, **one-page A4 case sheet**, **CSV export**
  of a chart or of every case, **save to a file you choose** (File System Access, with a download
  fallback), and a **backup reminder** when cases exist and nothing has ever been exported.

**App**
- **Command palette** (`Ctrl`/`Cmd + K`), **per-rubric notes**, **settings** sheet with text size
  and a **high-contrast** theme alongside light/dark/auto.
- **Service worker**: HTML network-first, assets cache-first, `CACHE` bumped per release,
  `registration.update()` on load, and a **build stamp** so "am I on the new one?" is answerable
  from the page. Installable manifest on `play/`.
- **Data audit** panel in About, computed from the embedded dataset.
- **Deep links** extended: `?browse=1`, `?palette=1`, `?settings=1`.
- **Fixed** the blanket `button{background:accent}` rule that painted the tab control, the browse
  rows and every icon-only control accent-on-accent, leaving their labels invisible.
- **Tests**: `scripts/check.sh` runs a syntax check, 20 browser assertions and 6 crypto assertions.


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
