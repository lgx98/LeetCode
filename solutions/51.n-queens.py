# @before-stub-for-debug-begin
from python3problem51 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List, Generator
# @lc code=start


class Solution:
    class Board:
        n: int  # n queens on n*n board
        queens: List[int] = []  # the col of each queen, starting from row 0
        used_cols: int = 0  # bitset for used cols
        used_diag_l: int = 0  # bitset for used (col + row)
        used_diag_r: int = 0  # bitset for used (col - row + n - 1)
        row_strs: List[str]  # pre-computed rows representing rows in answer
        """
        queens:     [1, 3]
                       6 5 4 3 2 1 0
        used_cols:  0b      [1 0 1 0]
        used_diag_l:0b 0[0 1 0 0]1 0
        used_diag_r:0b 0 1[1 0 0 0]0
         3 4 5 6
          \ \ \ \
         2 \0\1\2\3
          \0.|Q|.|.
         1 \-+-+-+-
          \1.|.|.|Q
         0 \-+-+-+-
          \2?|.|.|.
           \-+-+-+-
           3.|.|?|.
        """

        def __init__(self, n: int) -> None:
            self.n = n
            self.row_strs = ['.'*i+'Q'+'.'*(n-i-1) for i in range(n)]

        def solved(self) -> bool:
            return len(self.queens) == self.n

        def add_queen(self, col: int) -> None:
            row = len(self.queens)
            self.queens.append(col)
            self.used_cols |= (1 << col)
            self.used_diag_l |= (1 << (col+row))
            self.used_diag_r |= (1 << (col-row+self.n-1))

        def del_queen(self, col: int) -> int:
            self.queens.pop()
            row = len(self.queens)
            self.used_cols &= ~(1 << col)
            self.used_diag_l &= ~(1 << (col+row))
            self.used_diag_r &= ~(1 << (col-row+self.n-1))

        def get_avail_rows(self) -> Generator[int, None, None]:
            row = len(self.queens)
            used_bitset = self.used_cols | (self.used_diag_l >> (row)) | (
                self.used_diag_r >> (self.n-row-1))
            for i in range(self.n):
                used_bit = used_bitset & 1
                used_bitset >>= 1
                if not used_bit:
                    yield i

        def to_str(self) -> List[str]:
            return [self.row_strs[col] for col in self.queens]

    def helper(self, b: Board, ans: List[List[str]]):
        if b.solved():
            ans.append(b.to_str())
            return
        for Q_row in b.get_avail_rows():
            b.add_queen(Q_row)
            self.helper(b, ans)
            b.del_queen(Q_row)

    def solveNQueens(self, n: int) -> List[List[str]]:
        b = self.Board(n)
        ans = []
        self.helper(b, ans)
        return ans

        # @lc code=end
