class Student:
    roll_num = 101
    name = "Joseph"

    @classmethod
    def display(cls):
        print(cls.roll_num, cls.name)


st = Student()
st.display()
