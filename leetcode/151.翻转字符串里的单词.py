#
# @lc app=leetcode.cn id=151 lang=python3
# Medium
# [151] 翻转字符串里的单词
# string

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 复杂度 
        # 时间 O(n)  |  空间 O(n)
        return ' '.join(s.strip().split()[::-1])
# @lc code=end

