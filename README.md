<div align="center">

# Boericke's Repertory

<img src="docs/assets/badge-rubrics.svg" alt="rubrics: 6,110" height="22"> <img src="docs/assets/badge-remedies.svg" alt="remedies: 1,461" height="22"> <img src="docs/assets/badge-chapters.svg" alt="chapters: 25" height="22"> <img src="docs/assets/badge-offline.svg" alt="offline: no network" height="22"> <img src="docs/assets/badge-deps.svg" alt="dependencies: 0 runtime" height="22"> <img src="docs/assets/badge-file.svg" alt="single file: 889 kB" height="22"> <img src="docs/assets/badge-licence.svg" alt="licence: free use, attribution required" height="22">

### A classic clinical repertory, made searchable — one HTML file, offline, no account, no server

**Compiled and designed by Dr. Sohil Momin** · after *Oscar E. Boericke, M.D. (1927)*

[**Landing page**](https://drsamonline.github.io/boericke-repertory/) &nbsp;·&nbsp;
[**Live app**](https://drsamonline.github.io/boericke-repertory/play/) &nbsp;·&nbsp;
[**Releases**](https://github.com/drsamonline/boericke-repertory/releases/latest) &nbsp;·&nbsp;
[**Roadmap**](docs/ROADMAP.md) &nbsp;·&nbsp;
[**Licence**](LICENSE)

[Windows `.exe`](https://github.com/drsamonline/boericke-repertory/releases/latest/download/boericke-repertory-portable.exe) &nbsp;·&nbsp;
[Android `.apk`](https://github.com/drsamonline/boericke-repertory/releases/latest/download/boericke-repertory.apk) &nbsp;·&nbsp;
[`index.html`](https://github.com/drsamonline/boericke-repertory/raw/main/index.html)

</div>

<!-- shot:start -->

![Screenshot](docs/shot.png)

<!-- shot:end -->

<div align="center">

| Search | Repertorisation |
| :---: | :---: |
| [![Search](docs/assets/app-desktop.png)](docs/assets/app-desktop.png) | [![Repertorisation chart](docs/assets/app-chart-desktop.png)](docs/assets/app-chart-desktop.png) |

</div>

---

## What it is

Boericke's *Repertory* is the index to a homeopathic practice: a symptom path, a rubric, and the
remedies that belong to it, graded. This is that book as **one 889 kB HTML file** — the
stylesheet, the script and the whole dataset inline. Open it in a browser and it runs; there is
no install, no build step, no server and no account.

It is built for the consulting room, which is why it is offline-first rather than
offline-tolerant: once the page has loaded it never opens a socket. No CDN, no web font, no
analytics, no telemetry, no badge service — **including on the landing page that advertises it.**

## What it does

**Search like a query.** Instant results across 6,110 rubrics with real operators —
`"exact phrase"`, `-exclude`, `a or b` — and typo tolerance that only kicks in when nothing at
all matched. Remedy aliases mean *Gelsemium* finds the source's own *Gels*. `/` focuses the box,
`↑` `↓` move, `Enter` adds to the chart.

**Browse the book.** A **Browse** toggle walks the repertory by chapter and sub-rubric, expanded
lazily, so you can navigate the way the book is laid out instead of guessing at words.

**Repertorise, then eliminate.** Every selected rubric scores its remedies — grade 2 counts two
points, grade 1 counts one, and you can change both weights (the scale is printed on the chart
and in the print sheet, so a chart stays auditable). Mark a rubric **must-have** and every remedy
that misses one is faded, or filtered out entirely. Filter the table by name; tap any remedy to
see every rubric that lists it.

**Keep the case.** Patient details, notes and prescription sit alongside the selection and the
chart, grouped by patient. Cases can be **locked with a passphrase** — AES-256-GCM, key derived
with PBKDF2-SHA256 (200,000 rounds) in the browser and never stored. Print a one-page A4 case
sheet, export the chart as CSV, export every case as JSON, or save straight to a file you choose.

**Work fast.** A command palette on `Ctrl`/`Cmd + K`, undo on `Ctrl`/`Cmd + Z`, saved searches,
per-rubric notes, and computed "similar rubrics" for a rubric you are unsure about.

**Refuses to phone home.** No account · no server · no network after load · no external assets ·
no telemetry · no silent updates.

## What's new in 1.2.0

Query operators and typo tolerance · browse-by-chapter · must-have rubrics · configurable grade
weights · chart filter · encrypted vault · patient grouping and case search · command palette ·
undo · saved searches · per-rubric notes · similar rubrics · one-page case sheet · CSV export ·
backup reminder · service worker and installable manifest · text-size and high-contrast settings ·
data audit · remedy alias table. See the [changelog](CHANGELOG.md) and the
[roadmap](docs/ROADMAP.md) for what is deliberately not done.

## Use it

| | |
| :-- | :-- |
| **Online** | [drsamonline.github.io/boericke-repertory/play/](https://drsamonline.github.io/boericke-repertory/play/) |
| **Offline** | download [`index.html`](index.html) and open it — that is the whole installation |
| **Windows / Android** | the portable `.exe` and the signed `.apk` on [Releases](https://github.com/drsamonline/boericke-repertory/releases/latest) |
| **Self-host** | fork the repo, enable GitHub Pages, deploy from the default branch |

## The data

| | |
| :-- | --: |
| Rubrics | **6,110** |
| Unique remedies | **1,461** |
| Chapters | **25** |
| Graded entries | **48,385** (15,737 at grade 2) |
| Remedies with no rubric | **0** |
| Runtime dependencies | **0** |

The dataset is cleaned, not copied: OCR variants of a remedy name are merged into one canonical
name, duplicate rubrics are merged, and remedy-less category headings are kept for structure but
never appear in search results — so every rubric shown carries at least one remedy. The **About →
Data audit** panel recomputes these numbers in the app, so the cleaning can be checked rather than
trusted.

## The repository

```
index.html                  the app, standalone — this is the download
docs/index.html             the landing page (its own design, not the app's)
docs/play/index.html        the app as deployed
docs/play/sw.js             service worker: network-first HTML, cache-first assets
docs/play/manifest.webmanifest
docs/assets/                screenshots, local SVG badges, generated icons
docs/ROADMAP.md             the offline-only enhancement list
scripts/badges.py           draws docs/assets/badge-*.svg — no image service
scripts/icons.py            rasterises the icon: PNG sizes, .ico, adaptive layers
scripts/social.py           draws the 1280x630 social card
scripts/shot.sh             headless-Chromium screenshots of both surfaces
scripts/check.sh            syntax check + self-test + vault test, one command
scripts/selftest.html       20 assertions driving the app through its own API
scripts/vault_test.mjs      6 assertions on the encryption round trip
```

```bash
bash scripts/check.sh         # syntax + 20 browser assertions + 6 crypto assertions
python3 scripts/badges.py     # regenerate the badges
python3 scripts/icons.py      # regenerate the icons, .ico and adaptive layers
bash scripts/shot.sh landing  # screenshot the landing page
bash scripts/shot.sh app app '?q=burning%20headache'
```

The build pipeline (`.github/workflows/build-apps.yml`) builds the `.exe` and the `.apk` from
`docs/play`, publishes the rolling release and deploys `docs/` to Pages — all from one commit, so
the live demo and the released build can never disagree.

## Credits

- **Content** — *Repertory* by **Oscar E. Boericke, M.D.** (1927), companion to the *Pocket
  Manual of Homoeopathic Materia Medica*, 9th ed., by **William Boericke, M.D.** Text digitised
  from the public-domain edition at homeoint.org (presented by Médi-T).
- **Design & application** — © 2026 **Dr. Sohil Momin**.

## Licence

**Free to use, with attribution.** Copy, modify and distribute, provided that attribution is
given in both the documentation and the user interface:

> Content: *Repertory by Oscar E. Boericke, M.D. (1927)*
> Design & application: *Dr. Sohil Momin*

See [LICENSE](LICENSE) for the full terms.

<div align="center">

**Disclaimer** — provided *as is*, for study and reference by qualified practitioners.
Not a substitute for professional homoeopathic or medical judgment.

</div>
