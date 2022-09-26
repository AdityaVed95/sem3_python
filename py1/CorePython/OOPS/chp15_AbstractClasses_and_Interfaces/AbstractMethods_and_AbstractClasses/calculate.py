from abc import ABC, abstractmethod
import math


class AbstractClass(ABC):

    @abstractmethod
    def calculate(self, x):  # non-concrete method : behaviour is different for different
        # objects of the class (if it is an abstract method)

        pass

    def print_hello(self):  # concrete method , behaviour is same for all the objects of the class
        print("Hello")


class SubClass1(AbstractClass):
    def calculate(self, x):
        print("Square value is : ", x * x)


class SubClass2(AbstractClass):
    def calculate(self, x):
        print("Square root value is : ", math.sqrt(x))


class SubClass3(AbstractClass):
    def calculate(self, x):
        print("Cube value is : ", x ** 3)


object1 = SubClass1()
object1.calculate(100)

object2 = SubClass2()
object2.calculate(100)

object3 = SubClass3()
object3.calculate(100)
