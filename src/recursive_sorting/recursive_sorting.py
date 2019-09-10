# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # TO-DO
    for i in range(elements):
        if len(arrA) == 0:
            return merged_arr[:i] + arrB
        elif len(arrB) == 0:
            return merged_arr[:i] + arrA
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            arrA = arrA[1:]
        else:
            merged_arr[i] = arrB[0]
            arrB = arrB[1:]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, left_start, mid, end):
    # TO-DO
    right_start = mid + 1
    if arr[mid] <= arr[right_start]:
        return arr
    while left_start <= mid and right_start <= end:
        if arr[left_start] <= arr[right_start]:
            left_start += 1
        else:
            value_to_insert = arr[right_start]
            move = right_start
            while move != left_start:
                arr[move] = arr[move - 1]
                move -= 1
            arr[left_start] = value_to_insert
            left_start += 1
            mid += 1
            right_start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        m = (l + r) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the timsort function below
def timsort(arr):
    # TO-DO
    import sys
    sys.path.append("../iterative_sorting")
    # pylint: disable=import-error
    from iterative_sorting import insertion_sort
    RUN = 32
    for i in range(0, len(arr), RUN):
        insertion_sort(arr, i, min(i + RUN, len(arr)))
    merge_size = RUN
    while merge_size < len(arr):
        for start in range(0, len(arr), merge_size * 2):
            mid = start + merge_size
            end = min(start + (merge_size * 2), len(arr))
            merge_in_place(arr, start, mid, end)
        merge_size *= 2
    return arr


# ADDITIONAL: Quick sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = [arr[0]]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot[0]:
            left.append(arr[i])
        elif arr[i] > pivot[0]:
            right.append(arr[i])
        else:
            pivot.append(arr[i])
    if len(left) == 0:
        return pivot + quick_sort(right)
    if len(right) == 0:
        return quick_sort(left) + pivot
    return quick_sort(left) + pivot + quick_sort(right)
