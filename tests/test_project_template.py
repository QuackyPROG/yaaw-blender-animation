import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from yaaw_blender.contracts import validate_project

class TemplateTests(unittest.TestCase):
    def test_template(self):
        p = Path(__file__).resolve().parents[1] / 'projects/_template/project.json'
        with p.open(encoding='utf-8') as f: obj = json.load(f)
        validate_project(obj)
    def test_skills_frontmatter(self):
        base=Path(__file__).resolve().parents[1] / '.agents/skills'
        skill_files=list(base.glob('*/SKILL.md'))
        self.assertGreaterEqual(len(skill_files),6)
        for file in skill_files:
            s=file.read_text(encoding='utf-8')
            self.assertTrue(s.startswith("---" + chr(10)), file)
            self.assertIn(chr(10) + "name:", s, file)
            self.assertIn(chr(10) + "description:", s, file)

if __name__ == '__main__': unittest.main()
