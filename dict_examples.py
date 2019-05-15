#!/usr/bin/env python


d1 = dict()
d2 = {'BOS': "Boston Logan", "MAN": "Manchester",
      "PVD": "Providence"}
d3 = {}

# simple case
feeder_data = [
    ('36_10_23233', 200000),
    ('54_18_23093', 150000),
    ('22_13_39023', 360000),
]

feeders = dict(feeder_data)

print(feeders['36_10_23233'])

# more complex
feeder_data2 = [
    ('36_10_23233', 200000, 'A'),
    ('54_18_23093', 150000, 'B'),
    ('22_13_39023', 360000, 'C'),
]

feeders2 = {f: (a, b) for f, a, b in feeder_data2}

print(feeders2['36_10_23233'])
print(feeders2['36_10_23233'][0])
print(feeders2['36_10_23233'][1])

list1 = list()
list2 = []

t1 = tuple()
t2 = ()

s1 = set()
# .....

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

print(airports['MCO'])

airports['MAN'] = "Manchester"

print(airports, '\n')

print(airports.get("BOS"))
print(airports.get("BOS", "Boston"))

print(airports, '\n')

print(airports.setdefault("BOS", "Boston"))

print(airports, '\n')

print(airports.setdefault('MCO', 'Disneylandia'))


print(airports.keys(), '\n')
print(airports.values(), '\n')

for a in 'LAX', 'BOS', 'PVD', 'ELM', "RDU":
    print(a, a in airports)
print()

# similar to enumerate(LIST)
for abbr, name in airports.items():
    print(abbr, name.lower())
print()








