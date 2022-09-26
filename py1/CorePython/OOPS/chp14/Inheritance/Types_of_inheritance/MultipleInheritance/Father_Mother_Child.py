class Father:
    def height(self):
        print("Height is 6 foot")


class Mother:
    def color(self):
        print("Color is White")


class Child(Father, Mother):
    def __init__(self):
        print("Hello child")


c = Child()
c.height()
c.color()
c.__init__()  # will call the constructor of the child class and initialise the varaibles for the second time

