# @before-stub-for-debug-begin
from python3problem391 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=391 lang=python3
#
# [391] Perfect Rectangle
#
from typing import List
from collections import defaultdict
# @lc code=start


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        bmap: dict[int, int] = defaultdict(int)
        """bitmask:
        1---2
        |   |
        4---8
        """
        left, bottom, right, top = rectangles[0]
        for (l, b, r, t) in rectangles:
            tl, tr, bl, br = (t << 16)+l, (t << 16)+r, (b << 16)+l, (b << 16)+r
            if (bmap[tl] & 1) or (bmap[tr] & 2) or (bmap[bl] & 4) or (bmap[br] & 8):
                return False
            bmap[tl] |= 1
            bmap[tr] |= 2
            bmap[bl] |= 4
            bmap[br] |= 8
            left, bottom, right, top = min(left, l), min(
                bottom, b), max(right, r), max(top, t)
        for pt, bits in bmap.items():
            if bits in {6, 9, 7, 11, 13, 14}:
                return False
            if (bits == 1 and pt != (top << 16)+left) or (bits == 2 and pt != (top << 16)+right) or (bits == 4 and pt != (bottom << 16)+left) or (bits == 8 and pt != (bottom << 16)+right):
                return False
        return True
        # @lc code=end
