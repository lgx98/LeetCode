# @before-stub-for-debug-begin
from python3problem238 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from collections import deque
# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, ans = 1, [1]
        ans.extend((prod := prod*nums[i]) for i in range(len(nums)-1))
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= prod
            prod *= nums[i]
        return ans
        # deque(,maxlen=0)
# @lc code=end
