#!/usr/bin/env python3
"""Generate a newest-first catalog of the official AI Engineer YouTube channel."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "raw" / "youtube-aiengineer-channel-flat.json"
DEFAULT_OUTPUT = ROOT / "ai-engineer-youtube-channel-videos.md"
CHANNEL_URL = "https://www.youtube.com/@aiDotEngineer/videos"

STOPWORDS = {
    "about", "after", "again", "agent", "agents", "all", "and", "are", "at", "back",
    "be", "been", "being", "behind", "build", "building", "can", "code", "coding",
    "come", "context", "does", "for", "from", "get", "how", "in", "into", "is", "it",
    "its", "learned", "more", "new", "not", "of", "on", "or", "our", "production",
    "really", "scale", "scaling", "session", "software", "some", "that", "the", "their",
    "them", "there", "these", "this", "through", "to", "use", "using", "what", "when",
    "where", "which", "while", "with", "without", "world", "your",
}

PHRASE_TAGS = [
    ("computer use", "computer use"),
    ("model routing", "model routing"),
    ("local model", "local AI"),
    ("local llm", "local AI"),
    ("inference", "inference"),
    ("kubernetes", "Kubernetes"),
    ("sandbox", "sandboxes"),
    ("harness", "harness engineering"),
    ("eval", "evals"),
    ("benchmark", "benchmarks"),
    ("retrieval", "RAG/search"),
    ("rag", "RAG/search"),
    ("context", "context engineering"),
    ("memory", "memory"),
    ("training", "model training"),
    ("reinforcement", "reinforcement learning"),
    ("multimodal", "multimodal"),
    ("vision", "vision"),
    ("voice", "voice"),
    ("security", "security"),
    ("auth", "authentication"),
    ("commerce", "agentic commerce"),
    ("finance", "AI in finance"),
    ("health", "AI in healthcare"),
    ("healthcare", "AI in healthcare"),
    ("graph", "knowledge graphs"),
    ("mcp", "MCP"),
    ("skills", "agent skills"),
    ("coding", "coding agents"),
    ("developer", "developer productivity"),
    ("software factory", "software factories"),
    ("autoresearch", "autoresearch"),
    ("robot", "robotics"),
    ("edge", "edge AI"),
]


def load_entries(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("entries") if isinstance(data, dict) else data
    if not isinstance(entries, list):
        raise ValueError(f"Expected an entries list in {path}")
    result = []
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("id") or not entry.get("title"):
            continue
        result.append(entry)
    return result


def duration_text(seconds: object) -> str:
    try:
        total = int(str(seconds or 0))
    except (TypeError, ValueError):
        return "—"
    if total <= 0:
        return "—"
    minutes, seconds = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours}h {minutes:02d}m {seconds:02d}s"
    return f"{minutes}m {seconds:02d}s"


def tags_for(title: str) -> list[str]:
    folded = re.sub(r"[^a-z0-9+#]+", " ", title.lower())
    tags: list[str] = []
    for phrase, tag in PHRASE_TAGS:
        if phrase in folded and tag not in tags:
            tags.append(tag)
    words = re.findall(r"[A-Za-z][A-Za-z0-9+#-]{2,}", title)
    for word in words:
        value = word.lower()
        if value in STOPWORDS or value.isdigit():
            continue
        acronym = {"ai": "AI", "llm": "LLM", "llms": "LLMs", "mcp": "MCP", "gpu": "GPU", "gpus": "GPUs"}.get(value)
        shown = acronym or word
        if shown.lower() not in {tag.lower() for tag in tags}:
            tags.append(shown)
        if len(tags) >= 5:
            break
    return tags[:5] or ["AI engineering"]


def thumbnail(video_id: str) -> str:
    image = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
    url = f"https://www.youtube.com/watch?v={video_id}"
    return f'<a href="{url}" aria-label="Watch on YouTube"><img class="youtube-thumbnail" src="{image}" alt="YouTube thumbnail" loading="lazy"></a>'


def generate(entries: list[dict]) -> str:
    lines = [
        "---",
        "layout: default",
        'title: "AI Engineer YouTube Channel — Newest Videos"',
        "description: \"Newest-first catalog of videos published on the official AI Engineer YouTube channel.\"",
        "---",
        "",
        "# AI Engineer YouTube Channel — Newest Videos",
        "",
        f"Newest-first catalog of the official [AI Engineer YouTube channel]({CHANNEL_URL}). The channel's `/videos` feed order is preserved so newly uploaded videos appear at the top.",
        "",
        f"Catalog entries: **{len(entries)}**. Duration comes from the channel metadata. Tags are deterministic topic tags derived from each video title; they are not claims about hidden YouTube tags.",
        "",
        "| # | Video | Thumbnail | Duration | Tags |",
        "| ---: | --- | --- | ---: | --- |",
    ]
    for index, entry in enumerate(entries, start=1):
        video_id = str(entry["id"])
        title = str(entry["title"]).replace("|", "\\|").replace("\n", " ")
        url = f"https://www.youtube.com/watch?v={video_id}"
        tags = "; ".join(tags_for(title)).replace("|", "\\|")
        lines.append(f"| {index} | [{title}]({url}) | {thumbnail(video_id)} | {duration_text(entry.get('duration'))} | {tags} |")
    lines.extend([
        "",
        "## Sources",
        "",
        f"[1] {CHANNEL_URL} — official AI Engineer channel video feed.",
        "[2] https://www.youtube.com/ — video metadata retrieved with yt-dlp; the raw flat-channel snapshot is preserved in `raw/youtube-aiengineer-channel-flat.json`.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    text = generate(load_entries(args.input))
    args.output.write_text(text, encoding="utf-8")
    print(json.dumps({"output": str(args.output), "videos": text.count("| [")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
