import platform

def get_platform_separator():
    """
    Gets seperator specific to current operating system
    >>> LINUX   -> /
    >>> DARWIN  -> /
    >>> WINDOWS -> \\
    """
    if platform.system() == "Linux" or platform.system() == "Darwin":
        return "/"
    else:
        return "\\"
