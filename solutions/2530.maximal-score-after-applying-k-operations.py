#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq as pq
from math import floor


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]
        pq.heapify(nums)
        score = nums[0]
        for _ in range(k-1):
            pq.heapreplace(nums, floor(nums[0] / 3))
            score += nums[0]
        return -score


# @lc code=end
