import json

from . import update_functions as functions
from commands.create import create_functions
from utils import separator
from utils import picker


def update_command(args):
    file_separator = separator.get_platform_separator()
    config, config_path = create_functions.get_project_config(file_separator)

    if config == False:
        print('NOT A CODESEED PROJECT')
        return

    recent = config.get("recent_resources", [])

    if args.rename_from:
        old_filename = args.rename_from
    else:
        if not recent:
            print('NOTHING TO RENAME — NO RECENTLY CREATED RESOURCES TRACKED (last 5 kept). '
                  'Pass one directly: codeseed update --from <name> --to <new-name>')
            return
        old_filename = picker.pick_recent_resource(recent)
        if old_filename is None:
            return

    new_filename = args.rename_to
    if not new_filename:
        new_filename = input("New name for '" + old_filename + "': ").strip()
    if not new_filename:
        print('NEW NAME CANNOT BE EMPTY')
        return

    result = functions.update_files(config["root"], old_filename, new_filename, config["language"], file_separator)
    if result != 'DONE':
        print('PROBLEM RENAMING RESOURCE: ' + result)
        return

    if old_filename in recent:
        recent[recent.index(old_filename)] = new_filename
    config["recent_resources"] = recent
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

    print('RENAMED RESOURCE: ' + old_filename + ' -> ' + new_filename)
    print('NOTE: identifiers were renamed within these files only — if other files '
          'reference "' + old_filename.capitalize() + '", update those manually.')
