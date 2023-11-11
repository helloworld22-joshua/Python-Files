import turtle, colorsys

t = turtle.Pen()

turtle.bgcolor('black')

def resetScreen():
    turtle.clearscreen()
    turtle.bgcolor('black')
    t.home()

# My code

FULL_CIRCLE = 360

for x in range(FULL_CIRCLE):
    hue = x / FULL_CIRCLE
    t.pencolor(colorsys.hsv_to_rgb(hue, 1, 1))
    t.width(x / 25)
    t.forward(x)
    t.left(70)

resetScreen()

for x in range(FULL_CIRCLE):
    t.pencolor('white')
    t.width(x / 50)
    t.forward(x)
    t.left(120 - x / 4)

resetScreen()

# Example

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)