# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, max_len = 0, 0, 0
        chars: set[str] = set()
        while r < len(s):
            char = s[r]
            r+=1
            while char in chars:
                chars.remove(s[l])
                l+=1
            chars.add(char)
            max_len = max(max_len, r-l)
        return max_len
            



# @lc code=end
