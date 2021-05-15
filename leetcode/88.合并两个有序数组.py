#
# @lc app=leetcode.cn id=88 lang=python3
# Easy
# [88] 合并两个有序数组
# array | two-pointers

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 复杂度
        """
        # 时间 O((m+n)log(m+n))  |  空间 O(log(m+n))
        nums1[m:] = nums2
        nums1.sort()
        """
        # 逆向双指针
        # O(m+n)  |  O(1)
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


# @lc code=end

