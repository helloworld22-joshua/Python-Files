#https://www.youtube.com/watch?v=9KBwdDEwal8&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=5

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    print(f"i: {i} ({arr[i]}), j: {j} ({arr[j]}), p: {right} ({pivot})")

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
            print(f"i: {i} ({arr[i]})")

        while j > left and arr[j] >= pivot:
            j -= 1
            print(f"j: {j} ({arr[j]})")

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            print(f"Swapped {arr[i]} and {arr[j]}: {arr}")

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        print(f"Swapped {arr[i]} and {arr[right]}: {arr}")

    return i

arr = [4, 2, 1, 6, 3, 5] #[62, 76, 39, 58, 29, 44, 20, 92]
print("Start:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Result:", arr)