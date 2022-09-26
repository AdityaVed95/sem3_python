# to pass the member of class1 to class2 :
from Class2_main import Class2


class Class1:
    def __init__(self):
        self.name = "AV"
        self.id = 100
        self.salary = 10000000

    def display(self):
        print("Name : {} \nID : {} \nSalary : {}".format(self.name, self.id, self.salary))


e = Class1()
e.display()

# Class2.hello()
c2 = Class2()
c2.hello()

Class2.mymethod(e)
