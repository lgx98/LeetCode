# @before-stub-for-debug-begin
from python3problem981 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
import bisect
from collections import defaultdict
from typing import Dict, List, Tuple
# @lc code=start


class TimeMap:

    time_map: Dict[str, List[Tuple[int, str]]]

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value_history = self.time_map[key]
        index = bisect.bisect(value_history, timestamp, key=lambda tup: tup[0])
        return "" if index == 0 else value_history[index-1][1]

    # Your TimeMap object will be instantiated and called as such:
    # obj = TimeMap()
    # obj.set(key,value,timestamp)
    # param_2 = obj.get(key,timestamp)
    # @lc code=end
