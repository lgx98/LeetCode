# @before-stub-for-debug-begin
from python3problem322 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    # we keep track a dp chart:
    # min_coins[amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sort the coins so we can skip some cases
        coins.sort()
        # prepare the dp table: 0 coins => 0 amount; otherwise unreached
        unreached = amount + 1
        min_coins = [unreached] * (amount + 1)
        min_coins[0] = 0
        for curr_amount in range(amount):
            # if current amount is unreachable, skip to next
            if min_coins[curr_amount] == unreached:
                continue
            for coin in coins:
                if curr_amount + coin > amount:
                    break
                else:
                    min_coins[curr_amount + coin] = min(min_coins[curr_amount] + 1, min_coins[curr_amount + coin])
        return -1 if min_coins[amount] == unreached else min_coins[amount]

# @lc code=end

