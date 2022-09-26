# instance variables example :

class Sample:

    # constructor :
    def __init__(self):
        self.x = 10  # instance variable

    # instance method :
    def modify(self):
        self.x = self.x + 1  # self.x  :  way to access the instance variable inside the class


s1 = Sample()
s2 = Sample()

# s1.x or s2.x    :  way to access the instance variable outside the class
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)

s1.modify()
print("x in s1 = ", s1.x)
print("x in s2 = ", s2.x)
