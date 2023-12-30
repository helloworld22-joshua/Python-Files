import time
from PIL import Image

img = Image.open(r"Image Manipulation\Source\wild_anza.png")
pix = img.load()

new_img = Image.new(img.mode, img.size)
new_pix = new_img.load()

strength = 5                                                    # How far the values move from the original pixel

for y in range(img.size[1]):

    if not y % 100 or (y + 1) / img.size[1] == 1:
        print(f"Progress: {round(y / img.size[1] * 100)}%")
    
    for x in range(img.size[0]):
        r, g, b = pix[x, y]                                     # Current pixel

        if x - strength >= 0:
            _r, _g, _b = pix[x - strength, y]                   # New pixel on the left
            new_pix[x - strength, y] = (r, _g, _b)              # Change value of red to the red value of current pixel

        if x + strength < img.size[0]:
            _r, _g, _b = pix[x + strength, y]                   # New pixel on the right
            new_pix[x + strength, y] = (_r, _g, b)              # Change value of blue to the blue value of current pixel

new_img.save(f"Image Manipulation\Results\chromaticAberration_{round(time.time() * 1000)}.png")

img.close()
new_img.close()