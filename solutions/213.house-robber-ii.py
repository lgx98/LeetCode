# @before-stub-for-debug-begin
from python3problem213 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import Iterable


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[1:]), self.helper(nums[:-1])) if len(nums) > 1 else nums[0]

    def helper(self, nums: Iterable[int]) -> int:
        robbed, norob = 0, 0
        for num in nums:
            robbed, norob = norob+num, max(robbed, norob)
        return max(robbed, norob)

# @lc code=end
