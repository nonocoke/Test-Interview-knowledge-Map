#
# @lc app=leetcode.cn id=56 lang=python3
# Medium
# [56] 合并区间
# array | sort

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 复杂度 
        # 时间 O(log N + n)  |  空间 O(log N + n)
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])  # 先按区间左边界值由小到大排序  # log N | log N
        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:
                # 如果结果集最后一个元素的右边界比新加入区间的左边界小，直接加入结果集
                res.append(inter)
            else:
                # 否则，说明新加入的和结果集最后一个区间有重合，更新区间右边界即可
                res[-1][1] = max(res[-1][1], inter[1])
        return res

# @lc code=end

