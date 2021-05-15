#
# @lc app=leetcode.cn id=20 lang=python3
# Easy
# [20] 有效的括号
# string | stack

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 复杂度 
        # 时间 O(n)  |  空间 O(n + table.size)
        _stack = []
        table = {'(': ')', '{': '}', '[': ']'}
        if len(s) % 2 != 0: return False
        for c in s:
            if c in table.keys():
                _stack.append(c)
            elif len(_stack) == 0:  # ')', '}', ']' 放在最左边 -> False
                return False
            elif table[_stack.pop()] != c:  # c 不匹配 table[_stack[-1]] -> False
                return False
        return len(_stack) == 0
# @lc code=end

