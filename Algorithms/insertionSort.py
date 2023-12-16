#https://www.youtube.com/watch?v=R_wDA-PmGE4&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

arr = [21, 32, 65, 87, 40]
insertionSort(arr)
print(arr)