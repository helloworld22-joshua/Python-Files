import time
from PIL import Image

start_time = time.time()                                        # Checks how long it takes to execute (usefull when comparing sorting algorithms)

img = Image.open(r"Image Manipulation\Source\lava_ship.png")
pix = img.load()

def quicksort(arr, left, right):                                # See file (Algorithms -> quickSort.py) for documentation
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

print("Task: Transform image to array")

arr = []                                                        # Empty array

for y in range(img.size[1]):

    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")
    
    for x in range(img.size[0]):
        r, g, b = pix[x, y]

        arr.append([r + g + b, x, y])                           # Adds a new item with total pixels and coordinates to array
else:
    print("Status: Completed!")

print("Task: Sort array")

quicksort(arr, 0, len(arr) - 1)                                 # Other algorithms work too but this one seems to be the fastest

print("Task: Transform array to new image")

new_img = Image.new(img.mode, img.size)
new_pix = new_img.load()

for y in range(img.size[1]):

    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")

    for x in range(img.size[0]):
        position = y * img.size[1] + x                          # Converts array from one to two dimensions
        new_pix[x, y] = pix[arr[position][1], arr[position][2]] # Retrieves x and y coordinates from array
else:
    print("Status: Completed!")

print(f"Execution time: {time.time() - start_time}")            # Time it took to execute

new_img.save(f"Image Manipulation\Results\sortPixels_{round(time.time() * 1000)}.png")

img.close()
new_img.close()