#!/usr/bin/env python
import os
from datetime import datetime
from humanize import naturalsize

FOLDER = 'DATA'
FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)

with open(file_path) as alice_in:
    pass

raw_mod_date = os.path.getmtime(file_path)

print("raw mod date:", raw_mod_date)

mod_date = datetime.fromtimestamp(raw_mod_date)

print("mod date:", mod_date)
print("mod month/year: {}/{}".format(mod_date.month, mod_date.year))

file_size = os.path.getsize(file_path)
print("file size:", file_size)
print("file size:", naturalsize(file_size))

stat_info = os.stat(file_path)
print("stat info:", stat_info, '\n')

print(os.getuid())
print(os.getcwd())
print(os.getpid(), '\n')

print(file_path)
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.abspath(file_path), '\n')


# absolute path on Windows
#  C:\....
#  \\resource\name\name
