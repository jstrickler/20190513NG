#!/usr/bin/env python

for i in range(10):
    print("I like wombats!")
print()

#  range(STOP)  range(START, STOP) range(START, STOP, STEP)

for i in range(1, 11):
    print(i)
print()

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

indices = list(range(len(nums)))
print(indices)

for i in range(5, 101, 5):
    print(i, end=" ", sep="x") #
print()

print("\U0001F92F")

print("foo", "bar", "blah", sep="/")
