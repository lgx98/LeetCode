#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
from typing import List


class Solution:
    __pre_sum: List[int]
    __w_sum: int

    def __init__(self, w: List[int]):
        random.seed()
        sum = 0
        self.__pre_sum = [None]*len(w)
        for i, num in enumerate(w):
            self.__pre_sum[i] = sum
            sum += num
        self.__w_sum = sum

    def pickIndex(self) -> int:
        target = random.randrange(self.__w_sum)
        l, r = 0, len(self.__pre_sum)
        while l < r-1:
            m = (l+r)//2
            if self.__pre_sum[m] > target:
                r = m
            else:
                l = m
        return l

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()
        # @lc code=end
