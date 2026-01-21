# @before-stub-for-debug-begin
from collections import deque
from python3problem752 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from typing import Generator, Deque, Set


class Solution:
    def getNeighs(self, curr: str) -> Generator[str, None, None]:
        for i in range(4):
            for num in [1, 9]:
                yield curr[:i] + str((int(curr[i])+num) % 10) + curr[i+1:]

    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000" # type: str
        if start in deadends:
            return -1
        to_visit = deque()  # type: Deque[str]
        to_visit.append(start)
        visited = set(deadends)  # type: Set[str]
        visited.add(start)
        steps = 0 # int
        while to_visit:
            size = len(to_visit)
            for i in range(size):
                curr = to_visit.popleft()
                if curr == target:
                    return steps
                for neigh in self.getNeighs(curr):
                    if neigh not in visited:
                        visited.add(neigh)
                        to_visit.append(neigh)
            steps += 1
        return -1



# @lc code=end
