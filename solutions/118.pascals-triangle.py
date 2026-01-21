# @before-stub-for-debug-begin
from python3problem118 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
import operator as op
from itertools import pairwise, chain, starmap
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[1]] if (numRows == 1) or not (a:=self.generate(numRows-1)) or a.append(list(chain([1],starmap(op.add,pairwise(a[-1])),[1]))) else a
    
    # def generate(self, numRows: int) -> List[List[int]]:
    #     if numRows == 1:
    #         # Base case
    #         return [[1]]
    #     else:
    #         # Derive from the case of numRows-1, we will use numRows=5 for example
    #         a = self.generate(numRows-1) # [[1],[1,1],[1,2,1],[1,3,3,1]]
    #         last_row = a[-1] # [1,3,3,1]
    #         g0 = pairwise(last_row) # (1,3),(3,3),(3,1)
    #         g1 = starmap(op.add,g0) # add(1,3), add(3,3), add(3,1) => 4,6,4
    #         g2 = chain([1],g1,[1]) # 1,4,6,4,1
    #         new_last_row = list(g2) # [1,4,6,4,1]
    #         a.append(new_last_row) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    #         return a

# @lc code=end

