import random

class ConfigGen():

    def __init__(self) -> None:
        self.data = {}

    def _getlist(self, inpt_prompt):
        lines = []
        while True:
            line = input(f"{inpt_prompt}")
            if line:
                lines.append(line)
            else:
                break
        return lines

    def _getdict(self):
        user_dict = {}
        while True:
            _dict1 = {input(f"Enter question: "): input(f"Enter answer: ") }
            if _dict1 != {"":""}:
                user_dict.update(_dict1)
            else:
                break
        return user_dict
    
    def _lst2str(self, inpt_list):
        inpt_list = ["- " + item + "\n" for item in inpt_list]
        opt_str = "".join(inpt_list)
        return opt_str

    def _dict2str(self, inpt_dict):
        opt_str = ""
        for key, value in inpt_dict.items():
            t_str = f"""> {key}?    \n   {value}.    \n   \n"""
            opt_str += t_str
        return opt_str

    def _badgegen(self, list_badges):
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
    
    def get_data(self):
        
        self.data["title"]=input("Enter title of project -> ")
        self.data["description"]=input("Enter project description-> ")
        self.data["features"]= self._lst2str(self._getlist("Enter project features -> "))    
        self.data["list_badges"]= self._badgegen(self._getlist("Enter softwares used in the project -> "))
        self.data["steps"]= self._lst2str(self._getlist("Enter steps to run project -> ")) 
        self.data["FAQ"]= self._dict2str(self._getdict())
        self.data["dependencies"]= self._lst2str(self._getlist("Enter project dependencies -> "))
        self.data["user"]= "charudatta10"
        self.data["contact_link"]= "https://charudatta10.github.io/linktree/"
        self.data["license"]=input("Project is license -> ")
        self.data["img_slogo"]="favicon05.svg"
        self.data["img_profile"]="profile-picture.png"
        self.data["img_screenshot"]=input("Project usage screenshot path -> ")
        self.data["img_preview"]=input("Project preview image path -> ")
        self.data["img_logo"]=input("Enter project logo path -> ")

    def get_config(self):
        return self.data
        
if __name__ == "__main__":
    config = ConfigGen()
    config.get_data()
    print(config.get_config())





