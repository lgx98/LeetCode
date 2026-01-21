# @before-stub-for-debug-begin
from python3problem40 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

from typing import List
# @lc code=start


class Solution:
    def dfs(self, nums: List[int], start: int, remaining: int, path: List[int], ans: List[List[int]]) -> None:
        if remaining <=0:
            if remaining == 0:
                ans.append(path)
            return
        last_num = None
        for i in range(start, len(nums)):
            num = nums[i]
            if num == last_num:
                continue
            last_num = num
            self.dfs(nums, i+1, remaining - num, path + [num], ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], ans)
        return ans

# @lc code=end
