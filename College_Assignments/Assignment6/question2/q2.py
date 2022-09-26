class Student:

    # assuming that all the marks(marks1,marks2,marks3,marks4) are out of 100

    def __init__(self):
        self.roll_number = None
        self.marks1 = None
        self.marks2 = None
        self.marks3 = None
        self.marks4 = None

    def set_rollnum(self, rollnum):
        self.roll_number = rollnum

    def set_marks1(self, marks1):
        self.marks1 = marks1

    def set_marks2(self, marks2):
        self.marks2 = marks2

    def set_marks3(self, marks3):
        self.marks3 = marks3

    def set_marks4(self, marks4):
        self.marks4 = marks4

    def get_rollnum(self):
        print("Roll number is :", self.roll_number)

    def get_marks1(self):
        print("Marks in 1st subject is: ", self.marks1)

    def get_marks2(self):
        print("Marks in 2nd subject is: ", self.marks2)

    def get_marks3(self):
        print("Marks in 3rd subject is: ", self.marks3)

    def get_marks4(self):
        print("Marks in 4th subject is: ", self.marks4)

    def get_total_marks(self):
        total_marks = self.marks1 + self.marks2 + self.marks3 + self.marks4
        print("Total marks obtained are :", total_marks)

    def get_percentage(self):
        avg_marks = (self.marks1 + self.marks2 + self.marks3 + self.marks4) / 4
        percentage = avg_marks
        print("Percentage scored is : ", percentage)

