import sys

from . import upgrade_functions as functions
from utils.version import VERSION

MANUAL_UPDATE_HINT = "UPDATE MANUALLY INSTEAD: git pull in your CodeSeed clone, then re-run install.sh"


def upgrade_command(args):
    try:
        release = functions.fetch_latest_release()
    except Exception as e:
        print("COULD NOT REACH GITHUB TO CHECK FOR UPDATES: " + str(e))
        return

    latest = release["tag_name"]
    if not functions.is_newer(latest, VERSION):
        print("ALREADY UP TO DATE (v" + VERSION + ")")
        return

    print("NEW VERSION AVAILABLE: v" + VERSION + " -> " + latest)

    if not functions.is_frozen():
        print("RUNNING FROM SOURCE, NOT AN INSTALLED BINARY — NOTHING REPLACED. " + MANUAL_UPDATE_HINT)
        return

    name = functions.asset_name()
    asset = functions.find_asset(release, name)
    if asset is None:
        print("NO " + name + " BINARY ATTACHED TO RELEASE " + latest + ". " + MANUAL_UPDATE_HINT)
        return

    try:
        functions.replace_binary(asset["browser_download_url"], sys.executable)
    except Exception as e:
        # e.g. no write permission, or windows refusing to replace a running exe
        print("UPGRADE FAILED, INSTALLED BINARY LEFT AS IS: " + str(e))
        return

    print("UPGRADED TO " + latest)
