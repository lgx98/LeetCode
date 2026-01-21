# @before-stub-for-debug-begin
from python3problem454 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from collections import Counter
from itertools import product
# @lc code=start


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #sum12 = Counter(x+y for x in nums1 for y in nums2)
        #sum34_gen = (x+y for x in nums3 for y in nums4)
        sum12 = Counter(map(sum, product(nums1, nums2)))
        sum34 = Counter(map(sum, product(nums3, nums4)))
        return sum(v*sum34[-k] for k, v in sum12.items())

# @lc code=end
