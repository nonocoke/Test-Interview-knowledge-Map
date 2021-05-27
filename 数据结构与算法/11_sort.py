
"""
    原地排序 O(1) | 时间复杂度 O(n^2)
    Bubble sort, insertion sort and selection sort
    (冒泡排序、插入排序)(稳定) 、选择排序(不稳定)
    

"""

from typing import List
import itertools


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
