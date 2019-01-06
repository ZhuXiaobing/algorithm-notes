"""
根据树的前序和中序重构二叉树
"""
from 算法基础.树相关.TreeNode import TreeNode

preList = list('12473568')
midList = list("47215386")

# 根据前序和中序遍历序列构造出树结构。
troot = None


def constructTree(preList: list, midList: list, troot: TreeNode):
    if len(preList) == 0:
        return None
    if troot is None:
        troot = TreeNode()
    troot.val = preList[0]
    if len(preList) == 1:
        return troot
    index = midList.index(preList[0])
    troot.left = constructTree(preList[1:index + 1], midList[0:index], troot.left)
    if index + 1 < len(preList):
        troot.right = constructTree(preList[index + 1:], midList[index + 1:], troot.right)
    return troot


troot = TreeNode()
constructTree(preList, midList, troot)


# print(troot)

# 数的前序遍历序列
def preIter(troot: TreeNode):
    if troot is not None:
        print(troot.val)
        preIter(troot.left)
        preIter(troot.right)


preIter(troot)
