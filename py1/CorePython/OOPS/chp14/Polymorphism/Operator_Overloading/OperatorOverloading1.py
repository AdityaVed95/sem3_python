# program to overload the addition operator and to make it act on objects

class Book1:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    # here self.pages are the number of pages of Book1 class ka object
    # here other.pages are the number of pages of other class (here it is Book2 class) ka object

    # so when we directly compare objects , we are actually comparing some property of those objects

    def __gt__(self, other):
        return self.pages > other.pages


class Book2:
    def __init__(self, pages):
        self.pages = pages


b1 = Book1(100)
b2 = Book2(200)

print(b1.pages + b2.pages)
print(b1 + b2)
print(b1.__add__(b2))

if b1 > b2:
    print("b1 has more pages")
else:
    print("b2 has more pages")
