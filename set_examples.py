#!/usr/bin/env python

evan_countries = [
    "Ireland", "England", "France", "Netherlands", "Czech Republic",
    "Hungary", "Croatia", "Canada"
]

colin_countries = [
    "France", "Netherlands", "Belgium", "Germany", "Switzerland",
    "Italy", "Spain", "Turkey", "Vietnam", "UAE", "Canada",
    "Mexico", "Switzerland", "UAE", "UAE", "UAE"
]

evan = set(evan_countries)
colin = set(colin_countries)

print("evan:", evan, '\n')
print("colin:", colin, '\n')

print("Both:", evan & colin ,'\n')
print("Just one:", evan ^ colin ,'\n')
print("Either:", evan | colin, '\n')
print("Just Evan:", evan - colin)
print("Just Colin:", colin - evan)


r1 = 5 + 10
r2 = "foo" + "bar"


for country in "Bulgaria", "Israel", "Spain", "Netherlands":
    print(country, "Evan:", country in evan, "Colin:", country in colin)
