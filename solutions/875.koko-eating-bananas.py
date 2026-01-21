# @before-stub-for-debug-begin
from python3problem875 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from functools import partial
from math import ceil
from typing import Callable, List


class Solution:
    def eat_sim(self, speed: int, piles: List[int]):
        return sum(map(lambda x: ceil(x/speed), piles))

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

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        ans= self.bin_search(partial(self.eat_sim, piles=piles), h, ceil(sum(piles)/h), max(piles))
        return ans
        # @lc code=end
