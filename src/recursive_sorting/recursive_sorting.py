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
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the timsort function below
def timsort(arr):
    # TO-DO

    return arr
