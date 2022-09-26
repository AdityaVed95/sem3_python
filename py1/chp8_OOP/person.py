class Person:  # class
    # class variables :
    name = "aditya"
    age = 20

    # methods :
    def talk(cls):  # how to know whether we have to use cls or self (which one to use when)
        print("I can talk")
        # this gives error : print(name)

    def walk(self):
        print("I can walk")

    def study(self):
        print("I can study")

    # encapsulating class variables and methods inside a class : Encapsulation


p1 = Person()  # object of the class Person
p1.talk()  # calling the method of the object

# this gives error : print(name)
