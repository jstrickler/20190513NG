#!/usr/bin/env python
import os

start = '.'
# start = os.path.abspath(".")

for curr_folder, sub_folders, files in os.walk(start):
    if ".git" in curr_folder:
        continue
    print(curr_folder)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_folder, file_name)
            file_size = os.path.getsize(file_path)
            print("    {:6d} {}".format(file_size, file_name))

