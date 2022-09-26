from father import Father


# how to access the methods of the superclass is the subclass has the methods with the same name as
# that of the super class , how to handle method overriding ?


# super class = base class
# subclass = derived class
# Son is the subclass of the Father class

# subclass has an access to all the members(all types of variables and methods) of the super class


class Son(Father):
    def __init__(self, property1=0, property=0):
        super().__init__(property)  # we have to pass arguments to the super.__init__() if
        # the constructor of the super class is accepting arguments

        # IN the above step the constructor of the super class is called to
        # initialise the instance variable of the super class
        # which can be used in the subclass
        self.son_property = property1  # sons property

        # the following 2 are the instance variable initialised in the constructor
        # of the Father class
        print(self.father_age)
        print(self.father_property)

        # self.son_property is subclass ka instance variable
        # self.father_property is superclass ka instance variable

    def display_property(self):
        print("Total Son's property is : ", self.son_property + self.father_property)
        print("Age of Father is : " + self.father_age)


s = Son(100, 1000)
s.display_property()
