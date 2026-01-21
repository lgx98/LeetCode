#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

from typing import List, Optional, Dict, Tuple


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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo: Dict[Tuple[int], bool] = {}
        ans: List[TreeNode] = []
        if not root:
            return []

        def helper(root) -> Tuple[int]:
            nonlocal memo, ans
            ret: Tuple[int] = tuple()
            num = root.val
            if root.left:
                num += 1024
                ret += helper(root.left)
            if root.right:
                num += 512
                ret += helper(root.right)
            ret += (num,)
            if ret not in memo.keys():
                memo[ret] = True
            elif memo[ret]:
                ans.append(root)
                memo[ret] = False
            return ret

        helper(root)
        return ans

# @lc code=end
