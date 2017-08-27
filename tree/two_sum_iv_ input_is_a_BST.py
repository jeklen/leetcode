# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 遍历二叉树有两种方式
# 1. 迭代：实现简单，但是复杂度比较高
# 2. 用循环代替迭代，实现稍复杂，但是复杂度比较低

class Solution(object):
    def __init__(self):
        self.v = set()
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # 尝试用循环的方式来实现
        while root:
            ...

        pair = k - root.val
        if pair in self.v:
            return True
        self.v.add(root)
