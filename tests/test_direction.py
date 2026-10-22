import copy
import importlib.util
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('direction',ROOT/'skills/teaching-video-studio/scripts/validate_direction.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class DirectionTests(unittest.TestCase):
 def setUp(self):self.data=json.loads((ROOT/'examples/direction.json').read_text())
 def test_valid_but_not_reviewed(self):
  self.assertEqual(m.validate(self.data),[]);self.assertTrue(m.validate(self.data,True))
 def test_no_automatic_review(self):
  x=copy.deepcopy(self.data);m.validate(x,True);self.assertEqual(x,self.data)
 def test_missing_options_and_reason(self):
  self.data['transitions'][0]['candidates']=[];self.data['transitions'][0]['reason']='';self.assertGreaterEqual(len(m.validate(self.data)),2)
 def test_nonexistent_choice(self):
  self.data['transitions'][0]['selected']='made-up';self.assertTrue(m.validate(self.data))
 def test_no_visual_taste_automation(self):
  self.data['review']={'styleframe':'passed','transition_sample':'passed','evidence':['boards/style.png','sample.mp4 at 1.2s']};self.assertEqual(m.validate(self.data,True),[])
