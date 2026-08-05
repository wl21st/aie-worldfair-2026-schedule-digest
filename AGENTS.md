---
layout: default
title: "AGENTS.md — Repository Guidance & Agent Docs"
---

# AGENTS.md

## What this repo is

This is a **documentation/research repo**, not application code. It holds two large
generated Markdown "digest" documents about the **AI Engineer World's Fair 2026**
conference (June 29 – July 2, 2026, San Francisco):

- `ai-engineer-worlds-fair-2026-master.md` — top-30 sessions ranked per **12 AI
  categories** (`## 1.` … `## 12.`). Ranked for enterprise AI architects; exact
  duplicate schedule records are consolidated, distinct Part/Pt/continued sessions
  stay separate. Source rows: `sessions.json` + official YouTube channel.
- `ai-engineer-worlds-fair-2026-speakers.md` — all **552 speaker records** transcribed
  from `speakers.json`, plus a "recent social sharing" table (official X/LinkedIn and
  selected speaker posts).

There is **no build, test, lint, or typecheck tooling**. Do not look for one.

## Living upstream data sources

The repo is a snapshot of web sources; the raw JSON is **not** stored here. Data and
links go stale after each source update, so regenerating/refreshing means doing web
research again:

- `https://www.ai.engineer/worldsfair/2026/sessions.json`
- `https://www.ai.engineer/worldsfair/2026/speakers.json`
- Speaker photo URLs follow the pattern `https://www.ai.engineer/wf26/speakers/by-id/spk_<slug>.jpg`

## Citation convention (critical)

Both files use inline `[n]` markers appended to **nearly every field/value**, mapped in a
trailing `## Sources` section to the URL. Examples: `Company:** Reducto [1]` or
`[Watch](https://www.youtube.com/watch?v=...)`.

- Keep every inline `[n]` matching the corresponding numbered entry in `## Sources`.
- When adding a new citation, append a new numbered source at the end of `## Sources`
  and reuse its number throughout the body — do not renumber existing ones.

## Editing rules for these markdown files

- They are large (master ≈ 430 lines; speakers ≈ 5800 lines) and heavily templated
  (`### N. <Name> [1]` headings, `- **Role:** …` bullets). Match the existing
  formatting exactly when adding rows.
- Missing/unknown values are rendered as `—`, never left blank or dropped.
- Preserve original JSON field casing/values where present.
- When updating the speakers roster, keep the header stat (`Speakers in source: 552`)
  consistent with the record count.
- Schedule times use the format `Day 4 — Session Day 3 — 11:40am-12:00pm`; room names
  are transposed from source (watch for typos like "Westley" vs "Wesley" — fix in the
  source data, not the render).

## Skills

- `.agents/skills/schedule-design/SKILL.md` documents building a **separate** React
  schedule page (a different project). Reference it only for front-end schedule/modal/
  filter work — it is not relevant to editing these Markdown digests.

## Git

`main` has no commits yet. Only commit/push when explicitly asked.