#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def minMatixMulti(p, i, j):
    if i >= j:
        return 0
    tm = sys.maxsize
    for k in range(i, j):
        min = minMatixMulti(p, i, k) + minMatixMulti(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        if tm > min:
            tm = min
    return tm


P = (5, 6, 3, 4, 3)
print(minMatixMulti(P, 1, len(P) - 1))
