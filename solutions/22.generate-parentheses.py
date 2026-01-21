# @before-stub-for-debug-begin
from python3problem22 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# @lc code=start
from itertools import product, chain
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return None if setattr(self, 'a', [['']]) or deque((self.a.append(list(chain(*(('('+s0+')'+s1 for (s0, s1) in product(self.a[j], self.a[i-j])) for j in range(i+1))))) for i in range(n)), maxlen=0) else self.a[-1]


# @lc code=end
