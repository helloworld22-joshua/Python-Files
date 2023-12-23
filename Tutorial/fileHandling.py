import time

file = open('Tutorial/example.txt', 'r')
content = file.read()
file.close()

file = open(f"Convolution/example_{round(time.time() * 1000)}.txt", "x")
file.write(content)
file.close()

""" Alternative:
with open(f"Convolution/example_{round(time.time() * 1000)}.txt", "x") as file:
    file.write(content)
    file.close() """