import time, random
from PIL import Image

img = Image.open(r"Image Manipulation\Source\garfield.png")
pix = img.load()

max_noise = 100

def brightnessNoise(x, y, max_noise):
    randInt = random.randint(-max_noise, max_noise)

    return tuple(item + randInt for item in pix[x, y])

def colorNoise(x, y, max_noise):
    return tuple(item + random.randint(-max_noise, max_noise) for item in pix[x, y])

for y in range(img.size[1]):

    if not y % 100: print(f"Progress: {round(y / img.size[1] * 100)}%")         # Status report every 100 pixels on the y-axis

    for x in range(img.size[0]):
        pix[x, y] = brightnessNoise(x, y, max_noise)

print("Status: Completed!")

img.save(r"Image Manipulation\Results\noise_" + f"{round(time.time() * 1000)}.png")

img.close()