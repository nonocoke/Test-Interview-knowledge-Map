#
# @lc app=leetcode.cn id=215 lang=python3
# Medium
# [215] 数组中的第K个最大元素
# divide-and-conquer | heap

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1
        # 复杂度
        # 时间: O(n)，原版快排是O(nlogn)，而这里只需要在一个分支递归，因此降为O(n)
        # 空间: O(logn)，递归栈
        """
        快速排序核心思路就在于双指针 + 分治

        1. 先随机选择一个中间值pivot作为比较的基准base，因为求的是topK，因此比这个基准大的放到左边，比这个基准小的放到右边
        2. 把选择的基准放到最左边，也就是nums[low]和nums[pivot]交换位置
           [#] 可以把nums[low]理解为空位置
        3. 慢指针 i 从low位置开始，指向比基准大的数字；快指针 j 从low + 1位置开始遍历
        4. j <= high进入循环
            4.1 如果nums[j]比基准大，nums[i + 1]和nums[j]交换位置，并且i + 1
            4.2 j每次循环 + 1
        5. 循环结束后，当前 i 指针所在位置即为数组中比base大的最后一个位置，将其和最左边的base交换位置，也就是交换nums[low]和nums[i]；
        交换完后，i位置之前的都是比它大的，i位置之后的都是比它小的
        6. 然后是分治部分
            6.1 如果当前i就是第k个元素，也就是i == k - 1，找到topK，返回nums[i]
            6.2 如果当前i > k - 1，i偏大，要在[low, i - 1]区间内继续寻找
            6.3 如果当前i < k - 1，i偏小，要在[i + 1, high]区间内继续寻找
        """
        import random
        def findTopKth(low, high):
            pivot = random.randint(low, high)
            nums[low], nums[pivot] = nums[pivot], nums[low]
            base = nums[low]
            i = low
            j = low + 1
            while j <= high:
                if nums[j] > base:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[low], nums[i] = nums[i], nums[low]
            if i == k - 1:
                return nums[i]
            elif i > k - 1:
                return findTopKth(low, i - 1)
            else:
                return findTopKth(i + 1, high)
        return findTopKth(0, len(nums) - 1)

        """
        # 2
        import heapq
        return heapq.nlargest(k, nums)[-1]
        # 3
        nums.sort()
        return nums[-k]
        """

# @lc code=end

