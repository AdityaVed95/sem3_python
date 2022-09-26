class Sample:
    # class variable:
    x = 10
    self.y = 20

    # constructor which is an instance method
    def __init__(self):
        self.y = 20  # instance variable

    # instance method
    def modify(self):
        self.y = self.y + self.x

    # instance method
    def display(self):
        print("the value of y is : ", self.y)


s1 = Sample()
s1.display()
s1.modify()
s1.display()

print("the value of y is :", s1.y)
print("the class variable is :", s1.x)

# note :
# instance method can access class variables but at the class level , we cannot have access to
# instance variables
