import time
from PIL import Image

img = Image.open(r'Image Manipulation\garfield.png')
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


def convolution(multiplier):
    for _ in range(multiplier):                                     # Amount of repetitions (low values only)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pix[x, y] = convolut(x, y)                          # Convolutes each pixel

convolution(1)

img.save(f"Image Manipulation\img_{round(time.time() * 1000)}.png")        # Saves image and adds time in milliseconds into name








#print(im.format, im.size, im.mode)

""" for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y] == (252, 166, 172, 255):
            pix[x, y] = (255, 0, 0)

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if x % 2:
            pix[x, y] = (0, 0, 0) """