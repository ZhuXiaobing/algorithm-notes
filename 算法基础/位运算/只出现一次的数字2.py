"""
题目：给一组数字，这些数字里面每一个都重复出现了两次，只有两个数字只出现了一个，要求在时间O（n）空间O（1）内解出来。

解题角度：异或运算，然后根据某一个二进制位将数据分组查找。

"""
# 目标数组
l = [1, 2, 7, 1, 2, 4, 5, 5, 34, 34]

# 计算l的异或运算结果
res = 0
for item in l:
    res = res ^ item


# 定义一个函数，找到res的第一个为1的比特位。
def findFirstBit(res, bit):
    if (bit & res) != 0:
        return bit
    else:
        bit = bit << 1
        return findFirstBit(res, bit)


bit = 1
bit = findFirstBit(res, bit)


# 将原始l根据bit指定的位是否为1，分成两个序列
def setAndReturnIndex(l, bit, start, end):
    if (start >= end):
        if ((l[end] & bit) != 0):
            return end
        else:
            return end - 1
    while ((l[start] & bit) != 0):
        start = start + 1
    temp = l[start]
    l[start] = l[end]
    l[end] = temp;
    end = end - 1
    return setAndReturnIndex(l, bit, start, end)


index = setAndReturnIndex(l, bit, 0, len(l) - 1)

# 获取目标数值
id = 0
target1 = 0
target2 = 0
for item in l:
    if id <= index:
        target1 = target1 ^ item
        id = id + 1
    else:
        target2 = target2 ^ item
        id = id + 1

print(target1)
print(target2)
