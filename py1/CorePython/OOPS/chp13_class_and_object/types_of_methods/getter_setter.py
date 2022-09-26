class Student:

    # constructor which is an instance method :
    def __init__(self):
        self.college = "KJSCE"

    # setter method :
    def setName(self, name):
        self.name = name

    # getter method :
    def getName(self):
        return self.name

    # setter method :
    def setMarks(self, marks):
        self.marks = marks

    # getter method :
    def getMarks(self):
        return self.marks

    # getter method :
    def getCollege(self):
        return self.college


n = int(input("Enter the number of students : "))
i = 0
while i < n:
    # creating instance of the class
    s = Student()

    name = input("Enter the name : ")
    marks = int(input("Enter the marks : "))

    s.setName(name)
    s.setMarks(marks)

    print("hello ", s.getName())
    print("your marks are ", s.getMarks())
    print("-------------------------------------")
    i += 1
