# @before-stub-for-debug-begin
from python3problem139 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok=[True]
        lens=set(len(word) for word in wordDict)
        words=set(wordDict)
        for i in range(1,len(s)+1):
            ok+=any((ok[i-l] and (s[i-l:i] in words)) for l in lens if l<=i),
        return ok[len(s)+1]
# @lc code=end

