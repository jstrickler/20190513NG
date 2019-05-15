#!/usr/bin/env python

t = 'a', 'b', 'c'


def foo(x, *y):
    print(y)


foo(1, 'a', 'b', 'c')

