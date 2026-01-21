# @before-stub-for-debug-begin
from python3problem493 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

from typing import List

# @lc code=start


class Solution:
    temp: List[int]

    def m_sort(self, arr: List[int], l: int, r: int) -> int:
        """recursive mergesort on arr[l:r]

        Args:
            arr (List[int]): 
            l (int): 
            r (int): 

        Returns:
            int: # reverse pairs in the range
        """
        # base case
        if(r-l == 1):
            return 0
        m = (l+r)//2
        count = 0
        count += self.m_sort(arr, l, m)
        count += self.m_sort(arr, m, r)
        count += self.m_merge(arr, l, m, r)
        return count

    def m_merge(self, arr: List[int], l: int, m: int, r: int) -> int:
        """ mergesort, merging arr[l:m] and arr[m:r]

        Args:
            arr (List[int]): 
            l (int): 
            m (int): 
            r (int): 

        Returns:
            int: # reverse pairs that lie across two arrays
        """
        # counting
        count = 0
        l_start = l
        for r_num in (arr[i] for i in range(m, r)):
            while(l_start < m and arr[l_start] <= 2*r_num):
                l_start += 1
            if l_start == m:
                break
            count += m-l_start

        # merging
        # copy [l, m) into temp
        t_len = m-l
        self.temp[0:t_len] = arr[l:m]
        t_ptr, r_ptr = 0, m
        # while not filled, choose a num from heads of temp and right
        for m_ptr in range(l, r):
            if(t_ptr == t_len):
                # temp is used up
                break
            if(r_ptr == r):
                # right subarray is used up
                arr[m_ptr:r] = self.temp[t_ptr:t_len]
                break
            if(self.temp[t_ptr] > arr[r_ptr]):
                arr[m_ptr] = arr[r_ptr]
                r_ptr += 1
            else:
                arr[m_ptr] = self.temp[t_ptr]
                t_ptr += 1
        #print(f"merge[{l},{m}),[{m},{r}): {count}")
        return count

    def reversePairs(self, nums: List[int]) -> int:
        self.temp = [None]*(len(nums)//2)
        return self.m_sort(nums, 0, len(nums))


# @lc code=end
