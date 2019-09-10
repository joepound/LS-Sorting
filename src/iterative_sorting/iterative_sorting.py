# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            moving_index = j
            if arr[smallest_index] > arr[moving_index]:
                smallest_index = moving_index

        # TO-DO: swap
        if smallest_index != cur_index:
            arr[cur_index], arr[smallest_index] = (
                arr[smallest_index], arr[cur_index]
            )

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    has_swapped = True
    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - 1):
            left = i
            right = i + 1
            if arr[left] > arr[right]:
                arr[left], arr[right] = (arr[right], arr[left])
                has_swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr
    if maximum == -1:
        maximum = max(arr)
    value_counts = [0] * (maximum + 1)
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            value_counts[i] += 1
    arr = []
    for i in range(len(value_counts)):
        arr += [i] * value_counts[i]
    return arr


# ADDITIONAL: Insertion sort algorithm
def insertion_sort(arr, start, end):
    if end <= 1:
        return arr
    for i in range(start, end):
        temp = arr[i]
        track = None
        for j in range(i - 1, -1, -1):
            track = j
            if temp < arr[j]:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = temp
                track = None
                break
        if track is not None:
            arr[track] = temp
    return arr
