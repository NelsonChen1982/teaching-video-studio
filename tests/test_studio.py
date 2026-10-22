import importlib.util
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
studio=load('studio',ROOT/'skills/teaching-video-studio/scripts/studio.py')
installer=load('installer',ROOT/'install.py')
class Tests(unittest.TestCase):
 def test_init(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'lesson';studio.init_project(p)
   self.assertTrue((p/'PROJECT.json').exists());self.assertFalse((p/'hyperframes.json').exists())
   with self.assertRaises(ValueError):studio.init_project(p)
 def test_inventory(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'inputs';p.mkdir();(p/'教材.txt').write_text('test');(p/'.env').write_text('secret')
   (p/'.private').mkdir();(p/'.private'/'key.txt').write_text('secret')
   outside=Path(d)/'private.txt';outside.write_text('secret');(p/'linked.txt').symlink_to(outside)
   result=studio.inventory(p);self.assertEqual([x['path'] for x in result['assets']],['教材.txt'])
   self.assertEqual(len(result['assets'][0]['sha256']),64)
 def test_captions(self):
  data={'duration':3,'timing_source':'manual','cues':[{'start':.2,'end':1.2,'text':'前端送出請求。'},{'start':1.2,'end':3,'text':'後端處理。'}]}
  self.assertIn('00:00:00,200 --> 00:00:01,200',studio.to_srt(data))
  data['cues'][1]['start']=1.1
  with self.assertRaises(ValueError):studio.to_srt(data)
 def test_bad_times(self):
  for start,end in [(float('nan'),1),(0,float('inf')),(0,4),(.0001,.0002),(-1,1)]:
   with self.subTest(start=start,end=end),self.assertRaises(ValueError):studio.to_srt({'duration':3,'timing_source':'provider','cues':[{'start':start,'end':end,'text':'test'}]})
 def test_estimated(self):
  data={'duration':2,'timing_source':'estimated','cues':[{'start':0,'end':1,'text':'草稿'}]}
  with self.assertRaises(ValueError):studio.to_srt(data)
  self.assertIn('草稿',studio.to_srt(data,True))
 def test_install(self):
  with tempfile.TemporaryDirectory() as d:
   p=installer.install(d);self.assertTrue((p/'references/web-graphics.md').exists())
   with self.assertRaises(FileExistsError):installer.install(d)
 def test_existing_output(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'out';studio.save_new(p,'original')
   with self.assertRaises(FileExistsError):studio.save_new(p,'changed')
   self.assertEqual(p.read_text(),'original')
