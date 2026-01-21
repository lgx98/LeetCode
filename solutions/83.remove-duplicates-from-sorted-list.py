#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
from typing import Optional
from unittest.mock import sentinel


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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel=ListNode(101,head)
        curr= sentinel
        while curr.next:
            if curr.val == curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return sentinel.next
        # @lc code=end
