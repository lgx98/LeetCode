#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class DLLNode:
    key: int
    val: int
    pr: 'DLLNode'
    nx: 'DLLNode'

    def __init__(self, key: int = 0, val: int = 0, pr=None, nx=None) -> None:
        self.key, self.val, self.pr, self.nx = key, val, pr, nx

    @staticmethod
    def remove(n: 'DLLNode') -> 'DLLNode':
        n.nx.pr, n.pr.nx = n.pr, n.nx
        return n

    @staticmethod
    def insert_after(n: 'DLLNode', pos: 'DLLNode') -> None:
        n.pr, n.nx = pos, pos.nx
        pos.nx.pr = n
        pos.nx = n


class LRUCache:
    __stnl: DLLNode
    __map: dict[int, DLLNode]
    __capacity: int

    def __init__(self, capacity: int):
        self.__stnl = DLLNode()
        self.__stnl.pr, self.__stnl.nx = self.__stnl, self.__stnl
        self.__map = dict()
        self.__capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.__map.keys():
            return -1
        n = self.__map[key]
        DLLNode.insert_after(DLLNode.remove(n), self.__stnl)
        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.__map.keys():
            n = self.__map[key]
            DLLNode.insert_after(DLLNode.remove(n), self.__stnl)
            n.val = value
        else:
            if len(self.__map) == self.__capacity:
                n = DLLNode.remove(self.__stnl.pr)
                del(self.__map[n.key])
            n = DLLNode(key, value)
            DLLNode.insert_after(n, self.__stnl)
            self.__map[key] = n

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        # @lc code=end
