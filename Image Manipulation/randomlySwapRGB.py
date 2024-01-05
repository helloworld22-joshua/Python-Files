import time, random
from PIL import Image

img = Image.open(r"Image Manipulation\Source\mühle_warnstedt.jpg")
pix = img.load()

for y in range(img.size[1]):
    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")

    for x in range(img.size[0]):
        pix[x, y] = tuple(random.sample(pix[x, y], len(pix[x, y])))
else:
    print("Status: Completed!")

img.save(r"Image Manipulation\Results\randomlySwapRGB_" + f"{round(time.time() * 1000)}.png")

img.close()