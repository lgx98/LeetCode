# @before-stub-for-debug-begin
from python3problem78 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
from copy import deepcopy
# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        n = len(nums)
        for i in range(0, 1 << n):
            subset = []
            for j in range(n):
                if (i % 2) != 0:
                    subset.append(nums[j])
                elif i==0:
                    break
                i = i//2
            ans.append(deepcopy(subset))
        return ans

# @lc code=end
