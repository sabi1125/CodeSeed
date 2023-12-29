import platform

def get_platform_separator():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        return "/"
    else:
        return "\\"
