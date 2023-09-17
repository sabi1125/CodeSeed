#!/bin/bash

file_to_check = "./dist"
second_file_to_check = "./build"

if [ -e "$file_to_check" ]; then
    echo "Your binary has already been built"
elif [ -e "$second_file_to_check" ]; then
    echo "Your binary has already been built"
else
    mkdir ~/.codeseed
    python3 -m PyInstaller --distpath=~/.codeseed --onefile codeseed.py
fi
