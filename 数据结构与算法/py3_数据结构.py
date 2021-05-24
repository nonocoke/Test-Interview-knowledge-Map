# coding:utf8
#!/usr/bin/python3
import array
import enum


# enum 模块定义了一个具备可迭代性和可比较性的枚举类型。
# 它可以为值创建具有良好定义的标识符，而不是直接使用字面上的字符串或者整数
class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\Member name: {}'.format(BugStatus.wont_fix.name))
print('\Member value: {}'.format(BugStatus.wont_fix.value))


# array 模块定义了一个与 list 非常相似的序列化数据结构，只是所有的成员都必须是相同的初始类型。
# 支持的类型有：所有的数值型或者其他固定大小的初始类型，如 bytes 型
"""
代码 类型 最小占用空间 (bytes)
b	int	1
B	int	1
h	signed short	2
H	unsigned short	2
i	signed int	2
I	unsigned int	2
l	signed long	4
L	unsigned long	4
q	signed long long	8
Q	unsigned long long	8
f	float	4
d	double float	8
"""


a = array.array('i', range(3))
print('Initial :', a)
a.extend(range(3))  # 向末尾添加元素
print('Extend :', a)
print('Slice :', a[2:5])  # 切片
print('Iterator :')
print(list(enumerate(a)))  # 迭代

# 一个最大堆保证了父节点的值大于或等于子节点的值。一个最小堆则是父节点的值要小于等于子节点的值
# Python 的 heapq 模块使用的是最小堆
import math
import heapq
from io import StringIO

def show_tree(tree, total_width=36, file=' '):
    """ 格式化打印一颗树"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)
    print()

heap = []
data = [19, 9, 4, 10, 11]
print('random :', data)
print()

# 当使用 heappush() 这个方法的时候，
# 堆中数据的顺序会与从数据源加载进来时的数据的顺序保持一致
for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)

# 如果数据早就存储在内存中，
# 使用 heapify() 方法可以更快的对列表中的数据进行
# --> 原地重排
print('random :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
