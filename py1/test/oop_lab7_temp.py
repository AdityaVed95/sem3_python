class Base1:
    def __init__(self):
        self.str1 = "I am in Base1"
        print("This is Base1")


class Base2:
    def __init__(self):
        self.str2 = "I am in Base2"
        print("This is Base2")


class Derived1(Base1, Base2):
    def __init__(self):
        #
        # super().__init__()
        self.str3 = "I am in Derived1"
        Base1.__init__(self)
        Base2.__init__(self)
        print("This is Derived1 class")

    def display_all(self):
        print(self.str1)
        print(self.str2)
        print(self.str3)


derived_object = Derived1()
derived_object.display_all()
