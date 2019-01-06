"""
该方法要求所有节点必须不同，如果所有节点值相同，是无法相互推导的。
"""
preList = list('12473568')
midList = list("47215386")
print(preList)
print(midList)
afterList = list('')


def findAfterList(preList: list, midList: list, afterList: list):
    if len(preList) == 1:
        afterList.append(preList[0])
        return afterList
    if (len(preList) == 0):
        return afterList
    root = preList[0]
    index = midList.index(root)
    findAfterList(preList[1:index + 1], midList[0:index], afterList)
    if (index + 1 < len(preList)):
        findAfterList(preList[index + 1:], midList[index + 1:], afterList)
    afterList.append(root)
    return afterList


findAfterList(preList, midList, afterList)
print(afterList)
