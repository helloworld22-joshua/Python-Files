import time
from PIL import Image

img = Image.open(r'Image Manipulation\garfield.png')
pix = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        pix[x, y] = tuple(255 - item for item in pix[x, y])

img.save(f"Image Manipulation\invertion_{round(time.time() * 1000)}.png")

img.close()