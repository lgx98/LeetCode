# @before-stub-for-debug-begin
from python3problem216 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def dfs(self, nums: Tuple[int], index: int, path: List[int], ans: List[List[int]], k: int, remain: int):
        if remain <= 0 or len(path) == k:
            if remain ==0 and len(path) == k:
                ans.append(path[:])
            return
        for i in range(index, len(nums)):
            num = nums[i]
            path.append(num)
            self.dfs(nums, i+1, path, ans, k, remain-num)
            path.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        self.dfs(tuple(range(1,10)),0, [], ans,k,n)
        return ans
        # @lc code=end
