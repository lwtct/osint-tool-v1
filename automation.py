import os
import importlib.util

class Automate():
        def __init__(self):
                self.file_len = -1
                self.dict = {}
                self.filecheck()

        def execute(self, mod_names):
                self.filecheck()
                output_dict = {}
                for name in mod_names:
                        name = name.lower()
                        output_dict[name] = self.dict[name].DomainAutomation().exec()
                return output_dict

        def filecheck(self):
                dir_list = os.listdir("modules")
                if len(dir_list) != self.file_len:
                        print("MODULE CHANGE DETECTED")
                        self.file_len = len(dir_list)
                        for filename in dir_list:
                                if filename != "__pycache__":
                                        spec = importlib.util.spec_from_file_location(filename,"modules/"+filename)
                                        foo = spec.loader.load_module()
                                        self.dict[spec.name.split(".")[0]] = foo
        
