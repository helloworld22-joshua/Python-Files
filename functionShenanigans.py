from typing import overload, Union

from mymodule import me                                                     # You can choose to import only parts from a module
print(me["name"])

import mymodule                                                             # Import the module named mymodule
mymodule.greeting("module")

def my_function1(*args):                                                    # If the number of arguments is unknown, add a * before the parameter name. The parameter becomes a tuple.
    for arg in args:
        print(arg)

my_function1(1, 2, 3)

def my_function2(**kwargs):                                                 # Similar to one * except that the parameter becomes a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function2(name = "Joshua", age = 17, occupation = "Programmer")

@overload                                                                   # Multiple implementations functions that have with different argument types
def square(x: int) -> int:                                                  # The arrow -> is used to indicate what type of value the function is expected to return
    pass

@overload
def square(x: float) -> float:                                              # The colon : means it only accepts specific data types as an argument
    pass

def square(x: Union[int, float]) -> Union[int, float]:                      # Union means it can accept several data types as valid arguments
    if isinstance(x, int):                                                  # Checks if a variable is a certain data type
        return x * x
    elif isinstance(x, float):
        return x + x
    else:
        return "Unspecified data type!"

print(square(5))
print(square(2.3))
print(square("1"))