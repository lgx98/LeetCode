# @before-stub-for-debug-begin
from python3problem76 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# @lc code=start

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_l,best_r=-1,len(s)-1
        # current window is [l, r)
        l, r = 0, 0
        # the dict for unsatisfied char counts
        rem_counter: Dict[str, int] = dict(Counter(t))
        # the number of unsatisfied chars
        rem_num = len(rem_counter)
        while rem_num != 0 and r < len(s):
            # move right by 1 char
            char_in = s[r]
            r += 1
            if char_in not in rem_counter:
                # char not interested, skip
                continue
            rem_counter[char_in]-=1
            if rem_counter[char_in]==0:
                # this char is satisfied
                rem_num-=1
            
            while rem_num==0:
                # move left by 1 char
                char_out = s[l]
                l+=1
                if char_out not in rem_counter:
                    # char not interested, skip
                    continue
                rem_counter[char_out]+=1
                if rem_counter[char_out]==1:
                    # this char is unsatisfied again
                    rem_num+=1
                    if r-l+1<=best_r-best_l:
                        best_l,best_r=l-1,r
        return s[best_l:best_r]


# @lc code=end
