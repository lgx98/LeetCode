# @before-stub-for-debug-begin
from python3problem538 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev_inorder_iter(root: TreeNode) -> Generator[TreeNode, None, None]:
            if not root:
                return
            yield from rev_inorder_iter(root.right)
            yield root
            yield from rev_inorder_iter(root.left)

        sum = 0
        for node in rev_inorder_iter(root):
            node.val = (sum := sum+node.val)
        return root
# @lc code=end
