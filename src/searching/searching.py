# STRETCH: implement Linear Search
def linear_search(arr, target, start=0, end=None):
    if end is None:
        end = len(arr)
    for i in range(start, end):
        if arr[i] == target:
            return i
    return -1


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target, lowest_index=0, highest_index=None):
    if highest_index is None:
        highest_index = len(arr) - 1
    while lowest_index <= highest_index:
        mid_index = (lowest_index + highest_index) // 2
        if target > arr[mid_index]:
            lowest_index = mid_index + 1
        elif target < arr[mid_index]:
            highest_index = mid_index - 1
        else:
            return mid_index
    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, lowest_index=0, highest_index=None):
    if highest_index is None:
        highest_index = len(arr) - 1
    mid_index = (lowest_index + highest_index) // 2
    if lowest_index > highest_index:
        return -1
    if target == arr[mid_index]:
        return mid_index
    if target < arr[mid_index]:
        highest_index = mid_index - 1
    if target > arr[mid_index]:
        lowest_index = mid_index + 1
    return binary_search_recursive(arr, target, lowest_index, highest_index)
