from square import Square


class Rectangle(Square):
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
        super.__init__(x2)

    def area(self):
        area = self.x2 * self.y2
        print("Area is : ", area)
