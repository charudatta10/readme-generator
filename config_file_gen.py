import json
from datetime import datetime
from pathlib import Path

class config_gen():

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
    
    def get_data(self):
        temp = input("Is project hosted on GitHub? y/n : ")
        if (temp == "n"):
            self.data["title"]=input("Enter title of project -> ")
        else:
            self.data["title"]=input("Enter Github Project Link -> ").split("/")[-1]
        self.data["description"]=input("Enter project description-> ")
        self.data["features"]= self._getlist("Enter project features -> ")    
        self.data["list_badges"]= self._getlist("Enter softwares used in the project -> ")
        self.data["steps"]= self._getlist("Enter steps to run project -> ") 
        self.data["FAQ"]= self._getdict()
        self.data["dependencies"]= self._getlist("Enter project dependencies -> ")
        self.data["user"]= "charudatta10"
        self.data["contact_link"]= "https://charudatta10.github.io/linktree/"
        self.data["license"]=input("Project is license -> ")
        self.data["img_slogo"]="favicon05.svg"
        self.data["img_profile"]="profile-picture.png"
        self.data["img_screenshot"]=input("Project usage screenshot path -> ")
        self.data["img_preview"]=input("Project preview image path -> ")
        self.data["img_logo"]=input("Enter project logo path -> ")

    def gen_file(self, file_name='config.json'):
        with open(file_name,'w+') as f:
            json.dump(self.data,f,indent=4)

if __name__ == "__main__":
    config = config_gen()
    config.get_data()
    config.gen_file()





