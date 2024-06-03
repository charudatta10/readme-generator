import random
import json

from pathlib import Path
import os

user_name = os.getlogin()
local_file_path = Path(f"C:/Users/{user_name}/Documents/GitHub/readme-generator/")

class readme_gen:

    def __init__(self,
                 template_path=local_file_path,
                 config_path=local_file_path,
                 readme_path=local_file_path,) -> None:
        self.template_path = Path(template_path)
        self.config_path = Path(config_path)
        self.readme_path = Path(readme_path)

    def add_config(self, file_name="config.json"):
        with open(self.config_path / file_name, "r") as f:
            self.data = json.load(f)

    def ufunc_lst2str(self, inpt_list):
        inpt_list = ["- " + item + "\n" for item in inpt_list]
        opt_str = "".join(inpt_list)
        return opt_str

    def ufunc_dict2str(self, inpt_dict):
        opt_str = ""
        for key, value in inpt_dict.items():
            t_str = f"""> {key}?    \n   {value}.    \n   \n"""
            opt_str += t_str
        return opt_str

    def ufunc_badgegen(self, list_badges):
        tlist_badgegen = []
        for i in list_badges:
            badge_label = i.capitalize()
            badge_logo = i
            badge_color = "".join([random.choice("ABCDEF0123456789") for _ in range(6)])
            logo_color = (
                "000" if int(str(badge_color), 16) > int(str("7FFFFF"), 16) else "fff"
            )
            _badgegen = f"![](https://img.shields.io/badge/{badge_label}-{badge_color}?style=for-the-badge&logo={badge_logo}&logoColor={logo_color})"
            tlist_badgegen.append(_badgegen + " ")
        tstr_badgen = "".join(tlist_badgegen)
        return tstr_badgen

    def gen_str(self):
        with open(self.template_path / "template.md", "r", encoding="utf-8") as f:
            tdoc = f.read()
        self.doc = tdoc.format(
            title=self.data["title"],
            description=self.data["description"],
            features=self.ufunc_lst2str(self.data["features"]),
            list_badges=self.ufunc_badgegen(self.data["list_badges"]),
            dependencies=self.ufunc_lst2str(self.data["dependencies"]),
            steps=self.ufunc_lst2str(self.data["steps"]),
            FAQ=self.ufunc_dict2str(self.data["FAQ"]),
            user=self.data["user"],
            contact_link=self.data["contact_link"],
            license=self.data["license"],
            img_slogo=self.data["img_slogo"],
            img_profile=self.data["img_profile"],
            img_screenshot=self.data["img_screenshot"],
            img_preview=self.data["img_preview"],
            img_logo=self.data["img_logo"],
        )

    def gen_file(self, file_name="README.md"):
        with open(file_name, "w+", encoding="utf-8") as f:
            f.write(self.doc)


if __name__ == "__main__":
    file = readme_gen()
    file.add_config()
    file.gen_str()
    file.gen_file()

