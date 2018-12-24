#!/usr/bin/env python
# -*- coding: utf-8 -*-

def minMatixMulti(p: tuple):
    n = len(p) - 1
    mutrix = [[(0, 0)] * n for i in range(n)]
    for k in range(n):
        if k == 0:
            continue
        else:
            for j in range(n - k):
                a = mutrix[k - 1][j][0] + p[j] * p[j + k] * p[j + k + 1]
                b = mutrix[k - 1][j + 1][0] + p[j] * p[j + 1] * p[j + k + 1]
                if a < b:
                    mutrix[k][j] = (a, 0)
                else:
                    mutrix[k][j] = (b, 1)
    for line in mutrix:
        print(line)
    return mutrix[n - 1][0]


P = (5, 6, 3, 4, 3)
print(minMatixMulti(P))
