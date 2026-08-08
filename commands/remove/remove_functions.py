import os
import json

from commands.create import create_functions


# deletes every layer file for one resource, plus its test files if present.
# leaves directories in place — same as create leaves them, harmless empty dirs.
def _remove_golang_files(project_root, filename, file_separator):
    for target in create_functions.golang_layer_targets(project_root, filename, file_separator):
        if os.path.exists(target["path"]):
            os.remove(target["path"])
            print("REMOVED: " + target["path"])

        test_path = target["path"][:-3] + "_test.go"
        if os.path.exists(test_path):
            os.remove(test_path)
            print("REMOVED: " + test_path)

    return "DONE"


def remove_files(project_root, filename, project_language, file_separator):
    if project_language != "golang":
        return "REMOVE IS CURRENTLY ONLY SUPPORTED FOR GOLANG PROJECTS"

    return _remove_golang_files(project_root, filename, file_separator)


def forget_recent_resource(config, config_path, filename):
    recent = config.get("recent_resources", [])
    if filename in recent:
        recent.remove(filename)
    config["recent_resources"] = recent
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
