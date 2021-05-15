#
# @lc app=leetcode.cn id=71 lang=python3
# Medium
# [71] 简化路径
# string | stack

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 复杂度 
        # 时间 O(n)  |  空间 O(dict.size)
        r = []
        for s in path.split('/'):
            # dict.get(key[, default]) 方法属性：若dict存在key，则返回dict[key]，反之返回default
            # 使用字典存储对应关系， 配合dict.get特性代替 if 判断条件
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)
        """
        # 时间 O(n)  |  空间 O(path.split('/).size)
        stack = []
        Tpath = path.split('/')
        for t in Tpath:
            if t == "..":
                if stack:
                    stack.pop()
            elif t == "." or t == "":
                pass
            else:
                stack.append(t)
        return "/" + "/".join(stack)
        """
# @lc code=end

