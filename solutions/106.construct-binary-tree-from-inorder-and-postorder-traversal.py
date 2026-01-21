#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

from typing import List, Optional


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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i_lookup = {k: v for v, k in enumerate(inorder)}

        def helper(in_l: int, in_r: int, post_l: int, post_r: int):
            if post_l < post_r:
                val = postorder[post_r-1]
                in_i = i_lookup[val]
                len_l = in_i-in_l
                return TreeNode(val, helper(in_l, in_i, post_l, post_l+len_l),
                                helper(in_i+1, in_r, post_l+len_l, post_r-1))
            else:
                return None

        return helper(0, len(inorder), 0, len(postorder))
# @lc code=end
