#
# @lc app=leetcode.cn id=206 lang=python3
# Easy
# [206] 反转链表
# linked-list

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 复杂度 
        # 时间 O(n)  |  空间 O(n)
        real_head = None
        while head != None:
            tmp = head.next
            head.next = real_head
            real_head = head
            head = tmp
        return real_head
# @lc code=end

