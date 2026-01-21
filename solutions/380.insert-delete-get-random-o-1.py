# @before-stub-for-debug-begin
from python3problem380 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from random import choice, seed
from typing import Dict, List

"""
["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]\n[[],[0],[0],[0],[],[0],[0]]
"""

class RandomizedSet:
    _map: Dict[int, int] = {}  # from value to arr index
    _arr: List[int] = []  # holds value

    def __init__(self):
        self._map={}
        self._arr=[]
        seed()

    def insert(self, val: int) -> bool:
        if val in self._map.keys():
            return False
        else:
            i = len(self._arr)
            self._map[val] = i
            self._arr.append(val)
            # print(f"insert {val} @ {i}")
            # print(self._arr)
            # print(self._map)
            return True

    def remove(self, val: int) -> bool:
        if val not in self._map.keys():
            return False
        else:
            last_val = self._arr[-1]
            i = self._map[val]
            self._arr[i] = last_val
            self._map[last_val] = i
            self._arr.pop()
            self._map.pop(val)
            # print(f"remove {val} @ {i}; fill in {last_val}")
            # print(self._arr)
            # print(self._map)
            return True

    def getRandom(self) -> int:
        return choice(self._arr)

        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()
        # @lc code=end
