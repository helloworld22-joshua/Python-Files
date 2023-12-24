import time
from PIL import Image

img = Image.open(r'Image Manipulation\forza.png')
pix = img.load()

def convolut(x, y):
    result = (0, 0, 0)                                              # Sum of values of individual pixels
    skip = 0                                                        # Skipped pixels shouldn't be account for

    for i in range(y - 1, y + 2):                                   # Three by three square around pixel
        if not 0 <= i < img.size[1]:                                # Makes sure square doesn't take values from outside the image
            skip += 3                                               # Three skips since it's an entire row
            continue

        for j in range(x - 1, x + 2):
            if 0 <= j < img.size[0]:
                result = tuple(map(sum, zip(result, pix[j, i])))    # Adds values of pixel to the sum of the square
            else:
                skip += 1                                           # Only one skip since it's only one pixel

    return tuple(round(pixel / (9 - skip)) for pixel in result)     # Devide sum by nine for average value of the pixels combined

new_img = Image.new(img.mode, img.size)
new_pix = new_img.load()

def convolution(multiplier):
    for _ in range(multiplier):                                     # Amount of repetitions (low values only)
        for y in range(img.size[1]):

            if not y % 100: print(f"Progress ({multiplier}): {round(y / img.size[1] * 100)}%") # Status report every 100 pixels on the y-axis

            for x in range(img.size[0]):
                new_pix[x, y] = convolut(x, y)                      # Convolutes each pixel

    print("Status: Completed!")

convolution(1)

new_img.save(f"Image Manipulation\Results\convolution_{round(time.time() * 1000)}.png") # Saves image and adds time in milliseconds into name

img.close()
new_img.close()