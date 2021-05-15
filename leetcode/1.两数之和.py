# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
# Easy
# [1] 两数之和
# array | hash-table

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 复杂度 
        # 时间 O(n)  |  空间 O(n)
        _hash = {}  # 哈希
        for idx, num in enumerate(nums):
            if target - num in _hash.keys():
                return [_hash[target - num], idx]
            else:
                _hash[nums[idx]] = idx
        return []
        # 暴力匹配
        # 复杂度 
        # 时间 O(n^2)  |  空间 O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        """

# @lc code=end

