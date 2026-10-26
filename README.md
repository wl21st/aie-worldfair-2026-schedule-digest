# AI Engineer World's Fair 2026 Digest

[View the GitHub Pages site](https://wl21st.github.io/aie-worldfair-2026-schedule-digest/)

Research and reference materials for **AI Engineer World's Fair 2026**, held June 29–July 2, 2026, in San Francisco. The repository brings together curated schedule digests, the complete session catalog, speaker information, official video catalogs, keynote summaries, and a technical investigation of the accompanying speaker embeddings.

## Contents

- [Top 30 Master Digest](ai-engineer-worlds-fair-2026-master.md): ranked sessions organized across 12 AI categories for enterprise AI architects and engineers.
- [All Sessions](ai-engineer-worlds-fair-2026-sessions.md): the complete conference schedule with generated keywords and official recording links where a confident match was found.
- [Speaker Directory](ai-engineer-worlds-fair-2026-speakers.md): speaker profiles, affiliations, talk descriptions, and selected public event-sharing activity.
- [Keynote Summaries](keynotes.md): daily keynote summaries and cross-cutting conference analysis.
- [World's Fair YouTube Catalog](ai-engineer-worlds-fair-2026-youtube-videos.md): videos identified in the official World's Fair 2026 playlist.
- [AI Engineer YouTube Channel Catalog](ai-engineer-youtube-channel-videos.md): a broader catalog of videos from the official AI Engineer channel.
- [World's Fair 2026 Latest Uploads](ai-engineer-youtube-new-uploads.html): the official World's Fair playlist videos sorted by newest-first channel upload order, with search, topic filtering, and sorting.
- [Embedding Investigation Report](digest/embedding-investigation-report.md): analysis of vector preprocessing, duplicate detection, cosine similarity, and cluster verification.

## Data Sources

The published digests are based on the official conference schedule and speaker data, supplemented by the official AI Engineer YouTube channel and World's Fair playlist:

- [Official sessions data](https://www.ai.engineer/worldsfair/2026/sessions.json)
- [Official speakers data](https://www.ai.engineer/worldsfair/2026/speakers.json)
- [AI Engineer YouTube channel](https://www.youtube.com/@aiDotEngineer)
- [AI Engineer World's Fair](https://www.ai.engineer/worldsfair/2026)

The `raw/` directory contains source snapshots and intermediate research data used to generate or validate the Markdown catalogs. Source data and video availability can change over time, so the repository should be treated as a dated research snapshot rather than a permanently authoritative archive.

## Repository Layout

```text
.
├── ai-engineer-worlds-fair-2026-master.md
├── ai-engineer-worlds-fair-2026-sessions.md
├── ai-engineer-worlds-fair-2026-speakers.md
├── ai-engineer-worlds-fair-2026-youtube-videos.md
├── ai-engineer-youtube-channel-videos.md
├── keynotes*.md
├── digest/
├── raw/
├── scripts/
└── index.md
```

The site is published with GitHub Pages and uses the Jekyll Primer theme. Markdown documents can be read directly in the repository or through the linked HTML pages on the published site.

## Refreshing The Data

The generated documents are refreshed from live web sources using the scripts in `scripts/`. Refreshes may require web research because the upstream JSON snapshots are not guaranteed to remain unchanged. When updating the Markdown digests, preserve the existing inline citation markers and their corresponding entries in each document's `Sources` section.

This is a documentation and research repository. It does not contain an application build, test, lint, or typecheck workflow.
