import time
from PIL import Image

img = Image.open(r'Image Manipulation\forza.png')
pix = img.load()

for y in range(img.size[1]):
    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")             # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        r, g, b = pix[x, y]

        maximum = max(r, g, b)
        minimum = min(r, g, b)

        pix[x, y] = (minimum, maximum, maximum)
else:
    print("Status: Completed!")

img.save(r"Image Manipulation\Results\bwWithColor_" + f"{round(time.time() * 1000)}.png")

img.close()