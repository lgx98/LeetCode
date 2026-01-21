# @before-stub-for-debug-begin
from python3problem403 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#
from typing import List
# @lc code=start
from collections import defaultdict

class Solution:
    """
    fill table: dp[stone][next_jump]
    s
    0:  1   2   x
    1:  1   2   x
    3:  1   2   3   x
    5:  1   2   3   x
    6:  2   3   4   1x
    8:  2   3   4   1x
    12: 3   4   5x
    17: 4   5   6
    """

    def canCross(self, stones: List[int]) -> bool:
        next_steps: dict[int, set(int)]=defaultdict(set)
        next_steps[stones[0]].add(1)
        for i in range(len(stones)-1):
            if curr_steps:=next_steps[(curr_pos:=stones[i])]:
                max_reach=max(curr_steps)+curr_pos
                j=i+1
                while j<len(stones) and (dest_pos:=stones[j])<=max_reach:
                    if dest_pos-curr_pos in curr_steps:
                        next_steps[dest_pos].update(range(dest_pos-curr_pos-1,dest_pos-curr_pos+2))
                    j+=1
                del(next_steps[curr_pos])
        return bool(next_steps[stones[i+1]])




# @lc code=end
