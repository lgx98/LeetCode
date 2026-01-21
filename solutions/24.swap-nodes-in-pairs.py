#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
class ListNode:
    val: int
    next: "ListNode" | None

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
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        sentinel = ListNode(next=head)
        ptr: ListNode = sentinel
        while (n1 := ptr.next) and (n2 := n1.next):
            ptr.next = n2
            n1.next = n2.next
            n2.next = n1
            ptr = n1
        return sentinel.next


# @lc code=end
