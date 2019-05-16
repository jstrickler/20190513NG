#!/usr/bin/env python
import os
import sys

print(sys.executable, '\n')

print(sys.version, '\n')

print(sys.version_info, '\n')

print(sys.prefix, '\n')

for path in sys.path:   # current + PYTHONPATH + builtin
    print(path)
print()

print(sys.platform, '\n')
#  win32 = Windows (32 OR 64-bin)
#  linux* = Linux
#  darwin = Mac

for attribute in sorted(dir(sys)):
    if not attribute.startswith('_'):
        print(attribute)
print()


# from cympy import study
# for attribute in sorted(dir(study)):
#     if not attribute.startswith('_'):
#         print(attribute)
# print()

# os.system("netstat -an")

with os.popen("netstat -an") as netstat_in:
    for raw_line in netstat_in:
        if "ESTAB" in raw_line:
            line = raw_line.rstrip()
            print(line)

