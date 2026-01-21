#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry: int = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and carry == 1:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
        if carry == 1:
            return [1, *digits]
        else:
            return digits


# @lc code=end
s=Solution()
print(s.plusOne([9,9,9,9]))
print(s.plusOne([7,8,9,9]))