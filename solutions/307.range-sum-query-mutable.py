# @before-stub-for-debug-begin
from python3problem307 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
from typing import List
# @lc code=start


class NumArray:
    __bit: List[int]
    __nums: List[int]

    def __init__(self, nums: List[int]):
        self.__nums = nums
        self.__bit = [0]+nums
        step = 2
        while step <= len(nums):
            for i in range(step, len(nums)+1, step):
                self.__bit[i] += self.__bit[i-(step >> 1)]
            step <<= 1

    def __prefix_sum(self, index: int) -> int:
        i = index+1
        sum = 0
        while i != 0:
            sum += self.__bit[i]
            i -= i&(-i)
        return sum

    def update(self, index: int, val: int) -> None:
        delta = val-self.__nums[index]
        self.__nums[index] = val
        i = index+1
        while i < len(self.__bit):
            self.__bit[i] += delta
            i += i&(-i)

    def sumRange(self, left: int, right: int) -> int:
        return self.__prefix_sum(right)-self.__prefix_sum(left-1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
