# @before-stub-for-debug-begin
from python3problem204 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrime = [True]*(n)
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
                for j in range(i*2, n, i):
                    isPrime[j] = False
        return count
# @lc code=end
