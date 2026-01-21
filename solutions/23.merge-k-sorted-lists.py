# @before-stub-for-debug-begin
from python3problem23 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import Optional, List
import heapq


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # monkey patch
        ListNode.__lt__ = lambda self, other: self.val < other.val
        # populate the heap
        h = []
        [heapq.heappush(h, i) for i in lists if i]

        sentinel = ListNode()
        tail = sentinel
        while h:
            curr = h[0]
            if curr.next:
                heapq.heapreplace(h, curr.next)
            else:
                heapq.heappop(h)
            tail.next = curr
            tail = curr
        return sentinel.next

# @lc code=end
