try:
    print("Welcome to try block")
    print(x)
    print("I am never executed")
except NameError:
    print("Welcome to except block")
    print("please specify x")
    print()
else:
    print("No exception has occured if this is executed")
    print()
finally:
    print("I am always executed irrespective of exception occurrence")

