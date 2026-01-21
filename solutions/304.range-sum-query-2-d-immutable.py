#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List
from itertools import product


class NumMatrix:
    __pre_sum: List[List[int]]

    def __init__(self, matrix: List[List[int]]):
        print(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        self.__pre_sum = [[0]*(cols+1) for _ in range(rows+1)]
        for r, c in product(range(rows), range(cols)):
            self.__pre_sum[r+1][c+1] = self.__pre_sum[r][c+1] + \
                self.__pre_sum[r+1][c] - self.__pre_sum[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        return self.__pre_sum[row2][col2]+self.__pre_sum[row1][col1]-self.__pre_sum[row1][col2]-self.__pre_sum[row2][col1]
        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
        # @lc code=end
