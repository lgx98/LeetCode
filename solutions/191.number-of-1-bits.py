# @before-stub-for-debug-begin
from python3problem191 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start


class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
# @lc code=end
