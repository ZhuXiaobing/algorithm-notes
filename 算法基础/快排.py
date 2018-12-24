#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
快速排序的思想 :
    核心就是start 以及 end 来回填那个空格（因为挖空游标元素留下来的空）。
    初始的[]是游标所在的位置，之后就在start和end来回跳动。初始时stard占据游标位。
"""


def quicksort(array: list, initStart: int, initEnd: int):
    if initStart >= initEnd or initStart < 0 or initEnd >= len(array):
        return
    temp = array[initStart]
    start, end = initStart, initEnd
    while start != end:
        while end > start:
            if array[end] > temp:
                end = end - 1
            else:
                array[start] = array[end]
                start += 1
                break;  # 此处的break语句特别容易忘记。
        while start < end:
            if array[start] <= temp:
                start += 1
            else:
                array[end] = array[start]
                end -= 1
                break
    array[start] = temp
    quicksort(array, initStart, start - 1)
    quicksort(array, start + 1, initEnd)


l = [5, 4, 7, 2, 10, 1, 9, 824, 12, 2314, 62, 1, 2, 5, 524, 52, 123, 64, 1, 6432]
quicksort(l, 0, len(l) - 1)
print(str(l))
