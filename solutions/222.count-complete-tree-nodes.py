# @before-stub-for-debug-begin
from python3problem222 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        depth = 0
        ptr: Optional[TreeNode] = root
        while ptr:
            depth += 1
            ptr = ptr.left

        finished = False

        def countEmpty(root: Optional[TreeNode], curr_depth: int, depth: int) -> int:
            nonlocal finished
            if not root:
                return (1 << (depth-curr_depth))-1
            if curr_depth == depth-1:
                finished = True
                return 0
            n_empty = 0
            n_empty += countEmpty(root.right, curr_depth+1, depth)
            n_empty += countEmpty(root.left, curr_depth+1, depth)
            return n_empty

        n_empty = countEmpty(root, 0, depth)
        return (1 << depth)-1-n_empty

        # @lc code=end
