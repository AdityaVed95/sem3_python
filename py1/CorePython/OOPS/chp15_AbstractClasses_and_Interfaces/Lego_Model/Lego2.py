from abc import ABC, abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def fxn1(self):
        pass

    @abstractmethod
    def fxn2(self):
        pass


class DerivedClass1(BaseClass):

    def fxn1(self):
        print("This is fxn1 in DerivedClass1")

    def fxn2(self):
        print("This is fxn2 in DerivedClass1")

    def fxn3(self):
        print("This is fxn3 in DerivedClass1")


class DerivedClass2(BaseClass):

    def fxn1(self):
        print("This is fxn2 in DerivedClass2")

    def fxn2(self):
        print("This is fxn2 in DerivedClass2")


obj_dc1 = DerivedClass1()
obj_dc1.fxn3()

obj_dc2 = DerivedClass2()
