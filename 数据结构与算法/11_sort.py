
"""
    原地排序 O(1) | 时间复杂度 O(n^2)
    Bubble sort, insertion sort and selection sort
    (冒泡排序、插入排序)(稳定) 、选择排序(不稳定)
    

"""

from typing import List
import itertools
import random


# Bubble sort
def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        swap = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap = True
        if not swap:
            break


# insert sort
# 假设左侧1个元素为有序数组，遍历2-n元素，插入至左侧有序数组
# 变成了 逆序寻找插入位置，并后移相应数据 问题
# 时间 O(n^2)  |  空间 O(1)
def insert_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(1, length):
        val = a[i]
        j = i - 1
        while j >= 0 and a[j] > val:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = val


# 每次都选择一个最小的元素放在 i 位置上
def select_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


# 计数排序
def counting_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    # a中有counts[i]个数不大于i
    counts = [0] * (max(a) + 1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))
    print(counts)

    # 临时数组，储存排序之后的结果
    a_sorted = [0] * len(a)
    for num in reversed(a):
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1

    a[:] = a_sorted


# 快速排序
"""
    时间 O(nlog n)  |  空间 O(log n)
        递推公式
    quick_sort(p…r) = quick_sort(p…q-1) + quick_sort(q+1… r)
        终止条件
    p >= r
        伪代码
    // 快速排序，A是数组，n表示数组的大小
    quick_sort(A, n) {
    quick_sort_c(A, 0, n-1)
    }
    // 快速排序递归函数，p,r为下标
    quick_sort_c(A, p, r) {
    if p >= r then return

    q = partition(A, p, r) // 获取分区点
    quick_sort_c(A, p, q-1)
    quick_sort_c(A, q+1, r)
    }
"""

def quick_sort(a: List[int]):
    return _recur_quick_sort(a,  0, len(a) - 1)


def _recur_quick_sort(a: List[int], low: int, high: int):
    if low >= high:
        return
    # get a random position as the pivot
    k = random.randint(low, high)
    a[low], a[k] = a[k], a[low]
    m = _partition(a, low, high)  # a[m] is in final position
    _recur_quick_sort(a, low, m - 1)
    _recur_quick_sort(a, m + 1, high)


def _partition(a: List[int], low: int, high: int):
    pivot = a[low]
    j = low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]  # swap
    a[low], a[j] = a[j], a[low]
    return j

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# From 编程珠玑2

def quick_sort_2(a: List[int]):
    """ 
    - 双向排序: 提高非随机输入的性能
    - 不需要额外的空间,在待排序数组本身内部进行排序
    - 基准值通过random随机选取
    - 入参: 待排序数组, 数组开始索引 0, 数组结束索引 len(array)-1
    """
    if a is None or len(a) < 1:
        return a

    def swap(a: List[int], low: int, upper: int):
        a[low], a[upper] = a[upper], a[low]

    def QuickSort_TwoWay(a: List[int], low: int, upper: int):
        # 小数组排序i可以用插入或选择排序
        #       n = 1000000 数据分析后，u - l = 50 左右
        #       if upper-low < 50 : return insert_sort(a)
        # 基线条件: low index = upper index; 也就是只有一个值的区间
        if low >= upper:
            return a
        # 随机选取基准值, 并将基准值替换到数组第一个元素
        swap(a, low, int(random.uniform(low, upper)))
        tmp = a[low]
        # 缓存边界值, 从上下边界同时排序
        i, j = low, upper
        while True:
            # 第一个元素是基准值,所以要跳过
            i += 1
            # 在小区间中, 进行排序
            # 从下边界开始寻找大于基准值的索引
            while i <= upper and a[i] <= tmp:
                i += 1
            # 从上边界开始寻找小于基准值的索引
            # 因为j肯定大于i, 所以索引值肯定在小区间中
            while a[j] > tmp:
                j -= 1
            # 如果小索引大于等于大索引, 说明排序完成, 退出排序
            if i >= j:
                break
            # swap(a, i, j)
            # 优化代码 - 展开循环体内 swap 函数
            a[i], a[j] = a[j], a[i]
        # 将基准值的索引从下边界调换到索引分割点
        # 不在循环体内，影响不大
        # a[low], a[j] = a[j], a[low]
        swap(a, low, j)
        QuickSort_TwoWay(a, low, j - 1)
        QuickSort_TwoWay(a, j + 1, upper)
        return a

    return QuickSort_TwoWay(a, 0, len(a) - 1)

#python 版本简易实现 但空间复杂度不是O(1)
def quickSort(self,nums):
    if not nums:
        return []
    mid = nums[0]
    left = self.quickSort([x for x in nums[1:] if x<mid])
    right = self.quickSort([x for x in nums[1:] if x>=mid])
    return left+[mid]+right

# 归并排序
"""
    递推公式
    merge_sort(p…r) = merge(merge_sort(p…q), merge_sort(q+1…r))
    终止条件
    p >= r 不用再继续分解

    归并排序算法伪代码
    A是数组，n表示数组大小
    merge_sort(A, n) {
    merge_sort_c(A, 0, n-1)
    }
    // 递归调用函数
    merge_sort_c(A, p, r) {
    // 递归终止条件
    if p >= r  then return
    // 取p到r之间的中间位置q
    q = (p+r) / 2
    // 分治递归
    merge_sort_c(A, p, q)
    merge_sort_c(A, q+1, r)
    // 将A[p...q]和A[q+1...r]合并为A[p...r]
    merge(A[p...r], A[p...q], A[q+1...r])
    }
"""

def merge_sort(a: List[int]):
    _recur_merge_sort(a, 0, len(a) - 1)

def _recur_merge_sort(a: List[int], low: int, high: int):
    if low >= high: return
    mid = low + (high -low) // 2
    _recur_merge_sort(a, low, mid)
    _recur_merge_sort(a, mid + 1, high)
    _merge(a, low, mid, high)

def _merge(a: List[int], low: int, mid: int, high: int):
    # 转化问题为::合并特殊的两个有序数组
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


def test_bubble_sort():
    test_array = [1, 1, 1, 1]
    bubble_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_insert_sort():
    test_array = [1, 1, 1, 1]
    insert_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insert_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insert_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_select_sort():
    test_array = [1, 1, 1, 1]
    select_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    select_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    select_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_quick_sort():
    test_array = [1, 1, 1, 1]
    quick_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    quick_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    quick_sort(test_array)
    assert test_array == [1, 2, 3, 4]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insert_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    select_sort(array)
    print(array)

    a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    counting_sort(a3)
    print(a3)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    quick_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    quick_sort_2(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    merge_sort(array)
    print(array)