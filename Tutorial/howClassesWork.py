class Human:
    def __init__(self, name, age):                  # The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name                            # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.age = age
        print(self.name + " was created.")

    def __str__(self):                              # The __str__() function controls what should be returned when the class object is represented as a string.
        return f"{self.name} ({self.age})"

    def printAge(x):                                # Methods in objects are functions that belong to the object.
        print(f"I am {x.age} years old!")

class Worker(Human):                                # Create a class named Worker, which will inherit the properties and methods from the Human class.
    def __init__(self, name, age):                  # The child's __init__() function overrides the inheritance of the parent's __init__() function. To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__(name, age)
        self.occupation = "Programmer"

    def __del__(self):                              # The __del__() function is called once the class is being deleted.
        print(self.name + " was deleted.")

class Programmer(Worker):
    pass                                            # Use the pass keyword when you do not want to add any other properties or methods to the class.

person1 = Human("Joshua", 16)
print(person1)
person1.age = 17
person1.printAge()

person2 = Programmer("Martin", 22)
print("Occupation:", person2.occupation)

person3 = Worker("Albrecht", 27)
del person3

class MyNumbers:
    def __iter__(self):                             # The __iter__() method acts similar to the __init__(), you can do operations (initializing etc.), but must always return the iterator object itself.
        self.counter = 1
        return self

    def __next__(self):                             # The __next__() method also allows you to do operations, and must return the next item in the sequence.
        if self.counter >= 20: raise StopIteration
        x = self.counter
        self.counter += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

for x in range(5):
    print(next(myiter))

for x in myiter:
    print(x)