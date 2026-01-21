# @before-stub-for-debug-begin
from python3problem121 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    """dp[day,buy/sell]: total profit
    day     0   1   2   3   4   5
    price   7   1   5   3   6   4
    dp[0]   -7  -1  -1  -1  -1  -1
    dp[1]   Nan -6  4   4   5   5
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_buy, max_profit_sell= -10001,-10001
        for price in prices:
            max_profit_buy,max_profit_sell = max(max_profit_buy, -price),max(max_profit_sell, price+max_profit_buy)
        return max(max_profit_sell,0)
        
# @lc code=end

