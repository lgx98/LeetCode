#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

from collections import deque
from itertools import islice
from typing import Any, Iterable, Optional, Generator


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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        def rev_inorder_iter(root: TreeNode) -> Generator[TreeNode, None, None]:
            if root.right:
                for node in rev_inorder_iter(root.right):
                    yield node
            yield root
            if root.left:
                for node in rev_inorder_iter(root.left):
                    yield node

        sum = 0
        for node in rev_inorder_iter(root):
            node.val = (sum := sum+node.val)
        return root
        
# @lc code=end

