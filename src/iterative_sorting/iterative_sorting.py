# TO-DO: Complete the selection_sort() function below
def selection_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    for start in range(start, end - 1):
        for walk in range(start + 1, end):
            if arr[start] > arr[walk]:
                arr[start], arr[walk] = arr[walk], arr[start]


def bubble_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    while True:
        has_swapped = False
        for i in range(start, end - 1):
            left = i
            right = i + 1
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                has_swapped = True
        if not has_swapped:
            break


# STRETCH: implement the Count Sort function below
def count_sort(arr):
    if len(arr) <= 1:
        return arr
    value_counts = [0] * (max(arr) + 1)
    for val in arr:
        if val < 0:
            return "Error: count sort cannot have negative values"
        else:
            value_counts[val] += 1
    arr.clear()
    for value in range(len(value_counts)):
        arr += [value] * value_counts[value]


# ADDITIONAL: Insertion sort algorithm
def insertion_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    for moving_index in range(start, end):
        val_to_insert = arr[moving_index]
        for insertion_index in range(moving_index - 1, start - 1, -1):
            if val_to_insert < arr[insertion_index]:
                arr[insertion_index + 1] = arr[insertion_index]
                if insertion_index == 0:
                    arr[0] = val_to_insert
            else:
                arr[insertion_index + 1] = val_to_insert
                break
