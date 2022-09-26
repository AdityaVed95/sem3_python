# this is the main program in which we create an object of the inner class inside the constructor of
# the outer class

class Person:
    def __init__(self):
        self.name = "Aditya"
        self.db = self.Dob()  # creating inner class ka object inside the outer class and assigning
        # it to an instance variable
        # this statement seems like db is object of Dob class

    def display1(self):
        print("Name : ", self.name)

    class Dob:
        def __init__(self):
            self.dd = 17
            self.mm = 11
            self.yy = 2002

        def display2(self):
            print("Dob : {} / {} / {}".format(self.dd, self.mm, self.yy))


Person1 = Person()
Person1.display1()

Date1 = Person1.db
Date1.display2()  # this statement also seems like db is an object of Dob class
