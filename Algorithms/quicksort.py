#https://www.youtube.com/watch?v=9KBwdDEwal8&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=5

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i, j, pivot = left, right - 1, arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j < left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

arr = [62, 76, 39, 58, 29, 44, 20, 92]
quicksort(arr, 0, len(arr) - 1)
print(arr)