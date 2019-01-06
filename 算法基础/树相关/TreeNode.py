"""
定义树节点
"""


class TreeNode(object):

    def __init__(self, val=None, left=None, right=None):
        self.__val = val
        self.__left = left
        self.__right = right

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self.__val = val
