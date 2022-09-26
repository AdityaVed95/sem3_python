class Square:
    def area(self, length):
        print("Area of square is :", length * length)


class Circle(Square):
    def area(self, radius):
        print("Area of circle is : ", (22 / 7) * radius * radius)


c1 = Circle()
c1.area(7)

s1 = Square()
s1.area(7)

# if the name of the method in the subclass is the same as the name of the method in the super
# class then the subclass method will override over the super class method

# same area method is performing two different tasks depending upon the type of object
# thus this is an implementation of polymorphism
