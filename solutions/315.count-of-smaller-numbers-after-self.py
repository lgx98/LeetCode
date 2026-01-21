# @before-stub-for-debug-begin
from python3problem315 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

from typing import List, Tuple
# @lc code=start
# CDQ divide and conquer
# for the problem of finding pair [x,y] in range [l,r):
# divide into 3 sub-problems:
#   1) finding pair [x,y] in [l,m);
#   2) in [m,r); and
#   3) x in [l,m), y in [m,r)
# the first two can be divided and solved recursively,
# and deal with the last one
# also we want to make the array stably sorted for quick lookup


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # pre-allocating list for answer
        ans: List[int] = [0]*len(nums)
        # bind each num with its original idx
        pairs: List[Tuple[int, int]] = [
            (num, idx) for idx, num in enumerate(nums)]
        temp: List[Tuple[int, int]] = [None]*len(nums)

        def helper(l: int, r: int) -> None:
            nonlocal ans, pairs,temp
            if l >= r-1:  # the range is empty or a single element
                return
            m = (l+r+1)//2  # make sure that left part is not longer than right part
            helper(l, m)
            helper(m, r)
            temp[l:m] = pairs[l:m]
            i, j = l, m  # curr_ptr for l_copy; [m,r) and result
            for k in range(l, r):
                if i == m:  # left part is used up
                    break
                elif j == r:  # right part is used up
                    pairs[k:r] = temp[i:m]
                    num_smaller = j-m
                    for pair in temp[i:m]:
                        ans[pair[1]] += num_smaller
                    break
                elif temp[i][0] > pairs[j][0]:  # use right
                    pairs[k] = pairs[j]
                    j += 1
                else:  # use left
                    pairs[k] = temp[i]
                    ans[temp[i][1]] += j-m
                    i += 1

        helper(0, len(nums))
        return ans


# @lc code=end
