# @before-stub-for-debug-begin
from python3problem1095 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    def findPeak(self, target: int, mountain_arr: 'MountainArray') -> int:
        l,r=0, mountain_arr.length()-1
        while l<r:
            m0=(l+r)//2
            m1=m0+1
            if(mountain_arr.get(m0)<mountain_arr.get(m1)):
                l=m1
            else:
                r=m0
        return l

    def binsearch(self, target: int, mountain_arr: 'MountainArray',l:int,r:int,asc:bool) -> int:
        while l<=r:
            m=(l+r)//2
            val=mountain_arr.get(m)
            if val==target:
                return m
            if (target<val) == asc:
                r=m-1
            else:
                l=m+1
        return -1


    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        p=self.findPeak(target,mountain_arr)
        print(f"{p}")
        if (ans:= self.binsearch(target,mountain_arr,0,p,True))!=-1:
            return ans
        else:
            return self.binsearch(target,mountain_arr,p+1,mountain_arr.length()-1,False)
        # @lc code=end
#[1,2,3,4,5,3,1]\n2