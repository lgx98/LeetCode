#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        pre,cur=None,slow
        while cur!=None:
            nxt= cur.next
            cur.next=pre
            pre=cur
            cur=nxt

        while pre!=None:
            if pre.val!=head.val:
                return False
            pre=pre.next
            head=head.next
        return True
# @lc code=end

