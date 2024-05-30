import json
import subprocess
import os
import logging
from datetime import datetime
import time



now = datetime.now()

logging.basicConfig(level=logging.INFO, filename="a.log")
logging.info(f"Process start file entry : {now}")
def ufunc_getlist(inpt_prompt):
    lines = []
    while True:
        line = input(f"{inpt_prompt}")
        if line:
            lines.append(line)
        else:
            break
    return lines

def ufunc_getdict():
    user_dict = {}
    while True:
        _dict1 = {input(f"Enter question: "): input(f"Enter answer: ") }
        print(_dict1)
        if _dict1 != {"":""}:
            user_dict.update(_dict1)
        else:
            break
    return user_dict

data ={}
temp = input("Is project hosted on GitHub? y/n : ")
if (temp == "n"):
    data["title"]=input("Enter title of project -> ")
else:
    data["title"]=input("Enter Github Project Link -> ").split("/")[-1]
data["description"]=input("Enter project description-> ")
data["features"]= ufunc_getlist("Enter project features -> ")    
data["list_badges"]=ufunc_getlist("Enter softwares used in the project -> ")
data["steps"]=ufunc_getlist("Enter steps to run project -> ") 
data["FAQ"]=ufunc_getdict()
data["dependencies"]=ufunc_getlist("Enter project dependencies -> ")
data["user"]= "charudatta10"
data["contact_link"]= "https://charudatta10.github.io/linktree/"
data["license"]=input("Project is license -> ")
data["img_slogo"]="favicon05.svg"
data["img_profile"]="profile-picture.png"
data["img_screenshot"]=input("Project usage screenshot path -> ")
data["img_preview"]=input("Project preview image path -> ")
data["img_logo"]=input("Enter project logo path -> ")

with open('config.json','w') as f:
    json.dump(data,f,indent=4)

logging.info(f"config file created")
logging.info(f"config file : {data}")
logging.info(f"EOF")




