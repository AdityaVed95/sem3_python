from sq import Square


# lens is length
# wids is width

class Rectangle(Square):

    def __init__(self, lens, wids):
        super().__init__(lens)
        self.width = wids

    def calculate_and_print(self):
        super().calculate_and_print()  # calling the method in the super class which has the same
        # name as this method inside the subclass

        print("Area of Rectangle is : ", (self.length * self.width))


rec1 = Rectangle(10, 20)
rec1.calculate_and_print()
