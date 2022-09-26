class Student:
    college = "KJSCE"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display1(self):
        print(self.name)
        print(self.id)

    @classmethod
    def display2(cls):
        print(cls.college)


def display(acc_obj):
    acc_obj.display1()
    acc_obj.display2()


s1 = Student("name1", 10)
print(s1.name)
print(s1.id)
print()
display(s1)
