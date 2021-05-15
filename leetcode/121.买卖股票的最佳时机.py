#
# @lc app=leetcode.cn id=121 lang=python3
# Easy
# [121] 买卖股票的最佳时机
# array | dynamic-programming

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 复杂度 
        # 时间 O(n)  |  空间 O(1)
        import sys
        minprice, maxprofit = sys.maxsize, 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

# @lc code=end

