class Class1:
    def __init__(self):
        self.name = "AV"
        self.id = 100
        self.salary = 10000000

    def display(self):
        print("Name : {} \nID : {} \nSalary : {}".format(self.name, self.id, self.salary))


class Class2:

    def __init__(self):
        print("Hello there in Class2 ")

    @staticmethod
    def mymethod(emp):  # acts neither on class variable or instance varaible of Class2
        emp.salary += 100000
        emp.display()

    @staticmethod
    def calc(x, n):
        print("{} to the power of {} is {}".format(x, n, x ** n))


e = Class1()

Class2.mymethod(e)  # passing an instance of class1 as parameter to a static method of class2
# by passing the instance as the parameter , we are passing all the attributes and methods to Class2
# note : the constructor of Class2 is not executed on calling the static method of Class2
# constructor is executed only on creating an instance of class2


# pass some values from outside the fxn and perform calculation in the static method
# static methods are used when the class or instance variables of that particular class are not disturbed

Class2.calc(10, 3)
