# @before-stub-for-debug-begin
from python3problem90 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
from typing import List
from copy import deepcopy
# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        used = [False]*n
        ans: List[List[int]] = []

        def dfs(start: int = 0, path: List[int] = []):
            ans.append(deepcopy(path))
            for i in range(start, n):
                if (i > 0) and (nums[i-1] == nums[i]) and (not used[i-1]):
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
                used[i] = False

        dfs()
        return ans
# @lc code=end
