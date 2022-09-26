from abc import ABC, abstractmethod


# here the SuperClass is an interface :
# it is not possible to create an object of an interface or of an abstract class


class SuperClass(ABC):

    def meth(self):
        print("in meth")

    @abstractmethod
    def meth1(self):
        pass

    @abstractmethod
    def meth2(self):
        pass


class Sub1(SuperClass):
    def meth1(self):
        print("in meth1")

    def meth2(self):
        print("in meth2")


sub1 = Sub1()
sub1.meth1()
sub1.meth2()

sup1 = SuperClass()
# sup1.meth1()
# sup1.meth2()
