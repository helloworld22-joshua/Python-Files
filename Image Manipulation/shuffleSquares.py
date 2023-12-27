import time, random, math
from PIL import Image
from fractions import Fraction

img = Image.open(r'Image Manipulation\lava_ship.png')
pix = img.load()

new_img = Image.new(img.mode, img.size)
new_pix = new_img.load()

aspect_ratio = Fraction(img.size[0], img.size[1])                   # Get aspect ratio using resolution (E.g.: 1920 / 1080 = 16 / 9)

ar_numerator = aspect_ratio.numerator                               # Top number of fraction (16)
ar_denominator = aspect_ratio.denominator                           # Bottom number of fraction (9)

square_size = int(img.size[0] / ar_numerator)                       # Size of squares is horizontal width of image devided by numerator (1920 / 16 = 120)
square_amount = ar_numerator * ar_denominator                       # Total amount of squares by multiplying numerator and denominator (16 * 9 = 144)

rand_order = random.sample(range(square_amount), square_amount)     # Rearange order of squares by generating random unique numbers (0 - 143)

def shuffleSquares(square):
    squareX_1 = square % ar_numerator * square_size                 # The squares top left corner on the x-axis (E.g. 18th square: 18 % 16 = 2. 2 * 120 = 240)
    squareY_1 = math.floor(square / ar_numerator) * square_size     # The squares top left corner on the y-axis (18 / 16 ≈ 1. 1 * 120 = 120)

    squareX_2 = rand_order[square] % ar_numerator * square_size     # Same thing but the square is chosen from the random list
    squareY_2 = math.floor(rand_order[square] / ar_numerator) * square_size

    for y in range(square_size):
        for x in range(square_size):
            new_pix[squareX_1 + x, squareY_1 + y] = pix[squareX_2 + x, squareY_2 + y]   # Starts at the top left corner of the square and goes to the bottom right replacing all pixels

for square in range(square_amount):                                 # Iterates each square
    shuffleSquares(square)

    if not square % 10 or (square + 1) / square_amount == 1:        # Prints progress every ten iterations or when complete
        print(f"Progress: {round((square + 1) / square_amount * 100)}%")
else:
    print("Status: Completed!")

new_img.save(f"Image Manipulation\Results\shuffleSquares_{round(time.time() * 1000)}.png")  # Saves image and adds time in milliseconds into name

img.close()
new_img.close()