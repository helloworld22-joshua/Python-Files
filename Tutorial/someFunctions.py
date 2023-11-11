def myLambda(n):
    return lambda a, b : (a + b) * n

def printListReverse(my_numbers):
    my_numbers.reverse()
    [print(x) for x in my_numbers]

def printListReverseAlternative(my_list):
    for x in range(len(my_list) - 1, -1, -1):
        print(my_list[x])

def reverseString(my_string):
    return my_string[::-1]

addAndDouble = myLambda(2)
myString = "Hello, World!"
myNumbers = [1, 2, 3, 4, 5]
myList = ["Mathe", "Englisch", "Deutsch"]

print(addAndDouble(5, 10))
print(reverseString(myString))
printListReverse(myNumbers)
printListReverseAlternative(myList)