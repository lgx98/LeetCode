# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail+=1
                nums[tail]=nums[i]
        return tail+1


# @lc code=end
