#!/usr/bin/env python3
"""Detect new uploads in an ordered AI Engineer YouTube channel snapshot.

The watermark stores the IDs seen in the last applied snapshot. Because the
channel feed is newest-first, the script also reports whether all unseen IDs
form a contiguous prefix before the first previously known ID.
"""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WATERMARK = ROOT / "raw" / "youtube-aiengineer-channel-watermark.json"
CHANNEL_URL = "https://www.youtube.com/@aiDotEngineer/videos"
WATERMARK_SCHEMA_VERSION = 1
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        temporary = Path(handle.name)
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
    temporary.replace(path)


def load_entries(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("entries") if isinstance(data, dict) else data
    if not isinstance(entries, list):
        raise ValueError(f"Expected an entries list in {path}")

    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict) or not entry.get("id"):
            continue
        video_id = str(entry["id"])
        if not VIDEO_ID_RE.fullmatch(video_id):
            raise ValueError(f"Invalid YouTube video ID at entry {index}: {video_id!r}")
        if video_id in seen:
            raise ValueError(f"Duplicate YouTube video ID at entry {index}: {video_id}")
        seen.add(video_id)
        result.append(entry)
    if not result:
        raise ValueError(f"No usable YouTube entries found in {path}")
    return result


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def make_watermark(entries: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [str(entry["id"]) for entry in entries]
    return {
        "schema_version": WATERMARK_SCHEMA_VERSION,
        "source_url": CHANNEL_URL,
        "captured_at_utc": utc_now(),
        "entry_count": len(entries),
        "newest_video_id": ids[0],
        "oldest_video_id": ids[-1],
        "known_video_ids": ids,
    }


def load_watermark(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected a watermark object in {path}")
    if value.get("schema_version") != WATERMARK_SCHEMA_VERSION:
        raise ValueError(
            f"Unsupported watermark schema in {path}: {value.get('schema_version')!r}"
        )
    known_ids = value.get("known_video_ids")
    if not isinstance(known_ids, list) or not known_ids:
        raise ValueError(f"Watermark has no known_video_ids: {path}")
    normalized_ids = [str(video_id) for video_id in known_ids]
    invalid = [video_id for video_id in normalized_ids if not VIDEO_ID_RE.fullmatch(video_id)]
    if invalid:
        raise ValueError(f"Watermark contains invalid video IDs: {invalid[:3]}")
    if len(set(normalized_ids)) != len(normalized_ids):
        raise ValueError(f"Watermark contains duplicate video IDs: {path}")
    value["known_video_ids"] = normalized_ids
    return value


def entry_summary(entry: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"id": str(entry["id"]), "title": str(entry.get("title") or "—")}
    if entry.get("duration") is not None:
        result["duration"] = entry["duration"]
    return result


def detect_range(watermark: dict[str, Any], candidate_entries: list[dict[str, Any]]) -> dict[str, Any]:
    known_ids = set(watermark["known_video_ids"])
    candidate_ids = [str(entry["id"]) for entry in candidate_entries]
    candidate_by_id = {str(entry["id"]): entry for entry in candidate_entries}
    new_entries = [entry for entry in candidate_entries if str(entry["id"]) not in known_ids]
    missing_ids = [video_id for video_id in watermark["known_video_ids"] if video_id not in candidate_by_id]

    boundary_index = next(
        (index for index, video_id in enumerate(candidate_ids) if video_id in known_ids),
        None,
    )
    if boundary_index is None:
        range_status = "watermark-not-found"
        boundary_id = None
        prefix_new_entries = []
    else:
        boundary_id = candidate_ids[boundary_index]
        prefix_new_entries = [
            entry for entry in candidate_entries[:boundary_index]
            if str(entry["id"]) not in known_ids
        ]
        if not new_entries:
            range_status = "no-change"
        elif len(prefix_new_entries) == len(new_entries):
            range_status = "complete-prefix"
        else:
            range_status = "interleaved-new-ids"

    return {
        "watermark": {
            "captured_at_utc": watermark.get("captured_at_utc"),
            "entry_count": watermark.get("entry_count", len(known_ids)),
            "newest_video_id": watermark.get("newest_video_id"),
            "oldest_video_id": watermark.get("oldest_video_id"),
        },
        "candidate": {
            "entry_count": len(candidate_entries),
            "newest_video_id": candidate_ids[0],
            "oldest_video_id": candidate_ids[-1],
        },
        "range": {
            "status": range_status,
            "boundary_video_id": boundary_id,
            "boundary_index": boundary_index + 1 if boundary_index is not None else None,
            "new_video_ids": [str(entry["id"]) for entry in prefix_new_entries],
        },
        "new_entries": [entry_summary(entry) for entry in new_entries],
        "missing_video_ids": missing_ids,
    }


def render_text(result: dict[str, Any]) -> str:
    watermark = result["watermark"]
    candidate = result["candidate"]
    update_range = result["range"]
    lines = [
        f"status: {update_range['status']}",
        f"watermark: {watermark['entry_count']} entries, newest {watermark['newest_video_id']}",
        f"candidate: {candidate['entry_count']} entries, newest {candidate['newest_video_id']}",
        f"new uploads: {len(result['new_entries'])}",
    ]
    if update_range["boundary_video_id"]:
        lines.append(
            f"boundary: {update_range['boundary_video_id']} at candidate position "
            f"{update_range['boundary_index']}"
        )
    if result["missing_video_ids"]:
        lines.append(f"missing from candidate: {len(result['missing_video_ids'])}")
    if result["new_entries"]:
        lines.append("new upload range:")
        for entry in result["new_entries"]:
            lines.append(f"- {entry['id']} — {entry['title']}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True, help="Fresh channel JSON snapshot")
    parser.add_argument("--watermark", type=Path, default=DEFAULT_WATERMARK)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument(
        "--initialize",
        action="store_true",
        help="Create the watermark from the candidate instead of comparing it",
    )
    parser.add_argument(
        "--write-watermark",
        action="store_true",
        help="Advance the watermark to the candidate after comparison",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow initialization to replace an existing watermark",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    candidate_entries = load_entries(args.candidate)

    if args.initialize:
        if args.watermark.exists() and not args.force:
            raise SystemExit(
                f"Refusing to replace existing watermark {args.watermark}; use --force if intended"
            )
        watermark = make_watermark(candidate_entries)
        atomic_write_json(args.watermark, watermark)
        result = {
            "status": "initialized",
            "watermark_path": str(args.watermark),
            "entry_count": len(candidate_entries),
            "newest_video_id": watermark["newest_video_id"],
        }
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else render_text({
            "watermark": watermark,
            "candidate": {
                "entry_count": len(candidate_entries),
                "newest_video_id": watermark["newest_video_id"],
            },
            "range": {"status": "initialized", "boundary_video_id": None},
            "new_entries": [],
            "missing_video_ids": [],
        }))
        return 0

    if not args.watermark.exists():
        raise SystemExit(
            f"Watermark not found: {args.watermark}; initialize it with --initialize first"
        )
    watermark = load_watermark(args.watermark)
    result = detect_range(watermark, candidate_entries)

    if args.write_watermark:
        if (
            result["range"]["status"] == "watermark-not-found"
            or result["missing_video_ids"]
        ) and not args.force:
            raise SystemExit(
                "Refusing to advance the watermark: the candidate is missing the prior "
                "boundary or known IDs; use --force only after checking for an incomplete "
                "feed or deliberate removals"
            )
        new_watermark = make_watermark(candidate_entries)
        atomic_write_json(args.watermark, new_watermark)
        result["watermark_written"] = str(args.watermark)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
        if args.write_watermark:
            print(f"watermark written: {args.watermark}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
