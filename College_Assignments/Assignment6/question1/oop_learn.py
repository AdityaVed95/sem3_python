# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
    stream = 'cse'  # Class Variable

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

# print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(b.name)  # prints "Nerd"
print(a.roll)  # prints "1"
print(b.roll)  # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream)  # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'cse'

# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'mech'

# in this program :
# stream is a class variable
# we learn that for a particular instance of a class , the class variable remains like a class variable untill
# you modify the class variable from the instance namespace,
# when you try to modify the class variable from the instance namespace:
# then the class variable itself is not modified but for that instance of the class : a new variable with
# the same name as that of the class variable is created and now that variable is local for that instance
# of class only
# but this will not affect the actual value of the class variable

# in this case when we did a.stream = 'ece' then for the a object , stream was another local variable and no
# longer a class variable
# thus b.stream and CSStudent.stream still remained 'cse'

# and when we changed CSStudent.stream = 'mech' then it changed for b object but not for a object because :
# for b object it was still referring to the class variable but for the a object it was referring to the local
# variable that got created when we modified a.stream
