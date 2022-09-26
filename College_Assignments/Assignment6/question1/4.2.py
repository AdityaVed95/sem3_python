class Student:
    roll_num = 101
    name = "Joseph"

    def display(self):
        print(self.roll_num, self.name)

    def modify(self):
        self.roll_num = 102
        self.name = "John"

    # def __setattr__(self, key, value):


st1 = Student()
st1.display()

st2 = Student()
st2.display()

st1.modify()
st1.display()
st2.display()
