#!/usr/bin/env python

MAX = 50

hand = 25
football = 100

print("foot is", hand)



SPECIAL_VALUE = 100   # global variable


def spam():
    x = 25
    if x < MAX:
        print("wahooo")

    animal = "wolverine"   # local variable
    print("in spam(), x is", x)

spam()

# print("animal is", animal)

print("in main: SPECIAL_VALUE is", SPECIAL_VALUE)
