# @before-stub-for-debug-begin
from python3problem167 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1, r+1]


# @lc code=end
