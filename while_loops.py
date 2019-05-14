#!/usr/bin/env python

# i = 0
# while i < 5:
#     print("Wombats!")
#     i += 1

while True:
    user_name = input("What is your name (q to quit)? ")
    if user_name == 'q':
        break
    elif user_name.replace(' ', '').replace('\t', '') == '':
        continue

    print(f"Welcome, {user_name}")

