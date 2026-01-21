#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#


# @lc code=start
class Solution:
    def _partition(self, nums: list[int], lo: int, hi: int) -> int:
        pivot = nums[lo]
        while lo < hi:
            while (lo < hi) and (pivot <= nums[hi]):
                hi -= 1
            nums[lo] = nums[hi]
            while (lo < hi) and (pivot >= nums[lo]):
                lo += 1
            nums[hi] = nums[lo]
        nums[lo] = pivot
        return lo

    def _quicksort(self, nums: list[int], first: int, last: int) -> None:
        if first >= last:
            return
        i_pivot = self._partition(nums, first, last)
        self._quicksort(nums, first, i_pivot - 1)
        self._quicksort(nums, i_pivot + 1, last)
        return

    def sortArray(self, nums: list[int]) -> list[int]:
        #self._quicksort(nums, 0, len(nums) - 1)
        return sorted(nums)


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.sortArray([5, 1, 1, 2, 0, 0])
