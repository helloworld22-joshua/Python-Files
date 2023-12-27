import time
from PIL import Image

img1 = Image.open(r'Image Manipulation\forza.png')
img2 = Image.open(r'Image Manipulation\wild_anza.png')

pix1 = img1.load()
pix2 = img2.load()

ratio = 0.5

def combine(x, y, ratio):
    return tuple(map(lambda a, b: round(a * ratio + b * (1 - ratio)), pix1[x, y], pix2[x, y]))

for y in range(img1.size[1]):

    if not y % 100: print(f"Progress: {round(y / img1.size[1] * 100)}%")             # Status report every 100 pixels on the y-axis

    for x in range(img1.size[0]):
        pix1[x, y] = combine(x, y, ratio)

print("Status: Completed!")

img1.save(f"Image Manipulation\Results\combine_{round(time.time() * 1000)}.png")

img1.close()
img2.close()