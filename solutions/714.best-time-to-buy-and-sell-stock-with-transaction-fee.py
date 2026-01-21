#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -prices[0], 0
        for price in prices[1:]:
            buy, sell = max(buy, sell-price), max(sell, buy+price-fee)
        return sell
        
# @lc code=end

