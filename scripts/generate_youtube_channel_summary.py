#!/usr/bin/env python3
"""Generate a categorized, ranked summary of the full AI Engineer channel feed."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

from generate_youtube_channel_markdown import duration_text, load_entries

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "raw" / "youtube-aiengineer-channel-flat.json"
DEFAULT_OUTPUT = ROOT / "ai-engineer-youtube-channel-summary.md"
CHANNEL_URL = "https://www.youtube.com/@aiDotEngineer/videos"

# Rules are intentionally title-only and deterministic. The first matching rule wins.
CATEGORY_RULES: list[tuple[str, str]] = [
    (
        "Evaluation & observability",
        r"eval|evaluat|benchmark|observab|reliab|verify|verif|prove|llm judge|monitoring|quality gate",
    ),
    (
        "Security & authorization",
        r"security|auth|credential|secret|sandbox|leak|attack|hacker|threat|trust|permission|containment|lethal",
    ),
    (
        "Context, memory & retrieval",
        r"rag|retriev|search|context|memory|document|knowledge|graph|vector|embedding|ontology|chunk",
    ),
    (
        "Voice, multimodal & robotics",
        r"voice|speech|audio|phone call|robot|robotics|embodied|wearable|multimodal|vision|video",
    ),
    (
        "Commerce, finance & payments",
        r"payment|pay\b|commerce|wallet|checkout|stripe|finance|bank|tokenomics|money|insurance|claims|trading",
    ),
    (
        "Model training & architecture",
        r"training|train\b|fine[- ]tun|pretrain|model|llm|attention|multimodal|sota|decoding|distill",
    ),
    (
        "Inference & systems infrastructure",
        r"inference|gpu|cuda|vllm|latency|throughput|kubernetes|serverless|database|cluster|tensor|hardware|compute|runtime|deploy|docker|pipeline",
    ),
    (
        "Coding & software engineering",
        r"code|coding|software|developer|programming|cli|sd[lc]|repo|pull request|\bpr\b|factory|compile|debug|bug|framework",
    ),
    (
        "Agents, harnesses & orchestration",
        r"agent|harness|orchestrat|workflow|skill|autonom|multi[- ]agent|mcp|tool|prompt|copilot",
    ),
    (
        "Enterprise & organizational adoption",
        r"enterprise|company|organisation|organization|adopt|business|product|startup|leadership|m&a|transformation|workforce|gtm|sales|customer|production|management",
    ),
]

CATEGORY_DESCRIPTIONS = {
    "Evaluation & observability": "Testing, monitoring, verification, reliability, and quality gates.",
    "Security & authorization": "Security boundaries, credentials, authorization, isolation, and threats.",
    "Context, memory & retrieval": "Search, RAG, documents, memory, knowledge graphs, and context systems.",
    "Voice, multimodal & robotics": "Voice, speech, video, vision, embodied systems, and robots.",
    "Commerce, finance & payments": "Payments, commerce, financial services, insurance, and token economics.",
    "Model training & architecture": "Model design, training, fine-tuning, architectures, and model behavior.",
    "Inference & systems infrastructure": "Inference, hardware, serving, deployment, databases, and systems scale.",
    "Coding & software engineering": "Software development, code, developer workflows, debugging, and factories.",
    "Agents, harnesses & orchestration": "Agent behavior, harnesses, tools, skills, prompts, and orchestration.",
    "Enterprise & organizational adoption": "Enterprise implementation, products, companies, teams, and adoption.",
    "Other AI engineering": "Titles without a sufficiently specific match in the title taxonomy.",
}


def primary_category(title: str) -> str:
    folded = re.sub(r"[^a-z0-9+#&'-]+", " ", title.lower())
    for category, pattern in CATEGORY_RULES:
        if re.search(pattern, folded):
            return category
    return "Other AI engineering"


def format_views(value: object) -> str:
    if isinstance(value, (int, float)):
        return f"{int(value):,}"
    return "—"


def view_key(entry: dict, feed_rank: int) -> tuple[int, int]:
    value = entry.get("view_count")
    if isinstance(value, (int, float)):
        return (-int(value), feed_rank)
    return (1, feed_rank)


def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def category_anchor(category: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-")
    return f"category-{slug}"


def generate(entries: list[dict], captured_at: str) -> str:
    indexed = []
    for feed_rank, entry in enumerate(entries, start=1):
        indexed.append(
            {
                "entry": entry,
                "feed_rank": feed_rank,
                "category": primary_category(str(entry["title"])),
            }
        )

    by_views = sorted(indexed, key=lambda row: view_key(row["entry"], row["feed_rank"]))
    popularity_rank: dict[str, int] = {}
    for rank, row in enumerate(by_views, start=1):
        if row["entry"].get("view_count") is not None:
            popularity_rank[str(row["entry"]["id"])] = rank

    by_category: dict[str, list[dict]] = defaultdict(list)
    for row in indexed:
        by_category[row["category"]].append(row)

    category_rank: dict[str, int] = {}
    for category, rows in by_category.items():
        rows.sort(key=lambda row: view_key(row["entry"], row["feed_rank"]))
        for rank, row in enumerate(rows, start=1):
            category_rank[str(row["entry"]["id"])] = rank

    missing_view_count = sum(row["entry"].get("view_count") is None for row in indexed)
    ordered_categories = sorted(
        by_category,
        key=lambda category: (-len(by_category[category]), category),
    )

    lines = [
        "---",
        'layout: default',
        'title: "AI Engineer YouTube Channel — Full Categorized Summary"',
        'description: "Full categorized and ranked metadata summary of the official AI Engineer YouTube channel feed."',
        "---",
        "",
        "# AI Engineer YouTube Channel — Full Categorized Summary",
        "",
        f"Full metadata summary of the official [AI Engineer YouTube channel]({CHANNEL_URL}). The snapshot contains **{len(entries)} unique videos** and was captured at **{captured_at}**.[13]",
        "",
        "This is a **title-derived metadata summary**, not a transcript summary of every recording. The primary category is assigned deterministically from title keywords; it is a navigation aid, not a claim about the complete video content.",
        "",
        "## Table of contents",
        "",
        "- [Ranking and fields](#ranking-and-fields)",
        "- [Category overview](#category-overview)",
        "- [Full ranked catalog by category](#full-ranked-catalog-by-category)",
    ]
    for category in ordered_categories:
        lines.append(f"  - [{category}](#{category_anchor(category)})")
    lines.extend(
        [
            "- [Sources](#sources)",
            "",
            "## Ranking and fields",
            "",
            "- **Feed rank:** newest-first position in the official `/videos` feed; rank 1 is the newest upload.[13]",
            f"- **Popularity rank:** descending captured YouTube view count, with feed order breaking ties. {missing_view_count} videos have no captured view count and are shown as `—`.[14]",
            "- **Category rank:** popularity rank within the primary title-derived category.",
            "- View counts are snapshot metadata and can be rounded, stale, or change after capture; they are not quality judgments.[14]",
            "",
            "## Category overview",
            "",
            "| Category | Videos | Share | Description |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for category in ordered_categories:
        count = len(by_category[category])
        share = f"{count / len(entries):.1%}"
        lines.append(
            f"| [{category}](#{category_anchor(category)}) | {count} | {share} | {CATEGORY_DESCRIPTIONS[category]} |"
        )

    lines.extend(
        [
            "",
            "## Full ranked catalog by category",
            "",
            "Each section is sorted by captured popularity within the category. Use **feed rank** to recover the channel's newest-first order.",
            "",
        ]
    )

    for section_number, category in enumerate(ordered_categories, start=1):
        rows = sorted(by_category[category], key=lambda row: view_key(row["entry"], row["feed_rank"]))
        lines.extend(
            [
                f'<a id="{category_anchor(category)}"></a>',
                f"### {section_number}. {category} ({len(rows)} videos)",
                "",
                f"{CATEGORY_DESCRIPTIONS[category]}",
                "",
                "| Category rank | Popularity rank | Feed rank | Views | Duration | Video |",
                "| ---: | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for row in rows:
            entry = row["entry"]
            video_id = str(entry["id"])
            title = escape_cell(str(entry["title"]))
            url = f"https://www.youtube.com/watch?v={video_id}"
            pop = popularity_rank.get(video_id, "—")
            lines.append(
                f"| {category_rank[video_id]} | {pop} | {row['feed_rank']} | {format_views(entry.get('view_count'))} | {duration_text(entry.get('duration'))} | [{title}]({url}) |"
            )
        lines.append("")

    lines.extend(
        [
            "## Sources",
            "",
            f"[13] {CHANNEL_URL} — official AI Engineer channel feed and newest-first ordering.",
            "[14] https://www.youtube.com/ — channel metadata and captured view counts retrieved from YouTube metadata.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--captured-at",
        default="2026-10-19 23:36 UTC",
        help="Human-readable timestamp for the source snapshot.",
    )
    args = parser.parse_args()
    text = generate(load_entries(args.input), args.captured_at)
    args.output.write_text(text, encoding="utf-8")
    print(
        {
            "output": str(args.output),
            "videos": len(load_entries(args.input)),
            "bytes": len(text.encode("utf-8")),
        }
    )


if __name__ == "__main__":
    main()
