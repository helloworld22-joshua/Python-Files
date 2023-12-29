import time
from PIL import Image

img = Image.open(r'Image Manipulation\forza.png')
pix = img.load()

detail = 64

def colorContrast(pixel):
    pixel = tuple(round(i / detail) for i in pixel)                             # Devides the values to make them smaller so variation is more likely

    maximum = max(pixel)                                                        # Gets biggest value

    if all(maximum == i and i < 256 / detail / 2 for i in pixel): return (0, 0, 0)    # If all values are the same and less than half of the maximum value, they'll be black

    new_pix = [0, 0, 0]

    for i in range(len(pixel)):                                                 # For every value in a pixel
        if pixel[i] == maximum:                                                 # If the value is equal to the biggest,
            new_pix[i] = 255                                                    # it'll have the maximum value a pixel can have

    return tuple(new_pix)

for y in range(img.size[1]):
    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")

    for x in range(img.size[0]):
        pix[x, y] = colorContrast(pix[x, y])
else:
    print("Status: Completed!")

img.save(f"Image Manipulation\Results\colorContrast_{round(time.time() * 1000)}.png")

img.close()