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

    return arr
