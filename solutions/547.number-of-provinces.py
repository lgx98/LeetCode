#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#


# @lc code=start
from collections.abc import Generator


class UnionFind:
    _li: list[int]

    def __init__(self, size):
        self._li = [*range(size)]

    def find_root(self, n: int) -> int:
        if self._li[n] == n:
            return n
        root = self._li[n] = self.find_root(self._li[n])
        return root

    def connect(self, n1: int, n2: int) -> int:
        r1, r2 = self.find_root(n1), self.find_root(n2)
        if r1 == r2:
            return r1
        self._li[r2] = r1
        return r1

    def get_roots(self) -> Generator[int, None, None]:
        yield from (n for i, n in enumerate(self._li) if n == i)


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(1, n):
            for j in range(i):
                if isConnected[i][j]:
                    uf.connect(j, i)
        return len([*uf.get_roots()])


# @lc code=end
s = Solution()
is_connceted = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
print(s.findCircleNum(is_connceted))

"""
[0,3,2,1]
1 0 0 1
0 1 1 0
0 1 1 1
1 0 1 1
"""
