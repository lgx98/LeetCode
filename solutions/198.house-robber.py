# @before-stub-for-debug-begin
from python3problem198 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed, norob = 0, 0
        for num in nums:
            robbed, norob = norob+num, max(robbed, norob)
        return max(robbed, norob)
# @lc code=end
