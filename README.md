<div align="center">

# Boericke's Repertory

<img src="docs/assets/badge-rubrics.svg" alt="rubrics: 6,110" height="22"> <img src="docs/assets/badge-remedies.svg" alt="remedies: 1,461" height="22"> <img src="docs/assets/badge-chapters.svg" alt="chapters: 25" height="22"> <img src="docs/assets/badge-offline.svg" alt="offline: no network" height="22"> <img src="docs/assets/badge-deps.svg" alt="dependencies: 0 runtime" height="22"> <img src="docs/assets/badge-file.svg" alt="single file: 821 kB" height="22"> <img src="docs/assets/badge-licence.svg" alt="licence: free use, attribution required" height="22">

### A classic clinical repertory, made searchable — one HTML file, offline, no account, no server

**Compiled and designed by Dr. Sohil Momin** · after *Oscar E. Boericke, M.D. (1927)*

[**Landing page**](https://drsamonline.github.io/boericke-repertory/) &nbsp;·&nbsp;
[**Live app**](https://drsamonline.github.io/boericke-repertory/play/) &nbsp;·&nbsp;
[**Releases**](https://github.com/drsamonline/boericke-repertory/releases/latest) &nbsp;·&nbsp;
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

Boericke's *Repertory* is the index to a homeopathic practice: a symptom path, a rubric, and
the remedies that belong to it, graded. This is that book as **one 821 kB HTML file** — the
stylesheet, the script and the whole dataset inline. Open it in a browser and it runs; there is
no install, no build step, no server and no account.

It is built for the consulting room, which is why it is offline-first rather than
offline-tolerant: once the page has loaded it never opens a socket. No CDN, no web font, no
analytics, no telemetry, no badge service — **including on the landing page that advertises it.**

## What it does

**Search** — instant results across 6,110 rubrics by symptom, by path or by remedy name, with
matched terms highlighted and a chapter filter. `/` focuses the box, `↑` `↓` move, `Enter` adds
to the chart.

**Repertorise** — tap rubrics to build a chart that scores every remedy across them (grade 2
counts two points, grade 1 counts one) and ranks by total, rubric count or name, with bars for
the top ten. Tap any remedy to see **every rubric that lists it**, with its grade.

**Cases** — patient details, notes and prescription sit alongside the selection and the chart.
Save, reload, print, or export and import the whole case as JSON. It stays on your device.

**Deep links** — the app reads a few query parameters, so a specific view can be linked or
bookmarked: `play/?q=burning+headache`, `?q=thirst+fever&pick=4&tab=chart`,
`?remedy=Gelsemium`, `?tab=cases`. This is what the landing page's guided demo drives.

## What it refuses to do

No account · no server · no network after load · no external assets · no telemetry ·
no silent updates. A clinical tool that needs a connection is a clinical tool that stops
working when you need it.

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
| Runtime dependencies | **0** |

The dataset is cleaned, not copied: OCR variants of a remedy name are merged into one canonical
name, duplicate rubrics are merged, and remedy-less category headings are kept for structure but
never appear in search results — so every rubric shown carries at least one remedy.

## The repository

```
index.html                 the app, standalone — this is the download
docs/index.html            the landing page (its own design, not the app's)
docs/play/index.html       the app as deployed
docs/assets/               screenshots, local SVG badges, generated icons
docs/ROADMAP.md            the offline-only enhancement list
scripts/badges.py          draws docs/assets/badge-*.svg — no image service
scripts/icons.py           rasterises docs/icon.svg into the PNG sizes
scripts/shot.sh            headless-Chromium screenshots of both surfaces
```

```bash
python3 scripts/badges.py     # regenerate the badges
python3 scripts/icons.py      # regenerate the icon PNGs
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
