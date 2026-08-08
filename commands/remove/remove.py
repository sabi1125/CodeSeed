from . import remove_functions as functions
from commands.create import create_functions
from utils import separator
from utils import picker


def remove_command(args):
    file_separator = separator.get_platform_separator()
    config, config_path = create_functions.get_project_config(file_separator)

    if config == False:
        print('NOT A CODESEED PROJECT')
        return

    recent = config.get("recent_resources", [])

    if args.name:
        filename = args.name
    else:
        if not recent:
            print('NOTHING TO REMOVE — NO RECENTLY CREATED RESOURCES TRACKED (last 5 kept). '
                  'Pass a name directly: codeseed remove <name>')
            return
        filename = picker.pick_recent_resource(recent)
        if filename is None:
            return

    result = functions.remove_files(config["root"], filename, config["language"], file_separator)
    if result != 'DONE':
        print('PROBLEM REMOVING RESOURCE: ' + result)
        return

    functions.forget_recent_resource(config, config_path, filename)
    print('REMOVED RESOURCE: ' + filename)
