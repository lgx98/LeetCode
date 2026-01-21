# @before-stub-for-debug-begin
from python3problem707 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start


class ListNode:
    val: int
    prev: "ListNode"
    next: "ListNode"


class MyLinkedList:

    _sentinel: ListNode
    _length: int = 0

    def __init__(self):
        node = ListNode()
        node.prev, node.next = node, node
        self._sentinel = node

    def _getNodeAt(self, index: int) -> ListNode:
        """Get the indexth node; return sentinel if index == -1"""
        # TODO: optimisation: go backwards if that's shorter
        ptr: ListNode = self._sentinel
        for _ in range(index + 1):
            ptr = ptr.next
        return ptr

    def get(self, index: int) -> int:
        if not (0 <= index < self._length):
            return -1
        return self._getNodeAt(index).val

    def _addBetween(
        self, val: int, node_before: ListNode, node_after: ListNode
    ) -> None:
        """make a new node with val and add it between two neighboring nodes"""
        new = ListNode()
        new.val, new.prev, new.next = val, node_before, node_after
        node_before.next, node_after.prev = new, new
        self._length += 1

    def addAtHead(self, val: int) -> None:
        self._addBetween(val, self._sentinel, self._sentinel.next)

    def addAtTail(self, val: int) -> None:
        self._addBetween(val, self._sentinel.prev, self._sentinel)

    def addAtIndex(self, index: int, val: int) -> None:
        if not (0 <= index <= self._length):
            return
        n_before = self._getNodeAt(index - 1)
        self._addBetween(val, n_before, n_before.next)

    def deleteAtIndex(self, index: int) -> None:
        if not (0 <= index < self._length):
            return
        node = self._getNodeAt(index)
        node.prev.next, node.next.prev = node.next, node.prev
        self._length -= 1
        del node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
