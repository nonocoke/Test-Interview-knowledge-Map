# coding:utf8
#!/usr/bin/python3
import threading
import queue
import functools
import copy
import bisect
import random
import itertools
from io import StringIO
import heapq
import math
import array
import enum
from hashlib import new


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

# 当堆中元素排序好之后，
# 使用 heappop() 方法可以移除值最小的元素
for i in range(2):
    smallest = heapq.heappop(data)
    print('pop    {:>3}:'.format(smallest))
    show_tree(data)

# 移除堆中存在的元素并替换为其他元素，
# 可以使用方法 heapreplace() 实现
data = [19, 9, 4, 10, 11]
heapq.heapify(data)
show_tree(data)
# 原地替换元素并且维持指定大小的堆结构，可以用于实现例如优先队列这样的数据结构
for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}:'.format(smallest, n))
    show_tree(data)

# heapq 还包含两个用于检查可迭代对象并找到它所包含的最大或最小值范围的函数
# nlargest() 和 nsmallest() 这两个函数只对当 n > 1 并且 n 较小的时候表现出很高的效率，
# 但是在少数情况下仍然可以派上用场
data = [19, 9, 4, 10, 11]
print('all :', data)
print('3 largest :', heapq.nlargest(3, data))
print('from sort :', list(reversed(sorted(data)[-3:])))
print('3 smallest :', heapq.nsmallest(3, data))
print('from sort  :', sorted(data)[:3])

# 高效合并两个已排序的列表
# 1. 对于小数据集来说，将几个已排序列表组合成一个新列表是很容易的
a = [33, 58, 71, 88, 95]
b = [10, 11, 17, 38, 91]
# [10, 11, 17, 33, 38, 58, 71, 88, 91, 95]
print(list(sorted(itertools.chain(a, b))))
print()
# 2. 对于大数据集，上述方法会使用大量的内存
# merge() 使用堆去一次生成一个新的列表 ，
# 可以使用固定数量的内存来确定下一个元素，而不是对合并之后的列表进行整体排序
random.seed(2021)
data = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

print(data)
for i, d in enumerate(data):
    print('{}: {}'.format(i, d))
print('\nMerged: ')
# 因为 merge() 方法使用堆来实现，
# 它是根据被合并的列表的数量而不是列表中的元素数量来消耗内存的
for i in heapq.merge(*data):
    print(i, end=' ')
print()

# bisect 维护有序列表
# bisect 模块里实现了一个向列表插入元素时也会顺便排序的算法
# 二分查找出插入位置，然后插入
a = [1, 4, 6, 8, 12, 15, 20]
position = bisect.bisect(a, 13)
print(position)
# 用可变序列内置的 insert 方法插入
a.insert(position, 13)
print(a)

# 使用 bisect.insort(), 比 bisect 先查找插入位置，再用 insert 方法插入更快速
a = [1, 4, 6, 8, 12, 15, 20]
bisect.insort(a, 13)
print(a)

# 对重复的数据的处理
# 可以选择将新值插到旧值的左边，也可以插到右边
# insort() 函数实际上是 insort_right() 函数, 将新值插到旧值的右边
# insort_left() 将值插到旧值的左边
a = [1, 4, 6, 8, 12, 15, 20]
bisect.insort(a, 13)
bisect.insort_left(a, 13)
print(a)


# copy 对象复制
# 浅复制 是用 copy() 来创建的一个填充了对原始对象引用的新容器


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass('a')
my_list = [a]
dup = copy.copy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))

# 由 deepcopy() 创建的 深拷贝 是一个新的容器， 容器里面填充了原始对象内容的副本
# 为了创建一个 list 的深拷贝，会先创建一个新的 list 对象， 复制原序列里面的元素，然后将这些副本添加到新的序列当中
a = MyClass('a')
my_list = [a]
dup = copy.deepcopy(my_list)
print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))


# queue - 线程安全的 FIFO 队列
print('\n> queue')
# Queue 类实现了一个基本的先进先出的容器。
# 使用 put() 将元素添加到序列的一端，并适用 get() 从另一端移除
fifo_q = queue.Queue()
for i in range(5):
    fifo_q.put(i)
print(fifo_q)
while not fifo_q.empty():
    print(fifo_q.get(), end=' ')
print()

# LifoQueue 后进先出的模式（与普通的栈结构类似）
lifo_q = queue.LifoQueue()
for i in range(5):
    lifo_q.put(i)
print(lifo_q)
while not lifo_q.empty():
    print(lifo_q.get(), end=' ')
print()

# Priority Queue

@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()

q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()
