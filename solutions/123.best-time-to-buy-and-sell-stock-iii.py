# @before-stub-for-debug-begin
from python3problem123 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    """
    day     0   1   2   3   4   5   6   7
    prices  3   3   5   0   0   3   1   4
    sell0   0   0   0   0   0   0   0   0
    buy1    -3  -3  -3  0   0   0   0   0
    sell1       0   2   2   2   3   3   4
    buy2            -5  2   2   2   2   2
    sell2               -5  2   5   5   6
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for price in prices[1:]:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
        
# @lc code=end

