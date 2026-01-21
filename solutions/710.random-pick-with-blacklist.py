#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#

# @lc code=start
from random import choice, randrange, seed
from typing import Dict, List


class Solution:
    __n_white: int
    __mapping: Dict[int, int]
    __whitelist: List[int]

    def __init__(self, n: int, blacklist: List[int]):
        blackset = set(blacklist)
        if n <= 1e5:
            self.__whitelist = [x for x in range(n) if x not in blackset]
        else:
            self.__whitelist = None
            self.__n_white = n-len(blacklist)
            k = (x for x in blacklist if x < self.__n_white)
            v = (x for x in range(self.__n_white, n) if x not in blackset)
            self.__mapping = dict(zip(k, v))
        # seed()

    def pick(self) -> int:
        if self.__whitelist:
            return choice(self.__whitelist)
        else:
            num = randrange(self.__n_white)
            return self.__mapping[num] if num in self.__mapping.keys() else num

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(n, blacklist)
        # param_1 = obj.pick()
        # @lc code=end
