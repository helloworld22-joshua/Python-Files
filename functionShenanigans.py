from typing import overload, Union

""" def my_function1(*args):                                                # If the number of arguments is unknown, add a * before the parameter name. The parameter becomes a tuple.
    for arg in args:
        print(arg)

my_function1(1, 2, 3)

def my_function2(**kwargs):                                             # Similar to one * except that the parameter becomes a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function2(name = "Joshua", age = 17, occupation = "Programmer") """


""" def my_function4(x: Union[int, float]) -> int:
    return int(x)

print(my_function4(42))
print(my_function4(3.14))

def my_function5(x: Union[int, float]):
    return x + ""

print(my_function5(42))
print(my_function5(3.14)) """


""" @overload
def my_function3(x: None) -> None:
    pass

@overload
def my_function3(x: int) -> tuple[int, str]:
    pass

@overload
def my_function3(x: bytes) -> str:
    pass

def my_function3(x):
    return x

print(my_function3(42))
print(my_function3(3.14))
print(my_function3("Python")) """