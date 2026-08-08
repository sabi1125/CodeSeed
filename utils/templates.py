import os
import sys
import string


def _base_dir():
    # PyInstaller --onefile extracts bundled data to sys._MEIPASS at runtime.
    # In dev (python3 codeseed.py) there is no _MEIPASS, so fall back to the
    # project root (parent of this utils/ folder).
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TEMPLATES_DIR = os.path.join(_base_dir(), 'templates')


def render(relative_path, **kwargs):
    template_path = os.path.join(TEMPLATES_DIR, *relative_path.split('/'))
    with open(template_path, 'r') as f:
        template = string.Template(f.read())
    return template.substitute(**kwargs)
