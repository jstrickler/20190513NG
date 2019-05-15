#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1:", n1, '\n')

n2 = sorted(nums, reverse=True)
print("n2:", n2, '\n')


fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "fig25", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date",
          "2banana"]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(f):
    # print("f:", f)  # once for each element
    return f.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, "\n")

f3 = sorted(fruits, key=str.lower)
print("f3:", f3, "\n")

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

f5 = sorted(fruits, key=len, reverse=True)
print("f5:", f5, '\n')

def custom_sort(wombat):
    return len(wombat), wombat.lower()


f6 = sorted(fruits, key=custom_sort)
print("f6:", f6, '\n')

def wacky(x):
    #  x is NOT THE LIST!!!
    #  x is ONE ELEMENT!!
    print("x is", x)
    return x[-1]

# key function converts ONE ELEMENT to comparison value

f7 = sorted(fruits, key=wacky)
print("f7:", f7, '\n')


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for first_name, last_name, product, dob in sorted(people):
    print(first_name, last_name)
print('-' * 60)

def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, product, dob in sorted(people, key=by_last_name):
    print(first_name, last_name)
print('-' * 60)

data = [
    [5, 8, 19, 2, -3],
    [1, 15, -4, 18, 6],
    [5, 2, 19, 13, 8],
    [11, 2, 7, -1, 10],
]

for d in sorted(data):
    print(d)
print()

def by_col4(row):
    return row[3]

for d in sorted(data, key=by_col4):
    print(d)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

print(list(airports.items()))

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print('-' * 60)

def by_value(kv_pair):
    return kv_pair[1], kv_pair[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print('-' * 60)

print(nums)

print(sorted(nums, key=str), '\n')


for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print('-' * 60)


# lambda PARAM: RETURN_VALUE

# def xxx(PARAM):
#     return RETURN_VALUE
