# ActiveBox · Responsive front-end study

[![Live](https://img.shields.io/badge/live-GitHub%20Pages-0B5FFF)](https://rohaan2802.github.io/Web_Active_Box/)
[![Stack](https://img.shields.io/badge/stack-HTML%20%7C%20CSS%20%7C%20JS-111827)](#source-map)
[![Screenshots](https://img.shields.io/badge/screenshots-20%20labelled-1B7A4B)](#feature-screenshots-20)

A recreation of the original **ActiveBox** template by **Mohammad Rohaan**, refined into a responsive, accessible, interactive one-page portfolio demonstration — plain HTML/CSS/JS, no framework build step.

**Author:** Mohammad Rohaan · [rohaan2802](https://github.com/rohaan2802)

---

## Live demo

https://rohaan2802.github.io/WebActiveBox/

Repository:

https://github.com/rohaan2802/WebActiveBox

Design decisions:

https://github.com/rohaan2802/WebActiveBox/blob/master/CASE_STUDY.md

Verification notes:

https://github.com/rohaan2802/WebActiveBox/blob/master/RESPONSIVE_QA.md

---

## Table of contents

1. [Live demo](#live-demo)
2. [Quick review](#quick-review)
3. [Feature screenshots (20)](#feature-screenshots-20)
4. [Deep feature walkthrough](#deep-feature-walkthrough)
5. [What this project demonstrates](#what-this-project-demonstrates)
6. [Run locally](#run-locally)
7. [Source map](#source-map)
8. [Verification](#verification)
9. [Project structure](#project-structure)
10. [Attribution and scope](#attribution-and-scope)
11. [Author](#author)

---

## Quick review

1. Resize the page — grids and navigation adapt.
2. Toggle dark / light theme, reload, confirm the preference persists.
3. Filter the work gallery and open an image — try arrows, Tab, Escape.
4. Read **The build** (`#project-notes`) for scope and decisions.
5. Enable OS reduced motion — reveals and hover movement stop.

---

## Feature screenshots (20)

Previous `docs/preview.webp` gallery art was removed. These labelled captures replace it.

### 1. Hero — dark desktop

Full-bleed hero with brand, CTA pair, and dark theme as the default presentation.

![Hero dark desktop](docs/screenshots/01-hero-dark-desktop.jpg)

### 2. Hero — light desktop

Same composition after the theme switch — palette, contrast, and controls update together.

![Hero light desktop](docs/screenshots/02-hero-light-desktop.jpg)

### 3. Features section

Four capability cards (customize, responsive, modern, clean foundations) under a clear section heading.

![Features section](docs/screenshots/03-features-section.jpg)

### 4. Work gallery — all projects

Eight portfolio studies with filters enabled and “showing all” status text.

![Work gallery all](docs/screenshots/04-work-gallery-all.jpg)

### 5. Work filter — Objects

Category filter hides non-matching cards and updates the live status count.

![Work filter Objects](docs/screenshots/05-work-filter-objects.jpg)

### 6. Work filter — Photography

Second filter path for photography studies — same progressive-enhancement pattern.

![Work filter Photography](docs/screenshots/06-work-filter-photography.jpg)

### 7. Image viewer lightbox

Accessible dialog viewer with title, position (`n / total`), prev/next, and Escape to close.

![Image viewer lightbox](docs/screenshots/07-image-viewer-lightbox.jpg)

### 8. Team section

Illustrative team grid with portraits and roles from the template content.

![Team section](docs/screenshots/08-team-section.jpg)

### 9. Testimonials section

Static sample quote presentation (not a live CMS feed).

![Testimonials](docs/screenshots/09-testimonials-section.jpg)

### 10. Download / GitHub CTA

Tight crop of the download band — source zip + GitHub link, no neighboring sections bleeding in.

![Download CTA](docs/screenshots/10-download-cta.jpg)

### 11. The build — project notes

Full “Behind the build” block: project facts, Foundation / Interaction / Resilience cards, and source CTAs.

![Project notes](docs/screenshots/11-project-notes-build.jpg)

### 12. Work filter — Print

Third gallery path (Print) with the filtered set and live status — complements Objects / Photography shots above.

![Work filter Print](docs/screenshots/12-work-filter-print.jpg)

### 13. Reading progress (mid-scroll)

Top progress bar reflecting scroll depth through the long one-pager.

![Reading progress](docs/screenshots/13-reading-progress-midscroll.jpg)

### 14. Back-to-top control

Deferred control that appears after scrolling, returning focus to the top of the page.

![Back to top](docs/screenshots/14-back-to-top-control.jpg)

### 15. Header — nav + theme controls

Brand, section links, and theme toggle in the sticky/site header region.

![Header controls](docs/screenshots/15-header-nav-theme-controls.jpg)

### 16. Mobile hero

Compact viewport hero — type and actions remain usable without horizontal overflow.

![Mobile hero](docs/screenshots/16-mobile-hero.jpg)

### 17. Mobile navigation open

Hamburger / menu toggle expands the primary nav for small screens.

![Mobile nav](docs/screenshots/17-mobile-nav-open.jpg)

### 18. Mobile work gallery

Stacked work cards and filters on a phone-width canvas.

![Mobile work](docs/screenshots/18-mobile-work-gallery.jpg)

### 19. Tablet features layout

Mid-width arrangement of the features grid between phone and desktop.

![Tablet features](docs/screenshots/19-tablet-features-layout.jpg)

### 20. Skip link — keyboard focus

First Tab reveals “Skip to content” for keyboard and assistive-tech users.

![Skip link](docs/screenshots/20-skip-link-keyboard-focus.jpg)

---

## Deep feature walkthrough

### Theme system (`theme-init.js` + `enhancements.js`)

`theme-init.js` runs in `<head>` so the saved theme applies **before** CSS paints (reduces flash). Preference key: `WebActiveBox-theme`. If `localStorage` is blocked, the switch still works for the session. The toggle updates `data-theme`, button label/icon, and `theme-color` meta.

### Responsive composition (`style.css` + `presentation.css`)

Fluid headings, ~18px reading baseline, generous line-height, and bounded measure. Navigation collapses before links crowd. Features / work / team grids reflow across phone → tablet → desktop (screenshots 16–19).

### Work gallery filters

Buttons with `data-filter` set `aria-pressed` and hide non-matching `.work-card`s. Status text is a live region (`aria-live="polite"`). Without JS, all images remain normal links.

### Accessible image viewer

Uses a `<dialog>` when available. Supports Escape, arrow keys, focus trap on Tab, and position text. Modifier-click still opens the raw image URL (progressive enhancement).

### Navigation & section awareness (`script.js` + `presentation.js`)

Smooth in-page nav, menu toggle for small screens, and current-section indication while scrolling. Reading progress and reveal motion are cancellable under `prefers-reduced-motion`.

### Project notes + native FAQ

“The build” section explains Foundation / Interaction / Resilience. FAQ uses native `<details>` so it works without JS and without a dependency.

### Progressive enhancement & resilience

- Skip link for keyboard users  
- Content readable if JS fails  
- Reduced-motion respected  
- Theme fallback without storage  
- Local assets only — no CDN runtime required for core UI  

### Verification harness (`tests/responsive_check.py`)

Automated Playwright checks across many widths in both themes, keyboard gallery behavior, theme persistence, FAQ, reduced motion, and no-JS navigation. See [RESPONSIVE_QA.md](RESPONSIVE_QA.md).

---

## What this project demonstrates

- **Responsive composition** — fluid type and grids; nav collapses cleanly  
- **Interaction design** — theme, filters, viewer, back-to-top, progress, section tracking, FAQ  
- **Considered motion** — short reveals; no mandatory animation loop  
- **Progressive enhancement** — usable without JS; storage-safe theme  
- **Maintainable delivery** — static files, local assets, regression script  

---

## Run locally

```sh
python -m http.server 5500
```

Open http://localhost:5500

Regenerate README screenshots (optional):

```sh
python scripts/capture_feature_shots.py
```

---

## Source map

| File | Responsibility |
|------|----------------|
| `index.html` | Semantic page, content, FAQ, viewer markup |
| `assets/css/style.css` | Base layout + light palette |
| `assets/css/enhancements.css` | Dark palette, theme, gallery, viewer |
| `assets/css/presentation.css` | Larger type, project section, effects |
| `theme-init.js` | Early theme apply |
| `script.js` | Navigation / menu |
| `enhancements.js` | Theme, filters, viewer, back-to-top |
| `presentation.js` | Motion, progress, section tracking |
| `tests/responsive_check.py` | Browser regression checks |
| `scripts/capture_feature_shots.py` | README screenshot generator |

---

## Verification

```sh
python -m pip install playwright
python tests/responsive_check.py
```

Default browser channel: Chrome. Set `BROWSER_CHANNEL=msedge` for Edge. Artifacts land in ignored `tests/artifacts/`.

---

## Project structure

```text
WebActiveBox/
├── index.html · *.js
├── assets/css · fonts · images · Design
├── docs/screenshots/     # 20 labelled JPGs
├── scripts/capture_feature_shots.py
├── tests/responsive_check.py
├── CASE_STUDY.md · RESPONSIVE_QA.md
├── LICENSE · README.md · TREE.txt
```

---

## Attribution and scope

Independent front-end study of an existing template — **not** a commercial product claim or client delivery. Original imagery/fonts keep their attribution; review licenses before commercial reuse. Team / portfolio / testimonial copy is illustrative. No analytics, checkout, or Lighthouse score is claimed. Tests do not certify every physical device or AT.

---

## Author

**Mohammad Rohaan** · https://github.com/rohaan2802  
Live site: https://rohaan2802.github.io/WebActiveBox/  
Repository: https://github.com/rohaan2802/WebActiveBox
