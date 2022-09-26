import math


class Sample:
    @staticmethod
    def calculate(x):
        return math.sqrt(x)


num = float(input("Enter number: "))

result = Sample.calculate(num)
print("square root of {}  is {:.2f} : ".format(num, result))
