# @before-stub-for-debug-begin
from python3problem303 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
from typing import List


class NumArray:
    __pre_sum: List[int]

    def __init__(self, nums: List[int]):
        sum = 0
        self.__pre_sum = [None]*(len(nums)+1)
        for i, num in enumerate(nums):
            self.__pre_sum[i] = sum
            sum += num
        self.__pre_sum[-1] = sum

    def sumRange(self, left: int, right: int) -> int:
        return self.__pre_sum[right+1]-self.__pre_sum[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
