# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(nums)
        ans = [-1, -1]
        if len(nums) == 0:
            return ans
        # invariable:
        # all(num < target for num in nums[:l]) and all(num >= target for num in nums[r:])
        # bin-search until l == r
        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        if l>= len(nums) or nums[l] != target:
            return ans
        else:
            ans[0] = l

        r = len(nums)
        # invariable:
        # all(num <= target for num in nums[:l]) and all(num > target for num in nums[r:])
        # bin-search until l == r
        while l < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m+1
            else:
                r = m
        ans[1] = r-1
        return ans


# @lc code=end
