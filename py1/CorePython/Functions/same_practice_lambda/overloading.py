def adding_int(a, b, c=0, d=0):  # method overloading
    print(a + b + c + d)


def adding_string(a, b, c=""):
    print(a + b + c)


def adding_both(a, b):
    print(a + b)  # operator overloading


adding_int(10, 20)
adding_string("A", "V")
adding_both(30, 20)
adding_both("Go", "There")

# we can not create two methods with the same name and different number of
# parameters in python but this is possible in java
