import time, random
from PIL import Image

img = Image.open(r"Image Manipulation\Source\wild_anza.png")
pix = img.load()

length = 500

def combine(old_pix, new_pix, ratio):
    return tuple(map(lambda a, b: round(a * ratio + b * (1 - ratio)), old_pix, new_pix))

for y in range(img.size[1]):

    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")

    half = round(img.size[0] *  (1 - y / img.size[1]) + length / 2)

    for x in range(half):
        if x >= img.size[0]:
            continue

        r, g, b = pix[x, y]

        bw = round((r + b + g) / 3)

        new_pix = (bw, bw, bw)

        if x >= half - length:
            ratio = (half - x) / length
            pix[x, y] = tuple(map(lambda a, b: round(a * ratio + b * (1 - ratio)), new_pix, pix[x, y]))
            continue

        pix[x, y] = new_pix
else:
    print("Status: Completed!")

img.save(r"Image Manipulation\Results\cutItInHalf_" + f"{round(time.time() * 1000)}.png")

img.close()