#
# @lc app=leetcode.cn id=33 lang=python3
# Medium
# [33] 搜索旋转排序数组
# array | binary-search

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        用二分法，先判断左右两边哪一边是有序的，再判断是否在有序的列表之内
        """
        # 复杂度 
        # 时间 O(log n)  |  空间 O(1)
        if len(nums) <= 0:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            
            # 如果中间的值大于最左边的值，说明左边有序
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # 否则右边有序
            else:
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
                    
        return left if nums[left] == target else -1
# @lc code=end

