"""Exact, deterministic frame and musical beat conversions."""
from dataclasses import dataclass
from fractions import Fraction


def frame_to_time(frame: int, fps: int = 30) -> Fraction:
    if frame < 1 or fps <= 0:
        raise ValueError('frame must be >= 1 and fps > 0')
    return Fraction(frame - 1, fps)


def time_to_frame(seconds: Fraction | float | int, fps: int = 30) -> int:
    if fps <= 0 or seconds < 0:
        raise ValueError('time must be nonnegative and fps > 0')
    x = Fraction(str(seconds)) * fps
    return (2 * x.numerator + x.denominator) // (2 * x.denominator) + 1


def beat_time(beat_index: int, bpm: int, offset: Fraction = Fraction(0)) -> Fraction:
    if beat_index < 0 or bpm <= 0:
        raise ValueError('invalid beat index or bpm')
    return offset + Fraction(60 * beat_index, bpm)


def beat_frame(beat_index: int, bpm: int, fps: int = 30, offset: Fraction = Fraction(0)) -> int:
    return time_to_frame(beat_time(beat_index, bpm, offset), fps)


@dataclass(frozen=True)
class Shot:
    name: str
    start: int
    end: int

    def __post_init__(self):
        if not self.name or self.start < 1 or self.end < self.start:
            raise ValueError('Shot must have nonempty name and valid inclusive frame interval')

    @property
    def frame_count(self) -> int:
        return self.end - self.start + 1


def validate_shots(shots: list[Shot], first: int, last: int) -> None:
    if first < 1 or last < first or not shots:
        raise ValueError('Invalid frame range')
    expected = first
    for shot in shots:
        if shot.start != expected:
            raise ValueError(f'Shot {shot.name} begins at {shot.start}; expected {expected}')
        expected = shot.end + 1
    if expected != last + 1:
        raise ValueError(f'Final shot ends at {expected-1}; expected {last}')
