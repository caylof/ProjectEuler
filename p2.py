#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(max):
    a, b = 1, 2
    while a <= max:
        yield b
        a, b = b, a+b


def sumFibByEven(max):
    s = 0
    for i in fib(max):
        if i % 2 == 0:
            s += i
    return s


print sumFibByEven(4000000)
