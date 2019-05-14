#!/usr/bin/env python

list1 = list()
cities = ['Millbury', "Worcester", "Sanborn", 'Dorcester',
         'Gloucester', 'Framingham']
list3 = []
list4 = "spam ham eggs toast".split()

print(cities, '\n')
print(list4, '\n')

cities.append('Natick')
cities.append('Waltham')
print(cities, '\n')

more_cities = ['Marlborough', 'Foxborough', 'Concord', 'Lowell']

cities.extend(more_cities)

print(cities[8], '\n')
print(cities[8][2], '\n')


print(cities, '\n')


cities.insert(0, 'Salem')

print(cities, '\n')

cities.insert(5, "Haverhill")

print(cities, '\n')

cities.insert(8, "Leominster")

print(cities, '\n')

print(cities[0], cities[5])

print(cities[-1], cities[-2])

cities[3] = None

print(cities, '\n')

del cities[3]

print(cities, '\n')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

new_list = list(zip(list1, list2))

print("\U0001F92F")

print(new_list)
print(new_list[0], '\n')

print(cities, '\n')

c = cities.pop()

print(c)
print(cities, '\n')

c = cities.pop(4)
print(c)
print(cities, '\n')

cities.remove('Natick')

print(cities, '\n')

print(cities[0], cities[1], cities[2])

#    SEQ[START:STOP]
#    SEQ[START:STOP:STEP]
#    SEQ[:STOP]
#    SEQ[START:]
#    SEQ[:]

print(cities[0:3], '\n')
print(cities[4:9], '\n')

c2 = cities[4:9]

actor = 'Chris Hemsworth'
print(actor[:5])
print(actor[6:])
print(actor[6:9])
print(actor[-5:])
print(actor[0])
print(actor[:-1])
print(actor[1], actor[:5])
print(actor.split()[0])

spam = "fee,fi,fo,fum"
words = spam.split(',')
print(words)
print(words[-1])

print(actor[::2])
print(actor[1::2], '\n')

print(cities, '\n')


for city in cities:
    # city = next(cities)
    # city = next(cities)
    print(city.upper())

print(city)
print()

# for VAR ... in ITERABLE:
#      .... use VAR .....

for char in actor:
    print(char)
print()
















