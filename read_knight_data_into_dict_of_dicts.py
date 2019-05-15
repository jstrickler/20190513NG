#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment
        }

        # fields = line.split(':')
        # knight_data[fields[0]] = tuple(fields[1:])

pprint(knight_data)
print()

print(knight_data['Lancelot']['color'])
print(knight_data['Bedevere'])
print()

#    KEY    VALUE     DICT      .items()
for knight, info in knight_data.items():
    print(info['title'], knight)
print()

print(list(knight_data.items()), '\n')

for knight, info in knight_data.items():
    print("knight:", knight)
    print("info:", info)
    print()
print()

