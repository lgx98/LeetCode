# @before-stub-for-debug-begin
from python3problem151 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start


class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join([*filter(lambda x:bool(x),s.split(' '))][::-1])
        return ' '.join(reversed([*filter(lambda x:bool(x),s.split(' '))]))

# @lc code=end
