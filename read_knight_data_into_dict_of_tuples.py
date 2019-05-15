#!/usr/bin/env python
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    knight_info = read_data(FILE_NAME)

    pretty(knight_info)
    print_stuff(knight_info)
    print_titles_and_names(knight_info)


def read_data(file_name):
    knight_data = {}

    with open(file_name) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment

            # fields = line.split(':')
            # knight_data[fields[0]] = tuple(fields[1:])

    return knight_data


def pretty(data):
    pprint(data)

def print_stuff(data):
    print(data['Lancelot'][1])
    print(data['Bedevere'])
    print()


def print_titles_and_names(data): #    KEY    VALUE     DICT      .items()
    for knight, info in data.items():
        print(info[0], knight)
    print()

# print(list(knight_data.items()), '\n')
#
# for knight, info in knight_data.items():
#     print("knight:", knight)
#     print("info:", info)
#     print()
# print()


main()
