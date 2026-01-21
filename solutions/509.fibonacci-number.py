# @before-stub-for-debug-begin
from python3problem509 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        fib_i = 0
        fib_i_1 = 1
        for i in range(n):
            temp = fib_i_1
            fib_i_1 += fib_i
            fib_i = temp
        return fib_i
        
# @lc code=end

