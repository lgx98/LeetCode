# @before-stub-for-debug-begin
from python3problem393 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_follow:int=0
        for ch in data:
            if n_follow:
                if (ch&0xC0)==0x80:
                    n_follow-=1
                    continue
                else:
                    return False
            if (ch&0x80)==0:
                continue
            elif (ch&0xE0)==0xC0:
                n_follow=1
            elif (ch&0xF0)==0xE0:
                n_follow=2
            elif (ch&0xF8)==0xF0:
                n_follow=3
            else:
                return False
        return False if n_follow else True

# @lc code=end

