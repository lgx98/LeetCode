# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List, Dict
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        known: Dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in known.keys():
                return [i, known[num]]
            else:
                known[target-num] = i
# @lc code=end
