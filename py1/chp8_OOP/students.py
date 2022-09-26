class Student:
    # class variable :
    x = 343

    def __init__(self):  # purpose of __init__ method : declare and initialize the instance variables of the class :

        # protected attributes or instance variables
        self._id = 10
        self._name = "Raju"

    def display(self):
        # this method is displaying instance variables :
        print(self._id)
        print(self._name)
        print(x)

    def name(self):
        print(self._name)
        print("Hello")


if __name__ == "__main__":
    s1 = Student()

    print(s1._id)
    print()

    print(s1._name)
    print()

    s1.display()
    print()

    s1.name()
    print()

# Note :
# Class = Noun = prototype
# Attributes/characteristics/features  = variables = adjectives
# Behaviours = methods = verbs

#
# Instance variables: If the value of a variable varies from object to object, then such
# variables are called instance variables. For every object, a separate copy of the
# instance variable will be created.
# Class Variables: A class variable is a variable that is declared inside of class, but
# outside any instance method or __init__() method.
