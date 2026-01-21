# @before-stub-for-debug-begin
from python3problem47 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import List
# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used: List[bool] = [False] * len(nums)
        ans: List[List[int]] = []

        def dfs(path: List[int] = []):
            if len(path) == len(nums):
                ans.append(path)
                return
            for i in (i for i in range(len(nums)) if not used[i]):
                if (i > 0) and (nums[i] == nums[i-1]) and (not used[i-1]):
                    continue
                used[i] = True
                dfs(path+[nums[i]])
                used[i] = False
        dfs()
        return ans


# @lc code=end
