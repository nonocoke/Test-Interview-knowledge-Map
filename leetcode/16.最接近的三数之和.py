#
# @lc app=leetcode.cn id=16 lang=python3
# Medium
# [16] 最接近的三数之和
# array | two-pointers

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 复杂度
        # 时间 O(log N + n^2)  |  空间 O(log N)
        nums = sorted(nums)
        res = sum(nums[0:3])
        for i in range(len(nums)-1):
            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                elif total == target:
                    return total

                if abs(res-target) > abs(total-target):
                    res = total
        return res
# @lc code=end

