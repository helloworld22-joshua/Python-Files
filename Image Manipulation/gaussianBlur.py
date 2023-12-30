import time
from PIL import Image

img = Image.open(r"Image Manipulation\Source\garfield.png")
pix = img.load()

bell_curve = [[0.003, 0.013, 0.022, 0.013, 0.003],
              [0.013, 0.060, 0.098, 0.060, 0.013],
              [0.022, 0.098, 0.162, 0.098, 0.022],
              [0.013, 0.060, 0.098, 0.060, 0.013],
              [0.003, 0.013, 0.022, 0.013, 0.003]]

reverse_bell_curve = [[0.162, 0.098, 0.060, 0.098, 0.162],
                      [0.098, 0.022, 0.013, 0.022, 0.098],
                      [0.060, 0.013, 0.003, 0.013, 0.060],
                      [0.098, 0.022, 0.013, 0.022, 0.098],
                      [0.162, 0.098, 0.060, 0.098, 0.162]]

inverted_bell_curve = [[0.089, 0.054, 0.033, 0.054, 0.089],
                       [0.054, 0.012, 0.007, 0.012, 0.054],
                       [0.033, 0.007, 0.002, 0.007, 0.033],
                       [0.054, 0.012, 0.007, 0.012, 0.054],
                       [0.089, 0.054, 0.033, 0.054, 0.089]]

def gaussianBlur(x, y):
    result = (0, 0, 0)                                                          # Sum of values of individual pixels
    skip = 1                                                                    # Percentage of skipped pixels outside of image. Starts at 100%

    for i in range(-2, 3):                                                      # Five by five square around pixel
        for j in range(-2, 3):
            if 0 <= y + i < img.size[1] and 0 <= x + j < img.size[0]:           # Makes sure square doesn't take values from outside the image
                result = tuple(map(lambda a, b: a + b * bell_curve[i + 2][j + 2], result, pix[x + j, y + i])) # Individual values of pixel multiplied by value of bell curve, added to sum
            else:
                skip += bell_curve[i + 2][j + 2]                                # Adds value of skipped bell curve to total skipped value

    return tuple(map(lambda a: round(a * skip), result))                        # Sum is multiplied by total skipped value and rounded

new_img = Image.new(img.mode, img.size)                                         # Create a new image
new_pix = new_img.load()

for y in range(img.size[1]):

    if not y % 100: print(f"Progress: {round(y / img.size[1] * 100)}%")         # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        new_pix[x, y] = gaussianBlur(x, y)                                      # Set pixels to the manipulated pixels of the old image

print("Status: Completed!")

new_img.save(f"Image Manipulation\Results\gaussianBlur_{round(time.time() * 1000)}.png")  # Saves image and adds time in milliseconds into name

img.close()
new_img.close()

""" How I got the inverted bell curve:
total = 0
inverted_bell_curve = [[0] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        inverted_bell_curve[i][j] = round(reverse_bell_curve[i][j] / 1.815, 3)
        total += reverse_bell_curve[i][j] / 1.815

print(total, inverted_bell_curve) """