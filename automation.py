import os
import importlib.util

module_dict = {}

for filename in os.listdir('modules'):
        if filename != "__pycache__":
                spec = importlib.util.spec_from_file_location(filename,"modules/"+filename)
                foo = spec.loader.load_module()
                module_dict[spec.name.split(".")[0]] = foo

print("DONE")
class Automate():
        def __init__(self):
                self.dict = module_dict
        def execute(self, mod_names):
                output_dict = {}
                for name in mod_names:
                        output_dict[name] = module_dict[name].DomainAutomation().exec()
                return output_dict


