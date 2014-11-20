#!usr/bin/env python
# -*- coding: utf-8 -*-

def f(max):
    s = 0
    for i in range(1, max):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


print 'The sum of all the multiples of 3 or 5 below 1000 is: %s' % f(1000)
