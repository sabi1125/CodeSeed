#!/bin/bash

# dist/ and build/ are PyInstaller's own workspace — always start clean so a
# re-run (updating an existing install) doesn't get blocked by leftovers from
# a previous build (or a build that crashed partway through).
rm -rf ./dist ./build

pip3 install -r requirements.txt
mkdir -p ~/.codeseed
python3 -m PyInstaller --distpath=~/.codeseed --onefile --add-data "templates:templates" codeseed.py
