from typing import List


def binary_search(arr: List[int], target: int) -> int:
    '''Given a sorted array arr and a number target,
        return the index ind such that arr[ind] == target if it exists,
        and -1 otherwise.

    :param arr: the sorted list to search from.
    :param target: the number to search for in arr.
    :return: ind such that arr[ind] == target, or -1 if it does not exist.
    :rtype: int.
    '''

    if not arr:
        return -1

    start, end = 0, len(arr) - 1

    if arr[start] == target:
        return start
    elif arr[end] == target:
        return end

    if arr[start] > target or arr[end] < target:
        return -1

    while end - start > 1:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid
        else:
            start = mid

    return -1
