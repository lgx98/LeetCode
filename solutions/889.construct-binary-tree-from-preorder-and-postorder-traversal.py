#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i_lookup = {k: v for v, k in enumerate(postorder)}

        def helper(pre_l, pre_r, post_l, post_r):
            if pre_l < pre_r-1:
                val_l = preorder[pre_l+1]
                post_i = i_lookup[val_l]
                len_l = post_i+1-post_l
                return TreeNode(preorder[pre_l], helper(pre_l+1, pre_l+1+len_l, post_l, post_i+1),
                                helper(pre_l+1+len_l, pre_r, post_i+1, post_r-1))
            elif pre_l == pre_r-1:
                return TreeNode(preorder[pre_l], None, None)
            else:
                return None

        return helper(0, len(preorder), 0, len(postorder))
# @lc code=end
