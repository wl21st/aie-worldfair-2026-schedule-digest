#!/usr/bin/env python3
"""Generate a newest-first catalog of videos in the World's Fair 2026 playlist."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from generate_youtube_channel_markdown import duration_text, load_entries, tags_for, thumbnail

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CHANNEL = ROOT / "raw" / "youtube-aiengineer-channel-flat.json"
DEFAULT_PLAYLIST = ROOT / "raw" / "youtube-aiewf-2026-playlist.json"
DEFAULT_OUTPUT = ROOT / "ai-engineer-worlds-fair-2026-youtube-videos.md"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLDyBmFH9HlVc"
CHANNEL_URL = "https://www.youtube.com/@aiDotEngineer/videos"


def playlist_ids(path: Path) -> set[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("entries") if isinstance(data, dict) else data
    if not isinstance(entries, list):
        raise ValueError(f"Expected playlist entries in {path}")
    return {str(entry["id"]) for entry in entries if isinstance(entry, dict) and entry.get("id")}


def generate(entries: list[dict], playlist_id_set: set[str]) -> str:
    selected = [entry for entry in entries if str(entry["id"]) in playlist_id_set]
    lines = [
        "---",
        "layout: default",
        'title: "AI Engineer World\'s Fair 2026 — YouTube Videos"',
        'description: "Newest-first list of videos in the official AI Engineer World\'s Fair 2026 playlist."',
        "---",
        "",
        "# AI Engineer World's Fair 2026 — YouTube Videos",
        "",
        f"Newest-first list of videos currently in the official [AI Engineer World's Fair 2026 playlist]({PLAYLIST_URL}). Order follows the official channel's [video feed]({CHANNEL_URL}) so newly uploaded recordings appear first.",
        "",
        f"Playlist snapshot entries: **{len(playlist_id_set)}**. Matched channel-feed entries: **{len(selected)}**. Tags are deterministic topic tags derived from each title; they are not claims about hidden YouTube tags.",
        "",
        "| # | Video | Thumbnail | Duration | Tags |",
        "| ---: | --- | --- | ---: | --- |",
    ]
    for index, entry in enumerate(selected, start=1):
        video_id = str(entry["id"])
        title = str(entry["title"]).replace("|", "\\|").replace("\n", " ")
        url = f"https://www.youtube.com/watch?v={video_id}"
        tags = "; ".join(tags_for(title)).replace("|", "\\|")
        lines.append(f"| {index} | [{title}]({url}) | {thumbnail(video_id)} | {duration_text(entry.get('duration'))} | {tags} |")
    missing = sorted(playlist_id_set - {str(entry["id"]) for entry in selected})
    lines.extend(["", "## Verification", ""])
    if missing:
        lines.append("The following playlist IDs were not present in the current channel feed snapshot: " + ", ".join(missing) + ".")
    else:
        lines.append("Every video ID in the playlist snapshot was found in the channel feed snapshot.")
    lines.extend([
        "",
        "## Sources",
        "",
        f"[1] {PLAYLIST_URL} — official AI Engineer World's Fair 2026 playlist.",
        f"[2] {CHANNEL_URL} — official AI Engineer channel video feed used for newest-first ordering.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", type=Path, default=DEFAULT_CHANNEL)
    parser.add_argument("--playlist", type=Path, default=DEFAULT_PLAYLIST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    text = generate(load_entries(args.channel), playlist_ids(args.playlist))
    args.output.write_text(text, encoding="utf-8")
    print(json.dumps({"output": str(args.output), "playlist_entries": text.count("| ["), "bytes": len(text.encode("utf-8"))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
