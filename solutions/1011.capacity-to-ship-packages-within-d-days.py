# @before-stub-for-debug-begin
from python3problem1011 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from functools import partial
from typing import Callable, List


class Solution:
    def ship_sim(self, capacity: int, weights: List[int]) -> int:
        """ This function performs the package shipping simulation.

        Args:
            weights (List[int]): the weights of the packages
            capacity (int):  the maximum weight capacity of the ship each day

        Returns:
            int: total days needed to ship all the packages
        """
        day, remain = 1, capacity
        for weight in weights:
            if remain < weight:
                day += 1
                remain = capacity-weight
            else:
                remain -= weight
        return day

    def bin_search(self, func: Callable[[int], int], target: int, lo: int, hi: int) -> int:
        """ Performs binary serach on a nonincreasing function

        Args:
            func (Callable[[int], int]): the function being searched
            target (int): the target value
            lo (int): lower bound of the serch(included)
            hi (int): higher bound of the serach(excluded)

        Returns:
            int: the smallest x that satisfies func(x) <= target
        """
        while lo < hi:
            mid = (lo+hi)//2
            if func(mid) > target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        return self.bin_search(
            partial(self.ship_sim, weights=weights), days, max(weights), sum(weights)+1)
        # @lc code=end
