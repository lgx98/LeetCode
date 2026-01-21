# @before-stub-for-debug-begin
from python3problem215 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
# @lc code=start


class Solution:
    def partition(self, nums: List[int], l: int, r: int) -> int:
        p_val = nums[l]
        while l<r:
            while l<r and nums[r]>=p_val:
                r-=1
            nums[l]=nums[r]
            while l<r and nums[l]<p_val:
                l+=1
            nums[r]=nums[l]
        nums[l]=p_val
        return l
    
    def binsearch(self, nums: List[int], k: int, l:int, r:int):
        m=self.partition(nums,l,r)
        if(m<len(nums)-k):
            return self.binsearch(nums, k, m+1,r)
        elif(m>len(nums)-k):
            return self.binsearch(nums, k, l,m-1)
        else:
            return nums[m]

        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.binsearch(nums,k,0,len(nums)-1)
        # @lc code=end
