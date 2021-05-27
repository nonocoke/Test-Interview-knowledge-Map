
"""
    Bubble sort, insertion sort and selection sort
    冒泡排序、插入排序、选择排序
"""

from typing import List

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
