#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
from typing import List, Counter
# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        ans: List[int] = []
        exp_cnt: Counter[str] = Counter(s1)
        window_cnt: Counter[str] = Counter(s2[:len(s1)])
        l, r = 0, len(s1)
        if not +(exp_cnt-window_cnt):
            return True
        while r < len(s2):
            window_cnt[s2[r]] += 1
            window_cnt[s2[l]] -= 1
            l, r = l+1, r+1
            if not +(exp_cnt-window_cnt):
                return True
        return False
# @lc code=end
