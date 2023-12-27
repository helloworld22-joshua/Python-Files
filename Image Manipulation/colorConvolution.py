import time
from PIL import Image

img = Image.open(r'Image Manipulation\garfield.png')
pix = img.load()

matrix = [[-0.25, 0, 0.25],
          [-0.5,  0, 0.5 ],
          [-0.25, 0, 0.25]]

def convolut(x, y):
    result = (0, 0, 0)                                                          # Sum of values of individual pixels
    skip = 1                                                                    # Percentage of skipped pixels outside of image. Starts at 100%

    for i in range(-1, 2):                                                      # Five by five square around pixel
        for j in range(-1, 2):
            if 0 <= y + i < img.size[1] and 0 <= x + j < img.size[0]:           # Makes sure square doesn't take values from outside the image
                result = tuple(map(lambda a, b: a + b * matrix[i + 1][j + 1], result, pix[x + j, y + i])) # Individual values of pixel multiplied by value of bell curve, added to sum
            else:
                skip += matrix[i + 1][j + 1]                                    # Adds value of skipped bell curve to total skipped value

    return tuple(map(lambda a: round(a * skip), result))                        # Sum is multiplied by total skipped value and rounded

print(convolut(0, 0))

""" new_img = Image.new(img.mode, img.size)                                         # Create a new image
new_pix = new_img.load()

for y in range(img.size[1]):

    if not y % 100: print(f"Progress: {round(y / img.size[1] * 100)}%")         # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        new_pix[x, y] = gaussianBlur(x, y)                                      # Set pixels to the manipulated pixels of the old image

print("Status: Completed!")

img.show() """

#img.save(f"Image Manipulation\Results\colorConvolution_{round(time.time() * 1000)}.png")

img.close()