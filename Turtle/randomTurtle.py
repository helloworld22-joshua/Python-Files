import turtle, random, colorsys

t = turtle.Pen()

color = 0

t.fillcolor(colorsys.hsv_to_rgb(color, 1, 1))
t.begin_fill()

for i in range(1000):
    t.fd(random.randrange(100))
    t.lt(random.randrange(360))

    if any(abs(value) > 200 for value in t.pos()):
        t.home()
        t.end_fill()

        if (color > 360):
            color -= 360
        else:
            color += 18

        t.fillcolor(colorsys.hsv_to_rgb(color / 360, 1, 1))
        t.begin_fill()

    print(t.pos())