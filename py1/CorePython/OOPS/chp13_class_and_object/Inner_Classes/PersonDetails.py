# name and age have one value
# date of birth consists of 3 values : d,m,y
# thus Dob is another class within the PersonDetails class

class PersonDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display1(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

    class Dob:
        def __init__(self):
            print("enter date :")
            self.dd = input()
            print("enter month :")
            self.mm = input()
            print("enter year :")
            self.yy = input()

        def display2(self):
            print("Date of Birth : {} / {} / {}".format(self.dd, self.mm, self.yy))


Person1 = PersonDetails("Aditya", 19)
Person1.display1()

DOB1 = Person1.Dob
DOB1.display2()
