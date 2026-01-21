#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#
from typing import List
# @lc code=start
from itertools import accumulate
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+1)
        for first, last, seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats
        diff.pop()
        return accumulate(diff)
# @lc code=end

