# class employee:
#     def __init__(self, name, sal):
#         self.__name = name  # private attribute
#         self.__salary = sal  # private attribute
#
# Python performs name mangling of private variables. Every member
# with double underscore will be changed to _object._class__variable.
# If so required, it can still be accessed from outside the class,
# but the practice should be refrained.

# e1=Employee("Bill",10000)
# print(e1._Employee__salary)
# e1._Employee__salary=20000
# print(e1._Employee__salary)


class Employee:
    def __init__(self, name, sal, hobby):
        self._name = name
        self._sal = sal
        self.hobby = hobby


e1 = Employee("User1", 1000, "sports")
print(e1.hobby)
print(e1._Employee_sal)

# doubt : acc to thoery the above line should not have given error
