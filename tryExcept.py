try:                                            # Executes this block of code
    print(notARealVaribale)
except NameError:                               # If this specific error occurs
    print("Error: Variable is not defined!")
except:                                         # If any non-specific error occurs
    print("Error!")
else:                                           # If no error occurs
    print("No error")
finally:                                        # Executes at the end regardless of an error or not
    print("Done")

aNumber = 1

if not type(aNumber) is str:
    raise TypeError("You need a string!")