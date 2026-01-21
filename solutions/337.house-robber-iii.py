# @before-stub-for-debug-begin
from python3problem337 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

from typing import Tuple


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
    def helper(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root is None:
            return 0, 0
        l_rob, l_no = self.helper(root.left)
        r_rob, r_no = self.helper(root.right)
        return root.val+l_no+r_no, max(l_rob, l_no)+max(r_rob, r_no)

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(*self.helper(root))
        # @lc code=end
