import os

from . import create_functions as functions

# creates files for every layer
def create_command(args):
    config = functions.get_project_config()
    if config == False:
        print('NOT A CODESEED PROJECT')
        return

    create_files = functions.create_files(config["root"], args.filename, config["language"])
    if create_files == "DONE":
        print("CREATED: " + create_files)
    else:
        print("\n" + "ERROR OCCURED WHILE CREATING → " + create_files + "\n")
        return
