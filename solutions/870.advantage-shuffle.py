# @before-stub-for-debug-begin
from python3problem870 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
from heapq import heapify, heappop


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        pq = [(-v, i) for i, v in enumerate(nums2)]
        heapify(pq)
        l, r = 0, len(nums1)-1
        ans = [None]*len(nums1)
        while pq:
            v, i = heappop(pq)
            if nums1[r]+v <= 0:
                ans[i] = nums1[l]
                l += 1
            else:
                ans[i] = nums1[r]
                r -= 1
        return ans
# @lc code=end
