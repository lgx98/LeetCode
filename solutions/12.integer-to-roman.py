#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        LUT_1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        LUT_10 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        LUT_100 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        LUT_1000 = ["", "M", "MM", "MMM"]
        d_1000, num = divmod(num, 1000)
        d_100, num = divmod(num, 100)
        d_10, d_1 = divmod(num, 10)
        return LUT_1000[d_1000] + LUT_100[d_100] + LUT_10[d_10] + LUT_1[d_1]


# @lc code=end
