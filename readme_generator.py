
import json
from jinja2 import Template
from pathlib import Path
import os

user_name = os.getlogin()
local_file_path = Path(f"C:/Users/{user_name}/Documents/GitHub/readme-generator/")

class readme_gen:

    def __init__(self, template_path=local_file_path) -> None:
        self.template_path = Path(template_path)
        

    def add_template(self, template_path=local_file_path):
        with open(template_path, mode='r',encoding="utf-8") as template_file:
            template_content = template_file.read()
        # Create a Jinja2 template
        self.template = Template(template_content)   
        

    def add_config(self, config_path=local_file_path):
        with open(config_path, "r") as f:
            self.data = json.load(f)

    def gen_str(self):
       # self.template_path / "template.md"
        self.doc = self.template.render(**self.data)
       #     features=self.ufunc_lst2str(self.data["features"]),
       #     dependencies=self.ufunc_lst2str(self.data["dependencies"]),



    def gen_file(self, readme_path=local_file_path):
        with open(readme_path, "w+", encoding="utf-8") as f:
            f.write(self.doc)


if __name__ == "__main__":
    file = readme_gen()
    file.add_config()
    file.gen_str()
    file.gen_file()

