#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from math import gcd
from typing import List
from itertools import takewhile


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0]*(target+1)
        memo[0] = 1
        nums.sort()
        nums = list(takewhile(lambda x: x <= target, nums))
        if (g := gcd(*nums)) == 0 or (g > 1 and (target % g) != 0):
            return 0
        for i in range(target):
            if not nums:
                break
            if nums[-1] > target-i:
                nums.pop()
            for step in nums:
                memo[i+step] += memo[i]
        return memo[-1]


# @lc code=end
