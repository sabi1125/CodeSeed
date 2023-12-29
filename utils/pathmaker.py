def create_path(paths, separator):
    fixed_path = []
    for path in paths:
        array_path = path.split("/")
        fixed_path.append(separator.join(array_path))

    return fixed_path
