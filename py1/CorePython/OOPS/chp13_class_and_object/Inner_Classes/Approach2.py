class Person:
    def __init__(self):
        self.name = "Aditya"

    def display1(self):
        print("Name is : ", self.name)

    class Dob:
        def __init__(self):
            self.dd = 17
            self.mm = 11
            self.yy = 2002

        def display2(self):
            print("DOB is : {} / {} / {}".format(self.dd, self.mm, self.yy))


Person1 = Person()
Person1.display1()

InnerObj1 = Person().Dob()
InnerObj1.display2()
print(InnerObj1.yy)
