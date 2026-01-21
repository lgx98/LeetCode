# @before-stub-for-debug-begin
from python3problem97 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
"""dp[i][j]:list[list[bool]]
if s3[:i+j] can be formed by s1[:i] and s2[:j]
dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # check the length
        if len(s1)+len(s2) != len(s3):
            return False
        dp: list[bool] = [False]*(len(s2)+1)

        # first row
        dp[0] = True  # first col
        for k in range(len(s2)):
            if s2[k] != s3[k]:
                break
            dp[k+1] = True

        # dp[i+1][j] = dp[i][j] and s1[i]==s3[i+j]
        for i in range(len(s1)):
            # first col
            dp[0] = dp[0] and (s1[i] == s3[i])
            for j in range(len(s2)):
                dp[j+1] = (dp[j+1] and (s1[i] == s3[i+j+1])
                           ) or (dp[j] and (s2[j] == s3[i+j+1]))

        return dp[-1]


# @lc code=end
