#!/usr/bin/env python3

#from watchdog import
import pathlib
import os

class File:
    def __init__(self):
        self.name = ''
        self.date_created = ''
        self.date_last_modified = ''
        self.ext = ''


class Rule:
    def __init__(self):
        self.matcher = None
        self.dest = None
        self.inner_config = None

    def set_inner_config(self, inner_config):
        self.inner_config = inner_config

    def match(self, file):
        return self.matcher.match(file)

class Config:
    def __init__(self, rules=list([])):
        self.rules = rules

    def match_file(self, file):
        for rule in self.rules:
            if rule.match(file):
                dest = rule.dest.get_loc(file)

                # if folder doesn't exist yet, create it
                if False:
                    os.mkdir()
                os.rename()

class Chest:
    def __init__(self, folder_name):
        self.loc = folder_name

    def get_loc(self, file):
        return self.loc

class FormatChest(Chest):

    def __init__(self, folder_name_format):
        pass


    def get_loc(self, file):
        pass

class MonthChest(FormatChest):
    pass



# Two arguments
# directory to clean
# direction to yml
# default to this directory for both

# gyges_config.yml

# Read a configuration
rules = []
image_folder = Rule()
rules.append(image_folder)

config = Config()

# Actively Organizing
#script_loc = pathlib.Path(__file__).parent.parent.absolute()
hopper_loc = "."

for file_loc in os.listdir(hopper_loc):
    #f = File()
    #config.match_file(f)
    print(file_loc)



# Listening (watchdog)


# Run multiple different instances in each folder
# Or iterate through each folder