import time
from PIL import Image

img = Image.open(r"Image Manipulation\Source\forza.png")
pix = img.load()

new_img = Image.new(img.mode, img.size)                                         # Create a new image
new_pix = new_img.load()

def verticalShake(amount, modulo):
    for y in range(img.size[1]):

        if not y % 100: print(f"Progress: {round(y / img.size[1] * 100)}%")

        for x in range(img.size[0]):
            if x % modulo:
                new_pix[x, y] = pix[x, y - amount]
            else:
                if y + amount >= img.size[1]:
                    new_pix[x, y] = pix[x, amount]
                else:
                    new_pix[x, y] = pix[x, y + amount]

    print("Status: Completed!")


def horizontalShake(amount, modulo):
    for y in range(img.size[1]):

        if not y % 100: print(f"Progress: {round(y / img.size[1] * 100)}%")    # Status report every 100 pixels on the y-axis

        for x in range(img.size[0]):
            if y % modulo:
                new_pix[x, y] = pix[x - amount, y]
            else:
                if x + amount >= img.size[0]:
                    new_pix[x, y] = pix[amount, y]
                else:
                    new_pix[x, y] = pix[x + amount, y]
    
    print("Status: Completed!")


horizontalShake(4, 2)

new_img.save(f"Image Manipulation\Results\shake_{round(time.time() * 1000)}.png")  # Saves image and adds time in milliseconds into name

img.close()
new_img.close()