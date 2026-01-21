#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

from typing import List, Final, Optional


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

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l: int, r: int) -> Optional[TreeNode]:
            if l < r:
                val, idx = max((nums[i], i) for i in range(l, r))
                return TreeNode(val=val, left=helper(l, idx), right=helper(idx+1, r))
            else:
                return None
        return helper(0, len(nums))
        # @lc code=end
