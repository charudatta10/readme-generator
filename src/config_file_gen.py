import random

class ConfigGen():

    def __init__(self) -> dict:
        self.data = {}

    def _getlist(self, input_prompt):
        lines = ""
        while True:
            line = input(f"{input_prompt}")
            if line:
                lines += f"- {line} \n"
            else:
                break
        return lines
    
    def _labelGen(self, input_prompt):
        list_labels = ""
        while True:
            line = input(f"{input_prompt}")
            if line:
                list_labels +=  f"`{line}` "
            else:
                break
        return list_labels
    
    def get_data(self):
        
        self.data["title"]=input("Enter title of project -> ")
        self.data["description"]=input("Enter project description-> ")
        self.data["features"]= self._getlist("Enter project features -> ")    
        self.data["list_badges"]= self._labelGen("Enter softwares used in the project -> ")     
       
if __name__ == "__main__":
    config = ConfigGen()
    config.get_data()
    





