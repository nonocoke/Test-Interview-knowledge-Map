#
# @lc app=leetcode.cn id=26 lang=python3
# Easy
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 复杂度 
        # 时间 O(n)  |  空间 O(1)
        if len(nums) == 0: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
# @lc code=end

