import random
import json


class readme_gen():

    def add_config(self, file):
        with open(file , "r") as f:
            self.data = json.load(f)

    def ufunc_lst2str(self, inpt_list):
        inpt_list = ["- " + item + "\n" for item in inpt_list]
        opt_str = "".join(inpt_list)
        return opt_str

    def ufunc_dict2str(self, inpt_dict):
        opt_str = ""
        for (key, value) in inpt_dict.items():
            t_str = f"""> {key}?    \n   {value}.    \n   \n"""
            opt_str += t_str
        return opt_str

    def ufunc_badgegen(self, list_badges):
        tlist_badgegen = []
        for i in list_badges:
            badge_label = i.capitalize()
            badge_logo = i
            badge_color = ''.join([random.choice('ABCDEF0123456789') for _ in range(6)])
            logo_color =  '000' if int(str(badge_color),16) > int(str('7FFFFF'),16) else 'fff'
            _badgegen = f"![](https://img.shields.io/badge/{badge_label}-{badge_color}?style=for-the-badge&logo={badge_logo}&logoColor={logo_color})"
            tlist_badgegen.append(_badgegen+" ")
        tstr_badgen = "".join(tlist_badgegen)
        return tstr_badgen

    def gen_str(self):
        with open("template.md", "r", encoding="utf-8") as f:
            tdoc = f.read()
        print(self.data)
        self.doc = tdoc.format(title = self.data['title'],
                          description = self.data['description'],
                          features = self.ufunc_lst2str(self.data['features']),
                          list_badges = self.ufunc_badgegen(self.data['list_badges']),
                          dependencies = self.ufunc_lst2str(self.data['dependencies']),
                          steps = self.ufunc_lst2str(self.data['steps']),
                          FAQ = self.ufunc_dict2str(self.data['FAQ']),
                     )

        print(self.doc)

    def gen_file(self):
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(self.doc)
# print(doc)

if __name__ == "__main__":
    file = readme_gen()
    file.add_config("config.json")
    file.gen_str()
    #file.gen_file("README.md")