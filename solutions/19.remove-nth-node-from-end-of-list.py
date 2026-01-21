# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(val=0, next=head)
        first = sentinel
        for _ in range(n):
            first = first.next
        second = sentinel
        #print(f"{second.val}; {first.val}")
        while first.next:
            first = first.next
            second = second.next
        #print(f"{second.val}; {first.val}")
        second.next = second.next.next
        return sentinel.next
        
# @lc code=end

