from abc import ABC, abstractmethod


class BaseClass(ABC):

    def __init__(self):
        print("..in BaseClass constructor..")
        self.color = "grey"

    @abstractmethod
    def fxn1(self):
        pass

    @abstractmethod
    def fxn2(self):
        pass


class DerivedClass1(BaseClass):

    def setColor1(self):
        self.color = "Blue"

    def fxn1(self):
        print("This is fxn1 in DerivedClass1")

    def fxn2(self):
        print("This is fxn2 in DerivedClass1")


class DerivedClass2(BaseClass):

    def __init__(self):
        self.color = "Black"

    def fxn1(self):
        print("This is fxn2 in DerivedClass2")

    def fxn2(self):
        print("This is fxn2 in DerivedClass2")


obj_dc1 = DerivedClass1()
print(obj_dc1.color)

obj_dc2 = DerivedClass2()
print(obj_dc2.color)
