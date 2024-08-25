from src.imageGen import ImageGen
import unittest
from pathlib import Path

class TestReadmeGen(unittest.TestCase):
    def setUp(self):
        template_data = {"hero_title": "readme-generator" }
        ImageGen("hero_template.svg","hero.svg", template_data)  

    def test_gen_file(self):
        self.assertTrue(Path("hero.svg").exists(), f"Image did not generated.")

# Run the tests
if __name__ == '__main__':
    unittest.main()
