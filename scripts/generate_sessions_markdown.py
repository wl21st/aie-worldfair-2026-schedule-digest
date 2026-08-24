#!/usr/bin/env python3
"""Generate the all-sessions Markdown table from the schedule JSON snapshot.

The raw schedule stays immutable. YouTube metadata is read from a cached
official playlist export, or fetched with yt-dlp when --fetch-youtube is used.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "raw" / "sessions.json"
DEFAULT_YOUTUBE_JSON = ROOT / "raw" / "youtube-aiewf-2026-playlist.json"
DEFAULT_CHANNEL_JSON = ROOT / "raw" / "youtube-aiengineer-channel-flat.json"
DEFAULT_OUTPUT = ROOT / "ai-engineer-worlds-fair-2026-sessions.md"
DEFAULT_EXISTING_MARKDOWN = ROOT / "ai-engineer-worlds-fair-2026-master.md"
YOUTUBE_PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLDyBmFH9HlVc"
YOUTUBE_CHANNEL_URL = "https://www.youtube.com/@aiDotEngineer"
SESSIONS_SOURCE_URL = "https://www.ai.engineer/worldsfair/2026/sessions.json"

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9+#./-]*")
VIDEO_SUFFIX_RE = re.compile(r"\s+(?:[—–|-])\s+.*$")
PART_RE = re.compile(r"\bpart\s+\d+(?:\s+of\s+\d+)?\b", re.IGNORECASE)

# Generic words that make poor per-session keywords. Track names and the
# original title remain separate columns, so removing these improves signal.
STOPWORDS = {
    "about", "after", "again", "all", "also", "and", "any", "are", "around",
    "back", "been", "being", "best", "between", "beyond", "both", "build",
    "building", "can", "come", "comes", "could", "data", "does", "each", "end",
    "every", "from", "get", "getting", "give", "given", "going", "good", "have",
    "help", "how", "into", "just", "know", "like", "make", "making", "many",
    "more", "most", "much", "need", "needs", "new", "not", "now", "off", "one",
    "only", "our", "out", "over", "part", "people", "real", "really", "same",
    "scale", "scaling", "session", "should", "some", "such", "than", "that", "the",
    "their", "them", "then", "there", "these", "they", "this", "through", "to",
    "too", "under", "use", "used", "using", "very", "was", "were", "what", "when",
    "where", "which", "while", "who", "why", "will", "with", "without", "would",
    "your", "you", "agent", "agents", "artificial", "intelligence", "ai", "system",
    "systems", "software", "engineering", "engineer", "developers", "developer", "team",
    "teams", "company", "companies", "production", "work", "working", "world", "fair",
    "actually", "already", "anything", "around", "better", "different", "driven", "else",
    "evaluation", "evaluated", "evaluating", "explanation", "explanations", "first",
    "found", "going", "good", "know", "last", "often", "possible", "really", "running",
    "something", "started", "still", "thing", "things", "view", "way", "ways", "whether",
}

DISPLAY_ACRONYMS = {
    "api": "API", "apis": "APIs", "ai": "AI", "cua": "CUA", "gpu": "GPU",
    "gpus": "GPUs", "kg": "KG", "llm": "LLM", "llms": "LLMs", "mcp": "MCP",
    "mcps": "MCPs", "rag": "RAG", "rl": "RL", "sdlc": "SDLC", "sql": "SQL",
    "text2sql": "Text2SQL", "ux": "UX", "vllm": "vLLM", "vm": "VM", "vms": "VMs",
}


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as fh:
        temporary = Path(fh.name)
        fh.write(text)
        fh.flush()
    temporary.replace(path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def fold(text: str | None) -> str:
    value = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode("ascii")
    value = value.replace("&", " and ").replace("’", "'")
    value = re.sub(r"\[[^\]]*\]", " ", value)
    value = re.sub(r"[^a-zA-Z0-9]+", " ", value).lower()
    return re.sub(r"\s+", " ", value).strip()


def title_core(title: str | None) -> str:
    """Remove the speaker/channel suffix from a YouTube title."""
    value = (title or "").strip()
    value = VIDEO_SUFFIX_RE.sub("", value)
    value = re.sub(r"^\s*\[[^\]]+\]\s*", "", value)
    value = re.sub(r"^\s*(?:full\s+)?workshop\s*:\s*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^\s*keynote\s*:\s*", "", value, flags=re.IGNORECASE)
    return value.strip()


def title_key(title: str | None) -> str:
    value = title_core(title)
    value = PART_RE.sub(" ", value)
    value = re.sub(r"\b(?:full\s+)?workshop\b", " ", value, flags=re.IGNORECASE)
    value = re.sub(r"\bkeynote\b", " ", value, flags=re.IGNORECASE)
    return fold(value)


def token_values(text: str | None, *, remove_stopwords: bool = True) -> list[str]:
    values: list[str] = []
    for raw in TOKEN_RE.findall(text or ""):
        token = fold(raw)
        if len(token) < 3 or token.isdigit():
            continue
        if remove_stopwords and token in STOPWORDS:
            continue
        values.append(token)
    return values


def token_set(text: str | None) -> set[str]:
    return set(token_values(text))


def speaker_last_names(speakers: Iterable[str] | None) -> set[str]:
    result: set[str] = set()
    for speaker in speakers or []:
        words = token_values(speaker, remove_stopwords=False)
        if words:
            result.add(words[-1])
    return result


def escape_cell(value: Any) -> str:
    if value is None or value == "" or value == []:
        return "—"
    text = str(value).replace("\r", " ").replace("\n", " ")
    return text.replace("|", "\\|") or "—"


def youtube_thumbnail(url: str) -> str:
    """Render a compact clickable YouTube thumbnail for a watch URL."""
    match = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", url)
    if not match:
        raise ValueError(f"Expected a YouTube watch URL with an 11-character video ID: {url}")
    video_id = match.group(1)
    thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
    return (
        f'<a href="{url}" aria-label="Watch on YouTube">'
        f'<img class="youtube-thumbnail" src="{thumbnail_url}" '
        f'alt="YouTube thumbnail" loading="lazy">'
        "</a>"
    )


def load_sessions(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("sessions"), list):
        raise ValueError(f"Expected an object with a sessions list: {path}")
    rows = data["sessions"]
    if not all(isinstance(row, dict) for row in rows):
        raise ValueError("Every session record must be an object")
    return data, rows


def fetch_youtube_playlist(url: str, destination: Path) -> dict[str, Any]:
    command = [
        "yt-dlp",
        "--remote-components", "ejs:github",
        "--cookies-from-browser", "chrome",
        "--flat-playlist",
        "--dump-single-json",
        "--no-warnings",
        "--skip-download",
        url,
    ]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip().splitlines()[-8:]
        raise RuntimeError("yt-dlp failed:\n" + "\n".join(detail))
    value = json.loads(completed.stdout)
    if not isinstance(value, dict) or not isinstance(value.get("entries"), list):
        raise ValueError("yt-dlp did not return a playlist object")
    atomic_write_json(destination, value)
    return value


def load_youtube_entries(path: Path, *, source: str) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("entries") if isinstance(data, dict) else data
    if not isinstance(entries, list):
        raise ValueError(f"Expected an entries list in {path}")
    result: list[dict[str, str]] = []
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("id") or not entry.get("title"):
            continue
        video_id = str(entry["id"])
        result.append({
            "id": video_id,
            "title": str(entry["title"]),
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "source": source,
        })
    return result


def load_existing_links(path: Path) -> dict[str, str]:
    """Read already curated official links without trusting table spacing."""
    if not path.exists():
        return {}
    links: dict[str, str] = {}
    url_re = re.compile(r"https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}")
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        match = url_re.search(line)
        if not match:
            continue
        cells = line.split("|")
        if len(cells) < 4:
            continue
        session_title = re.sub(r"\s+\[\d+\]\s*$", "", cells[2].strip())
        key = title_key(session_title)
        if key:
            links.setdefault(key, match.group(0))
    return links


def choose_youtube_link(
    session: dict[str, Any],
    videos: list[dict[str, str]],
    existing_links: dict[str, str],
) -> tuple[str | None, str]:
    session_key = title_key(str(session.get("title", "")))
    if session_key in existing_links:
        return existing_links[session_key], "existing-master"

    session_tokens = token_set(str(session.get("title", "")))
    speaker_names = speaker_last_names(session.get("speakers"))
    candidates: list[tuple[float, float, int, int, int, dict[str, str]]] = []
    for video in videos:
        video_key = title_key(video["title"])
        video_tokens = token_set(title_core(video["title"]))
        shared = len(session_tokens & video_tokens)
        union = len(session_tokens | video_tokens) or 1
        jaccard = shared / union
        sequence = SequenceMatcher(None, session_key, video_key).ratio()
        speaker_overlap = len(speaker_names & token_set(video["title"]))
        video_key_tokens = set(video_key.split())
        equal = session_key == video_key
        contains = session_key in video_key or video_key in session_key
        # Do not treat a two-word video title such as "Perception Agents" as
        # the recording for a longer session called "Build with Perception
        # Agents" unless the named speaker also matches. Short-title
        # containment is otherwise a common source of false links.
        short_containment = contains and not equal and len(video_key_tokens) < 3
        if video.get("source") == "channel" and speaker_overlap == 0:
            continue
        exact = equal or (contains and not short_containment)
        # Exact title overlap is enough. Fuzzy matches must also share session
        # vocabulary and/or a named speaker to avoid linking generic AI videos.
        accepted = (
            exact
            or (sequence >= 0.88 and shared >= 2)
            or (sequence >= 0.68 and shared >= 5 and speaker_overlap >= 1)
            or (sequence >= 0.45 and shared >= 6 and speaker_overlap >= 1)
        )
        if not accepted:
            continue
        score = sequence + (0.25 if exact else 0.0) + min(shared, 8) * 0.02 + min(speaker_overlap, 2) * 0.08
        candidates.append((score, sequence, shared, speaker_overlap, int(exact), video))

    if not candidates:
        return None, "none"
    candidates.sort(key=lambda item: item[:5], reverse=True)
    best = candidates[0]
    second_score = candidates[1][0] if len(candidates) > 1 else 0.0
    # A small margin is acceptable for exact containment; fuzzy guesses need
    # separation from the next candidate.
    if not best[4] and len(candidates) > 1 and best[0] - second_score < 0.06:
        return None, "ambiguous"
    return best[5]["url"], best[5].get("source", "playlist")


def build_keyword_index(rows: list[dict[str, Any]]) -> tuple[Counter[str], dict[str, str]]:
    document_frequency: Counter[str] = Counter()
    display_forms: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        terms = set(token_values(str(row.get("title", "")) + " " + str(row.get("description") or "")))
        for term in terms:
            document_frequency[term] += 1
        for raw in TOKEN_RE.findall(str(row.get("title", "")) + " " + str(row.get("description") or "")):
            folded = fold(raw)
            if folded:
                display_forms[folded][raw] += 1
    canonical = {
        term: counts.most_common(1)[0][0]
        for term, counts in display_forms.items()
        if counts
    }
    return document_frequency, canonical


def display_keyword(term: str, canonical: dict[str, str]) -> str:
    if term in DISPLAY_ACRONYMS:
        return DISPLAY_ACRONYMS[term]
    original = canonical.get(term, term)
    if original.isupper() or any(char.isdigit() for char in original):
        return original
    return term


def keywords_for(row: dict[str, Any], document_frequency: Counter[str], canonical: dict[str, str], total: int) -> str:
    title_terms = Counter(token_values(str(row.get("title", ""))))
    description_terms = Counter(token_values(str(row.get("description") or "")))
    scores: dict[str, float] = {}
    for term in set(title_terms) | set(description_terms):
        if document_frequency[term] > total * 0.48 and term not in DISPLAY_ACRONYMS:
            continue
        idf = math.log((total + 1) / (document_frequency[term] + 1)) + 1.0
        scores[term] = (title_terms[term] * 3.0 + description_terms[term]) * idf
    ranked = sorted(scores, key=lambda term: (-scores[term], term))
    selected: list[str] = []
    for term in ranked:
        shown = display_keyword(term, canonical)
        if shown.lower() in {item.lower() for item in selected}:
            continue
        selected.append(shown)
        if len(selected) == 7:
            break
    if len(selected) < 3:
        for term in token_values(str(row.get("title", "")), remove_stopwords=False):
            shown = display_keyword(term, canonical)
            if shown.lower() not in {item.lower() for item in selected} and term not in {"the", "and", "for"}:
                selected.append(shown)
            if len(selected) == 3:
                break
    if not selected:
        track = str(row.get("track") or "").strip()
        selected = [track if track and not track.lower().startswith("track ") else "conference"]
    return "; ".join(selected)


def generate_markdown(
    rows: list[dict[str, Any]],
    videos: list[dict[str, str]],
    existing_links: dict[str, str],
) -> tuple[str, dict[str, int]]:
    document_frequency, canonical = build_keyword_index(rows)
    total = len(rows)
    linked = 0
    source_counts = Counter()
    video_rows = []
    complete_rows = []
    for index, row in enumerate(rows, start=1):
        youtube, source = choose_youtube_link(row, videos, existing_links)
        if youtube:
            linked += 1
            source_counts[source] += 1
            youtube_cell = youtube_thumbnail(youtube)
        else:
            youtube_cell = "—"
            source_counts[source] += 1
        speakers = row.get("speakers") or []
        speaker_text = ", ".join(str(item) for item in speakers) if speakers else "—"
        session_title = escape_cell(row.get("title")) + " [1]"
        keywords = escape_cell(keywords_for(row, document_frequency, canonical, total))
        if youtube:
            video_rows.append((index, row, youtube, keywords))
        complete_rows.append((
            index,
            row,
            session_title,
            youtube_cell,
            keywords,
            speaker_text,
        ))
    lines = [
        "---",
        "layout: default",
        'title: "AI Engineer World\'s Fair 2026 — All Sessions"',
        "---",
        "",
        "# AI Engineer World's Fair 2026 — All Sessions",
        "",
        f"Complete schedule table generated from the {total}-record `raw/sessions.json` snapshot. Session fields and descriptions are preserved from the official schedule export.[1]",
        "",
        f"YouTube links point to recordings found in the official AI Engineer channel's World's Fair 2026 playlist or channel feed, or previously verified official recording links; `—` means no confident match was found.[2]",
        "",
        "Keywords are deterministic summaries derived from each session title and description; the original track remains in its own column.",
        "",
        "## Table of Contents",
        "",
        "- [Sessions with YouTube recordings](#sessions-with-youtube-recordings)",
        "- [Complete schedule](#complete-schedule)",
        "- [Sources](#sources)",
        "",
        "## Sessions with YouTube recordings",
        "",
        f"Filtered view containing the {linked} schedule records with a confident YouTube match. The original session numbers are retained; repeated links remain when one recording covers multiple schedule records.[2]",
        "",
        "| # | Session | YouTube | Day | Time | Track | Type | Room | Speakers | Keywords | Status |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for index, row, youtube, keywords in video_rows:
        speakers = row.get("speakers") or []
        speaker_text = ", ".join(str(item) for item in speakers) if speakers else "—"
        lines.append(
            "| " + " | ".join([
                str(index),
                escape_cell(row.get("title")) + " [1]",
                youtube_thumbnail(youtube),
                escape_cell(row.get("day")),
                escape_cell(row.get("time")),
                escape_cell(row.get("track")),
                escape_cell(row.get("type")),
                escape_cell(row.get("room")),
                escape_cell(speaker_text),
                keywords,
                escape_cell(row.get("status")),
            ]) + " |"
        )
    lines.extend([
        "",
        "## Complete schedule",
        "",
        "Complete schedule, including records without a confident YouTube match.",
        "",
        "| # | Day | Time | Session | YouTube | Track | Type | Room | Speakers | Keywords | Status |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    for index, row, session_title, youtube_cell, keywords, speaker_text in complete_rows:
        lines.append(
            "| " + " | ".join([
                str(index),
                escape_cell(row.get("day")),
                escape_cell(row.get("time")),
                session_title,
                youtube_cell,
                escape_cell(row.get("track")),
                escape_cell(row.get("type")),
                escape_cell(row.get("room")),
                escape_cell(speaker_text),
                keywords,
                escape_cell(row.get("status")),
            ]) + " |"
        )
    lines.extend([
        "",
        "## Sources",
        "",
        f"[1] {SESSIONS_SOURCE_URL} — official AI Engineer World's Fair 2026 session schedule JSON.",
        f"[2] {YOUTUBE_PLAYLIST_URL} — official AI Engineer World's Fair 2026 Complete Playlist; channel: {YOUTUBE_CHANNEL_URL}.",
        "",
    ])
    stats = {
        "sessions": total,
        "youtube_links": linked,
        "playlist_links": source_counts["playlist"],
        "channel_links": source_counts["channel"],
        "existing_master_links": source_counts["existing-master"],
        "ambiguous_or_unmatched": source_counts["ambiguous"] + source_counts["none"],
        "playlist_entries": len(videos),
    }
    return "\n".join(lines), stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--youtube-json", type=Path, default=DEFAULT_YOUTUBE_JSON)
    parser.add_argument("--youtube-channel-json", type=Path, default=DEFAULT_CHANNEL_JSON)
    parser.add_argument("--youtube-url", default=YOUTUBE_PLAYLIST_URL)
    parser.add_argument("--existing-markdown", type=Path, default=DEFAULT_EXISTING_MARKDOWN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--fetch-youtube", action="store_true", help="Fetch the official playlist with yt-dlp before generating")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    _, rows = load_sessions(args.input)
    if args.fetch_youtube or not args.youtube_json.exists():
        print(f"Fetching YouTube playlist metadata: {args.youtube_url}", file=sys.stderr)
        fetch_youtube_playlist(args.youtube_url, args.youtube_json)
    playlist_videos = load_youtube_entries(args.youtube_json, source="playlist")
    channel_videos = load_youtube_entries(args.youtube_channel_json, source="channel") if args.youtube_channel_json.exists() else []
    playlist_ids = {video["id"] for video in playlist_videos}
    videos = playlist_videos + [video for video in channel_videos if video["id"] not in playlist_ids]
    existing_links = load_existing_links(args.existing_markdown)
    markdown, stats = generate_markdown(rows, videos, existing_links)
    stats["playlist_entries"] = len(playlist_videos)
    stats["channel_entries"] = len(channel_videos)
    atomic_write_text(args.output, markdown)
    print(json.dumps({"output": str(args.output), **stats}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
