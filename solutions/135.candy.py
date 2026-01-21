#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
from itertools import pairwise
from collections import deque
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ret,inc,dec,pre=1,1,0,1
        deque(((dec:=0,pre:=1 if y==x else(pre+1),ret:=ret+pre,inc:=pre)if y>=x else(dec:=dec+1,dec:=(dec+1)if dec==inc else dec,ret:=ret+dec,pre:=1)for(x,y)in pairwise(ratings)),maxlen=0)
        return ret
# @lc code=end

