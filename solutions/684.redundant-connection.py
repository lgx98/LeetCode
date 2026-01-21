#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        uf = [*range(len(edges)+1)]

        def find_root(node) -> int:
            ptr = uf[node]
            while uf[ptr] != ptr:
                ptr = uf[ptr]
            uf[node] = ptr
            return ptr

        for edge in edges:
            n1, n2 = edge
            r1, r2 = find_root(n1), find_root(n2)
            if r1 == r2:
                return edge
            uf[r2] = r1
        assert False


# @lc code=end
s = Solution()
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
result = s.findRedundantConnection(edges)
print(result)