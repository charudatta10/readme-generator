import json
from jinja2 import Template

class readme_gen:

    def __init__(self) -> None:
        pass
        
    def add_template(self, template_path):
        with open(template_path, mode='r',encoding="utf-8") as template_file:
            template_content = template_file.read()
        # Create a Jinja2 template
        self.template = Template(template_content)   
        
    def add_config(self, config_path):
        with open(config_path, "r") as f:
            self.data = json.load(f)

    def gen_str(self):
        self.doc = self.template.render(**self.data)

    def gen_file(self, readme_path):
        with open(readme_path, "w+", encoding="utf-8") as f:
            f.write(self.doc)

if __name__ == "__main__":
    file = readme_gen()
    file.add_template()
    file.add_config()
    file.gen_str()
    file.gen_file()

