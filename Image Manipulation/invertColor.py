import time
from PIL import Image

img = Image.open(r"Image Manipulation\Source\lava_ship.png")
pix = img.load()

invertR = True
invertG = False
invertB = False

for y in range(img.size[1]):

    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")             # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        r, g, b = pix[x, y]

        if invertR: r = 255 - r
        if invertG: g = 255 - g
        if invertB: b = 255 - b

        pix[x, y] = (r, g, b)
else:
    print("Status: Completed!")

img.save(f"Image Manipulation\Results\invertColor_{round(time.time() * 1000)}.png")

img.close()