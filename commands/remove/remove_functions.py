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


# drops Registered<Name>Router and its call inside Router(), if present
def _unwire_golang_router(project_root, filename, file_separator):
    content, path = create_functions.read_golang_router(project_root, file_separator)
    if content is None:
        return

    type_name = filename.capitalize()
    new_content = create_functions.registered_router_func_re(type_name).sub("\n", content, count=1)
    new_content = create_functions.registered_router_call_re(type_name).sub("", new_content)

    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        print("UNWIRED: Registered" + type_name + "Router FROM " + path)


def remove_files(project_root, filename, project_language, file_separator):
    if project_language != "golang":
        return "REMOVE IS CURRENTLY ONLY SUPPORTED FOR GOLANG PROJECTS"

    result = _remove_golang_files(project_root, filename, file_separator)
    _unwire_golang_router(project_root, filename, file_separator)
    return result


def forget_recent_resource(config, config_path, filename):
    recent = config.get("recent_resources", [])
    if filename in recent:
        recent.remove(filename)
    config["recent_resources"] = recent
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
