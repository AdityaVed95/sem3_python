class Hello(object):  # this is the same as : class Hello():
    pass


# object represents the base class name from where all classes in python are derived
# object in parentheses  is implied if it is not written

class Student:

    # both the methods are instance methods because self is one of their parameter, and thus
    # they know the location of instance in the heap memory

    # init method is the constructor , this method is called as soon as the instance of a
    # class is created , purpose of this method is to initialise the instance variables as soon
    # as instance of class is created

    def __init__(self):
        # instance variables :
        self.name = "AV"
        self.age = 20
        self.marks = 100
        print("id of self in init is :", id(self))

    # talk method gets the memory address of the instance variables from the self :
    def talk(self):
        print("i am ", self.name)
        print("my age is ", self.age)
        print("my marks is ", self.marks)
        print("id of self in talk is :", id(self))


s1 = Student()  # s1 contains the memory address of the instance
# inside the parenthesis of Student() are the parameters to the __init__ method
# here it is empty , thus no parameters passed to the __init__ method


print("id of s1 is : ", id(s1))  # id of s1 is the address of the memory allocated to the instance s1
s1.talk()

# Note : id(self) is same as the id(s1)

print()
print(s1)


class Student2:

    def __init__(self, n="", a=20, m=0):  # "" , 20 , 0  are the default values of the __init__
        # method if nothing is passed while creating the instance then these default values are assumed

        # instance variables :
        self.name = n
        self.age = a
        self.marks = m
        print("id of self in init is :", id(self))

        # talk method gets the memory address of the instance variables from the self :

    def talk(self):
        print("i am ", self.name)
        print("my age is ", self.age)
        print("my marks is ", self.marks)
        print("id of self in talk is :", id(self))


print("---------------------------------------------")

s2 = Student2()
s2.talk()

print("---------------------------------------------")
s3 = Student2("ARV", 19, 100)
s3.talk()
