#
# @lc app=leetcode.cn id=21 lang=python3
# Easy
# [21] 合并两个有序链表
# linked-list

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 复杂度 
        # 时间 O(m + n)  |  空间 O(1)
        if l1 is None and l2 is None: return None
        if l1 is None: return l2
        if l2 is None: return l1
        pre = ListNode(-1)  # 哨兵
        cur = pre
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None: cur.next = l2
        if l2 is None: cur.next = l1
        return pre.next
# @lc code=end

