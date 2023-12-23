def myFunction(count):
    print(count)
    count += 1
    if (count < 10): myFunction(count)

myFunction(0)