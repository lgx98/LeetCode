# @before-stub-for-debug-begin
from python3problem144 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def traverse(self, root: Optional[TreeNode], values: List[int] = []):
        if not root:
            return
        values.append(root.val)
        self.traverse(root.left, values)
        self.traverse(root.right, values)


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = [] # type: List[int]
        self.traverse(root, ans)
        return ans
        
        
# @lc code=end

