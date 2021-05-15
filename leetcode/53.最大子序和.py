#
# @lc app=leetcode.cn id=53 lang=python3
# Easy
# [53] 最大子序和
# array | divide-and-conquer | dynamic-programming

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 贪心
        # 复杂度 
        # 时间 O(log n)  |  空间 O(1)
        res = nums[0]
        cur_max = 0
        length = len(nums)
        if length == 1: return res
        for i in range(length):
            if cur_max > 0:
                cur_max += nums[i]
            else:
                cur_max = nums[i]
            res = max(res, cur_max) 
        return res
# @lc code=end

