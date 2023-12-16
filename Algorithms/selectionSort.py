#https://www.youtube.com/watch?v=ee80YmiaSVQ&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=2

def selectionSort(arr):
    for i in range (0, len(arr) - 1):
        curMinIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curMinIdx]:
                curMinIdx = j

        arr[i], arr[curMinIdx] = arr[curMinIdx], arr[i]

arr = [62, 76, 39, 58, 29]
selectionSort(arr)
print(arr)