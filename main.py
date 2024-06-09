from readme_generator import readme_gen

from readme2ppt_gen import readme2ppt

from config_file_gen import config_gen

from pathlib import Path

#from fire import Fire

import os

user_name = os.getlogin()
local_file_path = Path(f"C:/Users/{user_name}/Documents/GitHub/readme-generator/template.md")

class readme_main():

    def __init__(self, config_path, readme_path) -> None:
        self.config_path = Path(config_path)
        self.readme_path = Path(readme_path)
        self.template_path = Path(local_file_path)
        config = config_gen()
        config.get_data()
        config.gen_file(self.config_path)
        readme = readme_gen()
        readme.add_template(self.template_path)
        readme.add_config(self.config_path)
        readme.gen_str()
        readme.gen_file(self.readme_path)
        readme2ppt(self.readme_path)

if __name__ == "__main__":
        config_path = input("Enter path where config is stored-> ")
        readme_path = input("Enter path where readme is stored-> ")
        file = readme_main(config_path, readme_path)
        #Fire(file)