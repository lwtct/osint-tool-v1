import os
import importlib.util

module_dict = {}

for filename in os.listdir('modules'):
    if filename != "__pycache__":
        spec = importlib.util.spec_from_file_location(filename,"modules/"+filename)
        foo = spec.loader.load_module()
        module_dict[spec.name] = foo

for key in module_dict.keys():
    module_dict[key].exec()

