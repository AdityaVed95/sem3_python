class Duck:
    def talk(self):
        print("Quack Quack!")


class Human:
    def talk(self):
        print("Hello there")


class Cat:
    def maw(self):
        print("meow")


class Dog:
    def bark(self):
        print("bav bav")


def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()  # we do not need the type of the object to invoke a method of the object
    # according to the object passed , that method of that object will get called respectively

    elif hasattr(obj, 'maw'):
        obj.maw()

    elif hasattr(obj, 'bark'):
        obj.bark()


def only_talk(obj):
    obj.talk()


d1 = Duck()
h1 = Human()
c1 = Cat()
dog1 = Dog()

# these 4 demonstrate strong typing
call_talk(d1)
call_talk(h1)
call_talk(c1)
call_talk(dog1)

# these two demonstrate duck typing :
only_talk(h1)
only_talk(d1)

# we need not define the type of object when we call the talk method
# if the object is of type human then the talk method of human class is called
# and if the object is of type duck then the talk method of duck class is called
# thus this is polymorphism as the name of both the methods is talk but one method is of human
# class and the other is of duck class and method of which class to call is simply dependant on
# the type of object
