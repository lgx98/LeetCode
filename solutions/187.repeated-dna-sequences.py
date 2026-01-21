# @before-stub-for-debug-begin
from python3problem187 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # char  A   C   G   T
        # hex   41  43  47  54
        # this only works on C++
        # if len(s) <= 10:
        #     return []
        # hash = 0
        # for i in range(10):
        #     hash = (hash << 3) + (ord(s[i]) & 7)
        # known = Counter([hash])
        # ans=[]
        # for i in range(10, len(s)):
        #     hash = ((hash & 0x7FFFFFF) << 3) + (ord(s[i]) & 7)
        #     known[hash]+=1
        #     if known[hash]==2:
        #         ans.append(s[i-9:i+1])
        # return ans
        return [k for k, v in Counter(s[i:i+10] for i in range(len(s)-9)).items() if v > 1]


# @lc code=end
