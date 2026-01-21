#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
from typing import Optional
from __future__ import annotations

class ListNode:
    val: int
    next: Optional[ListNode]

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
# @lc code=end
