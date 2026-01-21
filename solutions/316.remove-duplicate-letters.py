# @before-stub-for-debug-begin
from python3problem316 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start=
from typing import Counter, List


class Solution:
    def removeDuplicateLetters(self, s: str) -> List[str]:
        ctr = Counter(s)
        stack = []
        stack_set = set()
        for c in s:
            ctr[c] -= 1
            if c in stack_set:
                continue
            while stack and stack[-1] > c:
                if ctr[stack[-1]] == 0:
                    break
                stack_set.remove(stack.pop())
            stack.append(c)
            stack_set.add(c)
        return ''.join(stack)

# @lc code=end
