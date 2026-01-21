# @before-stub-for-debug-begin
from python3problem77 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List
import copy
# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans: List[List[int]] = []

        def dfs(start: int = 1, path: List[int] = []) -> None:
            nonlocal ans
            if len(path) == k:
                ans.append(copy.deepcopy(path))
                return
            for i in range(start, n - k + len(path) + 2):
                path.append(i)
                dfs(i+1, path)
                path.pop()

        dfs(1, [])
        return ans

# @lc code=end
