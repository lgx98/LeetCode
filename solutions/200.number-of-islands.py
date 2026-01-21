# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
from collections import deque


class Solution:
    def dfs(self, grid: List[List[str]], r: int, c: int):
        grid[r][c] = "0"
        deque((self.dfs(grid, r+dr, c+dc) for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] if 0 <= r+dr < len(grid)
              and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == "1"), maxlen=0)

    def numIslands(self, grid: List[List[str]]) -> int:
        return sum(1 for _ in (self.dfs(grid, r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == "1"))


# @lc code=end
