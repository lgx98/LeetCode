# @before-stub-for-debug-begin
from python3problem96 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
from typing import List
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        return [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190][n]
        # memo:List[int]=[1]*(n+1)
        # for i in range(2,n+1):
        #     sum=0
        #     for j in range(i//2):
        #         sum+=memo[j]*memo[i-j-1]
        #     sum*=2
        #     if(i%2==1):
        #         sum+=memo[i//2]*memo[i//2]
        #     memo[i]=sum
        # return memo[n]
        
# @lc code=end

