class Student:
    x = 343

    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self._age = age  # variables whose names start with and underscore are protected variables in python


# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1._age)

# create second object
s2 = Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2._age)

print(s1.x)
print(s2.x)

print(id(s1.x))
print(id(s2.x))
print(id(s1.name))
print(id(s1._age))
print(id(s2.name))
print(id(s2._age))

# note that the id of the instance variables are different while the id of the
# class variables is the same for each object
# thus class varaibles are shared between multiple objects while
# each object has a unique instance variable
