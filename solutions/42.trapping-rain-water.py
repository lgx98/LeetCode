# @before-stub-for-debug-begin
from python3problem42 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from itertools import accumulate
# @lc code=start


class Solution:
    def trap(self, height: list[int]) -> int:
        premax = list(accumulate(height, max))
        postmax = height[-1]
        return sum(min(premax[i], postmax := max(postmax, height[i]))-height[i] for i in range(len(height)-1, -1, -1))

    """
    def trap(self, height: list[int]) -> int:
        total=0
        l,r=0, len(height)-1
        lmax,rmax=height[l],height[r]
        while l<r:
            if lmax<=rmax:
                while l<r and height[l]<=lmax:
                    total+=lmax-height[l]
                    l+=1
                lmax=height[l]
            else:
                while l<r and height[r]<=rmax:
                    total+=rmax-height[r]
                    r-=1
                rmax=height[r]
        return total
    """


# @lc code=end
