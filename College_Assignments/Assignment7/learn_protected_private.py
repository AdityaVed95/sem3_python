# protected members cannot be accessed from outside the class but
# they can be accessed by its sub class

# private members can strictly be accessed only from inside the class

class Person(object):
    def __init__(self, name, age, hobby):
        self._name = name  # protected attribute
        self.__age = age  # private attribute
        self.hobby = hobby  # public attribute


p1 = Person("user1", 25, "sports")
print(p1.hobby)


# next 3 lines generate errors
# print(p1._name)
# print(p1.name)
# print(p1.age)


class Employee(Person):
    def __init__(self, name, age, hobby, sal, position):
        Person.__init__(self, name, age, hobby)
        self.salary = sal  # public attribute
        self.position = position  # public attribute

    def display(self):
        print(self.hobby)
        print(self.salary)
        print(self.position)
        print(self._name)
        # the next line generates error because:
        # age is a private attribute and private attributes cannot be
        # accessed by sub class also
        # print(self.__age)


e1 = Employee("user2", 45, "read", 1000, "head")
print(e1.hobby)
e1.display()
print(e1._Employee__age)
