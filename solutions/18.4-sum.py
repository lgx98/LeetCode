#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        l, r = start, len(nums)-1
        ans: List[List[int]] = []
        while l < r:
            l_val, r_val = nums[l], nums[r]
            sum = l_val+r_val
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                ans.append([l_val, r_val])
                while l < r and nums[l] == l_val:
                    l += 1
                while l < r and nums[r] == r_val:
                    r -= 1
        return ans

    def nSum(self, n: int, nums: List[int], start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        ans: List[List[int]] = []
        if sz < n:
            return ans
        if n == 2:
            return self.twoSum(nums, start, target)
        else:
            i = start
            while i < sz:
                ans_sub = self.nSum(n-1, nums, i+1, target-nums[i])
                for each_ans in ans_sub:
                    ans.append([nums[i]]+each_ans)
                while i < sz-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
            return ans

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(4, nums, 0, target)
# @lc code=end

