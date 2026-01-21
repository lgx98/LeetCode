# @before-stub-for-debug-begin
from python3problem327 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

from typing import List

# @lc code=start


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = 0
        presum: List[int] = [0]
        presum.extend((s := s+num) for num in nums)
        temp: List[int] = [None]*(len(presum)//2)
        # to get the sum of [l,r): presum[r]-presum[l]

        """ merge sort the presum, recursively
        returns the count of valid ranges that lies within [l, r)
        """
        def sort(arr: List[int], l: int, r: int) -> int:
            if(r-l == 1):
                return 0
            m = (l+r)//2
            count = 0
            count += sort(arr, l, m)
            count += sort(arr, m, r)
            count += merge(arr, l, m, r)
            #print(f"sort[{l},{r}): {count}")
            return count

        """ merge the two sorted subarray [l, m) [m, r)
        returns the count of valid ranges, which has ends in different subarrays
        """
        def merge(arr: List[int], l: int, m: int, r: int) -> int:
            nonlocal lower, upper
            # count rangesum
            count = 0
            r_start, r_end = m, m
            for l_num in (arr[i] for i in range(l, m)):
                # move until range_sum >= lower
                while r_start < r and arr[r_start]-l_num < lower:
                    r_start += 1
                # move until range_sum > upper
                while r_end < r and arr[r_end]-l_num <= upper:
                    r_end += 1
                count += r_end-r_start

            # copy [l, m) into temp
            t_len = m-l
            temp[0:t_len] = arr[l:m]
            t_ptr, r_ptr = 0, m
            # while not filled, choose a num from heads of temp and right
            for m_ptr in range(l, r):
                if(t_ptr == t_len):
                    # temp is used up
                    break
                if(r_ptr == r):
                    # right subarray is used up
                    arr[m_ptr:r] = temp[t_ptr:t_len]
                    break
                if(temp[t_ptr] > arr[r_ptr]):
                    arr[m_ptr]=arr[r_ptr]
                    r_ptr+=1
                else:
                    arr[m_ptr]=temp[t_ptr]
                    t_ptr+=1
            #print(f"merge[{l},{m}),[{m},{r}): {count}")
            return count

        ans = sort(presum, 0, len(presum))
        print(ans)
        return ans

        # @lc code=end
