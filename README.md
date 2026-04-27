# Relvio Certifications Hub

Personal IBM Maximo certification prep courses, served as a single static HTML file at https://certif.relvio.app

## Courses hosted

| Code | Title | Sections | Lessons | Status |
|---|---|---|---|---|
| C1000-183 | Maximo Manage v9.0 Functional Deployment — Professional | 9 | 44 | Live |
| C1000-208 | Maximo Manage v9.1 Inventory Management — Associate | 7 | 20 | Live |
| Soon | Course #3 | — | — | Coming |

Switch courses via the cert tabs at the top of the sidebar. Each course has its own progress tracking (independent localStorage namespace) and deep-link format:

- `https://certif.relvio.app/#c1000-183/lesson-3-7` — explicit cert + lesson
- `https://certif.relvio.app/#c1000-208/lesson-2-1` — C1000-208 lesson
- `https://certif.relvio.app/#lesson-3-7` — backward-compat (resolves to C1000-183)

## Hosting

Static single-file HTML, served via GitHub Pages from the `main` branch with the `CNAME` file pointing the apex to `certif.relvio.app`.

Update the page by editing `index.html` and pushing — Pages rebuilds in under a minute.

## Why a separate repo

This guide is unrelated to the Relvio platform. Keeping it in its own repo avoids the deployment churn that previously caused the page to go down whenever a Relvio CI deploy overwrote a manual Traefik route on the shared VPS.

## Course mechanics

Each lesson has two tabs:

- **📚 Lesson** — IBM Objectives (verbatim from the official Study Guide), Key Points, IBM Trap, Flashcard
- **🎯 Exam scenarios** — interactive IBM-style multiple-choice questions with dense pedagogical rationales (300-600 words each — works as a mini-lesson, not a 2-line answer-key)

Progress (lessons studied, MCQ answers) is saved in the browser's `localStorage` per course. Resetting a section purges that section's MCQ state. The cert switcher persists the last-opened course across sessions.
