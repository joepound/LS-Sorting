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
    # TO-DO

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # TO-DO

    return arr
