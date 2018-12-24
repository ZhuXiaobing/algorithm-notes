# /usr/bin/env python
# -*- coding: utf-8 -*-

class bsclas:

    def binarySearch(self, target, *args):
        arys = args[0]
        xy = args[1]
        sy = args[2]
        arys.sort()
        la = sy + xy
        cur = int(la / 2)
        if target == arys[cur]:
            return cur
        elif xy == sy & target != arys[cur]:
            return "not in the sequence"
        elif (target < arys[cur]) & (cur >= 0):
            return self.binarySearch(target, arys, xy, cur - 1)
        elif (target > arys[cur]) & (cur < len(arys)):
            return self.binarySearch(target, arys, cur + 1, sy)


if __name__ == "__main__":
    arys = [2, 4, 65, 8, 25, 85, 123, 42, 90]
    bc = bsclas()
    print(bc.binarySearch(90, arys, 0, len(arys)))
