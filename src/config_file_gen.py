import random

class ConfigGen():

    def __init__(self) -> dict:
        self.data = {}
        self.get_data()
        return self.data

    def _getlist(self, inpt_prompt):
        lines = ""
        while True:
            line = input(f"{inpt_prompt}")
            if line:
                lines.append(["- "+ line + "\n"])
            else:
                break
        return lines
    
    def _badgegen(self, list_badges):
        tlist_badgegen = []
        for i in list_badges:
            badge_label = i.capitalize()
            badge_logo = i
            badge_color = "#314042"
            logo_color = (
                "000" if int(str(badge_color), 16) > int(str("7FFFFF"), 16) else "fff"
            )
            #_badgegen = f"![](https://img.shields.io/badge/{badge_label}-#263759?style=for-the-badge&logo={badge_logo}&logoColor={logo_color})"
            _badgegen=f"https://badgen.net/badge/%20/{badge_label}/blue?icon={badge_logo}"
            tlist_badgegen.append(_badgegen + " ")
            _badgegen=f"https://badgen.net/badge/%20/{badge_label}/blue?icon={badge_logo}"
        tstr_badgen = "".join(tlist_badgegen)
        #modify
        return tstr_badgen
    
    def get_data(self):
        
        self.data["title"]=input("Enter title of project -> ")
        self.data["description"]=input("Enter project description-> ")
        self.data["features"]= self._lst2str(self._getlist("Enter project features -> "))    
        self.data["list_badges"]= self._badgegen(self._getlist("Enter softwares used in the project -> "))       
       
if __name__ == "__main__":
    config = ConfigGen()
    





