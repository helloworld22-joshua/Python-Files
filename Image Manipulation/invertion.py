import time
from PIL import Image

img = Image.open(r"Image Manipulation\Source\garfield.png")
pix = img.load()

for y in range(img.size[1]):

    if not y % 100: print(f"Progress: {round(y / img.size[1] * 100)}%")             # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        pix[x, y] = tuple(255 - item for item in pix[x, y])

print("Status: Completed!")

img.save(f"Image Manipulation\Results\invertion_{round(time.time() * 1000)}.png")

img.close()