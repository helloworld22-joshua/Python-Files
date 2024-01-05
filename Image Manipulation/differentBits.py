import time
from PIL import Image

img = Image.open(r"Image Manipulation\Source\mühle_warnstedt.jpg")
pix = img.load()

bits = 2

b = round(256 / (bits ** 2))

for y in range(img.size[1]):
    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")

    for x in range(img.size[0]):
        pix[x, y] = tuple(round(i / b) * b for i in pix[x, y])
else:
    print("Status: Completed!")

img.save(f"Image Manipulation\Results\differentBits_{round(time.time() * 1000)}.png")

img.close()