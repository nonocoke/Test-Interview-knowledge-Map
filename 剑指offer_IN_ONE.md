# 剑指 Offer

## 面试指南

～

## 部分算法题

* [A 数据结构](#A)
* [B 动态规划](#B)
* [C 搜索与回溯算法](#C)
* [D 分治算法](#D)
* [E 排序](#E)
* [F 查找](#F)
* [G 双指针](#G)
* [H 位运算](#H)
* [I 数学](#I)
* [J 模拟](#J)

### <span id = "A">A 数据结构</span>

```python3
# Definition for singly-linked list.
class Node:
    def __init__(self, data: int, next=None):
        self.val = data
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data: int, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right
```

#### 05 替换空格

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

输入：s = "We are happy."    输出："We%20are%20happy."

```python3
# 分析
# 1. 内置函数replace
# 2. 遍历添加，申请一个list，然后遍历添加
# 3. 原地修改 (python中字符串不可更改，故此法无效)

def replaceSpace_1(s):
    return s.replace(' ', '%20')


def replaceSpace_2(s):
    res = []
    for c in s:
        if c == ' ':
            res.append('%20')
        else:
            res.append(c)
    return "".join(res)
```

#### 06 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）

```python3
# 辅助栈

def reversePrint(head: Node):
    _stack = []
    while head:
        _stack.append(head.val)
        head = head.next
    return _stack[::-1]
```

#### 24 反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点

输入: 1->2->3->4->5->NULL  输出: 5->4->3->2->1->NULL

```python3
# 分析
# 1. 迭代(双指针)
# 2. 递归

# O(N)  O(1)
def reversedList(head: Node) -> Node:
    r_head = None
    while head:
        tmp = head.next
        head.next = r_head
        r_head = head
        head = tmp
    return r_head

# O(N)  O(N)
def recurReversedList(head: Node) -> Node:
    def recur(cur, pre):
        if not cur:
            return pre
        # 递归后继节点
        res = recur(cur.next, pre)
        # 修改节点引用方向
        cur.next = pre
        return res
    return recur(head, None)
```

#### 30 包含 min 函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)

```python3
# 普通栈的 push() 和 pop() 函数的复杂度为 O(1) ；而获取栈最小值 min() 函数需要遍历整个栈，复杂度为 O(N)
# --> 将 min() 函数复杂度降为 O(1)。可借助辅助栈实现

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

class MinStack:

    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        # 这里出栈，出的是最小值，则两个栈同时弹出；反之，只弹出A；故不影响获取 min
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
```

#### 09 用两个栈实现队列

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

```python3
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        # 将栈 A 元素全部转移至栈 B 中，实现元素倒序，并返回栈 B 的栈顶元素
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
```

#### 59_2 队列的最大值

定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

```python3
# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

import queue

class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.stack = []

    def max_value(self) -> int:
        return self.stack[0] if self.stack else -1

    # 保证辅助队列单调递减
    def push_back(self, value: int) -> None:
        self.queue.put(value)
        # 删除 stack 内所有 < value 的元素，以保持 队列弹出最大值后，stack[0]存的是剩下的最大值
        while self.stack and self.stack[-1] < value:
            self.stack.pop()
        self.stack.append(value)

    def pop_front(self) -> int:
        if not self.stack: return -1
        res = self.queue.get()
        if res == self.stack[0]:
            self.stack.pop()
        return res
```

#### 58 左旋转字符串

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"

输入: s = "lrloseumgh", k = 6   输出: "umghlrlose"

```python3
# 分析
# 1. 字符串切片
# 2. 若面试规定不允许使用 切片函数 ，则使用列表遍历拼接，join拼接字符串
# 3. 旋转后的字符串肯定在strstr里，直接拿取strstr[n:len()+n]

class Solution:

    def reverseLeftWords(self, s: str, n: int) -> str:
        if n >= len(s):
            return s
        return s[n:] + s[:n]

    def reverseLeftWords_2(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)

    def reverseLeftWords_3(self, s: str, n: int) -> str:
        if n >= len(s):
            return s
        tmp = s + s
        return tmp[n:n + len(n)]
```

#### 59 滑动窗口的最大值

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

输入: nums = [1,3,-1,-3,5], 和 k = 3
输出: [3,3,5] 

```python3
"""
  滑动窗口的位置          最大值
---------------         -----
[1  3  -1] -3  5        3
 1 [3  -1  -3] 5        3
 1  3 [-1  -3  5]       5
"""

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        res = []
        _deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            # 删除 _deque 内所有 < nums[i] 的元素，以保持 _deque 递减，存的是滑动区间的最大值
            while _deque and _deque[-1] < nums[i]:
                _deque.pop()
            _deque.append(nums[i])
        # 形成窗口后
        for i in range(k, len(nums)):
            # 删除窗口外元素
            if _deuqe[0] == nums[i-k]:
                _deuqe.popleft()
            while _deque and _deque[-1] < nums[i]:
                _deque.pop()
            _deque.append(nums[i])
            res.append(deque[0])
        return res
```

#### 67 把字符串转换成整数

写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数

```python3
# 正则
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        num_re = re.compile(r'^[\+\-]?\d+')  # 设置正则规则
        num = num_re.findall(str.lstrip())
        num = int(*num)  # 由于返回的是个列表，解包并且转换成整数
        return max(min(num, INT_MAX), INT_MIN)
```

### <span id = "B">B 动态规划</span>

#### 10_2 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法

```python3
# 1. 迭代, python 特性
# 2. 递归 O(2^n)
# 3. dp

def climbStairs(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def climbStairs_recur(n):
    if n == 1: return 1
    if n == 2: return 2
    return climbStairs_recur(n - 1) + climbStairs_recur(n - 2)

dp = {}
def climbStairs2(n)
    if n == 1: return 1
    if n == 2: return 2
    # 优化递归，存储每一步的值，降低时间复杂度到 O(N)
    if n in dp.keys():
        return dp[n]
    ans = climbStairs2(n - 1) + climbStairs2(n - 2)
    dp[n] = res
    return res
```

#### 19 正则表达式匹配 -

请实现一个函数用来匹配包含'. '和'*'的正则表达式

    字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）

```python3
"""
s = "aaa"
p = "ab*.*"

      a  b  *  .  *
   1  0  0  0  0  0
a  0  1  0  1  0  1
a  0  0  0  0  1  1
a  0  0  0  0  0  1

True


dp[i][j] 代表字符串 s 的前 i 个字符和 p 的前 j 个字符能否匹配 (字符是 s[i - 1] 和 p[j - 1])
当 p[j - 1] = '*' 时， dp[i][j] 在当以下任一情况为 true 时等于 true: 
    dp[i][j - 2]: 即将字符组合 p[j - 2] * 看作出现 0 次时，能否匹配；
    dp[i - 1][j] 且 s[i - 1] = p[j - 2]: 即让字符 p[j - 2] 多出现 1 次时，能否匹配
    dp[i - 1][j] 且 p[j - 2] = '.': 即让字符 '.' 多出现 1 次时，能否匹配
当 p[j - 1] != '*' 时， dp[i][j] 在当以下任一情况为 true 时等于 true: 
    dp[i - 1][j - 1] 且 s[i - 1] = p[j - 1]: 即让字符 p[j - 1] 多出现一次时，能否匹配
    dp[i - 1][j - 1] 且 p[j - 1] = '.': 即将字符 . 看作字符 s[i - 1] 时，能否匹配

"""
class Solution:
    # O(MN)  |  O(MN)
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        # dp[i][j] 代表字符串 s 的前 i 个字符和 p 的前 j 个字符能否匹配
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True  # 两个空字符串能够匹配

        # 初始化首行
        # 首行 s 为空字符串，因此当 p 的偶数位为 * 时才能够匹配（即让 p 的奇数位出现 0 次，保持 p 是空字符串）
        # 因此，循环遍历字符串 p ，步长为 2（即只看偶数位）
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'

        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and s[i-1] == p[j-2]) or (dp[i-1][j] and p[j-2] = '.')
                else:
                    dp[i][j] = dp[i-1][j-1] or (p[j-1] ==  s[i-1] or p[j-1] = '.')
        return dp[-1][-1]
```

#### 42 连续子数组的最大和

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)

```python3
"""
dp[0] = nums[0]
         / dp[i-1] + nums[i]  (dp[i-1] > 0)
dp[i] = 
         \ nums[i]            (dp[i-1] <= 0)
"""

class Solution:
    # 时间复杂度 O(N): 线性遍历数组 nums 即可获得结果，使用 O(N) 时间。
    # 空间复杂度 O(1): 使用常数大小的额外空间

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
```

#### 48 最长不含重复字符的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3

```python3
"""
# 双指针 + 哈希表

· 更新左指针 i : 根据上轮左指针 i 和 dic[s[j]] ，每轮更新左边界 i ，保证区间 [i+1,j] 内无重复字符且最大。i=max(dic[s[j]],i)
· 哈希表 dic 统计： 指针 j 遍历字符 s , 哈希表统计字符 s[j] 最后一次出现的索引
· 更新结果 res : 取上轮 res 和本轮双指针区间 [i+1,j] 的宽度（即 j−i ）中的最大值。res=max(res,j−i)
"""

class Solution:
    # O(N)  |  O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res
```

#### 49 丑数

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数

```python3
"""
设已知长度为 n 的丑数序列 x1 x2 ... xn, 求第 n+1 个丑数 Xn+1
        Xa * 2,  1<a<=n
Xn+1 =  Xb * 3,  1<a<=n
        Xc * 5,  1<a<=n
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
```

#### 63 股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

    买卖该股票一次

    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
        注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格

相关题目: 
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）

```python3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MAX = 2 ** 31 - 1
        cost, profit = MAX, 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

    def maxProfitMore(self, prices: List[int]) -> int:
        length, earn = len(prices), 0
        for idx in range(length):
            if idx != 0:
                differ = prices[idx] - prices[idx-1]
                earn += differ if differ > 0 else 0
        return earn
```

### <span id = "C">C 搜索与回溯算法</span>

#### 12 矩阵中的路径|单词搜索 -

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用

[矩阵中的路径|单词搜索](https://leetcode-cn.com/problems/word-search/solution/79-dan-ci-sou-suo-dfs-hui-su-by-yiluolion/)

```python3
"""
1. 首先我们需要先找到单词的起始字母，然后再向四周扩散搜索
2. 默认从坐标 (0, 0) 开始搜索，先找到单词首字母，然后对其先进行标记（防止同个单元格被重复使用）；
然后向四个方位进行扩散搜索（注意限定边界，以及注意是否已被标记），对单元格的字母与单词中的字母继续比对：
    若匹配，则进行标记，继续扩散搜索；
    若不匹配，则尝试其他方位；
    若完全不匹配（四个方位都不匹配），则进行回退，同时释放当前单元格的标记。
3. 重复上面的步骤：
    当单词完全匹配，可直接返回 True；
    若所有单元格均搜索无果，则返回 False
"""

from typing import List
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]

        def dfs(x, y, idx):
            """搜索单词
            x: 行索引
            y: 列索引
            idx: 单词对应的字母索引
            """
            if board[x][y] != word[idx]: return False
            if idx == len(word) - 1: return True
            visited[x][y] = True  # 先标记

            # 找到符合的字母时开始向四个方向扩散搜索
            for i in range(4):
                nx = x + rows[i]
                ny = y + cols[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and dfs(nx, ny, idx + 1):
                    return True
            # 扩散未搜索对应的字母，释放标记
            # 继续往其他方位搜索
            visited[x][y] = False
            return False

        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0): return True
        return False
```

#### 26 树的子结构

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值

```python3
"""
1. 先序遍历树 A 中的每个节点 nA（对应函数 isSubStructure(A, B)）
2. 判断树 A 中 以 nA 为根节点的子树 是否包含树 B（对应函数 recur(A, B)）
"""
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
```

#### 27 二叉树的镜像

请完成一个函数，输入一个二叉树，该函数输出它的镜像

```python3
"""
    原二叉树              镜像二叉树
        4                     4
    2       7             7       2
  1   3   6   9         9   6   3   1

# 1. 递归
终止条件： 当节点 root 为空时（即越过叶节点），则返回 null
递推工作：
    初始化节点 tmp ，用于暂存 root 的左子节点；
    开启递归 右子节点 mirrorTree(root.right)，并将返回值作为 root 的左子节点
    开启递归 左子节点 mirrorTree(tmp)，并将返回值作为 root 的右子节点
返回值： 返回当前节点 root
# 2. 辅助栈 / 队列
"""
class Solution:
    # O(N)  |  O(N)
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        # tmp = root.left
        # root.left = self.mirrorTree(root.right)
        # root.right = self.mirrorTree(tmp)
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

    # O(N)  |  O(N)
    def mirrorTree_1(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
```

#### 28 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的

```python3
"""
L.val = R.val ：即此两对称节点值相等
L.left.val = R.right.val ：即 L 左子节点 和 R 右子节点 对称
L.right.val = R.left.val ：即 L 右子节点 和 R 左子节点 对称
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)
```

#### 32 从上到下打印二叉树 (BFS)

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印

    变形题目
    1. 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行
    2. 一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，其他行以此类推

```python3
import collections
class Solution:
    # BFS  O(N)  |  O(N)
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, _queue = [], collections.queue()
        _queue.append(root)
        while _queue:
            node = _queue.popleft()
            res.append(node.val)
            if node.left: _queue.append(node.left)
            if node.right: _queue.append(node.right)
        return res

    def levelOrder_1(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, _queue = [], collections.queue()
        _queue.append(root)
        while _queue:
            tmp = []
            for _ in range(len(_queue)):
                node = _queue.popleft()
                tmp.append(node.val)
                if node.left: _queue.append(node.left)
                if node.right: _queue.append(node.right)
            res.append(tmp)
        return res

    def levelOrder_2(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, _queue = [], collections.queue()
        _queue.append(root)
        while _queue:
            tmp = []
            n = len(_queue)
            for _ in range(n):
                node = _queue.popleft()
                tmp.append(node.val)
                if node.left: _queue.append(node.left)
                if node.right: _queue.append(node.right)
            # 通过 len(_queue) 的长度来判断当前行是偶数，还是奇数行
            res.append(tmp[::-1] if n % 2 else tmp)
        return res
```

#### 34 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径

```python3
# 先序遍历 + 路径记录
# 时间复杂度 O(N) ： N 为二叉树的节点数，先序遍历需要遍历所有节点
# 空间复杂度 O(N) ： 最差情况下，即树退化为链表时，path 存储所有树节点，使用 O(N) 额外空间

from typing import List
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, target):
            # 若节点 root 为空
            # 或当前值大于减去剩下的值(剪枝) or root.val > tar
            if not root or root.val > tar: return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                # 不用 res.append(path) 的原因
                #   若直接执行 res.append(path) ，则是将此 path 对象加入了 res
                #   后续 path 改变时， res 中的 path 对象也会随之改变，因此无法实现结果记录
                res.append(list(path))
            recur(root.left, target)
            recur(root.right, target)
            path.pop()

        recur(root, sum)
        return res
```

#### 36 二叉搜索树与双向链表

输入一棵二叉搜索树，将该二叉搜索树转换成一个 __排序的循环双向链表__。要求不能创建任何新的节点，只能调整树中节点指针的指向

```python3
class Solution:
    def treeToDoublyList(self, root: TreeNode) -> TreeNode:
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树

            # 修改节点引用
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else: 
                self.head = cur  # 最左侧节点，记录头节点
            self.pre = cur # 保存 cur

            dfs(cur.right)  # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)

        self.head.left, self.pre.right = self.pre, self.head
        return self.head
```

#### 37 序列化二叉树 (反序列化)

请实现两个函数，分别用来序列化和反序列化二叉树。保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构

```python3
# 层序遍历后恢复
import collections
class Solution:
    def serialize(self, root: TreeNode) -> str:
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data: str) -> TreeNode:
        if data == "[]": return
        vals = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
```

#### 38 字符串的排列 (全排列)

输入一个字符串，打印出该字符串中字符的所有排列。你可以以任意顺序返回这个字符串数组，但里面不能有重复元素

```python3
"""
        a - b   c
      /     c   b
  abc - b - a   c
      \     c   a
        c - a   b
            b   a
"""
from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            # 终止条件，最后一个元素
            if x == len(c) - 1:
                res.append(''.join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                # 重复，剪枝
                if c[i] in dic: continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[x], x[i] = c[i], x[x]  # 恢复

        dfs(0)
        return res
```

#### 54 二叉搜索树的第 k 大节点

给定一棵二叉搜索树，请找出其中第k大的节点

```python3
# 二叉搜索树的中序遍历为递增序列，易得二叉搜索树的 中序遍历倒序 为 递减序列

class Solution:
    # O(N)  |  O(N)
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
```

#### 55_1 二叉树的深度

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度

```python3
class Solution:
    def maxDepth_dfs(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_bfs(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res
```

#### 55_2 平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树

    树的深度 等于 左子树的深度 与 右子树的深度 中的 最大值 +1

```python3
# 后序遍历 + 剪枝 (从底至顶)
# 对二叉树做后序遍历，从底至顶返回子树深度，若判定某子树不是平衡树直接返回(剪枝)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0

            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1

            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1
```

#### 68 二叉搜索树的最近公共祖先

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先

    对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）

    若 root 是 p,q 的 最近公共祖先，三种情况之一：
        1. p 和 q 在 root 的子树中，且分列 root 的 两侧，即分别在左、右子树中
        2. p=root 且 q 在 root 的左或右子树中
        3. q=root 且 p 在 root 的左或右子树中

相关题目：
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先

```python3
class Solution:
    # 二叉搜索树特性: 任一左子节点的值小于它的父节点，任一右子节点的值大于它的父节点
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 保证 p.val < q.val
        if p.val > q.val: p, q = q, p
        while root:
            if root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left
            elif root.val < p.val:  # p,q 都在 root 的右子树中
                root = root.right
            else: break
        return root


    def lowestCommonAncestor_normal(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor_normal(root.left, p, q)
        right = self.lowestCommonAncestor_normal(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
```

### <span id = "D">D 分治算法</span>

#### 07 重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字

```python3
"""
前序遍历 preorder = [3,9,20,15,7]  # 根左右
中序遍历 inorder  = [9,3,15,20,7]  # 左根右
         3
      9      20
          15    7
"""

# 1. 递归  2. 迭代
from typing import List
class Solution:
    # O(N)  |  O(N)
    def buildTreeRecur(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left

            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = recur(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)

            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = recur(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        # 构造哈希映射，快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return recur(0, n - 1, 0, n - 1)

    # O(N)  |  O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root
```

#### 33 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同

```python3
# 递归、迭代
"""
[1, 3, 2,   6,      5]
   left  | right | root
"""

class Solution:
    # O(N^2)  |  O(N)
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            # 左子树节点 < root
            while postorder[p] < postorder[j]: p += 1
            m = p
            # 右子树节点 > root
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)
        return recur(0, len(postorder) - 1)

    # O(N)  |  O(N)
    def verifyPostorder(self, postorder: List[int]) -> bool:
        MAX = 2 ** 31 - 1
        stack, root = [], MAX  # 假设 postorder 均为正数，且小于 MAX
        # 倒序 遍历 (根、右、左)
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True
```

### <span id = "E">E 排序</span>

#### 40 最小的 k 个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4 (可混序，1、3、2、4也符合)

```python3
# 分析
# 1. python自带库小顶堆 heapq.nsmallest(k, arr)
# 2. 快速排序 (数组划分)，找前 K 大/前 K 小问题不需要对整个数组进行 O(NlogN) 的排序；直接通过快排切分排好第 K 小的数（下标为 K-1），那么它左边的数就是比它小的另外 K-1 个数
# 3. 计数排序

def getLeastNumbers_1(arr, k):
    import heapq
    return heapq.nsmallest(k, arr)

def getLeastNumbers_2(arr, k):
     # 快速排序，找前 K 大/前 K 小问题不需要对整个数组进行 O(NlogN) 的排序；
     # 直接通过快排切分排好第 K 小的数（下标为 K-1），那么它左边的数就是比它小的另外 K-1 个数
     if k >= len(arr): return arr
     def quick_sort(l, r):
        i, j = l, r
        while i < j:
            # pivot = arr[l]
            while i < j and arr[j] >= arr[l]:
                j -= 1
            while i < j and arr[i] <= arr[l]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[i] = arr[i], arr[l]
        if k < i:
            return quick_sort(l, i - 1)
        if k > i:
            return quick_sort(i + 1, l)
        return arr[:k]
        
    return quick_sort(0, len(arr) - 1)

def getLeastNumbers_3(arr, k):
    # 计数排序
    counter = [0] * (max(arr)+1)
    for i in range(len(arr)):
        counter[arr[i]] += 1
    cnt, idx, res = 0, 0, []
    while cnt < k:
        while counter[idx] > 0 and cnt < k:
            counter[idx] -= 1
            res.append(idx)
            cnt += 1
        idx += 1
    return res
```

#### 45 把数组排成最小的数

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个

e.g. 输入: [3,30,34,5,9]  输出: "3033459"

```python3 
"""
本质上是一个排序问题。
设数组 nums 中任意两数字的字符串为 x 和 y ，则规定 排序判断规则 为：

若拼接字符串 x+y>y+x ，则 x 大于 y; 反之，若 x+y<y+x ，则 x 小于 y
    (x 小于y 代表：排序完成后，数组中 x 应在 y 左边；“大于” 则反之)
"""

# 时间复杂度 O(NlogN): N 为最终返回值的字符数量（ strs 列表的长度 <= N ）；使用快排或内置函数的平均时间复杂度为 O(NlogN) ，最差为 O(N^2)
# 空间复杂度 O(N): 字符串列表 strs 占用线性大小的额外空间
def minNumber(nums) -> str:
    def quick_sort(l , r):
        if l >= r: return
        i, j = l, r
        while i < j:
            while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[l] = strs[l], strs[i]
        quick_sort(l, i - 1)
        quick_sort(i + 1, r)
    
    strs = [str(num) for num in nums]
    quick_sort(0, len(strs) - 1)
    return ''.join(strs)
```

#### 41 数据流中的中位数

如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数

```python3
"""
分析
给定一长度为 N 的无序数组，其中位数的计算方法：首先对数组执行排序 O(NlogN)，然后返回中间元素即可 O(1)

建立一个 小顶堆 A 和 大顶堆 B ，各保存列表的一半元素，且规定：
    A 保存较大的一半，长度为 N/2 [N为偶数] 或 (N+1)/2 [N为奇数]
    B 保存较小的一半，长度为 N/2 [N为偶数] 或 (N-1)/2 [N为奇数]
随后，中位数可仅根据 A, B 的堆顶元素计算得到
"""
from heapq import *
# Python 中 heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可

class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    def _addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
    
    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
```

#### 61 扑克牌中的顺子

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14

输入: [0,0,1,2,5]  输出: True

```python3
# 分析 (要考虑重复，直接退出)
# 1. 集合 Set + 遍历
# 2. 排序 + 遍历

def isStraight(arr):
    repeat = set()
    ma, mi = 0, 14
    for num in arr:
        if num == 0:
            continue
        ma = max(ma, num)
        mi = min(mi, num)
        if num in repeat:
            return False
        repeat.add(num)
    return ma - mi < 5

# 时间复杂度 O(1) ： 本题中给定牌数量 N≡5 ；数组排序使用 O(NlogN)=O(5log5)=O(1)
# 空间 O(1)
def isStraight_2(arr):
    joker = 0
    arr.sort()
    for i in range(4):
        if arr[i] == 0:
            joker += 1
        # 重复的，直接退出
        elif arr[i] == arr[i + 1]:
            return False
    return arr[4] - arr[joker] < 5
```


### <span id = "F">F 查找</span>

#### 03 数组中重复的数字

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字

```python3
# 1. 哈希表 / Set
# 2. 原地交换

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1

    def findRepeatNumber_1(self, nums: [int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            # Python 中，a,b=c,d 操作的原理是先暂存元组 (c,d) ，然后 “按左右顺序” 赋值给 a 和 b 。
            # 因此，若写为 nums[i],nums[nums[i]]=nums[nums[i]],nums[i] ，则nums[i] 会先被赋值
            #    之后 nums[nums[i]] 指向的元素则会出错
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
```

#### 04 二维数组中的查找

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

```python3
"""
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true
给定 target = 20，返回 false
"""
from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False
```

#### 11 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1

```python3
# 二分查找
from typing import List
class Solution:
    def minArray(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = i + (j - i) // 2  # >>   //2
            if nums[m] > nums[j]: i = m + 1
            elif nums[m] < nums[j]: j = m
            else: return min(nums[i:j])
        return numbers[i]
```

#### 50 第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母

```python3
# O(N)  |  O(1)
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '

    def firstUniqChar_1(self, s: str) -> str:
        import collections
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '
```

#### 53_1 在排序数组中查找数字

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]


```python3
from typing import List
class Solution:
    # O(log N)  |  O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        L, R = 0, n
        while L < R:
            mid = L + (R - L) // 2
            if nums[mid] == target:
                start, end = mid - 1, mid + 1
                while start >= 0 and nums[start] == target: start -= 1
                while end < n and nums[end] == target: end += 1
                return [start + 1, end - 1]
            elif nums[mid] < target: L = mid + 1
            else: R = mid
        return [-1, -1]
```

#### 53_2 0～n-1 中缺失的数字

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字

```python3
# 1. 二分法
# 2. 位运算 异或 ^

class Solution:
    # O(log N)  |  O(1)
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i
    
    # a^a=0；自己和自己异或等于0
    # a^0=a；任何数字和0异或还等于他自己
    def missingNumber_1(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i] ^ (i + 1)
        return xor
```

### <span id = "G">G 双指针</span>

#### 57 和为 s 的两个数字 [两数之和]

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可

相关题目

    1. 数组无序 > twoSum_1
    2. 三数之和 > threeSum
    3. 四数之和 > fourSum
    4. 最接近的三数之和 > threeSumClosest

```python3
from typing import List

class Solution:
    # 数组递增
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 头尾指针
        # 时间 O(n)  |  空间 O(1)
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []

    # 数组无序
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        # 复杂度
        # 时间 O(n)  |  空间 O(n)
        _hash = {}  # 哈希
        for idx, num in enumerate(nums):
            if target - num in _hash.keys():
                return [_hash[target - num], idx]
            else:
                _hash[nums[idx]] = idx
        return []
        """
        # 暴力匹配
        # 复杂度
        # 时间 O(n^2)  |  空间 O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序后遍历 (0，n-2)   另 2 个元素，首尾指针遍历
        # 复杂度
        # 时间 O(n^2)  |  空间 O(log N)
        nums.sort()  # 空间 log N
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break  # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1  # two-pointers
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res

    # 四数之和
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 复杂度
        # 时间 O(n^3)  |  空间 O(log N)
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append(
                            [nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets

    # 最接近的三数之和
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 复杂度
        # 时间 O(log N + n^2)  |  空间 O(log N)
        nums = sorted(nums)
        res = sum(nums[0:3])
        for i in range(len(nums)-1):
            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                elif total == target:
                    return total

                if abs(res-target) > abs(total-target):
                    res = total
        return res
```

#### 18 删除值对应链表的节点

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。 返回删除后的链表的头节点。

```python3
# 若链头为删除的节点，返回 head.next; 否则遍历找到前驱节点，删除对应节点后，返回 head
class Solution:
    def deleteNode(self, head: Node, val: int) -> Node:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head
```

#### 21 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。


```python3
# 双指针，从前开始找偶数，从后往前找奇数
# 时间复杂度 O(N)： N 为数组 nums 长度，双指针 head, tail 共同遍历整个数组。
# 空间复杂度 O(1)： 双指针 head, tail 使用常数大小的额外空间
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        head, tail = 0, len(nums) - 1
        while head < tail:
            # x&1 位运算 等价于 x%2 取余运算，即皆可用于判断数字奇偶性
            while head < tail and nums[head] & 1 == 1: head += 1
            while head < tail and nums[tail] & 1 == 0: tail -= 1
            nums[head], nums[tail] = nums[tail], nums[head]
        return nums
```

#### 22 链表中倒数第 k 个节点

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点

```python3
class Solution:
    def getKthFromEnd(self, head: Node, k: int) -> Node:
        fast, slow = head, head
        for _ in range(k):
            # 防止越界 k>len() return
            if not fast: return
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow
```

#### 25 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

```python3
# O(M+N) | O(1)
class Solution:
    def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
        cur = fake = Node(-1)
        while l1 and l2:
            if l1.val < l2.val: 
                cur.next, l1 = l1, l1.next
            else: 
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return fake.next
```

#### 52 两个链表的第一个公共节点

输入两个链表，找出它们的第一个公共节点。

    A: a1 -> a2 --------\
                        c1 -> c2 -> c3
    B: b1 -> b2 -> b3---/

```python3
# 若两链表相交于 c1 点，则 A 在相交前的距离为 A-c； B 在相交前距离为 B-c
# 指针 A 先遍历完链表 a1 ，再开始遍历链表 b1 ，当走到 node 时，共走步数为：a+(b−c)
# 指针 B 先遍历完链表 b1 ，再开始遍历链表 a1 ，当走到 node 时，共走步数为：b+(a−c)

# 若两链表 有 公共尾部 (即 c>0 ): 指针 A , B 同时指向 第一个公共节点 node
# 若两链表 无 公共尾部 (即 c=0 ): 指针 A , B 同时指向 null

class Solution:
    def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
```

#### 58_1 翻转单词顺序

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"

```python3
# 1. 分割 + 倒序
# 2. 双指针

class Solution:

    时间复杂度 O(N) ： 总体为线性时间复杂度，各函数时间复杂度和参考资料链接如下。
        split() 方法： O(N)
        trim() 和 strip() 方法：最差情况下（当字符串全为空格时）O(N)
        join() 方法：O(N)
        reverse() 方法：O(N)
    空间复杂度 O(N) ： 单词列表 strs 占用线性大小的额外空间

    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

    # O(N)  |  O(N)
    def reverseWords_1(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1  # 搜索首个空格
            res.append(s[i + 1: j + 1])  # 添加单词
            while i >= 0 and s[i] == ' ': i -= 1  # 跳过单词间空格
            j = i  # j 指向下个单词的尾字符
        return ' '.join(res)
```


### <span id = "H">H 位运算</span>

#### 15 求二进制中1的个数

对于一个字节(8bit)的变量，求其二进制表示中 '1' 的个数，要求算法的执行效率尽可能高

tips: 8bit的变量 即 0～255

    解法1 二进制操作，除以2，如果有余，表示当前位置有1
    解法2 除法 -> 位运算 (右移)
    --- python divmod 函数内部用的就是位运算
    解法3 只考虑和 '1' 的个数有关，判断二进制数中有且仅有一个 '1'，可以判断它是否为2的整数次幂。即用 v&v-1 判断
    例: 11111111 & (11111111 - 1) -> 11111111 & (11111110) = 11111110
    解法4 使用分支操作
    解法5 查表法

```python3
# 时间复杂度 O(log2v)
def count_one_bits_1_2(v):
    res = 0
    while(v):
        v, _cache = divmod(v, 2)
        res += _cache
    return res

# def count_one_bits_2(v):
#     res = 0
#     while(v):
#         res += v & 0x01
#         v >>= 1
#     return res

# 时间复杂度 O(1的个数)
def count_one_bits_3(v):
    res = 0
    while(v):
        v &= v - 1
        res += 1
    return res

# 时间复杂度 O(1)
def count_one_bits_4(v):
    # _hash = {{'0':0, '1':1, '2':1, '3':2,'4':1, '5':2, ...}
    _hash = {'0':0, '1':1, '2':1, '3':2,'4':1, '5':2}
    return _hash[str(v)]

# 时间复杂度 O(1)
def count_one_bits_5(v):
    # _list = [0, 1, 1, 2, 1, 2, ...]
    _list = [0, 1, 1, 2, 1, 2]
    return _list[v]
```

#### 56_1 数组中数字出现的次数

一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O(n)，空间复杂度是O(1)

    分析
    1. 异或运算: 两个相同数字异或为 0 ，即对于任意整数 a 有 a ^ a == 0
    2. 设两个只出现一次的数字为 x , y ，由于 x != y ，则 x 和 y 二进制至少有一位不同（即分别为 0 和 1 ），根据此位可以将 nums 拆分为分别包含 x 和 y 的两个子数组
    根据异或运算定义，若整数 x ^ y 某二进制位为 1 ，则 x 和 y 的此二进制位一定不同。换言之，找到 x ^ y 某为 1 的二进制位，即可将数组 nums 拆分为上述的两个子数组
    ---> 因此，初始化一个辅助变量 m=1 ，通过与运算从右向左循环判断，可 获取整数 x ^ y 首位 1 ，记录于 m 中

```python3
def singleNumber_1(arr):
    # 异或运算, 只出现1次的数字
    x = 0
    for i in arr:
        x ^= i
    return x

# 时间 O(N) 空间 O(1)
def singleNumber_2(arr):
    x, y, n, m = 0, 0, 0, 1
    for num in arr:
        # 1. 遍历异或, 得出不同的两个数异或的值
        n ^= num
    
    while n & m == 0:
        # 2. 循环左移 
        # 找到 n ^= m 某为 1 的二进制位
        m <<= 1

    for num in arr:
        # 3 若 num & m != 0 , 划分至子数组 1 ，执行遍历异或
        if num & m:
            x ^= num
        # 4 若 num & m == 0 , 划分至子数组 2 ，执行遍历异或
        else:
            y ^= num
    return x, y
```


### <span id = "I">I 数学</span>

#### 39 众数 <寻找发帖 "水王">

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字

    分析
    1. 哈希表统计法： 遍历数组 nums ，用 HashMap 统计各数字的数量，即可找出 众数 。此方法时间和空间复杂度均为 O(N)
    2. 数组排序法： 将数组 nums 排序，数组中点的元素 一定为众数
    3. 摩尔投票法： 核心理念为 票数正负抵消 。此方法时间和空间复杂度分别为 O(N) 和 O(1) ，为本题的最佳解法

相关题目
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素

分析
- “多数”是指超过n/3，不是n/2，因此最多会有两个元素是众数，要建立两个candidate
- 题目没保证多数元素一定存在，所以最后要对candidate进行检验。因此整个流程分为两步：step1投票阶段，step2检验阶段

    对于候选者cand1和cand2：
    - 如果投cand1，cand1加一票。
    - 如果投cand2，cand2加一票。
    - 如果投其他元素，cand1和cand2各减一票

```python3
# 时间复杂度 O(N)
def majorityElement_1(v):
    n = len(v)
    if n == 0:
        return 0
    _hash = {}
    for i in v:
        if i in _hash.keys():
            _hash[i] += 1
            if _hash[i] >= n // 2:
                # print("_hash[i] >= n // 2:", i)
                return i
        else:
            _hash[i] = 1

def majorityElement_2(v):
    return sorted(v)[len(v)//2]

def majorityElement_3(v):
    # 时间复杂度 O(N) ： N 为数组 nums 长度。
    # 空间复杂度 O(1) ： votes 变量使用常数大小的额外空间
    # 摩尔投票法
    votes = 0
    for i in v:
        if votes == 0:
            x = i
        votes += 1 if x == i else -1
    return x

# 找出所有出现超过 ⌊ n/3 ⌋ 次的元素
def majorityElement_3_1(v):
    # 时间复杂度 O(N) | 空间复杂度 O(1)
    majorityO, majority1, countO, count1 = 0, 0, 0, 0
    for i in v:
        if countO == 0 and i != majority1:
            majorityO = i
            countO += 1
            continue
        elif count1 == 0 and i != majorityO:
            majority1 = i
            count1 += 1
            continue
        else:
            if majorityO == i:
                countO += 1
            elif majority1 == i:
                count1 += 1
            else:
                countO -= 1
                count1 -= 1

    return [i for i in [majorityO, majority1] if v.count(i) > len(v)/3]
```

#### 43 数字 1 的个数

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数

```python3
# 时间复杂度：O(log10 N) | 空间 O(1)
def countDigitOne(n: int) -> int:
    # 思路 分别计算各个位置上1出现的次数 最后求和
    if n <= 0:
        return 0
    res = 0
    # base用来表示当前是计算哪个位置，比如说base等于1就表示是计算个位数，base=10表示当前计算十位数
    base = 1
    while n // base != 0:
        # cur_num表示当前位置上的数字
        cur_num = (n // base) % 10
        # high_num表示高位的数字，比如说当前计算十位数出现1的个数，那么1812中high_pos就应该是18
        high_num = n // (base * 10)
        # low_num表示低位的数字，比如说上面的例子就是2
        low_num = n - (n // base) * base
        # 接下来就是比较当前数字和1的大小
        # 1.如果=0，那么当前位置出现1的个数只取决于高位  high_num * base
        print("base, high_num, cur_num, low_num", base, high_num, cur_num, low_num)
        if cur_num == 0:
            res += high_num * base
            print("cur_num=0 res", res, high_num * base)
        # 2.如果=1，那么当前位置出现1的个数不光取决于高位，还取决于低位  (high_num * base + (low_num + 1))
        elif cur_num == 1:
            res += (high_num * base + (low_num + 1))
            print("cur_num=1 res", res, (high_num * base + (low_num + 1)))
        # 3.如果>1,那么当前位置出现1的个数只取决于高位  (high_num + 1) * base
        else:
            res += (high_num + 1) * base
            print("cur_num>1 res", res, (high_num + 1) * base)
        # 计算下一个位置的1的个数，base需要*10
        base *= 10
    return res
```

### <span id = "J">J 模拟</span>

#### 31 栈的压入、弹出序列 是否匹配

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列

    分析
    1. 初始化： 辅助栈 stack ，弹出序列的索引 i ；
    2. 遍历压栈序列： 各元素记为 num ；
        元素 num 入栈；
        循环出栈：若 stack 的栈顶元素 == 弹出序列元素 popped[i] ，则执行出栈与 i++ ；
    3. 返回值： 若 stack 为空，则此弹出序列合法

```python3
# O(N) | O(N)
def validateStackSequences(pushed, popped):
    stack, i = [], 0
    for num in pushed:
        stack.append(num) # num 入栈
        while stack and stack[-1] == popped[i]: # 循环判断与出栈
            stack.pop()
            i += 1
    return not stack
```

#### 02 实现Singleton模式

​单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案。

__new__()在__init__()之前被调用，用于生成实例对象。利用这个方法和类的属性的特点可以实现设计模式的单例模式。

1. 使用__new__方法

    ```python
    class Singleton(object):
        def __new__(cls, *args, **kw):
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            return cls._instance

    class MyClass(Singleton):
        a = 1
    ```

2. 共享属性

    创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法

    ```python
    class Borg(object):
        _state = {}
        def __new__(cls, *args, **kw):
            ob = super(Borg, cls).__new__(cls, *args, **kw)
            ob.__dict__ = cls._state
            return ob

    class MyClass2(Borg):
        a = 1
    ```

3. 装饰器版本

    ```python
    def singleton(cls):
        instances = {}
        def getinstance(*args, **kw):
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
        return getinstance

    @singleton
    class MyClass:
    ...
    ```

4. import 方法

    作为 python 的模块是天然的单例模式
    ```python
    # mysingleton.py
    class My_Singleton(object):
        def foo(self):
            pass

    my_singleton = My_Singleton()

    # to use
    from mysingleton import my_singleton

    my_singleton.foo()
    ```