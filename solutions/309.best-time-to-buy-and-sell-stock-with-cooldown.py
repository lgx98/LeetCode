#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell,cool=-float('inf'),-prices[0],0
        for price in prices:
            buy, sell, cool = max(buy, cool-price), max(sell,buy+price),max(cool, sell)
        return max(sell,cool)
# @lc code=end

