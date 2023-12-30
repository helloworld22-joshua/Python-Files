import time, math
from PIL import Image

img = Image.open(r"Image Manipulation\Source\forza.png")
pix = img.load()

EV = -2

for y in range(img.size[1]):
    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")             # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        #pix[x, y] = tuple(round(math.sqrt(i) * 16) for i in pix[x, y])
        pix[x, y] = tuple(min(round(2 ** EV * i), 255) for i in pix[x, y])
else:
    print("Status: Completed!")

#img.save(f"Image Manipulation\Results\exposure_{round(time.time() * 1000)}.png")
img.show()
img.close()