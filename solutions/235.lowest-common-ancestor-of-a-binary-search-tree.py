#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def search(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(p.val>root.val):
            return self.search(root.right,p,q)
        elif(q.val<root.val):
            return self.search(root.left,p,q)
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        (p, q) = (q, p) if p.val > q.val else (p, q)
        return self.search(root,p,q)

# @lc code=end
