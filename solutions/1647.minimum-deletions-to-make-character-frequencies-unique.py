#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        nums = sorted(Counter(s).values(),reverse=True)
        level, ans=nums[0],0
        for num in nums:
            if num<=level:
                level=num-1
            else:
                ans+=num-level
                level=max(level-1,0)
        return ans


# @lc code=end

