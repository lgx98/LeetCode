# @before-stub-for-debug-begin
from python3problem543 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
from typing import Optional, Tuple
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        """
        post order traverse the tree
        return (height, max diameter)
        """
        if not root:
            return 0,0
        l_height, l_max_diameter = self.helper(root.left)
        r_height, r_max_diameter = self.helper(root.right)
        height = 1 + max(l_height, r_height)
        diameter = l_height + r_height
        max_diameter = max(diameter, l_max_diameter, r_max_diameter)
        return height, max_diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, ans = self.helper(root)
        return ans
# @lc code=end

