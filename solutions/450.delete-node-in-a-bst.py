#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
from typing import Optional


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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                max_left: TreeNode = root.left
                while max_left.right:
                    max_left = max_left.right
                root.left = self.deleteNode(root.left, max_left.val)
                max_left.left = root.left
                max_left.right = root.right
                root = max_left
        return root

        # @lc code=end
