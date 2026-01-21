#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i_lookup = {k: v for v, k in enumerate(inorder)}

        def helper(pre_l: int, pre_r: int, in_l: int, in_r: int) -> Optional[TreeNode]:
            if pre_l < pre_r:
                val = preorder[pre_l]
                in_i = i_lookup[val]
                len_l = in_i-in_l
                return TreeNode(val, helper(pre_l+1, pre_l+len_l+1, in_l, in_i),
                                helper(pre_l+len_l+1, pre_r, in_i+1, in_r))
            else:
                return None

        return helper(0, len(preorder), 0, len(inorder))


# @lc code=end
