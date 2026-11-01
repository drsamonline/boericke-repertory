# Changelog

## 1.6.0 — 2026-11-01

**The interface is English only.** The Hindi and Gujarati dictionaries, the language row in
Settings, the `?lang=` deep link and the translation walker are gone — about 5 kB of code and 180
translated strings removed. The decision: the app is for a practitioner reading Boericke, and one
language done properly beats a half-translated clinical interface. The repertory text was never
translated and still is not.

**Elimination by repertory section.** The must-have rubrics now have a rule: *every rubric*, or
*one per chapter*. Under the second, a remedy has to appear in at least one must rubric from each
chapter that has one — which is how a case is actually reasoned when a symptom is required in the
mental picture **and** in the generals. The choice is remembered between sessions.

**Visit history per patient.** Each patient heading now shows its visit count and the date range
covered, with a **New visit** button that pre-fills the patient, clears the clinical fields and
leaves the earlier visit untouched.

**A release strip on the landing page.** Six versions with dates and one line each, linking to the
tags — the page is now a changelog you can read at a glance, not just a brochure.

**Also** — the self-test is 28 assertions (the four language assertions retired with the feature),
and the audit still passes 28 checks.


## 1.5.1 — 2026-11-01

**A final audit, and it is now a script.** `scripts/audit.py` checks every claim the repository
makes against the repository itself, reading the built files rather than the intent:

- the app loads nothing from the network — no `src`/`href` to a remote host, no `fetch`, no
  `XMLHttpRequest`, no `@import`, no external font; the landing page likewise;
- the version agrees in five places — `VERSION`, the app's build stamp, the service-worker `CACHE`,
  the landing page footer, and the top entry of this changelog;
- the counts in the README are the counts in the data (6,110 / 1,461 / 25), and the source-check
  totals in README and `SOURCES.md` are the ones the app actually ships (5,415 / 5,319);
- the assertion count quoted in the docs is the number of assertions in `selftest.html`;
- every local `src`/`href` in both surfaces resolves to a file that exists, and every file listed
  in the README tree exists;
- the Hindi and Gujarati dictionaries have the same number of keys;
- no element id is duplicated in the rendered page (checked against the DOM, with the inline
  scripts stripped — counting ids in the source counts the same id twice whenever it appears in two
  branches of a ternary, which is not a defect).

28 checks, all passing. It caught three things, all now fixed.

**The second repertory is off the roadmap.** This app is one book. A second dataset would roughly
double a file whose entire value is being one file, so the plan is gone from `ROADMAP.md` and the
scope is stated plainly in `SOURCES.md`.

**Dead code removed** — an unused helper left over from the source-check work.


## 1.5.0 — 2026-11-01

**Every rubric is now checked against the source.** A complete transcription of the same
public-domain 1927 text was obtained (see `SOURCES.md`), every rubric was aligned to its line, and
the remedies and grades were compared one by one:

- **5,415** rubrics carry remedies; **5,408** align to a line in the source (99.9%).
- **5,319** are identical — same remedies, same grades (98.2%).
- **96** differ, and **every one is listed in the app** with the source's own line and exactly what
  disagrees: a remedy in the book missing here, a remedy here not in the book, or a grade that
  disagrees. They are also marked ⚠ on the result row.

The citation sheet now carries the verdict for the rubric you are looking at, and **About → Source
check** shows the totals with a list of every difference. The whole check costs 22 kB, because
source lines are carried only where they disagree.

This replaces the "not shippable" note from 1.4.0: the earlier attempt failed because every
homeoint chapter page truncates at a fixed response budget, which `SOURCES.md` still records — the
verification text came from a complete transcription published on GitHub instead.

**Also** — five new assertions (32 browser assertions now), and the seven new interface strings are
translated into Hindi and Gujarati.


## 1.4.0 — 2026-11-01

**A citation for any rubric.** Press the new `❝` button on a result row and the app produces a
citable reference: the full path, the chapter, the edition, and the remedies split into grade 2
and grade 1, ready to copy into a case note. It is generated from the same data the chart uses, so
it cannot drift from it. Copy works offline (Clipboard API with a `execCommand` fallback).

**The author's own prefatory note, quoted in full.** About now carries Oscar Boericke's 1927
prefatory note — the five rules that explain why a rubric path looks the way it does (Hahnemannian
section order, alphabetical within a section, the Cause / Type / Location / Character /
Concomitants / Modalities captions, bracketed disease names, and what the italics mean). Quoted,
not paraphrased, and attributed.

**`SOURCES.md`** records what is in the app, where it came from, and — with the evidence — what
could not be obtained. The line-level source quotation in the roadmap is not shipped, and the
reason is written down rather than left as a silent gap: every chapter page of the digitisation
returns truncated at a fixed response budget, and a quotation attached to some rubrics but not
others would read as though the source were silent where it is not.

**Also** — three new assertions (27 browser assertions now), the data-audit grid no longer leaves
an empty bordered cell on a short last row, and the five new interface strings are translated into
Hindi and Gujarati.


## 1.3.0 — 2026-11-01

**The interface in Hindi and Gujarati.** The chrome — tabs, buttons, labels, placeholders, empty
states, toasts, chart headings, the print sheet and the settings panel — is now in English, Hindi
and Gujarati, chosen in Settings and remembered under `br_lang`. The repertory text itself stays in
Boericke's English: translating the rubrics would be inventing a source. Strings are keyed by their
English form, so a missing key falls back to English rather than to a blank, and the four new
assertions in `scripts/check.sh` prove the switch works in both directions without touching the
rubric text.

**The release pipeline now carries the real mark.** `docs/play/icon.png` is the file
`app-builder`'s `make_icons.py` looks for first, so the portable `.exe` and the `.apk` pick up the
book icon instead of the deterministic monogram fallback. Nothing in the kit changed; the app repo
was simply missing the file it reads.

**Also** — `?lang=hi` / `?lang=gu` deep links, so a language can be linked or bookmarked.


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
