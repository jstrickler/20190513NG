#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        # name, title, color, quest, comment = line.split(':')
        # knight_data[name] = title, color, quest, comment

        fields = line.split(':')
        knight_data[fields[0]] = tuple(fields[1:])

pprint(knight_data)
print()

print(knight_data['Lancelot'][1])
print(knight_data['Bedevere'])

