# @before-stub-for-debug-begin
from itertools import pairwise
from python3problem98 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
from typing import Generator, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @staticmethod
    def iter_tree(root: TreeNode) -> Generator[TreeNode, None, None]:
        if not root: return
        yield from Solution.iter_tree(root.left)
        yield root
        yield from Solution.iter_tree(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return all(x.val < y.val for (x, y) in pairwise(self.iter_tree(root)))
# @lc code=end
