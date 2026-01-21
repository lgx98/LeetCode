# @before-stub-for-debug-begin
from python3problem438 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from typing import List
from collections import Counter
# @lc code=start


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans: List[int] = []
        exp_cnt: Counter[str] = Counter(p)
        window_cnt: Counter[str] = Counter(s[:len(p)])
        l, r = 0, len(p)
        if not +(exp_cnt-window_cnt):
            ans.append(l)
        while r < len(s):
            window_cnt[s[r]] += 1
            window_cnt[s[l]] -= 1
            l, r = l+1, r+1
            if not +(exp_cnt-window_cnt):
                ans.append(l)
        return ans


# @lc code=end
