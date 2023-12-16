#https://www.youtube.com/watch?v=cVZMah9kEjI&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=4

def mergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        mergeSort(left_arr)
        mergeSort(right_arr)

        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr = [3, 5, 1, 9, 2, 8, 6, 4, 7]
mergeSort(arr)
print(arr)