class Student:
    def __init__(self, roll_num, name, marks):
        self.roll_num = roll_num
        self.name = name
        self.marks = marks

    def displaying(self):
        print("Roll Number : {} , Name : {} , Marks : {}".format(self.roll_num, self.name, self.marks))
