# @before-stub-for-debug-begin
from python3problem72 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_tmp: list[int] = [None]*(len(word1)+1)
        dp: list[int] = list(range(len(word1)+1))
        for j in range(1, len(word2)+1):
            dp_tmp[0] = j
            for i in range(1, len(word1)+1):
                dp_tmp[i] = min(dp[i]+1, dp_tmp[i-1]+1, dp[i-1] +
                                (0 if word1[i-1] == word2[j-1] else 1))
            dp, dp_tmp = dp_tmp, dp
        return dp[len(word1)]


""" dp chart: chart[i][j] represents min steps to match word1[0:i] and word[0:j]
consider filling chart[x][y]:
choices:
    a) insert/repalce: min(chart[x-1][y],chart[x][y-1])+1
    b) replace/match: chart[x-1][y-1] + (1 if word1[x-1]==word[y-1] else 1)
base case:
chart[0][j]=j
chart[i][0]=i

"""
# @lc code=end
