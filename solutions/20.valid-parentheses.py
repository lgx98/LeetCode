#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        sk: list[str] = []
        BR_MAP = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in BR_MAP:
                if not sk or BR_MAP[c] != sk[-1]:
                    return False
                sk.pop()
            else:
                sk.append(c)
        return not len(sk)


# @lc code=end
s = Solution()
print(s.isValid("({})[]"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("()}"))
