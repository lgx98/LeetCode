# @before-stub-for-debug-begin
from python3problem295 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
import heapq
# @lc code=start


class MedianFinder:
    """
    len(minheap)==lem(maxheap)
    or
    len(minheap)==lem(maxheap)+1
    """
    minheap: list[int]  # stores large half
    maxheap: list[int]  # stores small half

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            self.minheap.append(num)
            return
        if len(self.minheap) > len(self.maxheap):
            if num <= self.minheap[0]:
                heapq.heappush(self.maxheap, -num)
            else:
                evicted: int = heapq.heapreplace(self.minheap, num)
                heapq.heappush(self.maxheap, -evicted)
        else:
            if num >= -self.maxheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                evicted: int = -heapq.heapreplace(self.maxheap, -num)
                heapq.heappush(self.minheap, evicted)
        #print(f"{self.minheap},{self.maxheap}")

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0]-self.maxheap[0])/2
        else:
            return self.minheap[0]
"""
["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]\n[[],[40],[],[12],[],[16],[],[14],[],[35],[],[19],[],[34],[],[35],[],[28],[],[35],[],[26],[],[6],[],[8],[],[2],[],[14],[],[25],[],[25],[],[4],[],[33],[],[18],[],[10],[],[14],[],[27],[],[3],[],[35],[],[13],[],[24],[],[27],[],[14],[],[5],[],[0],[],[38],[],[19],[],[25],[],[11],[],[14],[],[31],[],[30],[],[11],[],[31],[],[0],[]]

"""
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
