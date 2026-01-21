#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#


# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        factor_tail = []
        for i in range(2, min(32, n)):
            quo, rem = divmod(n, i)
            if quo < i:
                break
            if rem == 0:
                factors.append(i)
                if quo != i:
                    factor_tail.append(quo)
        factors += [*reversed(factor_tail), n]
        if k > len(factors):
            return -1
        else:
            return factors[k - 1]


# @lc code=end
