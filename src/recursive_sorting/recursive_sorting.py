# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merge_arr = []
    while len(arrA) != 0 and len(arrB) != 0:
        merge_arr.append(arrA.pop(0) if arrA[0] < arrB[0] else arrB.pop(0))
    return merge_arr + arrA + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid_index = len(arr) // 2
    return merge(merge_sort(arr[:mid_index]), merge_sort(arr[mid_index:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, left_start_index, mid_index, end_index):
    right_start_index = mid_index + 1
    if arr[mid_index] <= arr[right_start_index]:
        return arr
    while left_start_index <= mid_index and right_start_index <= end_index:
        if arr[left_start_index] > arr[right_start_index]:
            value_to_insert = arr[right_start_index]
            for moving_index in range(right_start_index, left_start_index, -1):
                arr[moving_index] = arr[moving_index - 1]
            arr[left_start_index] = value_to_insert
            mid_index += 1
            right_start_index += 1
        left_start_index += 1


def merge_sort_in_place(arr, left_index, right_index):
    if left_index < right_index:
        mid_index = (left_index + right_index) // 2
        merge_sort_in_place(arr, left_index, mid_index)
        merge_sort_in_place(arr, mid_index + 1, right_index)
        merge_in_place(arr, left_index, mid_index, right_index)


# STRETCH: implement the timsort function below
def timsort(arr):
    import sys
    sys.path.append("../iterative_sorting")
    # pylint: disable=import-error
    from iterative_sorting import insertion_sort
    RUN = 32
    for i in range(0, len(arr), RUN):
        insertion_sort(arr, i, min(i + RUN, len(arr)))
    merge_size = RUN
    while merge_size < len(arr):
        for start_index in range(0, len(arr), merge_size * 2):
            mid_index = start_index + merge_size
            end_index = min(start_index + (merge_size * 2), len(arr))
            merge_in_place(arr, start_index, mid_index, end_index)
        merge_size *= 2


# ADDITIONAL: Quick sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_arr = [arr[0]]
    left_side_arr = []
    right_side_arr = []
    for i in range(1, len(arr)):
        if arr[i] < pivot_arr[0]:
            left_side_arr.append(arr[i])
        elif arr[i] > pivot_arr[0]:
            right_side_arr.append(arr[i])
        else:
            pivot_arr.append(arr[i])
    return quick_sort(left_side_arr) + pivot_arr + quick_sort(right_side_arr)
