from src.readme_generator import ReadmeGen
from src.config_file_gen import ConfigGen
import unittest
from pathlib import Path

class TestReadmeGen(unittest.TestCase):
    def setUp(self):
        self.readme = ReadmeGen()  

    def test_add_template(self):
        self.readme.add_template()
        self.assertEqual(self.readme.template_path, Path(__file__).parent.parent / "src/template.md")




# Run the tests
if __name__ == '__main__':
    unittest.main()
