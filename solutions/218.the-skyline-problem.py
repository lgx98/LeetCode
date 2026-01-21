# @before-stub-for-debug-begin
from python3problem218 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
from typing import List
# @lc code=start
from itertools import chain
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        last_nH, b_heap, ans = 0, [(0, 1 << 32)], []
        for L, nH, R in sorted(chain(((L, -H, R) for L, R, H in buildings), ((R, 0, 0) for _, R, _ in buildings))):
            while L >= b_heap[0][1]:
                heapq.heappop(b_heap)
            if nH:
                heapq.heappush(b_heap, (nH, R))
            curr_nH = b_heap[0][0]
            if curr_nH != last_nH:
                last_nH = curr_nH
                ans.append([L, -curr_nH])
        return ans

# @lc code=end
