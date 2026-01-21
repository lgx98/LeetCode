#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#


# @lc code=start
class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        uf = [*range(26)]

        def find_root(n):
            if n == uf[n]:
                return n
            r = uf[n] = find_root(uf[n])
            return r

        def find_root_char(c):
            return find_root(ord(c) - ord("a"))

        for eq in (e for e in equations if e[1] == "="):
            r0, r1 = find_root_char(eq[0]), find_root_char(eq[3])
            uf[r1] = r0

        for neq in (e for e in equations if e[1] == "!"):
            r0, r1 = find_root_char(neq[0]), find_root_char(neq[3])
            if r0 == r1:
                return False
            
        return True


# @lc code=end
s = Solution()
eqs=["c==c","b==d","x!=z"]
s.equationsPossible(eqs)