#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getLargestPrimeFactor(num):
    i = 2
    r = []
    while i ** 2 < num:
        while num % i == 0:
            num = num / i
        r.append(num)
        i += 1
    return r.pop()


print getLargestPrimeFactor(600851475143)
