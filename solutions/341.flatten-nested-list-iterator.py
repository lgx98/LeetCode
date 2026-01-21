# @before-stub-for-debug-begin
from python3problem341 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

from typing import List, Generator

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    __curr_int: int | None
    __iterator: Generator[int, None, None]

    def __init__(self, nestedList: List[NestedInteger]):
        self.__curr_int = None
        self.__iterator = self.__nested_iter_gen(nestedList)
        try:
            self.__curr_int = next(self.__iterator)
        except:
            pass

    def __nested_iter_gen(self, nestedList: List[NestedInteger]) -> Generator[int, None, None]:
        for elem in nestedList:
            if elem.isInteger():
                yield elem.getInteger()
            else:
                yield from self.__nested_iter_gen(elem.getList())

    def next(self) -> int:
        retval = self.__curr_int
        try:
            self.__curr_int = next(self.__iterator)
        except:
            self.__curr_int = None
        return retval

    def hasNext(self) -> bool:
        return self.__curr_int is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
