# @before-stub-for-debug-begin
from python3problem188 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0 or not prices:
            return 0
        elif k >= len(prices):
            buy, sell = -prices[0], 0
            for price in prices[1:]:
                buy, sell = max(buy, sell-price), max(sell, buy+price)
            return sell
        else:
            buy = [-prices[0]] + [float("-inf")] * k
            sell = [0] + [float("-inf")] * k
            for price in prices[1:]:
                buy[0] = max(buy[0], sell[0] - price)
                for j in range(1, k + 1):
                    buy[j] = max(buy[j], sell[j] - price)
                    sell[j] = max(sell[j], buy[j - 1] + price)
            return max(sell)

# @lc code=end

