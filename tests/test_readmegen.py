from src.readme_generator import ReadmeGen
import unittest
from pathlib import Path

class TestReadmeGen(unittest.TestCase):
    def setUp(self):
        self.readme = ReadmeGen() 
        self.file_name = "tests/test_README.md"
        self.readme.main()

    def test_add_template(self):
        self.assertEqual(self.readme.template_path, Path(__file__).parent.parent / "src/template.md")
        self.assertTrue(hasattr(self.readme, 'template'), "Template doesn't exist.")

    def test_add_config(self):
        self.assertTrue(hasattr(self.readme, 'data'), "Config is missing.")

    def test_gen_str(self):
        self.assertTrue(hasattr(self.readme, 'doc'), "Documentation did not generated.")

    def test_gen_file(self):
        self.assertTrue(Path("README.md").exists(), f"README did not generated.")

# Run the tests
if __name__ == '__main__':
    unittest.main()
