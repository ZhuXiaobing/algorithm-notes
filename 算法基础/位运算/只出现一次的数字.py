#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目：给一组数字，这些数字里面每一个都重复出现了三次，只有一个数字只出现了一个，要求在时间O（n）空间O（1）内解出来。

解题角度：统计二进制位的个数，肯能否被3整除。

"""
a = [1, 1, 72, 1, 2, 2, 6, 2, 4, 4, 4, 6, 6]
b = [bin(x).replace("0b", "") for x in a]

max = 0
for str in b:
    if len(str) > max:
        max = len(str)

array = [0] * max

for i in range(max):
    target = 1 << i
    count = 0
    for c in a:
        if (target & c) == target:
            count = count + 1
        else:
            count += 0
    array[max - 1 - i] = count

# print(array)

for k in range(len(array)):
    if array[k] % 3 == 0:
        array[k] = 0
    else:
        array[k] = 1

# print(array)

print(a)
for m in a:
    bo = True
    for i in range(len(array)):
        if array[i] == 1:
            t = 1 << len(array) - 1 - i
            if t & m == 0:
                bo = False
    if bo:
        print(m)
