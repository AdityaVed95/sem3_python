class Sample:
    x = 10

    def __init__(self):
        self.y = 20

    def modify_inst(self):
        self.y = self.y + 1

    @classmethod
    def modify_class(cls):
        cls.x = cls.x + 1

        # this gives error : self.y = 100


s1 = Sample()
s2 = Sample()

print("s1.x is : ", s1.x)  # 10
print("s1.y is : ", s1.y)  # 20

s1.modify_inst()  # x = 11 , y = 30
print("after modify_inst : ")
print("s1.x is : ", s1.x)
print("Sample.x is : ", Sample.x)  # class name works because only one copy created for all the
# instances of the class
print("s1.y is : ", s1.y)

s1.modify_class()  # x =100 , y = 500
print("after modify_class : ")
print("s1.x is : ", s1.x)
print("s1.y is : ", s1.y)

print(id(Sample.x) == id(s1.x))
