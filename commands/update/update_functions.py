import os

from commands.create import create_functions


# renames every layer file for a resource and rewrites the type/var name
# identifiers baked into that file's content (e.g. ProblemInteractor ->
# WidgetInteractor). Anything the user already wrote in these files survives
# the rename — only the exact old identifiers get swapped, not the whole
# file regenerated from the template. Does NOT chase references to the old
# name in other files (e.g. wiring in main.go) — caller is responsible for
# warning about that.
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


def update_files(project_root, old_filename, new_filename, project_language, file_separator):
    if project_language != "golang":
        return "UPDATE IS CURRENTLY ONLY SUPPORTED FOR GOLANG PROJECTS"

    return _rename_golang_files(project_root, old_filename, new_filename, file_separator)
