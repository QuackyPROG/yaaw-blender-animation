import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from yaaw_blender.timing import Shot, frame_to_time, time_to_frame, beat_frame, validate_shots
from yaaw_blender.music import beat_sheet
from yaaw_blender.contracts import validate_project

class TimingTests(unittest.TestCase):
    def test_frame_one_zero(self): self.assertEqual(frame_to_time(1,30), 0)
    def test_frame_751_is_25s(self): self.assertEqual(frame_to_time(751,30), Fraction(25,1))
    def test_120bpm_15frames(self): self.assertEqual(beat_frame(1,120,30), 16)
    def test_beatgrid_25s(self): self.assertEqual(len(beat_sheet(120,30,750)), 50)
    def test_continuity(self): validate_shots([Shot('a',1,45),Shot('b',46,90)],1,90)
    def test_gap_fails(self):
        with self.assertRaises(ValueError): validate_shots([Shot('a',1,45),Shot('b',47,90)],1,90)
    def test_overlap_fails(self):
        with self.assertRaises(ValueError): validate_shots([Shot('a',1,55),Shot('b',50,90)],1,90)
    def test_validation(self):
        validate_project({'video': {'fps': 30,'frame_start':1,'frame_end':90}, 'shots':[{'id':'a','start':1,'end':45},{'id':'b','start':46,'end':90}], 'events':[{'id':'impact','frame':16}]})
    def test_bad_event(self):
        with self.assertRaises(ValueError): validate_project({'video': {'fps':30,'frame_start':1,'frame_end':90},'shots':[{'id':'a','start':1,'end':90}], 'events':[{'id':'a','frame':100}]})

if __name__ == '__main__': unittest.main()
