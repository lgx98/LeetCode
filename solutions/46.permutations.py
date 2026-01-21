# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import Set, List
# @lc code=start
class Solution:
    def helper(self, nums: Set[int], prefix: List[int], permutes: List[List[int]]):
        if not nums:
            permutes.append(prefix[:])
            return
        for num in nums:
            prefix.append(num)
            new_nums=nums.copy()
            new_nums.remove(num)
            self.helper(new_nums, prefix, permutes)
            prefix.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.helper(nums,[],ans)
        return ans
# @lc code=end

