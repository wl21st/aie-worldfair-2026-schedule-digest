---
layout: default
title: "YouTube Refresh Range Detection"
description: "Watermark-based workflow for detecting new AI Engineer YouTube uploads."
---

# YouTube Refresh Range Detection

The channel refresh workflow uses `raw/youtube-aiengineer-channel-watermark.json` as a durable watermark. It records every video ID present in the last applied channel snapshot. Since the official channel feed is newest-first, the detector identifies the new-upload range before the first previously known ID.

## Detect the next update

Fetch a fresh channel snapshot to a temporary path, then compare it with the committed watermark:

```bash
yt-dlp --cookies-from-browser chrome \
  --flat-playlist --dump-single-json --no-warnings --skip-download \
  "https://www.youtube.com/@aiDotEngineer/videos" \
  > /tmp/aie-youtube-channel-candidate.json

python3 scripts/detect_youtube_update_range.py \
  --candidate /tmp/aie-youtube-channel-candidate.json
```

The detector reports:

- `complete-prefix` when every unseen ID is a contiguous newest-first prefix;
- `no-change` when the candidate contains no new IDs;
- `interleaved-new-ids` when new IDs appear after an existing ID and need review;
- `watermark-not-found` when the candidate does not contain any previously known ID, usually indicating an incomplete or unrelated feed.

Use `--json` for automation:

```bash
python3 scripts/detect_youtube_update_range.py \
  --candidate /tmp/aie-youtube-channel-candidate.json \
  --json
```

## Advance the watermark

Only advance the watermark after reviewing the reported range and applying the candidate snapshot to the repository:

```bash
cp /tmp/aie-youtube-channel-candidate.json raw/youtube-aiengineer-channel-flat.json
python3 scripts/generate_youtube_channel_markdown.py
python3 scripts/generate_sessions_markdown.py
python3 scripts/generate_worldfair_youtube_markdown.py
python3 scripts/detect_youtube_update_range.py \
  --candidate /tmp/aie-youtube-channel-candidate.json \
  --write-watermark
```

The detector refuses to advance the watermark when the prior boundary is absent or known IDs are missing from the candidate. Do not use `--force` unless the feed has been checked for truncation, deliberate removals, or a deliberate baseline reset. Initialize a new baseline explicitly with:

```bash
python3 scripts/detect_youtube_update_range.py \
  --candidate raw/youtube-aiengineer-channel-flat.json \
  --initialize
```
