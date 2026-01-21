# @before-stub-for-debug-begin
from python3problem39 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List
# @lc code=start
class Solution:
    # available nums: nums[range_min:]
    def dfs(self, nums: List[int], range_min: int, remaining: int, path: List[int], ans: List[List[int]]):
        if remaining <= 0:
            if remaining == 0:
                ans.append(path[:])
            return
        for index in range(range_min, len(nums)):
            num = nums[index]
            path.append(num)
            self.dfs(nums, index, remaining-num,path,ans)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(candidates, 0, target, [], ans)
        return ans
        
# @lc code=end

