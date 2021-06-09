#!/usr/bin/env python3

#from watchdog import
import pathlib
import os

from file import File
from config import Config, NoMatch
from rules.rule import Rule

from args_parser import GygesArgsParser


gyges_parser = GygesArgsParser()
args = gyges_parser.parse_args()

# Read a configuration
rules = []
image_folder = Rule()
rules.append(image_folder)

config = Config()

# Actively Organizing
#script_loc = pathlib.Path(__file__).parent.parent.absolute()
hopper_loc = args.hopper

for file_loc in os.listdir(hopper_loc):
    f = File(file_loc)

    try:
        chest = config.match_file(f)

        # Move file to new location
        # if folder doesn't exist yet, create it
        if os.path.exists(chest):
            os.mkdir(chest)

        final_loc = os.path.join(chest, file_loc)
        os.rename(file_loc, final_loc)

    except NoMatch:
        # Don't move the file
        pass


# Listening (watchdog)
if args.watch:
    print("WATCHING")

# Run multiple different instances in each folder
# Or iterate through each folder