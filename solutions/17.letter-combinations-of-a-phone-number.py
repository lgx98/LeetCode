#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return [] 
        LETTER_LUT = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        return [
            "".join(c_tuple) for c_tuple in product(*(LETTER_LUT[c] for c in digits))
        ]


# @lc code=end