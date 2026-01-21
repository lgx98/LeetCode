# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        height = len(matrix)
        width = len(matrix[0])
        r, d, l, u = width-1, height-1, 0, 0
        ans:List[int]=[]
        while True:
            ans+=matrix[u][l:r+1]
            u+=1
            if u>d:
                return ans
            ans.extend(matrix[y][r] for y in range(u,d+1))
            r-=1
            if l>r:
                return ans
            ans+=reversed(matrix[d][l:r+1])
            d-=1
            if u>d:
                return ans
            ans.extend(matrix[y][l] for y in range(d,u-1,-1))
            l+=1
            if l>r:
                return ans
# @lc code=end
