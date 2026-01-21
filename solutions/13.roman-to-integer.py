#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
from itertools import pairwise


class Solution:
    def romanToInt(self, s: str) -> int:
        VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        SPECIAL_COMB_ERROR = {
            ("I", "V"): -2,
            ("I", "X"): -2,
            ("X", "L"): -20,
            ("X", "C"): -20,
            ("C", "D"): -200,
            ("C", "M"): -200,
        }
        return sum(VALUES[c] for c in s) + sum(
            SPECIAL_COMB_ERROR[pair]
            for pair in pairwise(s)
            if pair in SPECIAL_COMB_ERROR
        )


# @lc code=end
