from readme_generator import readme_gen

from readme2ppt_gen import readme2ppt

from config_file_gen import config_gen

from pathlib import Path

from fire import Fire

class readme_main():

    def __init__(self, config_path, readme_path) -> None:
        self.config_path = Path(config_path)
        self.readme_path = Path(readme_path)
        print('debug step 1')
        config = config_gen()
        config.get_data()
        config.gen_file(self.config_path)
        print('debug step 2')
        readme = readme_gen()
        readme.add_config()
        readme.gen_str()
        readme.gen_file(self.readme_path)
        print('debug step 3')
        readme2ppt(self.readme_path)

if __name__ == "__main__":
        config_path = input("Enter path where config is stored-> ")
        readme_path = input("Enter path where readme is stored-> ")
        file = readme_main(config_path, readme_path)
        Fire(file)