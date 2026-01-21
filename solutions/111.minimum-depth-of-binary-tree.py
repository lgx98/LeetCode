# @before-stub-for-debug-begin
import re
from python3problem111 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
from typing import Deque, Optional
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
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        to_visit = deque([root]) #type: Deque[TreeNode|None]
        while (n := len(to_visit)) != 0:
            for _ in range(n):
                curr = to_visit.popleft()
                curr_is_leaf = True
                if (curr_l := curr.left):
                    to_visit.append(curr_l)
                    curr_is_leaf = False
                if (curr_r := curr.right):
                    to_visit.append(curr_r)
                    curr_is_leaf = False
                if curr_is_leaf:
                    return depth
            depth += 1
# @lc code=end

