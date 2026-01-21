# @before-stub-for-debug-begin
from python3problem95 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
from typing import List, Optional, Tuple, NamedTuple
from collections import deque
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
from itertools import chain
class Solution:
    
    SerialTree=Tuple[int]
    memo:List[List[SerialTree]]

    def generateSerialTrees(self, n: int)-> None:
        self.memo=[None]*(n+1)
        self.memo[0]=[]
        self.memo[1]=[(0,)]
        for i in range(2,n+1):
            self.memo[i]=[]
            for s_tree in self.memo[i-1]:
                self.memo[i].append(tuple(chain([1],s_tree)))
            for j in range(1,i-1):
                for l_tree, r_tree in ((l,r) for l in self.memo[j] for r in self.memo[i-1-j]):
                    self.memo[i].append(tuple(chain([3],l_tree,r_tree)))
            for s_tree in self.memo[i-1]:
                self.memo[i].append(tuple(chain([2],s_tree)))

    def deserializeTree(self, s_tree: Iterator[TreeNode])->TreeNode:
        s_node:int=next(s_tree)
        node:TreeNode=TreeNode()
        if(s_node&2):
            node.left=self.deserializeTree(s_tree)
        if(s_node&1):
            node.right=self.deserializeTree(s_tree)
        return node

    def inorder_iter(self, root:TreeNode) -> Generator[TreeNode,None,None]:
        if not root: return
        yield from self.inorder_iter(root.left)
        yield root
        yield from self.inorder_iter(root.right)

    def fillTree(self,root:TreeNode)->TreeNode:
        for i,node in enumerate(self.inorder_iter(root)):
            node.val = i+1
        return root

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.generateSerialTrees(n)
        return [self.fillTree(self.deserializeTree(iter(s_tree))) for s_tree in self.memo[n]]
        
# @lc code=end

