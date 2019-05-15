#!/usr/bin/env python


def spam(a, b):
    print("a is {} b is {}".format(a, b))

spam(5, 10)


spam('wombat', 'koala')
print()

def eggs(a, b, *c):
    print("a is {} b is {}".format(a, b))
    print("c is {}".format(c), '\n')

eggs(5, 10, 15)
eggs(5, 10, 15, 20, 25, 30, 35)
eggs(5, 10)
# eggs(5)

def toast(*args):
    print("args:", args, '\n')


toast('a')
toast('a', 'b', 'c')
toast()


x = "squid"
y = "whale"

spam(x, y)

def make_some_big_data_structure_thing():
    pass

spam(x, make_some_big_data_structure_thing())

result = make_some_big_data_structure_thing()
spam(x, result)

def times_ten(func):
    result = func()
    return result * 10

def foo():
    return 12

x = times_ten(foo)
print(x)

def bar():
    return "WOMBAT! "

print(times_ten(bar))












