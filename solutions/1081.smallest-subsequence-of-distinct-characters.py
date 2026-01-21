#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#

# @lc code=start
from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
