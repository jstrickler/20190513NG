#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

print(person)
print(type(person))

print(person[0], person[-1])

first_name, last_name, product = person

print(first_name, last_name, product)

#  var1, ...  =  ITERABLE

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, z = values[:3]
print(x, y, z)

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


capitals = [('MA', "Boston"), ('NH', "Concord"),
            ("VT", 'Montpelier'), ('RI', "Providence"),
            ('NY', 'Albany')]

print(capitals[0])
print(capitals[0][0], '\n')

for state, capital in capitals:
    print(f"{capital} is the capital of {state}")
print('-' * 60)

x = ['foo'] * 100

print(x)

print(x[34])

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

print(people[0])
print(people[0][0])
print(people[0][0][0])
# print(people[0][0][0][0])

for _, last_name, _, dob in people:
    print(last_name, dob)

print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

actor = "Chris Hemsworth"

print(len(nums), len(actor), len(people), len(people[0]),
      len(people[0][0]))

print(min(nums), min(actor), min(people))
print(max(nums), max(actor), max(people))

print(sum(nums))

print(sorted(nums))
print(sorted(actor))
print(sorted(people))
print()

r = reversed(nums)

print(r)

for i in reversed(nums):
    print(i)

x = ['a', 'b', 'c']
y = [5, 10, 15]

merged = zip(x, y)
print(merged)

for m in merged:
    print(m)
print()

cities = ['Millbury', "Worcester", "Sanborn", 'Dorcester',
    'Marlborough', 'Foxborough', 'Concord', 'Lowell']


for i, city in enumerate(cities):
    if i < 5:
        print(city)
print()

e = enumerate(cities)
print(list(e), '\n')
print(list(e), '\n')


for city in cities:
    print(city)



i = 0
for city in cities:
    print(i, city)
    i += 1

print("No enumerate():", i)

for i, city in enumerate(cities):
    print(city)


print("With enumerate():", i)


nums = [800, 80, 1000, 32, 255, 400, 5, 5000]


import numpy as np

a = np.array(nums)

print(a)

a += 10

print(a)

print(nums)

indices = list(range(len(nums)))
print(indices)

import random

indices_to_change = random.sample(indices, 3)

print(indices_to_change)

for i in indices_to_change:
    nums[i] *= 10

print(nums)

