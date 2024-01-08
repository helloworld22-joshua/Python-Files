import time, random
from PIL import Image

img = Image.open(r"Image Manipulation\Source\mühle_warnstedt.jpg")
pix = img.load()

for y in range(img.size[1]):
    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")

    #for x in range(round(img.size[0] / 2)):
    for x in range(img.size[0]):
        r, g, b = pix[x, y]

        total = r + g + b

        """ if total:
            green = g / total
        else:
            green = 1 """

        green = g / total if total else 1

        g = min(255, round(g + green ** 2))

        pix[x, y] = (r, g, b)
else:
    print("Status: Completed!")

#img.save(f"Image Manipulation\Results\saturation_{round(time.time() * 1000)}.png")
img.show()
img.close()

""" r, g, b = pix[x, y]

        total = r + g + b

        a = round(total / 3)

        pix[x, y] = (r, a, a) """