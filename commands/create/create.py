import os

from . import create_functions as functions
from utils import separator

# creates files for every layer
def create_command(args):
    for filename in args.files:
        file_separator = separator.get_platform_separator()
        config = functions.get_project_config(file_separator)

        if config == False:
            print('NOT A CODESEED PROJECT')
            return

        create_files = functions.create_files(config["root"], filename, config["language"], file_separator, args.withtest)
        if create_files == "DONE":
            print("CREATED: " + create_files)
        else:
            print("\n" + "ERROR OCCURED WHILE CREATING → " + create_files + "\n")
            return
