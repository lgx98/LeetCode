# @before-stub-for-debug-begin
from python3problem202 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        memo:set[int]=set()
        while n not in memo:
            memo.add(n)
            s=0
            while n:
                s+=(n%10)**2
                n=n//10
            n=s
        return 1 in memo
        
# @lc code=end

