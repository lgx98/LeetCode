#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        best_end=nums[0]
        for num in nums[1:]:
            best_end=max(best_end,0)+num
            best=max(best,best_end)
        return best

        
# @lc code=end

