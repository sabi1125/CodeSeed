import os
import re
import sys
import json
import platform
import tempfile
import urllib.request

LATEST_RELEASE_URL = "https://api.github.com/repos/sabi1125/CodeSeed/releases/latest"


# "v1.0.1" -> (1, 0, 1). only the leading digits of each part count, so a
# suffix like "v0.2.0-patch" still compares as (0, 2, 0).
def parse_version(tag):
    parts = []
    for part in tag.lstrip("v").split("."):
        match = re.match(r"\d+", part)
        parts.append(int(match.group()) if match else 0)
    return tuple(parts)


def is_newer(latest_tag, installed_version):
    return parse_version(latest_tag) > parse_version(installed_version)


# matches the asset names the release workflow uploads,
# e.g. codeseed-linux-amd64, codeseed-darwin-arm64, codeseed-windows-amd64.exe
def asset_name():
    system = platform.system().lower()
    machine = platform.machine().lower()
    arch = {"x86_64": "amd64", "amd64": "amd64", "arm64": "arm64", "aarch64": "arm64"}.get(machine, machine)
    name = "codeseed-" + system + "-" + arch
    if system == "windows":
        name += ".exe"
    return name


def fetch_latest_release():
    # github's api rejects requests without a User-Agent
    request = urllib.request.Request(LATEST_RELEASE_URL, headers={"User-Agent": "codeseed"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def find_asset(release, name):
    for asset in release.get("assets", []):
        if asset["name"] == name:
            return asset
    return None


# PyInstaller sets sys.frozen; from source sys.executable is python itself,
# which we must never overwrite.
def is_frozen():
    return getattr(sys, "frozen", False)


def download(url, path):
    request = urllib.request.Request(url, headers={"User-Agent": "codeseed"})
    with urllib.request.urlopen(request, timeout=60) as response, open(path, "wb") as f:
        f.write(response.read())


# downloads next to the target (same filesystem) then renames over it, so the
# installed binary is either the old one or the complete new one — never half
# written. a failed download leaves the old binary untouched.
def replace_binary(download_url, target_path):
    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(target_path), prefix=".codeseed-upgrade-")
    os.close(fd)
    try:
        download(download_url, tmp_path)
        os.chmod(tmp_path, 0o755)
        os.replace(tmp_path, target_path)
    except BaseException:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise
