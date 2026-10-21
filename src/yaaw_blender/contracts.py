"""Independent structural validators before a creative spec reaches Blender."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Any
from .timing import Shot, validate_shots

ALLOWED_STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT_RUN", "HUMAN_REVIEW_REQUIRED"}

@dataclass(frozen=True)
class SoundEvent:
    event_id: str
    frame: int
    audio_path: str | None


def validate_project(config: Mapping[str, Any]) -> None:
    """Raise on structural problems; NEVER certify artistic quality."""
    video = config['video']
    fps, start, end = video['fps'], video['frame_start'], video['frame_end']
    if not all(isinstance(i, int) for i in (fps, start, end)) or fps <= 0:
        raise ValueError('Invalid numeric timeline')
    shots = [Shot(s['id'], s['start'], s['end']) for s in config['shots']]
    validate_shots(shots, start, end)
    ids = [s.name for s in shots]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate shot IDs')
    events = config.get('events', [])
    seen = set()
    for event in events:
        event_id, frame = event['id'], event['frame']
        if event_id in seen or not (start <= frame <= end):
            raise ValueError(f'Bad event: {event_id}')
        seen.add(event_id)


def validate_asset_reference(path: str, project_root: str | Path) -> Path:
    root = Path(project_root).resolve()
    candidate = (root / path).resolve()
    if not candidate.is_relative_to(root):
        raise ValueError('Asset path escapes project root')
    if not candidate.exists() or not candidate.is_file():
        raise FileNotFoundError(str(candidate))
    return candidate


def require_human_review(status: str) -> None:
    if status not in ALLOWED_STATUSES:
        raise ValueError('Unknown QA status')
    if status != 'PASS':
        raise RuntimeError(f'Cannot cross approval gate with status {status}')
