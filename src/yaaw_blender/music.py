"""Simple beat-sheet model, NOT an audio-onset detector."""
from fractions import Fraction
from .timing import beat_frame, beat_time


def beat_sheet(bpm: int, fps: int, duration_frames: int, phase_seconds: float = 0.0) -> list[dict]:
    if bpm <= 0 or fps <= 0 or duration_frames <= 0 or phase_seconds < 0:
        raise ValueError('invalid musical specification')
    sheet = []
    n = 0
    phase = Fraction(str(phase_seconds))
    while True:
        f = beat_frame(n, bpm, fps, phase)
        if f > duration_frames:
            break
        sheet.append({'beat': n, 'frame': f, 'seconds': float(beat_time(n, bpm, phase))})
        n += 1
    return sheet
