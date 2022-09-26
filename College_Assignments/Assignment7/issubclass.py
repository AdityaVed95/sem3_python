class Person:
    pass


class Mammal:
    pass


class Insect:
    pass


class Employee(Person, Mammal):
    pass


x = issubclass(Employee, (Person, Mammal, Insect))
print(x)
