#!/usr/bin/env python

def get_message():
    return "Hello, world"

def print_message():
    m = get_message()
    print(m)

x = get_message()

print(x)

print(get_message(), "and the galaxy, too (but not Frostheim)")

def spam():
    return "wombat"

x = spam()
print("x is", x)

for i in range(25):
    spam()
