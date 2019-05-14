#!/usr/bin/env python

x = 12.1
y = 3.9

result = x / y

actor = 'Chris Hemsworth'
city = 'Malibu'

print(result)

print(x, "/", y, "=", result)

print(actor, "lives in", city)

t1 = "duck"
t2 = "wombat"
t3 = "Jell-o"
t4 = 1234

print(t1, t2, t3, t4)

print(t1, t2, t3, t4, sep='')

print(t1)
print(t2)
print(t3)
print(t4)
print()

print(t1, end=':')
print(t2, end=':')
print(t3, end=':')
print(t4)

print(t1, t2, t3, t4, sep=' ', end="//")
print("END")

print()
print()
print("More END")

print("{} / {} = {}".format(x, y, result))
print("{} lives in {}".format(actor, city))

print("{} / {} = {:.2f}".format(x, y, result))

print(f"{x} / {y} = {result:.2f}")
print(f"{actor} lives in {city}")


big_number = 293203984203984203948.293093

print("{:,.3f}".format(big_number))

first_name = 'George'
last_name = 'Washington'

print('{:12s} {}'.format(first_name, last_name))

first_name = 'James'
last_name = 'Monroe'

print('{:12s} {}'.format(first_name, last_name))
print('{:>12s} {}'.format(first_name, last_name))
print('{:^12s} {}'.format(first_name, last_name))
