#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

rx_code = re.compile(r'[a-z]\d{2,3}', re.I)  # <1>

#  re.IGNORECASE   re.I
#  re.MULTILINE    re.M    ^ and $ match embedded lines
#  re.DOTALL       re.S  (aka singleline)  . matches \n in strings
#  re.LOCALE       re.L
#  re.VERBOSE      re.X

if rx_code.search(s):  # <2>
    print("Found pattern.")
print()

m = rx_code.search(s)
if m:
    print("Found:", m.group())
print()

for m in rx_code.finditer(s):
    print(m.group())
print()

matches = rx_code.findall(s)
print("matches:", matches)


with open('../DATA/mary.txt') as mary_in:
    mary = mary_in.read()

print(repr(mary))
print()
print(mary)
print()

print(re.search(r'^M', mary))
print(re.search(r'^A', mary, re.M))

print(re.findall(r'^[A-Z][a-z]+', mary, re.M), '\n')

for m in re.finditer(r'[rm]([aeiou])', mary, re.I):
    print(m.group(0), m.start(0), m.group(1), m.start(1))



