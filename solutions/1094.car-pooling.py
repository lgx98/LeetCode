#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#
from typing import List
# @lc code=start


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0]*1001
        for num, fr, to in trips:
            stops[fr] += num
            stops[to] -= num
        n_passenger = 0
        for stop in stops:
            n_passenger += stop
            if n_passenger > capacity:
                return False
        return True


# @lc code=end
