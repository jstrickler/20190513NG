#!/usr/bin/env python
from difflib import context_diff

with open('DATA/alice.txt') as alice_in:
    alice = [line.rstrip() for line in alice_in]

with open('DATA/betsy.txt') as betsy_in:
    betsy = [line.rstrip() for line in betsy_in]

for line in context_diff(alice, betsy):
    print(line)
