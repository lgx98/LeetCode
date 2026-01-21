# @before-stub-for-debug-begin
from python3problem86 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
from typing import Optional


class ListNode:
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
    @staticmethod
    def insert_after(pos, node):
        node.next = pos.next
        pos.next = node

    @staticmethod
    def remove_after(pos):
        removed = pos.next
        pos.next = removed.next
        return removed

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sentinel_orig = ListNode(val=0, next=head)
        sentinel_ans = ListNode(val=0)
        curr = sentinel_orig
        tail = sentinel_ans
        while curr.next:
            if curr.next.val < x:
                removed = self.remove_after(curr)
                self.insert_after(tail, removed)
                tail = tail.next
            else:
                curr = curr.next
        tail.next = sentinel_orig.next
        return sentinel_ans.next

# @lc code=end
