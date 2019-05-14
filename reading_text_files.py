#!/usr/bin/env python
from pprint import pprint

# with open('/Users/jstrick/Desktop/py3intro/DATA/mary.txt') as mary_in:
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
    mary_in.seek(0)  # rewind file (go back to beginning)
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print(contents)
    print('=' * 20)
    print(repr(contents))
    print('=' * 20)
    print(list(contents))
print()

knight_names = []
titles = set()
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_names.append(name)
        titles.add(title)

print(knight_names, '\n')
print(titles)
print('-' * 60)

knight_data = []
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        knight_data.append(fields)

pprint(knight_data)

titles = {k[1] for k in knight_data}
print(titles)

names = [k[0] for k in knight_data]
print(names)


