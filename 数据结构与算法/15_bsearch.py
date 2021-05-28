
from typing import List

# 迭代


def bsearch(nums: List[int], target: int) -> int:
    """Binary search of a target in a sorted array
    without duplicates. If such a target does not exist,
    return -1, othewise, return its index.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 递归
def bsearch2(nums: List[int], target: int) -> int:
    return _recur_bsearch2(nums, 0, len(nums) - 1, target)


def _recur_bsearch2(nums: List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return _recur_bsearch2(nums, mid + 1, high, target)
    else:
        return _recur_bsearch2(nums, low, mid - 1, target)


if __name__ == "__main__":
    nums = [1, 2, 4, 5, 7, 9, 10, 22]
    print(bsearch(nums, 4))
    print(bsearch2(nums, 4))
