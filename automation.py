import os
import importlib.util

class Automate():
        def __init__(self): # init variables
                self.file_len = -1 
                self.dict = {}
                self.filecheck() # execute a filecheck

        def execute(self, mod_names):
                self.filecheck()
                output_list = []
                for name in mod_names:
                        try:
                                name = name.lower()
                                output_list.append(self.dict[name].DomainAutomation().exec())
                        except:
                                output_list.append("Error Module Doesn't Exist")
                                print("{} module doen't exist.".format(name))
                return output_list


        def filecheck(self):
                dir_list = os.listdir("modules") # get all files in modules folder 
                if len(dir_list) != self.file_len: # check if number of file has changed
                        print("MODULE CHANGE DETECTED")
                        self.file_len = len(dir_list) # set file_len variable for upcomming check
                        for filename in dir_list: # loop over every file in modules folder
                                if filename != "__pycache__":  # verify that it isn't the pycache folder
                                        spec = importlib.util.spec_from_file_location(filename,"modules/"+filename) #import module as spec
                                        foo = spec.loader.load_module() # load the spec module as foo
                                        self.dict[spec.name.split(".")[0]] = foo # add the loaded module into the dictionary with the name of the file
        
