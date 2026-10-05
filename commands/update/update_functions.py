import os
import re

from commands.create import create_functions


# renames every layer file for a resource and rewrites the type/var name
# identifiers baked into that file's content (e.g. ProblemInteractor ->
# WidgetInteractor). Anything the user already wrote in these files survives
# the rename — only the exact old identifiers get swapped, not the whole
# file regenerated from the template. Does NOT chase references to the old
# name in other files (e.g. wiring in main.go) — caller is responsible for
# warning about that. router.go is the exception, see _rename_golang_router.
def _rename_golang_files(project_root, old_filename, new_filename, file_separator):
    old_targets = create_functions.golang_layer_targets(project_root, old_filename, file_separator)
    new_targets = create_functions.golang_layer_targets(project_root, new_filename, file_separator)

    old_type_name = old_filename.capitalize()
    new_type_name = new_filename.capitalize()

    for old_target, new_target in zip(old_targets, new_targets):
        if not os.path.exists(old_target["path"]):
            continue

        if os.path.exists(new_target["path"]):
            return new_target["path"]

        with open(old_target["path"], "r") as f:
            content = f.read()

        content = content.replace(old_type_name, new_type_name)
        content = content.replace(old_filename, new_filename)

        with open(new_target["path"], "w") as f:
            f.write(content)
        os.remove(old_target["path"])
        print("RENAMED: " + old_target["path"] + " -> " + new_target["path"])

        old_test_path = old_target["path"][:-3] + "_test.go"
        new_test_path = new_target["path"][:-3] + "_test.go"
        if os.path.exists(old_test_path):
            os.rename(old_test_path, new_test_path)
            print("RENAMED: " + old_test_path + " -> " + new_test_path)

    return "DONE"


# renames Registered<Old>Router and its call inside Router(). Inside that
# function the old type name and the old var/group name (whole word only, so
# e.g. "repo" doesn't touch "repository") are swapped — the rest of router.go
# is left alone.
def _rename_golang_router(project_root, old_filename, new_filename, file_separator):
    content, path = create_functions.read_golang_router(project_root, file_separator)
    if content is None:
        return

    old_type_name = old_filename.capitalize()
    new_type_name = new_filename.capitalize()

    if create_functions.registered_router_func_re(new_type_name).search(content):
        print("SKIPPING ROUTER RENAME: Registered" + new_type_name + "Router ALREADY EXISTS IN " + path)
        return

    def rename_func(match):
        block = match.group(0).replace(old_type_name, new_type_name)
        return re.sub(r"\b" + re.escape(old_filename) + r"\b", new_filename, block)

    new_content = create_functions.registered_router_func_re(old_type_name).sub(rename_func, content, count=1)
    new_content = create_functions.registered_router_call_re(old_type_name).sub(
        lambda m: m.group(0).replace(old_type_name, new_type_name), new_content)

    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        print("RENAMED: Registered" + old_type_name + "Router -> Registered" + new_type_name + "Router IN " + path)


def update_files(project_root, old_filename, new_filename, project_language, file_separator):
    if project_language != "golang":
        return "UPDATE IS CURRENTLY ONLY SUPPORTED FOR GOLANG PROJECTS"

    result = _rename_golang_files(project_root, old_filename, new_filename, file_separator)
    if result == "DONE":
        _rename_golang_router(project_root, old_filename, new_filename, file_separator)
    return result
