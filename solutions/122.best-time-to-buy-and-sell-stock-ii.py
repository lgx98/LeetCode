#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    """dp[day,buy/sell]: total profit
    day     0   1   2   3   4
    price   1   2   3   4   5
    buy     -1  -1  -1  
    sell    0   1   2   
    """
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = -prices[0], 0
        for price in prices[1:]:
            buy, sell = max(buy, sell-price), max(sell, buy+price)
        return sell
        
# @lc code=end

