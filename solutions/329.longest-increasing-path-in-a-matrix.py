# @before-stub-for-debug-begin
from python3problem329 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
from typing import List
# @lc code=start

#[[1,2]]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[None]*len(matrix[0]) for _ in range(len(matrix))]
        def dfs(memo: List[List[int]], r: int, c: int):
            memo[r][c] = max((memo[nr][nc] if memo[nr][nc] else dfs(memo, nr, nc) for nr, nc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)] if (0 <= nr < len(matrix)) and (0 <= nc < len(matrix[0])) and (matrix[nr][nc] < matrix[r][c])), default=0)+1
            return memo[r][c]
        return max(memo[r][c] if memo[r][c] else dfs(memo, r, c) for c in range(len(matrix[0])) for r in range(len(matrix)))


# @lc code=end
