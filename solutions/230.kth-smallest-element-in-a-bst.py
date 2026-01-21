# @before-stub-for-debug-begin
from python3problem230 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def tree_iter(root: TreeNode) -> Generator[TreeNode, None, None]:
            if not root: return
            yield from tree_iter(root.left)
            yield root
            yield from tree_iter(root.right)

        def iter_ith(it: Iterable, i: int)->Any:
            return next(islice(it, i, None))
        ans = iter_ith(tree_iter(root), k-1).val
        return ans
# @lc code=end
